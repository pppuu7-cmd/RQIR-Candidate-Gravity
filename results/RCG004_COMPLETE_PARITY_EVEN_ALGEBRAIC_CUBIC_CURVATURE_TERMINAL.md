# RCG-004 — complete parity-even algebraic cubic-curvature class terminal

Date: 2026-09-17
Status: **TERMINAL SCIENTIFIC FAIL IN FROZEN RCG004-v0 SCOPE**

## Programme authority and chronology

Explicit A1 programme declaration:
- `results/RCG004_A1_PROGRAMME_AUTHORITY_DECLARATION.md`
- commit `dae86c4ccf885622fbf5b4254be4b3fa80ccf5a2`

Authority terminal:
- `results/RCG004_FORMATION_AUTHORITY_TERMINAL.md`
- commit `28781bc1873413b214f751eaa963cf1c51423e0b`
- classification `RCG004_FORMATION_AUTHORIZED_SCOPED`

Scientific preregistration:
- `prereg/RCG004_COMPLETE_PARITY_EVEN_ALGEBRAIC_CUBIC_CURVATURE_FAMILY_V0.md`
- commit `345213253f2ecf415af40cb4fbae47b4f58d8870`

Held-out preregistration, frozen before survivor inspection:
- `prereg/RCG004B_RESTORED_LAPSE_TRIAXIAL_HELDOUT.md`
- commit `5f83a594309429b45a8edd1bdc72b9653fffdc75`

Parent RCG003B terminal:
`72f9ab2ab5ad85259a18fc1f368777c431a56324`.

No RCG004 basis/nullspace/survivor outcome preceded the authority or scientific preregistrations.

## Frozen model class

Version:
`RCG004_COMPLETE_PARITY_EVEN_ALGEBRAIC_CUBIC_CURVATURE_FAMILY_V0`.

Scope:
- exactly 4D;
- parity even;
- exactly cubic in curvature;
- complete algebraic metric contractions of three Riemann tensors, including all Ricci/scalar contractions as subcases;
- `VACUUM_ZERO`;
- no curvature derivatives;
- no quartic/higher curvature;
- no matter, torsion, extra fields, or nonlocality;
- `FIELD_REDEFINITION_EQUIVALENCE = OUT_OF_SCOPE_RCG004_V0`.

## Canonical implementation provenance

- Constructor: `scripts/rcg004_complete_cubic_constructor.py`, commit `070e1594b3691755d5e2dd1db29f9191ceb49cad`.
- Independent Critic: `scripts/rcg004_complete_cubic_critic.py`, commit `bf77cb21c2109c1c7f1df4058bc827db5f6bda28`.
- Direct Euler-Lagrange cross-check: `scripts/rcg004_direct_euler_crosscheck.py`, commit `ec68b6dd77a1cd236912c14822f4806364205ff3`.
- Negative controls: `scripts/rcg004_negative_controls.py`, commit `77cbd509ca3e7449e93b9d0ea653f62e700fe944`.
- Frozen aggregate: `scripts/rcg004_terminal_aggregate.py`, commit `2a6bcfce86cd31a816c3178a1e0fbcb5c03f4c46`.
- Workflow head: `f62d3ad892453725e6838059929f0f6212d4d3d6`.

## Canonical GitHub Actions execution

Run `35175941323`, run number `1`, run attempt `1`, status `completed`, conclusion `success`.

Jobs:
- Constructor `105057546423` — success;
- independent Critic `105057546296` — success;
- direct Euler cross-check `105057593950` — success;
- negative controls `105057593932` — success;
- aggregate `105057676864` — success.

Artifacts:
- Constructor `10478268717`, digest `sha256:82d5347c4031bf9cbd1ca37a57e96973b6921f26f04ac750435e81d40f685ab7`;
- Critic `10478029848`, digest `sha256:55342f3747b15edb39bd08932d0fdee5f106944ba15e1bd696397fdc76482bc6`;
- Euler `10479110111`, digest `sha256:7b66b06c5945cebd4d61990c5555587890a79293ae963a4aa2b55a8019639eff`;
- negative controls `10477789460`, digest `sha256:f3f2a40df1f71b2ad696d99ee90322340e7dd89f0923bc9c80a3e2255ef12e8c`;
- terminal aggregate `10478064839`, digest `sha256:570db330d40847f128c10ed1f0c32468bac23f5fddfa7f1c9f72fbbd0ae5e348`.

