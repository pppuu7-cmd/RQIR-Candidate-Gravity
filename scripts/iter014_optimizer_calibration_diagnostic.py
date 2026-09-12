#!/usr/bin/env python3
"""Iter014 / G32: positive-control optimizer calibration diagnostics.

Prospectively frozen before execution.

Purpose: diagnose the G31 positive in-family recovery failure without inspecting or
retuning against the RCG-002 adversarial target.  The same four hidden K=2 source
families used by G31 are tested through independent plumbing, symmetry, local-basin,
deep-global, and hybrid-global/local streams.

Scientific rule: no adversarial residual is interpretable unless a prospectively
specified positive-control search method closes the existing RECOVERY_TOL=2e-3.
"""
import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, minimize

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES, RECOVERY_TOL, bounds, decode, multi_L, objective
from iter011_robustness_suite import evolve, td

ORACLE_TOL = 1e-10
SYMMETRY_TOL = 1e-10
LOCAL_NOISE = 0.08


def source_params(shard: int) -> np.ndarray:
    return np.array([
        0.35+0.11*shard, 0.65+0.08*shard, -0.55+0.09*shard, 1.05-0.06*shard, -0.7+0.35*shard,
        -1.0+0.13*shard, 1.25-0.07*shard, 0.8-0.1*shard, 0.72+0.05*shard, 0.6-0.25*shard,
        0.37+0.07*shard
    ], dtype=float)


def hidden_target(scale: float, theta: float, shard: int):
    th = scale * theta
    src = source_params(shard)
    tar = evolve(multi_L(th, decode(src, 2)))
    return th, src, tar


def within_bounds(x, b):
    return all(lo <= float(v) <= hi for v, (lo, hi) in zip(x, b))


def oracle_replay(scale, theta, shard):
    th, src, tar = hidden_target(scale, theta, shard)
    gap = float(objective(src, 2, th, tar))
    ch = decode(src, 2)
    weights = [float(c[0]) for c in ch]
    in_bounds = within_bounds(src, bounds(2))
    support = in_bounds and abs(sum(weights)-1.0) < 1e-14 and gap < ORACLE_TOL
    return {
        'oracle_gap': gap,
        'source_inside_frozen_bounds': bool(in_bounds),
        'decoded_weights': weights,
        'weight_sum_error': float(abs(sum(weights)-1.0)),
        'scientific_support': bool(support),
        'interpretation': 'Exact source replay isolates parameterization/objective plumbing from optimizer performance.'
    }


def swap_symmetry(scale, theta, shard):
    th, src, tar = hidden_target(scale, theta, shard)
    # K=2 stick variable is the first-channel weight. Swapping the two additive
    # channels therefore swaps their five-parameter blocks and maps w -> 1-w.
    sw = np.concatenate([src[5:10], src[0:5], [1.0-src[10]]])
    L0 = multi_L(th, decode(src, 2))
    L1 = multi_L(th, decode(sw, 2))
    ldiff = float(np.linalg.norm(L0-L1))
    tgap = float(td(evolve(L1), tar))
    support = within_bounds(sw, bounds(2)) and ldiff < SYMMETRY_TOL and tgap < SYMMETRY_TOL
    return {
        'liouvillian_swap_norm': ldiff,
        'target_swap_gap': tgap,
        'swapped_inside_frozen_bounds': bool(within_bounds(sw, bounds(2))),
        'scientific_support': bool(support),
        'interpretation': 'K=2 channel-permutation symmetry control; failure would indicate parameterization/objective inconsistency.'
    }


