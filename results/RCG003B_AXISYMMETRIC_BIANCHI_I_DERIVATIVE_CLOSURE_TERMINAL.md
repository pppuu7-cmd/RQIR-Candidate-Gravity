# RCG-003B — axisymmetric Bianchi-I derivative-closure terminal

Date: 2026-09-17
Status: **TERMINAL SCIENTIFIC FAIL IN FROZEN SCOPE**

## Frozen authority

- Parent RCG003 scientific terminal: `ded5a44078c57909aeb6592b88bdac5c0917f85d`.
- RCG003B preregistration: `dbb0b54465c628b533c646a5b3b74b8458eaf24e`.
- Fixed production ray: `(lambda,mu,nu)=(7,-36,36)`.
- Source: `VACUUM_ZERO`.
- Held-out metric: `ds^2=-dt^2+exp(2a(t))dx^2+exp(2b(t))(dy^2+dz^2)` with independent arbitrary off-shell `a(t),b(t)`.
- No refit, family enlargement, basis search, matter insertion, isotropy condition, EOM use, special trajectory, or successor import was permitted.

## Frozen implementation provenance

- Constructor commit: `f7353512a31bdee081e63dc832a675ec16987121`.
- Independent Critic commit: `49ea8d43f1dbca0e5212a67314cba9d5226a087c`.
- Direct Euler-Lagrange cross-check commit: `b8dbe1c00fc7ad32444f682309526b3116ca9ede`.
- Frozen aggregate commit: `7989f4ace99d5efc6432f8ac41a7cb42eb0c98b0`.
- Workflow head: `241a923523b2c770ffc8c48315d931af6e61846f`.

## Canonical GitHub Actions execution

Run `35156147876`, run number `1`, run attempt `1`, status `completed`, conclusion `success`.

Jobs:
- Constructor: `104995924624` — success.
- Euler cross-check: `104995924852` — success.
- independent Critic: `104995924979` — success.
- aggregate: `105000677452` — success.

Artifacts:
- Constructor `10471991651`, digest `sha256:9f230b1ca16a31e3459309f0eb245217b37dcdc77f918f505db2ce506bad32f6`.
- Critic `10472051589`, digest `sha256:7691b12c0205010c15c645966400c8088bdd2b91e5f458ab4c4f9bfbe1f8b076`.
- Euler cross-check `10471213517`, digest `sha256:1ccaf2da2fd6eedd1ca56b5c8a8d2172638752ba9891f5a68dc2f8341c5a35a8`.
- terminal aggregate `10471802799`, digest `sha256:3f0be5fe8255ba2368f6d125ef537340db7d21b1ecef046031861d2033a06e86`.

Downloaded canonical JSON SHA256:
- Constructor JSON: `96eaed1364048f3490294c7fd6756b17c4e4505adfcca3a599c6805819f2d7cf`.
- Critic JSON: `af0ad5f78e16622d17d3617010c1a6ca3580041343653d07b63199dff7cd64a6`.
- Euler JSON: `adb6fed96c8ea1dab8ac05f2b90df9f4166496b77f20e01a2d95b90caee5cb04`.
- Aggregate JSON: `9bbe837aebc84d19824f698c9b2f7123e023a3f8fa0a99bc508593fc937e0992`.

Scientific payload SHA256:
- Constructor: `4493bbdafbea64d91bb66725673a023baca91411ed5d1679ccbfde4985f1997b`.
- Critic: `480a39eede957a3986dd19acb8fa5f4ab6886d82e5e49b1e82fa955c1cdca94e`.
- Euler: `c93c50597bf1a4fa26c4cb909d33cee319aedac5bc2a14d839adf100cd5911fa`.
- Aggregate: `7bcfd23a92ab892f0446f12cf2878fd100e7e2f732755943920a5d5fe8f84eab`.

Symbolic-expression SHA256:
- Constructor: `1aa5be6f7a8f5f6eaa1575790108bbbce1f008c2eae4d7b5d02731015a7db3d3`.
- Critic: `51699117a70ca1e0694f67c447befcdf55216164ad83b01bd7a0f51ec32f315a`.
- Euler: `8c9cd01db4cd4b6c9a173e9371fac62ee0ec1a37c69ab9ec9a7ab75d5a715b04`.

## Frozen aggregate validity