Downloaded artifact JSON SHA256:
- Constructor `f1d99ce8e4b4494ee0b960af36cde67854a27bd068b7252b4e67cc8f0338f678`;
- Critic `2d181059dc4f373fddb3035c7ea42102222913e903bc2ee29038613df59041d8`;
- Euler `87fae7fb38d40028dfb1d3ec1c2bb4142e8c12ae34c33d37c7fb3cbd47a6d664`;
- negative controls `afc57fcba8100d530bf1afc858e1338020ddc8edac739aed1162397788af4200`;
- aggregate `e28b8dcfab71b7f5825253dccb5059247c180aa342ae7143b7690969442f68a8`.

Durable manifest:
`results/raw/RCG004_CANONICAL_ARTIFACT_MANIFEST.json`, commit `094dfa5e3eec39fe5fea674b627812850342832e`.

Durable aggregate:
`results/raw/RCG004_TERMINAL_AGGREGATE.json`, commit `5ed5954f072259b1a612c1acdf7e46db1e6b2349`.

## Complete raw contraction enumeration

The class was not started from a remembered invariant list.

Three labelled Riemann factors provide twelve covariant slots. The Constructor and Critic independently enumerated **all perfect matchings** of those twelve slots:

`raw contraction matchings = 11!! = 10395`.

After exact Riemann pair antisymmetries, pair exchange, factor permutation and self-negating contractions:

- nonzero canonical contraction classes: `13`;
- symmetry-zero classes: `20`.

Constructor raw manifest SHA256:
`c7eead842d92f580a258987f78df05c8bb001825f7c3d6f7d493a178b4a7f454`.

Critic uses a different raw enumeration ordering/encoding, so its raw-manifest hash differs while the exact canonical class manifest agrees.

## Exact 4D algebraic quotient

Constructor certificate:
- exact generic 4D algebraic curvature tensor dimension: `20`;
- universal cubic polynomial coefficient matrix shape: `238 x 13`;
- exact rank: `6`;
- exact relation nullity: `7`;
- quotient dimension: **`N = 6`**;
- universal matrix SHA256: `3e5d03c1c4f15b4b55bb710970fe49a2f60cadd8d0f79d69d7916953fe695437`;
- deterministic quotient basis class indices `[0,1,2,4,5,8]`.

The universal certificate is an exact polynomial identity calculation on the full 20-dimensional algebraic-curvature space, not a finite metric sample.

Independent Critic uses the self-dual/anti-self-dual `Lambda^2` block parametrization with exact Bianchi condition and independently obtains:
- generic curvature dimension `20`;
- exact quotient rank/dimension **`6`**;
- a different independent basis `[12,11,7,5,4,3]`.

Thus basis labels are not being forced to agree; the independent dimension/completeness result agrees.

## RCG003 embedding regression

Exact embedding rank of the old Ricci-only cubic subspace is `3`.

In the Constructor basis:
- `R^3 -> (1,0,0,0,0,0)`;
- `R R_ab R^ab -> (0,1,0,0,0,0)`;
- `Tr(Ricci^3) -> (0,0,0,0,-1,0)`.

The old primitive ray `(7,-36,36)` therefore transports to

`(7,-36,0,0,-36,0)`.

When restricted to the RCG003B axisymmetric geometry, the new RCG004 framework reproduces the canonical RCG003B Hessian **exactly**, including the prior shear obstruction. Regression status: PASS.

Transverse-shear negative control on isotropic background recovers

`H_beta_beta = -1296*(u_sigma + v_sigma^2)`.

Thus symmetry masking is detected rather than silently reintroduced.

## Primary fully triaxial off-shell gate

Production geometry:

`ds^2 = -dt^2 + exp(2a(t))dx^2 + exp(2b(t))dy^2 + exp(2c(t))dz^2`,

with independent arbitrary off-shell `a,b,c`.

