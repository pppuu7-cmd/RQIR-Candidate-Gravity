# RCG-006 — field-redefinition generator completeness freeze

Date: 2026-09-17
Status: **CANONICAL PRE-MAP GENERATOR SPACE FROZEN BEFORE M_FR OUTCOME**

Programme selection terminal:
`dc955720822d353d446186437ee2ca69458633bd`.

Scientific preregistration:
`fc3ff1f49c56f2befc039e09ebd8f388833dbff1`.

Held-out preregistration:
`43748579a78f40e0825d5ae01dc634d55ba7b928`.

The first workflow run `35181593199` was infrastructure-only: both lanes stopped at a Rational zero-default TypeError before any scientific artifact/rank. The execution-only repair was frozen in `9cf77f0092df8fa494860af115698404c37a0ab1`; no science definition changed.

## Canonical generator run

Run `35181666571`, run number `1`, attempt `1`, head `e1ae6681378f7c92e558c356b6ae933d35c507eb`.

Jobs:
- Constructor `105074944360` — success;
- independent Critic `105074944319` — success;
- aggregate `105075052051` — success.

Artifacts and digests are frozen in `results/raw/RCG006_GENERATOR_CANONICAL_ARTIFACT_MANIFEST.json`.

Canonical aggregate:
`aggregate_valid = true`.

Classification:
`PASS_RCG006_GENERATOR_COMPLETENESS_READY_TO_FREEZE`.

The aggregate explicitly states:
`M_FR_status = NOT_COMPUTED_PREMAP`.

Therefore no field-redefinition action-map rank, image, EFT quotient or discriminator-invariance outcome was available when this generator space was frozen.

## Complete raw generator family

The two and only frozen engineering-dimension-four partitions are:
- `ALG_RIEMANN2`;
- `DER_NABLA2_RIEMANN`.

Mechanical raw counts:
- algebraic `Riemann^2` rank-2 tensors: `525`;
- derivative `nabla^2 Riemann` rank-2 tensors: `60`;
- total raw templates: `585`.

Constructor symmetry-orbit diagnostics:
- ALG nonzero canonical symmetry classes: `9`;
- ALG symmetry-zero classes: `12`;
- DER ordered nonzero classes: `7`;
- DER ordered zero classes: `7`.

## Exact universal tensor quotient

Constructor exact generic-curvature matrix:
- shape `312 x 525`;
- SHA256 `71d5a1298bc42a47ba022470653fd03c6b62bb88d0f5379369ea508b8ac9b644`;
- exact algebraic generator dimension `M_ALG = 6`.

Constructor exact normal-coordinate fourth-metric-jet principal matrix:
- 350 independent symmetric fourth metric-jet variables;
- shape `474 x 60`;
- SHA256 `335a59826532c4bab74fc30f078bd145363eb08d2f685151c6d6dcef66200d99`;
- exact new derivative principal dimension `M_DER = 3`.

All derivative-order antisymmetry/commutator lower-order remainders lie in the exact ALG span. Hence the filtered universal generator space has

**`M = 6 + 3 = 9`**.

Independent Critic reconstructs the same exact dimensions `6 + 3 = 9` via reverse raw enumeration, an independent self-dual/anti-self-dual generic-curvature parametrization and independently indexed normal-coordinate fourth metric jets. Its pivot sets differ from the Constructor pivot sets, so agreement is not forced by identical basis choice.

## Frozen deterministic production basis

For all subsequent RCG006 production maps, use the Constructor lexicographic exact pivot representatives:

`FR_ALG` raw indices:
`[16, 19, 46, 52, 436, 439]`.

Additional `FR_DER` raw indices:
`[1, 30, 46]`.

Thus the production generator coefficient vector has exactly nine coordinates, ordered as six ALG then three DER pivots above.

This basis is a deterministic coordinate choice only. The universal nine-dimensional span is the scientific object.

No generator may be added, removed or replaced after this freeze on the basis of `M_FR`, image rank, EFT quotient size or higher-derivative-discriminator behavior.

## Parent and claim locks

RCG005 remains unchanged at terminal commit
`aef9882924ffd128c6c30934e4f95394aae874fc`
with classification
`FAIL_SCOPED_RCG005_COMPLETE_LOCAL_DIM6_PURE_METRIC_CLASS_HAS_NO_NONZERO_SECOND_ORDER_SURVIVOR`.

Next permitted scientific action:
construct the exact first-order EH field-redefinition action map for this frozen nine-dimensional generator space into the frozen eight-dimensional RCG005 quotient, with independent Critic reconstruction and no post-map generator changes.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
