# ITER047 / G51-K — branchwise-retarded weak-field kernel audit (preregistration)

This protocol is frozen **before implementation and before production output**.

## Question

The early ITER003 microscopic proxy used a common delay `max(0,t-r_max/c)` multiplying the full four-branch geometric cross-difference. G51-K tests an independent branchwise-retarded weak-field kernel instead:

`k_BR(t) = sum_{ij} s_ij max(0,t-d_ij/c)/d_ij`, with signs `(+,-,-,+)`.

The common-delay proxy is

`k_common(t) = max(0,t-r_max/c) sum_{ij} s_ij/d_ij`.

This is a causality/kernel audit only. It does not fit RCG-002 data and does not use comparator outcomes.

## Frozen panel

Eight deterministic positive four-branch geometries, fixed in the implementation, spanning sub-metre to metre scales and all with nonzero geometric cross-difference.

For every geometry the following rules are frozen:

1. **Pre-lightcone null:** at `t = 0.5*min(d_ij)/c`, `|k_BR| <= 1e-18`.
2. **Post-all-branches identity:** at `t in {1.25, 2, 10}*r_max/c`, compare `k_BR(t)` with `t * sum s_ij/d_ij`. Relative discrepancy must be `<= 1e-12`.
3. **Shared-rmax proxy discrimination:** at `t=2*r_max/c`, the relative difference between `k_common` and `k_BR` must be `>= 0.1` for every nonnull frozen geometry.
4. **Exact geometry null control:** for `d00=d01=d10=d11`, branchwise and common kernels must both vanish to `<=1e-18` over the frozen time panel.
5. No post-hoc geometry, time, or threshold changes.

## Frozen classification

All 8 lanes structurally valid and satisfying rules 1–4:

`BRANCHWISE_RETARDED_KERNEL_VALIDATED_AND_SHARED_RMAX_CAUSAL_PROXY_REJECTED`

Otherwise:

`G51K_FROZEN_RULE_NOT_MET`

## Interpretation lock

A PASS would establish only that the branchwise-retarded weak-field toy kernel satisfies this finite causal-support panel and that the old common-`r_max` delay proxy is not equivalent to it near light-crossing times. It would **not** establish a covariant GR retarded Green-function derivation, a full continuum gravity dynamics, or new physics.

This audit alone cannot change programme readiness. Theory established remains 0%.
