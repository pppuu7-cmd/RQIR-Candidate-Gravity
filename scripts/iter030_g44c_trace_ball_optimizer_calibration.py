#!/usr/bin/env python3
"""Iter030 / G44-C: positive-control optimizer calibration for the
basis-invariant PSD trace-ball C=A^2, A symmetric, ||A||_F<=2.

PRODUCTION LAUNCH IS LOCKED UNTIL TERMINAL G44-P PASS.
No RCG-002 target/result is used.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
from scipy.stats import qmc,norm

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import td
from iter022b_g40c_rtn_optimizer_calibration import PROBES
from iter024a_g41p_high_rank_classical_kossakowski import map_apply
from iter025a_g42j_full_psd_kossakowski_identifiability import TIMES,generator_from_C

METHODS=('sobol_lsq','lhs_lsq')
RADIUS=2.0
TARGET_NORMS=(0.75,1.05,1.30,1.55,1.80,2.00)
N_START=32; N_REFINE=6; MAX_NFEV=1200
RECOVERY_TOL=0.002; C_REL_TOL=0.02; RANK_EIG_TOL=1e-5
C_FLOOR=-1e-10; TRACE_TOL=1e-9
LOWER=[(i,j) for i in range(6) for j in range(i+1)]
WEIGHTS=np.asarray([1.0 if i==j else np.sqrt(2.0) for i,j in LOWER],float)
LO=-np.ones(21,float); HI=np.ones(21,float)


def weighted_pack(A):
    return np.asarray([A[i,j]*(1.0 if i==j else np.sqrt(2.0)) for i,j in LOWER],float)


def weighted_unpack(w):
    A=np.zeros((6,6),float)
    for k,(i,j) in enumerate(LOWER):
        v=float(w[k]/(1.0 if i==j else np.sqrt(2.0)))
        A[i,j]=v; A[j,i]=v
    return A


def z_to_A(z):
    z=np.asarray(z,float)
    n=float(np.linalg.norm(z))
    w=RADIUS*z/max(1.0,n)
    return weighted_unpack(w)


def cmat(z):
    A=z_to_A(z)
    return A@A


def hidden_A(rank):
    rng=np.random.default_rng(150000+rank)
    M=rng.normal(size=(6,rank)); Q,_=np.linalg.qr(M); Q=Q[:,:rank]
    ev=np.linspace(1.0,1.0+0.22*(rank-1),rank)
    ev=ev/np.linalg.norm(ev)*TARGET_NORMS[rank-1]
    A=Q@np.diag(ev)@Q.T
    return (A+A.T)/2


def hidden_z(rank):
    A=hidden_A(rank); w=weighted_pack(A)
    return w/RADIUS


def trajectory(z):
    G=generator_from_C(cmat(z)); out=[]
    for t in TIMES:
        E=expm(G*float(t)); out.append([map_apply(E,rho) for rho in PROBES])
    return out


def residual(z,target):
    pred=trajectory(z); arr=[]
    for aa,bb in zip(pred,target):
        for x,y in zip(aa,bb):
            d=x-y; arr.extend(d.real.reshape(-1)); arr.extend(d.imag.reshape(-1))
    return np.asarray(arr,float)


def diagnostics(z,target,C_hidden):
    pred=trajectory(z)
    gaps=[td(x,y) for aa,bb in zip(pred,target) for x,y in zip(aa,bb)]
    rr=residual(z,target); C=cmat(z); eig=np.linalg.eigvalsh((C+C.T)/2)
    rel=float(np.linalg.norm(C-C_hidden)/max(np.linalg.norm(C_hidden),1e-15))
    rank=int(np.sum(eig>RANK_EIG_TOL))
    trc=float(np.trace(C).real)
    return float(max(gaps)),float(np.linalg.norm(rr)),rel,rank,float(eig.min()),trc


def qmc_starts(method,rank):
    seed=151000+100*rank+(0 if method=='sobol_lsq' else 41)
    if method=='sobol_lsq':
        u=qmc.Sobol(d=22,scramble=True,seed=seed).random_base2(5)
    else:
        u=qmc.LatinHypercube(d=22,seed=seed).random(N_START)
    out=[]
    for row in u:
        # Gaussian direction from first 21 coordinates, radial CDF in 22nd.
        g=norm.ppf(np.clip(row[:21],1e-12,1-1e-12))
        ng=float(np.linalg.norm(g))
        if not np.isfinite(ng) or ng<1e-14:
            g=np.ones(21,float); ng=float(np.linalg.norm(g))
        direction=g/ng
        r=float(np.clip(row[21],0.0,1.0)**(1.0/21.0))
        out.append(r*direction)
    return np.asarray(out,float)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--method',choices=METHODS,required=True)
    ap.add_argument('--rank',type=int,choices=range(1,7),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()

    hidden=hidden_z(a.rank); Ah=hidden_A(a.rank); C_hidden=Ah@Ah
    he=np.linalg.eigvalsh((C_hidden+C_hidden.T)/2); hidden_rank=int(np.sum(he>1e-10))
    hidden_norm=float(np.linalg.norm(Ah,'fro')); target=trajectory(hidden)

    scored=[]
    for z0 in qmc_starts(a.method,a.rank):
        r=residual(z0,target); scored.append((float(np.dot(r,r)),np.asarray(z0,float)))
    scored.sort(key=lambda x:x[0]); cands=[]
    for _,z0 in scored[:N_REFINE]:
        fit=least_squares(lambda z:residual(z,target),z0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-10,xtol=1e-10,gtol=1e-10)
        gap,rn,crel,rrank,mineig,trc=diagnostics(fit.x,target,C_hidden)
        cands.append({'gap':gap,'residual_norm':rn,'relative_kossakowski_error':crel,'recovered_effective_rank':rrank,'min_kossakowski_eigenvalue':mineig,'trace_C':trc,'search_z_norm':float(np.linalg.norm(fit.x)),'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success)})
    best=min(cands,key=lambda c:(c['gap'],c['relative_kossakowski_error'],c['residual_norm']))
    vals=[hidden_norm,*he]
    for c in cands: vals += [c['gap'],c['residual_norm'],c['relative_kossakowski_error'],c['min_kossakowski_eigenvalue'],c['trace_C'],c['search_z_norm']]
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)) and hidden_rank==a.rank and he.min()>-1e-12 and hidden_norm<=RADIUS+1e-12)
    support=bool(structural and best['gap']<RECOVERY_TOL and best['relative_kossakowski_error']<C_REL_TOL and best['recovered_effective_rank']==a.rank and best['min_kossakowski_eigenvalue']>=C_FLOOR and best['trace_C']<=RADIUS**2+TRACE_TOL)

    out={'iteration':'Iter030','gate':'G44-C','method':a.method,'rank':a.rank,
         'hidden':{'effective_rank':hidden_rank,'sqrt_frobenius_norm':hidden_norm,'trace_C':float(np.trace(C_hidden)),'min_C_eigenvalue':float(he.min()),'radial_boundary_control':bool(abs(hidden_norm-RADIUS)<1e-12)},
         'best_candidate':best,'n_refined_candidates':len(cands),'structural_valid':structural,'scientific_support':support,
         'classification':'BASIS_INVARIANT_TRACE_BALL_PSD_CALIBRATION_LANE_PASS' if support else 'TRACE_BALL_PSD_CALIBRATION_LANE_NOT_ESTABLISHED',
         'frozen':{'family':'C=A^2; A symmetric; ||A||_F<=2','trace_C_max':4.0,'target_sqrt_norms':list(TARGET_NORMS),'times':TIMES.tolist(),'n_probes':len(PROBES),'n_starts':N_START,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'trace_recovery_tolerance':RECOVERY_TOL,'relative_kossakowski_tolerance':C_REL_TOL,'rank_eigenvalue_threshold':RANK_EIG_TOL,'hidden_coordinates_used_as_starts':False,'RCG002_target_used':False},
         'authorization_lock':'Production launch permitted only after terminal G44-P PASS.',
         'scope_lock':'Optimizer calibration for the bounded basis-invariant real-PSD trace-ball tr(C)<=4 only.',
         'interpretation':'Positive-control calibration only. PASS cannot raise readiness; may authorize only separately preregistered prospective G44-A.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)

if __name__=='__main__': main()
