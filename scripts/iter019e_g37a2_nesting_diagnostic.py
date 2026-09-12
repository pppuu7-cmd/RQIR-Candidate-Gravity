#!/usr/bin/env python3
"""Iter019E / G37-A2-N: frozen shared-parent embedding diagnostic.

Diagnose the terminal G37-A2 shard-2 nesting violation without changing the
comparator family, target, optimizer bounds, or any science threshold.  The
corrected G37-C2 family claims to contain the G36 shared-noise family exactly at
lambda_MF=0.  For each frozen method/shard this script:
  1. reproduces the calibrated G36 shared-noise adversarial search and retains
     its fitted coordinates;
  2. maps those coordinates into the G37-C2 19D chart with lambda_MF=0;
  3. evaluates that legal combined-family boundary point exactly;
  4. refines from the embedded point with the existing G37-C2 residual/bounds.

Prospective interpretation:
- exact embedding agreement <=1e-10 and seeded combined gap no worse than the
  embedding by >1e-10 => any G37-A2 violation against the shared parent is an
  optimizer/search miss, not a scientific failure of RCG-002;
- exact embedding failure => implementation/nesting failure; stop scientific
  interpretation and repair the family implementation only.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES
from iter011_robustness_suite import target,td
from iter018b_g36c_shared_noise_optimizer_calibration import METHODS,optimize as shared_optimize,LO,HI
from iter019c_g37c2_nested_combined_calibration import state_from_unit,residual,MAX_NFEV

EMBED_TOL=1e-10


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    scale,t0=CASES[a.shard]; theta=float(scale*t0); tar=target(theta)
    gp,xhat,nfev,rp=shared_optimize(a.method,a.shard,tar)
    u7=np.clip((np.asarray(xhat,float)-LO)/(HI-LO),0.0,1.0)
    uc=np.full(19,0.5,float); uc[0]=0.0; uc[12:19]=u7
    ge=float(td(state_from_unit(uc,theta),tar)); re=float(np.linalg.norm(residual(uc,theta,tar)))
    fit=least_squares(lambda z:residual(z,theta,tar),uc,bounds=(0,1),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-11,xtol=1e-11,gtol=1e-11)
    gs=float(td(state_from_unit(fit.x,theta),tar)); rs=float(np.linalg.norm(fit.fun))
    embed_ok=bool(abs(ge-gp)<=EMBED_TOL)
    refine_ok=bool(gs<=ge+EMBED_TOL)
    structural=bool(np.all(np.isfinite([gp,rp,ge,re,gs,rs])))
    support=bool(structural and embed_ok and refine_ok)
    out={'iteration':'Iter019E','gate':'G37-A2-N','method':a.method,'shard':a.shard,'theta':theta,
         'shared_parent_reproduced':{'gap':float(gp),'residual_norm':float(rp),'nfev':int(nfev)},
         'combined_exact_shared_embedding':{'gap':ge,'residual_norm':re,'lambda_MF':0.0},
         'combined_seeded_refinement':{'gap':gs,'residual_norm':rs,'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success)},
         'checks':{'embedding_agrees_shared_parent_1e-10':embed_ok,'seeded_combined_not_worse_1e-10':refine_ok},
         'structural_valid':structural,'diagnostic_support':support,
         'frozen_thresholds':{'embedding_tolerance':EMBED_TOL,'same_original_target':True,'same_shared_parent_optimizer':True,'same_G37_bounds':True},
         'interpretation':'PASS diagnoses a G37-A2 shared-parent nesting violation as optimizer/search miss. It does not establish the adversarial nonzero-gap claim.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
