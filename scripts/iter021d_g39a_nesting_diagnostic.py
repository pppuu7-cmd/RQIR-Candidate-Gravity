#!/usr/bin/env python3
"""Iter021D / G39-A-N: frozen optimizer/nesting diagnostic.

Purpose: diagnose the terminal G39-A rank3-vs-rank2 nesting violation without
changing the comparator family, science thresholds, target, or optimizer bounds.
Rank 3 mathematically contains rank 2 through an exactly zero third-mode rate.
For each original method/shard this script:
  1. reproduces the frozen rank-2 search while retaining its best coordinates;
  2. embeds those coordinates exactly in rank 3 with third-mode rate = 0;
  3. evaluates the embedded rank-3 objective before any refinement;
  4. optionally refines from that legal embedded point with the same bounds.

Interpretation was frozen prospectively:
- if embedded rank3 reproduces rank2 to 1e-10 and seeded rank3 is no worse than
  embedded by more than 1e-10, any original G39-A nesting violation is an
  OPTIMIZER/NUMERICAL SEARCH MISS, not a scientific failure of RCG-002;
- if exact embedding itself fails, classify IMPLEMENTATION/NESTING FAIL and do
  not use G39-A as scientific evidence.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import target,td
from iter013_global_search_calibration import CASES
from iter021b_g39c_multimode_optimizer_calibration import (
    METHODS,N_REFINE,MAX_NFEV,design,residual,state_u,dim
)

EMBED_TOL=1e-10


def best_rank2_with_x(method,shard,tar):
    scored=[]
    for u in design(method,2,shard):
        r=residual(u,2,tar); scored.append((float(np.dot(r,r)),u))
    scored.sort(key=lambda x:x[0])
    best=None
    for _,u0 in scored[:N_REFINE]:
        fit=least_squares(lambda z:residual(z,2,tar),u0,bounds=(0,1),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-11,xtol=1e-11,gtol=1e-11)
        gap=float(td(state_u(fit.x,2),tar)); rn=float(np.linalg.norm(fit.fun))
        cand=(gap,rn,int(fit.nfev),bool(fit.success),fit.x.copy())
        if best is None or (gap,rn)<(best[0],best[1]): best=cand
    return best


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--method',choices=METHODS,required=True)
    ap.add_argument('--shard',type=int,choices=range(4),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    scale,t0=CASES[a.shard]; tar=target(float(scale*t0))
    g2,r2,n2,ok2,x2=best_rank2_with_x(a.method,a.shard,tar)

    x3=np.full(dim(3),0.5,float)
    x3[:dim(2)]=x2
    x3[2*7+6]=0.0  # exact zero rate => exact rank-2 boundary
    g3_embed=float(td(state_u(x3,3),tar))
    r3_embed=float(np.linalg.norm(residual(x3,3,tar)))

    fit3=least_squares(lambda z:residual(z,3,tar),x3,bounds=(0,1),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-11,xtol=1e-11,gtol=1e-11)
    g3_seed=float(td(state_u(fit3.x,3),tar)); r3_seed=float(np.linalg.norm(fit3.fun))

    embed_ok=bool(abs(g3_embed-g2)<=EMBED_TOL and abs(r3_embed-r2)<=EMBED_TOL)
    refine_ok=bool(g3_seed<=g3_embed+EMBED_TOL)
    structural=bool(all(np.isfinite(v) for v in (g2,r2,g3_embed,r3_embed,g3_seed,r3_seed)))
    diagnostic_pass=bool(structural and embed_ok and refine_ok)
    out={
      'iteration':'Iter021D','gate':'G39-A-N','method':a.method,'shard':a.shard,
      'rank2_reproduced':{'gap':g2,'residual_norm':r2,'nfev':n2,'optimizer_success_flag':ok2},
      'rank3_exact_embedding':{'gap':g3_embed,'residual_norm':r3_embed,'zero_third_mode_rate':True},
      'rank3_seeded_refinement':{'gap':g3_seed,'residual_norm':r3_seed,'nfev':int(fit3.nfev),'optimizer_success_flag':bool(fit3.success)},
      'checks':{'embedding_agrees_rank2_1e-10':embed_ok,'seeded_rank3_not_worse_1e-10':refine_ok},
      'structural_valid':structural,'diagnostic_support':diagnostic_pass,
      'frozen_thresholds':{'embedding_tolerance':EMBED_TOL,'same_original_bounds':True,'same_original_target':True,'same_rank2_design_and_refinement':True},
      'interpretation':'PASS diagnoses any original G39-A rank3>rank2 nesting violation as optimizer/search miss because an explicit legal rank3 point reproduces the rank2 optimum. It does not itself establish a nonzero adversarial gap.'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)

if __name__=='__main__': main()
