# Iter075 / G77 — C/D anchored estimator statistical-noise robustness — TERMINAL

Date: 2026-09-13

Classification: `G75_ANCHORED_ESTIMATOR_VARIANCE_GROWS_AS_ANCHORS_WEAKEN_SCOPED`
Scientific status: **PASS, scoped**
Programme readiness: **66%**
Theory established: **0%**

## Frozen authority
- sibling base: terminal G75 commit `c91151054a460cb804f054fc4eb81eedff08945a`
- preregistration: `a129e300ab7f9417f75ca9225d3310148f8434c3`
- implementation: `dcc92b98c2250f08e4c2eff2d2176803e89e3f83`
- production head: `b8a72889133a99eb78a57ea70b4f2344d7f4d49f`
- branch: `g77-statistical-noise-robustness`
- run: `34782611134`
- jobs: A `103792245334`, B `103792245594`, C `103792245494`, D `103792245557`, aggregate `103792282451`
- artifacts/digests:
  - A `10324974927`, `sha256:f0f77efd10aefa2db79e03e3740b9d653e00676a8b2e4718adb103959f375ea9`
  - B `10325224653`, `sha256:71f6cbdb68d3a322300f368f3052e0e909f5e3350bd27d578caa20a53d06ebae`
  - C `10325690793`, `sha256:3416425ecf822651f061ae692c2958f9460a50aa382b7e3bca8634ab67ebd7fc`
  - D `10325139808`, `sha256:44470b7a5244e60a61703d2963c36c03924c984feba792440391d2f438d745b8`
  - aggregate `10325735611`, `sha256:fe26c1f3939d0af34c2cd2ad0c9412787c73f06effd401e366389c38d79d0e39`

## Frozen result
All four raw streams and the frozen aggregate were independently rechecked against the preregistered predicates before terminal classification.

- A `ANALYTIC_ESTIMATOR_VARIANCE_WEAK_ANCHOR_AMPLIFICATION_SCOPED`: on the primary and both held-out panels, every nonzero frozen anchor strength retains rank four, while C variance, D variance and maximum parameter variance increase strictly as `a` decreases. At `a=0`, the exact-alias design has rank two.
- B `GAUSSIAN_COVARIANCE_SIGMA2_SCALING_SCOPED`: `Cov/sigma^2` agrees with `(M^T M)^(-1)` across all frozen `(a,sigma)` cases with maximum relative discrepancy below `2e-16`, far inside the frozen `1e-11` tolerance.
- C `FIXED_SEED_MONTE_CARLO_COVARIANCE_REPLICATION_SCOPED`: with seed `76077`, `12000` draws and `sigma=0.02`, the maximum covariance-diagonal relative error is `0.0286502711`, below the frozen `0.08` ceiling.
- D `ORTHOGONAL_PARAMETER_COVARIANCE_AND_ONE_SIDED_CONTROL_SCOPED`: frozen orthogonal coordinate transformations preserve the covariance spectrum within maximum relative error `1.3222521305e-09`, below the frozen `1e-8` tolerance; AQ-only and AD-only controls each remain rank three.

## Scientific interpretation
Within the prospectively frozen linear G75 tangent design and iid Gaussian row-noise surrogate, exact alias-breaking remains statistically fragile as anchors weaken: estimator variance grows rapidly even while the design retains algebraic rank four. This is consistent with, but scientifically independent from, G76 conditioning because G77 was frozen from terminal G75 without consuming G76 results.

## Scope ceiling
This result does **not** define a physical detector/noise model, signal-to-noise requirement, physical detectability threshold, physically realizable anchors, architecture selection, candidate-owned RCG-002 dynamics, nonlinear/quantum closure, or new physics.
