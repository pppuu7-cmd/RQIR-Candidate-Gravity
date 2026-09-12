#!/usr/bin/env python3
"""Iter023C / G40-RC-A: prospective RCG-002 toy-trajectory adversarial
search against the calibrated axis-frame-covariant strict-BLP finite RTN family.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES,GAP_THRESHOLD,RECOVERY_TOL
from iter011_robustness_suite import I4,Z
from iter022b_g40c_rtn_optimizer_calibration import METHODS,TIMES,PROBES
from iter023b_g40rc_axis_covariant_calibration import strict_optimize,BACKFLOW_MIN

ZZ=np.kron(Z,Z)


def target_traj(theta):
    out=[]
    for t in TIMES:
        a=float(theta*t); U=np.cos(a)*I4-1j*np.sin(a)*ZZ
        out.append([U@rho@U.conj().T for rho in PROBES])
    return out


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    scale,t0=CASES[a.shard]; theta=float(scale*t0); tar=target_traj(theta)
    best,cands=strict_optimize(a.method,a.shard,tar)
    vals=[]
    for c in cands: vals += [c['gap'],c['residual_norm'],c['axis_covariant_BLP']]
    structural=bool(len(cands)>0 and np.all(np.isfinite(vals)))
    lane_support=bool(structural and best is not None and best['gap']>GAP_THRESHOLD and best['axis_covariant_BLP']>BACKFLOW_MIN)
    out={'iteration':'Iter023C','gate':'G40-RC-A','method':a.method,'shard':a.shard,'theta':theta,
         'best_strict_candidate':best,'n_refined_candidates':len(cands),'n_strict_candidates':sum(int(c['strict_admissible']) for c in cands),
         'structural_valid':structural,'lane_support':lane_support,
         'checks':{'strict_candidate_exists':bool(best is not None),'nonzero_gap':bool(best is not None and best['gap']>GAP_THRESHOLD),'axis_covariant_BLP_filter_pass':bool(best is not None and best['axis_covariant_BLP']>BACKFLOW_MIN)},
         'frozen':{'times':TIMES.tolist(),'n_probes':len(PROBES),'axis_covariant_BLP_filter':BACKFLOW_MIN,'nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':RECOVERY_TOL,'same_search_rule_as_G40RCC':True,'same_family_bounds_design_refinement':True,'target_convention':'exp(-i theta*t ZxZ) toy trajectory'},
         'scope_lock':'Finite hidden-classical symmetric RTN family with candidate-axis-frame covariant BLP witness. Not globally optimized BLP, not all non-Markovian classical channels.',
         'interpretation':'Prospective adversarial toy-trajectory search. Any support remains strictly finite-family scoped.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
