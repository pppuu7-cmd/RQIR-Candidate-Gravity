#!/usr/bin/env python3
"""Iter029 / G40-TM-C: response-blind positive-control calibration of an
RTN optimizer aligned directly to the scientific max trace-distance metric.

Terminal G40-RC-A/G40-RC-D2 results are not altered. No RCG-002 target is used.
"""
import argparse, json, sys
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from scipy.stats import qmc

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter022b_g40c_rtn_optimizer_calibration import LO,HI,trajectory,metric_u,RECOVERY_TOL,BACKFLOW_MIN
from iter022c_g40c2_control_eligibility import CONTROLS_C2
from iter023b_g40rc_axis_covariant_calibration import covariant_blp_p,covariant_blp_u

METHODS=('sobol_powell','lhs_powell')
N_START=24
N_REFINE=4
MAXFEV=1600
XTOL=1e-6
FTOL=1e-8
BOUNDS=[(0.0,1.0)]*8


def design(method,shard):
    seed=149000+100*shard+(0 if method=='sobol_powell' else 53)
    if method=='sobol_powell':
        # Generate 32 prospectively, use the first frozen 24 only.
        return qmc.Sobol(d=8,scramble=True,seed=seed).random_base2(5)[:N_START]
    return qmc.LatinHypercube(d=8,seed=seed).random(N_START)


def direct_gap(u,target):
    return float(metric_u(np.clip(np.asarray(u,float),0.0,1.0),target)[0])


def optimize(method,shard,target):
    starts=[]
    for u in design(method,shard):
        g=direct_gap(u,target)
        starts.append((g,np.asarray(u,float)))
    starts.sort(key=lambda x:x[0])
    cands=[]
    for g0,u0 in starts[:N_REFINE]:
        fit=minimize(lambda z:direct_gap(z,target),u0,method='Powell',bounds=BOUNDS,
                     options={'maxfev':MAXFEV,'xtol':XTOL,'ftol':FTOL,'disp':False})
        u=np.clip(np.asarray(fit.x,float),0.0,1.0)
        gap,rn=metric_u(u,target)
        blp=covariant_blp_u(u)
        cands.append({
            'initial_direct_gap':float(g0),'gap':float(gap),'residual_norm_diagnostic':float(rn),
            'axis_covariant_BLP':float(blp),'nfev':int(getattr(fit,'nfev',-1)),
            'optimizer_success_flag':bool(fit.success),'strict_admissible':bool(blp>BACKFLOW_MIN)
        })
    strict=[c for c in cands if c['strict_admissible']]
    best=min(strict,key=lambda c:c['gap']) if strict else None
    return best,cands


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--method',choices=METHODS,required=True)
    ap.add_argument('--shard',type=int,choices=range(4),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()

    hidden=np.asarray(CONTROLS_C2[a.shard],float)
    hidden_blp=float(covariant_blp_p(hidden))
    eligible=bool(hidden_blp>BACKFLOW_MIN and np.all(hidden>=LO) and np.all(hidden<=HI))
    target=trajectory(hidden)
    best,cands=optimize(a.method,a.shard,target)
    vals=[hidden_blp]+[x for c in cands for x in (c['initial_direct_gap'],c['gap'],c['residual_norm_diagnostic'],c['axis_covariant_BLP'])]
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)))
    support=bool(structural and eligible and best is not None and best['gap']<RECOVERY_TOL and best['axis_covariant_BLP']>BACKFLOW_MIN)

    out={
      'iteration':'Iter029','gate':'G40-TM-C','method':a.method,'shard':a.shard,
      'hidden_control_axis_covariant_BLP':hidden_blp,'hidden_control_eligible':eligible,
      'best_strict_candidate':best,'n_refined_candidates':len(cands),'n_strict_candidates':sum(int(c['strict_admissible']) for c in cands),
      'structural_valid':structural,'scientific_support':support,
      'classification':'TRACE_METRIC_ALIGNED_RTN_CALIBRATION_LANE_PASS' if support else 'TRACE_METRIC_ALIGNED_RTN_CALIBRATION_LANE_NOT_ESTABLISHED',
      'frozen':{'objective':'maximum_trace_distance_trajectory_gap','n_starts':N_START,'n_refine':N_REFINE,'maxfev':MAXFEV,'xtol':XTOL,'ftol':FTOL,'recovery_tolerance':RECOVERY_TOL,'axis_covariant_BLP_min':BACKFLOW_MIN,'hidden_coordinates_used_as_starts':False,'RCG002_target_used':False},
      'scope_lock':'Finite symmetric hidden-classical RTN family and candidate-axis-frame covariant BLP witness inherited unchanged from G40-RC-C.',
      'interpretation':'Positive-control optimizer calibration only; cannot alter terminal G40 results or raise readiness.'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)

if __name__=='__main__': main()
