#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

OUT = Path("compute_results")
OUT.mkdir(exist_ok=True)

# Pauli channel p=(p_I,p_X,p_Y,p_Z), p_i>=0, sum p_i=1.
# Bloch contractions:
# lambda_x = pI+pX-pY-pZ
# lambda_y = pI-pX+pY-pZ
# lambda_z = pI-pX-pY+pZ
# We fix lambda_z=eta and impose axial symmetry lambda_x=lambda_y.
# If lambda_perp still spans an interval, CPTP + symmetry + fixed transfer
# does not select a unique channel.

lx = np.array([1.0, 1.0, -1.0, -1.0])
ly = np.array([1.0, -1.0, 1.0, -1.0])
lz = np.array([1.0, -1.0, -1.0, 1.0])
ones = np.ones(4)

results = []
for eta in [0.0, 0.25, 0.5, 0.75, 0.95, 1.0]:
    Aeq = np.vstack([ones, lz, lx-ly])
    beq = np.array([1.0, eta, 0.0])
    bounds = [(0.0, 1.0)] * 4

    lo = linprog(lx, A_eq=Aeq, b_eq=beq, bounds=bounds, method="highs")
    hi = linprog(-lx, A_eq=Aeq, b_eq=beq, bounds=bounds, method="highs")
    if not (lo.success and hi.success):
        raise RuntimeError(f"LP infeasible for eta={eta}: {lo.message} / {hi.message}")

    lmin = float(lo.fun)
    lmax = float(-hi.fun)
    width = lmax - lmin
    results.append({
        "eta": eta,
        "lambda_perp_min": lmin,
        "lambda_perp_max": lmax,
        "interval_width": width,
        "p_at_min": [float(x) for x in lo.x],
        "p_at_max": [float(x) for x in hi.x],
        "unique_at_tolerance_1e-9": abs(width) < 1e-9,
    })

summary = {
    "test": "CPTP Pauli-channel uniqueness under fixed lambda_z and axial symmetry",
    "interpretation_scope": "finite qubit-channel proxy for process-level closure; not a gravity theorem",
    "results": results,
    "all_nontrivial_eta_unique": all(r["unique_at_tolerance_1e-9"] for r in results if r["eta"] < 1.0),
}

(OUT / "channel_polytope.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

lines = [
    "# Channel-polytope uniqueness result",
    "",
    "Fixed constraints: CPTP Pauli channel, axial symmetry `lambda_x=lambda_y`, and fixed `lambda_z=eta`.",
    "",
    "| eta | lambda_perp min | lambda_perp max | width | unique? |",
    "|---:|---:|---:|---:|:---:|",
]
for r in results:
    lines.append(f"| {r['eta']:.2f} | {r['lambda_perp_min']:.6g} | {r['lambda_perp_max']:.6g} | {r['interval_width']:.6g} | {r['unique_at_tolerance_1e-9']} |")
lines += [
    "",
    "A nonzero interval is an explicit CPTP family sharing the same fixed low-order transfer and symmetry.",
]
(OUT / "channel_polytope.md").write_text("\n".join(lines), encoding="utf-8")

print(json.dumps(summary, indent=2))
