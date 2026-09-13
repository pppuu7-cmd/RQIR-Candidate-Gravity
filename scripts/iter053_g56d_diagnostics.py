import argparse
import json
import math
import os
from pathlib import Path

import numpy as np
from scipy.integrate import quad

RATIOS = (0.35, 0.70, 1.20, 2.00, 3.00, 4.00)
SCALES = (0.071, 0.113, 0.173, 0.257, 0.389, 0.541)
STEP_RATIOS = (0.04, 0.02, 0.01, 0.005, 0.0025)
ORIENTATIONS = (
    np.array([1.0, 0.0, 0.0]),
    np.array([1.0, 1.0, 1.0]),
    np.array([2.0, -1.0, 3.0]),
)
ORIENTATIONS = tuple(v / np.linalg.norm(v) for v in ORIENTATIONS)
SQRT2PI = math.sqrt(2.0 / math.pi)


def kernel_r(r, s):
    if r == 0.0:
        return SQRT2PI / s
    return math.erf(r / (math.sqrt(2.0) * s)) / r


def rho_r(r, s):
    return math.exp(-0.5 * (r / s) ** 2) / ((2.0 * math.pi) ** 1.5 * s ** 3)


def enclosed_fraction(r, s):
    u = r / s
    return math.erf(u / math.sqrt(2.0)) - SQRT2PI * u * math.exp(-0.5 * u * u)


def second_derivative_5(f, x, h, axis):
    e = np.zeros(3)
    e[axis] = h
    return (-f(x + 2 * e) + 16 * f(x + e) - 30 * f(x) + 16 * f(x - e) - f(x - 2 * e)) / (12 * h * h)


def cartesian_laplacian(x, s, h):
    f = lambda y: kernel_r(float(np.linalg.norm(y)), s)
    return sum(second_derivative_5(f, x, h, a) for a in range(3))


def radial_first_5(r, s, h):
    f = lambda z: kernel_r(float(z), s)
    return (f(r - 2 * h) - 8 * f(r - h) + 8 * f(r + h) - f(r + 2 * h)) / (12 * h)


def relerr(a, b):
    return abs(a - b) / max(abs(b), 1e-300)


def convergence_orders(errors):
    out = []
    for a, b in zip(errors[:-1], errors[1:]):
        if a > 0.0 and b > 0.0 and np.isfinite(a) and np.isfinite(b):
            out.append(float(math.log(a / b, 2.0)))
        else:
            out.append(None)
    return out


def stream_d1():
    lanes = []
    original_ok = True
    for case, (u, s) in enumerate(zip(RATIOS, SCALES)):
        r = u * s
        source_lap = -4.0 * math.pi * rho_r(r, s)
        mfrac = enclosed_fraction(r, s)
        per_step = []
        lap_errors = []
        flux_errors = []
        for hs in STEP_RATIOS:
            h = hs * s
            laps = []
            for n in ORIENTATIONS:
                laps.append(float(cartesian_laplacian(r * n, s, h)))
            lap_rel = max(relerr(x, source_lap) for x in laps)
            scaled = [(s ** 3) * x for x in laps]
            spread = max(scaled) - min(scaled)
            flux = -r * r * radial_first_5(r, s, h)
            flux_err = abs(flux - mfrac)
            per_step.append({
                "h_over_s": hs,
                "worst_cartesian_laplacian_relative_error": float(lap_rel),
                "orientation_scaled_laplacian_spread": float(spread),
                "gauss_flux_absolute_error": float(flux_err),
            })
            lap_errors.append(float(lap_rel))
            flux_errors.append(float(flux_err))
            if abs(hs - 0.01) < 1e-15:
                original_ok = bool(original_ok and lap_rel <= 2e-5 and spread <= 2e-7 and flux_err <= 2e-8)
        lanes.append({
            "case": case,
            "u_r_over_s": u,
            "s": s,
            "steps": per_step,
            "laplacian_convergence_orders": convergence_orders(lap_errors),
            "gauss_flux_convergence_orders": convergence_orders(flux_errors),
        })
    return {
        "iteration": "Iter053",
        "gate": "G56-D",
        "stream": "D1_FD_CONVERGENCE",
        "lanes": lanes,
        "original_numeric_predicates_reproduced": bool(original_ok),
        "structural_valid": bool(len(lanes) == 6 and all(len(x["steps"]) == 5 for x in lanes)),
        "retroactive_rescue_allowed": False,
    }


