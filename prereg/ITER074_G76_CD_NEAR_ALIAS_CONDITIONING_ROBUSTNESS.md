# Iter074 / G76 — C/D near-alias conditioning robustness

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/RESULTS**
Date: 2026-09-13

## Scope
G75 established exact algebraic full rank after two independent alias-breaking information directions. G76 tests whether that exact rank remains numerically well separated from rank deficiency when anchors weaken or added responses approach the G74 same-shape aliases.

This is a numerical identifiability robustness gate only. Condition numbers are coordinate/normalization dependent, so comparisons are restricted to frozen normalizations and orthogonal parameter transformations. No physical detectability, architecture selection, or candidate-law claim is permitted.

Frozen primary panel: `z={1/3,2/3,5/4,7/3}` with baseline four columns `(C,D,N1,N3)` exactly as G75.

## Independent streams
### A — direct-anchor strength scaling
Append direct nuisance anchor rows `AQ=(0,0,a,0)` and `AD=(0,0,0,a)` for `a in {1,1e-1,1e-2,1e-3,1e-4,1e-5,1e-6}`.
Frozen predicates:
- numerical rank is 4 for every nonzero `a` using fixed SVD tolerance `1e-12`;
- smallest singular value is strictly positive and strictly decreases as `a` decreases;
- condition number strictly increases as `a` decreases;
- the exact zero-anchor control has numerical rank 2 at the same tolerance.

### B — near-shape added-observable approach to alias
At frozen `z*=3/2`, append rows
- `Q(delta)=(-z*+delta,0,z*,0)`;
- `D(delta)=(0,1,0,1+delta)`
for `delta in {1,1e-1,1e-2,1e-3,1e-4,1e-5,1e-6}`.
Frozen predicates mirror A: rank 4 for every nonzero delta at tolerance `1e-12`, strictly decreasing smallest singular value and increasing condition number as delta approaches zero, while delta=0 returns rank 2.

### C — held-out panel and orthogonal-coordinate robustness
Use held-out panels from G75. For each panel and anchor strengths `a in {1,1e-3,1e-6}`, require the fully anchored design to remain rank 4 at tolerance `1e-12`.
Apply frozen orthogonal parameter transformations consisting of the identity, swaps `(C<->N1)`, `(D<->N3)`, both swaps, and independent sign flips of C and D. Singular values must agree with the untransformed design to relative tolerance `1e-12`.

### D — precision/convergence and false-positive calibration
For the primary panel evaluate A designs at `a in {1,1e-2,1e-4,1e-6}` in float64 and with an independent high-precision mpmath eigenvalue route (`80` decimal digits) on `M^T M`.
Frozen predicates:
- relative disagreement of smallest and largest singular values is `<1e-8` for all nonzero cases;
- exact zero-anchor and exact same-shape controls remain below absolute smallest-singular-value threshold `1e-12`;
- a deliberately one-sided anchor control remains numerical rank 3, not 4.

## Frozen aggregate rule
All streams valid => `G75_EXACT_IDENTIFIABILITY_DEGRADES_CONTINUOUSLY_TOWARD_ALIAS_SCOPED`.
Any failed scientific predicate => `SCIENTIFIC_FAIL_FROZEN_NEAR_ALIAS_ROBUSTNESS_PREDICATE`.
Missing/invalid artifacts or precision control => `INFRASTRUCTURE_OR_GATE_INVALID`.

## Interpretation ceiling
PASS means only that in the frozen normalized tangent designs, G75 exact identifiability becomes progressively ill-conditioned as independent anchor strength vanishes or added responses approach exact same-shape aliases, while the computation is stable across held-out panels, orthogonal coordinate changes and an independent high-precision route. It does not define an acceptable experimental signal-to-noise threshold, prove physical anchor realizability, select C or D, or define candidate-owned dynamics.

Readiness remains 66%; theory established remains 0%.
