# RCG-005 — complete local parity-even dimension-six pure-metric curvature class terminal

Date: 2026-09-17
Status: **TERMINAL SCIENTIFIC FAIL IN FROZEN RCG005-v0 SCOPE**

## Programme authority and prospective chronology

Programme selector preregistration:
`prereg/RCG005_NEXT_MODEL_CLASS_SELECTION_GATE.md`, commit `1bde9c52e00d855f92dcc28cdf8afcf04bd40026`.

Explicit external selection declaration:
`results/RCG005_CURVATURE_DERIVATIVE_CLASS_SELECTION_DECLARATION.md`, commit `513fca5a7df4a69bab56a29b4044f019b97466e6`.

Selection terminal:
`results/RCG005_MODEL_CLASS_SELECTION_TERMINAL.md`, commit `355ac8a2d892e311bd1989e7057c3defac2e7e8a`, classification
`RCG005_CURVATURE_DERIVATIVE_BOUNDED_CLASS_SELECTED_SCOPED`.

Scoped formation authority:
`results/RCG005_FORMATION_AUTHORITY.md`, commit `d2e38871ee5ac2e1331934647575e4a5b6144e4a`, classification
`RCG005_FORMATION_AUTHORIZED_SCOPED`.

Scientific preregistration:
`prereg/RCG005_COMPLETE_PARITY_EVEN_LOCAL_DIM6_PURE_METRIC_CURVATURE_CLASS_V0.md`, commit `1ac1c032dcbbd8e3f0a527a470acc0a44ddffa08`.

Independent generic metric-jet held-out preregistration:
`prereg/RCG005B_GENERIC_METRIC_JET_PRINCIPAL_SYMBOL_HELDOUT.md`, commit `1fb26a399264747fc2ffa8a564d4d281c0586f9c`.

Canonical exact quotient was certified in a separate preprimary phase and then durably frozen **before canonical primary dynamics**:
`results/RCG005_EXACT_QUOTIENT_COMPLETENESS_FREEZE.md`, commit `f4d6f11490c0e668aa934e25580abad3015f0ae1`.

No canonical RCG005 A6/A5/A4/A3/nullspace outcome preceded that quotient freeze.

## Frozen scientific class

Version:
`RCG005_COMPLETE_PARITY_EVEN_LOCAL_DIMENSION_SIX_PURE_METRIC_CURVATURE_CLASS_V0`.

Scope:
- exactly four spacetime dimensions;
- local;
- parity even;
- pure metric;
- correction engineering mass dimension six;
- `VACUUM_ZERO`;
- all scalar contractions of factors `nabla^{k_i} Riemann` satisfying `sum_i (2+k_i)=6` before quotient;
- exact action quotient by Riemann symmetries, algebraic/differential Bianchi identities, exact derivative commutators, exact integration by parts / total derivatives, exact 4D identities and exact duplicates;
- parity-even double-epsilon structures reduced to the exact generalized-delta / metric-contraction span;
- no EOM/on-shell quotient;
- no background-specific quotient;
- no perturbative or derivative-dependent metric field-redefinition quotient;
- no quartic/dimension-eight curvature, matter, extra fields, torsion or nonlocality.

`FIELD_REDEFINITION_EQUIVALENCE = UNRESOLVED_OUT_OF_SCOPE_RCG005_V0`.

EH plus optional cosmological constant is a fixed lower-order reference only and is not an RCG005 correction direction.

## Outcome-independent family-completeness certificate

A separate audit that does not read primary survivor outcomes ran canonically as GitHub Actions run `35178717498`, run number `1`, attempt `1`, head `fa3fa43c2c4357dd3aec99be74a756e5e05da411`, audit job `105066050302`, conclusion `success`.

Artifact:
`10479503273`, digest `sha256:b30a3c3c999a90c7af8463a73482b91b35c3d0ace29b894a1d68b05c3a273e13`.

Audit classification:
`PASS_RCG005_FAMILY_COMPLETENESS_AUDIT`.

The engineering-dimension equation has exactly the four unordered derivative partitions

`(0,0,0), (0,2), (1,1), (4)`,

corresponding to:
- `Riemann^3`;
- `Riemann * nabla^2 Riemann`;
- `(nabla Riemann)*(nabla Riemann)`;
- `nabla^4 Riemann`.

Mechanical raw counts:
- `Riemann^3`: `10395`;
- `D1D1`: `945`;
- `R_D2R`: `945`;
- `D4R`: `105`;
- total: **`12390`**.

Every one of the `945` `R_D2R` raw contractions maps under one exact action-level integration by parts to a `D1D1` raw contraction; the unique image count is `945`.

Every one of the `105` one-curvature `D4R` contractions is an exact covariant total divergence because the outermost derivative index is necessarily metric-contracted and the metric is covariantly constant. The audit explicitly checks all `105`; each possible partner of the outer derivative occurs `15` times.

The derivative-order-swap consistency gives exactly `3` independent commutator relations of exact rank `3`, with generated cubic-curvature terms retained in the same family.

Thus no declared dimension-six template is silently omitted from the action quotient.

