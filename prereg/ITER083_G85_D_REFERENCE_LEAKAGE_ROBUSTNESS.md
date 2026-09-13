# Iter083 / G85 — D reference-channel leakage / imperfect-decoupling robustness

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/RESULTS**
Date: 2026-09-13
Parallel status: **D-SPECIFIC SIBLING OF G84-C; COMMON BASE IS POST-G83 MAIN**

## Scope
G83 established a construction-sufficiency witness using one ideal candidate-blind retarded D nuisance-reference row `(0,q)`. G85 relaxes that idealization without changing the D candidate cubic functional. It asks how local identifiability degrades when the reference channel has candidate leakage and/or weakening nuisance gain.

This is still a finite construction-robustness audit. No physical cubic-source preparation or detector model is claimed.

## Frozen design
Science coordinates remain `(D,N3)` with identical source-resolved columns from the frozen G72 retarded symmetric cubic kernel.

An imperfect reference row is
`R_D(epsilon,q)=(epsilon,q)`.
Define leakage ratio `rho=epsilon/q` for `q != 0`. The exact same-shape/non-informative boundary is `rho=+1`, where `R_D` is proportional to the science direction `(1,1)`.

Frozen leakage ratios:
`rho in {0, 1/10, -1/10, 1/2, -1/2, 9/10, 99/100, 999/1000}`.
Frozen approach-to-boundary sequence:
`rho in {0,1/2,9/10,99/100,999/1000}`.
Frozen gain sequence at fixed `rho=1/10`:
`q in {1,1e-1,1e-2,1e-3,1e-4,1e-5,1e-6}`.
Numerical SVD tolerance: `1e-12`.

The G83 source-defined reference kernel remains the frozen symmetric retarded two-entry kernel with exact squared norm `q_ref=2`.

## Independent streams
### A — exact leakage boundary
Using all nonzero source-resolved entries of the frozen candidate D kernel, for every frozen leakage ratio away from `rho=1`, exact rank of science plus one reference row must be two. At exactly `rho=1`, exact rank must be one. Science-only rank remains one.

### B — continuous conditioning toward same-shape leakage
With `q=1`, along the frozen approach-to-boundary sequence require:
- numerical rank two at tolerance `1e-12` for every `rho < 1` in the sequence;
- smallest singular value strictly decreases as `rho -> 1`;
- condition number strictly increases;
- exact `rho=1` control is rank one.

### C — nuisance-gain weakening with inherited retarded/source constraints
At fixed `rho=1/10`, for every frozen nonzero q require exact and numerical rank two. Smallest singular value must strictly decrease and condition number strictly increase as q weakens. `q=0` with epsilon=0 returns science rank one.

Reconstruct candidate and G83 reference kernels. Require both to remain exactly retarded and Sigma-symmetric, candidate CTP normalization to remain exact, and candidate Hessian/third-derivative structure to remain unchanged. With `q=q_ref`, every frozen non-boundary leakage ratio must give rank two.

### D — precision and false-reference controls
For cases `(rho,q)={(0,1),(9/10,1),(999/1000,1),(1/10,1e-6)}`, compare float64 extremal singular values to an independent 80-digit eigenvalue route on `M^T M`; relative disagreement must be `<1e-8`.

Frozen controls:
- exact same-kernel row `(q,q)` gives rank one;
- zero row `(0,0)` gives rank one;
- candidate-only row `(q,0)` gives rank two but is flagged as **not an accepted nuisance reference**;
- an advanced-support reference kernel is detected and rejected;
- changing only leakage/gain must not alter any candidate K3 entry or frozen jet property.

## Frozen aggregate rule
All streams valid =>
`D_REFERENCE_CONSTRUCTION_REMAINS_IDENTIFIABLE_UNDER_FROZEN_LEAKAGE_UNTIL_SAME_SHAPE_LIMIT_SCOPED`.

Any failed scientific predicate => `SCIENTIFIC_FAIL_FROZEN_D_REFERENCE_LEAKAGE_ROBUSTNESS`.
Missing/invalid artifacts or precision control => `INFRASTRUCTURE_OR_GATE_INVALID`.

## Interpretation ceiling
PASS means only that the G83 reference-channel construction remains algebraically identifiable over the frozen imperfect-decoupling family and degrades continuously toward the exact same-shape boundary or zero gain. It does not establish that such leakage bounds, reference gains, retarded reference sources or calibration are physically achievable.

Readiness remains 66%; theory established remains 0%.
