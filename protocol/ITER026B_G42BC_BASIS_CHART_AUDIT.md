# Iter026B / G42-BC — response-blind basis/chart covariance audit

Status: **PREREGISTERED WITHOUT USING G42-A RESULTS**.

## Purpose

The G42 comparator is mathematically a real-PSD 6x6 Kossakowski family on the six local Pauli generators, but the production optimizer uses a **bounded lower-Cholesky coordinate chart**. This audit asks two separate questions before any stronger interpretation of a G42-A result:

1. Does the implemented generator transform covariantly under physical local `SO(3)_A × SO(3)_B` Pauli-basis rotations induced by local `SU(2)` unitaries?
2. Do PSD matrices that lie inside the frozen Cholesky box remain representable inside the same box after those basis rotations?

No RCG-002 target, G42-A candidate, or G42-A residual is used.

## Frozen response-blind panel

- Six deterministic hidden controls with effective ranks 1–6, generated from lower-triangular factors already inside the production box.
- Four deterministic local rotation pairs, spanning mild and strong non-axis-aligned rotations.
- 24 independent `(rank, rotation)` lanes.
- Physical Kossakowski transform is frozen as `C' = O C O^T`, where `O = R_A ⊕ R_B` is obtained directly from the selected local `SU(2)` conjugations on the Pauli basis.

## Frozen implementation-covariance rule

For every lane:

- original and rotated `C` must be PSD within `-1e-10`;
- effective rank must be preserved at threshold `1e-10`;
- relative generator covariance error `||L(C') - S L(C) S^{-1}||_F / max(||L(C')||_F,1e-15) < 1e-10`, with `S = U* ⊗ U` in column-vectorization convention;
- all reported quantities finite.

Failure here is an implementation/basis-covariance failure, not a physics result.

## Frozen chart-coverage rule

For each rotated PSD matrix, compute its canonical nonnegative-diagonal semidefinite Cholesky factor without fitting to RCG-002. A rotated control is `inside_frozen_chart` iff:

- reconstruction relative error `<1e-10`;
- every diagonal factor coordinate is within `[0,0.60]` up to `1e-12`;
- every off-diagonal coordinate is within `[-0.30,0.30]` up to `1e-12`.

Aggregate classification:

- `BOUNDED_CHART_ROTATION_COVERAGE_PASS_ON_PANEL` iff all 24 implementation-covariance checks pass and all 24 rotated controls remain inside the box;
- `BOUNDED_CHART_ROTATION_COVERAGE_LIMIT_FOUND` iff all implementation-covariance checks pass but at least one rotated control leaves the box;
- `BASIS_COVARIANCE_IMPLEMENTATION_FAIL` iff any implementation-covariance check fails.

## Interpretation lock

A chart-coverage limit does not alter the numerical G42-A result for the chart that was actually tested, but it forbids interpreting that result as basis-invariant evidence for the entire mathematical real-PSD family. A panel PASS is still finite evidence, not a theorem for all rotations or unbounded PSD matrices.