The canonical aggregate has `aggregate_valid=true`. Every preregistered validity predicate is true:

- `prereg_all_exact=true`;
- `parent_terminal_all_exact=true`;
- `run_head_all_exact=true`;
- `fixed_ray_all_exact=true`;
- `constructor_controls_valid=true`;
- `critic_controls_valid=true`;
- `critic_provenance_pass=true`;
- `constructor_critic_hessian_exact_match=true`;
- `euler_hessian_correspondence=true`;
- `lane_classifications_agree=true`;
- `classification_allowed=true`;
- `source_lock=true`.

Thus green CI is not being used as the classifier; the frozen scientific predicates are satisfied and the artifact classification is admissible.

## Exact canonical obstruction

After factoring the common nonzero density factor `exp(a+2b)`, with

`va=adot`, `vb=bdot`, `ua=addot`, `ub=bddot`,

the canonical acceleration Hessian is

`H_aa = -48*(2*ua + ub + 2*va^2 + va*vb)`

`H_ab = -48*(ua - 4*ub + va^2 + 2*va*vb - 6*vb^2)`

`H_bb = 48*(4*ua - 7*ub + 4*va^2 + 5*va*vb - 12*vb^2)`.

It is not the zero polynomial on the independent off-shell anisotropic history space.

Minimal exact obstruction witness, reproduced by Constructor and Critic:
- component `H_aa`;
- monomial `ub`;
- exact coefficient `-48`;
- common density factor `exp(a+2b)`.

The direct Euler-Lagrange lane independently reproduces the same normalized coefficient as a fourth-derivative obstruction in `E_a` and verifies `fourth_hessian_correspondence=true`.

A descriptive exact determinant diagnostic derived from the canonical Hessian is

`det(H) = -20736*(ua-ub+va^2+va*vb-2*vb^2)^2`.

This determinant is not an additional classifier.

## Controls

Constructor controls all pass:
- isotropic recovery;
- perturbed ray `(8,-36,36)` negative control;
- Einstein-Hilbert reference control;
- `R^2` higher-derivative sensitivity;
- axis-label duplicate;
- off-shell lock;
- source lock.

The Critic independently passes those controls plus `constructor_not_imported=true` and `fixed_parent_ray_no_refit=true`.

Critic classification:

`PASS_INDEPENDENT_CRITIC_RCG003B_SCOPE_AND_PROVENANCE`.

## Canonical terminal classification

**`FAIL_SCOPED_RCG003B_AXISYMMETRIC_HIGHER_DERIVATIVE_SURVIVOR_FALSIFIED`**

Because the acceleration Hessian is already nonzero, the frozen velocity-curl criterion is not a rescue mechanism and is not applicable to the PASS path.

## Dimension accounting

Only inside the frozen combined scope:

- raw RCG003-v0 cubic-Ricci coefficient dimension: `3`;
- after conformal derivative-order closure: `1` nonzero ray;
- after RCG003B axisymmetric derivative-order closure: **`0` nonzero rays**.

Thus the entire remaining nonzero survivor of `RCG003_MINIMAL_NONLINEAR_CUBIC_RICCI_FAMILY_V0` is scientifically falsified by the stronger held-out anisotropic derivative-order requirement.

## Interpretation

The earlier conformal cancellation is insufficient once anisotropy is allowed. The exact `(7,-36,36)` ray is therefore an **isotropic/conformal cancellation artifact with respect to this stronger derivative-order requirement**.

This does not imply that all cubic gravity, all higher-curvature gravity, or arbitrary nonlinear gravity fails. It does not select GR and is not a no-go theorem outside the frozen RCG003-v0 family.

The prior local preterminal reproduction is now only an independent reproduction comparison. It agrees with the canonical artifact on classification, exact Hessian, witness, determinant mechanism, controls and dimension reduction; the canonical artifact, not the local record, is authoritative.

## Programme boundary after FAIL

The external D3 authority states that it authorizes only a **prospectively controlled new-version formation attempt**. That authority was consumed by RCG003 formation. It does not automatically authorize a second new-version family after RCG003-v0 falsification.

Therefore no RCG004 coefficient family, operator basis, or survivor computation is authorized by this terminal alone. The next programme object must be a bounded prospective authority gate for a complete algebraic cubic-curvature extension; it must not choose coefficients or assert that the enlarged class succeeds.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