def local_basin(scale, theta, shard):
    th, src, tar = hidden_target(scale, theta, shard)
    rng = np.random.default_rng(51000+shard)
    widths = np.array([hi-lo for lo,hi in bounds(2)], dtype=float)
    perturb = rng.normal(0.0, LOCAL_NOISE, size=src.size) * widths
    x0 = src + perturb
    for i,(lo,hi) in enumerate(bounds(2)):
        x0[i] = np.clip(x0[i], lo+1e-9, hi-1e-9)
    start_gap = float(objective(x0, 2, th, tar))
    res = minimize(
        lambda x: objective(x,2,th,tar), x0, method='Powell', bounds=bounds(2),
        options={'maxiter':1800, 'xtol':1e-9, 'ftol':1e-11, 'disp':False})
    best = float(res.fun)
    return {
        'start_gap': start_gap,
        'recovery_gap': best,
        'recovery_tolerance': RECOVERY_TOL,
        'evaluations': int(res.nfev),
        'optimizer_success_flag': bool(res.success),
        'optimizer_message': str(res.message),
        'scientific_support': bool(best < RECOVERY_TOL),
        'interpretation': 'Local-basin recovery from a prospectively fixed perturbation around the hidden in-family source.'
    }


def global_de(scale, theta, shard, deep: bool):
    th, src, tar = hidden_target(scale, theta, shard)
    if deep:
        maxiter, popsize, seed = 180, 12, 52000+shard
        label = 'deep_global'
    else:
        maxiter, popsize, seed = 85, 8, 53000+shard
        label = 'hybrid_global_local'
    de = differential_evolution(
        lambda x: objective(x,2,th,tar), bounds(2), seed=seed,
        maxiter=maxiter, popsize=popsize, tol=1e-7, atol=1e-9,
        mutation=(0.45,1.0), recombination=0.75, polish=False,
        workers=1, updating='immediate')
    de_gap = float(de.fun)
    if deep:
        # Deep stream tests enlarged global budget as a standalone method, with the
        # standard bounded Powell polish applied only after the frozen DE search.
        local_maxiter = 2400
    else:
        local_maxiter = 3200
    loc = minimize(
        lambda x: objective(x,2,th,tar), np.asarray(de.x,dtype=float),
        method='Powell', bounds=bounds(2),
        options={'maxiter':local_maxiter, 'xtol':1e-10, 'ftol':1e-12, 'disp':False})
    best = float(loc.fun)
    return {
        'method': label,
        'de_gap_before_polish': de_gap,
        'recovery_gap': best,
        'recovery_tolerance': RECOVERY_TOL,
        'de_evaluations': int(de.nfev),
        'de_iterations': int(de.nit),
        'local_evaluations': int(loc.nfev),
        'de_success_flag': bool(de.success),
        'local_success_flag': bool(loc.success),
        'scientific_support': bool(best < RECOVERY_TOL),
        'interpretation': 'Positive-control calibration only; no RCG-002 adversarial target is inspected in G32.'
    }


STREAMS = {
    'oracle_replay': oracle_replay,
    'swap_symmetry': swap_symmetry,
    'local_basin': local_basin,
    'deep_global': lambda s,t,h: global_de(s,t,h,True),
    'hybrid_global_local': lambda s,t,h: global_de(s,t,h,False),
}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stream', choices=STREAMS, required=True)
    ap.add_argument('--shard', type=int, choices=range(4), required=True)
    ap.add_argument('--out', required=True)
    a=ap.parse_args()
    scale,theta=CASES[a.shard]
    r=STREAMS[a.stream](scale,theta,a.shard)
    numeric=[]
    for k,v in r.items():
        if isinstance(v,(int,float,np.integer,np.floating)) and not isinstance(v,(bool,np.bool_)):
            numeric.append(float(v))
    valid=all(np.isfinite(v) for v in numeric) and isinstance(r.get('scientific_support'),(bool,np.bool_))
    out={
        'iteration':'Iter014','gate':'G32','stream':a.stream,'shard':a.shard,
        'theta':scale*theta,'result':r,'structural_valid':bool(valid),
        'frozen_thresholds':{
            'oracle_gap':ORACLE_TOL,
            'swap_symmetry':SYMMETRY_TOL,
            'positive_recovery':RECOVERY_TOL,
            'local_noise_fraction_of_parameter_width':LOCAL_NOISE
        },
        'scope_lock':'Positive-control optimizer diagnostics only; RCG-002 adversarial target forbidden in this gate.'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    if not valid:
        raise SystemExit(2)

if __name__=='__main__':
    main()
