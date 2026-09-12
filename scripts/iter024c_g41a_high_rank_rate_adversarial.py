#!/usr/bin/env python3
"""Iter024C / G41-A: prospective RCG-002 toy-trajectory adversarial search
against calibrated positive-rate subfamilies on frozen rank-4/5/6 classical
Kossakowski frames.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I4,Z,td
from iter013_global_search_calibration import CASES,GAP_THRESHOLD,RECOVERY_TOL
from iter022b_g40c_rtn_optimizer_calibration import PROBES
from iter024a_g41p_high_rank_classical_kossakowski import construction,dsuper,map_apply
from iter024b_g41c_high_rank_rate_calibration import METHODS,TIMES,LO,HI,N_REFINE,MAX_NFEV,starts

ZZ=np.kron(Z,Z)


def generator(Fs,rates):
    return sum(float(k)*dsuper(F) for k,F in zip(rates,Fs))


def candidate_traj(Fs,rates):
    L=generator(Fs,rates); out=[]
    for t in TIMES:
        E=expm(L*float(t)); out.append([map_apply(E,rho) for rho in PROBES])
    return out


def target_traj(theta):
    out=[]
    for t in TIMES:
        a=float(theta*t); U=np.cos(a)*I4-1j*np.sin(a)*ZZ
        out.append([U@rho@U.conj().T for rho in PROBES])
    return out


def residual(rates,Fs,target):
    pred=candidate_traj(Fs,rates); arr=[]
    for aa,bb in zip(pred,target):
        for x,y in zip(aa,bb):
            d=x-y; arr.extend(d.real.reshape(-1)); arr.extend(d.imag.reshape(-1))
    return np.asarray(arr,float)


def metric(rates,Fs,target):
    pred=candidate_traj(Fs,rates)
    gaps=[td(x,y) for aa,bb in zip(pred,target) for x,y in zip(aa,bb)]
    rr=residual(rates,Fs,target)
    return float(max(gaps)),float(np.linalg.norm(rr))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--rank',type=int,choices=(4,5,6),required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    V,hidden,Fs,C,L=construction(a.rank,a.shard)
    scale,t0=CASES[a.shard]; theta=float(scale*t0); target=target_traj(theta)
    scored=[]
    for x0 in starts(a.method,a.rank,a.shard):
        rr=residual(x0,Fs,target); scored.append((float(np.dot(rr,rr)),np.asarray(x0,float)))
    scored.sort(key=lambda z:z[0]); cands=[]
    for _,x0 in scored[:N_REFINE]:
        fit=least_squares(lambda x:residual(x,Fs,target),x0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-11,xtol=1e-11,gtol=1e-11)
        gap,rn=metric(fit.x,Fs,target)
        cands.append({'gap':gap,'residual_norm':rn,'rates':fit.x.tolist(),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success)})
    best=min(cands,key=lambda c:(c['gap'],c['residual_norm']))
    vals=[x for c in cands for x in (c['gap'],c['residual_norm'],*c['rates'])]
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)))
    lane_support=bool(structural and best['gap']>GAP_THRESHOLD)
    out={'iteration':'Iter024C','gate':'G41-A','rank':a.rank,'shard':a.shard,'method':a.method,'theta':theta,
         'best_candidate':best,'n_refined_candidates':len(cands),'structural_valid':structural,'lane_support':lane_support,
         'frozen':{'rate_bounds':[LO,HI],'times':TIMES.tolist(),'n_probes':len(PROBES),'n_starts':16,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':RECOVERY_TOL,'same_search_as_G41C':True,'cross_rank_nesting_required':False},
         'scope_lock':'Finite positive-rate subfamilies on deterministic rank-4/5/6 classical mode frames; not arbitrary PSD Kossakowski orientations.',
         'interpretation':'Prospective finite-family adversarial toy-trajectory search only.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
