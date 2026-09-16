# RCG003B preterminal local reproduction — Actions provenance pending

Date: 2026-09-17
Status: **NONTERMINAL / DO NOT USE AS CANONICAL SCIENTIFIC TERMINAL**

## Why this record exists

The prospectively frozen RCG003B gate has been implemented without changing the science contract, but the canonical GitHub Actions run has remained queued without an assigned runner. This record preserves the independently reproduced exact mathematics while keeping CI/artifact provenance distinct from the terminal classification.

This file does **not** replace `results/RCG003B_*_TERMINAL.md`, does not create a second preregistration, and does not authorize a duplicate Actions run.

## Frozen authority

- Parent RCG003 terminal: `ded5a44078c57909aeb6592b88bdac5c0917f85d`.
- RCG003B preregistration: `dbb0b54465c628b533c646a5b3b74b8458eaf24e`.
- Production coefficient ray fixed exactly to `(7,-36,36)`.
- Production source fixed to `VACUUM_ZERO`.
- No refit, family enlargement, basis search, matter insertion, successor import, isotropy condition, EOM use, or special trajectory was introduced.

## Frozen implementation commits

- Constructor: `f7353512a31bdee081e63dc832a675ec16987121`.
- Independent Critic: `49ea8d43f1dbca0e5212a67314cba9d5226a087c`.
- Direct Euler–Lagrange cross-check final implementation: `b8dbe1c00fc7ad32444f682309526b3116ca9ede`.
- Frozen aggregate: `7989f4ace99d5efc6432f8ac41a7cb42eb0c98b0`.
- Workflow head: `241a923523b2c770ffc8c48315d931af6e61846f`.

## Canonical Actions run — not yet terminal

Run: `35156147876`.

Current state at this record: `queued`.

Queued job IDs:
- Constructor: `104995924624`;
- Euler cross-check: `104995924852`;
- independent Critic: `104995924979`.

No workflow artifact existed at the time of this record. Therefore the repository must not treat the local reproduction below as satisfying the requested Actions/artifact provenance layer.

Exact next infrastructure action: **consume this same run when it executes; do not launch a duplicate scientific run merely because it is queued.**

## Independent local exact reproduction

The frozen scripts were executed independently against workflow head identity `241a9235...` in the available local exact-symbolic environment (`Python 3.13.5`, `SymPy 1.14.0`). This is an additional reproduction layer only; the workflow itself pins Python 3.12 and SymPy 1.13.3.

All three local lanes agree on the candidate frozen classifier result:

`FAIL_SCOPED_RCG003B_AXISYMMETRIC_HIGHER_DERIVATIVE_SURVIVOR_FALSIFIED`

The aggregate check is locally `valid=true` and gives residual nonzero ray dimension `0` **inside the frozen combined RCG003-v0 derivative-order scope only**.

Because Actions provenance is still pending, this is recorded as a **preterminal candidate outcome**, not the canonical terminal result.

## Exact anisotropic acceleration Hessian

After factoring the common nonzero density factor `exp(a+2b)`, with

- `va = adot`,
- `vb = bdot`,
- `ua = addot`,
- `ub = bddot`,

the independently reproduced Hessian is

`H_aa = -48 (2 ua + ub + 2 va^2 + va vb)`

`H_ab = -48 (ua - 4 ub + va^2 + 2 va vb - 6 vb^2)`

`H_bb =  48 (4 ua - 7 ub + 4 va^2 + 5 va vb - 12 vb^2)`.

Hence the Hessian is not the zero polynomial on the independent off-shell anisotropic history space.

A compact additional mechanism diagnostic is

`det(H) = -20736 (ua - ub + va^2 + va vb - 2 vb^2)^2`,

after the same common density normalization. This determinant is descriptive; it is not a new classifier.

## Minimal exact obstruction witness

Constructor and independent Critic reproduce the same normalized witness:

- component: `H_aa`;
- monomial: `ub`;
- exact coefficient: `-48`;
- common density factor: `exp(a+2b)`.

The direct Euler–Lagrange route independently reproduces the equivalent highest-derivative witness:

- equation: `E_a`;
- highest derivative: `a''''` coefficient structure equals `H_aa`;
- monomial inside that coefficient: `ub`;
- exact coefficient: `-48`;
- common density factor: `exp(a+2b)`.

Thus the direct E-L route verifies the Hessian/fourth-derivative correspondence rather than merely trusting the Hessian theorem implementation.

## Controls reproduced locally

All frozen controls pass in both Constructor/Critic logic:

- isotropic recovery;
- perturbed ray `(8,-36,36)` negative control;
- Einstein–Hilbert reference control;
- `R^2` higher-derivative sensitivity control;
- axis-label duplicate control;
- off-shell lock;
- source lock `VACUUM_ZERO`;
- fixed parent ray / no-refit lock.

The isotropic recovery is important: the pullback Hessian along `a=b=sigma` vanishes exactly even though the full two-field anisotropic Hessian is nonzero. Therefore the locally reproduced mechanism is precisely **isotropic/conformal masking of an anisotropic higher-derivative obstruction**, not a failure to reproduce the parent conformal calculation.

## Local reproduction digests

File SHA256:
- Constructor JSON: `6dde19bcc1882bcfdb82f7e3ad3250d205f83806260519967b0f2f1004b455a7`;
- Critic JSON: `f7bcf26a2daf20e04b8f5c72e6e3066ad06e971920550dcacf0ecd537598c8a0`;
- Euler JSON: `45623521dcad31facd39be94c5601df9fe260bb2c49794da32ebdfeb8b9419c4`;
- aggregate JSON: `20fbaf4535fe32db379f64ab5d9f2296c51ee21022de0f97943efc9a444419fa`.

Scientific payload SHA256:
- Constructor: `0b2130aa0fc32b258950bcc3ff49c0aef473802a83626f364a10a86b2911ca66`;
- Critic: `a434eba93af032c85e7c3bc2fe23360577139766bde7acf870651bd6db6d70a1`;
- Euler: `8cad5bc6b1c1d48a7eaeffffaaff15596ca0e7286c5b614c4717db4aba72df16`;
- aggregate: `49e329cc8a6bfd2c3bac66f9c30dc68ace224dd2fa4561c6b4aeb05cc115cf17`.

Symbolic-expression SHA256:
- Constructor: `1aa5be6f7a8f5f6eaa1575790108bbbce1f008c2eae4d7b5d02731015a7db3d3`;
- Critic: `51699117a70ca1e0694f67c447befcdf55216164ad83b01bd7a0f51ec32f315a`;
- Euler: `8c9cd01db4cd4b6c9a173e9371fac62ee0ec1a37c69ab9ec9a7ab75d5a715b04`.

Different symbolic hashes are expected because the three lanes use different derivation routes; exact Hessian/witness agreement is the scientific cross-check.

## Interpretation lock

If the queued Actions run reproduces the same valid result, the frozen terminal dimension accounting is:

`1 -> 0`

for nonzero rays inside the intersection of:

1. the frozen RCG003-v0 cubic-Ricci family;
2. the conformal derivative-order requirement;
3. the axisymmetric Bianchi-I derivative-order requirement.

That would **not** be a no-go theorem for arbitrary nonlinear gravity and would not authorize coefficient refitting or automatic family enlargement.

No result here establishes GR, full constraint closure, hyperbolicity, stability, unitarity, matter completion, quantum gravity, experiment, or new physics.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
