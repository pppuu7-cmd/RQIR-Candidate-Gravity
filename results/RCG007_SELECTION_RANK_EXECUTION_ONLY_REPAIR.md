# RCG-007 — execution-only source-guard repair after invalid initial aggregate

Date: 2026-09-17
Status: **PROSPECTIVE EXECUTION-ONLY REPAIR BEFORE RETRY**

Scientific preregistration remains unchanged:
`prereg/RCG007_WEYL3_INHERITED_RQIR_SELECTION_RANK_AUDIT_V0.md`, commit `85d6e8ef6a29ffac2ba1481fc6213e5f6f67abb4`.

Initial workflow run:
`35254221385`, head `fef1267b9f67795b441a41b2a2593a12eee4c587`.

The initial run has **no scientific verdict** because the aggregate classification was
`INVALID_RCG007_SELECTION_RANK_AUDIT_AGGREGATE`.

Diagnostic facts from the invalid run may be used only to localize implementation defects, not as terminal science:
- Constructor exact selector matrix shape was `22 x 1`, rank `0`, residual dimension `1`, but `constructor_valid=false` solely because `source_checks=false`;
- independent Critic exact selector rank was also `0`, residual dimension `1`, and its frozen scientific branch was the preregistered zero-rank blocker;
- all Constructor mathematical/object/order/control checks other than the source-wording guard were true.

The failed Constructor source subcheck was exactly:
`RCG002_is_hypothesis_only = false`.

Direct inspection of the frozen source `candidates/RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md` shows the required authority is present:
- status `HYPOTHESIS / BASELINE EMBEDDING ONLY — NOT A VALIDATED THEORY AND NOT A NOVELTY CLAIM`;
- exact heading `## Candidate-owned linearized dynamical rule`;
- the text explicitly calls this the candidate's first field-dynamics hypothesis.

Cause: the Constructor guard searched the heading substring with lower-case initial `candidate-owned`, while the frozen file contains upper-case `Candidate-owned`. Python substring matching is case-sensitive.

## Frozen repair

Change only the RCG002 source-wording guard to match the exact frozen capitalization (or equivalently perform case-insensitive comparison for this wording check).

Forbidden repair changes:
- no change to admissible selector rows;
- no change to Weyl-cubed object or perturbative-order calculation;
- no change to selector matrix/rank calculation;
- no change to G89 D-specific exclusion;
- no change to RCG002 scientific status/exclusion;
- no change to positive/negative controls;
- no change to PASS/BLOCKED/INVALID classifiers or interpretation ceiling;
- no assignment of `alpha`.

Retry the exact same frozen gate after this wording-only repair. The invalid initial run remains historical and cannot be reclassified.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
