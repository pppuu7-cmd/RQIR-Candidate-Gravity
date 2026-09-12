#!/usr/bin/env python3
"""Iter026R / G42-R: held-out positive-control replication for the
boundary-capable bounded real-PSD Kossakowski optimizer. No RCG-002 target.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.stats import qmc

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter025c_g42c2_psd_boundary_calibration import METHODS,LOWER,LO,HI,RECOVERY_TOL,C_REL_TOL,RANK_EIG_TOL,pack,cmat,trajectory,residual,diagnostics

RANKS=(1,2,3,4,5,6)
N_START=32; N_REFINE=6; MAX_NFEV=1000


def hidden_q(rank):
    rng=np.random.default_rng(112000+rank)
    B=np.zeros((6,6),float)
    for j in range(rank):
        B[j,j]=0.145+0.031*j+0.007*rank
        for i in range(j+1,6):
            B[i,j]=float(rng.uniform(-0.085,0.085))
    return pack(B)


def starts(method,rank):
    seed=113000+100*rank+(0 if method=='sobol_lsq' else 59)
    if method=='sobol_lsq': u=qmc.Sobol(d=21,scramble=True,seed=seed).random_base2(5)
    else: u=qmc.LatinHypercube(d=21,seed=seed).random(N_START)
    return LO+u*(HI-LO)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--rank',type=int,choices=RANKS,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    hidden=hidden_q(a.rank); C_hidden=cmat(hidden); eig=np.linalg.eigvalsh(C_hidden); hidden_rank=int(np.sum(eig>1e-10)); target=trajectory(hidden)
    scored=[]
    for q0 in starts(a.method,a.rank):
        rr=residual(q0,target); scored.append((float(np.dot(rr,rr)),np.asarray(q0,float)))
    scored.sort(key=lambda z:z[0]); cands=[]
    for _,q0 in scored[:N_REFINE]:
        fit=least_squares(lambda q:residual(q,target),q0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-10,xtol=1e-10,gtol=1e-10)
        gap,rn,crel,rrank,mineig=diagnostics(fit.x,target,C_hidden)
        cands.append({'gap':gap,'residual_norm':rn,'relative_kossakowski_error':crel,'recovered_effective_rank':rrank,'min_kossakowski_eigenvalue':mineig,'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success)})
    best=min(cands,key=lambda c:(c['gap'],c['relative_kossakowski_error'],c['residual_norm']))
    vals=[x for c in cands for x in (c['gap'],c['residual_norm'],c['relative_kossakowski_error'],c['min_kossakowski_eigenvalue'])]
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)) and hidden_rank==a.rank and eig.min()>-1e-12)
    support=bool(structural and best['gap']<RECOVERY_TOL and best['relative_kossakowski_error']<C_REL_TOL and best['recovered_effective_rank']==a.rank and best['min_kossakowski_eigenvalue']>-1e-10)
    out={'iteration':'Iter026R','gate':'G42-R','method':a.method,'intended_hidden_rank':a.rank,'hidden_rank_1e-10':hidden_rank,'hidden_min_kossakowski_eigenvalue':float(eig.min()),'best_candidate':best,'n_refined_candidates':len(cands),'structural_valid':structural,'scientific_support':support,
         'frozen':{'diag_bounds':[0.0,0.60],'offdiag_bounds':[-0.30,0.30],'n_starts':N_START,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'trace_recovery_tolerance':RECOVERY_TOL,'relative_kossakowski_tolerance':C_REL_TOL,'rank_eigenvalue_threshold':RANK_EIG_TOL,'hidden_coordinates_used_as_starts':False,'RCG002_target_used':False},
         'scope_lock':'Held-out optimizer replication across new positive controls ranks 1-6 only; methodology robustness, no comparator claim.',
         'interpretation':'Cannot alter G42-A frozen physics verdict or programme readiness by itself.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
