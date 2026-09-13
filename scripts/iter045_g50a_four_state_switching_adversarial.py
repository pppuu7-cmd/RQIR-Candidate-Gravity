#!/usr/bin/env python3
"""Iter045/G50-A: preregistered RCG-002 adversarial transport against exact calibrated 20D four-state hidden-classical switching family."""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.stats import qmc
sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I4,Z,td
from iter013_global_search_calibration import CASES,GAP_THRESHOLD
from iter043_g50p_four_state_classical_switching_provenance import product_states,apply_map
from iter044_g50c_four_state_switching_calibration import (
    TIMES,HOLDOUT,LO,HI,N_START,N_REFINE,MAX_NFEV,METHODS,superops,provenance
)

ZZ=np.kron(Z,Z)
PROBES=product_states()


def target_superops(theta,times):
    out=[]
    for t in times:
        a=float(theta*t)
        U=np.cos(a)*I4-1j*np.sin(a)*ZZ
        out.append(np.kron(U.conj(),U))
    return out


def residual(x,target):
    arr=[]
    for E,T in zip(superops(x,TIMES),target):
        d=E-T
        arr.extend(d.real.reshape(-1)); arr.extend(d.imag.reshape(-1))
    return np.asarray(arr,float)


def max_probe_gap(x,target,times):
    g=0.0
    for E,T in zip(superops(x,times),target):
        for rho in PROBES:
            g=max(g,td(apply_map(E,rho),apply_map(T,rho)))
    return float(g)


def starts(method,shard):
    seed=26000+100*shard+(0 if method=='sobol_lsq' else 17)
    if method=='sobol_lsq':
        u=qmc.Sobol(d=20,scramble=True,seed=seed).random_base2(5)
    else:
        u=qmc.LatinHypercube(d=20,seed=seed).random(N_START)
    return LO+(HI-LO)*u


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--method',choices=METHODS,required=True)
    ap.add_argument('--shard',type=int,choices=range(4),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    scale,t0=CASES[a.shard]
    theta=float(scale*t0)
    target_train=target_superops(theta,TIMES)
    target_hold=target_superops(theta,HOLDOUT)
    scored=[]
    for x0 in starts(a.method,a.shard):
        r=residual(x0,target_train)
        scored.append((float(r@r),np.asarray(x0,float)))
    scored.sort(key=lambda z:z[0])
    cands=[]
    for _,x0 in scored[:N_REFINE]:
        fit=least_squares(lambda x:residual(x,target_train),x0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-9,xtol=1e-9,gtol=1e-9)
        train=max_probe_gap(fit.x,target_train,TIMES)
        hold=max_probe_gap(fit.x,target_hold,HOLDOUT)
        rn=float(np.linalg.norm(residual(fit.x,target_train)))
        prov,pdiag=provenance(fit.x)
        cands.append({'train_max_trace_gap':train,'holdout_max_trace_gap':hold,'residual_norm':rn,'parameters':fit.x.tolist(),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success),'provenance_valid':prov,'provenance':pdiag})
    best=min(cands,key=lambda c:(c['train_max_trace_gap'],c['holdout_max_trace_gap'],c['residual_norm']))
    vals=[v for c in cands for v in (c['train_max_trace_gap'],c['holdout_max_trace_gap'],c['residual_norm'],*c['parameters'])]
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)))
    admissible=bool(structural and best['provenance_valid'])
    lane_support=bool(admissible and best['train_max_trace_gap']>GAP_THRESHOLD and best['holdout_max_trace_gap']>GAP_THRESHOLD)
    out={
        'iteration':'Iter045','gate':'G50-A','method':a.method,'shard':a.shard,'theta':theta,
        'best_candidate':best,'n_refined_candidates':len(cands),'structural_valid':structural,'admissible':admissible,'lane_support':lane_support,
        'classification':'FOUR_STATE_CLASSICAL_SWITCHING_ADVERSARIAL_LANE_SUPPORT' if lane_support else ('G50A_LANE_BLOCKED_ADMISSIBILITY' if structural and not admissible else 'G50A_LANE_SUPPORT_RULE_NOT_MET'),
        'frozen':{
            'family_dimension':20,'times':list(TIMES),'holdout_times':list(HOLDOUT),'n_product_probes':len(PROBES),'n_starts':N_START,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,
            'nonzero_gap_threshold_train':GAP_THRESHOLD,'nonzero_gap_threshold_holdout':GAP_THRESHOLD,
            'cross_method_train_agreement':0.002,'cross_method_holdout_agreement':0.003,
            'same_family_bounds_and_provenance_as_G50C':True,'same_RCG002_target_convention_as_prior_adversarial_gates':True
        },
        'authorization_lock':'Production permitted only after terminal G50-C optimizer calibration PASS.',
        'scope_lock':'Finite bounded stationary 20D four-state hidden-classical CTMC switching/local-sum-Hamiltonian family only; not arbitrary classical memory or all-classical no-go.',
        'interpretation':'Prospective scoped adversarial RCG-002 transport with independent training and held-out time checks.'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)

if __name__=='__main__': main()
