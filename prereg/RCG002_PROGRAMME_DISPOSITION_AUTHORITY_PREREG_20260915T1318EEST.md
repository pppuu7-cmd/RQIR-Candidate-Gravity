# RCG-002 programme disposition authority check — prospective preregistration

Status: `PROSPECTIVELY_FROZEN_NO_SUBSTANTIVE_RESULT`
Date: 2026-09-15
Authority source for this run: `recovery/CURRENT_FRONT.md` at blob `7de5125965bba2f2fcdc3f6105da8d9bf6e8fabd`
Frontier: `PROGRAMME_DISPOSITION_AUTHORITY_FRONTIER`
Exact next parent action: `EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY_REQUIRED`

## Frozen question
Does current GitHub-authoritative programme/governance material explicitly select exactly one of the already frozen AD1 dispositions D1, D2, or D3?

## Frozen disposition labels
- D1 `FREEZE_RSC_UNSELECTED_ARCHITECTURE`
- D2 `RETIRE_RSC_FROM_ACTIVE_PARENT_FORMATION`
- D3 `AUTHORIZE_EXPLICIT_NEW_VERSION_FORMATION_ATTEMPT`, workflow-level permission only

## Allowed next micro-audit result
A future ultra-bounded run may inspect only authority explicitly named or directly exposed by the then-current frontier and classify exactly one of:

- `AUTHORITY_PRESENT_D1`
- `AUTHORITY_PRESENT_D2`
- `AUTHORITY_PRESENT_D3`
- `BLOCKED_PENDING_EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY`
- `INVALID_AMBIGUOUS_OR_MULTIPLE_AUTHORITY`

Absence of authority is `BLOCKED`, not `FAIL`. Scientific admissibility of D1/D2/D3 is not itself programme authority.

## Locks
The audit may not create a new scientific tie-breaker, infer authority from convenience or expected outcomes, import dynamics/coefficients from other candidate projects, promote successor-only results retroactively, form a new RCG-002 version, or compute `chi_ABC`.

All existing claim locks remain in force. Green CI is not science; a finite witness is not a theorem.

## Interpretation ceiling
This preregistration freezes an authority/provenance check only. It does not choose D1/D2/D3 and does not add scientific model content.