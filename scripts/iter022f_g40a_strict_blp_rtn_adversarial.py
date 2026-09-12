#!/usr/bin/env python3
"""Iter022F / G40-A: prospective RCG-002 adversarial search against the
calibrated fixed-witness strict-BLP hidden-classical RTN subset.

Authorized only after G40-C2 calibrated the underlying RTN optimizer and G40-C3
calibrated the BLP>0.02 filtered search rule.  No family, bounds, start design,
time grid, probes, filter or thresholds are changed here.

Target is the preregistered controlled-phase toy trajectory
  U(t)=exp[-i theta t (Z⊗Z)]
on the same four times and six probes used by G40-C2/C3.  This is not a
continuum gravity-time model.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES,GAP_THRESHOLD,RECOVERY_TOL
from iter011_robustness_suite import I4,Z,td
from iter022b_g40c_rtn_optimizer_calibration import METHODS,TIMES,PROBES
from iter022e_g40c3_strict_subset_search_calibration import strict_optimize

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
    finite=all(np.all(np.isfinite([c['gap'],c['residual_norm'],c['BLP']])) for c in cands)
    structural=bool(finite)
    out={'iteration':'Iter022F','gate':'G40-A','method':a.method,'shard':a.shard,'theta':theta,
         'best_strict_candidate':best,'n_refined_candidates':len(cands),'n_strict_candidates':sum(int(c['strict_admissible']) for c in cands),
         'structural_valid':structural,
         'checks':{'strict_candidate_exists':bool(best is not None),'nonzero_gap':bool(best is not None and best['gap']>GAP_THRESHOLD),'fixed_witness_BLP_filter_pass':bool(best is not None and best['BLP']>0.02)},
         'frozen':{'times':TIMES.tolist(),'n_probes':len(PROBES),'strict_BLP_filter':0.02,'nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':RECOVERY_TOL,'same_search_rule_as_G40C3':True,'same_family_bounds_design_refinement':True,'target_convention':'exp(-i theta*t ZxZ) toy trajectory'},
         'scope_lock':'Finite hidden-classical symmetric RTN family restricted to the G40-C3 fixed-pair BLP>0.02 subset. Not rotation-covariant all-BLP RTN and not all non-Markovian classical channels.',
         'interpretation':'Prospective adversarial toy-trajectory search. Any support remains strictly finite-family/fixed-witness scoped and cannot establish a general classical-mediator no-go.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
