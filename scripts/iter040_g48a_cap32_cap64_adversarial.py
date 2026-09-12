#!/usr/bin/env python3
"""Iter040/G48-A: frozen cap32/cap64 adversarial transport after terminal G48-C calibration."""
import argparse,json
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from iter038_g46a_extended_trace_ball_adversarial import (
    METHODS,CASES,GAP_THRESHOLD,RECOVERY_TOL,N_REFINE,MAX_NFEV,LO,HI,
    target_traj,starts,residual,metric,admissibility
)

CAPS=(32.0,64.0)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--cap',type=float,choices=CAPS,required=True)
    ap.add_argument('--method',choices=METHODS,required=True)
    ap.add_argument('--shard',type=int,choices=range(4),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    scale,t0=CASES[a.shard]; theta=float(scale*t0); target=target_traj(theta)
    scored=[]
    for z0 in starts(a.method,a.shard,a.cap):
        rr=residual(z0,target,a.cap); scored.append((float(np.dot(rr,rr)),np.asarray(z0,float)))
    scored.sort(key=lambda q:q[0]); cands=[]
    for _,z0 in scored[:N_REFINE]:
        fit=least_squares(lambda z:residual(z,target,a.cap),z0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-10,xtol=1e-10,gtol=1e-10)
        gap,rn=metric(fit.x,target,a.cap)
        cands.append({'gap':gap,'residual_norm':rn,'search_coordinates':fit.x.tolist(),'search_z_norm':float(np.linalg.norm(fit.x)),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success)})
    best=min(cands,key=lambda c:(c['gap'],c['residual_norm']))
    z=np.asarray(best['search_coordinates'],float); adm=admissibility(z,a.cap)
    vals=[x for c in cands for x in (c['gap'],c['residual_norm'],c['search_z_norm'],*c['search_coordinates'])]+list(adm.values())
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)))
    admissible=bool(structural and adm['min_kossakowski_eigenvalue']>=-1e-10 and adm['trace_C']<=a.cap+1e-8 and adm['max_tp_residual']<1e-10 and adm['min_choi_eigenvalue']>-1e-8 and adm['min_output_state_eigenvalue']>-1e-8 and adm['max_trace_error']<1e-10)
    lane_support=bool(admissible and best['gap']>GAP_THRESHOLD)
    out={'iteration':'Iter040','gate':'G48-A','trace_cap':a.cap,'method':a.method,'shard':a.shard,'theta':theta,'best_candidate':best,'admissibility':adm,'n_refined_candidates':len(cands),'structural_valid':structural,'admissible':admissible,'lane_support':lane_support,'frozen':{'family':'C=A^2; A symmetric; tr(C)<=cap','caps':list(CAPS),'same_target_family_optimizer_and_thresholds_as_G46A':True,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':RECOVERY_TOL,'nesting_tolerance':0.002},'authorization_lock':'Production permitted only after terminal G48-C calibration PASS.','scope_lock':'Finite basis-invariant real-PSD Markovian trace caps 32/64 only; not unbounded PSD or all-classical no-go.','interpretation':'Prospective scoped adversarial toy-trajectory transport only.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)

if __name__=='__main__': main()
