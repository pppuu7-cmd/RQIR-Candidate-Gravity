# RCG-005 preprimary quotient — execution-only repair record

Date: 2026-09-17
Status: **PROSPECTIVE EXECUTION REPAIR AFTER NON-SCIENTIFIC RUN FAILURE**

Failed workflow run:
`35178140025`.

Failed job:
Constructor `105064295131`.

The independent Critic job completed successfully, but the Constructor terminated before producing an artifact. The aggregate was skipped. Therefore this run has no admissible RCG005 quotient classification.

Exact defect:
`scripts/rcg005_quotient_constructor.py` attempted to read `c.PARENT_MANIFEST`, but `scripts/rcg005_dim6_constructor.py` does not define that helper attribute. The intended parent object is already fixed independently as the persisted canonical file:

`results/raw/RCG004_CANONICAL_ARTIFACT_MANIFEST.json`.

Frozen repair:
replace only

`Path(c.PARENT_MANIFEST)`

with

`Path('results/raw/RCG004_CANONICAL_ARTIFACT_MANIFEST.json')`.

No other scientific code, raw enumeration, equivalence relation, relation matrix construction, exact-rank method, quotient criterion, candidate basis, RCG004 embedding criterion, preregistration, held-out, classifier, or claim lock may be changed by this repair.

The failed run remains an infrastructure/implementation failure and must not be classified as scientific FAIL or PASS.

A fresh workflow execution at a new head containing exactly this repair is required. `run_number` may advance; no rerun at the old head can incorporate the repair.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
