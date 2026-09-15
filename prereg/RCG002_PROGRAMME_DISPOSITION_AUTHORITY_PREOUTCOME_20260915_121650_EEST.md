# RCG-002 — programme disposition authority check

Status: PROSPECTIVELY FROZEN; NO SUBSTANTIVE AUTHORITY VERDICT IN THIS COMMIT
Date: 2026-09-15
Starting recovery blob: `7de5125965bba2f2fcdc3f6105da8d9bf6e8fabd`
Current frontier: `PROGRAMME_DISPOSITION_AUTHORITY_FRONTIER`
Required action from recovery: `EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY_REQUIRED`

## Scope
Audit only whether current GitHub-authoritative programme/governance authority explicitly selects exactly one already-frozen AD1 disposition:

- D1 `FREEZE_RSC_UNSELECTED_ARCHITECTURE`;
- D2 `RETIRE_RSC_FROM_ACTIVE_PARENT_FORMATION`;
- D3 `AUTHORIZE_EXPLICIT_NEW_VERSION_FORMATION_ATTEMPT` at workflow level only.

This is an authority/provenance check, not a new parent science gate and not a scientific tie-break.

## Frozen admissible outcomes
- `AUTHORITY_PRESENT_D1` only if explicit programme/governance authority selects D1.
- `AUTHORITY_PRESENT_D2` only if explicit programme/governance authority selects D2.
- `AUTHORITY_PRESENT_D3` only if explicit programme/governance authority selects D3.
- `BLOCKED_PENDING_EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY` if no explicit selecting authority is present.
- `INVALID_AMBIGUOUS_OR_MULTIPLE_AUTHORITY` if the supposed authority does not uniquely select one frozen disposition.

## Controls
AD1 scientific admissibility of D1/D2/D3 is not itself programme authority. Convenience, elegance, expected connected signal, resemblance to GR, resemblance to another candidate project, or administrative preference are not scientific authority and cannot be used as substitutes.

## Claim ceilings retained
No new RCG-002 version is authorized by this preregistration. RSC remains `NEAR_SURVIVOR_NOT_SELECTED`. No representation class, dynamics, source constitution, state/measure, quantum law, coefficient, or prediction is selected. No Einstein/GR import is authorized. `chi_ABC` remains `UNAUTHORIZED_NOT_COMPUTED`. BLOCKED is not FAIL. Green CI is not science. A finite witness is not a theorem. All existing claim locks remain unchanged.

## Next bounded microstep
Perform exactly one authority/provenance audit under this frozen rule and commit exactly one scoped result. Do not run Actions, broad search, historical scans, multiple lanes, or any parent principle/theorem tie-break.
