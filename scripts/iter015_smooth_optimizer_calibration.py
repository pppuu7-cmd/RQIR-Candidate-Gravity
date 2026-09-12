#!/usr/bin/env python3
"""Iter015 / G33: smooth positive-control optimizer calibration.

Prospectively frozen before execution. RCG-002 adversarial targets are forbidden.
The hidden K=2 controls are used only to generate target density matrices; hidden
source coordinates are never supplied to an optimizer.

Optimizer coordinates are affine unit-box parameters. Search objectives use a
smooth density-matrix residual, while the scientific acceptance criterion remains
the unchanged trace-distance gap < 2e-3.
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, least_squares
from scipy.stats import qmc

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter013_global_search_calibration import CASES, RECOVERY_TOL, bounds, decode, multi_L
from iter014_optimizer_calibration_diagnostic import source_params
from iter011_robustness_suite import evolve, td

DIM = 11
LSQ_MAX_NFEV = 2500
SOBOL_STARTS = 32
LHS_STARTS = 32
DE_MAXITER = 120
DE_POPSIZE = 10

B = np.asarray(bounds(2), dtype=float)
LO = B[:, 0]
HI = B[:, 1]
WIDTH = HI - LO


def unit_to_native(u):
    u = np.asarray(u, dtype=float)
    return LO + np.clip(u, 0.0, 1.0) * WIDTH


def target_for(shard):
    scale, theta0 = CASES[shard]
    theta = scale * theta0
    src = source_params(shard)
    target = evolve(multi_L(theta, decode(src, 2)))
    return theta, target


def residual_vector(u, theta, target):
    x = unit_to_native(u)
    rho = evolve(multi_L(theta, decode(x, 2)))
    d = np.asarray(rho - target, dtype=complex).reshape(-1)
    # Full real/imag embedding is deliberately redundant but smooth and
    # convention-independent. Acceptance is evaluated separately in trace distance.
    return np.concatenate([d.real, d.imag])


def final_metrics(u, theta, target):
    x = unit_to_native(u)
    rho = evolve(multi_L(theta, decode(x, 2)))
    r = residual_vector(u, theta, target)
    return float(td(rho, target)), float(np.linalg.norm(r))


def run_lsq(u0, theta, target):
    res = least_squares(
        lambda u: residual_vector(u, theta, target),
        np.asarray(u0, dtype=float),
        bounds=(np.zeros(DIM), np.ones(DIM)),
        method='trf', x_scale='jac',
        ftol=1e-11, xtol=1e-11, gtol=1e-11,
        max_nfev=LSQ_MAX_NFEV, verbose=0,
    )
    gap, rn = final_metrics(res.x, theta, target)
    return {
        'u': np.asarray(res.x, dtype=float),
        'trace_gap': gap,
        'residual_norm': rn,
        'nfev': int(res.nfev),
        'status': int(res.status),
        'success': bool(res.success),
    }


def multistart(method, shard, theta, target):
    if method == 'sobol_lsq':
        starts = qmc.Sobol(d=DIM, scramble=True, seed=61000 + shard).random_base2(m=5)
    elif method == 'lhs_lsq':
        starts = qmc.LatinHypercube(d=DIM, seed=62000 + shard).random(n=LHS_STARTS)
    else:
        raise ValueError(method)
    results = [run_lsq(u, theta, target) for u in starts]
    best = min(results, key=lambda r: (r['trace_gap'], r['residual_norm']))
    return {
        'method': method,
        'n_starts': int(len(results)),
        'best_trace_gap': float(best['trace_gap']),
        'best_residual_norm': float(best['residual_norm']),
        'best_nfev': int(best['nfev']),
        'total_nfev': int(sum(r['nfev'] for r in results)),
        'n_trace_pass': int(sum(r['trace_gap'] < RECOVERY_TOL for r in results)),
        'scientific_support': bool(best['trace_gap'] < RECOVERY_TOL),
    }


def de_smooth_lsq(shard, theta, target):
    def smooth_obj(u):
        r = residual_vector(u, theta, target)
        return float(np.dot(r, r))
    de = differential_evolution(
        smooth_obj, [(0.0, 1.0)] * DIM,
        seed=63000 + shard, maxiter=DE_MAXITER, popsize=DE_POPSIZE,
        tol=1e-8, atol=1e-12, mutation=(0.45, 1.0), recombination=0.75,
        polish=False, workers=1, updating='immediate',
    )
    de_gap, de_rn = final_metrics(de.x, theta, target)
    lsq = run_lsq(de.x, theta, target)
    return {
        'method': 'de_smooth_lsq',
        'de_trace_gap': float(de_gap),
        'de_residual_norm': float(de_rn),
        'de_nfev': int(de.nfev),
        'de_nit': int(de.nit),
        'best_trace_gap': float(lsq['trace_gap']),
        'best_residual_norm': float(lsq['residual_norm']),
        'lsq_nfev': int(lsq['nfev']),
        'scientific_support': bool(lsq['trace_gap'] < RECOVERY_TOL),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--method', choices=['sobol_lsq', 'lhs_lsq', 'de_smooth_lsq'], required=True)
    ap.add_argument('--shard', type=int, choices=range(4), required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    theta, target = target_for(a.shard)
    if a.method in ('sobol_lsq', 'lhs_lsq'):
        r = multistart(a.method, a.shard, theta, target)
    else:
        r = de_smooth_lsq(a.shard, theta, target)

    numeric = [float(v) for v in r.values() if isinstance(v, (int, float, np.integer, np.floating)) and not isinstance(v, (bool, np.bool_))]
    structural_valid = bool(all(np.isfinite(v) for v in numeric))
    out = {
        'iteration': 'Iter015', 'gate': 'G33', 'method': a.method,
        'shard': a.shard, 'theta': theta,
        'result': r,
        'structural_valid': structural_valid,
        'frozen_thresholds': {
            'trace_distance_recovery': RECOVERY_TOL,
            'unit_box_dimension': DIM,
            'least_squares_max_nfev_per_start': LSQ_MAX_NFEV,
            'sobol_starts': SOBOL_STARTS,
            'lhs_starts': LHS_STARTS,
            'de_maxiter': DE_MAXITER,
            'de_popsize': DE_POPSIZE,
        },
        'scope_lock': 'Positive-control calibration only; hidden source coordinates forbidden as optimizer initializers; no RCG-002 adversarial target.',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))
    if not structural_valid:
        raise SystemExit(2)

if __name__ == '__main__':
    main()
