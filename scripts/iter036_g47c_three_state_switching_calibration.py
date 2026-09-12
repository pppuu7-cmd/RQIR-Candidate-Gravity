#!/usr/bin/env python3
"""Iter036 / G47-C: response-blind optimizer calibration for explicit 3-state classical switching."""
import argparse, json, sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.stats import qmc

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter011_robustness_suite import td
from iter035_g47p_three_state_classical_switching_provenance import (
    h2, stationary, block_generator, visible_superop, product_states, apply_map, choi, I2
)

TIMES=(0.15,0.45,0.9,1.4)
HOLDOUT=(0.27,0.67,1.17)
RATE_LO,RATE_HI=0.015,0.14
SCALE_LO,SCALE_HI=0.55,1.45
LO=np.array([RATE_LO]*6+[SCALE_LO]*6,float)
HI=np.array([RATE_HI]*6+[SCALE_HI]*6,float)
N_START=16
N_REFINE=4
MAX_NFEV=500
TRAIN_TOL=0.002
HOLDOUT_TOL=0.003
PARAM_TOL=0.08
TP_TOL=1e-10
CHOI_FLOOR=-1e-8
METHODS=('sobol_lsq','lhs_lsq')
PROBES=product_states()

A_DIRS=np.array([[0.62,0.08,0.03],[0.04,0.79,-0.11],[0.18,-0.05,0.93]],float)
B_DIRS=np.array([[-0.31,0.51,0.07],[0.57,-0.16,0.12],[-0.09,0.23,-0.72]],float)
A_DIRS=A_DIRS/np.linalg.norm(A_DIRS,axis=1)[:,None]
B_DIRS=B_DIRS/np.linalg.norm(B_DIRS,axis=1)[:,None]
RATE_POS=((1,0),(2,0),(0,1),(2,1),(0,2),(1,2))


def hidden_params(control):
    rng=np.random.default_rng(1701+int(control))
    u=rng.uniform(0.24,0.76,size=12)
    return LO+(HI-LO)*u


def build(theta):
    x=np.asarray(theta,float)
    Q=np.zeros((3,3),float)
    for val,(i,j) in zip(x[:6],RATE_POS): Q[i,j]=float(val)
    for j in range(3): Q[j,j]=-float(np.sum(Q[:,j]))
    a=[x[6+j]*A_DIRS[j] for j in range(3)]
    b=[x[9+j]*B_DIRS[j] for j in range(3)]
    Hs=[np.kron(h2(a[j]),I2)+np.kron(I2,h2(b[j])) for j in range(3)]
    pi=stationary(Q)
    B=block_generator(Q,Hs)
    return Q,pi,B


def superops(theta,times):
    _,pi,B=build(theta)
    return [visible_superop(B,pi,t) for t in times]


def residual(theta,target):
    pred=superops(theta,TIMES)
    out=[]
    # Compact tomography objective on the full visible superoperator.
    for E,T in zip(pred,target):
        d=E-T
        out.extend(d.real.reshape(-1))
        out.extend(d.imag.reshape(-1))
    return np.asarray(out,float)


def max_probe_gap(theta,target_theta,times):
    p=superops(theta,times); q=superops(target_theta,times)
    g=0.0
    for E,T in zip(p,q):
        for rho in PROBES:
            g=max(g,td(apply_map(E,rho),apply_map(T,rho)))
    return float(g)


