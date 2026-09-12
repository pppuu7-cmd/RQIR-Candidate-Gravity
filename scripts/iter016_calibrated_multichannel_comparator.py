#!/usr/bin/env python3
"""Iter016 / G34: calibrated K=2 adversarial rerun + K=3/K=4 positive controls.

Prospectively frozen after G33 and before G34 result inspection.

Authority optimizer constructions are exactly the two G33-calibrated families:
Sobol multistart + bounded smooth least-squares, and Latin-hypercube multistart +
bounded smooth least-squares.  Hidden positive-control source coordinates are never
used as optimizer starts.  Scientific acceptance is always evaluated in trace distance.

Scope remains the finite additive independent single-axis Markovian measurement-
feedback GKSL comparator family; this is not a no-go theorem for semiclassical gravity.
"""
import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares
from scipy.stats import qmc

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES, GAP_THRESHOLD, RECOVERY_TOL, bounds, decode, multi_L
from iter011_robustness_suite import evolve, target, td

LSQ_MAX_NFEV = 3000
STARTS = {2: 32, 3: 64, 4: 64}
METHODS = ('sobol_lsq','lhs_lsq')
CROSS_METHOD_AGREEMENT_TOL = RECOVERY_TOL


def b_arrays(K):
    b=np.asarray(bounds(K),dtype=float)
    return b[:,0],b[:,1],b[:,1]-b[:,0]


def unit_to_native(u,K):
    lo,hi,w=b_arrays(K)
    return lo+np.clip(np.asarray(u,dtype=float),0.0,1.0)*w


def residual_vector(u,K,theta,tar):
    x=unit_to_native(u,K)
    rho=evolve(multi_L(theta,decode(x,K)))
    d=np.asarray(rho-tar,dtype=complex).reshape(-1)
    return np.concatenate([d.real,d.imag])


def metrics(u,K,theta,tar):
    x=unit_to_native(u,K)
    rho=evolve(multi_L(theta,decode(x,K)))
    r=residual_vector(u,K,theta,tar)
    return float(td(rho,tar)),float(np.linalg.norm(r))


def starts(method,K,shard):
    n=STARTS[K]; d=5*K+(K-1)
    if method=='sobol_lsq':
        # Preserve exact G33 K=2 design; freeze dimension-specific extensions for K=3/4.
        seed=(61000+shard) if K==2 else (61000+100*K+shard)
        m=int(round(math.log2(n)))
        return qmc.Sobol(d=d,scramble=True,seed=seed).random_base2(m=m)
    if method=='lhs_lsq':
        seed=(62000+shard) if K==2 else (62000+100*K+shard)
        return qmc.LatinHypercube(d=d,seed=seed).random(n=n)
    raise ValueError(method)


def optimize(method,K,shard,theta,tar):
    rr=[]
    for u0 in starts(method,K,shard):
        res=least_squares(
            lambda u: residual_vector(u,K,theta,tar),
            np.asarray(u0,dtype=float),
            bounds=(np.zeros_like(u0),np.ones_like(u0)),
            method='trf',x_scale='jac',
            ftol=1e-11,xtol=1e-11,gtol=1e-11,
            max_nfev=LSQ_MAX_NFEV,verbose=0)
        gap,rn=metrics(res.x,K,theta,tar)
        rr.append((gap,rn,int(res.nfev),bool(res.success)))
    best=min(rr,key=lambda z:(z[0],z[1]))
    return {
      'method':method,'K':K,'n_starts':len(rr),
      'best_trace_gap':float(best[0]),'best_residual_norm':float(best[1]),
      'best_nfev':int(best[2]),'best_success_flag':bool(best[3]),
      'total_nfev':int(sum(z[2] for z in rr)),
      'n_below_recovery_tol':int(sum(z[0]<RECOVERY_TOL for z in rr)),
    }


def hidden_source(K,shard):
    # Prospectively fixed, nontrivial, interior in-family sources. Their coordinates
    # generate the target only and are never provided to the optimizer.
    x=[]
    for k in range(K):
        x += [
          -1.35 + 0.72*k + 0.06*shard,
           0.58 + 0.23*k + 0.035*shard,
           1.22 - 0.47*k + 0.045*shard,
           0.76 + 0.19*k + 0.025*shard,
          -1.25 + 0.74*k - 0.10*shard,
        ]
    base=[0.31+0.04*shard,0.43-0.025*shard,0.52+0.015*shard]
    x += base[:K-1]
    arr=np.asarray(x,dtype=float)
    lo,hi,_=b_arrays(K)
    if not np.all((arr>lo)&(arr<hi)):
        raise RuntimeError('prospective hidden source left frozen bounds')
    return arr


def positive_control(method,K,shard,theta):
    src=hidden_source(K,shard)
    tar=evolve(multi_L(theta,decode(src,K)))
    r=optimize(method,K,shard,theta,tar)
    r.update({
      'stream':'positive_control',
      'recovery_tolerance':RECOVERY_TOL,
      'scientific_support':bool(r['best_trace_gap']<RECOVERY_TOL),
      'hidden_source_used_as_initializer':False,
      'interpretation':f'Prospective in-family K={K} positive control for the calibrated smooth multistart method extension.'
    })
    return r


def adversarial_k2(method,shard,theta):
    tar=target(theta)
    r=optimize(method,2,shard,theta,tar)
    r.update({
      'stream':'adversarial_k2',
      'nonzero_gap_threshold':GAP_THRESHOLD,
      'scientific_support':bool(r['best_trace_gap']>GAP_THRESHOLD),
      'interpretation':'Prospective RCG-002 comparison using a G33-calibrated K=2 optimizer. Scoped finite-family result only; cross-method aggregate agreement is additionally required.'
    })
    return r


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stream',choices=['adversarial_k2','positive_k3','positive_k4'],required=True)
    ap.add_argument('--method',choices=METHODS,required=True)
    ap.add_argument('--shard',type=int,choices=range(4),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    scale,theta0=CASES[a.shard]; theta=scale*theta0
    if a.stream=='adversarial_k2':
        r=adversarial_k2(a.method,a.shard,theta); K=2
    elif a.stream=='positive_k3':
        r=positive_control(a.method,3,a.shard,theta); K=3
    else:
        r=positive_control(a.method,4,a.shard,theta); K=4
    nums=[float(v) for v in r.values() if isinstance(v,(int,float,np.integer,np.floating)) and not isinstance(v,(bool,np.bool_))]
    valid=bool(all(np.isfinite(v) for v in nums))
    out={
      'iteration':'Iter016','gate':'G34','stream':a.stream,'method':a.method,
      'K':K,'shard':a.shard,'theta':theta,'result':r,'structural_valid':valid,
      'frozen_thresholds':{
        'positive_recovery_trace_distance':RECOVERY_TOL,
        'adversarial_nonzero_gap':GAP_THRESHOLD,
        'cross_method_agreement':CROSS_METHOD_AGREEMENT_TOL,
        'starts':STARTS[K],
        'least_squares_max_nfev_per_start':LSQ_MAX_NFEV,
      },
      'scope_lock':'Finite additive independent single-axis Markovian measurement-feedback GKSL comparator family only.'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    if not valid: raise SystemExit(2)

if __name__=='__main__': main()
