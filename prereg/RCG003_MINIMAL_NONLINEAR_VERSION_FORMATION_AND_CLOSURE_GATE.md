# RCG-003 — minimal nonlinear version formation + conformal derivative-closure gate (FROZEN)

Date: 2026-09-17
Status: **PROSPECTIVELY FROZEN BEFORE PRODUCTION EVALUATION**
Parent authority terminal: `d9187a60d2e7545ae3f082762d4a747b9681b69f`
Consumed D3 declaration: `464bbb6fd3c602a1fdc5194f0a6a03b8327fb7f4`
Historical RCG-002 remains unchanged and scientifically terminal in its scope.

## Scientific objective

Form the smallest explicit nonlinear RQIRCG version-family that is sufficient for one exact structural falsification/reduction test without importing successor-project physics or silently promoting standard GR structure to a derivation.

The first discriminator is a necessary nonlinear derivative/causal-constraint safeguard:

> Does the frozen bounded cubic-curvature deformation family contain a nonzero coefficient direction whose homogeneous conformal reduction has equations of motion of at most second time-derivative order for every off-shell conformal history?

This is a structural gate. It is not a phenomenology, quantization, or prediction gate.

## Independent-construction firewall

No RQIRCGSF, RHPI, ADM/Einstein successor construction, QGR, ISQGR, or other candidate-project result is an input to this gate.

Historical parent inputs are limited to:

- the weak-field linearized spin-2 baseline as historical reference/control: `candidates/RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md`;
- the G90 fact that `sqrt(|g|) R^3` and `sqrt(|g|) R R_{mu nu}R^{mu nu}` can be used as explicit covariant higher-order witnesses. G90 did not make them candidate dynamics.

Their promotion into the RCG-003 bounded candidate family below is **NEW_MODEL_POSTULATE**, effective only from this preregistration. No G90 selector outcome is reused.

## Shared prospective model-definition layer

Every substantive object is classified explicitly.

1. **Version identity** — `RCG003_MINIMAL_NONLINEAR_CUBIC_RICCI_FAMILY_V0`; `NEW_MODEL_POSTULATE`.
2. **Parent authority** — D3 terminal `d9187a60...`; `SOURCE_AUTHORIZED`.
3. **Fundamental variable** — one Lorentzian metric `g_{mu nu}`; `NEW_MODEL_POSTULATE` for RCG-003, with its linear perturbation required to admit the historical spin-2 control limit.
4. **Representation class** — local metric representation in 4 spacetime dimensions; `NEW_MODEL_POSTULATE`.
5. **Configuration/state space** — smooth Lorentzian metrics on a patch admitting a Minkowski weak-field neighborhood; for the hard gate, arbitrary smooth off-shell homogeneous conformal histories `g_{mu nu}=exp(2 sigma(t)) eta_{mu nu}`; `NEW_MODEL_POSTULATE`.
6. **Gauge/redundancy structure** — spacetime diffeomorphism covariance of the covariant action family; `NEW_MODEL_POSTULATE`. No claim that historical RCG-002 derived nonlinear diffeomorphism invariance.
7. **Causal structure** — local differential dynamics; full hyperbolicity/well-posedness `UNRESOLVED`. The hard gate freezes only the necessary conformal-sector no-extra-time-derivative lock below.
8. **Locality/nonlocality** — local finite-derivative action family; `NEW_MODEL_POSTULATE`. Nonlocal terms are `UNAUTHORIZED` in RCG003-v0.
9. **Source constitution** — hard-gate source is exactly vacuum `T_{mu nu}=0`; `NEW_MODEL_POSTULATE` for this scope. Arbitrary external stress tensors are forbidden in this gate.
10. **Carrier self-source status** — metric self-interaction is encoded only through variation of the frozen metric action; no separate local gravitational stress tensor is postulated; `NEW_MODEL_POSTULATE` plus local-stress representative `UNRESOLVED`.
11. **Matter coupling** — `UNRESOLVED` and excluded from the hard-gate domain. No matter source is inserted by hand.
12. **Nonlinear dynamics class** — the bounded three-parameter cubic-Ricci deformation family below; `NEW_MODEL_POSTULATE`.
13. **Action/Hamiltonian/generator** — covariant action family below is the generator; `NEW_MODEL_POSTULATE`. No Hamiltonian or CTP generator is separately asserted.
14. **Conservation structure** — vacuum diffeomorphism Noether/Bianchi identity is the formal conservation structure of the action family; `NEW_MODEL_POSTULATE` as model structure, not a historical derivation. Matter conservation is `UNRESOLVED` because matter is outside scope.
15. **Observable map** — `UNRESOLVED`; no physical prediction is authorized by this gate.
16. **Quantum-state status** — `UNAUTHORIZED`.
17. **Measure status** — `UNAUTHORIZED`.
18. **Coefficient classes** — `lambda, mu, nu` are exact `SYMBOLIC / NEW_MODEL_PARAMETER`; no fitting. `ell>0` is a symbolic bookkeeping length scale. Overall Einstein-Hilbert normalization is reference/control only and irrelevant to the rank test.
19. **Field-redefinition equivalence** — frozen below; `NEW_MODEL_POSTULATE`.
20. **Domain of validity** — classical local metric family, with the first discriminator evaluated on the exact off-shell homogeneous conformal subfamily; `NEW_MODEL_POSTULATE`.
21. **Classical/quantum interpretation ceiling** — classical structural mathematics only. No quantum theory, measurement prediction, experimental claim, or new physics claim.
22. **PASS / FAIL / BLOCKED / INVALID rules** — frozen below.