## Preprimary exact quotient certification

The first quotient workflow execution `35178140025` failed only because of an undefined parent-manifest helper reference before the Constructor artifact was produced. It has no scientific classification. The execution-only repair was prospectively frozen in commit `c03c693719040ff5ec80da839782379e1b9ae7d3` and repaired code commit `ce4cfe07d8226562700fb193c8b14eefba28f803` without changing science.

Canonical quotient-only run:
- run `35178250959`;
- run number `2`, attempt `1`;
- head `ac3c646b0fc1a5bec2fa6781e5bdb9c8bbb1b820`;
- Constructor `105064632969` — success;
- independent Critic `105064633044` — success;
- aggregate `105064698593` — success.

The quotient aggregate has `aggregate_valid=true` and explicitly records `primary_dynamics_status = NOT_COMPUTED_PREPRIMARY`.

Exact quotient facts:
- canonical algebraic cubic symmetry classes: `13` nonzero;
- canonical `D1D1` symmetry classes: `12` nonzero;
- generic algebraic `nabla Riemann` component dimension after differential Bianchi: `60`;
- exact pointwise rank of the twelve `D1D1` scalar classes: `4`;
- inherited 4D cubic quotient dimension: `6`;
- independent commutator relation count/rank: `3/3`;
- total exact relation-matrix rank on the `12 + 13 = 25` canonical derivative-plus-cubic directions: **`17`**;
- exact action quotient dimension: **`N = 8`**;
- exact relation RREF SHA256: `4b6f9b9713b076a10513adb1b10ab0bfc91b822acda441f976aee2f14a5fd38e`.

Constructor and independent Critic reconstruct the same exact relation-span hash by different tensor routes.

The frozen production quotient is

`2 new derivative directions + 6 inherited canonical RCG004 algebraic-cubic directions`.

The exact embedding rank of RCG004 into RCG005 is `6`.

## Frozen new derivative directions

The two genuinely new quotient axes are canonical `D1D1` classes `9` and `11` under the frozen slot convention. Their exact representatives are recorded in the quotient-freeze document.

On the restored-lapse triaxial primary geometry, their normalized highest-time-derivative quadratic forms are

`P_9 = -(x1+x2+x3)^2`

and

`P_11 = -(x1^2+x2^2+x3^2)`,

with common principal density

`exp(a+b+c-5*n)`

for lapse variable `N=exp(n)`.

A source-faithful metric derivation verifies the spatial curvature-derivative principal coefficient

`partial (nabla_0 R_0i0i) / partial q_i''' = -exp(-3*n)`.

Thus the lapse was not set to one before the new highest-order structure was derived.

## Canonical primary execution

Workflow head:
`23b426084168aef9e95dba7ee903a100effeec92`.

GitHub Actions run:
`35178534613`, run number `1`, attempt `1`, status `completed`, conclusion `success`.

Jobs:
- Constructor `105065495844` — success;
- independent Critic `105065496077` — success;
- direct generalized Euler cross-check `105065554582` — success;
- negative controls `105065632807` — success;
- aggregate `105065703647` — success.

Artifacts:
- Constructor `10479527938`, digest `sha256:b2969ed62bafb7748d413674682520dfe4861ba59ef7c6d9932c9b7a2a1126d4`;
- Critic `10479289150`, digest `sha256:bbc9da42f886def669bb01f1f0e86103d20655a6f1e959c6bf2316802bb469a9`;
- direct Euler `10479537894`, digest `sha256:4f890ed5a93aad6081c1ed54ca5b4eaf0fc370731330fd4607cb4a4d81266ba3`;
- negative controls `10478548700`, digest `sha256:a2eb5068b7c1ae771cee097b14c8338fb7a5c0cb201f5a38dea201b4d07cc232`;
- terminal aggregate `10479114573`, digest `sha256:8e043b361e784aed1a1629720965b1938396e156cf320e9fe4372a03b7f3e587`.

Downloaded JSON SHA256:
- Constructor `f60ce49f94169dd389b4dd40de2bcf118b4bd8191fae91a448fe475a2ffe86a5`;
- Critic `aba9deaa04d5725a3812c037473b2311a4939f8667d0646242c9099dba18e8a6`;
- direct Euler `50768450cb99034310c7f21403d40378970e7b42ac5544236abf8d30a9ac590f`;
- negative controls `1f1f90fc0cf0f7926b563e63ed912dddfdd9dc76e11b0ce3bc45dbf9c0b7c145`;
- aggregate `c5bf49ec1b4f2d93aee2abb70461f1003425375fbd36dfb2674a659d3bb19409`.

Durable provenance manifest:
`results/raw/RCG005_CANONICAL_ARTIFACT_MANIFEST.json`, commit `ac7ba30cd1c58fc029c37dfb0df9191021a56eb8`.

Canonical aggregate has `aggregate_valid=true`; all frozen aggregate predicates are true.

## Exact derivative-order mechanism and sequential elimination

For the two new derivative quotient directions, the Constructor exact sixth-order witness matrix is

