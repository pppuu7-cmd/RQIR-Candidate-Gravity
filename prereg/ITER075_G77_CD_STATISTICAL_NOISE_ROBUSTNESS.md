# Iter075 / G77 — C/D anchored estimator statistical-noise robustness

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/RESULTS**
Date: 2026-09-13
Parallel status: **INDEPENDENT SIBLING FROM TERMINAL G75; DOES NOT CONSUME G76 RESULTS**

## Scope
G75 established exact algebraic full rank for the frozen `(C,D,N1,N3)` tangent model once two independent alias-breaking anchor directions are supplied. G77 asks a separate statistical-design question: under a deliberately simple homoscedastic Gaussian row-noise surrogate, how does linear-estimator covariance behave as those anchors weaken?

This gate freezes a mathematical noise surrogate only. It does not assert a physical detector noise model, an experimental signal-to-noise threshold, physical realizability of anchors, architecture selection, or candidate-owned dynamics.

## Frozen design
For a momentum panel `z_i`, parameter order is `(C,D,N1,N3)` and the rows are:
- four quadratic rows `(-z_i,0,z_i,0)`;
- one cubic row `(0,1,0,1)`;
- quadratic nuisance anchor `AQ=(0,0,a,0)`;
- cubic nuisance anchor `AD=(0,0,0,a)`.

Primary panel: `{1/3,2/3,5/4,7/3}`.
Held-out panels: `{1/5,3/5,4/3,9/4}` and `{2/7,5/6,7/5,11/3}`.
Frozen nonzero anchor strengths for the main trend: `a in {1,1e-1,1e-2,1e-3}`. Numerical rank tolerance: `1e-12`.

For iid Gaussian row noise with variance `sigma^2`, the frozen linear covariance is `sigma^2 (M^T M)^(-1)` whenever rank is four.

## Independent streams
### A — analytic weak-anchor variance amplification
On primary plus both held-out panels, require rank four for every nonzero frozen `a`. As `a` decreases in the frozen sequence, the variances of C and D and the maximum parameter variance must increase strictly. At `a=0`, exact-alias rank must be two.

### B — exact sigma-squared covariance scaling
At `a in {1,1e-2,1e-4}` and `sigma in {1e-3,1e-2,1e-1}`, require `Cov/sigma^2` to agree with `(M^T M)^(-1)` to relative tolerance `1e-11`.

### C — fixed-seed Monte Carlo replication
Use seed `76077`, `12000` iid Gaussian draws, `sigma=0.02`, and `a in {1,1e-1,1e-2}`. Zero true parameter vector is used because only covariance is audited. The maximum relative error among the four empirical covariance diagonals must be `<0.08` against the analytic covariance for every frozen `a`.

### D — orthogonal coordinate covariance and one-sided controls
At `a=1e-3`, apply identity, C/N1 swap, D/N3 swap, C sign flip and D sign flip. Covariance eigenvalues must agree with the untransformed design to relative tolerance `1e-8`. AQ-only and AD-only designs must each remain rank three.

## Frozen aggregate rule
All streams valid => `G75_ANCHORED_ESTIMATOR_VARIANCE_GROWS_AS_ANCHORS_WEAKEN_SCOPED`.
Any failed scientific predicate => `SCIENTIFIC_FAIL_FROZEN_STATISTICAL_NOISE_PREDICATE`.
Missing/invalid artifacts or controls => `INFRASTRUCTURE_OR_GATE_INVALID`.

## Interpretation ceiling
PASS means only that, in the frozen linear tangent design with the frozen iid Gaussian surrogate, weak alias-breaking anchors amplify estimator variance while the calculation obeys expected scaling, fixed-seed replication and orthogonal-coordinate controls. It does not define physical detectability or a required experimental precision.

Readiness remains 66%; theory established remains 0%.
