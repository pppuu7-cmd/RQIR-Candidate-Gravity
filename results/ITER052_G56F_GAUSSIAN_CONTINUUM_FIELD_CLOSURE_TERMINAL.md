# Iter052 / G56-F — terminal classification

Date: 2026-09-13

## Frozen outcome

Classification: `G56F_FROZEN_CONTINUUM_FIELD_CLOSURE_RULE_NOT_MET`.

This classification is preserved exactly as preregistered. Green CI is not scientific PASS and no threshold is changed after observing the result.

## Authority

- preregistration commit: `f27b25d290fae7e45f4584b5a66c902d33c0e568`
- implementation commit: `0b459d3a36826387194a25655d5014d397c039bc`
- production head: `fc8bed7571d88bf48a3cb168e71067185a5ad1e6`
- run: `34746540910`
- aggregate job: `103695482197`
- aggregate artifact: `10313798716`
- aggregate digest: `sha256:57de2f010d09a2f0d584f4238c98d98e0eb28261582515cbfbea7f03539a4b1b`

Aggregate consumed 6/6 results. All six lanes are structural-valid, but `all_lane_support=false`, therefore the frozen aggregate rule does not pass.

## Localization

The only observed frozen predicate failure is lane case 3, `u=r/s=2.0`, on the preregistered wrong-width (`1.3s`) negative control:

- required wrong-width relative difference: `>= 0.05`
- observed: `0.029913948838822833`
- `wrong_width_negative_control=false`

In the same lane, the source/kernel identities and numerical checks pass strongly:

- worst Cartesian Laplacian relative error: `1.0614870158684851e-09` (threshold `<=2e-5`)
- orientation scaled-Laplacian spread: `1.6777244871146735e-10` (threshold `<=2e-7`)
- Gauss-flux absolute error: `3.1327862526353556e-10` (threshold `<=2e-8`)
- source normalization absolute error: `0.0` (threshold `<=2e-10`)
- scale-collapse predicates: pass
- wrong-sign control: pass (`1.9999999995077784 >= 1.5`)

Across the aggregate, worst Cartesian Laplacian relative error is `2.6255427924608605e-08`; worst Gauss-flux error is `3.1327862526353556e-10`; all structural/source/kernel checks remain within frozen thresholds.

## Interpretation discipline

G56-F itself is a terminal frozen-rule FAIL and is not relabelled PASS. The observed failure is localized to a single-point negative-control discriminability blind spot, not to an observed violation of the Gaussian source/kernel identity. This distinction is diagnostic only and does not retroactively alter G56-F.

Readiness remains **66%**. Theory established remains **0%**.

Any follow-up must be separately preregistered. Diagnostics may determine whether the wrong-width control has an analytic crossing/blind region and independently test finite-difference/high-precision identity convergence, but they cannot rescue this frozen run. A future replacement production gate, if justified, must be prospectively defined after diagnostics with a non-degenerate control and must remain a new gate.

Scope lock: isotropic Gaussian weak-field RCG-002 source/kernel closure only. No generally covariant gravity theory, relativistic dynamics, quantum measure/path integral, complete-QG, all-classical, or all-semiclassical conclusion follows.