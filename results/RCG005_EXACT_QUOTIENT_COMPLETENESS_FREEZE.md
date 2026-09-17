# RCG-005 — exact quotient/completeness freeze before primary dynamics

Date: 2026-09-17
Status: **DURABLY FROZEN AFTER QUOTIENT-ONLY CERTIFICATION AND BEFORE CANONICAL PRIMARY DYNAMICS**

Scientific preregistration:
`prereg/RCG005_COMPLETE_PARITY_EVEN_LOCAL_DIM6_PURE_METRIC_CURVATURE_CLASS_V0.md`, commit `1ac1c032dcbbd8e3f0a527a470acc0a44ddffa08`.

Held-out preregistration:
`prereg/RCG005B_GENERIC_METRIC_JET_PRINCIPAL_SYMBOL_HELDOUT.md`, commit `1fb26a399264747fc2ffa8a564d4d281c0586f9c`.

## Canonical quotient-only execution

The first execution attempt `35178140025` had an implementation-only missing helper reference and produced no admissible aggregate. The prospective repair is frozen in `recovery/RCG005_PREPRIMARY_EXECUTION_REPAIR.md`, commit `c03c693719040ff5ec80da839782379e1b9ae7d3`, with repaired code commit `ce4cfe07d8226562700fb193c8b14eefba28f803`.

Canonical successful quotient-only run:
- run `35178250959`;
- run number `2`, attempt `1`;
- workflow head `ac3c646b0fc1a5bec2fa6781e5bdb9c8bbb1b820`;
- Constructor job `105064632969` — success;
- independent Critic job `105064633044` — success;
- aggregate job `105064698593` — success.

Artifacts:
- Constructor `10479537361`, digest `sha256:4dc0741d1beaf5ec66edb75508be8600742e6a45b046b71e1bb248d49b2e354c`;
- Critic `10479243645`, digest `sha256:8159a877e47d5a459f1597bc316ad1cdb963d339ab27aa44811a723bc57862d3`;
- aggregate `10479278706`, digest `sha256:b72001be7aa2a15eeb950f7c0d343c70aa93b3ac40adae725d50cf7aca6aeb4e`.

Downloaded JSON SHA256:
- Constructor `f32e278194e9c30c6649dc5f88756cf2f66b7886f852c33030447624a5479feb`;
- Critic `449eebfc90e699bc7ea1a4328e90a0676985cd920ec99f41ab2c883f3840ab60`;
- aggregate `22f730c36c9ed4e95a67429de1f55e7bcb64b67c59287cfdc0507c274f275c5d`.

Durable payloads:
- `results/raw/RCG005_QUOTIENT_CONSTRUCTOR.json`, commit `ce70d8bf82d9dc9455a04d0473591bae4faba02b`;
- `results/raw/RCG005_QUOTIENT_CRITIC.json`, commit `21d7ed96d483434077cf699874cb5eae40411805`;
- `results/raw/RCG005_QUOTIENT_AGGREGATE.json`, commit `ec1484c7c610a9e3b14491c7d5ed6e1d7ef25fe4`;
- `results/raw/RCG005_QUOTIENT_ARTIFACT_MANIFEST.json`, commit `b6b01be27036e2bccea8f0f3549ca3db66632604`.

Aggregate classification:
`PASS_RCG005_PREPRIMARY_QUOTIENT_COMPLETENESS_READY_TO_FREEZE`.

Every frozen quotient aggregate predicate is true. Both scientific lanes explicitly report `no_primary_dynamics_computed=true`; thus this freeze precedes canonical A6/A5/A4/A3/nullspace outcome.

## Mechanically enumerated raw family

The exact raw counts are frozen as:
- algebraic `Riemann^3`: `10395` complete pairings;
- `(nabla Riemann)(nabla Riemann)`: `945` complete pairings;
- `Riemann * nabla^2 Riemann`: `945` complete pairings;
- one-curvature/four-derivative raw template: `105` complete pairings;
- total raw pairings/templates: **`12390`**.

