#!/usr/bin/env python3
"""Iter022E / G40-C3: calibrate a strict-BLP-filtered RTN search.

G40-C2 calibrated the underlying unconstrained RTN optimizer.  A later
adversarial claim specifically about the frozen fixed-witness strict-BLP subset
requires a new search rule: only refined candidates with BLP total positive
trace-distance increment >0.02 are scientifically admissible.  This gate
calibrates that rule prospectively before any RCG-002 target is used.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter022b_g40c_rtn_optimizer_calibration import METHODS,RECOVERY_TOL,BACKFLOW_MIN,N_REFINE,MAX_NFEV,trajectory,design,residual_u,metric_u,blp_u
from iter022c_g40c2_control_eligibility import CONTROLS_C2


def strict_optimize(method,shard,target_traj):
    scored=[]
    for u in design(method,shard):
        rr=residual_u(u,target_traj); scored.append((float(np.dot(rr,rr)),np.asarray(u,float)))
    scored.sort(key=lambda z:z[0])
    candidates=[]
    for _,u0 in scored[:N_REFINE]:
        fit=least_squares(lambda z:residual_u(z,target_traj),u0,bounds=(0,1),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-10,xtol=1e-10,gtol=1e-10)
        gap,rn=metric_u(fit.x,target_traj); b=blp_u(fit.x)
        candidates.append({'gap':float(gap),'residual_norm':float(rn),'BLP':float(b),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success),'strict_admissible':bool(b>BACKFLOW_MIN)})
    admiss=[c for c in candidates if c['strict_admissible']]
    best=min(admiss,key=lambda c:(c['gap'],c['residual_norm'])) if admiss else None
    return best,candidates


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    hidden=CONTROLS_C2[a.shard]; target_traj=trajectory(hidden); best,cands=strict_optimize(a.method,a.shard,target_traj)
    structural=bool(all(np.isfinite([c['gap'],c['residual_norm'],c['BLP']]).all() if isinstance(np.array([c['gap'],c['residual_norm'],c['BLP']]),np.ndarray) else True for c in cands))
    support=bool(structural and best is not None and best['gap']<RECOVERY_TOL and best['BLP']>BACKFLOW_MIN)
    out={'iteration':'Iter022E','gate':'G40-C3','method':a.method,'shard':a.shard,'best_strict_candidate':best,'n_refined_candidates':len(cands),'n_strict_candidates':sum(int(c['strict_admissible']) for c in cands),'structural_valid':structural,'scientific_support':support,
         'frozen':{'strict_BLP_filter':BACKFLOW_MIN,'recovery_tolerance':RECOVERY_TOL,'same_family_bounds_design_and_refinement_as_G40C2':True,'top_refinements':N_REFINE,'max_nfev':MAX_NFEV,'RCG002_target_used':False},
         'scope_lock':'Fixed-witness strict-BLP subset of the finite hidden-classical RTN family calibrated by G40-C2.',
         'interpretation':'Search-rule calibration only. PASS authorizes a separate prospective RCG-002 adversarial search restricted by the same BLP filter.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
