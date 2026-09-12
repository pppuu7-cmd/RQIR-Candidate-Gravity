#!/usr/bin/env python3
"""Iter019F / G37-A3: prospective boundary-preserving adversarial repair.

Authorized after G37-A2-N showed exact shared-parent embedding agreement to
machine precision but LSQ surrogate refinement could worsen the final trace-
distance objective.  This is a new prospective gate; no prior result is promoted.

Family, target, bounds, Sobol/LHS designs and science thresholds are unchanged.
The repair retains every original G37-A2 start/refinement and additionally
includes both mathematically exact parent boundaries:
  - shared parent: lambda_MF=0, coordinates from the calibrated G36 optimizer;
  - K2 MF parent: lambda_MF=1, shared cA=cB=0, coordinates from G34 optimizer.
Exact parent points remain legal candidates even if LSQ refinement worsens them.
All candidates are finally ranked by trace distance, the scientific metric.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES,GAP_THRESHOLD,RECOVERY_TOL
from iter011_robustness_suite import target,td
from iter018b_g36c_shared_noise_optimizer_calibration import METHODS, optimize as shared_optimize, LO, HI
from iter016_calibrated_multichannel_comparator import starts as mf_starts, residual_vector as mf_residual, metrics as mf_metrics, LSQ_MAX_NFEV
from iter019c_g37c2_nested_combined_calibration import design as combined_design, residual as combined_residual, state_from_unit, MAX_NFEV, N_REFINE

EMBED_TOL=1e-10


def best_mf_with_u(method,shard,theta,tar):
    best=None
    for u0 in mf_starts(method,2,shard):
        fit=least_squares(lambda u:mf_residual(u,2,theta,tar),np.asarray(u0,float),bounds=(0,1),method='trf',x_scale='jac',ftol=1e-11,xtol=1e-11,gtol=1e-11,max_nfev=LSQ_MAX_NFEV)
        gap,rn=mf_metrics(fit.x,2,theta,tar); cand=(gap,rn,int(fit.nfev),bool(fit.success),fit.x.copy())
        if best is None or (gap,rn)<(best[0],best[1]): best=cand
    return best


def refine_combined(u0,theta,tar):
    fit=least_squares(lambda z:combined_residual(z,theta,tar),np.asarray(u0,float),bounds=(0,1),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-11,xtol=1e-11,gtol=1e-11)
    gap=float(td(state_from_unit(fit.x,theta),tar)); rn=float(np.linalg.norm(fit.fun))
    return gap,rn,int(fit.nfev),bool(fit.success),fit.x.copy()


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    scale,t0=CASES[a.shard]; theta=float(scale*t0); tar=target(theta)

    # Exact shared-parent boundary.
    gs, xs, ns, rs = shared_optimize(a.method,a.shard,tar)
    us=np.clip((np.asarray(xs,float)-LO)/(HI-LO),0.0,1.0)
    cs=np.full(19,0.5,float); cs[0]=0.0; cs[12:19]=us
    gs_embed=float(td(state_from_unit(cs,theta),tar))

    # Exact K2 measurement-feedback parent boundary.
    gm,rm,nm,okm,um=best_mf_with_u(a.method,a.shard,theta,tar)
    cm=np.full(19,0.5,float); cm[0]=1.0; cm[1:12]=um; cm[16]=0.5; cm[17]=0.5
    gm_embed=float(td(state_from_unit(cm,theta),tar))

    candidates=[
      (gs_embed,float(np.linalg.norm(combined_residual(cs,theta,tar))),0,True,'exact_shared_parent',cs.copy()),
      (gm_embed,float(np.linalg.norm(combined_residual(cm,theta,tar))),0,True,'exact_mf_parent',cm.copy()),
    ]

    # Retain original G37-A2 design: rank starts by smooth residual then refine top N_REFINE.
    scored=[]
    for u in combined_design(a.method,a.shard):
        rr=combined_residual(u,theta,tar); scored.append((float(np.dot(rr,rr)),u))
    scored.sort(key=lambda z:z[0])
    for _,u0 in scored[:N_REFINE]:
        g,r,n,ok,x=refine_combined(u0,theta,tar); candidates.append((g,r,n,ok,'original_combined_design',x))

    # Add both legal parent seeds; keep exact parents regardless of refinement behavior.
    for label,u0 in [('shared_parent_seeded_refinement',cs),('mf_parent_seeded_refinement',cm)]:
        g,r,n,ok,x=refine_combined(u0,theta,tar); candidates.append((g,r,n,ok,label,x))

    best=min(candidates,key=lambda z:(z[0],z[1]))
    gb,rb,nb,okb,source,_=best
    parent_best=min(gs_embed,gm_embed)
    structural=bool(np.all(np.isfinite([gs,gs_embed,gm,gm_embed,gb,rb])))
    shared_embed_ok=bool(abs(gs_embed-gs)<=EMBED_TOL)
    mf_embed_ok=bool(abs(gm_embed-gm)<=EMBED_TOL)
    nesting_ok=bool(gb<=parent_best+EMBED_TOL)
    out={'iteration':'Iter019F','gate':'G37-A3','method':a.method,'shard':a.shard,'theta':theta,
         'shared_parent':{'gap':float(gs),'embedded_gap':gs_embed,'embedding_ok_1e-10':shared_embed_ok},
         'mf_parent':{'gap':float(gm),'embedded_gap':gm_embed,'embedding_ok_1e-10':mf_embed_ok},
         'boundary_preserving_best':{'gap':float(gb),'residual_norm':float(rb),'nfev':int(nb),'optimizer_success_flag':bool(okb),'winner_source':source},
         'checks':{'both_parent_embeddings_exact_1e-10':bool(shared_embed_ok and mf_embed_ok),'combined_not_worse_than_best_parent_1e-10':nesting_ok,'nonzero_gap':bool(gb>GAP_THRESHOLD)},
         'structural_valid':structural,
         'frozen_thresholds':{'adversarial_nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':RECOVERY_TOL,'embedding_and_nesting_tolerance':EMBED_TOL,'original_combined_design_retained':True,'both_exact_parent_boundaries_retained_as_candidates':True},
         'scope_lock':'Truly nested finite Markovian family: lambda_MF-scaled K2 single-axis measurement-feedback plus one shared Gaussian classical Hamiltonian-noise process.',
         'interpretation':'New prospective boundary-preserving adversarial gate after surrogate-objective refinement failure. Support, if any, remains finite-family scoped only.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
