# Iter074 / G76 — C/D near-alias conditioning robustness — TERMINAL

Date: 2026-09-13

Classification: `G75_EXACT_IDENTIFIABILITY_DEGRADES_CONTINUOUSLY_TOWARD_ALIAS_SCOPED`
Scientific status: **PASS, scoped**
Programme readiness: **66%**
Theory established: **0%**

## Frozen authority
- preregistration: `7ede8341aea99338d250a6eba8522378aee8cca8`
- implementation: `3be0d3569596256f61c0931b4d40b1ce8f19713b`
- production head: `3a983cbd4490bf1a1bb284e3f25227d05f268680`
- run: `34782314724`
- jobs: A `103791437374`, B `103791437309`, C `103791437350`, D `103791437160`, aggregate `103791568561`
- artifacts/digests:
  - A `10325013006`, `sha256:1a8746559dcc3743fee83aed216ecff87c418c9622464226690d32fc0cb3386b`
  - B `10325735185`, `sha256:38008b5b4c73e62f268654e74f80d3d11069b22a7b65a93b9ad3eb93b02e6220`
  - C `10325780136`, `sha256:889866c92c1c333be601c487ed89f736ae6001253be3bf6903733e9a727b4817`
  - D `10324824728`, `sha256:51acb114351cd178c9e3aa81e4d20d88ddee70f132dfa1ffd0eb53f6c5852e16`
  - aggregate `10324864695`, `sha256:1d9124e8be09bc07a03a874fc5e183c2573a4b76991d38eba5ae6c92d6455e70`

## Frozen result
All four raw streams were consumed and their prospective predicates were validated before terminal classification.

- A `DIRECT_ANCHOR_STRENGTH_CONDITIONING_SCOPED`: rank remains four for every frozen nonzero anchor strength down to `a=1e-6`; the smallest singular value falls monotonically from about `0.618` to `7.07e-7`, the condition number rises from about `6.40` to `5.50e6`, and the exact zero-anchor control has rank two.
- B `NEAR_SHAPE_APPROACH_TO_ALIAS_CONDITIONING_SCOPED`: for `delta` from `1` to `1e-6`, rank remains four while the smallest singular value falls to about `5.00e-7` and the condition number rises to about `8.86e6`; the exact alias control has rank two.
- C `HELDOUT_AND_ORTHOGONAL_COORDINATE_ROBUSTNESS_SCOPED`: all frozen held-out panels remain rank four for nonzero anchors, and singular spectra are invariant under the frozen orthogonal parameter transformations to numerical relative errors of order `1e-16`.
- D `PRECISION_CONVERGENCE_AND_FALSE_POSITIVE_CALIBRATION_SCOPED`: float64 and the independent 80-digit high-precision route agree on extremal singular values far inside the frozen `1e-8` tolerance; exact zero/same-shape controls remain below the frozen singular-value threshold and a one-sided anchor remains rank three.

## Scientific interpretation
G75 exact algebraic identifiability is continuously lost as independent anchor strength vanishes or an added response approaches the exact same-shape nuisance alias. Full rank by itself therefore does not imply useful numerical separation. The conclusion is restricted to the frozen normalized tangent designs and controls.

## Scope ceiling
This result does **not** define a physical detectability threshold, establish physically realizable anchors, select C or D, determine physical coefficients, define candidate-owned RCG-002 dynamics, establish nonlinear/quantum closure, or establish new physics.

## Parallel continuation
Independent sibling audits G77/G78/G79 were prospectively frozen from terminal G75 without consuming G76 results: statistical estimator-noise amplification, row-deletion/redundancy structure, and GLS correlated-noise robustness respectively. Their outcomes must be classified independently before any synthesis.
