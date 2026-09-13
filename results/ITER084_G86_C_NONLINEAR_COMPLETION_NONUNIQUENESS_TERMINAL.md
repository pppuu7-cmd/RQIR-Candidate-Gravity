# Iter084 / G86 — C nonlinear-completion nonuniqueness — TERMINAL

Date: 2026-09-13

Classification: `BLOCKED_C_FROZEN_QUADRATIC_DATA_ADMIT_MULTIPLE_CUBIC_CTP_COMPLETIONS_SCOPED`
Scientific status: **BLOCKED / UNDERDETERMINED, scoped**
Programme readiness: **66%**
Theory established: **0%**

## Frozen authority
- common base: `16ddcaa12059569f84bdb51c8ea0dbddee7a6f38`
- preregistration: `ff73cfb96a7be4afb51b31f73fc7660087fd9296`
- implementation: `e6488cc00d6d1e3c9e7f61640eca2c0d1c3ac3c6`
- production head: `697e65afd9bb53827a857afb34242fbdd0dfd7c9`
- branch: `g86-c-nonlinear-completion-nonuniqueness`
- run: `34784240659`
- jobs: A `103796697101`, B `103796697242`, C `103796697151`, D `103796697257`, aggregate `103796818156`
- artifacts/digests:
  - A `10326535037`, `sha256:bbfd853839edb0f9e8a10fec2a781b5d89a9a1db9e2947af2fa5db705892535c`
  - B `10325807847`, `sha256:a0a3357cb81bf21467262f245bc86f6ced42e9cb8341ee1a9b0bf1fabca2bf1a`
  - C `10326136876`, `sha256:967dec775a32b7413e7573545295467872e63811ab4ffee1f9475fceb6b02a93`
  - D `10326450277`, `sha256:c3466ca97941cfd15781d6bc6e22ad786ed3eb357080a0b5c5ae5dd8942535fe`
  - aggregate `10325852621`, `sha256:cd675a05da4cbbed7294665449ac98d1f0a83f8e840b1bab96298298b8839c3d`

## Frozen result
All raw lanes and the aggregate were independently rechecked before terminal classification.

- A `C_CUBIC_ADDITIONS_PRESERVE_FROZEN_QUADRATIC_JET_SCOPED`: for both frozen cubic witness shapes and all `lambda in {-2,1,3}`, value/gradient/Hessian remain exactly identical to the frozen quadratic witness; the unchanged Hessian is exactly `diag(2,4)`, while the third derivative changes nontrivially.
- B `C_DISTINCT_CUBIC_JET_SHAPES_LINEAR_COORDINATE_ROBUST_SCOPED`: the `x^3` and `x y^2` third-derivative tensor mode-1 flattenings have exact ranks one and two; the tensors are non-proportional and those ranks remain one/two under all four frozen invertible linear reparameterizations.
- C `C_CUBIC_CTP_NORMALIZATION_BRANCH_STRUCTURE_SCOPED`: both branch-difference cubic additions vanish on equal histories, are odd under branch exchange, have zero flat-background Hessian and nonzero third derivative.
- D `C_NONLINEAR_NONUNIQUENESS_ADVERSARIAL_CONTROLS_SCOPED`: a quadratic addition changes the frozen Hessian and is rejected; scalar multiples of the same cubic shape are detected as the same shape family; zero addition and singular-transform controls behave as frozen.

## Scientific interpretation
The frozen C quadratic/two-point data do not uniquely determine a cubic nonlinear extension. At least two distinct reduced cubic jet shapes survive while preserving the audited lower jet and CTP normalization. Therefore selecting a unique nonlinear C law requires additional candidate-owned principles or higher-order constraints not contained in the current frozen C information.

This is **BLOCKED/UNDERDETERMINED**, not an architecture failure and not a proof about the complete space of generally covariant theories.

## Scope ceiling
The finite reduced-jet witnesses do not establish a complete nonlinear C theory, inequivalence modulo arbitrary nonlinear field redefinitions/integrations by parts, full causal/unitary/measure closure, or physical validity of either higher-order witness. No readiness increase or new physics follows.
