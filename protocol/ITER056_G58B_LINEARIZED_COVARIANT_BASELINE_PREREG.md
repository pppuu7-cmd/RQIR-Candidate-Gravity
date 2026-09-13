# Iter056 / G58-B — linearized covariant baseline embedding audit

Date frozen: 2026-09-13
Status: **FROZEN BEFORE IMPLEMENTATION/PRODUCTION**

## Objective
Test the hypothesis-only object `candidates/RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md` as the minimum linearized spin-2 embedding of the existing RCG-002 weak-field branch.

This gate has two deliberately separate questions:

1. Is the proposed linearized field/source/gauge/retarded structure internally consistent on frozen tests and does it reduce to the validated Gaussian weak-field branch?
2. Is the already validated weak-field RCG-002 interaction *indistinguishable from the standard linearized spin-2 tree/static baseline at this order*?

A positive answer to question 2 is a **negative result for novelty at this order**, not a failure of mathematical consistency and not evidence for new physics.

Programme readiness is frozen at **66%** for G58-B. Theory established remains **0%**. This gate cannot establish nonlinear general covariance, full GR, interacting quantum gravity, a gravitational path-integral measure, or full QG.

## Frozen conventions
Metric signature `eta = diag(-1,+1,+1,+1)`.

`g_mu_nu = eta_mu_nu + h_mu_nu`, `|h| << 1`.

`bar h_mu_nu = h_mu_nu - (1/2) eta_mu_nu h`.

Linearized gauge law:
`delta h_mu_nu = partial_mu xi_nu + partial_nu xi_mu`.

de Donder condition:
`partial^mu bar h_mu_nu = 0`.

Source conservation:
`partial_mu T^mu_nu = 0`.

Field equation:
`Box bar h_mu_nu = -(16*pi*G/c^4) T_mu_nu`.

Static potential identification:
`Phi = -(c^2/4) bar h_00`, giving `nabla^2 Phi = 4*pi*G rho`.

Spin-2 de Donder numerator:
`P_mu_nu_alpha_beta = 1/2(eta_mu_alpha eta_nu_beta + eta_mu_beta eta_nu_alpha - eta_mu_nu eta_alpha_beta)`.

Linearized coupling normalization for the baseline audit:
`kappa^2 = 32*pi*G/c^4`, vertex magnitude `kappa T^mu_nu/2`.

## Stream A — conservation, gauge curvature, linearized Bianchi
Use 12 deterministic non-collinear static Fourier wavevectors `k=(0,qx,qy,qz)`. Construct deterministic symmetric sources projected so that `k_mu T^mu_nu=0` to machine precision.

For each lane require:
- conservation residual / source norm `<=2e-13`;
- de Donder response residual / response norm `<=2e-13` for `bar h proportional T/q^2`;
- linearized Riemann tensor is invariant under a deterministic gauge perturbation `delta h_mu_nu=k_mu xi_nu+k_nu xi_mu`, relative max error `<=2e-12` or absolute `<=2e-12` when the reference component scale is tiny;
- contracted linearized Bianchi residual `|k^mu G^L_mu_nu|/max(||G^L||,1) <=2e-12` for an independent deterministic symmetric test field;
- all values finite.

All 12 lanes must pass.

## Stream B — static Gaussian field reduction
Use new held-out ratios
`u=[0.31,0.63,1.08,1.66,2.31,3.14,4.02,5.11]`
and widths
`s=[0.094,0.143,0.211,0.287,0.359,0.449,0.557,0.673]`.

For unit mass and physical G,c, set
`Phi_s(r)=-G erf[r/(sqrt(2)s)]/r`
and `bar h_00=-4 Phi/c^2`.

With five-point Cartesian Laplacians at `h=0.01s`, require all eight lanes:
- `laplacian Phi = 4*pi*G rho_s` relative error `<=2e-5`;
- `laplacian bar h_00 = -16*pi*G rho_s/c^2` relative error `<=2e-5`;
- `Phi + c^2 bar h_00/4` absolute error normalized by `max(|Phi|,G/s)` `<=2e-13`;
- field/source finite and source positive.

This stream is a new field-equation embedding check, not a repeat classification of G56-F2.

