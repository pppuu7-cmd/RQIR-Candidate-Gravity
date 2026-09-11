#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

OUT = Path("compute_results")
OUT.mkdir(exist_ok=True)

# Positive symmetric discrete distributions on x in {-3,...,3}.
# We fix L1-L3 moment data: normalization, mean=0, variance=1, third moment=0,
# plus exact parity symmetry p(x)=p(-x), and optimize the fourth cumulant.
# Then we additionally fix a Gaussian-like fourth moment E[x^4]=3 and optimize
# the sixth cumulant. This is a finite counterexample test for cross-order closure.

x = np.arange(-3, 4, dtype=float)
n = len(x)

rows = [np.ones(n), x, x**2, x**3]
vals = [1.0, 0.0, 1.0, 0.0]
# parity constraints p(-a)-p(a)=0 for a=1,2,3
for a in [1, 2, 3]:
    row = np.zeros(n)
    row[np.where(x == -a)[0][0]] = 1.0
    row[np.where(x == a)[0][0]] = -1.0
    rows.append(row)
    vals.append(0.0)
Aeq = np.vstack(rows)
beq = np.array(vals)
bounds = [(0.0, 1.0)] * n

m4 = x**4
lo4 = linprog(m4, A_eq=Aeq, b_eq=beq, bounds=bounds, method="highs")
hi4 = linprog(-m4, A_eq=Aeq, b_eq=beq, bounds=bounds, method="highs")
if not (lo4.success and hi4.success):
    raise RuntimeError(f"L4 LP failed: {lo4.message} / {hi4.message}")

E4_min = float(lo4.fun)
E4_max = float(-hi4.fun)
k4_min = E4_min - 3.0  # mean 0, variance 1
k4_max = E4_max - 3.0

# Now fix E4=3 (kappa4=0) and optimize E6. For symmetric mean-zero unit-variance
# distributions with third moment zero and E4 fixed, kappa6 = E6 - 15 E4 E2 + 30 E2^3
# = E6 - 45 + 30 = E6 - 15.
Aeq6 = np.vstack([Aeq, m4])
beq6 = np.concatenate([beq, [3.0]])
m6 = x**6
lo6 = linprog(m6, A_eq=Aeq6, b_eq=beq6, bounds=bounds, method="highs")
hi6 = linprog(-m6, A_eq=Aeq6, b_eq=beq6, bounds=bounds, method="highs")
if not (lo6.success and hi6.success):
    raise RuntimeError(f"L6 LP failed: {lo6.message} / {hi6.message}")

E6_min = float(lo6.fun)
E6_max = float(-hi6.fun)
k6_min = E6_min - 15.0
k6_max = E6_max - 15.0

summary = {
    "test": "finite positive symmetric moment/cumulant hierarchy closure",
    "support": [float(v) for v in x],
    "fixed_L1_L3": {"mean": 0.0, "variance": 1.0, "third_moment": 0.0, "parity": True},
    "L4": {
        "E4_min": E4_min,
        "E4_max": E4_max,
        "kappa4_min": k4_min,
        "kappa4_max": k4_max,
        "kappa4_width": k4_max - k4_min,
        "p_at_min": [float(v) for v in lo4.x],
        "p_at_max": [float(v) for v in hi4.x],
    },
    "L6_given_E4_3": {
        "E6_min": E6_min,
        "E6_max": E6_max,
        "kappa6_min": k6_min,
        "kappa6_max": k6_max,
        "kappa6_width": k6_max - k6_min,
        "p_at_min": [float(v) for v in lo6.x],
        "p_at_max": [float(v) for v in hi6.x],
    },
    "scope": "finite classical-positive moment proxy for cross-order underdetermination; not a QFT/gravity theorem",
}

(OUT / "cumulant_hierarchy.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
lines = [
    "# Cumulant hierarchy uniqueness test",
    "",
    "Fixed: normalization, parity, mean=0, variance=1, third moment=0.",
    "",
    f"- Allowed fourth cumulant range: **[{k4_min:.6g}, {k4_max:.6g}]** (width {k4_max-k4_min:.6g}).",
    f"- After additionally fixing `E[x^4]=3` (`kappa4=0`), allowed sixth cumulant range: **[{k6_min:.6g}, {k6_max:.6g}]** (width {k6_max-k6_min:.6g}).",
    "",
    "Nonzero widths give explicit positive distributions sharing all lower-order constraints but differing at the next order.",
]
(OUT / "cumulant_hierarchy.md").write_text("\n".join(lines), encoding="utf-8")
print(json.dumps(summary, indent=2))
