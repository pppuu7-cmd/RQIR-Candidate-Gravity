# Iter053 / G56-D — terminal diagnostics

Date: 2026-09-13

## Terminal diagnosis

`NEGATIVE_CONTROL_LOCAL_BLIND_SPOT_WITH_INDEPENDENT_IDENTITY_SUPPORT`

This is a diagnostic label only. It does **not** relabel or rescue Iter052 / G56-F, whose frozen terminal classification remains `G56F_FROZEN_CONTINUUM_FIELD_CLOSURE_RULE_NOT_MET`.

Programme readiness remains **66%**. Theory established remains **0%**.

## Authority

- preregistration: `325b4a44328c9f00b9a1a6643cdf79c47e90b22b`
- implementation: `b8e1498b8ee08b351a06780558a9212792331466`
- production head: `fa9c90366b10970e55d18277caf0e16edca96d31`
- run: `34748468285`
- D1 job: `103700644293`; artifact `10315435658`; digest `sha256:5f78d99b6a756bb6e31596bd253230f7208261720cdae611b2f10cdec12daf2d`
- D2 job: `103700643877`; artifact `10314752825`; digest `sha256:57de945788f9386e323bd2028986e8f627ae7696bc3e083020cef1095bbfb747`
- D3 job: `103700643726`; artifact `10315460569`; digest `sha256:dedcbb09a5a1344edbee6b024ece40fd49983e98fb236a01ed9a1d998b912e9f`
- aggregate job: `103700722982`; artifact `10314747849`; digest `sha256:f5590714a7179159e20a2fb3ec204f87e47e2c25768b049318fa067160615124`

All three streams are structural-valid and were consumed by the aggregate.

## D1 — finite-difference convergence

The original `h/s=0.01` numerical predicates reproduce on all six original lanes: `original_numeric_predicates_reproduced=true`.

The coarse-to-intermediate step sequence shows the expected approximately fourth-order behavior for the five-point stencils before round-off dominates the smallest Cartesian-Laplacian steps. The Gauss derivative remains approximately fourth order across the useful range.

Representative failed-G56F lane `u=2.0`:
- `h/s=0.04`: Laplacian rel. err `2.836534215321079e-07`, Gauss err `8.010522745127702e-08`;
- `0.02`: `1.7744037356797404e-08`, `5.011244308406049e-09`;
- `0.01`: `1.0614870158684851e-09`, `3.1327862526353556e-10`;
- `0.005`: `2.7450393220009546e-10`, `1.9583668020572986e-11`;
- `0.0025`: round-off starts increasing Cartesian error while Gauss remains `1.22379884004431e-12`.

This independently supports that the original identity numerics were not the source of the frozen failure.

## D2 — wrong-width discriminability

For the frozen wrong-width factor `q=1.3`, exact density equality occurs at

`u_cross = 1.9635717388164815`.

The connected interval in which the single-point relative density difference is below the old frozen 5% requirement is

`u in [1.899, 2.023]`.

The failed G56-F lane `u=2.0` lies inside that interval and gives

`|rho_1.3s/rho_s - 1| = 0.029913948838822924`,

reproducing the terminal G56-F value. Therefore `case3_blind_spot_confirmed=true`.

The dimensionless radial profile L1 separation over `u in [0,8]` is `0.4772096540261944`, showing that the two normalized source profiles are globally well separated even though they nearly cross at the single old control point.

## D3 — 80-digit held-out identity certificate

Seven new held-out `(u,s)` pairs were evaluated with 80-decimal-digit arbitrary-precision differentiation, independently of the G56-F double-precision finite-difference implementation.

- maximum Laplacian relative error: `2.76121848733739194017909059486e-78`;
- maximum Gauss-flux absolute error: `1.05421979432305232243485740513e-81`;
- `high_precision_identity_support=true`.

## Interpretation

The evidence supports a specific protocol diagnosis: the old wrong-width control was a single-point discriminator with an accidental crossing/blind interval, while the source/kernel identities themselves remain independently supported. This does not change the historical G56-F FAIL.

A replacement field-closure gate, if run, must be a new prospectively preregistered experiment with a global/non-degenerate width control and held-out numerical panel. It must not weaken or edit the original G56-F thresholds or classification.

Scope lock: RCG-002 isotropic Gaussian weak-field source/kernel mathematics only; no covariant gravity theory, relativistic field dynamics, quantum measure/path integral, full-QG or broad no-go conclusion.