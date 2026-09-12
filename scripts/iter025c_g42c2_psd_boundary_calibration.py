#!/usr/bin/env python3
"""Iter025C / G42-C2: positive-control calibration for a boundary-capable
real-PSD 6x6 classical random-Hamiltonian Kossakowski family.

The direct nonnegative Cholesky diagonals include rank-deficient PSD boundary
points exactly. No RCG-002 target is used.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
from scipy.stats import qmc

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import td
from iter022b_g40c_rtn_optimizer_calibration import PROBES
from iter024a_g41p_high_rank_classical_kossakowski import map_apply
from iter025a_g42j_full_psd_kossakowski_identifiability import TIMES,LOWER,generator_from_C

METHODS=('sobol_lsq','lhs_lsq')
RANKS=(2,4,5,6)
N_START=32; N_REFINE=6; MAX_NFEV=1000
RECOVERY_TOL=0.002; C_REL_TOL=0.02; RANK_EIG_TOL=1e-5
LO=np.array([0.0 if i==j else -0.30 for i,j in LOWER],float)
HI=np.array([0.60 if i==j else  0.30 for i,j in LOWER],float)


def unpack(q):
    q=np.asarray(q,float); B=np.zeros((6,6),float)
    for k,(i,j) in enumerate(LOWER): B[i,j]=q[k]
    return B


def pack(B):
    return np.asarray([B[i,j] for i,j in LOWER],float)


def cmat(q):
    B=unpack(q); return B@B.T


def hidden_q(shard):
    rank=RANKS[shard]; rng=np.random.default_rng(98000+shard)
    B=np.zeros((6,6),float)
    for j in range(rank):
        B[j,j]=0.18+0.025*j+0.01*shard
        for i in range(j+1,6):
            B[i,j]=float(rng.uniform(-0.07,0.07))
    return pack(B)


def trajectory(q):
    G=generator_from_C(cmat(q)); out=[]
    for t in TIMES:
        E=expm(G*float(t)); out.append([map_apply(E,rho) for rho in PROBES])
    return out


def residual(q,target):
    pred=trajectory(q); arr=[]
    for aa,bb in zip(pred,target):
        for x,y in zip(aa,bb):
            d=x-y; arr.extend(d.real.reshape(-1)); arr.extend(d.imag.reshape(-1))
    return np.asarray(arr,float)


def diagnostics(q,target,C_hidden):
    pred=trajectory(q); gaps=[td(x,y) for aa,bb in zip(pred,target) for x,y in zip(aa,bb)]
    rr=residual(q,target); C=cmat(q); eig=np.linalg.eigvalsh(C)
    rel=float(np.linalg.norm(C-C_hidden)/max(np.linalg.norm(C_hidden),1e-15))
    rank=int(np.sum(eig>RANK_EIG_TOL))
    return float(max(gaps)),float(np.linalg.norm(rr)),rel,rank,float(eig.min())


def starts(method,shard):
    seed=99000+100*shard+(0 if method=='sobol_lsq' else 43)
    if method=='sobol_lsq': u=qmc.Sobol(d=21,scramble=True,seed=seed).random_base2(5)
    else: u=qmc.LatinHypercube(d=21,seed=seed).random(N_START)
    return LO+u*(HI-LO)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    intended=RANKS[a.shard]; hidden=hidden_q(a.shard); C_hidden=cmat(hidden); hidden_eig=np.linalg.eigvalsh(C_hidden); hidden_rank=int(np.sum(hidden_eig>1e-10)); target=trajectory(hidden)
    scored=[]
    for q0 in starts(a.method,a.shard):
        r=residual(q0,target); scored.append((float(np.dot(r,r)),np.asarray(q0,float)))
    scored.sort(key=lambda z:z[0]); cands=[]
    for _,q0 in scored[:N_REFINE]:
        fit=least_squares(lambda q:residual(q,target),q0,bounds=(LO,HI),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-10,xtol=1e-10,gtol=1e-10)
        gap,rn,crel,rrank,mineig=diagnostics(fit.x,target,C_hidden)
        cands.append({'gap':gap,'residual_norm':rn,'relative_kossakowski_error':crel,'recovered_effective_rank':rrank,'min_kossakowski_eigenvalue':mineig,'nfev':int(fit.nfev),'optimizer_success_flag':bool(fit.success)})
    best=min(cands,key=lambda c:(c['gap'],c['relative_kossakowski_error'],c['residual_norm']))
    vals=[x for c in cands for x in (c['gap'],c['residual_norm'],c['relative_kossakowski_error'],c['min_kossakowski_eigenvalue'])]
    structural=bool(len(cands)==N_REFINE and np.all(np.isfinite(vals)) and hidden_rank==intended and hidden_eig.min()>-1e-12)
    support=bool(structural and best['gap']<RECOVERY_TOL and best['relative_kossakowski_error']<C_REL_TOL and best['recovered_effective_rank']==intended and best['min_kossakowski_eigenvalue']>-1e-10)
    out={'iteration':'Iter025C','gate':'G42-C2','method':a.method,'shard':a.shard,'intended_hidden_rank':intended,'hidden_rank_1e-10':hidden_rank,
         'hidden_min_kossakowski_eigenvalue':float(hidden_eig.min()),'best_candidate':best,'n_refined_candidates':len(cands),
         'structural_valid':structural,'scientific_support':support,
         'frozen':{'diag_bounds':[0.0,0.60],'offdiag_bounds':[-0.30,0.30],'times':TIMES.tolist(),'n_probes':len(PROBES),'n_starts':N_START,'n_refine':N_REFINE,'max_nfev':MAX_NFEV,'trace_recovery_tolerance':RECOVERY_TOL,'relative_kossakowski_tolerance':C_REL_TOL,'rank_eigenvalue_threshold':RANK_EIG_TOL,'hidden_coordinates_used_as_starts':False,'RCG002_target_used':False},
         'scope_lock':'Boundary-capable bounded real-PSD 6x6 classical random-Hamiltonian Kossakowski calibration with rank-2/4/5/6 positive controls.',
         'interpretation':'Positive-control boundary calibration only. PASS may authorize only a separately preregistered adversarial gate with identical PSD coordinates/search rules.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