Objects marked `UNRESOLVED` or `UNAUTHORIZED` are not inputs to the hard gate and cannot be inferred from its result.

## Frozen bounded model family

Use, up to an irrelevant common nonzero normalization,

`S[g;lambda,mu,nu] = Integral d^4x sqrt(|g|) [ R + ell^4 ( lambda O1 + mu O2 + nu O3 ) ]`,

with

- `O1 = R^3`,
- `O2 = R R_{mu nu} R^{mu nu}`,
- `O3 = R_mu^nu R_nu^rho R_rho^mu`.

The `sqrt(|g|) R` term is **REFERENCE / CONTROL**, not `DERIVED` RQIRCG physics and not a novelty claim. The three cubic operators and their use as candidate dynamics are `NEW_MODEL_POSTULATE`.

Frozen basis restrictions:

- parity even;
- local;
- algebraic in curvature (no covariant derivatives of curvature);
- exactly cubic in Ricci/scalar curvature for the deformation sector;
- four spacetime dimensions;
- no Weyl/Riemann-cubic, nonlocal, stochastic, state-dependent, CTP, higher-than-cubic-curvature, or matter operators in v0.

No coefficient may be changed or fitted after the outcome.

## Frozen equivalence / quotient

For this first gate only, two descriptions are identified when related by:

1. an invertible rational change of coefficient coordinates spanning the same operator subspace; or
2. an invertible local **point** redefinition of the conformal history variable `sigma=f(tau)` with `f' != 0`, preserving the weak-field orientation/normalization locally.

Derivative-dependent metric/field redefinitions are **FORBIDDEN STRUCTURES in RCG003-v0**, not silently quotiented. Consequently this gate makes no claim about a broader EFT equivalence relation.

The raw family dimension is 3. The evaluator must compute the closure rank and residual dimension after the frozen structural equations. It must also verify with a point-field-redefinition control that the residual dimension is unchanged by an allowed invertible redefinition.

No uniqueness claim is allowed unless the exact residual dimension is zero; even then it would be uniqueness only inside this frozen bounded family/equivalence convention.

## Frozen hard discriminator: conformal second-order lock

Set

`g_{mu nu}=exp(2 sigma(t)) eta_{mu nu}`, signature `(-,+,+,+)`.

Define `x=(dot sigma)^2` and `y=ddot sigma`.

The evaluator must derive the reduced curvature invariants directly from the metric/tensor definitions or independently verify the following preregistered kinematic identities before using them:

- `sqrt(|g|)=exp(4 sigma)`;
- `R = 6 exp(-2 sigma) (x+y)`;
- `R_{mu nu}R^{mu nu} = 12 exp(-4 sigma) (x^2+x y+y^2)`;
- mixed Ricci eigenvalues are `exp(-2 sigma){3y, y+2x, y+2x, y+2x}`, so `O3` is fixed without a fitted convention.

For any one-dimensional second-derivative reduced Lagrangian `L(sigma,dot sigma,ddot sigma)`, the coefficient of `sigma''''` in the Euler-Lagrange equation is the Hessian `partial^2 L / partial(ddot sigma)^2`. The frozen `CONFORMAL_SECOND_ORDER_LOCK` requires that Hessian to vanish identically as a polynomial in independent off-shell `x,y` for the deformation sector.

The exact compatibility system is therefore constructed by collecting every independent `x,y` coefficient of that Hessian into

`A c = 0`, `c=(lambda,mu,nu)^T`.

