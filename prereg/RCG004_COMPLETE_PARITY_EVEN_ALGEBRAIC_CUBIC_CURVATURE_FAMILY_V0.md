# RCG-004 — complete parity-even algebraic cubic-curvature family v0 (PREOUTCOME)

Date: 2026-09-17
Status: **PROSPECTIVELY FROZEN BEFORE BASIS/RANK/NULLSPACE/SURVIVOR OUTCOME**

Programme authority terminal:
- `results/RCG004_FORMATION_AUTHORITY_TERMINAL.md`
- commit `28781bc1873413b214f751eaa963cf1c51423e0b`
- classification `RCG004_FORMATION_AUTHORIZED_SCOPED`

Parent scientific terminal:
- `results/RCG003B_AXISYMMETRIC_BIANCHI_I_DERIVATIVE_CLOSURE_TERMINAL.md`
- commit `72f9ab2ab5ad85259a18fc1f368777c431a56324`
- classification `FAIL_SCOPED_RCG003B_AXISYMMETRIC_HIGHER_DERIVATIVE_SURVIVOR_FALSIFIED`

## Version identity

`RCG004_COMPLETE_PARITY_EVEN_ALGEBRAIC_CUBIC_CURVATURE_FAMILY_V0`

This is new prospectively authorized model content. It is not historical RCG003 law and does not rewrite RCG003B.

## Main scientific question

Does **any nonzero member** of the complete bounded 4D parity-even algebraic curvature-cubic class survive a genuinely anisotropic second-order derivative-closure test?

The whole finite class is tested. No operator is added after seeing a witness.

## Frozen scope

- spacetime dimension: exactly `4`;
- parity: `even`;
- curvature order: exactly cubic;
- building blocks: metric contractions of `R`, `R_ab`, `R_abcd`, equivalently all complete contractions of three algebraic Riemann tensors;
- source: exactly `VACUUM_ZERO`;
- no curvature derivatives;
- no `nabla R`, `Box R`, or derivative-curvature operators;
- no quartic/higher curvature order;
- no torsion;
- no matter;
- no additional fields;
- no nonlocality;
- no coefficient fitting;
- no approximate numerical nullspace.

`FIELD_REDEFINITION_EQUIVALENCE = OUT_OF_SCOPE_RCG004_V0`.

## Mechanical raw contraction generator

Do **not** begin from a remembered invariant list.

Represent the raw class by three labelled abstract Riemann factors, each with four covariant index slots. Generate every perfect matching of the twelve slots; each matching denotes a complete metric contraction. This mechanically includes contractions conventionally expressible using scalar curvature and Ricci tensors because those are contractions of Riemann.

Persist the complete raw matching manifest before quotient reduction, together with a deterministic canonical encoding and SHA256.

Raw generation is purely combinatorial. No scientific survivor information is used to generate or filter the set.

## Frozen exact quotient/equivalence convention

Quotient only by exact algebraic identities valid in 4D:
- Riemann antisymmetry in each pair;
- exchange of index pairs;
- algebraic first Bianchi identity;
- Ricci/scalar contraction identities inherited from Riemann contraction;
- exact duplicate contractions;
- exact dimension-specific 4D tensor identities, including Schouten identities where applicable.

Do **not** quotient by:
- equations of motion;
- integration by parts involving derivative-curvature structures;
- perturbative/on-shell equivalence;
- field redefinitions;
- derivative-dependent metric redefinitions;
- phenomenological equivalence.

### Exact universal 4D component certificate route (Constructor)

For quotient certification, use an exact generic 4D algebraic curvature tensor, not a sampled metric.

Encode an arbitrary algebraic curvature tensor as a symmetric bilinear form on `Lambda^2(R^4)` (six oriented 2-form basis elements), with the exact single 4D first-Bianchi constraint imposed so that the representation has the full 20-dimensional algebraic-curvature freedom. Its independent entries are algebraically independent symbolic variables over `Q` after solving the Bianchi relation.

