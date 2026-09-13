# ITER061 / G63 — auxiliary second-order factorization and real-congruence inertia audit

Status: **FROZEN BEFORE IMPLEMENTATION**
Date: 2026-09-13
Prerequisite: terminal G62 classification `FOUR_DERIVATIVE_LINEARIZED_SECTOR_RELATIVE_RESIDUE_OPPOSITION_SCOPED` from run `34761167760`.

## Scope
Candidate-independent algebraic audit only. No coefficient ray is selected. No QGR/KMQGB/RQIR physical ansatz/result is imported.

For the frozen G61/G62 conserved-sector responses, audit whether a nonexceptional real two-simple-pole response can be represented exactly by two real second-order auxiliary modes coupled linearly to the same scalarized conserved source, and whether the sign inertia required by the source-coupled quadratic form is invariant under real invertible field redefinitions.

This gate does **not** identify a physical ghost, prove instability, prove quantum unitarity failure, or establish a global higher-derivative no-go theorem.

## Frozen inputs
Sector denominators from G61:
- TT: `P_TT(z)=z*(b*z-4)/2`, nonexceptional when `b != 0`.
- scalar: `P_s(z)=3*z*((3*a+b)*z+2)`, nonexceptional when `3*a+b != 0`.

Exact G62 residues:
- TT: massless/additional `(-1/2,+1/2)`.
- scalar: massless/additional `(+1/6,-1/6)`.

Frozen rational rays:
`(1,1),(2,-1),(1,-2),(-1,1),(-2,3),(3,2),(2,-5),(-3,4),(5,-1),(4,-7),(7,3),(-5,2)`.

Frozen real invertible congruence matrices:
`[[1,0],[0,1]], [[1,1],[0,1]], [[1,0],[1,1]], [[2,1],[1,1]], [[1,2],[1,3]], [[-1,1],[1,1]], [[2,-1],[1,1]], [[3,1],[-1,1]]`.

## Frozen streams
### A — exact auxiliary reconstruction
For each sector derive `R(z)=r0/z+r1/(z-z1)` from the frozen polynomial and residues, construct canonical two-mode inverse quadratic form `K^{-1}=diag(s0/z,s1/(z-z1))` with nonzero real source couplings chosen so `c_i^2 s_i=r_i`, and verify exact reconstruction. Required: opposite signs `s0*s1=-1` for both sectors and exact symbolic equality.

### B — held-out rational-ray census
For all 12 frozen `(a,b)` rays and each nonexceptional sector, verify: real additional root, nonzero residues, exact reconstruction, and canonical inertia `(1 positive,1 negative)`. Exceptional sector lines are not silently dropped; they are classified as one-pole limits.

### C — real-congruence invariance
For each canonical nonexceptional 2x2 sign matrix `S=diag(sign(r0),sign(r1))` and each frozen real invertible integer matrix `M`, verify exact `det(M.T*S*M)=det(M)^2*det(S)<0`; therefore inertia remains `(1,1)` by exact 2x2 Sylvester logic. Required 16/16 sector×matrix checks.

### D — controls and exceptional limits
Verify TT `b=0` and scalar `3a+b=0` reduce to a single simple massless pole. Reject deliberately wrong definite-sign two-mode controls `diag(+1,+1)` and `diag(-1,-1)` because their determinant is positive and cannot be real-congruent to the frozen indefinite sign matrix. Also reject a zero-coupling fake two-mode reconstruction for a nonexceptional response.

## Frozen classification rule
PASS iff A/B/C/D all report `valid=true` and `pass=true` with all exact predicates satisfied.

Allowed PASS label only:
`FOUR_DERIVATIVE_LINEARIZED_AUXILIARY_TWO_MODE_INDEFINITE_INERTIA_SCOPED`

Any predicate mismatch is scientific FAIL unless the run fails before evaluating frozen predicates due to a clearly identified infrastructure/numerical error. Technical repair may not alter inputs, rays, matrices, interpretation, or PASS rule.

## Interpretation ceiling
Even PASS means only: for these frozen scalarized conserved-sector rational responses, a real nondegenerate two-second-order-mode source-coupled auxiliary representation requires an indefinite algebraic sign inertia, invariant under real invertible field redefinitions. It does not establish that either auxiliary mode is a physical state or ghost, and does not establish unitarity failure or a global theorem.

Programme readiness remains 66% solely from this structural gate. Theory established remains 0%.
