#!/usr/bin/env python3
"""Iter031 / G40-TM-A: prospective RCG-002 toy-trajectory adversarial
search using the trace-metric-aligned RTN optimizer calibrated in G40-TM-C.

PRODUCTION LAUNCH IS LOCKED UNTIL TERMINAL G40-TM-C PASS.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES,GAP_THRESHOLD,RECOVERY_TOL
from iter011_robustness_suite import I4,Z
from iter022b_g40c_rtn_optimizer_calibration import TIMES,PROBES
from iter023b_g40rc_axis_covariant_calibration import BACKFLOW_MIN
from iter029_g40tmc_trace_metric_rtn_calibration import METHODS,optimize

ZZ=np.kron(Z,Z)


def target_traj(theta):
    out=[]
    for t in TIMES:
        a=float(theta*t); U=np.cos(a)*I4-1j*np.sin(a)*ZZ
        out.append([U@rho@U.conj().T for rho in PROBES])
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--method',choices=METHODS,required=True)
    ap.add_argument('--shard',type=int,choices=range(4),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    scale,t0=CASES[a.shard]; theta=float(scale*t0); tar=target_traj(theta)
    best,cands=optimize(a.method,a.shard,tar)
    vals=[]
    for c in cands:
        vals += [c['initial_direct_gap'],c['gap'],c['residual_norm_diagnostic'],c['axis_covariant_BLP']]
    structural=bool(len(cands)==4 and np.all(np.isfinite(vals)))
    lane_support=bool(structural and best is not None and best['gap']>GAP_THRESHOLD and best['axis_covariant_BLP']>BACKFLOW_MIN)
    out={
      'iteration':'Iter031','gate':'G40-TM-A','method':a.method,'shard':a.shard,'theta':theta,
      'best_strict_candidate':best,'n_refined_candidates':len(cands),'n_strict_candidates':sum(int(c['strict_admissible']) for c in cands),
      'structural_valid':structural,'lane_support':lane_support,
      'checks':{'strict_candidate_exists':bool(best is not None),'nonzero_gap':bool(best is not None and best['gap']>GAP_THRESHOLD),'axis_covariant_BLP_filter_pass':bool(best is not None and best['axis_covariant_BLP']>BACKFLOW_MIN)},
      'frozen':{'times':TIMES.tolist(),'n_probes':len(PROBES),'axis_covariant_BLP_filter':BACKFLOW_MIN,'nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':RECOVERY_TOL,'methods':list(METHODS),'n_starts':24,'n_refine':4,'maxfev':1600,'direct_objective':'maximum_trace_distance_trajectory_gap','target_convention':'exp(-i theta*t ZxZ) toy trajectory','same_target_shards_as_G40RCA':True},
      'authorization_lock':'Production launch permitted only after terminal G40-TM-C PASS.',
      'scope_lock':'Finite hidden-classical symmetric RTN family with candidate-axis-frame covariant BLP witness. Not all non-Markovian classical channels.',
      'interpretation':'Prospective adversarial toy-trajectory search. Any support remains strictly finite-family scoped.'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)

if __name__=='__main__': main()
