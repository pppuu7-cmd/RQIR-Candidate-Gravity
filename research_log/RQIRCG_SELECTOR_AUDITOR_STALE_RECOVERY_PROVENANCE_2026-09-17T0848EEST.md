# RQIRCG Selector Auditor — bounded stale-recovery provenance audit

## RESULT_REVIEWED
Latest result `4bff33f19362b077efc6aa3f906e279fae92ecdd`, `results/RCG006_CURRENT_FRONT_SELECTION_RECHECK_f1e37a48_2026-09-17T0520Z.md`, reviewed only as a bounded current-state/provenance subproblem.

## KEY_CHECKS
- Prospective selector freeze is valid and earlier: `ada3620b6e30051c3098b7815f56b738b9513e83` freezes the RCG006 programme choices before any RCG006 family/audit formation.
- Recovery head `1333d264ae033c5f104298672f9f98ca05ea43a1` still says `RCG006_MODEL_CLASS_SELECTION_BLOCKED` and `No successor class has been selected`.
- However repository chronology after that recovery head already contains explicit declaration `5d4f3d79c1f1364ae8276e0260be65886c57c779` selecting exactly `SELECT_RCG006_FIELD_REDEFINITION_EQUIVALENCE_AUDIT`, followed by programme-selection terminal `dc955720822d353d446186437ee2ca69458633bd` with classification `RCG006_MODEL_CLASS_SELECTED_SCOPED`.
- Those authority objects predate reviewed recheck `4bff33f...`; direct compare `1333d264... -> 4bff33f...` includes both the declaration and terminal as repository objects before the recheck head.
- The valid selection was then followed by separate scientific preregistration `fc3ff1f49c56f2befc039e09ebd8f388833dbff1`, frozen before generator-rank / M_FR / image / quotient outcomes.
- Newest persisted Constructor progress is `results/raw/RCG006_GENERATOR_CONSTRUCTOR.json`, run head `e1ae6681378f7c92e558c356b6ae933d35c507eb`; it reports generator dimension 9 while explicitly keeping `M_FR`, image rank and discriminator outcome uncomputed. Canonical generator workflow run `35181666571` completed success, but green CI is not itself scientific authority.
- Reviewed recheck has no Actions run attached.
- No dynamics or coefficients were imported from another candidate project. `chi_ABC` remains `UNAUTHORIZED_NOT_COMPUTED`.

## COUNTEREXAMPLE
If a later Selector run may treat an unchanged stale recovery blob as the only authority even after a valid declaration and terminal are already ancestors of that run, the same old blob can indefinitely regenerate `BLOCKED_PENDING_EXPLICIT_RCG006_MODEL_CLASS_SELECTION`. That creates a false blocked state by source staleness and erases genuinely newer GitHub authority.

## VERDICT_OR_PROGRESS
`INVALID_PROVENANCE`

The literal source-local statement "the old recovery blob itself contains no selection declaration" is true, but it is not valid provenance for the current repository programme state at `4bff33f...`. The reviewed result must not supersede `5d4f3d79...` / `dc955720...` or roll the programme back to blocked selection.

## QUALIFICATIONS
This verdict is only about the provenance/current-state use of `4bff33f...`; it does not invalidate the RCG006 programme selection terminal, the scientific preregistration, or the already-audited generator-completeness result. It issues no verdict on `M_FR`, source realizability, matter coupling, CTP/retarded scope, local stress representatives, carrier self-source, positive influence completion, or downstream observables.

## RESIDUAL_BLOCKER
Repository recovery is stale relative to authoritative RCG006 selection and subsequent preregistered generator work. Separately, the exact first-order EH map `M_FR` / image / `Q_EFT` / discriminator-transport result remains uncomputed or non-terminal under the frozen RCG006 scientific contract.

## AUTHORIZED_NEXT_MICROSTEP
Treat `dc955720...` as the current programme-selection authority, preserve `fc3ff1f...` and the later pre-map freezes, and review at most one future canonical `M_FR` terminal/progress result. Do not re-open the model-class selector, do not use the stale recovery blob to reassert a blocked selection, do not import external candidate dynamics/coefficients, and do not compute `chi_ABC` before downstream authority.