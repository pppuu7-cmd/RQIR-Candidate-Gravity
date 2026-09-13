# Iter085 / G87 — D nonlinear-completion nonuniqueness — TERMINAL

Date: 2026-09-13

Classification: `BLOCKED_D_FROZEN_CUBIC_DATA_ADMIT_MULTIPLE_QUARTIC_CTP_COMPLETIONS_SCOPED`
Scientific status: **BLOCKED / UNDERDETERMINED, scoped**
Programme readiness: **66%**
Theory established: **0%**

## Frozen authority
- common base: `16ddcaa12059569f84bdb51c8ea0dbddee7a6f38`
- preregistration: `fe22a538fc7fc92ccf53ab1470e6f434d3ffe9a0`
- implementation: `f2d6b19efc24e5ba4cd0b3156d78a7ca7b001800`
- production head: `f6ae9e9872f84940d5a63b4f536dac7f0ffe5d2c`
- branch: `g87-d-nonlinear-completion-nonuniqueness`
- run: `34784249423`
- jobs: A `103796721293`, B `103796721337`, C `103796721253`, D `103796721295`, aggregate `103796784537`
- artifacts/digests:
  - A `10326112031`, `sha256:02eb1c6062da87398e9b7e570f95d73625b0be68697cca0a9b32dbe57a9b7ca6`
  - B `10326131117`, `sha256:c130a8078728236cf6675b83f099c11e335a63dd2315a3417657bda24bd5f533`
  - C `10325927419`, `sha256:f0f05dc1975fd33cbb8679c4bcc819d12c8ebdc4cb440509986325b9cd96969c`
  - D `10326286414`, `sha256:4f57d0a847f531b65b2ddaeeacaedcc17ad42a71dffab7ba8e02530d5e0bff86`
  - aggregate `10326181714`, `sha256:ca832f5d674f8347673a5fc9386808fa71e7ba593d31301feaabb08553e435ad`

## Frozen result
All raw lanes and the aggregate were independently rechecked before terminal classification.

- A `D_QUARTIC_ADDITIONS_PRESERVE_FROZEN_CUBIC_JET_SCOPED`: both frozen quartic witness shapes have exactly zero derivatives through order three and nonzero fourth derivative; for all `lambda in {-2,1,3}` they leave the complete frozen cubic jet of the D representative unchanged.
- B `D_DISTINCT_QUARTIC_JET_SHAPES_LINEAR_COORDINATE_ROBUST_SCOPED`: the `x^4` and `x^2 y^2` fourth-derivative tensor mode-1 flattenings have exact ranks one and two; the tensors are non-proportional and those ranks remain one/two under all four frozen invertible linear reparameterizations.
- C `D_QUARTIC_CTP_NORMALIZATION_AND_CUBIC_STRUCTURE_PRESERVATION_SCOPED`: both branch-difference quartic additions vanish on equal histories, are odd under branch exchange, have zero derivatives through cubic order and nonzero fourth derivative; the frozen D Hessian remains zero, its third derivative remains nonzero, and the audited cubic kernel remains unchanged, retarded and Sigma-symmetric.
- D `D_NONLINEAR_NONUNIQUENESS_ADVERSARIAL_CONTROLS_SCOPED`: a cubic addition changes the frozen third-order jet and is rejected; scalar multiples of the same quartic shape are detected as the same shape family; zero addition and singular-transform controls behave as frozen.

## Scientific interpretation
The frozen D cubic/three-point data do not uniquely determine a quartic nonlinear extension. At least two distinct reduced quartic jet shapes survive while preserving the audited lower jet, CTP normalization and the frozen cubic-kernel structure. Therefore selecting a unique nonlinear D law requires additional candidate-owned principles or higher-order constraints not contained in the current frozen D information.

This is **BLOCKED/UNDERDETERMINED**, not an architecture failure and not a proof about the complete space of generally covariant theories.

## Scope ceiling
The finite reduced-jet witnesses do not establish a complete nonlinear D theory, inequivalence modulo arbitrary nonlinear field redefinitions/integrations by parts, full retarded/unitary/measure closure of quartic terms, or physical validity of either higher-order witness. No readiness increase or new physics follows.
