#!/usr/bin/env python3
"""Iter017R / G35-R: independent held-out calibration replication.

Prospectively frozen while G35 K=3/K=4 adversarial lanes are still running.
This gate is method-robustness only and cannot change the G35 physics verdict.

It tests the same Sobol-LSQ/LHS-LSQ construction family on new theta values,
new hidden in-family sources (shards 4..6), and therefore new deterministic
initial-design seeds. Hidden source coordinates are never optimizer starts.
Final acceptance remains trace distance < 2e-3.
"""
import argparse, json, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import RECOVERY_TOL
from iter016_calibrated_multichannel_comparator import METHODS, positive_control

HOLDOUT_THETA = {0:0.055, 1:0.22, 2:0.80}
HOLDOUT_SOURCE_SHARD = {0:4, 1:5, 2:6}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--K',type=int,choices=[2,3,4],required=True)
    ap.add_argument('--method',choices=METHODS,required=True)
    ap.add_argument('--holdout',type=int,choices=[0,1,2],required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    theta=HOLDOUT_THETA[a.holdout]
    source_shard=HOLDOUT_SOURCE_SHARD[a.holdout]
    r=positive_control(a.method,a.K,source_shard,theta)
    # Explicitly relabel: this is an independent held-out replication, not G34 authority.
    r['stream']='heldout_positive_control'
    r['holdout_id']=a.holdout
    r['source_shard']=source_shard
    r['scientific_support']=bool(r['best_trace_gap'] < RECOVERY_TOL)
    r['interpretation']='Held-out optimizer-family robustness replication on a new theta, hidden source, and deterministic initial-design seed. Methodology robustness only; does not alter G35 adversarial verdict.'
    nums=[float(v) for v in r.values() if isinstance(v,(int,float,np.integer,np.floating)) and not isinstance(v,(bool,np.bool_))]
    valid=bool(all(np.isfinite(v) for v in nums))
    out={
      'iteration':'Iter017R','gate':'G35-R','K':a.K,'method':a.method,
      'holdout':a.holdout,'theta':theta,'source_shard':source_shard,
      'result':r,'structural_valid':valid,
      'frozen_thresholds':{'positive_recovery_trace_distance':RECOVERY_TOL},
      'scope_lock':'Optimizer robustness only inside finite additive independent single-axis Markovian measurement-feedback GKSL family; no adversarial/physics promotion.'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    if not valid: raise SystemExit(2)

if __name__=='__main__': main()
