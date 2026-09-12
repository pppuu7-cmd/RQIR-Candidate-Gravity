#!/usr/bin/env python3
"""Iter023D / G40-RC-D2: deeper independent-search diagnostic for the sole
G40-RC-A shard-3 Sobol/LHS disagreement. Diagnostic only; cannot promote G40-RC-A.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.stats import qmc

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter022b_g40c_rtn_optimizer_calibration import LO,HI,residual_u,metric_u
from iter023b_g40rc_axis_covariant_calibration import covariant_blp_u,BACKFLOW_MIN
from iter023c_g40rc_axis_covariant_adversarial import target_traj

METHODS=('sobol64','lhs64','halton64','random64')
N_START=64; N_REFINE=12; MAX_NFEV=900; THETA=1.4


def starts(method):
    d=len(LO); seed={'sobol64':93103,'lhs64':93203,'halton64':93303,'random64':93403}[method]
    if method=='sobol64': return qmc.Sobol(d=d,scramble=True,seed=seed).random_base2(6)
    if method=='lhs64': return qmc.LatinHypercube(d=d,seed=seed).random(N_START)
    if method=='halton64': return qmc.Halton(d=d,scramble=True,seed=seed).random(N_START)
    return np.random.default_rng(seed).random((N_START,d))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    tar=target_traj(THETA); scored=[]
    for u in starts(a.method):
        r=residual_u(u,tar); scored.append((float(np.dot(r,r)),np.asarray(u,float)))
    scored.sort(key=lambda z:z[0]); candidates=[]
    for _,u0 in scored[:N_REFINE]:
        fit=least_squares(lambda z:residual_u(z,tar),u0,bounds=(0,1),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-11,xtol=1e-11,gtol=1e-11)
        gap,rn=metric_u(fit.x,tar); blp=covariant_blp_u(fit.x)
        candidates.append({'gap':float(gap),'residual_norm':float(rn),'axis_covariant_BLP':float(blp),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success),'strict_admissible':bool(blp>BACKFLOW_MIN)})
    strict=[c for c in candidates if c['strict_admissible']]
    best=min(strict,key=lambda c:(c['gap'],c['residual_norm'])) if strict else None
    vals=[x for c in candidates for x in (c['gap'],c['residual_norm'],c['axis_covariant_BLP'])]
    structural=bool(len(candidates)==N_REFINE and np.all(np.isfinite(vals)))
    out={'iteration':'Iter023D','gate':'G40-RC-D2','method':a.method,'shard':3,'theta':THETA,
         'best_strict_candidate':best,'n_refined_candidates':len(candidates),'n_strict_candidates':len(strict),'structural_valid':structural,
         'frozen':{'n_starts':N_START,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'axis_covariant_BLP_min':BACKFLOW_MIN,'agreement_tolerance':0.002,'previous_best_coordinates_injected':False,'winner_selected_by':'max_trace_distance_gap'},
         'interpretation':'Optimizer/objective-geometry diagnostic only; cannot promote terminal G40-RC-A.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
