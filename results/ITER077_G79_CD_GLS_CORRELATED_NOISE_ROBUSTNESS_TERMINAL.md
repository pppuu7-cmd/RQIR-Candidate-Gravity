# Iter077 / G79 — C/D GLS correlated-noise robustness — TERMINAL

Date: 2026-09-13

Classification: `G75_SPD_GLS_IDENTIFIABILITY_PERSISTS_WHILE_WEAK_ANCHOR_VARIANCE_GROWS_SCOPED`
Scientific status: **PASS, scoped**
Programme readiness: **66%**
Theory established: **0%**

## Frozen authority
- sibling base: terminal G75 commit `c91151054a460cb804f054fc4eb81eedff08945a`
- preregistration: `33d2e5c2796cf31935a4011251b3e1b7053ffb28`
- implementation: `453db6d07ed1225161beb43903ca3360db638258`
- production head: `3ef34d8f56ce2025cd97ef99eae11fa5ffcbabb5`
- branch: `g79-gls-correlated-noise`
- run: `34782623331`
- jobs: A `103792280125`, B `103792280107`, C `103792279994`, D `103792280124`, aggregate `103792333378`
- artifacts/digests:
  - A `10325715659`, `sha256:15693812e4eab5f4af211d065bfa51f19ad1f947df431bd185b67e7820c7fba1`
  - B `10325583530`, `sha256:21e7503f5f062ed8c5033bff3238502c4ea2ae2b6fb8c2a3f8ed5b5e0d3d13b0`
  - C `10325324464`, `sha256:8445744839a0e9d0fcad9a5f5f342074da19d1d5d7403bafcce64c3f5a7dae07`
  - D `10324504034`, `sha256:9b01790471e40b3373fc8ae5709b3656d0e5b76f5eb59e37e915efe11b669f2f`
  - aggregate `10325004941`, `sha256:c234cde41380cbd64a24c13ccc3a3aafa2d22c534520f16ea7c775e4e9904281`

## Frozen result
All four raw streams and the frozen aggregate were independently rechecked against the preregistered predicates before terminal classification.

- A `SPD_GLS_FULL_RANK_WITH_WEAK_ANCHOR_VARIANCE_GROWTH_SCOPED`: across all four frozen SPD covariance surrogates and all nonzero anchor strengths, the GLS Fisher matrix remains rank four with positive minimum eigenvalue. C and D variances increase strictly as anchors weaken. The smallest frozen positive Fisher eigenvalue is `4.1666667894e-09`.
- B `CHOLESKY_AND_EIGEN_WHITENING_AGREE_SCOPED`: Cholesky and symmetric-eigendecomposition whitening routes agree on the Fisher matrix to maximum relative discrepancy `8.7358725667e-16`, well inside the frozen `1e-10` tolerance.
- C `ORTHOGONAL_GLS_FISHER_SPECTRUM_INVARIANCE_SCOPED`: frozen orthogonal parameter-coordinate transformations preserve the Fisher spectrum to maximum relative error `2.6261104101e-11`, below the frozen `1e-8` tolerance.
- D `SINGULAR_COVARIANCE_AND_ONE_SIDED_GLS_CONTROLS_SCOPED`: the prospectively frozen singular covariance is rejected by the inverse-based GLS route, and AQ-only/AD-only parameter-column designs each remain rank three.

## Scientific interpretation
Within the prospectively frozen G75 tangent design, positive-definite correlated/heteroscedastic row weighting does not remove local algebraic GLS identifiability, but uncertainty still grows sharply as independent alias-breaking anchors weaken. The conclusion is scientifically independent from G76/G77/G78 because G79 was frozen directly from terminal G75.

## Scope ceiling
This result does **not** identify a physical apparatus covariance model, define a signal-to-noise requirement or physical detectability threshold, establish physically realizable anchors, select C or D, define candidate-owned RCG-002 dynamics, establish nonlinear/quantum closure, or establish new physics.
