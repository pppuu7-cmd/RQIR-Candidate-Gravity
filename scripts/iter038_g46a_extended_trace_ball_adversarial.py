#!/usr/bin/env python3
"""Iter038 / G46-A: prospective RCG-002 adversarial search against calibrated real-PSD trace caps 8 and 16."""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
from scipy.stats import qmc,norm

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I4,td,choi
from iter013_global_search_calibration import CASES,GAP_THRESHOLD,RECOVERY_TOL
from iter022b_g40c_rtn_optimizer_calibration import PROBES
from iter024a_g41p_high_rank_classical_kossakowski import map_apply
from iter025a_g42j_full_psd_kossakowski_identifiability import TIMES,generator_from_C
from iter030_g44c_trace_ball_optimizer_calibration import METHODS
from iter032_g44a_trace_ball_psd_adversarial import target_traj
from iter034_g46c_extended_trace_ball_calibration import CAPS,N_START,N_REFINE,MAX_NFEV,z_to_A

LO=-np.ones(21,float); HI=np.ones(21,float)
TP_TOL=1e-10; CHOI_FLOOR=-1e-8; STATE_FLOOR=-1e-8; TRACE_TOL=1e-10; C_FLOOR=-1e-10; TRACE_C_TOL=1e-8


def cmat(z,cap):
    A=z_to_A(z,cap)
    return A@A


def candidate_traj(z,cap):
    G=generator_from_C(cmat(z,cap)); out=[]
    for t in TIMES:
        E=expm(G*float(t)); out.append([map_apply(E,rho) for rho in PROBES])
    return out


def residual(z,target,cap):
    pred=candidate_traj(z,cap); arr=[]
    for aa,bb in zip(pred,target):
        for x,y in zip(aa,bb):
            d=x-y; arr.extend(d.real.reshape(-1)); arr.extend(d.imag.reshape(-1))
    return np.asarray(arr,float)


def metric(z,target,cap):
    pred=candidate_traj(z,cap)
    gaps=[td(x,y) for aa,bb in zip(pred,target) for x,y in zip(aa,bb)]
    return float(max(gaps)),float(np.linalg.norm(residual(z,target,cap)))


def starts(method,shard,cap):
    seed=20000+1000*int(cap)+100*shard+(0 if method=='sobol_lsq' else 29)
    if method=='sobol_lsq':
        u=qmc.Sobol(d=22,scramble=True,seed=seed).random_base2(5)
    else:
        u=qmc.LatinHypercube(d=22,seed=seed).random(N_START)
    out=[]
    for row in u:
        g=norm.ppf(np.clip(row[:21],1e-12,1-1e-12)); ng=float(np.linalg.norm(g))
        if not np.isfinite(ng) or ng<1e-14:
            g=np.ones(21,float); ng=float(np.linalg.norm(g))
        direction=g/ng; r=float(np.clip(row[21],0.0,1.0)**(1.0/21.0))
        out.append(r*direction)
    return np.asarray(out,float)


def admissibility(z,cap):
    C=cmat(z,cap); ce=np.linalg.eigvalsh((C+C.T)/2); G=generator_from_C(C)
    trrow=I4.reshape(-1,order='F').conj(); tp=[]; cp=[]; se=[]; te=[]
    for t in TIMES:
        E=expm(G*float(t)); tp.append(float(np.linalg.norm(trrow@E-trrow))); cp.append(float(np.min(np.linalg.eigvalsh(choi(E)))))
        for rho in PROBES:
            out=map_apply(E,rho); se.append(float(np.min(np.linalg.eigvalsh((out+out.conj().T)/2)))); te.append(float(abs(np.trace(out)-1.0)))
    return {'min_kossakowski_eigenvalue':float(ce.min()),'trace_C':float(np.trace(C).real),'max_tp_residual':max(tp),'min_choi_eigenvalue':min(cp),'min_output_state_eigenvalue':min(se),'max_trace_error':max(te)}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--cap',type=float,choices=CAPS,required=True); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    scale,t0=CASES[a.shard]; theta=float(scale*t0); target=target_traj(theta)
    scored=[]
    for z0 in starts(a.method,a.shard,a.cap):
        rr=residual(z0,target,a.cap); scored.append((float(np.dot(rr,rr)),np.asarray(z0,float)))
    scored.sort(key=lambda q:q[0]); cands=[]
    for _,z0 in scored[:N_REFINE]:
        fit=least_squares(lambda z:residual(z,target,a.cap),z0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-10,xtol=1e-10,gtol=1e-10)
        gap,rn=metric(fit.x,target,a.cap)
        cands.append({'gap':gap,'residual_norm':rn,'search_coordinates':fit.x.tolist(),'search_z_norm':float(np.linalg.norm(fit.x)),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success)})
    best=min(cands,key=lambda c:(c['gap'],c['residual_norm']))
    z=np.asarray(best['search_coordinates'],float); adm=admissibility(z,a.cap)
    vals=[x for c in cands for x in (c['gap'],c['residual_norm'],c['search_z_norm'],*c['search_coordinates'])]+list(adm.values())
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)))
    admissible=bool(structural and adm['min_kossakowski_eigenvalue']>=C_FLOOR and adm['trace_C']<=a.cap+TRACE_C_TOL and adm['max_tp_residual']<TP_TOL and adm['min_choi_eigenvalue']>CHOI_FLOOR and adm['min_output_state_eigenvalue']>STATE_FLOOR and adm['max_trace_error']<TRACE_TOL)
    lane_support=bool(admissible and best['gap']>GAP_THRESHOLD)
    out={'iteration':'Iter038','gate':'G46-A','trace_cap':a.cap,'method':a.method,'shard':a.shard,'theta':theta,'best_candidate':best,'admissibility':adm,'n_refined_candidates':len(cands),'structural_valid':structural,'admissible':admissible,'lane_support':lane_support,'frozen':{'family':'C=A^2; A symmetric; tr(C)<=cap','caps':list(CAPS),'times':TIMES.tolist(),'n_probes':len(PROBES),'n_starts':N_START,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':RECOVERY_TOL,'cap_nesting_tolerance':0.002,'same_family_and_optimizer_hyperparameters_as_G46C':True,'same_RCG002_target_convention_as_G44A':True},'authorization_lock':'Production permitted only after terminal G46-C calibration PASS.','scope_lock':'Bounded basis-invariant real-PSD Markovian random-Hamiltonian trace caps 8 and 16 only; not unbounded PSD or all-classical no-go.','interpretation':'Prospective scoped adversarial toy-trajectory search only.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
