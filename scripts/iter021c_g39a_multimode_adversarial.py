#!/usr/bin/env python3
"""Iter021C / G39-A: prospective RCG-002 adversarial search against the
G39-C-calibrated finite rank-2/rank-3 multimode shared-classical-noise family.

Rank 3 contains rank 2 exactly through a zero third-mode rate. Optimizer
construction and parameter bounds are imported unchanged from terminal G39-C.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES,GAP_THRESHOLD,RECOVERY_TOL
from iter011_robustness_suite import target
from iter021b_g39c_multimode_optimizer_calibration import METHODS,optimize


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--rank',type=int,choices=[2,3],required=True); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    scale,t0=CASES[a.shard]; theta=float(scale*t0); tar=target(theta)
    gap,rn,nfev,ok=optimize(a.method,a.rank,a.shard,tar)
    valid=bool(np.isfinite(gap) and np.isfinite(rn))
    out={'iteration':'Iter021C','gate':'G39-A','rank':a.rank,'method':a.method,'shard':a.shard,'theta':theta,'result':{'best_trace_gap':float(gap),'residual_norm':float(rn),'nfev':int(nfev),'optimizer_success_flag':bool(ok),'local_nonzero_support':bool(valid and gap>GAP_THRESHOLD)},'structural_valid':valid,'frozen_thresholds':{'adversarial_nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':RECOVERY_TOL,'rank3_vs_rank2_nesting_slack':RECOVERY_TOL},'optimizer_authority':'Exact terminal G39-C rank-specific Sobol/LHS + bounded least-squares construction; no post-calibration retuning.','scope_lock':'Finite rank-2/rank-3 multimode shared classical white-noise positive-rate family with arbitrary local Pauli axes.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not valid: raise SystemExit(2)
if __name__=='__main__': main()