After algebraic Riemann symmetry orbiting, the Constructor obtains:
- cubic nonzero/zero classes: `13 / 20`;
- `D1D1` nonzero/zero classes: `12 / 14`;
- `R_D2R` nonzero/zero classes: `14 / 24`;
- `D4R` nonzero/zero classes: `12 / 9`.

The independent Critic reconstructs the cubic and `D1D1` sectors from reverse pairing enumeration and a different tensor realization.

## Exact derivative-tensor and action quotient

Constructor differential-Bianchi route:
- raw `nabla Riemann` component space before differential Bianchi: `80`;
- exact differential-Bianchi relation rank: `20`;
- exact generic 4D `nabla Riemann` tensor dimension: **`60`**;
- twelve nonzero `D1D1` scalar symmetry classes have exact pointwise rank **`4`**.

Independent Critic route:
- constructs `200` independent normal-coordinate metric third-jet variables (`10` symmetric metric pairs times `20` symmetric derivative triples);
- independently obtains the same `D1D1` pointwise rank **`4`**.

Action-level exact relations combine:
- pointwise derivative-tensor relations;
- inherited exact 4D cubic relations;
- exact integration-by-parts / derivative-commutator relations, with generated cubic curvature terms retained.

Three independent commutator relations are generated. The total exact relation matrix on the `12 + 13 = 25` canonical derivative-plus-cubic directions has:
- exact rank **`17`**;
- exact quotient dimension **`N=8`**;
- exact RREF SHA256 **`4b6f9b9713b076a10513adb1b10ab0bfc91b822acda441f976aee2f14a5fd38e`**.

Constructor and Critic independently produce this same RREF hash, so they agree on the exact relation span rather than merely its rank.

## Frozen RCG005 production quotient basis

From this commit onward, the production quotient coordinates are frozen **before canonical primary dynamics** as eight directions in this order:

1. `D1D1_CLASS_9`;
2. `D1D1_CLASS_11`;
3–8. the inherited canonical RCG004 Constructor quotient axes with parent class indices `[0,1,2,4,5,8]` in their existing parent order.

For a `D1D1` raw object the slot convention is:
- first factor: slot `0` is its covariant-derivative index and slots `1,2,3,4` are its four Riemann indices;
- second factor: slot `5` is its covariant-derivative index and slots `6,7,8,9` are its four Riemann indices;
- each pair below denotes an exact metric contraction of those slots.

The two new frozen canonical representatives are:

`D1D1_CLASS_9 = ((0,6),(1,3),(2,5),(4,8),(7,9))`

`D1D1_CLASS_11 = ((0,6),(1,5),(2,8),(3,7),(4,9))`.

Their class indices are defined by the deterministic sorted nonzero canonical-class manifest produced by `scripts/rcg005_dim6_constructor.py` / `scripts/rcg005_quotient_constructor.py` under the frozen Riemann symmetry group.

The inherited six axes are not regenerated or redefined here: they are exactly the canonical parent RCG004 Constructor basis class indices `[0,1,2,4,5,8]` from canonical RCG004 artifact manifest/run `35175941323`.

The exact embedding rank of the inherited RCG004 quotient into this eight-dimensional quotient is **`6`**.

No coefficient normalization or survivor information is encoded by this coordinate choice.

## Exact next permitted scientific action

Canonical primary production may now evaluate, for this frozen eight-dimensional quotient only:
- restored-lapse fully triaxial off-shell derivative-order maps;
- the prospectively frozen A_m cascade for every actual order `m>2`;
- independent direct generalized Euler-Lagrange reconstruction;
- frozen negative controls;
- the already frozen generic metric-jet held-out only if the primary survivor dimension is nonzero.

No basis extension or quotient alteration is permitted after this freeze without invalidating the primary run.

`FIELD_REDEFINITION_EQUIVALENCE = UNRESOLVED_OUT_OF_SCOPE_RCG005_V0`.
`VACUUM_ZERO`.
`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
