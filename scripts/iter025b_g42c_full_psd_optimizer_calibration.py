#!/usr/bin/env python3
"""Iter025B / G42-C: positive-control optimizer calibration for the full
21-parameter real-PSD classical Kossakowski family. No RCG-002 target.
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
from iter024a_g41p_high_rank_classical_kossakowski import map_apply
from iter025a_g42j_full_psd_kossakowski_identifiability import TIMES,LOWER,hidden_z,koss,generator_from_C

METHODS=('sobol_lsq','lhs_lsq'); N_START=32; N_REFINE=6; MAX_NFEV=1000; RECOVERY_TOL=0.002
LO=np.array([-2.0 if i==j else -0.12 for i,j in LOWER],float)
HI=np.array([-0.5 if i==j else 0.12 for i,j in LOWER],float)


def trajectory(z):
    G=generator_from_C(koss(z)); out=[]
    for t in TIMES:
        E=expm(G*float(t)); out.append([map_apply(E,rho) for rho in PROBES])
    return out


def residual(z,target):
    pred=trajectory(z); arr=[]
    for aa,bb in zip(pred,target):
        for x,y in zip(aa,bb):
            d=x-y; arr.extend(d.real.reshape(-1)); arr.extend(d.imag.reshape(-1))
    return np.asarray(arr,float)


def metric(z,target):
    pred=trajectory(z); gaps=[td(x,y) for aa,bb in zip(pred,target) for x,y in zip(aa,bb)]
    rr=residual(z,target); return float(max(gaps)),float(np.linalg.norm(rr))


def starts(method,shard):
    seed=96000+100*shard+(0 if method=='sobol_lsq' else 37)
    if method=='sobol_lsq': u=qmc.Sobol(d=21,scramble=True,seed=seed).random_base2(5)
    else: u=qmc.LatinHypercube(d=21,seed=seed).random(N_START)
    return LO+u*(HI-LO)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    hidden=hidden_z(a.shard); target=trajectory(hidden); scored=[]
    for z0 in starts(a.method,a.shard):
        r=residual(z0,target); scored.append((float(np.dot(r,r)),np.asarray(z0,float)))
    scored.sort(key=lambda q:q[0]); cands=[]
    for _,z0 in scored[:N_REFINE]:
        fit=least_squares(lambda z:residual(z,target),z0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-10,xtol=1e-10,gtol=1e-10)
        gap,rn=metric(fit.x,target); ce=np.linalg.eigvalsh(koss(fit.x))
        cands.append({'gap':gap,'residual_norm':rn,'min_kossakowski_eigenvalue':float(ce.min()),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success)})
    best=min(cands,key=lambda c:(c['gap'],c['residual_norm']))
    vals=[x for c in cands for x in (c['gap'],c['residual_norm'],c['min_kossakowski_eigenvalue'])]
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)))
    support=bool(structural and best['gap']<RECOVERY_TOL and best['min_kossakowski_eigenvalue']>0)
    out={'iteration':'Iter025B','gate':'G42-C','method':a.method,'shard':a.shard,
         'best_candidate':best,'n_refined_candidates':len(cands),'structural_valid':structural,'scientific_support':support,
         'frozen':{'n_parameters':21,'diag_log_bounds':[-2.0,-0.5],'offdiag_bounds':[-0.12,0.12],'times':TIMES.tolist(),'n_probes':len(PROBES),'n_starts':N_START,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'recovery_tolerance':RECOVERY_TOL,'hidden_coordinates_used_as_starts':False,'RCG002_target_used':False},
         'scope_lock':'Full real-PSD 6x6 classical random-Hamiltonian Kossakowski positive-control search in 21 Cholesky coordinates; calibration only.',
         'interpretation':'Positive-control optimizer calibration only.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
