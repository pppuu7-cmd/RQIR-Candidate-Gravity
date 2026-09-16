# RCG-003 — minimal nonlinear family / conformal derivative-closure terminal

Date: 2026-09-17
Status: **TERMINAL SCIENTIFIC RESULT IN FROZEN SCOPE**

## Provenance

Programme authority:
- D3 declaration commit: `464bbb6fd3c602a1fdc5194f0a6a03b8327fb7f4`;
- D3 terminal commit: `d9187a60d2e7545ae3f082762d4a747b9681b69f`;
- authority classification: `D3_AUTHORIZED_SCOPED_NEW_VERSION_FORMATION_ATTEMPT`.

Scientific preregistration:
- file: `prereg/RCG003_MINIMAL_NONLINEAR_VERSION_FORMATION_AND_CLOSURE_GATE.md`;
- commit: `0bba0ea6e1d4e13635f70f3b5056e131afba6c7d`;
- frozen blob: `b87bd703bd4c5b8e190c78100537bbcd45eb50ae`.

Implementation:
- constructor commit: `f7f9c2f9bf69c226f26601d7045513c2f410ba9e`;
- independent Critic commit: `68a726ef72a124fb4deba58e07b725635aa58d86`;
- aggregate commit: `48eafce9606252702686b2b88aaa0b126d216f88`;
- workflow/head commit: `9e710f12f0b1bc79d6e2bc6bc2a77fe81b9a8aa5`.

GitHub Actions:
- run: `35152559990`;
- overall conclusion: `success`;
- constructor artifact: `10469790962`, digest `sha256:ac50a966dbcfbd51342b18be353d1724badb78f31c7812144c91128417a22c12`;
- Critic artifact: `10469348848`, digest `sha256:65ebf79c5e30996a89dcaeb346df19a6d36ff971da1b5a22780708b2c831f5ac`;
- aggregate artifact: `10470035974`, digest `sha256:34fdedbc1734ee27227b3b96bc4d3b5a0f240e95709f169b91542a5e717cd9d1`.

Committed raw records:
- `results/raw/RCG003_CONFORMAL_CLOSURE_CONSTRUCTOR.json` at commit `e614826bdd20c63d48d1b79b6d3b1762a2743fb9`;
- `results/raw/RCG003_INDEPENDENT_CRITIC.json` at commit `3f8ee3d14c192ba5a042f518e9817900362672bf`;
- `results/raw/RCG003_TERMINAL_AGGREGATE.json` at commit `fbfc82a8988ed2b0dd66fee133a8e9d2f3d3b72a`.

## Frozen RCG003-v0 family

The deformation sector was frozen before production evaluation as

`lambda R^3 + mu R R_{mu nu}R^{mu nu} + nu R_mu^nu R_nu^rho R_rho^mu`,

inside a local 4D metric action. The Einstein-Hilbert term is only `REFERENCE / CONTROL`; it is not a derived RQIRCG result. The cubic deformation basis and its use as candidate dynamics are `NEW_MODEL_POSTULATE`.

Raw coefficient-space dimension: **3**.

The production source is exactly vacuum `T=0`. Matter coupling, observable map, full causal/hyperbolic closure, quantum state and measure are outside this gate and remain unresolved/unauthorized as frozen.

## Exact conformal reduction

For

`g_{mu nu}=exp(2 sigma(t)) eta_{mu nu}`,

with `x=(dot sigma)^2` and `y=ddot sigma`, the constructor independently recovered the frozen curvature identities and formed the `ddot sigma` Hessians of the three deformation densities.

After removing the common nonzero `exp(-2 sigma)` factor, the Hessian coefficient rows are exactly

`A = [[1296, 432, 180], [1296, 288, 36]]`

for coefficient order `(lambda,mu,nu)` and row monomials `(y,x)`.

Exact rational algebra gives:

- `rank(A)=2`;
- `nullity(A)=1`;
- raw dimension = `3`;
- residual dimension = `1`;
- rational null vector = `(7/36,-1,1)`;
- primitive integer direction = **`(7,-36,36)`**.