The matrix entries, rank, nullspace, and residual dimension are **outcomes**. They may not be hard-coded from a desired coefficient vector.

## Structural interpretation

- `raw_dimension = 3`.
- `rank(A)` is exact over rationals.
- `residual_dimension = 3-rank(A)`.
- a nonzero nullspace vector is an admissible deformation direction only for this conformal derivative-order test; it is not a complete theory.

## Source-realizability layer

The production gate is vacuum, so the only admitted physical source for its equations is exactly `T=0`, which is trivially conserved and realizable in the frozen state space.

A separately tagged conserved tensor may be used only as a **CONTROL** for the source-admission checker. It does not enter the action or closure equations.

Arbitrary/unregistered external stress tensors must be rejected rather than used to close the model.

## Prospectively frozen negative controls

All controls must be distinguished for the expected reason:

1. **broken conservation sign** — for covector `k_mu=(1,2,0,0)` with `k^mu=(-1,2,0,0)`, start from conserved symmetric control `T00=4,T01=T10=2,T11=1` and flip the off-diagonal sign; the mutated tensor must fail exact `k^mu T_{mu nu}=0`.
2. **forbidden source** — the same otherwise conserved tensor, if tagged as an unregistered external physical source for the vacuum production gate, must be rejected by source provenance before it can enter closure.
3. **gauge-inconsistent variant** — a deformation term tagged as a coordinate scalar without the required scalar-density `sqrt(|g|)` factor must be rejected from the diffeomorphism-covariant action basis.
4. **field-redefinition duplicate** — under the invertible point map `sigma=tau+(1/3)tau^2`, on the frozen local panel `tau in {0,1/2}` where `f' != 0`, the transformed highest-derivative compatibility system must have the same rank and nullspace dimension as the original; it must not be counted as a new physical model direction.
5. **perturbed closure coefficient** — after obtaining a primitive exact nullspace direction, change exactly one coefficient by `+1`; the mutated vector must fail at least one exact compatibility equation.
6. **reference positive control** — the reduced Einstein-Hilbert density is linear in `ddot sigma`, so its `ddot sigma` Hessian must vanish exactly. This is a REFERENCE/CONTROL only.
7. **higher-derivative sensitivity control** — `sqrt(|g|) R^2` must produce a nonzero `ddot sigma` Hessian on the same conformal panel, proving the discriminator is not identically blind.

## Exact classifier

First validate chronology, identities, exact arithmetic, basis manifest, equivalence controls, source controls, and negative controls.

- `INVALID` if preregistration chronology is violated, basis/model content changes after outcome, coefficients are fitted/refit, a forbidden source is inserted, successor-project content masquerades as derivation, or required provenance/control artifacts are malformed.
- `BLOCKED_SCOPED` if a required object for **this exact hard gate** is absent so that `A`, its quotient convention, or its classifier is undefined without a new assumption.
- `PASS_SCOPED_RCG003_CONFORMAL_SECOND_ORDER_NONZERO_DEFORMATION_EXISTS` iff all controls pass and `residual_dimension > 0`; report exact basis vectors. This is existence only, not uniqueness.
- `FAIL_SCOPED_RCG003_CONFORMAL_SECOND_ORDER_NONZERO_DEFORMATION_EXCLUDED` iff all controls pass and `residual_dimension = 0`; this falsifies nonzero deformation only inside the frozen RCG003-v0 family.

Formation-validity side classification:

`RCG003_MINIMAL_NONLINEAR_FAMILY_FORMED_FOR_VACUUM_STRUCTURAL_TEST_SCOPED`

is allowed iff all 22 model-definition slots are explicitly classified and every object required by this gate is defined. This side classification does not mean a complete interacting theory has been formed.

## Independent Critic preregistration

After the evaluator emits its result, an independent Critic lane must check, without changing the model or classifier:

- hidden GR/Einstein import;
- circular definition of the selector;
- source inserted by hand;
- coefficient fitting or null-vector targeting;
- post-outcome basis change;
- gauge/density artifact;
- double counting under the frozen equivalence;
- successor-project contamination;
- implicit assumptions absent from this preregistration;
- whether the result exceeds the conformal/vacuum/bounded-family scope.

Critic can invalidate provenance or narrow interpretation, but cannot repair a failed model by modifying the family after seeing the result.

## Claim locks

No outcome of this gate may be reported as:

- GR or Einstein dynamics derived;
- a complete or globally unique candidate theory;
- quantum theory or quantum gravity;
- experimental confirmation;
- `chi_ABC` prediction;
- new physics.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED` and theory established = **0%** throughout this gate.
