#!/usr/bin/env python3
"""Iter019B / G37-A: prospective RCG-002 adversarial search against the
G37-C calibrated combined finite Markovian classical comparator.

The combined family is exactly the G37-C family: K=2 additive independent
single-axis measurement-feedback GKSL plus one shared Gaussian classical
Hamiltonian-noise process. Optimizer construction and bounds are imported
unchanged from G37-C. No post-calibration retuning is allowed.
"""
import argparse, json, sys
from pathlib import Path
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES, GAP_THRESHOLD, RECOVERY_TOL
from iter011_robustness_suite import target
from iter019a_g37c_combined_comparator_calibration import METHODS, optimize

AGREEMENT_TOL=RECOVERY_TOL


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); scale,t0=CASES[a.shard]; theta=float(scale*t0); tar=target(theta)
    gap,rn,nfev,ok=optimize(a.method,a.shard,theta,tar)
    valid=bool(np.isfinite(gap) and np.isfinite(rn))
    out={
      'iteration':'Iter019B','gate':'G37-A','method':a.method,'shard':a.shard,'theta':theta,
      'result':{'best_trace_gap':float(gap),'best_residual_norm':float(rn),'best_nfev':int(nfev),'optimizer_success_flag':bool(ok),'local_nonzero_support':bool(valid and gap>GAP_THRESHOLD)},
      'structural_valid':valid,
      'frozen_thresholds':{'adversarial_nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':AGREEMENT_TOL,'nesting_slack':RECOVERY_TOL},
      'optimizer_authority':'Exact G37-C 18-dimensional combined-family Sobol/LHS + bounded least-squares construction; no post-calibration retuning.',
      'scope_lock':'K=2 additive independent single-axis measurement-feedback GKSL plus one shared Gaussian classical Hamiltonian-noise process.'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not valid: raise SystemExit(2)

if __name__=='__main__': main()
