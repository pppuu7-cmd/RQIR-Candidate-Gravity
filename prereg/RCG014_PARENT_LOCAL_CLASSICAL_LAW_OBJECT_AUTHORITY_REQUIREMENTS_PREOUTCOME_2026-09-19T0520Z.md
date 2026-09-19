# RCG014 — Parent Local Classical Law Object Authority Requirements — Prospective Preregistration

Status: `PROSPECTIVE_PREOUTCOME_FROZEN`

Gate:
`RCG014_PARENT_LOCAL_CLASSICAL_LAW_OBJECT_AUTHORITY_REQUIREMENTS_GATE`

## Scope

This gate is repo-local and outcome-blind. It does **not** construct, import, infer, reconstruct, or select a parent local classical-law object. It freezes only the authority/provenance package that must already exist before any object A may receive the status
`PARENT_LOCAL_EXACT_SELECTED_OBJECT`.

## Frozen repo-only restrictions

- Do not fetch any successor repository.
- Do not reconstruct RHPI or any other candidate/project content from memory.
- Do not fabricate missing source content.
- Do not import dynamics, coefficients, source laws, or model-defining structure from other candidate projects.
- Do not compute `chi_ABC`.
- `BLOCKED != FAIL`.
- Green CI is not scientific authority.
- A finite witness is not a theorem.
- Existing claim locks remain in force.

## Authority package required before object-selection credit

A candidate object may receive `PARENT_LOCAL_EXACT_SELECTED_OBJECT` credit only if the repository authority supplies a content-addressed package that fixes, at minimum:

1. **Exact object identity** — the complete mathematical object/law, not a verbal family label or mnemonic.
2. **Exact provenance** — repository path(s), immutable commit/blob identity, and an unambiguous lineage showing where the object is defined.
3. **Domain** — the fields/states/configurations on which the object is defined, including dimensional or regularity assumptions needed for the definition.
4. **Transformation/equivalence law** — the precise gauge, coordinate, field-redefinition, or other equivalence structure under which the object is interpreted.
5. **Normalization/convention data** — all conventions whose change would alter numerical coefficients, signs, index placement, or observable interpretation.
6. **Selection authority** — an explicit repository-authoritative statement that selects this exact object for the parent programme, rather than merely exhibiting it as an admissible example.
7. **Candidate independence / firewall** — evidence that the selection was not obtained by importing downstream candidate outcomes, desired `alpha`, desired Weyl-cubed sensitivity, `chi_ABC`, or successor-only information.
8. **Use license** — an explicit statement of which downstream operation is authorized once the object is selected; no response/value/bridge computation is inferred merely from object existence.

## Classifier

`PASS_SCOPED_RCG014_PARENT_LOCAL_EXACT_SELECTED_OBJECT_AUTHORITY_PRESENT`
may be returned only if every required item above is satisfied by current repository authority.

Otherwise classify only the missing-authority condition, e.g.
`BLOCKED_SCOPED_RCG014_PARENT_LOCAL_EXACT_SELECTED_OBJECT_AUTHORITY_INCOMPLETE`,
without converting absence of authority into a scientific FAIL of any candidate law.

## Stop rule

This preregistration itself creates no substantive scientific result and selects no object. After freezing it, STOP. A later run may perform at most one bounded source-audit allowed by the current frontier against these frozen requirements.

Locks retained:
`alpha = UNSELECTED`;
`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`;
`THEORY_ESTABLISHED = 0%`.
