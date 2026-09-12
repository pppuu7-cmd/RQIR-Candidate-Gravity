#!/usr/bin/env python3
"""Iter037 / G47-A: prospective RCG-002 adversarial search against the calibrated explicit 3-state hidden-classical switching family."""
import argparse, json, sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.stats import qmc

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I4, Z, td
from iter013_global_search_calibration import CASES, GAP_THRESHOLD, RECOVERY_TOL
from iter035_g47p_three_state_classical_switching_provenance import product_states, apply_map
from iter036_g47c_three_state_switching_calibration import (
    TIMES, LO, HI, N_START, N_REFINE, MAX_NFEV, METHODS, superops, provenance
)

ZZ=np.kron(Z,Z)
PROBES=product_states()


def target_superops(theta):
    out=[]
    for t in TIMES:
        a=float(theta*t)
        U=np.cos(a)*I4-1j*np.sin(a)*ZZ
        out.append(np.kron(U.conj(),U))
    return out


def residual(x,target):
    pred=superops(x,TIMES)
    arr=[]
    for E,T in zip(pred,target):
        d=E-T
        arr.extend(d.real.reshape(-1))
        arr.extend(d.imag.reshape(-1))
    return np.asarray(arr,float)


def metric(x,target):
    pred=superops(x,TIMES)
    gaps=[]
    for E,T in zip(pred,target):
        for rho in PROBES:
            gaps.append(td(apply_map(E,rho),apply_map(T,rho)))
    return float(max(gaps)),float(np.linalg.norm(residual(x,target)))


def starts(method,shard):
    seed=19000+100*shard+(0 if method=='sobol_lsq' else 17)
    if method=='sobol_lsq':
        u=qmc.Sobol(d=12,scramble=True,seed=seed).random_base2(4)
    else:
        u=qmc.LatinHypercube(d=12,seed=seed).random(N_START)
    return LO+(HI-LO)*u


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--method',choices=METHODS,required=True)
    ap.add_argument('--shard',type=int,choices=range(4),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    scale,t0=CASES[a.shard]
    theta=float(scale*t0)
    target=target_superops(theta)
    scored=[]
    for x0 in starts(a.method,a.shard):
        r=residual(x0,target)
        scored.append((float(np.dot(r,r)),np.asarray(x0,float)))
    scored.sort(key=lambda z:z[0])
    cands=[]
    for _,x0 in scored[:N_REFINE]:
        fit=least_squares(lambda x:residual(x,target),x0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-9,xtol=1e-9,gtol=1e-9)
        gap,rn=metric(fit.x,target)
        prov,pdiag=provenance(fit.x)
        cands.append({'gap':gap,'residual_norm':rn,'parameters':fit.x.tolist(),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success),'provenance_valid':prov,'provenance':pdiag})
    best=min(cands,key=lambda c:(c['gap'],c['residual_norm']))
    vals=[v for c in cands for v in (c['gap'],c['residual_norm'],*c['parameters'])]
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)))
    admissible=bool(structural and best['provenance_valid'])
    lane_support=bool(admissible and best['gap']>GAP_THRESHOLD)
    out={'iteration':'Iter037','gate':'G47-A','method':a.method,'shard':a.shard,'theta':theta,'best_candidate':best,'n_refined_candidates':len(cands),'structural_valid':structural,'admissible':admissible,'lane_support':lane_support,'frozen':{'family_dimension':12,'rate_bounds':[float(LO[0]),float(HI[0])],'field_scale_bounds':[float(LO[6]),float(HI[6])],'times':list(TIMES),'n_product_probes':len(PROBES),'n_starts':N_START,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':RECOVERY_TOL,'same_family_bounds_QMC_and_optimizer_as_G47C':True,'same_RCG002_target_convention_as_G44A':True},'authorization_lock':'Production permitted only after terminal G47-C optimizer calibration PASS.','scope_lock':'Finite explicit 12D stationary three-state hidden-classical switching/product-unitary family only; not arbitrary classical memory or all-classical no-go.','interpretation':'Prospective scoped adversarial toy-trajectory search only.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)

if __name__=='__main__': main()
