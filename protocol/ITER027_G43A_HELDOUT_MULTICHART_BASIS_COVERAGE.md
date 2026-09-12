# Iter027 / G43-A — held-out response-blind multi-chart basis coverage

Status: **PREREGISTERED BEFORE IMPLEMENTATION/PRODUCTION**.

## Scientific purpose

G42-A established scoped comparator support only inside the frozen bounded lower-Cholesky chart. G42-BC independently showed that the implemented generator is locally basis covariant, but 10/24 rotated positive controls leave that single coordinate box. G43-A asks whether a **fixed finite atlas of basis charts chosen without any RCG-002 target/result** materially repairs this coordinate-coverage defect on held-out positive controls and held-out rotations.

This is a methodology/coverage gate, not a physics gate. It cannot retroactively change G42-A and cannot raise programme readiness by itself.

## Frozen objects

- No RCG-002 target, response, residual, candidate or G42-A result is used by the computation.
- Six new deterministic positive controls with effective ranks 1–6, generated from lower-triangular factors inside the original production box using seeds disjoint from G42-C2/C3/G42-R/G42-BC.
- Six held-out local `SO(3)_A x SO(3)_B` rotation pairs, none equal to the four G42-BC rotations.
- 36 independent `(rank, heldout_rotation)` lanes.
- Physical Kossakowski rotation remains `C' = O C O^T`, `O = R_A direct-sum R_B`.

## Frozen atlas

Five charts fixed before production:

1. identity basis;
2–5. the four local basis rotations used in G42-BC.

For each held-out rotated matrix `C'` and each atlas chart `O_c`, compute chart coordinates `C_c = O_c^T C' O_c`, then its canonical nonnegative-diagonal semidefinite Cholesky factor. A lane is atlas-covered iff **at least one** of the five frozen charts satisfies the unchanged production coordinate box:

- diagonal coordinates in `[0,0.60]` up to `1e-12`;
- off-diagonal coordinates in `[-0.30,0.30]` up to `1e-12`;
- reconstruction relative error `<1e-10`.

No chart is added after seeing results.

## Frozen validity controls

For every lane:

- original and held-out-rotated `C` PSD within `-1e-10`;
- effective rank preserved at threshold `1e-10`;
- relative generator covariance error `<1e-10` under the held-out physical rotation;
- every reported quantity finite.

Any failure here is `MULTICHART_IMPLEMENTATION_OR_VALIDITY_FAIL`, not scientific evidence against the PSD family.

## Frozen aggregate classifier

- `HELDOUT_MULTICHART_BASIS_COVERAGE_PASS` iff all 36 lanes are valid/covariant and all 36 are covered by at least one of the five frozen charts.
- `HELDOUT_MULTICHART_BASIS_COVERAGE_PARTIAL_LIMIT` iff all 36 lanes are valid/covariant but one or more lanes remain outside all five charts.
- `MULTICHART_IMPLEMENTATION_OR_VALIDITY_FAIL` iff any structural/covariance validity condition fails.

Report total covered count, uncovered count, coverage by rank, winning-chart histogram and worst covariance/reconstruction errors.

## Interpretation lock

A PASS would show only that this finite response-blind five-chart atlas covers this finite held-out rank/rotation panel. It is not a theorem for all PSD matrices or all basis rotations and does not authorize a basis-invariant G42 adversarial claim by itself. A PARTIAL_LIMIT preserves the G42-BC coverage blocker and motivates a genuinely basis-invariant/unbounded parameterization rather than post-hoc enlargement of this atlas. Thresholds, atlas membership and held-out panel are frozen and must not be retuned after production.