def provenance(theta):
    Q,pi,B=build(theta)
    off=[Q[i,j] for i,j in RATE_POS]
    col=float(np.max(np.abs(np.sum(Q,axis=0))))
    stat=float(np.linalg.norm(Q@pi))
    pinorm=float(abs(np.sum(pi)-1.0))
    tvec=np.eye(4,dtype=complex).reshape(-1,order='F').conj()
    max_tp=0.0; min_ch=1e9
    vals=[*theta,*off,col,stat,pinorm,*pi]
    for t in TIMES:
        E=visible_superop(B,pi,t)
        max_tp=max(max_tp,float(np.linalg.norm(tvec@E-tvec)))
        min_ch=min(min_ch,float(np.min(np.linalg.eigvalsh(choi(E))).real))
    vals += [max_tp,min_ch]
    valid=bool(np.all(np.isfinite(vals)) and min(off)>=-1e-12 and col<=1e-12 and min(pi)>=-1e-12 and pinorm<=1e-12 and stat<=1e-10 and max_tp<=TP_TOL and min_ch>=CHOI_FLOOR)
    return valid, {'min_offdiag_rate':float(min(off)),'max_Q_column_sum_residual':col,'stationary_residual':stat,'stationary_normalization_error':pinorm,'min_stationary_probability':float(min(pi)),'max_tp_residual':max_tp,'min_choi_eigenvalue':min_ch}


def starts(method,control):
    seed=18000+100*control+(0 if method=='sobol_lsq' else 7)
    if method=='sobol_lsq':
        u=qmc.Sobol(d=12,scramble=True,seed=seed).random_base2(4)
    else:
        u=qmc.LatinHypercube(d=12,seed=seed).random(N_START)
    return LO+(HI-LO)*u


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--method',choices=METHODS,required=True)
    ap.add_argument('--control',type=int,choices=range(4),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    hidden=hidden_params(a.control)
    target=superops(hidden,TIMES)
    scored=[]
    for x0 in starts(a.method,a.control):
        r=residual(x0,target); scored.append((float(np.dot(r,r)),x0))
    scored.sort(key=lambda z:z[0])
    cands=[]
    for _,x0 in scored[:N_REFINE]:
        fit=least_squares(lambda x: residual(x,target),x0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-9,xtol=1e-9,gtol=1e-9)
        train=max_probe_gap(fit.x,hidden,TIMES)
        hold=max_probe_gap(fit.x,hidden,HOLDOUT)
        perr=float(np.linalg.norm((fit.x-hidden)/(HI-LO))/np.sqrt(12.0))
        prov,pdiag=provenance(fit.x)
        cands.append({'train_max_trace_gap':train,'holdout_max_trace_gap':hold,'normalized_parameter_error':perr,'residual_norm':float(np.linalg.norm(residual(fit.x,target))),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success),'provenance_valid':prov,'provenance':pdiag})
    best=min(cands,key=lambda c:(c['train_max_trace_gap'],c['holdout_max_trace_gap'],c['normalized_parameter_error']))
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite([v for c in cands for v in (c['train_max_trace_gap'],c['holdout_max_trace_gap'],c['normalized_parameter_error'],c['residual_norm'])])))
    support=bool(structural and best['provenance_valid'] and best['train_max_trace_gap']<TRAIN_TOL and best['holdout_max_trace_gap']<HOLDOUT_TOL and best['normalized_parameter_error']<PARAM_TOL)
    out={'iteration':'Iter036','gate':'G47-C','method':a.method,'control':a.control,'best_candidate':best,'n_refined_candidates':len(cands),'structural_valid':structural,'scientific_support':support,'classification':'THREE_STATE_CLASSICAL_SWITCHING_CALIBRATION_LANE_PASS' if support else 'THREE_STATE_CLASSICAL_SWITCHING_CALIBRATION_LANE_NOT_ESTABLISHED','frozen':{'dimension':12,'rate_bounds':[RATE_LO,RATE_HI],'field_scale_bounds':[SCALE_LO,SCALE_HI],'times':list(TIMES),'holdout_times':list(HOLDOUT),'n_starts':N_START,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'train_trace_gap_tolerance':TRAIN_TOL,'holdout_trace_gap_tolerance':HOLDOUT_TOL,'normalized_parameter_error_tolerance':PARAM_TOL,'hidden_parameters_used_as_starts':False,'RCG002_target_used':False},'scope_lock':'Response-blind optimizer calibration only for the explicit finite 12D three-state hidden-classical switching family.','interpretation':'Calibration only; no readiness increment or comparator-separation claim.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)

if __name__=='__main__': main()
