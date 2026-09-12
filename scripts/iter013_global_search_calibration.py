#!/usr/bin/env python3
"""Iter013 / G31: global nearest-comparator search calibration.

Frozen before result inspection.

Scope: additive K<=4 finite two-qubit Markovian independent single-axis
measurement-feedback GKSL channels, each satisfying Gamma_A Gamma_B = chi_k^2.
This is not a theorem about all semiclassical gravity.

Key rule: a residual adversarial gap is scientifically interpretable only if the
same global optimizer closes prospectively defined in-family positive controls.
Scientific failures are written to JSON and do not fail CI; only invalid numerics
raise an infrastructure failure.
"""
import argparse, json, math, sys
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I4, RHO0, axis, op, Lgen, evolve, target, td, exp_super, choi

CASES=[(0.5,0.05),(1.0,0.10),(2.0,0.20),(4.0,0.35)]
GAP_THRESHOLD=1e-4
RECOVERY_TOL=2e-3


def decode(x,K):
    """Five physical params/channel plus K-1 stick-breaking variables."""
    x=np.asarray(x,dtype=float)
    channels=[]
    sticks=np.clip(x[5*K:],0.0,1.0)
    rem=1.0; weights=[]
    for i in range(K-1):
        wi=rem*float(sticks[i]); weights.append(wi); rem-=wi
    weights.append(rem)
    for k in range(K):
        alA,beA,alB,beB,a=x[5*k:5*k+5]
        channels.append((weights[k],float(alA),float(beA),float(alB),float(beB),float(np.clip(a,-3,3))))
    return channels


def bounds(K):
    b=[]
    for _ in range(K):
        b += [(-math.pi,math.pi),(0,math.pi),(-math.pi,math.pi),(0,math.pi),(-3,3)]
    b += [(0,1)]*(K-1)
    return b


def multi_L(theta,channels):
    L=np.zeros((16,16),dtype=complex)
    for w,alA,beA,alB,beB,a in channels:
        chi=theta*w
        Li,_,_=Lgen(chi,op(axis(alA,beA)),op(axis(alB,beB)),a)
        L += Li
    return L


def objective(x,K,theta,tar):
    try:
        return td(evolve(multi_L(theta,decode(x,K))),tar)
    except Exception:
        return 1e6


def run_de(K,theta,tar,seed,maxiter=None):
    # Prospectively fixed budgets. Population scales with dimension through scipy.
    if maxiter is None: maxiter={2:28,3:24,4:20}[K]
    res=differential_evolution(
        lambda x: objective(x,K,theta,tar), bounds(K), seed=seed,
        maxiter=maxiter, popsize=5, tol=1e-6, atol=1e-8,
        mutation=(0.5,1.0), recombination=0.7, polish=False,
        workers=1, updating='immediate')
    return res


def adversarial(scale,theta,shard,K):
    th=scale*theta; tar=target(th)
    res=run_de(K,th,tar,41000+100*K+shard)
    best=float(res.fun)
    return {
        'K':K,'best_gap':best,'evaluations':int(res.nfev),'nit':int(res.nit),
        'optimizer_success_flag':bool(res.success),'optimizer_message':str(res.message),
        'nonzero_gap':bool(best>GAP_THRESHOLD),
        'scientific_support':bool(best>GAP_THRESHOLD),
        'best_parameters':np.asarray(res.x,dtype=float).tolist(),
        'interpretation':f'Global differential-evolution search in additive K={K} independent-channel family; interpretation conditional on positive-control recovery.'
    }


def recovery_k2(scale,theta,shard):
    """Positive calibration: target generated inside K=2 family; optimizer sees only density matrix."""
    th=scale*theta
    # Deterministic nontrivial, shard-dependent in-family source away from singular weights.
    src=np.array([
        0.35+0.11*shard, 0.65+0.08*shard, -0.55+0.09*shard, 1.05-0.06*shard, -0.7+0.35*shard,
        -1.0+0.13*shard, 1.25-0.07*shard, 0.8-0.1*shard, 0.72+0.05*shard, 0.6-0.25*shard,
        0.37+0.07*shard
    ],dtype=float)
    tar=evolve(multi_L(th,decode(src,2)))
    res=run_de(2,th,tar,42000+shard,maxiter=34)
    best=float(res.fun)
    return {
        'K':2,'recovery_gap':best,'recovery_tolerance':RECOVERY_TOL,
        'evaluations':int(res.nfev),'nit':int(res.nit),
        'optimizer_success_flag':bool(res.success),'optimizer_message':str(res.message),
        'scientific_support':bool(best<RECOVERY_TOL),
        'source_parameters_hidden_from_optimizer':src.tolist(),
        'best_parameters':np.asarray(res.x,dtype=float).tolist(),
        'interpretation':'Positive in-family optimizer calibration. Failure blocks interpretation of residual adversarial gaps.'
    }


def admissibility_k4(scale,theta,shard):
    th=scale*theta
    rng=np.random.default_rng(43000+shard)
    x=[]
    for _ in range(4):
        x += [rng.uniform(-math.pi,math.pi),rng.uniform(0,math.pi),rng.uniform(-math.pi,math.pi),rng.uniform(0,math.pi),rng.uniform(-2.5,2.5)]
    x += list(rng.uniform(0.1,0.9,size=3))
    L=multi_L(th,decode(np.array(x),4)); E=exp_super(L)
    tr=I4.reshape(-1,order='F').conj()
    tp=float(np.linalg.norm(tr@L))
    mine=float(np.min(np.linalg.eigvalsh(choi(E))))
    rho=evolve(L); psd=float(np.min(np.linalg.eigvalsh(rho)))
    trace_err=float(abs(np.trace(rho)-1.0))
    support=tp<1e-10 and mine>-1e-8 and psd>-1e-8 and trace_err<1e-10
    return {
        'K':4,'tp_residual':tp,'choi_min_eig':mine,'state_min_eig':psd,'trace_error':trace_err,
        'scientific_support':bool(support),
        'interpretation':'CPTP/PSD numerical admissibility control for sampled additive K=4 generators.'
    }

STREAMS={
    'adversarial_k2':lambda s,t,h:adversarial(s,t,h,2),
    'adversarial_k3':lambda s,t,h:adversarial(s,t,h,3),
    'adversarial_k4':lambda s,t,h:adversarial(s,t,h,4),
    'recovery_k2':recovery_k2,
    'admissibility_k4':admissibility_k4,
}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stream',choices=STREAMS,required=True)
    ap.add_argument('--shard',type=int,choices=range(4),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    scale,theta=CASES[a.shard]
    r=STREAMS[a.stream](scale,theta,a.shard)
    valid=all(np.isfinite(v) for v in [scale,theta]) and isinstance(r.get('scientific_support'),(bool,np.bool_))
    out={
        'iteration':'Iter013','gate':'G31','stream':a.stream,'shard':a.shard,
        'theta':scale*theta,'result':r,'structural_valid':bool(valid),
        'frozen_thresholds':{'adversarial_gap':GAP_THRESHOLD,'positive_recovery':RECOVERY_TOL},
        'scope_lock':'Additive K<=4 finite two-qubit Markovian independent single-axis measurement-feedback GKSL channels only.'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    if not valid: raise SystemExit(2)

if __name__=='__main__': main()
