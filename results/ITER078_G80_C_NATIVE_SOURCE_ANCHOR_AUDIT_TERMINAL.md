# Iter078 / G80 — C native source-anchor availability audit — TERMINAL

Date: 2026-09-13

Classification: `BLOCKED_C_NATIVE_SOURCE_OBJECT_DOES_NOT_BREAK_EXACT_SLOPE_ALIAS_SCOPED`
Scientific status: **BLOCKED, scoped**
Programme readiness: **66%**
Theory established: **0%**

## Frozen authority
- common base: `080c219d20f8ed16fa24845ffa180ea5c5d57bc0`
- preregistration: `c09e2298a746cc5055e8f67c6c9edb182e52dabe`
- implementation: `0f53469f396248a5ba00a35dcb3450cb9318e74f`
- production head: `6d159d77d3feace880784d229067e30cb8afb657`
- branch: `g80-c-native-source-anchor-audit`
- run: `34783125605`
- jobs: A `103793637626`, B `103793637691`, C `103793637755`, D `103793637736`, aggregate `103793724031`
- artifacts/digests:
  - A `10326250030`, `sha256:c46108e01029df42ecdb8f7efc23a9eb350f916393aefea3feaadc6ea016a7d5`
  - B `10325721295`, `sha256:c6a0db336f42f9a421c913167945f43f9d5dcd747401d93cf0bf5a37b44f6f4b`
  - C `10326020575`, `sha256:f028b6752659da7b85f8c0317eb6554477e63341dd9fbe618a137cbeefaf147a`
  - D `10325905809`, `sha256:20cdd12bed51ff55f1b1fd3dc2c544806cc3f09e837998c33a669c3ddf2128cf`
  - aggregate `10325925907`, `sha256:b2f9214940e746650cbad54cda6363c9ff5c8de69aa25f0abe1e80573be47610`

## Frozen result
All four raw lane artifacts and the aggregate were independently rechecked before terminal classification.

- A `C_EXACT_RESPONSE_SLOPE_ALIAS_CONFIRMED_SCOPED`: on primary and both held-out panels, `(C,N1)=(-z,+z)` has exact rank one and `C+N1=0`.
- B `C_TRANSVERSE_SOURCE_SAMPLING_PRESERVES_ALIAS_SCOPED`: all twelve frozen G72 projected-source cases have nonzero exact source weights, but common source weighting preserves exact rank one and `C+N1=0`.
- C `C_NATIVE_CTP_ZERO_DERIVATIVE_SECTORS_DO_NOT_ANCHOR_SCOPED`: appending the already-native Gaussian CTP noise/normalization rows with zero derivative in the frozen response coordinates leaves rank one.
- D `C_ANCHOR_AUDIT_SEPARABILITY_CONTROLS_VALID_SCOPED`: a distinct `z^2` nuisance shape or deliberately non-native direct calibration row raises rank to two, while a zero pseudo-anchor and common rescalings leave rank one.

## Scientific interpretation
The already-frozen C source-functional object does not contain an independent information direction that separates the C response-slope tangent from the exact same-shape N1 nuisance. Transverse/Ward projection and native Gaussian CTP sectors preserve, rather than resolve, the alias in this local audit.

This is **BLOCKED**, not a failure of architecture C. The next admissible C-specific construction must explicitly add or derive a source/calibration response direction linearly independent of the C tangent while preserving the frozen Ward/causal/pole constraints.

## Scope ceiling
No physical observable, detector calibration, source preparation, nonlinear candidate law, architecture selection or new physics is established. Positive controls are deliberately non-native and cannot be promoted to candidate physics.
