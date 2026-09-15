# RCG-002 programme disposition authority check — prospective preregistration

Status: `PROSPECTIVELY_FROZEN_NO_SUBSTANTIVE_RESULT`
Date: 2026-09-15
Starting recovery blob: `7de5125965bba2f2fcdc3f6105da8d9bf6e8fabd`
Active frontier: `EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY_REQUIRED`

## Scope
Audit only whether current GitHub-authoritative programme/governance instruction explicitly selects exactly one already-admissible AD1 disposition:

- D1 `FREEZE_RSC_UNSELECTED_ARCHITECTURE`;
- D2 `RETIRE_RSC_FROM_ACTIVE_PARENT_FORMATION`;
- D3 `AUTHORIZE_EXPLICIT_NEW_VERSION_FORMATION_ATTEMPT` at workflow level only.

## Frozen outcomes
- `AUTHORITY_PRESENT_D1`
- `AUTHORITY_PRESENT_D2`
- `AUTHORITY_PRESENT_D3`
- `BLOCKED_PENDING_EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY`
- `INVALID_AMBIGUOUS_OR_MULTIPLE_AUTHORITY`

## Decision rule
A positive authority result requires an explicit, provenance-clear programme/governance instruction selecting exactly one of D1/D2/D3. Scientific admissibility, convenience, elegance, expected connected signal, resemblance to GR, resemblance to another candidate project, or administrative preference do not count as authority.

If no explicit unique authority is present in the permitted audit scope, classify `BLOCKED_PENDING_EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY`; BLOCKED is not FAIL.

## Locks
No new parent science gate; no new representation class/action/source/state/quantum-law/coefficient/version; no retroactive successor import; no dynamics import from other candidate projects; no `chi_ABC`; no connected-outcome selection; all current claim locks remain.

## Interpretation ceiling
This audit may establish only programme-disposition authority provenance. It cannot establish RCG-002 dynamics, theory validity, new physics, uniqueness, or a physical prediction.
