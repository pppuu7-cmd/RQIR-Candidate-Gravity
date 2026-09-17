# RQIR-Candidate-Gravity current front

Updated: 2026-09-17 after canonical RCG003B Actions terminalization and prospective RCG004 authority-gate freeze.

## Canonical programme/scientific phase

`RCG002_HISTORICAL_SCIENCE_TERMINAL / D3_CONSUMED_BY_RCG003_FORMATION / RCG003_CONFORMAL_PASS / RCG003B_AXISYMMETRIC_FAIL / RCG003_V0_NONZERO_SURVIVORS_ZERO_IN_FROZEN_DERIVATIVE_SCOPE / RCG004_FORMATION_AUTHORITY_BLOCKED`

The old programme-disposition wait-state is closed and must not be reopened.

Historical RCG-002 state remains:
- `RSC = NEAR_SURVIVOR_NOT_SELECTED`;
- `AD1 = ARCHITECTURE_DISPOSITION_NOT_UNIQUELY_SELECTED_PREOUTCOME`;
- historical science unchanged by later programme authority.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.

## RCG003-v0 formation and conformal gate

Version:
`RCG003_MINIMAL_NONLINEAR_CUBIC_RICCI_FAMILY_V0`.

Frozen family:
`lambda R^3 + mu R R_{mu nu}R^{mu nu} + nu R_mu^nu R_nu^rho R_rho^mu`.

Status: `NEW_MODEL_POSTULATE`, not historical RCG-002 law.

Conformal formation/gate preregistration:
`0bba0ea6e1d4e13635f70f3b5056e131afba6c7d`.

Conformal terminal:
`ded5a44078c57909aeb6592b88bdac5c0917f85d`.

Conformal result:
`PASS_SCOPED_RCG003_CONFORMAL_SECOND_ORDER_NONZERO_DEFORMATION_EXISTS`.

Exact coefficient-space reduction:
`3 -> 1`, with primitive surviving ray `(7,-36,36)`.

This conformal survivor was never a physical selection or global uniqueness statement.

## Canonical RCG003B held-out anisotropic result — TERMINAL FAIL

Gate:
`RCG003B_AXISYMMETRIC_BIANCHI_I_DERIVATIVE_CLOSURE`.

Frozen preregistration:
`dbb0b54465c628b533c646a5b3b74b8458eaf24e`.

Terminal result file:
`results/RCG003B_AXISYMMETRIC_BIANCHI_I_DERIVATIVE_CLOSURE_TERMINAL.md`.

Terminal commit:
`72f9ab2ab5ad85259a18fc1f368777c431a56324`.

Canonical Actions:
- run `35156147876`;
- run number `1`, attempt `1`;
- workflow head `241a923523b2c770ffc8c48315d931af6e61846f`;
- all Constructor / Critic / Euler / aggregate jobs completed `success`.

Artifacts:
- Constructor `10471991651`, digest `sha256:9f230b1ca16a31e3459309f0eb245217b37dcdc77f918f505db2ce506bad32f6`;
- Critic `10472051589`, digest `sha256:7691b12c0205010c15c645966400c8088bdd2b91e5f458ab4c4f9bfbe1f8b076`;
- Euler cross-check `10471213517`, digest `sha256:1ccaf2da2fd6eedd1ca56b5c8a8d2172638752ba9891f5a68dc2f8341c5a35a8`;
- aggregate `10471802799`, digest `sha256:3f0be5fe8255ba2368f6d125ef537340db7d21b1ecef046031861d2033a06e86`.

Raw repository persistence:
- aggregate commit `9fc74204c70dfffcd60d42295ab60de28da648de`;
- Constructor commit `2b2bac6825ac531305c98e305e6e3227a669697e`;
- Critic commit `2971785dc5bf8941250269e74d85f05edffdfd9b`;
- Euler commit `72deca7ed04e7476c790c0e1f4d1bc20487327da`.

Canonical aggregate has `aggregate_valid=true`; all twelve frozen validity predicates are true, including exact prereg/parent/head/ray locks, both control lanes, Critic provenance, Constructor–Critic Hessian identity, Euler–Hessian correspondence, lane agreement, allowed classification, and source lock.

Primary terminal classification:

