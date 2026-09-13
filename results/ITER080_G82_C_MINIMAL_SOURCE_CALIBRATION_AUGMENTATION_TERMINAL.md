# Iter080 / G82 — C minimal source-calibration augmentation — TERMINAL

Date: 2026-09-13

Classification: `C_SINGLE_SOURCE_REFERENCE_CALIBRATION_BREAKS_SLOPE_ALIAS_WITHOUT_MODIFYING_C_FUNCTIONAL_SCOPED`
Scientific status: **PASS, scoped construction witness**
Programme readiness: **66%**
Theory established: **0%**

## Frozen authority
- common base: `5830d944ad5b1ef076a8ddf0509116506c94b384`
- preregistration: `43e9a1e9ee838e48c3aa5b6640e588f4dc92ad80`
- implementation: `a77e89acabbd0f6c9c171f04c25b6de03013fafb`
- production head: `ac64c3d740a1954816fe66ab54ad6f36577ca095`
- branch: `g82-c-minimal-source-calibration`
- run: `34783507013`
- jobs: A `103794684364`, B `103794684386`, C `103794684218`, D `103794684355`, aggregate `103794729260`
- artifacts/digests:
  - A `10325766858`, `sha256:bfa9614436f213da4423a3d80c01917af3ca428021f23c53cb53ca5bc4fb6128`
  - B `10324764404`, `sha256:58729a5accbfcd274283930c0e93c229c00ca0afde0d456123ccae86e5120e3d`
  - C `10326135827`, `sha256:35c7dfa789f22f4662d03bf9ad30356941a1fc681421031ad0176052c89c02fe`
  - D `10325632672`, `sha256:0c68423b7bf24c7acb28c675f29e87e9e28c36a6c7e851b7fcf3d6ef899e2735`
  - aggregate `10325248911`, `sha256:c5088a9b335987ecdc383c0ed2192fe0abfc9a933a1fc9ada0154abc3b1127d7`

## Frozen result
All four raw lane artifacts and the aggregate were independently rechecked before terminal classification.

- A `C_SINGLE_REFERENCE_CHANNEL_ALGEBRAIC_SUFFICIENCY_SCOPED`: science-only C/N1 rank is one on primary and both held-out panels; every frozen nonzero reference strength raises rank to two; zero reference strength leaves rank one.
- B `C_SOURCE_DEFINED_REFERENCE_WITH_WARD_COMPATIBILITY_SCOPED`: all twelve frozen projected-source science cases are nonzero and exactly Ward/transverse compatible; the new frozen reference seed gives `q_ref=201559/448`; appending the candidate-blind `(0,q_ref)` row raises every source-resolved design to rank two.
- C `C_REFERENCE_CHANNEL_BLOCK_SEPARATE_NONMODIFICATION_SCOPED`: science rows are algebraically unchanged, native Gaussian CTP response-zero rows remain zero, the frozen `exp(-ell2 z)` candidate response factor is unchanged, and removing the reference row exactly recovers rank one.
- D `C_REFERENCE_CHANNEL_FALSE_ANCHOR_CONTROLS_SCOPED`: same-shape and zero pseudo-reference rows remain rank one; a candidate-only row is detected as rank-restoring but is explicitly rejected as an accepted calibration construction; nonzero rescalings of the accepted nuisance-reference row preserve rank two.

## Scientific interpretation
One explicitly added source-labelled reference calibration channel is algebraically sufficient to remove the exact C/N1 slope alias while leaving the frozen C candidate functional unchanged in this finite construction audit.

This closes the **construction-sufficiency** question opened by G80, but it does not close physical realizability. The reference channel is a new external/source-calibration hypothesis, not a native consequence of C and not an established observable.

## Scope ceiling
No claim is made that the reference source can be physically prepared, isolated, measured, calibrated to the required precision, or made candidate-blind in a real realization. No architecture selection, nonlinear candidate law, readiness increase, or new physics follows.
