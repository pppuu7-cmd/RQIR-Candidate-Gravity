#!/usr/bin/env python3
"""Iter019A / G37-C: prospective positive-control calibration for a broader
combined classical comparator: calibrated K=2 measurement-feedback GKSL plus
validated shared Gaussian classical Hamiltonian noise.

This is an in-family calibration gate only. Hidden source coordinates are not
optimizer starts. Two independent low-discrepancy/design constructions feed
bounded least-squares. Final authority is trace distance <2e-3 on every frozen
positive control. Separate admissibility lanes audit TP/CP/PSD/trace.

PASS authorizes a later combined-family RCG-002 adversarial gate; it does not
prejudge that gate and does not authorize a general classical/semiclassical no-go.
"""
import argparse, json, math, sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.stats import qmc

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES, RECOVERY_TOL, decode, multi_L
from iter016_calibrated_multichannel_comparator import unit_to_native
from iter018b_g36c_shared_noise_optimizer_calibration import decode_unit as decode_shared
from iter018a_correlated_classical_noise_validation import d_super
from iter011_robustness_suite import I2,I4,axis,op,evolve,td,exp_super,choi

METHODS=('sobol_lsq','lhs_lsq')
N_STARTS=128
N_REFINE=16
MAX_NFEV=1000
TP_TOL=1e-10
CHOI_TOL=-1e-8
PSD_TOL=-1e-8
TRACE_TOL=1e-10


def generator_from_unit(u,theta):
    u=np.asarray(u,float)
    if u.shape!=(18,): raise ValueError('combined unit vector must have 18 coordinates')
    xm=unit_to_native(u[:11],2)
    L=multi_L(theta,decode(xm,2))
    xs=decode_shared(u[11:])
    aaz,apol,baz,bpol,cA,cB,logk=xs
    A=op(axis(aaz,apol)); B=op(axis(baz,bpol)); kappa=float(np.exp(logk))
    F=cA*np.kron(A,I2)+cB*np.kron(I2,B)
    return L+kappa*d_super(F)


def state_from_unit(u,theta):
    return evolve(generator_from_unit(u,theta))


def residual(u,theta,tar):
    d=state_from_unit(u,theta)-tar
    return np.concatenate((d.real.ravel(),d.imag.ravel()))


def design(method,shard):
    seed=37200+100*shard+(0 if method=='sobol_lsq' else 1)
    if method=='sobol_lsq':
        return qmc.Sobol(d=18,scramble=True,seed=seed).random_base2(m=7)
    if method=='lhs_lsq':
        return qmc.LatinHypercube(d=18,seed=seed).random(N_STARTS)
    raise ValueError(method)


def hidden_unit(shard):
    rng=np.random.default_rng(37100+shard)
    u=rng.uniform(0.08,0.92,size=18)
    label='interior_combined'
    if shard==4:
        # Exact K=2 measurement-feedback boundary: shared coupling coefficients zero.
        u[15]=0.5; u[16]=0.5
        label='mf_only_boundary'
    elif shard==5:
        # Prospectively fixed strong shared-noise interior control.
        u[15]=0.85; u[16]=0.15; u[17]=0.78
        label='strong_shared_noise'
    return u,label


def optimize(method,shard,theta,tar):
    scored=[]
    for u in design(method,shard):
        r=residual(u,theta,tar); scored.append((float(np.dot(r,r)),u))
    scored.sort(key=lambda z:z[0])
    best=None
    for _,u0 in scored[:N_REFINE]:
        fit=least_squares(lambda z:residual(z,theta,tar),u0,bounds=(0.0,1.0),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-11,xtol=1e-11,gtol=1e-11)
        rho=state_from_unit(fit.x,theta); gap=float(td(rho,tar)); rn=float(np.linalg.norm(fit.fun))
        cand=(gap,rn,int(fit.nfev),bool(fit.success))
        if best is None or (gap,rn)<(best[0],best[1]): best=cand
    return best


def positive_control(method,shard):
    case=shard%4; scale,t0=CASES[case]; theta=float(scale*t0)
    src,label=hidden_unit(shard); tar=state_from_unit(src,theta)
    gap,rn,nfev,ok=optimize(method,shard,theta,tar)
    valid=bool(np.isfinite(gap) and np.isfinite(rn))
    return {
      'iteration':'Iter019A','gate':'G37-C','stream':'positive_control','method':method,'shard':shard,'theta':theta,
      'result':{'best_trace_gap':gap,'best_residual_norm':rn,'best_nfev':nfev,'optimizer_success_flag':ok,'scientific_support':bool(valid and gap<RECOVERY_TOL)},
      'hidden_target_metadata':{'control_type':label,'hidden_coordinates_not_used_as_starts':True},
      'structural_valid':valid,
      'frozen_thresholds':{'recovery_trace_distance':RECOVERY_TOL,'n_starts':N_STARTS,'n_refine':N_REFINE,'max_nfev':MAX_NFEV},
      'scope_lock':'K=2 additive independent single-axis measurement-feedback GKSL plus one shared Gaussian classical Hamiltonian-noise process.'
    }


def admissibility(shard):
    scale,t0=CASES[shard]; theta=float(scale*t0)
    rng=np.random.default_rng(37300+shard); u=rng.uniform(0.08,0.92,size=18)
    L=generator_from_unit(u,theta); E=exp_super(L)
    tr=I4.reshape(-1,order='F').conj(); tp=float(np.linalg.norm(tr@L))
    cm=float(np.min(np.linalg.eigvalsh(choi(E))))
    rho=evolve(L); rh=(rho+rho.conj().T)/2
    psd=float(np.min(np.linalg.eigvalsh(rh))); terr=float(abs(np.trace(rho)-1.0)); herm=float(np.linalg.norm(rho-rho.conj().T))
    support=bool(tp<TP_TOL and cm>CHOI_TOL and psd>PSD_TOL and terr<TRACE_TOL and herm<1e-10)
    vals=(tp,cm,psd,terr,herm); valid=bool(all(np.isfinite(v) for v in vals))
    return {
      'iteration':'Iter019A','gate':'G37-C','stream':'admissibility','method':'none','shard':shard,'theta':theta,
      'result':{'tp_residual':tp,'choi_min_eig':cm,'state_min_eig':psd,'trace_error':terr,'hermiticity_error':herm,'scientific_support':support},
      'structural_valid':valid,
      'frozen_thresholds':{'tp':TP_TOL,'choi_floor':CHOI_TOL,'state_floor':PSD_TOL,'trace':TRACE_TOL,'hermiticity':1e-10},
      'scope_lock':'Same prospectively defined combined finite Markovian comparator family.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=['positive_control','admissibility'],required=True); ap.add_argument('--method',choices=['sobol_lsq','lhs_lsq','none'],required=True); ap.add_argument('--shard',type=int,required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if a.stream=='positive_control':
        if a.method not in METHODS or a.shard not in range(6): raise SystemExit('positive controls require calibrated method and shard 0..5')
        out=positive_control(a.method,a.shard)
    else:
        if a.method!='none' or a.shard not in range(4): raise SystemExit('admissibility requires method none and shard 0..3')
        out=admissibility(a.shard)
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not out['structural_valid']: raise SystemExit(2)

if __name__=='__main__': main()
