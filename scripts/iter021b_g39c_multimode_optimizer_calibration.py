#!/usr/bin/env python3
"""Iter021B / G39-C: prospective positive-control optimizer calibration for
finite rank-2/rank-3 multimode shared-classical-noise Markovian comparators.

For K modes:
    L = sum_k kappa_k D[F_k],
    F_k = cA_k A_k⊗I + cB_k I⊗B_k,
with kappa_k in [0,1.2]. Zero rate is included exactly, so rank K contains the
lower-rank boundary. Hidden source coordinates are never optimizer starts.

Two independent designs (scrambled Sobol and Latin hypercube) score 64 starts
and refine the best 12 with bounded least-squares on a smooth density-matrix
residual. Final authority remains trace distance < 0.002.
"""
import argparse,json,math,sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.stats import qmc

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I2,axis,op,evolve,td
from iter018a_correlated_classical_noise_validation import d_super

METHODS=('sobol_lsq','lhs_lsq')
RECOVERY_TOL=2e-3
N_STARTS=64
N_REFINE=12
MAX_NFEV=1200


def dim(K): return 7*K

def decode_unit(u,K):
    u=np.asarray(u,float)
    if u.shape!=(dim(K),): raise ValueError('wrong multimode dimension')
    modes=[]
    for k in range(K):
        z=u[7*k:7*(k+1)]
        aaz=-math.pi+2*math.pi*z[0]; apol=0.10+(math.pi-0.20)*z[1]
        baz=-math.pi+2*math.pi*z[2]; bpol=0.10+(math.pi-0.20)*z[3]
        cA=-1.8+3.6*z[4]; cB=-1.8+3.6*z[5]; rate=1.2*z[6]
        A=op(axis(aaz,apol)); B=op(axis(baz,bpol)); F=cA*np.kron(A,I2)+cB*np.kron(I2,B)
        modes.append((float(rate),F))
    return modes

def generator_u(u,K):
    L=np.zeros((16,16),complex)
    for rate,F in decode_unit(u,K): L += rate*d_super(F)
    return L

def state_u(u,K): return evolve(generator_u(u,K))
def residual(u,K,tar):
    d=state_u(u,K)-tar
    return np.concatenate((d.real.ravel(),d.imag.ravel()))

def hidden_unit(K,shard):
    rng=np.random.default_rng(43000+100*K+shard); u=rng.uniform(0.08,0.92,size=dim(K)); label='interior'
    if shard==2:
        # Prospectively fixed lower-rank exact boundary.
        u[7*(K-1)+6]=0.0; label=f'exact_rank_{K-1}_boundary'
    elif shard==3:
        # Strong multi-axis dissipative control.
        for k in range(K): u[7*k+6]=0.82-0.12*k/max(1,K-1)
        label='strong_multimode'
    return u,label

def design(method,K,shard):
    seed=44000+1000*K+100*shard+(0 if method=='sobol_lsq' else 1)
    if method=='sobol_lsq': return qmc.Sobol(d=dim(K),scramble=True,seed=seed).random_base2(m=6)
    return qmc.LatinHypercube(d=dim(K),seed=seed).random(N_STARTS)

def optimize(method,K,shard,tar):
    scored=[]
    for u in design(method,K,shard):
        r=residual(u,K,tar); scored.append((float(np.dot(r,r)),u))
    scored.sort(key=lambda x:x[0]); best=None
    for _,u0 in scored[:N_REFINE]:
        fit=least_squares(lambda z:residual(z,K,tar),u0,bounds=(0,1),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-11,xtol=1e-11,gtol=1e-11)
        gap=float(td(state_u(fit.x,K),tar)); rn=float(np.linalg.norm(fit.fun)); cand=(gap,rn,int(fit.nfev),bool(fit.success))
        if best is None or (gap,rn)<(best[0],best[1]): best=cand
    return best

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--rank',type=int,choices=[2,3],required=True); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    hu,label=hidden_unit(a.rank,a.shard); tar=state_u(hu,a.rank); gap,rn,nfev,ok=optimize(a.method,a.rank,a.shard,tar); valid=bool(np.isfinite(gap) and np.isfinite(rn)); support=bool(valid and gap<RECOVERY_TOL)
    out={'iteration':'Iter021B','gate':'G39-C','rank':a.rank,'method':a.method,'shard':a.shard,'result':{'best_trace_gap':gap,'residual_norm':rn,'nfev':nfev,'optimizer_success_flag':ok,'scientific_support':support},'hidden_target_metadata':{'control_type':label,'hidden_coordinates_not_used_as_starts':True},'structural_valid':valid,'frozen_thresholds':{'recovery_trace_distance':RECOVERY_TOL,'n_starts':N_STARTS,'n_refine':N_REFINE,'max_nfev':MAX_NFEV},'scope_lock':'Finite rank-2/rank-3 multimode shared classical white-noise family with positive rates, arbitrary local Pauli axes, and exact zero-rate lower-rank boundaries.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not valid: raise SystemExit(2)
if __name__=='__main__': main()
