# Iter063 / G65 — full conserved-source projector audit (FROZEN)

Preregistered prospectively on 2026-09-13, before implementation or production output.

## Scientific question
Do the G61–G64 TT/scalar algebraic conclusions extend from two canonical representatives to the complete conserved symmetric-source tensor space of the same 4D Minkowski-linearized/local four-derivative class, at the level of exact transverse spin-2/scalar projector decomposition?

This gate is candidate-independent and does not import QGR/KMQGB/RQIR physical assumptions or conclusions.

## Frozen mathematical object
Use exact rational arithmetic on symmetric rank-2 tensors in four dimensions with non-null rational covectors `k` and transverse projector
`theta = I - k k^T/(k.k)`.
On the symmetric tensor space define
- `P2_{mn,ab} = 1/2(theta_ma theta_nb + theta_mb theta_na) - 1/3 theta_mn theta_ab`,
- `P0_{mn,ab} = 1/3 theta_mn theta_ab`.
For conserved/transverse symmetric sources, `P2+P0` must be the identity on the 6-dimensional transverse symmetric subspace, with exact ranks `rank(P2)=5`, `rank(P0)=1`, idempotence and orthogonality.

The frozen sector polynomials inherited only from already-closed RQIR-CG G61 are
`P_TT(z)=z(-2 + b z/2)` and `P_0(z)=z(6 + 3(3a+b) z)`.
No coefficient ray is selected physically.

## Frozen coefficient and evaluation panel
Coefficient rays:
`(1,1),(2,-1),(1,-2),(-1,1),(-2,3),(3,2),(2,-5),(-3,4)`.
Exclude a sector evaluation only when its frozen polynomial vanishes at that exact `z`.
Evaluation values: `z in {1/5, 2/3, 5/4}`.
Momentum covectors for exact checks:
`k1=(1,2,3,4)`, `k2=(2,-1,1,3)`, `k3=(3,1,-2,2)`.

## Stream A — exact projector algebra
For all three frozen `k`:
1. exact symmetry of `theta`, `P2`, `P0`;
2. `theta^2=theta` and `theta k=0`;
3. exact `P2^2=P2`, `P0^2=P0`, `P2 P0=P0 P2=0`;
4. exact ranks `rank(P2)=5`, `rank(P0)=1`, `rank(P2+P0)=6` on the 10-dimensional symmetric-tensor representation.
PASS requires every predicate exactly.

## Stream B — held-out conserved-source reconstruction and response
For each frozen `k`, deterministically construct at least 8 held-out integer symmetric seed tensors and transverse-project them to conserved sources `T`.
Require exactly:
- conservation `k^m T_mn=0`;
- reconstruction `T=P2 T + P0 T`;
- response equality for every non-singular frozen `(a,b,z)` lane between direct projector contraction and the sum of separately contracted spin-2/scalar sector responses.
No fitted coefficients or retuning are allowed.

## Stream C — basis/frame covariance
Use the following frozen signed-permutation 4x4 orthogonal integer matrices: identity; swaps `(0 1)`, `(1 2)`, `(2 3)`; sign flips of axes 0, 1, 2, 3; and the four compositions swap(0,1)+flip(2), swap(1,2)+flip(3), swap(2,3)+flip(0), cyclic permutation `(0->1->2->0)`.
For transformed `k` and sources require unchanged projector ranks, exact transformed projector tensors, and exact quadratic-response invariance for the frozen non-singular lanes.

## Stream D — false-positive controls
All must be rejected/detected:
1. a deliberately nonconserved symmetric source must fail `T=(P2+P0)T`;
2. malformed scalar projector coefficient `1/4` instead of `1/3` must fail idempotence and/or rank/decomposition predicates;
3. omitting `P0` must fail reconstruction for an explicitly transverse pure-trace source;
4. omitting `P2` must fail reconstruction for an explicitly transverse traceless source.

## Frozen aggregate rule
Scientific PASS iff A/B/C/D are individually `valid=true` and `pass=true` with all exact predicates satisfied.
Allowed PASS classification only:
`FOUR_DERIVATIVE_LINEARIZED_FULL_CONSERVED_SOURCE_PROJECTOR_DECOMPOSITION_SCOPED`.
Otherwise, a valid violation is `SCIENTIFIC_FAIL`; malformed/missing artifacts are `INFRASTRUCTURE_OR_ARTIFACT_INVALID`.

## Claim ceiling
Even full PASS establishes only exact full-conserved-source projector coverage for the already-frozen local linearized four-derivative response. It does **not** prove a physical ghost, instability, quantum-unitarity failure, nonlinear inconsistency, coefficient selection, or a global higher-derivative/no-go theorem. Programme readiness remains 66%; theory established remains 0% unless a separate rubric gate authorizes a change.
