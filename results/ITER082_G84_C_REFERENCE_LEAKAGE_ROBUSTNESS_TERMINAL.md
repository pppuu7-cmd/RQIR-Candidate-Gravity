# Iter082 / G84 — C reference-channel leakage robustness — TERMINAL

Date: 2026-09-13

Classification: `C_REFERENCE_CONSTRUCTION_REMAINS_IDENTIFIABLE_UNDER_FROZEN_LEAKAGE_UNTIL_SAME_SHAPE_LIMIT_SCOPED`
Scientific status: **PASS, scoped construction robustness**
Programme readiness: **66%**
Theory established: **0%**

## Frozen authority
- common base: `27bc7d7622d681a977a31ef040665f3b4defc49b`
- preregistration: `962312fc0c9f677e1d9ca4478dcc78f60bf51fe0`
- implementation: `79815c519016ebbceb061fcd3f9f19cbce7645fd`
- production head: `2033fbe1314861e2e7e1b4d5ec04f2f3215cc946`
- branch: `g84-c-reference-leakage-robustness`
- run: `34783862061`
- jobs: A `103795663242`, B `103795663120`, C `103795663224`, D `103795663255`, aggregate `103795792115`
- artifacts/digests:
  - A `10326355690`, `sha256:d8ac7075ad045dbdfa45db8eb7b3d439a6d0da91365eae7461ff5acb1bd43ded`
  - B `10325777401`, `sha256:7e68ea7f9aff582ab657bdddb6189dedd9d199af5f9b990307e384390621a69c`
  - C `10325797222`, `sha256:afeb1c0fc696690a139605981f6da00485dfee719dc0b5ea484f9c37ae9079b6`
  - D `10326016660`, `sha256:0e9bc3814ba8cc71549706b14633508b489f0618d4570577daf70c1c4478fbfe`
  - aggregate `10326141440`, `sha256:470c5b7116a11e7ac1b79ef26e9db5390c8fefeb9e51d9f74e056975e6f846b8`

## Frozen result
All four raw lane artifacts and the aggregate were independently rechecked before terminal classification.

- A `C_EXACT_REFERENCE_LEAKAGE_BOUNDARY_SCOPED`: science-only rank is one on primary and both held-out panels; every prospectively frozen non-boundary leakage ratio gives exact rank two; the exact same-shape boundary `rho=-1` returns rank one.
- B `C_REFERENCE_CONDITIONING_DEGRADES_TO_SAME_SHAPE_LIMIT_SCOPED`: along `rho={0,-1/2,-9/10,-99/100,-999/1000}`, rank remains two while the smallest singular value falls from about `0.69533` to `6.6457e-4` and condition number rises from about `5.6878` to `6226.55`; the exact boundary is rank one.
- C `C_REFERENCE_GAIN_AND_WARD_SOURCE_ROBUSTNESS_SCOPED`: at fixed `rho=-1/10`, nonzero reference gain down to `1e-6` retains exact/numerical rank two while `s_min` falls to about `6.364e-7` and condition number rises to about `6.111e6`. All twelve frozen source-resolved science cases remain exactly Ward compatible, and `q_ref=201559/448` restores rank two throughout the frozen non-boundary leakage family.
- D `C_REFERENCE_PRECISION_AND_FALSE_REFERENCE_CONTROLS_SCOPED`: float64 extremal singular values agree with the independent 80-digit route with maximum frozen relative disagreement about `1.4e-13`, well inside `1e-8`; same-shape and zero controls remain rank one, while a candidate-only row is rank-restoring but explicitly rejected as an accepted nuisance reference.

## Scientific interpretation
The G82 C reference-channel construction is robust over the prospectively frozen imperfect-decoupling family: moderate candidate leakage does not destroy local identifiability, but conditioning degrades continuously as the reference response approaches the exact science-shape direction or its nuisance gain vanishes.

## Scope ceiling
This is not a physical realizability result. It does not establish a source-preparation protocol, experimental leakage bound, reference calibration precision, physical candidate-blindness, architecture selection, nonlinear dynamics, readiness increase, or new physics.