For each raw contraction, perform the complete finite 4D index sums exactly and expand the result as a homogeneous cubic polynomial in those independent algebraic-curvature variables. Equality of these universal symbolic polynomials is an exact 4D algebraic identity certificate; it is not finite random metric testing.

Persist:
- raw contraction manifest;
- canonical contraction classes under manifest symmetries;
- universal polynomial coefficient vectors/hashes;
- exact relation matrix;
- exact relation rank;
- quotient dimension `N`;
- exact independent quotient basis/spanning set.

Do not assume `N` in advance.

### Independent Critic completeness route

Critic must not import Constructor relation matrix, rank, basis, or verdict. It must independently reconstruct the quotient using a distinct contraction-graph/tensor-symmetry route and exact 4D identity reconstruction. Different basis labels are allowed; compare exact spans/ranks rather than names.

Finite random exact metrics may be negative/diagnostic controls only, never the sole proof of a universal identity.

## RCG003 embedding regression

Identify the exact quotient-space embedding of:
- `R^3`;
- `R R_ab R^ab`;
- `R_a^b R_b^c R_c^a`.

Verify the exact embedded rank. Transport old primitive ray `(7,-36,36)` only as a regression vector. It must reproduce the canonical RCG003B higher-derivative shear obstruction. It may never be used as a fit target.

## Primary production geometry

Use fully triaxial off-shell Bianchi-I with unit lapse:

`ds^2 = -dt^2 + exp(2a(t)) dx^2 + exp(2b(t)) dy^2 + exp(2c(t)) dz^2`.

`a(t), b(t), c(t)` are independent arbitrary smooth histories.

Forbidden in production:
- `a=b`, `b=c`, `a=c`, or `a=b=c`;
- equations of motion;
- constant-Hubble assumptions;
- special trajectories.

Derive metric, inverse metric, Christoffels, Riemann, Ricci, scalar curvature, and every quotient-basis invariant directly from this metric. Old simplified RCG003 expressions are regression controls only.

## General reduced Lagrangian

`L = sqrt(|g|) * Sum_i c_i I_i`,

where `(I_1,...,I_N)` is the exact quotient basis and `c=(c_1,...,c_N)` is an exact symbolic coefficient vector.

Do not normalize any coefficient before a nonzero survivor subspace exists.

## Primary acceleration-Hessian classifier

Define
- `v_a=adot`, `v_b=bdot`, `v_c=cdot`;
- `u_a=addot`, `u_b=bddot`, `u_c=cddot`.

Compute all symmetric entries of
`H_ij = partial^2 L / (partial u_i partial u_j)`
for `i,j in {a,b,c}`.

Remove only globally known nonzero common density factors. Collect every independent exact polynomial coefficient to build

`A_H c = 0`.

Persist exact:
- number of quotient columns `N`;
- raw collected equations;
- independent equation count;
- `rank(A_H)`;
- `nullity(A_H)`;
- exact kernel basis/span certificate.

No floating SVD and no tolerance-based zero.

## Linear-acceleration integrability

For the Hessian kernel only, write

`L = A_a(q,v) u_a + A_b(q,v) u_b + A_c(q,v) u_c + B(q,v)`

and impose exact velocity-space curls

`C_ab = dA_a/dv_b - dA_b/dv_a`,
`C_ac = dA_a/dv_c - dA_c/dv_a`,
`C_bc = dA_b/dv_c - dA_c/dv_b`.

Collect them into `A_C c=0` and define

`A_primary = stack(A_H,A_C)`.

Persist exact rank/nullity and the **entire** survivor subspace. Never select a preferred vector merely because one looks simple.

## Direct Euler-Lagrange cross-check

An independent route must derive reduced Euler-Lagrange equations for `a,b,c` and collect all coefficients of fourth derivatives and independent third-derivative structures. Their common vanishing subspace must equal the Hessian+curl survivor span exactly.

