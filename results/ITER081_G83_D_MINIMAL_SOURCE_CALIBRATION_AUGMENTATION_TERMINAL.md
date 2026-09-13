# Iter081 / G83 — D minimal source-calibration augmentation — TERMINAL

Date: 2026-09-13

Classification: `D_SINGLE_RETARDED_SOURCE_REFERENCE_CALIBRATION_BREAKS_CUBIC_GAIN_ALIAS_WITHOUT_MODIFYING_D_FUNCTIONAL_SCOPED`
Scientific status: **PASS, scoped construction witness**
Programme readiness: **66%**
Theory established: **0%**

## Frozen authority
- common base: `5830d944ad5b1ef076a8ddf0509116506c94b384`
- preregistration: `6c03aa2cfa462ae78e6410f1152ca476e679a195`
- implementation: `ff62a450d6b801a28a6f16422c1add117e2afcc1`
- production head: `0e6e088579a0f12f5d2b7f7aaf340beebca82944`
- branch: `g83-d-minimal-source-calibration`
- run: `34783514167`
- jobs: A `103794705371`, B `103794705361`, C `103794705480`, D `103794705293`, aggregate `103794773369`
- artifacts/digests:
  - A `10325308790`, `sha256:924f52630f7b25cce29717761e226344c7b4bf56d23e649e549dc693c347ff84`
  - B `10324999208`, `sha256:9319dd4eb8e272162dded2c74d3e2555353979d7b08bbe24230af634f635a887`
  - C `10324474946`, `sha256:2e961c6b700d6036b72843d5232e0740e3fd71e782b35dd3b9587e6d41134bc6`
  - D `10325687124`, `sha256:99d405cc9bb73a03d1defd7bf8245e74bd99613138391c7b9a5bf30a53348b31`
  - aggregate `10325334117`, `sha256:faca91a4782d2dfef0d40e085417cac6c435834201881ed6d8b9ddb3fe615c78`

## Frozen result
All four raw lane artifacts and the aggregate were independently rechecked before terminal classification.

- A `D_SINGLE_REFERENCE_CHANNEL_ALGEBRAIC_SUFFICIENCY_SCOPED`: the 26 nonzero frozen D-kernel science entries give identical D/N3 columns of rank one; every frozen nonzero reference strength raises rank to two; zero reference strength leaves rank one.
- B `D_RETARDED_SOURCE_DEFINED_REFERENCE_COMPATIBILITY_SCOPED`: both candidate and reference kernels are exactly retarded and Sigma-symmetric; the frozen reference kernel has `q_ref=2`; appending `(0,q_ref)` restores rank two without introducing advanced support.
- C `D_REFERENCE_CHANNEL_BLOCK_SEPARATE_NONMODIFICATION_SCOPED`: candidate K3 entries remain unchanged, CTP normalization remains exact, the frozen Hessian stays zero, the third derivative stays nonzero, and removing the reference row recovers rank one.
- D `D_REFERENCE_CHANNEL_FALSE_ANCHOR_CONTROLS_SCOPED`: same-kernel and zero pseudo-reference rows leave rank one; a candidate-only row is detected as rank-restoring but rejected as an accepted calibration construction; an advanced-support reference is rejected; nonzero rescalings of the accepted nuisance-reference row preserve rank two.

## Scientific interpretation
One explicitly added retarded source-labelled reference calibration channel is algebraically sufficient to remove the exact D/N3 cubic-gain alias while leaving the frozen D candidate functional unchanged in this finite construction audit.

This closes the **construction-sufficiency** question opened by G81, but it does not close physical realizability. The reference channel is a new external/source-calibration hypothesis, not a native consequence of D and not an established observable.

## Scope ceiling
No claim is made that the reference cubic source can be physically prepared, isolated, measured, calibrated to the required precision, or made candidate-blind in a real realization. No architecture selection, nonlinear candidate law, readiness increase, or new physics follows.