## Stream C — retarded support versus advanced control
Freeze compact-support source pulse
`S(t)=sin^2(pi t/T)` for `0<t<T`, otherwise `0`, with `T=1` and `c=1` in dimensionless diagnostic units.

For radii `r=[0.2,0.35,0.5,0.8,1.1,1.4]`, evaluate the retarded profile `S(t-r)/r` at a frozen grid containing pre-arrival and post-arrival times. Require:
- all pre-arrival retarded samples `t<r` are exactly zero within `1e-14`;
- at least one post-arrival sample per radius is positive;
- an intentionally advanced control `S(t+r)/r` is nonzero for at least one pre-arrival sample in at least 5/6 radii;
- retarded result depends only on retarded time in the implemented formula and all values are finite.

This is a linearized support/causality diagnostic only, not a proof of nonlinear microcausality.

## Stream D — standard spin-2 tree/static baseline equivalence
For 10 frozen positive `(m1,m2,q)` triples, calculate the nonrelativistic exchange coefficient using
`(kappa^2/4) * P_0000 * (m1 c^2)(m2 c^2) / q^2`, with `P_0000=1/2` and `kappa^2=32*pi*G/c^4`.

Require the coefficient before `1/q^2` to equal `4*pi*G*m1*m2` with relative error `<=2e-14` in every lane.

Then for held-out Gaussian effective widths and separations, independently Fourier-transform
`-4*pi*G*m1*m2 exp(-s^2 q^2/2)/q^2`
and compare to
`-G*m1*m2 erf[R/(sqrt(2)s)]/R`.
Require relative agreement `<=2e-10` in all 10 lanes.

If all predicates pass, freeze the interpretation:
`RCG002_WEAK_FIELD_BRANCH_BASELINE_EQUIVALENT_TO_LINEARIZED_SPIN2_AT_STATIC_TREE_ORDER`.
This means the currently validated weak-field phase/kernel is not by itself a new-physics discriminator.

## Stream E — coupling limits diagnostic
For 8 frozen positive actions built from held-out masses, distances and times, evaluate the controlled phase quotient at coupling scale multipliers
`lambda_G=[1,0.5,0.1,0.01,0]` with `G -> lambda_G G`.
Require:
- phase quotient linearity in `lambda_G` relative error `<=2e-13` for nonzero multipliers;
- exactly zero interaction phase at `lambda_G=0` within `1e-14` absolute;
- operational unitary tends to identity as `G->0` on the frozen sequence.

Separately evaluate `|chi|` under `hbar -> lambda_h hbar`, `lambda_h=[1,0.5,0.25,0.125]` at fixed classical action. Require the numerical scaling `|chi| proportional 1/lambda_h` within `2e-13`. This is **not** a classical-limit PASS. If observed, record
`HBAR_ZERO_POINTWISE_PHASE_LIMIT_NOT_AVAILABLE_FROM_CHANNEL_ALONE`.

## Aggregate rule
Exactly five structural-valid stream artifacts A–E are required.

Internal consistency support requires A, B, C and E-G-zero predicates all pass.

Baseline-equivalence support requires all D predicates pass.

If both are true, aggregate classification:
`LINEARIZED_COVARIANT_BASELINE_EMBEDDING_SUPPORTED_AND_WEAK_FIELD_NOVELTY_NOT_ESTABLISHED`.

If the mathematical consistency predicates fail under valid implementation:
`G58B_LINEARIZED_BASELINE_CONSISTENCY_RULE_NOT_MET`.

If consistency passes but D does not establish equivalence:
`G58B_BASELINE_EQUIVALENCE_NOT_ESTABLISHED`.

Technical/runtime/serialization errors are not scientific FAIL and may receive only implementation-only repair without changing any frozen science rule.

## Interpretation/readiness lock
G58-B cannot raise programme readiness above 66% and cannot raise theory-established above 0%. Even a full PASS supplies only a linearized baseline embedding and a novelty-location result.

If baseline equivalence is established, future theory construction must place any claimed new physics in an explicitly defined `Delta Gamma` or equivalent structure beyond the standard linearized spin-2 static/tree baseline. No such deformation may be chosen post hoc inside G58-B.