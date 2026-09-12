#!/usr/bin/env python3
"""Iter019D / G37-A2: prospective RCG-002 adversarial search against the
G37-C2-calibrated truly nested combined finite Markovian classical comparator.

Family and optimizer are imported unchanged from terminal G37-C2. The family
contains both calibrated parents exactly: lambda_MF=0 gives shared-noise-only;
cA=cB=0 gives K=2 measurement-feedback-only. The aggregate therefore applies a
valid frozen nesting sanity check against the better exact parent minimum.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES,GAP_THRESHOLD,RECOVERY_TOL
from iter011_robustness_suite import target
from iter019c_g37c2_nested_combined_calibration import METHODS,optimize


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    scale,t0=CASES[a.shard]; theta=float(scale*t0); tar=target(theta)
    gap,rn,nfev,ok=optimize(a.method,a.shard,theta,tar)
    valid=bool(np.isfinite(gap) and np.isfinite(rn))
    out={'iteration':'Iter019D','gate':'G37-A2','method':a.method,'shard':a.shard,'theta':theta,'result':{'best_trace_gap':float(gap),'residual_norm':float(rn),'nfev':int(nfev),'optimizer_success_flag':bool(ok),'local_nonzero_support':bool(valid and gap>GAP_THRESHOLD)},'structural_valid':valid,'frozen_thresholds':{'adversarial_nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':RECOVERY_TOL,'nesting_slack':RECOVERY_TOL},'optimizer_authority':'Exact terminal G37-C2 19-dimensional Sobol/LHS + bounded least-squares construction, unchanged after calibration.','scope_lock':'Truly nested finite Markovian family: lambda_MF-scaled K2 single-axis measurement-feedback plus one shared Gaussian classical Hamiltonian-noise process.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not valid: raise SystemExit(2)
if __name__=='__main__': main()
