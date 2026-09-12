# ITER025D / G42-C3 — preregistered PSD boundary rank-completion calibration

Purpose: complete positive-control coverage of the boundary-capable bounded real-PSD 6x6 classical Kossakowski search before any broad arbitrary-orientation adversarial gate. G42-C2 covers intended ranks 2/4/5/6; G42-C3 independently covers the missing boundary ranks 1 and 3.

This protocol is frozen before the G42-C2 aggregate verdict. G42-C2 is not modified or reinterpreted.

Frozen family/search:
- exactly the G42-C2 direct lower-triangular coordinates `C=B B^T`;
- diagonal bounds `[0,0.60]`, strict-lower bounds `[-0.30,0.30]`;
- same times `(0.15,0.45,0.9,1.4)`, same six product probes, same Sobol/LHS constructions, 32 starts, top-6 bounded least-squares refinements, `max_nfev=1000`, and `ftol=xtol=gtol=1e-10`;
- exact hidden coordinates are never starts;
- no RCG-002 target.

Frozen hidden controls:
- four deterministic controls independent of RCG-002: two intended-rank-1 controls and two intended-rank-3 controls;
- active Cholesky columns have strictly positive pivots and seeded lower entries; inactive columns are exactly zero.

Frozen lane support:
- max output-state trace-distance gap `<0.002`;
- relative Kossakowski Frobenius error `<0.02`;
- recovered effective Kossakowski rank at eigenvalue threshold `1e-5` equals the hidden intended rank;
- all diagnostics finite and PSD by construction.

Overall PASS requires 4/4 Sobol and 4/4 LHS support.

Authorization lock:
- a broad boundary-capable arbitrary-orientation PSD adversarial gate is authorized only if **both G42-C2 and G42-C3 terminally PASS**;
- failure of either blocks that adversarial gate; no rank threshold, family bounds, controls, starts, probes, times, budgets or recovery tolerances may be changed inside these runs;
- calibration does not increase readiness.
