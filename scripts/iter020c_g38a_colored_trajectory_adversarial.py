#!/usr/bin/env python3
"""Iter020C / G38-A: prospective three-time RCG-002 toy-trajectory adversarial
search against the G38-C-calibrated OU colored classical-noise trajectory family.

Frozen target convention: for each base RCG-002 shard angle theta, the toy
trajectory is target(theta*T) at T=[0.25,0.5,1.0]. This is only the existing
controlled-phase toy-channel parameter scaled linearly with toy evolution time;
it is NOT asserted to be the full gravity-time dynamics of any continuum theory.

Optimizer family/construction is imported unchanged from terminal G38-C.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES,GAP_THRESHOLD,RECOVERY_TOL
from iter011_robustness_suite import target
from iter020b_g38c_colored_trajectory_calibration import METHODS,TIMES,optimize

AGREEMENT_TOL=RECOVERY_TOL


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    scale,t0=CASES[a.shard]; theta=float(scale*t0)
    tars=[target(theta*float(T)) for T in TIMES]
    maxgap,gaps,rn,nfev=optimize(a.method,a.shard,tars)
    valid=bool(np.isfinite(maxgap) and np.all(np.isfinite(gaps)) and np.isfinite(rn))
    out={'iteration':'Iter020C','gate':'G38-A','method':a.method,'shard':a.shard,'theta':theta,'times':TIMES.tolist(),'result':{'per_time_trace_gaps':[float(x) for x in gaps],'max_trace_gap':float(maxgap),'residual_norm':float(rn),'nfev':int(nfev),'local_trajectory_nonzero_support':bool(valid and maxgap>GAP_THRESHOLD)},'structural_valid':valid,'frozen_thresholds':{'trajectory_nonzero_max_gap':GAP_THRESHOLD,'cross_method_per_time_agreement':AGREEMENT_TOL},'target_convention':'Toy RCG-002 trajectory target(theta*T) at T=[0.25,0.5,1.0]; linear toy-time angle scaling only, not continuum gravity-time dynamics.','optimizer_authority':'Exact terminal G38-C OU trajectory Sobol/LHS + bounded least-squares construction; no post-calibration retuning.','scope_lock':'Stationary OU finite-correlation scalar classical noise with one fixed local-sum coupling; three-time trajectory only.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not valid: raise SystemExit(2)
if __name__=='__main__': main()
