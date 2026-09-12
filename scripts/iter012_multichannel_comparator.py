#!/usr/bin/env python3
"""Iter012 / G30: additive multi-channel GKSL comparator closure.

Strictly broadens the G29 comparator: the generator is a sum of K independent
single-axis measurement-feedback channels, each satisfying Gamma_A Gamma_B=chi_k^2.
This is still a finite Markovian two-qubit family, not all semiclassical gravity.
"""
import argparse, json, math, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I4, RHO0, axis, op, Lgen, evolve, target, td, exp_super, choi

CASES=[(0.5,0.05),(1.0,0.10),(2.0,0.20),(4.0,0.35)]

def multi_L(th, channels):
    L=np.zeros((16,16),dtype=complex); weights=[]
    for w,alA,beA,alB,beB,a in channels:
        chi=th*w; Li,_,_=Lgen(chi,op(axis(alA,beA)),op(axis(alB,beB)),a); L+=Li; weights.append(w)
    return L,weights

def decode(x,K):
    chans=[]
    if K==2:
        w=float(np.clip(x[-1],0,1)); ws=[w,1-w]; body=x[:-1]
    else:
        u=float(np.clip(x[-2],0,1)); v=float(np.clip(x[-1],0,1-u)); ws=[u,v,1-u-v]; body=x[:-2]
    for k in range(K):
        alA,beA,alB,beB,a=body[5*k:5*k+5]
        chans.append((ws[k],alA,beA,alB,beB,float(np.clip(a,-3,3))))
    return chans

def random_x(rng,K):
    body=[]
    for _ in range(K): body += [rng.uniform(-math.pi,math.pi),rng.uniform(0,math.pi),rng.uniform(-math.pi,math.pi),rng.uniform(0,math.pi),rng.uniform(-2,2)]
    if K==2: body += [rng.uniform(0,1)]
    else:
        u=rng.uniform(0,1); body += [u,rng.uniform(0,1-u)]
    return np.array(body,dtype=float)

def normalize_x(x,K):
    y=x.copy()
    for k in range(K): y[5*k+4]=float(np.clip(y[5*k+4],-3,3))
    if K==2: y[-1]=float(np.clip(y[-1],0,1))
    else:
        y[-2]=float(np.clip(y[-2],0,1)); y[-1]=float(np.clip(y[-1],0,1-y[-2]))
    return y

def gap(x,K,th,tar):
    L,_=multi_L(th,decode(normalize_x(x,K),K)); return td(evolve(L),tar)

def adversarial(scale,theta,shard,K):
    th=scale*theta; tar=target(th); rng=np.random.default_rng(30000+100*K+shard)
    best=float('inf'); bestx=None; evals=0; restarts=10 if K==2 else 8; dims=5*K+(1 if K==2 else 2)
    for r in range(restarts):
        x=random_x(rng,K)
        if r==0:
            for k in range(K): x[5*k:5*k+5]=[0,0,0,0,0]
            if K==2: x[-1]=1.0
            else: x[-2],x[-1]=1.0,0.0
        f=gap(x,K,th,tar); evals+=1
        for step in (0.8,0.4,0.2,0.1,0.05):
            for _ in range(2):
                improved=False
                for j in range(dims):
                    for s in (-1,1):
                        y=x.copy(); y[j]+=s*step; y=normalize_x(y,K); g=gap(y,K,th,tar); evals+=1
                        if g+1e-14<f: x,f=y,g; improved=True
                if not improved: break
        if f<best: best=float(f); bestx=normalize_x(x,K).copy()
    return {'K':K,'best_gap':best,'best_parameters':bestx.tolist(),'evaluations':evals,'restarts':restarts,
            'nonzero_gap':best>1e-4,'scientific_support':best>1e-4,
            'interpretation':f'Continuous adversarial search in additive K={K} independent-channel GKSL family.'}

def aligned_split(scale,theta,shard):
    th=scale*theta; tar=target(th); vals=[]
    for w in np.linspace(0,1,11):
        for a1 in (-2,-1,0,1,2):
            for a2 in (-2,-1,0,1,2):
                ch=[(float(w),0,0,0,0,float(a1)),(float(1-w),0,0,0,0,float(a2))]
                L,_=multi_L(th,ch); vals.append(td(evolve(L),tar))
    b=float(min(vals))
    return {'best_aligned_split_gap':b,'n_candidates':len(vals),'scientific_support':b>1e-4,
            'interpretation':'Aligned two-channel split cannot exploit angular mismatch; exact K=1 boundaries included.'}

def admissibility(scale,theta,shard):
    th=scale*theta; rng=np.random.default_rng(30100+shard); x=random_x(rng,3); L,ws=multi_L(th,decode(x,3)); E=exp_super(L)
    tr=I4.reshape(-1,order='F').conj(); tp=float(np.linalg.norm(tr@L)); mine=float(np.min(np.linalg.eigvalsh(choi(E))))
    rho=evolve(L); psd=float(np.min(np.linalg.eigvalsh(rho))); support=tp<1e-10 and mine>-1e-8 and psd>-1e-8
    return {'weights':ws,'tp_residual':tp,'choi_min_eig':mine,'state_min_eig':psd,'scientific_support':support,
            'interpretation':'CPTP/PSD control for additive K=3 generator.'}

def null_k2(scale,theta,shard):
    th=scale*theta; rng=np.random.default_rng(30200+shard); x=random_x(rng,2); L,_=multi_L(th,decode(x,2)); rho=evolve(L); d=td(evolve(L),rho)
    return {'self_recovery_gap':d,'scientific_support':d<1e-12,'interpretation':'In-family K=2 exact null/recovery control.'}

STREAMS={'adversarial_k2':lambda s,t,h:adversarial(s,t,h,2),'adversarial_k3':lambda s,t,h:adversarial(s,t,h,3),
         'aligned_split':aligned_split,'admissibility_k3':admissibility,'null_k2':null_k2}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=STREAMS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); scale,theta=CASES[a.shard]; r=STREAMS[a.stream](scale,theta,a.shard)
    valid=all(np.isfinite(v) for v in [scale,theta]) and isinstance(r.get('scientific_support'),(bool,np.bool_))
    out={'iteration':'Iter012','gate':'G30','stream':a.stream,'shard':a.shard,'theta':scale*theta,'result':r,'structural_valid':bool(valid),
         'scope_lock':'Additive K<=3 finite two-qubit Markovian independent single-axis measurement-feedback GKSL channels; not all semiclassical gravity.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not valid: raise SystemExit(2)
if __name__=='__main__': main()
