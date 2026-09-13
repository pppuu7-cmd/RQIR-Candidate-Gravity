# Iter077 / G79 — C/D GLS correlated-noise robustness

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/RESULTS**
Date: 2026-09-13
Parallel status: **INDEPENDENT SIBLING FROM TERMINAL G75; DOES NOT CONSUME G76/G77/G78 RESULTS**

## Scope
G75 established exact rank four after two independent alias-breaking anchors. G79 asks whether the corresponding generalized least-squares Fisher matrix remains full rank across a prospectively frozen family of positive-definite correlated/heteroscedastic row-covariance surrogates, and whether weak anchors still amplify target-parameter variance.

This gate does not assign any covariance family to a physical apparatus. It is a robustness audit over frozen SPD surrogates only.

## Frozen design
Parameter order `(C,D,N1,N3)`, primary momentum panel `z={1/3,2/3,5/4,7/3}` and rows:
- four quadratic rows `(-z_i,0,z_i,0)`;
- one cubic row `(0,1,0,1)`;
- `AQ=(0,0,a,0)`;
- `AD=(0,0,0,a)`.
Frozen anchor strengths: `a in {1,1e-2,1e-4}`. Rank/eigenvalue tolerance: `1e-12`.

Frozen 7x7 SPD row-covariance families:
1. identity;
2. diagonal heteroscedastic `diag(1,2,4,3,1.5,0.8,1.2)`;
3. compound correlation `rho=0.25`;
4. quadratic-block correlation `rho=0.55` on the first four rows, identity elsewhere.

For covariance `Sigma`, the frozen Fisher matrix is `F=M^T Sigma^{-1} M` and GLS covariance is `F^{-1}` when rank four.

## Independent streams
### A — SPD GLS rank and weak-anchor variance growth
For every frozen SPD family and every nonzero frozen `a`, require Fisher rank four and strictly positive minimum eigenvalue. As `a` decreases, C and D GLS variances must increase strictly within each covariance family.

### B — independent whitening routes
At `a=1e-2`, compare Fisher matrices produced by Cholesky whitening and symmetric eigen-decomposition whitening. Relative matrix disagreement must be `<1e-10` for every frozen covariance family.

### C — orthogonal parameter-coordinate robustness
At `a=1e-2`, apply identity, C/N1 swap, D/N3 swap and C sign flip. Fisher eigenvalues must agree with the untransformed design to relative tolerance `1e-8` for every frozen covariance family.

### D — invalid-covariance and one-sided-anchor controls
A prospectively frozen singular row-covariance control formed by duplicating one covariance row/column must be rejected by the ordinary inverse-based GLS route. AQ-only and AD-only designs must each remain parameter-column rank three.

## Frozen aggregate rule
All streams valid => `G75_SPD_GLS_IDENTIFIABILITY_PERSISTS_WHILE_WEAK_ANCHOR_VARIANCE_GROWS_SCOPED`.
Any failed scientific predicate => `SCIENTIFIC_FAIL_FROZEN_GLS_ROBUSTNESS_PREDICATE`.
Missing/invalid artifacts or controls => `INFRASTRUCTURE_OR_GATE_INVALID`.

## Interpretation ceiling
PASS means only that G75 local algebraic identifiability persists under the frozen SPD weighting families and that weak anchors increase GLS uncertainty in those surrogates. It does not establish a physical covariance model, detector feasibility, experimental precision, architecture selection, or candidate-owned dynamics.

Readiness remains 66%; theory established remains 0%.
