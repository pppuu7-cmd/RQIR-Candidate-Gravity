#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

OUT = Path("wave2_results")
OUT.mkdir(exist_ok=True)

# Gravity-specific finite proxy:
#   D_TT(Q^2) = 1/Q^2 + sum_i w_i/(Q^2 + M_i^2),  w_i >= 0.
# The unit-residue massless pole is fixed to the GR value. Positive massive
# residues model a ghost-free positive spectral correction in the TT sector.
# At low Q^2, the massive correction has coefficients
#   c_n = (-1)^n sum_i w_i/(M_i^2)^(n+1).
# We ask whether finitely many c_n fix the next coefficient / spectral weights.

M2 = np.array([1.0, 2.0, 4.0, 8.0, 16.0, 32.0])
n = len(M2)
w_ref = np.ones(n) / n

def invpow(p):
    return 1.0 / (M2 ** p)

records = []
for r in range(1, 5):
    # Normalize total positive massive spectral weight and fix r low-energy
    # coefficients (equivalently inverse moments powers 1..r).
    Aeq = [np.ones(n)] + [invpow(p) for p in range(1, r + 1)]
    beq = [1.0] + [float(invpow(p) @ w_ref) for p in range(1, r + 1)]
    Aeq = np.vstack(Aeq)
    beq = np.array(beq)

    target = invpow(r + 1)
    lo = linprog(target, A_eq=Aeq, b_eq=beq, bounds=[(0.0, None)] * n, method="highs")
    hi = linprog(-target, A_eq=Aeq, b_eq=beq, bounds=[(0.0, None)] * n, method="highs")
    if not (lo.success and hi.success):
        raise RuntimeError(f"spin-2 spectral LP failed r={r}: {lo.message} / {hi.message}")

    rank = int(np.linalg.matrix_rank(Aeq, tol=1e-11))
    vmin = float(lo.fun)
    vmax = float(-hi.fun)
    records.append({
        "fixed_low_energy_coefficients": r,
        "constraint_rank": rank,
        "spectral_affine_nullity": n - rank,
        "next_inverse_moment_min": vmin,
        "next_inverse_moment_max": vmax,
        "width": vmax - vmin,
        "unique": abs(vmax - vmin) < 1e-10,
        "weights_min": [float(x) for x in lo.x],
        "weights_max": [float(x) for x in hi.x],
    })

# Also optimize a finite Euclidean momentum response after fixing first 2 moments.
r = 2
Aeq = np.vstack([np.ones(n), invpow(1), invpow(2)])
beq = np.array([1.0, float(invpow(1)@w_ref), float(invpow(2)@w_ref)])
finite_q = []
for Q2 in [0.25, 1.0, 4.0, 10.0]:
    response = 1.0/(M2 + Q2)
    lo = linprog(response, A_eq=Aeq, b_eq=beq, bounds=[(0.0,None)]*n, method="highs")
    hi = linprog(-response, A_eq=Aeq, b_eq=beq, bounds=[(0.0,None)]*n, method="highs")
    if not (lo.success and hi.success):
        raise RuntimeError("finite-Q response LP failed")
    finite_q.append({"Q2":Q2,"corr_min":float(lo.fun),"corr_max":float(-hi.fun),"width":float(-hi.fun-lo.fun)})

summary = {
    "test":"TT propagator with fixed unit GR massless pole plus positive massive spectral sector",
    "mass_squared_nodes":[float(x) for x in M2],
    "fixed_massless_pole_residue":1.0,
    "positive_massive_residues":True,
    "records":records,
    "finite_Q_after_two_low_energy_coefficients":finite_q,
    "scope":"finite spectral proxy for the physical TT two-point sector; not a continuum Kallen-Lehmann uniqueness theorem"
}
(OUT/"spin2_positive_spectral.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
