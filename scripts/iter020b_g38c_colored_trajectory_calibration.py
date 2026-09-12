#!/usr/bin/env python3
"""Iter020B / G38-C: prospective positive-control calibration for the
multi-time OU colored-classical-noise trajectory comparator.

Single-time OU phase noise is equivalent to a shared Gaussian phase-variance
channel, so this gate deliberately uses three frozen observation times to make
the finite correlation time tau identifiable at the trajectory level.

Hidden in-family trajectories are generated at T={0.25,0.5,1.0}. Hidden source
coordinates are never optimizer starts. Two independent design constructions
feed bounded least squares. Scientific acceptance is max per-time trace distance
<2e-3 on every positive control.
"""
import argparse,json,math,sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.stats import qmc

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I2,I4,axis,op,td,exp_super
from iter018a_correlated_classical_noise_validation import d_super,evolve_super
from iter020a_g38p_colored_classical_noise_validation import variance

METHODS=('sobol_lsq','lhs_lsq')
TIMES=np.array([0.25,0.5,1.0],float)
RECOVERY_TOL=2e-3
N_STARTS=96
N_REFINE=16
MAX_NFEV=800
LO=np.array([-math.pi,0.10,-math.pi,0.10,-2.0,-2.0,-4.0,-2.0],float)
HI=np.array([ math.pi,math.pi-0.10, math.pi,math.pi-0.10, 2.0, 2.0, 1.0, 1.0],float)


def decode_unit(u): return LO+(HI-LO)*np.asarray(u,float)

def trajectory_x(x):
    aaz,apol,baz,bpol,cA,cB,logs2,logtau=np.asarray(x,float)
    A=op(axis(aaz,apol)); B=op(axis(baz,bpol)); s2=float(np.exp(logs2)); tau=float(np.exp(logtau))
    F=cA*np.kron(A,I2)+cB*np.kron(I2,B); D=d_super(F)
    return [evolve_super(exp_super(variance(float(T),s2,tau)*D)) for T in TIMES]

def residual_u(u,tars):
    rs=[]
    for rho,tar in zip(trajectory_x(decode_unit(u)),tars):
        d=rho-tar; rs.extend(d.real.ravel()); rs.extend(d.imag.ravel())
    return np.asarray(rs,float)

def design(method,shard):
    seed=38200+100*shard+(0 if method=='sobol_lsq' else 1)
    if method=='sobol_lsq': return qmc.Sobol(d=8,scramble=True,seed=seed).random_base2(m=7)[:N_STARTS]
    return qmc.LatinHypercube(d=8,seed=seed).random(N_STARTS)

def hidden_unit(shard):
    rng=np.random.default_rng(38100+shard); u=rng.uniform(0.10,0.90,size=8); label='interior_ou'
    if shard==4:
        u[7]=0.08; label='short_correlation_boundary'
    elif shard==5:
        u[7]=0.92; label='long_correlation_boundary'
    return u,label

def optimize(method,shard,tars):
    scored=[]
    for u in design(method,shard):
        r=residual_u(u,tars); scored.append((float(np.dot(r,r)),u))
    scored.sort(key=lambda z:z[0]); best=None
    for _,u0 in scored[:N_REFINE]:
        fit=least_squares(lambda z:residual_u(z,tars),u0,bounds=(0,1),method='trf',x_scale='jac',max_nfev=MAX_NFEV,ftol=1e-11,xtol=1e-11,gtol=1e-11)
        rhos=trajectory_x(decode_unit(fit.x)); gaps=[float(td(r,t)) for r,t in zip(rhos,tars)]; cand=(max(gaps),gaps,float(np.linalg.norm(fit.fun)),int(fit.nfev))
        if best is None or (cand[0],cand[2])<(best[0],best[2]): best=cand
    return best

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(6),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    hu,label=hidden_unit(a.shard); tars=trajectory_x(decode_unit(hu)); maxgap,gaps,rn,nfev=optimize(a.method,a.shard,tars)
    valid=bool(np.isfinite(maxgap) and np.all(np.isfinite(gaps)) and np.isfinite(rn)); support=bool(valid and maxgap<RECOVERY_TOL)
    out={'iteration':'Iter020B','gate':'G38-C','method':a.method,'shard':a.shard,'times':TIMES.tolist(),'result':{'per_time_trace_gaps':gaps,'max_trace_gap':maxgap,'residual_norm':rn,'nfev':nfev,'scientific_support':support},'hidden_target_metadata':{'control_type':label,'hidden_coordinates_not_used_as_starts':True},'structural_valid':valid,'frozen_thresholds':{'max_per_time_trace_distance':RECOVERY_TOL,'n_starts':N_STARTS,'n_refine':N_REFINE,'max_nfev':MAX_NFEV},'interpretation':'Prospective in-family trajectory optimizer calibration only. PASS authorizes a separate multi-time RCG-002 adversarial test.','scope_lock':'Stationary OU finite-correlation scalar classical noise with one fixed local-sum coupling; three-time trajectory T=[0.25,0.5,1].'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not valid: raise SystemExit(2)
if __name__=='__main__': main()
