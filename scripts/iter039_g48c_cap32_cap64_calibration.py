#!/usr/bin/env python3
"""Iter039/G48-C response-blind calibration for trace caps 32 and 64."""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter034_g46c_extended_trace_ball_calibration import (
    METHODS,RADIAL_FRACTIONS,N_START,N_REFINE,MAX_NFEV,RECOVERY_TOL,C_REL_TOL,
    RANK_EIG_TOL,C_FLOOR,TRACE_TOL,LO,HI,hidden_A,weighted_pack,trajectory,
    residual,diagnostics,qmc_starts,radius
)

CAPS=(32.0,64.0)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--rank',type=int,choices=range(1,7),required=True); ap.add_argument('--cap',type=float,choices=CAPS,required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    Ah=hidden_A(a.rank,a.cap); hidden=weighted_pack(Ah)/radius(a.cap); C_hidden=Ah@Ah
    he=np.linalg.eigvalsh((C_hidden+C_hidden.T)/2); hidden_rank=int(np.sum(he>1e-10)); hidden_norm=float(np.linalg.norm(Ah,'fro')); target=trajectory(hidden,a.cap)
    scored=[]
    for z0 in qmc_starts(a.method,a.rank,a.cap):
        r=residual(z0,target,a.cap); scored.append((float(np.dot(r,r)),np.asarray(z0,float)))
    scored.sort(key=lambda x:x[0]); cands=[]
    for _,z0 in scored[:N_REFINE]:
        fit=least_squares(lambda z:residual(z,target,a.cap),z0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-10,xtol=1e-10,gtol=1e-10)
        gap,rn,crel,rrank,mineig,trc=diagnostics(fit.x,target,C_hidden,a.cap)
        cands.append({'gap':gap,'residual_norm':rn,'relative_kossakowski_error':crel,'recovered_effective_rank':rrank,'min_kossakowski_eigenvalue':mineig,'trace_C':trc,'search_z_norm':float(np.linalg.norm(fit.x)),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success)})
    best=min(cands,key=lambda c:(c['gap'],c['relative_kossakowski_error'],c['residual_norm']))
    vals=[hidden_norm,*he]+[x for c in cands for x in (c['gap'],c['residual_norm'],c['relative_kossakowski_error'],c['min_kossakowski_eigenvalue'],c['trace_C'],c['search_z_norm'])]
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)) and hidden_rank==a.rank and he.min()>-1e-12 and hidden_norm<=radius(a.cap)+1e-12)
    support=bool(structural and best['gap']<RECOVERY_TOL and best['relative_kossakowski_error']<C_REL_TOL and best['recovered_effective_rank']==a.rank and best['min_kossakowski_eigenvalue']>=C_FLOOR and best['trace_C']<=a.cap+TRACE_TOL)
    out={'iteration':'Iter039','gate':'G48-C','method':a.method,'rank':a.rank,'trace_cap':a.cap,'hidden':{'effective_rank':hidden_rank,'sqrt_frobenius_norm':hidden_norm,'trace_C':float(np.trace(C_hidden)),'min_C_eigenvalue':float(he.min()),'radial_fraction':RADIAL_FRACTIONS[a.rank-1]},'best_candidate':best,'n_refined_candidates':len(cands),'structural_valid':structural,'scientific_support':support,'classification':'CAP32_CAP64_TRACE_BALL_PSD_CALIBRATION_LANE_PASS' if support else ('G48C_IMPLEMENTATION_OR_NUMERICAL_INVALID' if not structural else 'G48C_FROZEN_CALIBRATION_RULE_NOT_MET'),'frozen':{'family':'C=A^2; A symmetric; tr(C)<=cap','caps':list(CAPS),'radial_fractions':list(RADIAL_FRACTIONS),'n_starts':N_START,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'trace_recovery_tolerance':RECOVERY_TOL,'relative_kossakowski_tolerance':C_REL_TOL,'rank_eigenvalue_threshold':RANK_EIG_TOL,'RCG002_target_used':False},'scope_lock':'Response-blind optimizer calibration only for finite real-PSD trace caps 32 and 64.','interpretation':'Calibration only; no comparator-separation or unbounded-PSD claim.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
