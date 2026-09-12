#!/usr/bin/env python3
"""Iter017 / G35: prospective calibrated K=3/K=4 adversarial reruns + admissibility.

Frozen after terminal G34 and before G35 result inspection.

Authority optimizers are exactly the G34-calibrated Sobol-LSQ and LHS-LSQ
extensions. Historical G30/G31 adversarial minima are never reused as authority.
Scientific interpretation remains restricted to the finite additive independent
single-axis Markovian measurement-feedback GKSL comparator family.
"""
import argparse, json, math, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES, GAP_THRESHOLD, RECOVERY_TOL, decode, multi_L
from iter011_robustness_suite import I4, evolve, target, exp_super, choi
from iter016_calibrated_multichannel_comparator import optimize, METHODS

TP_TOL=1e-10
CHOI_TOL=-1e-8
PSD_TOL=-1e-8
TRACE_TOL=1e-10
AGREEMENT_TOL=RECOVERY_TOL
NESTING_SLACK=RECOVERY_TOL


def adversarial(method,K,shard,theta):
    tar=target(theta)
    r=optimize(method,K,shard,theta,tar)
    r.update({
      'stream':f'adversarial_k{K}',
      'nonzero_gap_threshold':GAP_THRESHOLD,
      'scientific_support_local':bool(r['best_trace_gap']>GAP_THRESHOLD),
      'interpretation':f'Prospective calibrated K={K} RCG-002 nearest-comparator search. Aggregate cross-method and nesting gates are additionally required.'
    })
    return r


def admissibility(K,shard,theta):
    rng=np.random.default_rng(71000+100*K+shard)
    x=[]
    for _ in range(K):
        x += [rng.uniform(-math.pi,math.pi),rng.uniform(0,math.pi),
              rng.uniform(-math.pi,math.pi),rng.uniform(0,math.pi),
              rng.uniform(-2.5,2.5)]
    x += list(rng.uniform(0.1,0.9,size=K-1))
    arr=np.asarray(x,dtype=float)
    L=multi_L(theta,decode(arr,K)); E=exp_super(L)
    tr=I4.reshape(-1,order='F').conj()
    tp=float(np.linalg.norm(tr@L))
    choi_min=float(np.min(np.linalg.eigvalsh(choi(E))))
    rho=evolve(L)
    herm=float(np.linalg.norm(rho-rho.conj().T))
    psd=float(np.min(np.linalg.eigvalsh((rho+rho.conj().T)/2)))
    trace_err=float(abs(np.trace(rho)-1.0))
    ok=tp<TP_TOL and choi_min>CHOI_TOL and psd>PSD_TOL and trace_err<TRACE_TOL and herm<1e-10
    return {
      'stream':f'admissibility_k{K}','K':K,
      'tp_residual':tp,'choi_min_eig':choi_min,'state_min_eig':psd,
      'trace_error':trace_err,'hermiticity_error':herm,
      'scientific_support':bool(ok),
      'interpretation':f'Independent numerical GKSL/CPTP/PSD admissibility control for a prospectively fixed sampled K={K} additive generator.'
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stream',choices=['adversarial_k3','adversarial_k4','admissibility_k3','admissibility_k4'],required=True)
    ap.add_argument('--method',choices=['sobol_lsq','lhs_lsq','none'],required=True)
    ap.add_argument('--shard',type=int,choices=range(4),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    scale,theta0=CASES[a.shard]; theta=scale*theta0
    K=3 if a.stream.endswith('k3') else 4
    if a.stream.startswith('adversarial'):
        if a.method not in METHODS: raise SystemExit('adversarial stream requires calibrated method')
        r=adversarial(a.method,K,a.shard,theta)
    else:
        if a.method!='none': raise SystemExit('admissibility stream uses method=none')
        r=admissibility(K,a.shard,theta)
    nums=[]
    for v in r.values():
        if isinstance(v,(int,float,np.integer,np.floating)) and not isinstance(v,(bool,np.bool_)): nums.append(float(v))
    valid=bool(all(np.isfinite(v) for v in nums))
    out={
      'iteration':'Iter017','gate':'G35','stream':a.stream,'method':a.method,
      'K':K,'shard':a.shard,'theta':theta,'result':r,'structural_valid':valid,
      'frozen_thresholds':{
        'adversarial_nonzero_gap':GAP_THRESHOLD,
        'cross_method_agreement':AGREEMENT_TOL,
        'nesting_slack':NESTING_SLACK,
        'tp_residual':TP_TOL,'choi_min_eig':CHOI_TOL,'state_min_eig':PSD_TOL,'trace_error':TRACE_TOL,
      },
      'scope_lock':'Finite additive independent single-axis Markovian measurement-feedback GKSL comparator family only.'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    if not valid: raise SystemExit(2)

if __name__=='__main__': main()
