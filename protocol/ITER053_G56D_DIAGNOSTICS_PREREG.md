# Iter053 / G56-D — post-terminal G56-F diagnostics preregistration

Date frozen: 2026-09-13
Status: **FROZEN AFTER G56-F TERMINAL CLASSIFICATION, BEFORE DIAGNOSTIC IMPLEMENTATION/PRODUCTION**

## Non-rescue contract
Iter052 / G56-F remains terminal `G56F_FROZEN_CONTINUUM_FIELD_CLOSURE_RULE_NOT_MET`. These diagnostics cannot relabel, repair, rescore, or rescue G56-F and cannot change any Iter052 threshold, lane, source/kernel formula, or classification.

The sole purpose is to localize why the preregistered wrong-width negative control failed at `u=r/s=2.0` while the source/kernel identity metrics passed, and to decide what a future *new* prospective gate would need to test.

No readiness point can be earned by G56-D. Programme readiness is frozen at 66%; theory established remains 0%.

## Stream D1 — finite-difference convergence localization
Use exactly the six Iter052 `(u,s)` pairs and the same three Cartesian orientations. Recompute independent five-point Cartesian Laplacians and five-point radial Gauss derivatives at frozen dimensionless steps

`h/s = [0.04, 0.02, 0.01, 0.005, 0.0025]`.

Report, for every lane and step:
- worst Cartesian relative error against `-4*pi*rho_s`;
- orientation spread in `s^3 laplacian K_s`;
- Gauss-flux absolute error;
- empirical base-2 convergence orders between adjacent steps when finite/nonzero.

Diagnostic marker `original_numeric_predicates_reproduced=true` requires all six lanes at `h/s=0.01` to reproduce the original numerical predicates: Laplacian relative error `<=2e-5`, orientation spread `<=2e-7`, Gauss-flux error `<=2e-8`. This marker is diagnostic only.

## Stream D2 — wrong-width control discriminability
Freeze width factor `q=1.3`. For dimensionless `u`, evaluate the exact source-density ratio

`R_q(u)=rho_{q s}(u s)/rho_s(u s)=q^-3 exp[0.5 u^2 (1-q^-2)]`.

On frozen grid `u=0.10..6.00` inclusive with spacing `0.001`, report `|R_q-1|`, the analytic equality crossing

`u_cross = sqrt(6 ln(q)/(1-q^-2))`,

and the connected grid interval containing that crossing where `|R_q-1|<0.05`.

Diagnostic marker `case3_blind_spot_confirmed=true` requires the frozen Iter052 point `u=2.0` to lie in that `<0.05` interval and its exact relative difference to reproduce `0.029913948838822833` within `1e-12` absolute error. This does not alter the Iter052 threshold.

Also report the dimensionless radial L1 separation

`Integral_0^8 4*pi*u^2*|rho_1(u)-rho_q(u)| du`

for future control design only; no threshold is attached to it.

## Stream D3 — high-precision identity certificate
Use 80-decimal-digit `mpmath` differentiation, independent of the Iter052 double-precision finite-difference implementation, on frozen held-out ratios

`u=[0.23,0.51,0.93,1.57,2.41,3.73,5.20]`

paired with

`s=[0.083,0.137,0.191,0.283,0.367,0.457,0.613]`.

For each point compute `K_s(r)`, first and second radial derivatives by arbitrary-precision numerical differentiation, radial Laplacian `K''+2K'/r`, and Gauss flux `-r^2 K'`. Compare against `-4*pi*rho_s` and the analytic enclosed-source fraction.

Diagnostic marker `high_precision_identity_support=true` requires maximum relative Laplacian error `<1e-40` and maximum absolute Gauss-flux error `<1e-40` across all seven held-out points.

## Aggregate diagnostic interpretation
Exactly three structural-valid stream artifacts are required. If D1 reproduces the original numeric predicates, D2 confirms the local control blind spot, and D3 supports the identities at high precision, aggregate diagnosis is

`NEGATIVE_CONTROL_LOCAL_BLIND_SPOT_WITH_INDEPENDENT_IDENTITY_SUPPORT`.

Otherwise aggregate diagnosis is

`MIXED_G56F_FAILURE_DIAGNOSTIC_REQUIRES_FURTHER_LOCALIZATION`.

Neither label is scientific PASS for G56-F or for a gravity theory. No dependent constitution/covariance claim may be made from this diagnostic alone. Any replacement field-closure gate must be separately preregistered after these terminal diagnostics and must use a prospectively non-degenerate control rather than post-hoc relaxation of the old one.

Scope lock: RCG-002 isotropic Gaussian weak-field source/kernel mathematics only; no imported QGR/KMQGB/RQIR physics or desired conclusion.