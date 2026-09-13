#!/usr/bin/env python3
"""Iter042/G49-A: preregistered cap-free direct-PSD RCG-002 adversarial transport."""
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
from iter034_g46c_extended_trace_ball_calibration import weighted_unpack

BOX=8.0
N_START=32
N_REFINE=6
MAX_NFEV=1200
LO=-BOX*np.ones(21,float)
HI=BOX*np.ones(21,float)


def cmat(w):
    A=weighted_unpack(np.asarray(w,float))
    return A@A


def candidate_traj(w):
    G=generator_from_C(cmat(w)); out=[]
    for t in TIMES:
        E=expm(G*float(t)); out.append([map_apply(E,rho) for rho in PROBES])
    return out


def residual(w,target):
    pred=candidate_traj(w); arr=[]
    for aa,bb in zip(pred,target):
        for x,y in zip(aa,bb):
            d=x-y; arr.extend(d.real.reshape(-1)); arr.extend(d.imag.reshape(-1))
    return np.asarray(arr,float)


def metric(w,target):
    pred=candidate_traj(w)
    gaps=[td(x,y) for aa,bb in zip(pred,target) for x,y in zip(aa,bb)]
    return float(max(gaps)),float(np.linalg.norm(residual(w,target)))


def starts(method,shard):
    seed=249000+100*int(shard)+(0 if method=='sobol_lsq' else 29)
    if method=='sobol_lsq':
        u=qmc.Sobol(d=21,scramble=True,seed=seed).random_base2(5)
    else:
        u=qmc.LatinHypercube(d=21,seed=seed).random(N_START)
    g=norm.ppf(np.clip(u,1e-12,1-1e-12))
    scale=1.5/np.maximum(np.linalg.norm(g,axis=1,keepdims=True),1e-15)
    return g*scale


def physicality(C):
    ce=np.linalg.eigvalsh((C+C.T)/2); G=generator_from_C(C)
    trrow=I4.reshape(-1,order='F').conj(); tp=[]; cp=[]; se=[]; te=[]
    for t in TIMES:
        E=expm(G*float(t))
        tp.append(float(np.linalg.norm(trrow@E-trrow)))
        cp.append(float(np.min(np.linalg.eigvalsh(choi(E)))))
        for rho in PROBES:
            out=map_apply(E,rho)
            se.append(float(np.min(np.linalg.eigvalsh((out+out.conj().T)/2))))
            te.append(float(abs(np.trace(out)-1.0)))
    return {
        'min_kossakowski_eigenvalue':float(ce.min()),
        'trace_C':float(np.trace(C).real),
        'max_tp_residual':max(tp),
        'min_choi_eigenvalue':min(cp),
        'min_output_state_eigenvalue':min(se),
        'max_trace_error':max(te)
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--method',choices=METHODS,required=True)
    ap.add_argument('--shard',type=int,choices=range(4),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()

    scale,t0=CASES[a.shard]
    theta=float(scale*t0)
    target=target_traj(theta)
    scored=[]
    for w0 in starts(a.method,a.shard):
        rr=residual(w0,target)
        scored.append((float(rr@rr),np.asarray(w0,float)))
    scored.sort(key=lambda x:x[0])

    cands=[]
    for _,w0 in scored[:N_REFINE]:
        fit=least_squares(lambda w:residual(w,target),w0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-10,xtol=1e-10,gtol=1e-10)
        gap,rn=metric(fit.x,target)
        C=cmat(fit.x); phy=physicality(C)
        cands.append({
            'gap':gap,
            'residual_norm':rn,
            'w':fit.x.tolist(),
            'box_fraction':float(np.max(np.abs(fit.x))/BOX),
            'trace_C':float(np.trace(C).real),
            'nfev':int(fit.nfev),
            'optimizer_success_flag':bool(fit.success),
            'physicality':phy
        })

    best=min(cands,key=lambda c:(c['gap'],c['residual_norm']))
    p=best['physicality']
    vals=[v for c in cands for v in (c['gap'],c['residual_norm'],c['box_fraction'],c['trace_C'],*c['w'])]+list(p.values())
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)))
    admissible=bool(
        structural and best['box_fraction']<0.80 and
        p['min_kossakowski_eigenvalue']>=-1e-10 and
        p['max_tp_residual']<1e-10 and
        p['min_choi_eigenvalue']>-1e-8 and
        p['min_output_state_eigenvalue']>-1e-8 and
        p['max_trace_error']<1e-10
    )
    lane_support=bool(admissible and best['gap']>GAP_THRESHOLD)

    out={
        'iteration':'Iter042','gate':'G49-A','method':a.method,'shard':a.shard,'theta':theta,
        'best_candidate':best,'n_refined_candidates':len(cands),
        'structural_valid':structural,'admissible':admissible,'lane_support':lane_support,
        'classification':'CAPFREE_DIRECT_PSD_RCG002_LANE_SUPPORT' if lane_support else 'CAPFREE_DIRECT_PSD_RCG002_LANE_NOT_ESTABLISHED',
        'frozen':{
            'family':'C=A^2, A real symmetric, direct weighted physical-scale coordinates, no trace cap',
            'numerical_box':BOX,'box_inactivity_fraction':0.80,
            'times':TIMES.tolist(),'n_probes':len(PROBES),
            'n_starts':N_START,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,
            'nonzero_gap':GAP_THRESHOLD,'cross_method_agreement':RECOVERY_TOL,
            'cap64_consistency_tolerance':0.002,
            'same_RCG002_target_convention_as_G48A':True,
            'same_direct_parameterization_and_optimizer_budget_as_G49C':True
        },
        'scope_lock':'Frozen four-shard RCG-002 toy target and calibrated direct real-PSD Markovian comparator only; not a mathematical unbounded-PSD theorem or universal no-go.',
        'interpretation':'Prospective scoped numerical adversarial transport only.'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    if not structural:
        raise SystemExit(2)

if __name__=='__main__':
    main()
