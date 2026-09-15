# RCG-002 programme disposition authority check — prospective preregistration

Status: `PROSPECTIVELY_FROZEN_NO_SUBSTANTIVE_RESULT`
Date: 2026-09-15
Starting recovery blob: `7de5125965bba2f2fcdc3f6105da8d9bf6e8fabd`
Active frontier: `PROGRAMME_DISPOSITION_AUTHORITY_FRONTIER`
Required parent action: `EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY_REQUIRED`

## Scope
A future ultra-bounded run may perform exactly one source/authority audit: determine whether current GitHub authority explicitly selects exactly one frozen disposition from AD1:

- D1 `FREEZE_RSC_UNSELECTED_ARCHITECTURE`;
- D2 `RETIRE_RSC_FROM_ACTIVE_PARENT_FORMATION`;
- D3 `AUTHORIZE_EXPLICIT_NEW_VERSION_FORMATION_ATTEMPT` at workflow level only.

## Frozen outcomes
- `AUTHORITY_PRESENT_D1`
- `AUTHORITY_PRESENT_D2`
- `AUTHORITY_PRESENT_D3`
- `BLOCKED_PENDING_EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY`
- `INVALID_MULTIPLE_OR_AMBIGUOUS_AUTHORITY`

## Decision rule
Scientific admissibility, convenience, elegance, expected connected signal, resemblance to GR, resemblance to another candidate project, or administrative preference are not programme-disposition authority. Explicit authority must identify one D1/D2/D3 choice and its provenance. If no such explicit authority is present within the permitted source scope, classify `BLOCKED_PENDING_EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY`; BLOCKED is not FAIL.

## Locks
This audit cannot create a new parent science gate, select a representation class or dynamics, import Einstein/GR or other candidate-project dynamics/coefficients, form a new RCG-002 version, or compute `chi_ABC`. RSC remains `NEAR_SURVIVOR_NOT_SELECTED`; theory established remains 0% absent separate authority. Green CI is not science; finite witness is not theorem.
