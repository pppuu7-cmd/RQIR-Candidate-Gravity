#!/usr/bin/env python3
"""Iter021E / G39-A2: prospectively repaired rank-3 adversarial search.

Authorized only after terminal G39-A-N proved that the original G39-A nesting
violation was an optimizer/search miss.  Family, target, bounds and science
thresholds are unchanged.  The repair adds one mathematically mandatory legal
rank-2 boundary point (zero third-mode rate) to the existing independent rank-3
Sobol/LHS multistart construction.  The original rank-3 design remains intact.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES,GAP_THRESHOLD,RECOVERY_TOL
from iter011_robustness_suite import target,td
from iter021b_g39c_multimode_optimizer_calibration import METHODS,N_REFINE,MAX_NFEV,design,residual,state_u,dim
from iter021d_g39a_nesting_diagnostic import best_rank2_with_x

EMBED_TOL=1e-10


def refine_rank3(u0,tar):
    fit=least_squares(lambda z:residual(z,3,tar),u0,bounds=(0,1),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-11,xtol=1e-11,gtol=1e-11)
    gap=float(td(state_u(fit.x,3),tar)); rn=float(np.linalg.norm(fit.fun))
    return gap,rn,int(fit.nfev),bool(fit.success)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    scale,t0=CASES[a.shard]; theta=float(scale*t0); tar=target(theta)
    g2,r2,n2,ok2,x2=best_rank2_with_x(a.method,a.shard,tar)
    x3=np.full(dim(3),0.5,float); x3[:dim(2)]=x2; x3[2*7+6]=0.0
    gembed=float(td(state_u(x3,3),tar)); rembed=float(np.linalg.norm(residual(x3,3,tar)))

    scored=[]
    for u in design(a.method,3,a.shard):
        rr=residual(u,3,tar); scored.append((float(np.dot(rr,rr)),u))
    scored.sort(key=lambda z:z[0])
    candidates=[(gembed,rembed,0,True,'exact_rank2_boundary')]
    for _,u0 in scored[:N_REFINE]:
        g,r,n,ok=refine_rank3(u0,tar); candidates.append((g,r,n,ok,'original_rank3_design'))
    g,r,n,ok=refine_rank3(x3,tar); candidates.append((g,r,n,ok,'rank2_boundary_seeded_refinement'))
    best=min(candidates,key=lambda z:(z[0],z[1]))
    g3,r3,n3,ok3,source=best
    structural=bool(np.all(np.isfinite([g2,r2,gembed,rembed,g3,r3])))
    embedding_ok=bool(abs(gembed-g2)<=EMBED_TOL)
    nesting_ok=bool(g3<=g2+EMBED_TOL)
    out={'iteration':'Iter021E','gate':'G39-A2','method':a.method,'shard':a.shard,'theta':theta,
         'rank2_parent':{'gap':float(g2),'residual_norm':float(r2),'nfev':int(n2),'optimizer_success_flag':bool(ok2)},
         'rank3_exact_embedding':{'gap':gembed,'residual_norm':rembed,'zero_third_mode_rate':True},
         'rank3_repaired_best':{'gap':float(g3),'residual_norm':float(r3),'nfev':int(n3),'optimizer_success_flag':bool(ok3),'winner_source':source},
         'checks':{'exact_embedding_agrees_parent_1e-10':embedding_ok,'rank3_not_worse_than_parent_1e-10':nesting_ok,'rank3_nonzero':bool(g3>GAP_THRESHOLD)},
         'structural_valid':structural,
         'frozen_thresholds':{'adversarial_nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':RECOVERY_TOL,'embedding_and_nesting_tolerance':EMBED_TOL,'original_rank3_design_retained':True,'one_legal_parent_boundary_seed_added':True},
         'interpretation':'Prospectively repaired adversarial search after G39-A-N. Any support remains restricted to the calibrated finite rank-3 multimode shared classical white-noise family.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
