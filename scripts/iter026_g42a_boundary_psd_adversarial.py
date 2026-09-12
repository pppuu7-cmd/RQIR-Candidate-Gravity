#!/usr/bin/env python3
"""Iter026 / G42-A: prospective RCG-002 adversarial search against the
boundary-capable bounded real-PSD 6x6 classical random-Hamiltonian
Kossakowski family calibrated by G42-C2/C3.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
from scipy.stats import qmc

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I4,Z,td,choi
from iter013_global_search_calibration import CASES,GAP_THRESHOLD,RECOVERY_TOL
from iter022b_g40c_rtn_optimizer_calibration import PROBES
from iter024a_g41p_high_rank_classical_kossakowski import map_apply
from iter025a_g42j_full_psd_kossakowski_identifiability import TIMES,generator_from_C
from iter025c_g42c2_psd_boundary_calibration import METHODS,LO,HI,cmat

ZZ=np.kron(Z,Z)
N_START=32; N_REFINE=6; MAX_NFEV=1000
TP_TOL=1e-10; CHOI_FLOOR=-1e-8; STATE_FLOOR=-1e-8; TRACE_TOL=1e-10; C_FLOOR=-1e-10


def target_traj(theta):
    out=[]
    for t in TIMES:
        a=float(theta*t); U=np.cos(a)*I4-1j*np.sin(a)*ZZ
        out.append([U@rho@U.conj().T for rho in PROBES])
    return out


def candidate_traj(q):
    G=generator_from_C(cmat(q)); out=[]
    for t in TIMES:
        E=expm(G*float(t)); out.append([map_apply(E,rho) for rho in PROBES])
    return out


def residual(q,target):
    pred=candidate_traj(q); arr=[]
    for aa,bb in zip(pred,target):
        for x,y in zip(aa,bb):
            d=x-y; arr.extend(d.real.reshape(-1)); arr.extend(d.imag.reshape(-1))
    return np.asarray(arr,float)


def metric(q,target):
    pred=candidate_traj(q)
    gaps=[td(x,y) for aa,bb in zip(pred,target) for x,y in zip(aa,bb)]
    rr=residual(q,target)
    return float(max(gaps)),float(np.linalg.norm(rr))


def starts(method,shard):
    seed=106000+100*shard+(0 if method=='sobol_lsq' else 47)
    if method=='sobol_lsq':
        u=qmc.Sobol(d=21,scramble=True,seed=seed).random_base2(5)
    else:
        u=qmc.LatinHypercube(d=21,seed=seed).random(N_START)
    return LO+u*(HI-LO)


def admissibility(q):
    C=cmat(q); ce=np.linalg.eigvalsh(C); G=generator_from_C(C)
    trrow=I4.reshape(-1,order='F').conj(); tp=[]; cp=[]; se=[]; te=[]
    for t in TIMES:
        E=expm(G*float(t)); tp.append(float(np.linalg.norm(trrow@E-trrow))); cp.append(float(np.min(np.linalg.eigvalsh(choi(E)))))
        for rho in PROBES:
            out=map_apply(E,rho); se.append(float(np.min(np.linalg.eigvalsh((out+out.conj().T)/2)))); te.append(float(abs(np.trace(out)-1.0)))
    return {'min_kossakowski_eigenvalue':float(ce.min()),'max_tp_residual':max(tp),'min_choi_eigenvalue':min(cp),'min_output_state_eigenvalue':min(se),'max_trace_error':max(te)}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    scale,t0=CASES[a.shard]; theta=float(scale*t0); target=target_traj(theta)
    scored=[]
    for q0 in starts(a.method,a.shard):
        rr=residual(q0,target); scored.append((float(np.dot(rr,rr)),np.asarray(q0,float)))
    scored.sort(key=lambda z:z[0]); cands=[]
    for _,q0 in scored[:N_REFINE]:
        fit=least_squares(lambda q:residual(q,target),q0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-10,xtol=1e-10,gtol=1e-10)
        gap,rn=metric(fit.x,target)
        cands.append({'gap':gap,'residual_norm':rn,'coordinates':fit.x.tolist(),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success)})
    best=min(cands,key=lambda c:(c['gap'],c['residual_norm']))
    adm=admissibility(np.asarray(best['coordinates'],float))
    vals=[x for c in cands for x in (c['gap'],c['residual_norm'],*c['coordinates'])]+list(adm.values())
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)))
    admissible=bool(structural and adm['min_kossakowski_eigenvalue']>=C_FLOOR and adm['max_tp_residual']<TP_TOL and adm['min_choi_eigenvalue']>CHOI_FLOOR and adm['min_output_state_eigenvalue']>STATE_FLOOR and adm['max_trace_error']<TRACE_TOL)
    lane_support=bool(admissible and best['gap']>GAP_THRESHOLD)
    out={'iteration':'Iter026','gate':'G42-A','method':a.method,'shard':a.shard,'theta':theta,'best_candidate':best,'admissibility':adm,'n_refined_candidates':len(cands),'structural_valid':structural,'admissible':admissible,'lane_support':lane_support,
         'frozen':{'diag_bounds':[0.0,0.60],'offdiag_bounds':[-0.30,0.30],'times':TIMES.tolist(),'n_probes':len(PROBES),'n_starts':N_START,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':RECOVERY_TOL,'tp_tolerance':TP_TOL,'choi_floor':CHOI_FLOOR,'state_floor':STATE_FLOOR,'trace_tolerance':TRACE_TOL,'kossakowski_floor':C_FLOOR,'same_coordinate_family_as_G42C2C3':True},
         'scope_lock':'Bounded 21-coordinate real-PSD 6x6 Markovian classical random-Hamiltonian Kossakowski family; not an unbounded PSD, arbitrary non-Markovian, LOCC, semiclassical-gravity, or all-classical no-go.',
         'interpretation':'Prospective scoped adversarial toy-trajectory search only.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
