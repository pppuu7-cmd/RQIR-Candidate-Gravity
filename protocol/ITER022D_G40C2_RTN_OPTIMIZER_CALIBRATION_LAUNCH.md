# ITER022D / G40-C2 — corrected strict-BLP RTN optimizer calibration

Authorized only after terminal G40-C2-E eligibility PASS. The original G40-C remains frozen as a protocol-design failure and is not retroactively modified.

Frozen before G40-C2 results:
- same G40-C 8-parameter RTN family, parameter bounds, four trajectory times, six product probes, Sobol/LHS start constructions, 16 starts, top-4 refinement and max_nfev=600;
- same scientific recovery metric: maximum trace distance `<0.002`;
- same strict information-backflow rule: recovered BLP total positive increment `>0.02`;
- controls 0/1/2 are exactly unchanged from G40-C;
- control 3 is the new control prospectively certified by G40-C2-E, with target BLP ≈0.16064;
- hidden controls are never inserted into optimizer starts;
- both methods must recover all four controls;
- no result-dependent changes.

PASS only calibrates the strict-BLP hidden-classical RTN comparator and may authorize a separate RCG-002 adversarial gate. It is not novelty evidence or a no-go theorem.