Constructor and Critic independently derive the curvature from the metric and verify the compact orthonormal Riemann table before evaluating invariants.

For the six-dimensional exact quotient coefficient space, the collected acceleration-Hessian constraint system has:

Constructor:
- rows `54`;
- columns `6`;
- exact rank **`6`**;
- nullity **`0`**;
- Hessian matrix SHA256 `7014978a97fce634d93f00e414903597245b8e4268b2c575dd1764547f96ced9`.

Independent Critic on its different basis:
- rows `54`;
- columns `6`;
- exact rank **`6`**;
- nullity **`0`**;
- matrix SHA256 `e3e7c503deb87a85f6107b86a04652ec9ea73e78e246aad2bcfbc8d9ffe996fc`.

Therefore

`ker(A_H) = {0}`.

Since the Hessian kernel is already zero, no acceleration-linear curl can rescue a nonzero member. The combined Hessian+curl survivor dimension is also `0`.

## Direct Euler-Lagrange adversarial cross-check

The independent direct E-L lane derives the reduced equations and collects all high-derivative structures:

- high-derivative coefficient rows: `270`;
- exact high-derivative rank: `6`;
- high-derivative nullity: `0`;
- fourth-derivative rows: `81`, rank `6`;
- third-derivative rows: `189`, rank `6`;
- elementwise fourth-derivative/Hessian correspondence: `true`.

Classification:
`PASS_RCG004_DIRECT_EL_CONFIRMS_PRIMARY_NULLITY_ZERO`.

## Negative controls

All frozen adversarial controls pass, including detection/guards for omitted/duplicate invariants, false 4D identity, wrong Riemann sign, wrong Ricci contraction, density-factor change, accidental isotropy/axisymmetry, EOM substitution, coefficient-column permutation, post-outcome basis extension, approximate nullspace, source/dimension changes, field-redefinition quotient contamination, and removal of shear variation.

## Aggregate validity

Canonical aggregate has `aggregate_valid=true`.

Every frozen predicate is true, including authority/prereg/held-out chronology, complete raw enumeration agreement, canonical class agreement, both exact quotient routes, independent basis selection, metric derivations, RCG003 embedding/regression, both full-rank triaxial Hessians, direct E-L nullity zero, Hessian correspondence, negative controls, source lock and field-redefinition firewall.

## Exact dimension chain

Inside the frozen RCG004-v0 scope:

`10395 raw matchings`

`-> 13 nonzero symmetry classes`

`-> 6 exact independent 4D algebraic cubic-curvature directions`

`-> 0 triaxial Hessian survivors`

`-> 0 direct-Euler verified survivors`.

The restored-lapse held-out gate was prospectively frozen before survivor inspection, but is

`NOT_APPLICABLE_PRIMARY_NULLITY_ZERO`

because there is no nonzero primary survivor subspace to test or refit.

## Terminal scientific classification

**`FAIL_SCOPED_RCG004_COMPLETE_PARITY_EVEN_ALGEBRAIC_CUBIC_CURVATURE_CLASS_HAS_NO_NONZERO_TRIAXIAL_SECOND_ORDER_SURVIVOR`**

## Scientific interpretation

This answers the specific next question posed after RCG003B: the RCG003-v0 failure was **not merely caused by excluding Riemann-containing algebraic cubic invariants**, because the complete bounded 4D parity-even algebraic curvature-cubic class itself has zero nonzero survivors under the frozen genuinely triaxial second-order derivative-closure requirement.

This is a class-level scoped falsification, not a coefficient-level failed ansatz.

It is **not** a no-go theorem for:
- arbitrary cubic gravity under broader equivalence conventions;
- curvature-derivative theories;
- quartic/higher-curvature theories;
- theories with extra fields;
- nonlocal theories;
- arbitrary modified gravity.

It does not select GR and does not establish uniqueness, ghost freedom, stability, hyperbolicity, unitarity, matter completion, phenomenology, quantum gravity, or new physics.

## Anti-patching next step

Do not append one curvature-derivative term or one quartic term to cancel this witness post-outcome.

The next object must be a separate prospective **model-class selection gate** comparing bounded next-family options before any one family is formed.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
