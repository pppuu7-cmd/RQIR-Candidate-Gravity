# Iter076 / G78 — C/D anchored-design row-deletion redundancy

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/RESULTS**
Date: 2026-09-13
Parallel status: **INDEPENDENT SIBLING FROM TERMINAL G75; DOES NOT CONSUME G76/G77 RESULTS**

## Scope
G75 established exact rank four after adding the two independent alias-breaking anchor rows. G78 asks which individual observable/anchor rows are structurally indispensable and what minimal extra cubic response is sufficient to remove the single-row failure associated with the sole cubic target row.

This is an exact finite-dimensional design-redundancy audit only. Rows are algebraic information channels, not claims that corresponding physical measurements exist.

## Frozen design
Parameter order `(C,D,N1,N3)`. Primary panel `z={1/3,2/3,5/4,7/3}` with rows:
- four quadratic rows `(-z_i,0,z_i,0)`;
- sole cubic row `(0,1,0,1)`;
- `AQ=(0,0,1,0)`;
- `AD=(0,0,0,1)`.
Numerical rank tolerance: `1e-12`.

Held-out panels: `{1/5,3/5,4/3,9/4}`, `{2/7,5/6,7/5,11/3}`, `{1/2,4/5,3/2,13/5}`.

## Independent streams
### A — single-row deletion map
Full primary design must have rank four. Deleting any one of the four ordinary quadratic rows must leave rank four. Deleting the sole cubic row, AQ, or AD must each reduce rank to three.

### B — minimal cubic-row redundancy
Append exactly one distinct cubic-response row `(0,2,0,1)`. The augmented design must have rank four; deleting either the original cubic row or the added cubic row individually must retain rank four; deleting both cubic rows must reduce rank to three.

### C — false-positive redundancy controls
A duplicated AQ cannot replace a missing AD; a duplicated AD cannot replace a missing AQ; and a same-shape cubic nuisance pseudo-row cannot replace the missing target-support cubic row. Each frozen control must remain rank three.

### D — held-out deletion pattern
On all three held-out momentum panels, the same pattern as stream A must hold: full rank four; any single ordinary quadratic-row deletion rank four; deletion of sole cubic, AQ, or AD rank three.

## Frozen aggregate rule
All streams valid => `G75_ANCHORED_DESIGN_SINGLE_ROW_FAILURE_MODES_AND_MINIMAL_CUBIC_REDUNDANCY_SCOPED`.
Any failed scientific predicate => `SCIENTIFIC_FAIL_FROZEN_ROW_REDUNDANCY_PREDICATE`.
Missing/invalid artifacts or controls => `INFRASTRUCTURE_OR_GATE_INVALID`.

## Interpretation ceiling
PASS identifies exact algebraic single-row failure modes and one minimal cubic redundancy construction inside the frozen G75 tangent design. It does not prove physical observability, experimental feasibility, nonlinear closure, or candidate-owned dynamics.

Readiness remains 66%; theory established remains 0%.
