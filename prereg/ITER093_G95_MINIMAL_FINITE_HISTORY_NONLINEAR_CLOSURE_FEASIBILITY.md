# ITER093 / G95 — Minimal finite-history nonlinear closure feasibility

Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION
Project: RQIR-Candidate-Gravity only

## Purpose
Test whether a nonzero connected nonlinear source-to-influence completion exists inside a deliberately finite, minimal polynomial history ansatz when ONLY the already-established RQIR-CG structural requirements are imposed. This gate does not import candidate dynamics, ansatz coefficients, or desired outcomes from RQIR/KMQGB/QGR/MSQGR/ISQGR or other projects.

This is a feasibility/obstruction gate, not a proposal of the final RCG-002 law.

## Frozen finite model
Use three ordered time cells t0<t1<t2. For each history h define real scalar branch-source coordinates j_i(h), i=0,1,2. For a pair of histories (x,y), define d_i=x_i-y_i and s_i=(x_i+y_i)/2.

Search the most general real cubic one-Delta polynomial

Gamma3(x,y) = sum_{i,j,k} c_{i;jk} d_i s_j s_k,

with j<=k and rational coefficients. This is a finite-history source-sector model only. No spacetime, gravity-field, or continuum claim is authorized.

## Frozen structural constraints
1. CTP normalization: Gamma3(x,x)=0 (automatic for the one-Delta basis; still checked).
2. Branch exchange: Gamma3(y,x)=-Gamma3(x,y).
3. Retarded support: c_{i;jk}=0 whenever max(j,k)>i. Response at time i may depend only on source averages at times <=i.
4. Discrete total-source conservation surrogate: invariance under addition of a common affine history q_i=a+b t_i to BOTH branches, tested exactly for basis shifts q=(1,1,1) and q=(0,1,2). This is only a finite-history surrogate; it is NOT nonlinear Bianchi closure.
5. Pairwise weak-field preservation: Gamma3 must vanish on all histories supported in only one time cell and on all branch pairs with s_j s_k=0 for every allowed quadratic factor; this prevents the cubic completion from altering the frozen pairwise linear normalization in this finite model.
6. Connectedness requirement: a scientific existence witness must have at least one coefficient involving two distinct average-time indices j!=k OR an exactly nonzero third mixed derivative with respect to three independent source amplitudes on the frozen test embedding.

## Positivity / integrability requirement
A noiseless unit-modulus influence kernel K(x,y)=exp(i Gamma3(x,y)) is NOT assumed physical merely from the polynomial. For the frozen finite history set H={0,e0,e1,e2,e0+e1,e0+e2,e1+e2,e0+e1+e2}, require BOTH:

A. exact cocycle integrability Gamma3(x,y)+Gamma3(y,z)-Gamma3(x,z)=0 modulo exact symbolic equality for all x,y,z in H; and
B. equivalent rank-one phase representation existence on H (there exist phi_h with Gamma3(x,y)=phi_x-phi_y on H).

If A/B fail for every nonzero structural solution, classify the noiseless finite completion as obstructed. No claim is made about noisy kernels, retained mediators, continuum contact terms, or restricted protocols.

## Frozen independent lanes
A — exact rational linear-constraint nullspace for constraints 1-5; report dimension, basis, and whether any connected direction exists.

B — impose cocycle/integrability on the structural nullspace over H; report surviving dimension and exact counterexample triples for rejected directions.

C — independent exact rank-one phase reconstruction over H plus positive-semidefinite Gram check for representative surviving directions (if any). If no survivor, verify the obstruction on every structural basis direction and on random small rational combinations selected prospectively by deterministic seed 9503.

D — adversarial controls: (i) coherent local-potential difference V(x)-V(y) must pass cocycle when constructed exactly; (ii) known one-Delta cubic k*d*s^2 without the d^3/12 completion must fail for nonzero k; (iii) zero polynomial must pass but is not a connected witness; (iv) removing the affine-shift conservation surrogate must not be silently counted as satisfying it.

Use exact rational/symbolic algebra for A/B/D. Numerical eigenvalues in C are diagnostic only and must be cross-checked against exact rank/minors where feasible.

## Frozen interpretation
Possible terminal classifications:

- `PASS_EXISTENCE_MINIMAL_FINITE_HISTORY_COHERENT_CLOSURE_SCOPED` only if a nonzero connected direction satisfies all frozen structural constraints AND exact cocycle/rank-one conditions on H.
- `NEGATIVE_MINIMAL_FINITE_HISTORY_NOISELESS_CLOSURE_OBSTRUCTED_SCOPED` if structural connected directions exist but none survive exact cocycle/rank-one conditions.
- `BLOCKED_MINIMAL_FINITE_HISTORY_STRUCTURAL_SPACE_EMPTY_SCOPED` if constraints 1-5 themselves leave no connected nonlinear direction.
- `INFRASTRUCTURE_OR_IMPLEMENTATION_FAIL` for technical failure or disagreement between independently coded exact checks.

A PASS is only an existence witness inside the frozen finite model. It does not select coefficients, establish physical gravity, prove nonlinear Bianchi closure, or raise theory-established above zero by itself.

A NEGATIVE/BLOCKED result is scoped only to this finite polynomial/noiseless/unrestricted-history ansatz and must not be generalized to all RCG-002 completions.

## Readiness rule
Programme readiness remains 66% regardless of G95 outcome unless a separately defined stable rubric item is genuinely closed. Theory established remains 0%.
