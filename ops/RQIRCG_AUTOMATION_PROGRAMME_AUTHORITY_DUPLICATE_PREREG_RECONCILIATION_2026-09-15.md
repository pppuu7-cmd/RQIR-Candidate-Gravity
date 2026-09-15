# RQIRCG automation programme-authority duplicate-prereg reconciliation

Date: 2026-09-15

## Incident class

`AUTOMATION_RECOVERY_LAG_CAUSED_DUPLICATE_PREREGISTRATION_ACCUMULATION`.

This is a provenance/governance incident only. It is not a scientific result and does not change AD1.

## Starting authority

After AD1 the durable recovery frontier remained:

`EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY_REQUIRED`.

The ultra-bounded Constructor reads only `recovery/CURRENT_FRONT.md`. Because recovery did not record the existence of the first valid programme-authority preregistration, later hourly runs repeatedly concluded that no preregistration existed and created new timestamped variants.

The Auditor correctly identified several later files as duplicate/nonterminal preregistrations, but the recovery front still was not synchronized, so the loop continued.

## Canonical preregistration

The earliest clean preregistration directly matching the AD1 exact next action is:

commit `e366de3c68b38dad0a2e3388e5cc8e7801cb1c41`

file `prereg/RCG002_PROGRAMME_DISPOSITION_AUTHORITY_PREOUTCOME.md`.

It prospectively freezes the valid forms of a D1/D2/D3 programme-authority declaration and explicitly states that no disposition is chosen by the preregistration itself.

This file is the canonical programme-authority preregistration.

## Later duplicate files

Later timestamped/renamed programme-authority preregistrations created after `e366de3c...` are retained for provenance but are **non-authoritative duplicates**. They do not create parallel gates and do not reset prospective chronology.

This includes the later programme-disposition authority/check/block/required/prereg variants visible in the compare from the AD1 head to the 2026-09-15 automation head.

The repeated file

`results/RCG002_RSC_ARCHDISP_D1_MICROAUDIT.md`

is also non-authoritative for current frontier purposes because AD1 had already prospectively audited and terminalized D1, D2 and D3. Its scoped statement that D1 is defensible is compatible with AD1 but adds no selection authority.

## Canonical terminal

The canonical programme-authority check is now terminalized as:

`BLOCKED_PENDING_EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY`

in

`results/RCG002_PROGRAMME_DISPOSITION_AUTHORITY_CHECK_TERMINAL.md`.

This terminal uses the canonical preregistration `e366de3c...` and does not select D1/D2/D3.

## Automation rule after reconciliation

Until an external explicit programme-authority declaration appears:

- do not create another programme-disposition preregistration;
- do not repeat AD1 micro-audits;
- do not create another scientific selector/theorem gate to break the tie;
- treat the parent as parked on `WAIT_FOR_EXPLICIT_PROGRAMME_DISPOSITION_DECLARATION`;
- successor RQIRCGSF work may continue independently.

A future automation run may only record a new parent result if a genuinely new explicit authority declaration or repository authority appears after this reconciliation.

## Scientific impact

None.

Historical RCG-002 remains terminal at the nonlinear model-definition boundary.
RSC remains `NEAR_SURVIVOR_NOT_SELECTED`.
No new version is authorized.
`chi_ABC` remains unauthorized.
Readiness remains 66%; theory established remains 0%.
