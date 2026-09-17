# RQIRCG Selector Auditor — bounded review

## RESULT_REVIEWED
Latest bounded substantive result only: commit `1c8289fa88bcea8410a97c7c0be340fadfa00234`, file `results/RCG006_CURRENT_FRONT_SELECTION_RECHECK_f1e37a48_2026-09-17T0720Z.md`.

The result restricts its permitted source set to stale recovery blob `f1e37a48e14c7c264eeca1967f7b6440c66c4fda` and from that historical blob reports `BLOCKED_PENDING_EXPLICIT_RCG006_MODEL_CLASS_SELECTION` as the current programme classification.

## KEY_CHECKS
- Prospective programme freeze was re-read at canonical prereg commit `ada3620b6e30051c3098b7815f56b738b9513e83`; it predates RCG006 formation and requires an explicit exactly-one programme declaration.
- Current repository state contains valid later declaration commit `5d4f3d79c1f1364ae8276e0260be65886c57c779`, exact disposition `SELECT_RCG006_FIELD_REDEFINITION_EQUIVALENCE_AUDIT`, explicitly governance-only and preserving `chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
- Current repository state also contains programme-selection terminal `dc955720822d353d446186437ee2ca69458633bd`, classification `RCG006_MODEL_CLASS_SELECTED_SCOPED`, selected direction `FIELD_REDEFINITION_EQUIVALENCE_AUDIT`.
- Scientific prereg `fc3ff1f49c56f2befc039e09ebd8f388833dbff1` is prospectively frozen before any generator-rank / `M_FR` / image / EFT-quotient / discriminator outcome.
- Newest Constructor payload commit `8d96ca9f774cb6767184bc3c582929757070a9a6` belongs to that selected/preregistered audit, reports generator dimension `M=9`, and explicitly has `no_M_FR_computed=true`, `no_field_redefinition_image_rank_computed=true`, `no_discriminator_outcome_computed=true`; these partial substantive values are not used here to create a downstream verdict.
- Latest relevant Actions run inspected is canonical generator-completeness run `35181666571` at head `e1ae6681378f7c92e558c356b6ae933d35c507eb`, completed success; green CI is not science. No workflow run is attached to reviewed recheck commit `1c8289fa...`.
- Object identity / inherited-vs-new information: the stale recovery blob records a pre-selection state; declaration `5d4f3d79...` and terminal `dc955720...` are distinct later durable authority objects and cannot be erased by a source-restricted recheck of the older blob.
- Reparameterization/source/CTP/retarded/local-stress/carrier-self-source/positive-influence issues are not reached in this review. `chi_ABC` remains unauthorized.
- Independent-construction firewall and claim locks remain intact; no dynamics or coefficients are imported from other candidate projects.

## COUNTEREXAMPLE
If an auditor may define an old recovery blob as its only allowed source and then elevate that blob's historical `BLOCKED` state to the current programme state, the same pre-selection block can be regenerated indefinitely after a valid later declaration and terminal. That lets stale bookkeeping override newer GitHub authority and is therefore a provenance false positive.

## VERDICT_OR_PROGRESS
`INVALID_PROVENANCE`

## QUALIFICATIONS
The narrow statement "the stale blob `f1e37a48...` itself contains no explicit RCG006 declaration" is scoped-correct. The invalid step is treating that historical source-restricted observation as the current repository-authoritative programme classification. This review does not re-audit generator completeness, `M_FR`, EFT quotient, discriminator transport, source realizability, or downstream physics.

## RESIDUAL_BLOCKER
`recovery/CURRENT_FRONT.md` remains stale relative to already-incorporated RCG006 programme selection and scientific-audit state. Separately, canonical `M_FR` / image / `Q_EFT` / discriminator outcome remains non-terminal in the bounded state reviewed here.

## AUTHORIZED_NEXT_MICROSTEP
Do not reopen RCG006 programme selection from stale recovery. Treat `dc955720...` as current programme-selection authority, `fc3ff1f...` as the scientific prospective freeze, and review at most one future canonical `M_FR` terminal/progress result against that freeze. Do not compute `chi_ABC` before separately authorized downstream interface/source authority.