Disagreement => `INVALID_RCG004_IMPLEMENTATION_DISCREPANCY`, not a scientific PASS/FAIL.

## Symmetry-masking lesson / transverse-shear regression

Background symmetry and variation space are distinct.

Dedicated regression control: on `a=b=c=sigma` background, retain independent infinitesimal anisotropic/shear perturbation directions. The embedded RCG003 ray must still expose its known shear obstruction. If an implementation makes `(7,-36,36)` fully second-order after removing transverse variations, stop and classify implementation invalidity.

## Arithmetic policy

Primary policy: exact integer/rational/symbolic polynomial arithmetic over `Q`; exact sparse Gaussian elimination where feasible.

No modular rank is authorized in the initial implementation. If exact sparse elimination becomes computationally infeasible, a **new prospective execution-only arithmetic preregistration** must freeze primes, denominator clearing, rank reconstruction, unlucky-prime detection and exact verification before modular results are read.

## Mandatory controls

Positive/regression:
1. RCG003 embedding has expected exact span unless an explicitly certified 4D identity changes it;
2. embedded `(7,-36,36)` reproduces canonical RCG003B shear obstruction;
3. conformal restriction control;
4. axisymmetric restriction control;
5. axis permutation consistency;
6. off-shell lock;
7. source lock `VACUUM_ZERO`;
8. transverse-shear control.

Negative controls must detect at least:
- omitted invariant/contraction orbit;
- duplicate quotient basis element;
- false 4D identity;
- wrong Riemann sign;
- wrong Ricci contraction;
- wrong density factor;
- accidental isotropy/axisymmetry;
- EOM substitution;
- coefficient-column permutation;
- post-outcome basis extension;
- numerical approximate nullspace;
- changed source/dimension;
- field-redefinition quotient accidentally enabled;
- shear direction removed from perturbation space.

## Independent Critic

Critic must independently reconstruct at minimum:
- raw/completeness certificate;
- quotient dimension/span;
- triaxial curvature route;
- Hessian constraints;
- curl constraints;
- exact ranks/nullity;
- complete survivor span.

Critic may not import Constructor matrices, rank, kernel, basis or verdict. If bases differ, certify mutual containment/exact span equality.

## Held-out chronology lock

A separate restored-lapse triaxial held-out preregistration **must be committed before any primary survivor/nullspace is inspected**. The held-out result cannot alter the primary coefficients or quotient basis.

## Frozen scientific classifiers

Provided basis completeness, quotient validity, controls, chronology and Critic all pass:

- if `ker(A_primary)={0}`:
  `FAIL_SCOPED_RCG004_COMPLETE_PARITY_EVEN_ALGEBRAIC_CUBIC_CURVATURE_CLASS_HAS_NO_NONZERO_TRIAXIAL_SECOND_ORDER_SURVIVOR`;

- if primary nullity `>0`:
  `PASS_SCOPED_RCG004_PRIMARY_NONZERO_SURVIVOR_SUBSPACE_EXISTS`, with the full exact subspace retained and no preferred-vector selection;

- if held-out later reduces every primary survivor to zero:
  `FAIL_SCOPED_RCG004_HELDOUT_RESTORED_LAPSE_FALSIFIES_ALL_PRIMARY_SURVIVORS`;

- if held-out leaves dimension `>0`:
  `PASS_SCOPED_RCG004_HELDOUT_NONZERO_SURVIVOR_SUBSPACE_REMAINS`, retaining the full residual subspace;

- chronology, completeness, identity, source, coefficient-fit or implementation contamination:
  `INVALID_RCG004` with exact reason.

`BLOCKED` is reserved for inability to construct a frozen object without a new substantive assumption, not for scientific failure.

## Claim ceiling

No outcome of this gate alone establishes GR, unique gravity, all cubic-gravity failure, arbitrary higher-curvature no-go, ghost freedom, hyperbolicity, stability, unitarity, matter completion, phenomenology, quantum gravity, or new physics.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.