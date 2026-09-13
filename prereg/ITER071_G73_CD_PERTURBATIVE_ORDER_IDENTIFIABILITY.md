# Iter071 / G73 — C/D perturbative-order identifiability

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/RESULTS**
Date: 2026-09-13

## Scope
G72 established only that both remaining C and D architecture hypotheses admit the tested minimal completion witnesses. G73 does not select either architecture and does not define candidate-owned RCG-002 dynamics. It asks a narrower structural question: given the G72 hypothesis objects, what perturbative-order observable content is minimally required to identify their two independent deformation directions?

## Frozen hypothesis representatives
Use only order-support information already frozen by G71/G72:

- C two-point representative: `F_C(z;c)=exp(-c z)`. At the baseline `c=0`, the deformation tangent is `dF_C/dc = -z`. C contributes to the quadratic/two-point observable block.
- D three-point representative: `Gamma_D(x;d)=d*x^3/6`. At the baseline `d=0`, its Hessian is exactly zero and its third derivative tangent is exactly `1`. D contributes to the cubic/three-point observable block.

The parameters `c,d` are bookkeeping coordinates for identifiability only. They are not physical fitted parameters or candidate coefficients.

Frozen nonzero momentum panel: `z in {1/3, 2/3, 5/4, 7/3}` (exact rationals).

## Independent streams
### A — exact joint Jacobian rank
Construct the observable tangent vector
`O = (F_C(z1),...,F_C(z4), V_D)`
and the exact baseline Jacobian with columns `(partial_c O, partial_d O)`.

PASS iff:
- C column is `(-z1,-z2,-z3,-z4,0)^T`;
- D column is `(0,0,0,0,1)^T`;
- exact joint rank is 2;
- quadratic-only rows have exact rank 1;
- cubic-only row has exact rank 1.

### B — perturbative jet separation
For `Gamma_D=d*x^3/6`, verify exactly that its baseline Hessian vanishes and its third derivative is `d` (parameter tangent 1). For a quadratic C control `Gamma_C=c*x^2/2`, verify nonzero Hessian tangent and zero third derivative. PASS iff the two order supports are exactly disjoint in this frozen jet audit.

### C — basis/reparameterization covariance
Apply the following frozen invertible rational parameter transformations to the two Jacobian columns:
`[[1,1],[0,1]]`, `[[2,0],[1,1]]`, `[[1,-1],[1,2]]`, `[[-1,2],[1,1]]`.
PASS iff all transformed full Jacobians retain rank 2 and the intrinsic column-space dimension is unchanged. No individual transformed column is interpreted physically.

### D — adversarial rank-loss / leakage controls
Frozen controls:
1. Replace the nonzero momentum panel by `z={0,0,0,0}`: full Jacobian must drop to rank 1 because C becomes locally unidentifiable.
2. Remove the cubic row: rank must be 1.
3. Remove all quadratic rows: rank must be 1.
4. Deliberately contaminate D with a quadratic tangent `(1,1,1,1,1)^T`; this must be detected as violating the frozen order-support pattern even if matrix rank remains 2.

PASS iff all four controls are detected exactly.

## Frozen aggregate rule
All A/B/C/D streams valid =>
`CD_ORDER_SEPARATED_DIRECTIONS_JOINTLY_IDENTIFIABLE_ONLY_WITH_MULTIORDER_PANEL_SCOPED`.

Any failed scientific predicate => `SCIENTIFIC_FAIL_FROZEN_IDENTIFIABILITY_PREDICATE`.
Missing/invalid controls or incomplete artifacts => `INFRASTRUCTURE_OR_GATE_INVALID`.

## Interpretation ceiling
A PASS means only that, for these prospectively frozen G72 construction representatives, the C and D deformation tangents occupy distinct perturbative-order observable blocks and require a multi-order panel for joint local identifiability. It does **not** select C or D, establish physical coefficients, establish nonlinear dynamics, validate a quantum measure, or imply new physics.

Programme readiness remains 66% regardless of PASS. `THEORY_ESTABLISHED=0%`.
