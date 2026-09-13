# Iter073 / G75 — C/D minimal nuisance-anchor augmentation

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/RESULTS**
Date: 2026-09-13

## Scope
G74 established exact local aliasing of the frozen C direction with same-shape quadratic slope nuisance N1 and of D with same-shape cubic calibration nuisance N3. G75 asks a narrower structural question: what minimal independent anchor/added-response augmentation restores algebraic local identifiability of the four columns (C,D,N1,N3) in the frozen tangent model?

This is an identifiability/experimental-design gate only. It cannot select C or D, establish an actual experimental anchor, fit physical coefficients, define RCG-002 dynamics, or establish new physics.

## Frozen baseline
Primary momentum panel: `z={1/3,2/3,5/4,7/3}`.
Primary rows:
- `C=(-z_i,0_cubic)`
- `D=(0,0,0,0,1)`
- `N1=(z_i,0)`
- `N3=(0,0,0,0,1)`
Thus baseline parameter-column rank is exactly 2 for four formal parameters because `C=-N1` and `D=N3`.

## Independent streams
### A — direct nuisance-anchor minimality
Append two independent calibration rows:
- quadratic nuisance anchor `AQ`: `(C,D,N1,N3)=(0,0,1,0)`;
- cubic nuisance anchor `AD`: `(0,0,0,1)`.
Frozen predicates:
- baseline rank = 2;
- AQ only rank = 3;
- AD only rank = 3;
- AQ+AD rank = 4.
This establishes minimality only inside the frozen exact-alias model.

### B — added response-shape augmentation
Instead of direct nuisance anchors, append:
- one auxiliary quadratic row with `(C,D,N1,N3)=(-z_*^2,0,z_*,0)`, frozen `z_*=3/2`;
- one auxiliary cubic row with `(0,1,0,2)`.
Frozen predicates:
- either auxiliary row alone raises rank only to 3;
- both together raise rank to 4;
- same-shape controls `(-z_*,0,z_*,0)` and `(0,1,0,1)` do not break the corresponding aliases.

### C — held-out panel and reparameterization robustness
Held-out exact rational panels:
1. `{1/5,3/5,4/3,9/4}`
2. `{2/7,5/6,7/5,11/3}`
3. `{1/2,4/5,3/2,13/5}`
For each panel, direct two-anchor augmentation must give rank 4, each single anchor rank 3, and baseline rank 2.
Then apply the frozen invertible parameter reparameterizations
`R1=[[1,1,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]`,
`R2=[[1,0,0,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]]`,
`R3=[[2,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,2]]`.
Rank of the fully anchored design must remain 4.

### D — adversarial null/false-positive controls
Frozen predicates:
- duplicated AQ row without AD leaves rank 3;
- duplicated AD row without AQ leaves rank 3;
- two added same-shape rows preserving `C=-N1` and `D=N3` leave rank 2;
- zero anchor rows leave rank 2;
- replacing only one exact alias with a distinct response raises rank to 3, not 4.

## Frozen aggregate rule
All streams valid => `CD_MINIMAL_TWO_INDEPENDENT_ANCHOR_DIRECTIONS_RESTORE_LOCAL_IDENTIFIABILITY_SCOPED`.
Any failed scientific predicate => `SCIENTIFIC_FAIL_FROZEN_MINIMAL_ANCHOR_PREDICATE`.
Missing/invalid controls/artifacts => `INFRASTRUCTURE_OR_GATE_INVALID`.

## Interpretation ceiling
PASS means only that, inside the exact G74 tangent model, two independent pieces of information that separately break the quadratic and cubic alias directions are sufficient and individually necessary for full four-column local rank. These may be direct nuisance calibrations or linearly distinct added-response observables in the frozen constructions. PASS does not show that such anchors exist physically, does not select C or D, and does not promote any hypothesis to candidate-owned dynamics.

Readiness remains 66%; theory established remains 0%.
