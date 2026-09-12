#!/usr/bin/env python3
"""Iter024B / G41-C: positive-control optimizer calibration for the
positive-rate subfamily on frozen rank-4/5/6 classical Kossakowski frames.
No RCG-002 target is used.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
from scipy.stats import qmc

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import td
from iter022b_g40c_rtn_optimizer_calibration import PROBES
from iter024a_g41p_high_rank_classical_kossakowski import construction,dsuper,map_apply

METHODS=('sobol_lsq','lhs_lsq'); TIMES=np.array([0.2,0.7,1.3],float)
LO=0.02; HI=0.25; N_START=16; N_REFINE=4; MAX_NFEV=400; RECOVERY_TOL=0.002


def generator(Fs,rates):
    return sum(float(k)*dsuper(F) for k,F in zip(rates,Fs))


def trajectory(Fs,rates):
    L=generator(Fs,rates); out=[]
    for t in TIMES:
        E=expm(L*float(t)); out.append([map_apply(E,rho) for rho in PROBES])
    return out


def residual_rates(rates,target):
    pred=trajectory(FS,rates); arr=[]
    for aa,bb in zip(pred,target):
        for x,y in zip(aa,bb):
            d=x-y; arr.extend(d.real.reshape(-1)); arr.extend(d.imag.reshape(-1))
    return np.asarray(arr,float)


def metric_rates(rates,target):
    pred=trajectory(FS,rates); gaps=[td(x,y) for aa,bb in zip(pred,target) for x,y in zip(aa,bb)]
    rr=residual_rates(rates,target)
    return float(max(gaps)),float(np.linalg.norm(rr))


def starts(method,rank,shard):
    seed=81000+1000*rank+100*shard+(0 if method=='sobol_lsq' else 41)
    if method=='sobol_lsq':
        u=qmc.Sobol(d=rank,scramble=True,seed=seed).random_base2(4)
    else:
        u=qmc.LatinHypercube(d=rank,seed=seed).random(N_START)
    return LO+u*(HI-LO)


def main():
    global FS
    ap=argparse.ArgumentParser(); ap.add_argument('--rank',type=int,choices=(4,5,6),required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    V,hidden,FS,C,L=construction(a.rank,a.shard); target=trajectory(FS,hidden)
    scored=[]
    for x0 in starts(a.method,a.rank,a.shard):
        r=residual_rates(x0,target); scored.append((float(np.dot(r,r)),x0))
    scored.sort(key=lambda z:z[0]); cands=[]
    for _,x0 in scored[:N_REFINE]:
        fit=least_squares(lambda x:residual_rates(x,target),x0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-11,xtol=1e-11,gtol=1e-11)
        gap,rn=metric_rates(fit.x,target)
        cands.append({'gap':gap,'residual_norm':rn,'rates':fit.x.tolist(),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success)})
    best=min(cands,key=lambda c:(c['gap'],c['residual_norm']))
    vals=[z for c in cands for z in [c['gap'],c['residual_norm'],*c['rates']]]
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)))
    support=bool(structural and best['gap']<RECOVERY_TOL)
    out={'iteration':'Iter024B','gate':'G41-C','rank':a.rank,'shard':a.shard,'method':a.method,
         'hidden_rates':hidden.tolist(),'best_candidate':best,'n_refined_candidates':len(cands),
         'structural_valid':structural,'scientific_support':support,
         'frozen':{'rate_bounds':[LO,HI],'times':TIMES.tolist(),'n_probes':len(PROBES),'n_starts':N_START,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'recovery_tolerance':RECOVERY_TOL,'hidden_coordinates_used_as_starts':False,'RCG002_target_used':False},
         'scope_lock':'Positive-rate search only on deterministic G41-P rank-4/5/6 mode frames; not arbitrary PSD Kossakowski orientations.',
         'interpretation':'Positive-control optimizer calibration only.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