def stream_d2():
    q = 1.3
    def ratio(u):
        return q ** -3 * math.exp(0.5 * u * u * (1.0 - q ** -2))
    u_cross = math.sqrt(6.0 * math.log(q) / (1.0 - q ** -2))
    grid = np.round(np.arange(0.10, 6.0001, 0.001), 3)
    diffs = np.array([abs(ratio(float(u)) - 1.0) for u in grid])
    mask = diffs < 0.05
    idx_cross = int(np.argmin(np.abs(grid - u_cross)))
    if not mask[idx_cross]:
        blind_interval = None
    else:
        lo = idx_cross
        hi = idx_cross
        while lo > 0 and mask[lo - 1]:
            lo -= 1
        while hi + 1 < len(mask) and mask[hi + 1]:
            hi += 1
        blind_interval = [float(grid[lo]), float(grid[hi])]
    u2_diff = abs(ratio(2.0) - 1.0)
    rho1 = lambda u: math.exp(-0.5 * u * u) / ((2.0 * math.pi) ** 1.5)
    rhoq = lambda u: math.exp(-0.5 * (u / q) ** 2) / ((2.0 * math.pi) ** 1.5 * q ** 3)
    l1, l1_err = quad(lambda u: 4.0 * math.pi * u * u * abs(rho1(u) - rhoq(u)), 0.0, 8.0,
                      epsabs=1e-12, epsrel=1e-12, limit=500)
    blind_confirmed = bool(
        blind_interval is not None
        and blind_interval[0] <= 2.0 <= blind_interval[1]
        and abs(u2_diff - 0.029913948838822833) <= 1e-12
    )
    return {
        "iteration": "Iter053",
        "gate": "G56-D",
        "stream": "D2_WIDTH_CONTROL_DISCRIMINABILITY",
        "width_factor_q": q,
        "analytic_equality_crossing_u": float(u_cross),
        "blind_interval_abs_relative_difference_lt_0p05": blind_interval,
        "u2_relative_difference": float(u2_diff),
        "case3_blind_spot_confirmed": blind_confirmed,
        "dimensionless_radial_L1_separation_0_8": float(l1),
        "quadrature_error": float(l1_err),
        "structural_valid": bool(len(grid) == 5901 and blind_interval is not None),
        "retroactive_rescue_allowed": False,
    }