`A6 = [[-2,-2],[-2,0],[-2,0],[-2,-2],[-2,0],[-2,-2]]`,

with exact rank

**`rank(A6)=2`**.

Therefore both genuinely new derivative coefficients must vanish before any lower-order cancellation can occur:

`dim(Q_RCG005)=8 -> dim(K6)=6`.

This is mechanism branch

**`A_DERIVATIVE_SECTOR_HAS_NO_NONZERO_HIGHEST_ORDER_DEGENERATE_COMBINATION`**.

The remaining six-dimensional `K6` is exactly the inherited algebraic-cubic RCG004 subspace. Algebraic curvature cubics generate no fifth-order equation terms, hence

`rank(A5 | K6)=0`,

`dim(K5)=6`.

The canonical inherited RCG004 fourth-order restriction has exact rank `6`, so

`rank(A4 | K5)=6`,

`dim(K4)=0`.

Therefore

**`dim(K_SO)=0`**.

There is no nonzero correction vector requiring a third-order rescue check: once `K4={0}`, all further intersections remain zero.

Exact dimension chain:

`12390 raw contractions/templates`
`-> exact action quotient N=8`
`-> A6 rank 2`
`-> K6 dimension 6`
`-> A5-restricted rank 0`
`-> K5 dimension 6`
`-> inherited A4 rank 6`
`-> K4 = K_SO = 0`.

## Independent Critic and generalized Euler confirmation

The independent Critic does not import the Constructor final matrix. It uses reverse pairing enumeration, a self-dual/anti-self-dual cubic route and `200` independent normal-coordinate metric third-jet variables. It independently obtains:
- quotient dimension `8`;
- derivative pointwise rank `4`;
- total relation rank `17`;
- the same exact relation-span SHA256;
- sixth-order rank `2`;
- `K6` dimension `6`;
- inherited A4 restriction rank `6`;
- `K_SO=0`.

Critic classification:
`PASS_INDEPENDENT_CRITIC_RCG005_QUOTIENT_AND_PRIMARY_NULLITY_ZERO`.

The direct generalized-Euler lane independently differentiates the restored-lapse principal reduced action and collects sixth derivatives in `E_a,E_b,E_c`. It obtains a `9 x 2` exact A6 matrix of rank `2`; its overall sign convention differs from the Constructor but its row space is full on the two derivative coefficients. It then independently combines the exact K6 result with the canonical parent direct-Euler A4 restriction rank `6` and obtains `K_SO=0`.

Direct-Euler classification:
`PASS_RCG005_DIRECT_EL_CONFIRMS_PRIMARY_NULLITY_ZERO`.

## Negative controls

All frozen adversarial controls pass. In particular:
- accidental isotropic projection collapses the new A6 rank from `2` to `1`, so the symmetry-masking trap is detected;
- lapse-gauge-fixed-before-variation contamination is detected;
- a known total derivative has zero generalized Euler equation;
- duplicate/basis/column permutations are handled exactly;
- omission of a raw derivative contraction is detected;
- sign-flipped commutator and wrong 4D identity produce different exact relation RREF hashes;
- differential-Bianchi, parity, field-redefinition and source locks all pass.

## Held-out status

The generic metric-jet held-out was frozen before primary outcome, including exact rational seeds, but the frozen rule states that if the primary survivor dimension is zero its scientific survivor test is

**`NOT_APPLICABLE_PRIMARY_NULLITY_ZERO`**.

That condition applies here. No held-out coefficients are inspected or used to refit anything because no primary survivor exists.

## Terminal scientific classification

**`FAIL_SCOPED_RCG005_COMPLETE_LOCAL_DIM6_PURE_METRIC_CLASS_HAS_NO_NONZERO_SECOND_ORDER_SURVIVOR`**

## Scientific interpretation

Within the frozen equivalence convention and exact off-shell second-order criterion, the RCG004 obstruction was **not** merely a consequence of omitting curvature-derivative directions at the same engineering mass dimension.

The complete bounded local parity-even pure-metric dimension-six action quotient contains only two genuinely new derivative directions beyond the six algebraic cubic directions. Those two new directions are independently forced to zero already by sixth-order restored-lapse triaxial dynamics; the remaining six inherited algebraic directions are then eliminated by the already-canonical fourth-order RCG004 obstruction.

This is a class-level scoped falsification of the complete declared RCG005-v0 local dimension-six pure-metric correction class under exact off-shell second-order closure. It is not a failure of one chosen ansatz.

It does **not** prove:
- GR is unique;
- arbitrary higher-curvature gravity fails;
- dimension-eight/quartic classes fail;
- theories with additional fields fail;
- nonlocal theories fail;
- all EFT-equivalent representatives fail under a future field-redefinition quotient;
- ghost freedom, stability, hyperbolicity or unitarity;
- quantum gravity;
- experimental confirmation or new physics.

## Anti-patching next step

Do not append one quartic invariant, scalar/vector field or nonlocal kernel post-outcome. The next object must be a separate prospective programme-level class selector comparing the remaining bounded architectures before any RCG006 family is formed.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