`FAIL_SCOPED_RCG003B_AXISYMMETRIC_HIGHER_DERIVATIVE_SURVIVOR_FALSIFIED`.

Independent Critic:

`PASS_INDEPENDENT_CRITIC_RCG003B_SCOPE_AND_PROVENANCE`.

## Exact anisotropic obstruction

After factoring the common nonzero density factor `exp(a+2b)`, with `va=adot`, `vb=bdot`, `ua=addot`, `ub=bddot`:

`H_aa = -48*(2*ua + ub + 2*va^2 + va*vb)`

`H_ab = -48*(ua - 4*ub + va^2 + 2*va*vb - 6*vb^2)`

`H_bb = 48*(4*ua - 7*ub + 4*va^2 + 5*va*vb - 12*vb^2)`.

Minimal exact witness:
- `H_aa`;
- monomial `ub`;
- coefficient `-48`;
- common density factor `exp(a+2b)`.

Direct Euler-Lagrange cross-check independently reproduces the same fourth-derivative coefficient structure and has `fourth_hessian_correspondence=true`.

Exact descriptive determinant:
`det(H) = -20736*(ua-ub+va^2+va*vb-2*vb^2)^2`.

The isotropic pullback still recovers zero Hessian, so the mechanism is specifically isotropic/conformal masking of an anisotropic higher-derivative obstruction.

## Model-space accounting

Only inside the frozen RCG003-v0 family and frozen derivative-order requirements:

`dim(raw)=3 -> dim(after conformal)=1 -> dim(after axisymmetric RCG003B)=0 nonzero rays`.

This is a real scoped falsification of the entire remaining nonzero RCG003-v0 ray. It is not a no-go theorem for all cubic gravity, higher-curvature gravity, or arbitrary nonlinear gravity.

Do not refit `(7,-36,36)` and do not add an operator post-outcome to rescue RCG003-v0.

## RCG004 programme boundary

The extant D3 declaration authorized only one prospectively controlled new-version formation attempt. That authority was consumed by RCG003 formation.

A broader Riemann-containing cubic family would be a new version, not an implementation repair.

Prospective authority gate:
`prereg/RCG004_MINIMAL_ALGEBRAIC_CUBIC_EXTENSION_AUTHORITY.md`.

Authority preregistration commit:
`b2d2cdc1c9bc169317e3e7dfd1a6d17109d01251`.

Current programme classification:
`BLOCKED_PENDING_EXPLICIT_RCG004_FORMATION_AUTHORITY`.

Blocker record:
`results/RCG004_MINIMAL_ALGEBRAIC_CUBIC_EXTENSION_AUTHORITY_BLOCKED.md`, commit `f7bf6d899c05ba0d5de0f7eefee8266b78604f15`.

A future programme declaration must choose exactly one:
- `AUTHORIZE_RCG004_COMPLETE_PARITY_EVEN_ALGEBRAIC_CUBIC_CURVATURE_FORMATION_ATTEMPT`, or
- `DO_NOT_AUTHORIZE_RCG004_FORMATION_HOLD_PROGRAMME`.

No scientific RCG004 operator basis, coefficient nullspace, survivor, or triaxial outcome is authorized before that declaration is incorporated.

If authorization A1 is later granted, the highest-information scientific target is already bounded conceptually: complete 4D parity-even algebraic curvature-cubic sector, exact algebraic/dimensional quotient, no curvature derivatives/quartics/matter, exact symbolic coefficients, full triaxial off-shell derivative-order constraint map, independent Critic, and a held-out no-refit test frozen before survivor inspection. These are scope ceilings for future preregistration, not current model content.

## Exact next action

`CONSUME_EXPLICIT_RCG004_FORMATION_AUTHORITY_DECLARATION_IF_PROVIDED; OTHERWISE_DO_NOT_FORM_OR_EVALUATE_RCG004`.

Do not repeat RCG003 conformal closure or RCG003B run `35156147876`.
Do not refit the RCG003 ray.
Do not compute `chi_ABC`.

## Claim locks

No current result establishes:
- GR/Einstein dynamics derived;
- complete or unique gravity theory;
- arbitrary nonlinear-gravity no-go;
- full nonlinear constraint closure;
- hyperbolicity, stability, ghost freedom, or unitarity;
- matter completion;
- quantum gravity;
- experimental confirmation;
- new physics.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