def stream_d3():
    import mpmath as mp
    mp.mp.dps = 80
    us = [mp.mpf(x) for x in ("0.23", "0.51", "0.93", "1.57", "2.41", "3.73", "5.20")]
    ss = [mp.mpf(x) for x in ("0.083", "0.137", "0.191", "0.283", "0.367", "0.457", "0.613")]
    sqrt2pi = mp.sqrt(mp.mpf(2) / mp.pi)
    rows = []
    max_lap_rel = mp.mpf("0")
    max_flux_abs = mp.mpf("0")
    for u, s in zip(us, ss):
        r = u * s
        def kfun(x):
            return mp.erf(x / (mp.sqrt(2) * s)) / x
        d1 = mp.diff(kfun, r, 1)
        d2 = mp.diff(kfun, r, 2)
        lap = d2 + 2 * d1 / r
        rho = mp.e ** (-mp.mpf("0.5") * u * u) / ((2 * mp.pi) ** mp.mpf("1.5") * s ** 3)
        target_lap = -4 * mp.pi * rho
        lap_rel = abs(lap - target_lap) / abs(target_lap)
        mfrac = mp.erf(u / mp.sqrt(2)) - sqrt2pi * u * mp.e ** (-mp.mpf("0.5") * u * u)
        flux = -r * r * d1
        flux_abs = abs(flux - mfrac)
        max_lap_rel = max(max_lap_rel, lap_rel)
        max_flux_abs = max(max_flux_abs, flux_abs)
        rows.append({
            "u": str(u),
            "s": str(s),
            "laplacian_relative_error": mp.nstr(lap_rel, 20),
            "gauss_flux_absolute_error": mp.nstr(flux_abs, 20),
        })
    support = bool(max_lap_rel < mp.mpf("1e-40") and max_flux_abs < mp.mpf("1e-40"))
    return {
        "iteration": "Iter053",
        "gate": "G56-D",
        "stream": "D3_HIGH_PRECISION_IDENTITY",
        "mpmath_decimal_digits": 80,
        "points": rows,
        "max_laplacian_relative_error": mp.nstr(max_lap_rel, 30),
        "max_gauss_flux_absolute_error": mp.nstr(max_flux_abs, 30),
        "high_precision_identity_support": support,
        "structural_valid": bool(len(rows) == 7),
        "retroactive_rescue_allowed": False,
    }


def aggregate(directory):
    p = Path(directory)
    files = sorted(p.rglob("*.json"))
    data = []
    for f in files:
        with open(f) as h:
            x = json.load(h)
        if x.get("iteration") == "Iter053" and x.get("gate") == "G56-D" and x.get("stream"):
            data.append(x)
    by_stream = {x["stream"]: x for x in data}
    expected = {
        "D1_FD_CONVERGENCE",
        "D2_WIDTH_CONTROL_DISCRIMINABILITY",
        "D3_HIGH_PRECISION_IDENTITY",
    }
    structural = bool(set(by_stream) == expected and all(by_stream[k].get("structural_valid") for k in expected))
    combined = bool(
        structural
        and by_stream["D1_FD_CONVERGENCE"].get("original_numeric_predicates_reproduced")
        and by_stream["D2_WIDTH_CONTROL_DISCRIMINABILITY"].get("case3_blind_spot_confirmed")
        and by_stream["D3_HIGH_PRECISION_IDENTITY"].get("high_precision_identity_support")
    )
    diagnosis = (
        "NEGATIVE_CONTROL_LOCAL_BLIND_SPOT_WITH_INDEPENDENT_IDENTITY_SUPPORT"
        if combined else
        "MIXED_G56F_FAILURE_DIAGNOSTIC_REQUIRES_FURTHER_LOCALIZATION"
    )
    return {
        "iteration": "Iter053",
        "gate": "G56-D",
        "streams_consumed": sorted(by_stream),
        "all_streams_structural_valid": structural,
        "diagnosis": diagnosis,
        "g56f_terminal_classification_unchanged": "G56F_FROZEN_CONTINUUM_FIELD_CLOSURE_RULE_NOT_MET",
        "programme_readiness_percent": 66,
        "theory_established_percent": 0,
        "scientific_pass_for_g56f": False,
        "retroactive_rescue_allowed": False,
        "scope_lock": "Diagnostic localization of RCG-002 isotropic Gaussian weak-field source/kernel mathematics only."
    }


def write_json(obj, out):
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w") as f:
        json.dump(obj, f, indent=2)
    print(json.dumps(obj, indent=2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stream", choices=("d1", "d2", "d3"))
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    if a.aggregate_dir:
        result = aggregate(a.aggregate_dir)
    elif a.stream == "d1":
        result = stream_d1()
    elif a.stream == "d2":
        result = stream_d2()
    elif a.stream == "d3":
        result = stream_d3()
    else:
        raise SystemExit("provide --stream or --aggregate-dir")
    write_json(result, a.out)
    if not result.get("structural_valid", result.get("all_streams_structural_valid", False)):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
