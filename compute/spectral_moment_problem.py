#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

OUT = Path("compute_results")
OUT.mkdir(exist_ok=True)

# Finite positive spectral proxy. The massless C5 pole is conceptually treated as
# the fixed low-energy root; here we ask whether finitely many moments of an
# additional positive spectral sector uniquely select its spectral weights.
# Nodes are fixed only to make the truncated moment problem computable.

m2 = np.array([1.0, 2.0, 4.0, 8.0, 16.0, 32.0])
n = len(m2)
w_ref = np.ones(n) / n

# inverse moments are the natural low-energy expansion coefficients of many
# Stieltjes-type response functions: M_k = sum_i w_i / (m_i^2)^k.
def moment_vector(k):
    return 1.0 / (m2 ** k)

records = []
for r in range(1, 5):
    # constraints: normalization plus first r inverse moments fixed to a strictly
    # positive interior reference distribution.
    Aeq = [np.ones(n)] + [moment_vector(k) for k in range(1, r + 1)]
    beq = [1.0] + [float(moment_vector(k) @ w_ref) for k in range(1, r + 1)]
    Aeq = np.vstack(Aeq)
    beq = np.array(beq)

    target = moment_vector(r + 1)
    lo = linprog(target, A_eq=Aeq, b_eq=beq, bounds=[(0.0, None)] * n, method="highs")
    hi = linprog(-target, A_eq=Aeq, b_eq=beq, bounds=[(0.0, None)] * n, method="highs")
    if not (lo.success and hi.success):
        raise RuntimeError(f"Moment LP failed at r={r}: {lo.message} / {hi.message}")

    rank = int(np.linalg.matrix_rank(Aeq, tol=1e-11))
    affine_nullity = n - rank
    vmin = float(lo.fun)
    vmax = float(-hi.fun)
    records.append({
        "fixed_inverse_moments": r,
        "constraint_rank": rank,
        "affine_nullity_before_positivity_faces": affine_nullity,
        "next_moment_order": r + 1,
        "next_moment_min": vmin,
        "next_moment_max": vmax,
        "range_width": vmax - vmin,
        "unique_at_tolerance_1e-10": abs(vmax - vmin) < 1e-10,
        "weights_at_min": [float(x) for x in lo.x],
        "weights_at_max": [float(x) for x in hi.x],
    })

summary = {
    "test": "positive finite-grid spectral moment uniqueness",
    "nodes_m2": [float(x) for x in m2],
    "reference_weights": [float(x) for x in w_ref],
    "scope": "finite proxy for a positive spectral/Stieltjes sector; not a continuum uniqueness theorem",
    "records": records,
}
(OUT / "spectral_moment_problem.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

lines = [
    "# Positive spectral moment problem",
    "",
    "A six-node positive spectral proxy is constrained by normalization and the first `r` inverse moments. We then optimize the next inverse moment.",
    "",
    "| fixed moments r | affine nullity | next moment min | next moment max | width | unique? |",
    "|---:|---:|---:|---:|---:|:---:|",
]
for rec in records:
    lines.append(
        f"| {rec['fixed_inverse_moments']} | {rec['affine_nullity_before_positivity_faces']} | "
        f"{rec['next_moment_min']:.9g} | {rec['next_moment_max']:.9g} | "
        f"{rec['range_width']:.9g} | {rec['unique_at_tolerance_1e-10']} |"
    )
lines += [
    "",
    "A nonzero optimized range proves non-uniqueness on this finite positive proxy even after the listed low-energy moments are fixed.",
]
(OUT / "spectral_moment_problem.md").write_text("\n".join(lines), encoding="utf-8")
print(json.dumps(summary, indent=2))