Thus the frozen conformal second-order lock removes two of three raw coefficient directions and leaves exactly one nonzero deformation direction inside RCG003-v0.

For interpretation only, substituting the primitive survivor into the already-derived reduced operator polynomials gives a deformation proportional to

`-216 x^3 + 648 x^2 y = -216 x^2 (x-3y)`,

which is linear in `y=ddot sigma`; therefore its `ddot sigma` Hessian vanishes identically in this conformal sector. This identity does not establish second-order dynamics on general metrics.

## Controls

Every prospectively frozen control passed:

- kinematic curvature identities;
- exact nullspace check;
- conserved-source control;
- broken-conservation-sign detection;
- rejection of an unregistered external source;
- rejection of a malformed non-density deformation;
- allowed point-field-redefinition duplicate preserves rank/nullity on both frozen panels;
- `+1` perturbation of a null-direction coefficient is detected by nonzero closure residual;
- Einstein-Hilbert reference has zero acceleration Hessian;
- `R^2` sensitivity control has nonzero acceleration Hessian.

No coefficient was fitted to obtain the survivor.

## Independent Critic

Terminal Critic classification:

`PASS_INDEPENDENT_CRITIC_RCG003_SCOPE_AND_PROVENANCE`.

The Critic independently reconstructed the compatibility matrix using exact centered second differences of the cubic reduced polynomials. It reproduced

- rank `2`;
- nullity `1`;
- primitive nullspace direction `(7,-36,36)`.

It also passed every chronology, historical-blob-integrity, anti-fit, successor-firewall, source, equivalence and claim-scope check. There were no Critic failures.

## Formation side classification

`RCG003_MINIMAL_NONLINEAR_FAMILY_FORMED_FOR_VACUUM_STRUCTURAL_TEST_SCOPED`.

All 22 required model-definition slots are explicitly classified for this gate. This means the new version is sufficiently defined to support the stated vacuum structural test; it does **not** mean a complete interacting candidate theory is formed.

## Terminal scientific classification

**`PASS_SCOPED_RCG003_CONFORMAL_SECOND_ORDER_NONZERO_DEFORMATION_EXISTS`**

This is an existence-and-rank-reduction result only:

`dim(raw)=3 -> rank(closure)=2 -> dim(residual)=1`.

It is not global uniqueness. It is not evidence that `(7,-36,36)` is the physical coefficient ray. It is not a derivation of GR/Einstein dynamics, not full constraint closure, not a hyperbolicity result, not source/matter closure, not a quantum theory and not a phenomenological success.

## What is now established

Inside the prospectively frozen local cubic-Ricci RCG003-v0 family, there exists exactly one coefficient direction modulo the frozen coefficient-coordinate/point-field-redefinition convention that survives the homogeneous conformal no-fourth-time-derivative condition.

The former historical statement that no new version had been authorized is no longer the programme front: D3 was explicitly consumed and RCG003-v0 was prospectively formed for this structural scope. Historical RCG-002 scientific terminals are unchanged.

## What remains unresolved

At minimum:

- whether the one-dimensional survivor also avoids higher-time-derivative equations on anisotropic/off-conformal metrics;
- full nonlinear constraint propagation and hyperbolicity;
- whether the surviving direction is redundant under broader derivative-dependent metric redefinitions, which are outside the frozen v0 quotient;
- carrier self-source realizability beyond action variation;
- matter coupling and matter/source conservation closure;
- observable map;
- quantum state and measure;
- any physical coefficient scale `ell`;
- any prediction.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
Theory established = **0%**.

## Highest-information next discriminator

Because only one coefficient direction remains, the next highest-information gate is not another family enumeration. It is a held-out anisotropic homogeneous derivative-closure test on the **fixed** survivor `(7,-36,36)`, with no refit.

The purpose is to determine whether the conformal PASS reflects a genuine structural degeneracy or only isotropic/conformal masking. The next gate must be prospectively frozen before any anisotropic outcome is computed.
