# Compute Wave 19 — Cross-Order Closure Results

**Authoritative corrected run:** `34659576513`  
**Branch:** `cross-order-closure-wave19`  
**Commit:** `0f1659c3fff1cfa2d07cf77c2398e2402e81eb36`  
**Status:** 7/7 primary jobs + aggregator SUCCESS; all predeclared signals true.

The prior run `34659505867` is retained as a technical failure record. Correction `WAVE19_TECHNICAL_CORRECTION_001.md` changed only result serialization infrastructure.

## Ward cross-order rank

Reduced vertex basis: `L1,L2,L3,T1,T2,T3`.

- Ward rank = **3**.
- Vertex nullity after Ward = **3**.
- Ward-fixed longitudinal solution = `[0.582, -0.361, 0.14, 0, 0, 0]`.
- The nullspace is exactly the three preregistered transverse directions.
- Untouched finite-kinematic holdout sensitivity to that Ward nullspace = **0.7986864215698174**.

Thus Ward consistency links orders but does not derive the full physical 3-point vertex from the 2-point object.

## Soft-contact freedom

For `C(q)=c2 q^2+c3 q^3`, every tested deformation obeys `C(0)=0` and `C'(0)=0` while the finite-`q` holdout width at `q=0.65` is

**0.4045437500000001**.

Leading and first-subleading soft information therefore leave higher-derivative transverse contact freedom.

## Causality inequality

The preregistered positive-delay surrogate leaves

`c in [-0.95, 0.95]`,

width **1.9**, with finite-kinematic holdout width **0.6517**.

This is only an inequality-vs-uniqueness logic test, not a numerical CEMZ shockwave calculation.

## Explicit cross-order holdout

Two candidates use the identical Wave-18 two-point dressing:

- design `E(0.25)=0.9`;
- holdout `E(0.90)=0.6843417467591262`;
- identical Ward-longitudinal data `[0.51,-0.22,0.14]`;
- identical leading and first-subleading soft contact data.

They differ only by a physical cubic contact `c=±0.38` and predict finite 3-point holdouts

- `0.23300800000000005`;
- `0.626992`.

Width = **0.39398399999999995**.

## C5/EFT obstruction

A curvature-cubed degree-counting control starts at `O(h^3)` about the flat background. It can therefore alter a three-graviton interaction while leaving the leading quadratic/two-point kernel unchanged. This is the concrete C5-compatible cross-order obstruction.

## Strong selector control

A deliberately stronger product law using the same exponential two-point dressing predicts the reduced 3-point dressing with zero new vertex parameters. This demonstrates the strength a genuine closure law would need, but the product rule is an additional modeling postulate and is not RQIR-derived or C5-distinct.

## Authoritative verdict

`C5_EFT_cross_order_obstruction_present = true`

`frozen_Ward_soft_causality_uniquely_determine_three_point_from_two_point = false`

`restricted_product_law_demonstrates_required_selector_strength = true`

`restricted_product_law_is_derived_new_QG_primitive = false`

`candidate_new_QG_primitive_found = false`

The missing physics is now localized to an independently motivated cross-order dynamical closure principle.
