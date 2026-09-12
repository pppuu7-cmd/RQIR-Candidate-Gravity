# Wave 33 preregistration — FRG basis ingest and surrogate machinery

Status: **FROZEN BEFORE COMPUTE**
Date: 2026-09-12
Branch: `frg-basis-ingest-wave33`

## Scientific boundary

Wave 33 does **not** promote the Appendix-F / Truncation-4 analytic system to physical J8 evidence. The best F1 realization remains blocked until a reusable numerical 5x5 stability matrix under one frozen closure, or an equivalent normalized right-eigenvector basis, is available.

The analytic Truncation-4 spectrum is used only as a surrogate input to test the downstream machinery.

## Frozen input contract

Coordinates: `(mu, lambda3, lambda4, g3, g4)`.

Physical J8 input must provide either:

1. a real 5x5 stability matrix with metadata identifying the closure and fixed point; or
2. a normalized right-eigenvector basis plus eigenvalues in the same five coordinates.

For one real attractive eigenvalue plus one attractive complex-conjugate pair, the physical real relevant subspace has dimension 3. A complex eigenvector `v=a+i b` is realified as the two-dimensional plane spanned by `a` and `b`.

## Frozen surrogate

Truncation-4 / Section-6 analytic-flow surrogate fixed point:
`(-0.23, -0.060, -0.11, 0.64, 0.55)`.

Published first-approximation spectrum used only for machinery testing:
`(-3.0, -1.9+1.6i, -1.9-1.6i, 1.7, 3.4)`.

Classification is permanently `SURROGATE_NOT_J8`.

## Predeclared tests

1. `ingest_schema`: reject wrong matrix shape, non-finite entries, coordinate mismatch, and incomplete metadata; accept a valid 5x5 object.
2. `complex_realification`: one real attractive mode plus one attractive complex pair yields a rank-3 real orthonormal basis.
3. `phase_invariance`: multiplying the complex eigenvector by arbitrary complex phase must leave the real 2-plane projector invariant to numerical tolerance.
4. `matrix_basis_equivalence`: matrix ingest and direct-eigenbasis ingest produce the same relevant projector for a controlled test object.
5. `seven_trajectory_generator`: produce exactly `x*` and `x* ± eps v_i` for i=1..3; opposite pairs must cancel around the fixed point.
6. `normalization_invariance`: rescaling input eigenvectors must not alter generated unit-direction trajectories.
7. `uncertainty_subspace_stress`: small matrix perturbations must generate a finite distribution of projector/principal-angle changes and retain dimension 3 while the spectral gap is not crossed.
8. `surrogate_firewall`: every surrogate output must carry `SURROGATE_NOT_J8`; no Wave-33 surrogate artifact may claim physical J8 closure.
9. `information_firewall`: no polygon/KMQGB-derived QGR equation, architecture, fitted parameter, or repair is admitted.

## Pass rule

Wave 33 is PASS only if every predeclared signal is true in the aggregator. PASS means **machinery ready**, not physical J8 ready.

Expected scientific route after PASS: attempt a strictly partial Appendix-F projected-Jacobian audit (Wave 34) while keeping full best-realization J8 blocked.
