#!/usr/bin/env python3
"""Iter018C / G36-A: prospective RCG-002 adversarial search against the
G36-C calibrated shared-classical-noise comparator.

Frozen after terminal G36-C and before any G36-A result inspection.
The optimizer construction is imported unchanged from G36-C. Scientific support
requires a nonzero trace-distance gap >1e-4 for both independently calibrated
Sobol/LHS constructions and aggregate cross-method agreement <=2e-3 per shard.

Scope is deliberately narrow: one shared Gaussian classical scalar process
coupled to two local Pauli axes, represented as a convex mixture of product
unitaries. This is not a theorem about all classical or semiclassical mediators.
"""
import argparse, json, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES, GAP_THRESHOLD, RECOVERY_TOL
from iter011_robustness_suite import target
from iter018b_g36c_shared_noise_optimizer_calibration import METHODS, optimize

AGREEMENT_TOL = RECOVERY_TOL


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--method',choices=METHODS,required=True)
    ap.add_argument('--shard',type=int,choices=range(4),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    scale,theta0=CASES[a.shard]; theta=float(scale*theta0)
    tar=target(theta)
    gap,xhat,nfev,resnorm=optimize(a.method,a.shard,tar)
    valid=bool(np.isfinite(gap) and np.all(np.isfinite(xhat)) and np.isfinite(resnorm))
    local=bool(valid and gap>GAP_THRESHOLD)
    out={
      'iteration':'Iter018C','gate':'G36-A','method':a.method,'shard':a.shard,'theta':theta,
      'result':{'best_trace_gap':float(gap),'local_nonzero_support':local,'nfev':int(nfev),'residual_norm':float(resnorm)},
      'structural_valid':valid,
      'frozen_thresholds':{'adversarial_nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':AGREEMENT_TOL},
      'optimizer_authority':'Exact G36-C shared-noise Sobol/LHS + bounded least-squares construction; no post-calibration retuning.',
      'interpretation':'Prospective RCG-002 nearest-comparator search in the calibrated finite shared-classical-noise family. Aggregate two-method agreement is additionally required.',
      'scope_lock':'One shared Gaussian classical Hamiltonian-noise process coupled to two local Pauli axes; convex mixture of product unitaries only.'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not valid: raise SystemExit(2)

if __name__=='__main__': main()
