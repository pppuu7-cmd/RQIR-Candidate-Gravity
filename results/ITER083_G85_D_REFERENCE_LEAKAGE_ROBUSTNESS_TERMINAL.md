# Iter083 / G85 — D reference-channel leakage robustness — TERMINAL

Date: 2026-09-13

Classification: `D_REFERENCE_CONSTRUCTION_REMAINS_IDENTIFIABLE_UNDER_FROZEN_LEAKAGE_UNTIL_SAME_SHAPE_LIMIT_SCOPED`
Scientific status: **PASS, scoped construction robustness**
Programme readiness: **66%**
Theory established: **0%**

## Frozen authority
- common base: `27bc7d7622d681a977a31ef040665f3b4defc49b`
- preregistration: `aa64e9a75ec7ed6b2162413232b8fa4cd00b9b8e`
- implementation: `3d90591276ba089b3a2ce1593c0de582b2a53c09`
- production head: `db783513ec3940f402c61f71f1f61ff5c0e4d4e3`
- branch: `g85-d-reference-leakage-robustness`
- run: `34783869306`
- jobs: A `103795681799`, B `103795681796`, C `103795681788`, D `103795681661`, aggregate `103795801049`
- artifacts/digests:
  - A `10326130747`, `sha256:e74e605a6d57657b73341715755139f35808719cc5eba71b1d454071c0cdbc41`
  - B `10326345689`, `sha256:b835e6dca3f57e0a396c8e2e1bbc8f9fe7fc78351c0b9f28b72f93e2dc398149`
  - C `10325876972`, `sha256:cbde176ea3341f677988b1595f07c4596c37d6641d29d2aef3314cf06694b663`
  - D `10324899718`, `sha256:cdcfa12dd4b2aee1f583c8354bbc826c52c8dbf99aca4bf5bff51a4579f3e6d8`
  - aggregate `10326400165`, `sha256:0b77669cd6b7327c5f654b7c9bbafb49ece64add94553e9df117d93b92eaaf79`

## Frozen result
All four raw lane artifacts and the aggregate were independently rechecked before terminal classification.

- A `D_EXACT_REFERENCE_LEAKAGE_BOUNDARY_SCOPED`: the 26-entry source-resolved science design has rank one; every prospectively frozen non-boundary leakage ratio gives exact rank two; the exact same-shape boundary `rho=+1` returns rank one.
- B `D_REFERENCE_CONDITIONING_DEGRADES_TO_SAME_SHAPE_LIMIT_SCOPED`: along `rho={0,1/2,9/10,99/100,999/1000}`, rank remains two while the smallest singular value falls from about `0.7060` to `7.027e-4` and condition number rises from about `17.92` to `1.8084e4`; the exact boundary is rank one.
- C `D_REFERENCE_GAIN_AND_RETARDED_SOURCE_ROBUSTNESS_SCOPED`: at fixed `rho=1/10`, nonzero reference gain down to `1e-6` retains exact/numerical rank two while `s_min` falls to about `6.364e-7` and condition number rises to about `1.9845e7`. Candidate and reference kernels remain retarded and Sigma-symmetric; `q_ref=2`; candidate CTP normalization, zero Hessian and nonzero third derivative remain unchanged.
- D `D_REFERENCE_PRECISION_AND_FALSE_REFERENCE_CONTROLS_SCOPED`: float64 extremal singular values agree with the independent 80-digit route with maximum frozen relative disagreement about `2.0e-14`, well inside `1e-8`; same-shape and zero controls remain rank one, candidate-only reference is rejected as a nuisance-calibration construction, and an advanced-support reference is rejected.

## Scientific interpretation
The G83 D reference-channel construction is robust over the prospectively frozen imperfect-decoupling family: moderate candidate leakage does not destroy local identifiability, but conditioning degrades continuously as the reference response approaches the exact same-kernel direction or its nuisance gain vanishes.

## Scope ceiling
This is not a physical realizability result. It does not establish a retarded source-preparation protocol, experimental leakage bound, reference calibration precision, physical candidate-blindness, architecture selection, nonlinear dynamics, readiness increase, or new physics.
