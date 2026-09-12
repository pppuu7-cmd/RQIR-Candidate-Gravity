#!/usr/bin/env python3
"""Iter032 / G44-A: prospective RCG-002 adversarial search against the
basis-invariant bounded real-PSD trace-ball tr(C)<=4 calibrated by G44-C.

PRODUCTION LAUNCH IS LOCKED UNTIL TERMINAL G44-C PASS.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
from scipy.stats import qmc,norm

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I4,Z,td,choi
from iter013_global_search_calibration import CASES,GAP_THRESHOLD,RECOVERY_TOL
from iter022b_g40c_rtn_optimizer_calibration import PROBES
from iter024a_g41p_high_rank_classical_kossakowski import map_apply
from iter025a_g42j_full_psd_kossakowski_identifiability import TIMES,generator_from_C
from iter030_g44c_trace_ball_optimizer_calibration import METHODS,RADIUS,z_to_A

ZZ=np.kron(Z,Z)
N_START=32; N_REFINE=6; MAX_NFEV=1200
TP_TOL=1e-10; CHOI_FLOOR=-1e-8; STATE_FLOOR=-1e-8; TRACE_TOL=1e-10; C_FLOOR=-1e-10; TRACE_C_TOL=1e-9
LO=-np.ones(21,float); HI=np.ones(21,float)


def cmat(z):
    A=z_to_A(z)
    return A@A


def target_traj(theta):
    out=[]
    for t in TIMES:
        a=float(theta*t); U=np.cos(a)*I4-1j*np.sin(a)*ZZ
        out.append([U@rho@U.conj().T for rho in PROBES])
    return out


def candidate_traj(z):
    G=generator_from_C(cmat(z)); out=[]
    for t in TIMES:
        E=expm(G*float(t)); out.append([map_apply(E,rho) for rho in PROBES])
    return out


def residual(z,target):
    pred=candidate_traj(z); arr=[]
    for aa,bb in zip(pred,target):
        for x,y in zip(aa,bb):
            d=x-y; arr.extend(d.real.reshape(-1)); arr.extend(d.imag.reshape(-1))
    return np.asarray(arr,float)


def metric(z,target):
    pred=candidate_traj(z)
    gaps=[td(x,y) for aa,bb in zip(pred,target) for x,y in zip(aa,bb)]
    rr=residual(z,target)
    return float(max(gaps)),float(np.linalg.norm(rr))


def starts(method,shard):
    seed=152000+100*shard+(0 if method=='sobol_lsq' else 43)
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


def admissibility(z):
    C=cmat(z); ce=np.linalg.eigvalsh((C+C.T)/2); G=generator_from_C(C)
    trrow=I4.reshape(-1,order='F').conj(); tp=[]; cp=[]; se=[]; te=[]
    for t in TIMES:
        E=expm(G*float(t)); tp.append(float(np.linalg.norm(trrow@E-trrow))); cp.append(float(np.min(np.linalg.eigvalsh(choi(E)))))
        for rho in PROBES:
            out=map_apply(E,rho); se.append(float(np.min(np.linalg.eigvalsh((out+out.conj().T)/2)))); te.append(float(abs(np.trace(out)-1.0)))
    return {'min_kossakowski_eigenvalue':float(ce.min()),'trace_C':float(np.trace(C).real),'max_tp_residual':max(tp),'min_choi_eigenvalue':min(cp),'min_output_state_eigenvalue':min(se),'max_trace_error':max(te)}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    scale,t0=CASES[a.shard]; theta=float(scale*t0); target=target_traj(theta)
    scored=[]
    for z0 in starts(a.method,a.shard):
        rr=residual(z0,target); scored.append((float(np.dot(rr,rr)),np.asarray(z0,float)))
    scored.sort(key=lambda q:q[0]); cands=[]
    for _,z0 in scored[:N_REFINE]:
        fit=least_squares(lambda z:residual(z,target),z0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-10,xtol=1e-10,gtol=1e-10)
        gap,rn=metric(fit.x,target)
        cands.append({'gap':gap,'residual_norm':rn,'search_coordinates':fit.x.tolist(),'search_z_norm':float(np.linalg.norm(fit.x)),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success)})
    best=min(cands,key=lambda c:(c['gap'],c['residual_norm']))
    z=np.asarray(best['search_coordinates'],float); adm=admissibility(z)
    vals=[x for c in cands for x in (c['gap'],c['residual_norm'],c['search_z_norm'],*c['search_coordinates'])]+list(adm.values())
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)))
    admissible=bool(structural and adm['min_kossakowski_eigenvalue']>=C_FLOOR and adm['trace_C']<=RADIUS**2+TRACE_C_TOL and adm['max_tp_residual']<TP_TOL and adm['min_choi_eigenvalue']>CHOI_FLOOR and adm['min_output_state_eigenvalue']>STATE_FLOOR and adm['max_trace_error']<TRACE_TOL)
    lane_support=bool(admissible and best['gap']>GAP_THRESHOLD)
    out={'iteration':'Iter032','gate':'G44-A','method':a.method,'shard':a.shard,'theta':theta,'best_candidate':best,'admissibility':adm,'n_refined_candidates':len(cands),'structural_valid':structural,'admissible':admissible,'lane_support':lane_support,
         'frozen':{'family':'C=A^2; A symmetric; ||A||_F<=2','trace_C_max':4.0,'times':TIMES.tolist(),'n_probes':len(PROBES),'n_starts':N_START,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':RECOVERY_TOL,'tp_tolerance':TP_TOL,'choi_floor':CHOI_FLOOR,'state_floor':STATE_FLOOR,'trace_tolerance':TRACE_TOL,'kossakowski_floor':C_FLOOR,'same_physical_family_and_search_map_as_G44C':True,'same_target_convention_as_G42A':True},
         'authorization_lock':'Production launch permitted only after terminal G44-C PASS.',
         'scope_lock':'Bounded basis-invariant real-PSD Markovian classical random-Hamiltonian trace-ball tr(C)<=4; not unbounded PSD, arbitrary non-Markovian, LOCC, semiclassical-gravity, or all-classical no-go.',
         'interpretation':'Prospective scoped adversarial toy-trajectory search only.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
