#!/usr/bin/env python3
"""Iter023B / G40-RC-C: positive-control calibration of an axis-frame-covariant
BLP witness/search rule for the finite hidden-classical RTN family.

No RCG-002 target is used.  The BLP pair co-rotates with each candidate's
local noise axes, removing the fixed-basis fragility diagnosed by G40-D.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import Y,Z,td
from iter022b_g40c_rtn_optimizer_calibration import (
    METHODS,TIMES,PROBES,BLP_TIMES,LO,HI,N_REFINE,MAX_NFEV,
    RECOVERY_TOL,BACKFLOW_MIN,trajectory,design,residual_u,metric_u,block,
    reduced_map,apply,
)
from iter022c_g40c2_control_eligibility import CONTROLS_C2


def frame_unitary(theta,phi):
    """U with U Z U^dagger = n(theta,phi).sigma."""
    return expm(-0.5j*phi*Z) @ expm(-0.5j*theta*Y)


def covariant_pair_from_p(p):
    p=np.asarray(p,float)
    _,_,_,_,ta,pa,tb,pb=p
    UA=frame_unitary(ta,pa); UB=frame_unitary(tb,pb)
    z0=np.array([1,0],complex)
    xp=np.array([1,1],complex)/np.sqrt(2)
    xm=np.array([1,-1],complex)/np.sqrt(2)
    va=np.kron(UA@xp,UB@z0); vb=np.kron(UA@xm,UB@z0)
    return np.outer(va,va.conj()),np.outer(vb,vb.conj())


def covariant_blp_p(p):
    p=np.asarray(p,float); G=block(p); a,b=covariant_pair_from_p(p); ds=[]
    for t in BLP_TIMES:
        E=reduced_map(G,float(t)); ds.append(td(apply(E,a),apply(E,b)))
    ds=np.asarray(ds,float)
    return float(np.sum(np.clip(np.diff(ds),0,None)))


def covariant_blp_u(u):
    p=LO+np.clip(np.asarray(u,float),0,1)*(HI-LO)
    return covariant_blp_p(p)


def strict_optimize(method,shard,target_traj):
    scored=[]
    for u in design(method,shard):
        rr=residual_u(u,target_traj); scored.append((float(np.dot(rr,rr)),np.asarray(u,float)))
    scored.sort(key=lambda z:z[0]); candidates=[]
    for _,u0 in scored[:N_REFINE]:
        fit=least_squares(lambda z:residual_u(z,target_traj),u0,bounds=(0,1),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-10,xtol=1e-10,gtol=1e-10)
        gap,rn=metric_u(fit.x,target_traj); b=covariant_blp_u(fit.x)
        candidates.append({'gap':float(gap),'residual_norm':float(rn),'axis_covariant_BLP':float(b),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success),'strict_admissible':bool(b>BACKFLOW_MIN)})
    admiss=[c for c in candidates if c['strict_admissible']]
    best=min(admiss,key=lambda c:(c['gap'],c['residual_norm'])) if admiss else None
    return best,candidates


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    hidden=np.asarray(CONTROLS_C2[a.shard],float); hidden_blp=covariant_blp_p(hidden); eligible=bool(hidden_blp>BACKFLOW_MIN)
    target_traj=trajectory(hidden); best,cands=strict_optimize(a.method,a.shard,target_traj)
    vals=[]
    for c in cands: vals += [c['gap'],c['residual_norm'],c['axis_covariant_BLP']]
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals+[hidden_blp])))
    support=bool(structural and eligible and best is not None and best['gap']<RECOVERY_TOL and best['axis_covariant_BLP']>BACKFLOW_MIN)
    out={'iteration':'Iter023B','gate':'G40-RC-C','method':a.method,'shard':a.shard,
         'hidden_control_axis_covariant_BLP':float(hidden_blp),'hidden_control_eligible':eligible,
         'best_strict_candidate':best,'n_refined_candidates':len(cands),'n_strict_candidates':sum(int(c['strict_admissible']) for c in cands),
         'structural_valid':structural,'scientific_support':support,
         'frozen':{'BLP_threshold':BACKFLOW_MIN,'recovery_tolerance':RECOVERY_TOL,'times':TIMES.tolist(),'n_probes':len(PROBES),'top_refinements':N_REFINE,'max_nfev':MAX_NFEV,'same_family_bounds_design_as_G40C2_C3':True,'RCG002_target_used':False},
         'scope_lock':'Finite hidden-classical symmetric RTN family with a candidate-axis-frame covariant BLP witness; not a global optimization over all BLP state pairs.',
         'interpretation':'Positive-control calibration only. PASS may authorize a separate prospective RCG-002 adversarial gate with this exact covariant witness rule.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
