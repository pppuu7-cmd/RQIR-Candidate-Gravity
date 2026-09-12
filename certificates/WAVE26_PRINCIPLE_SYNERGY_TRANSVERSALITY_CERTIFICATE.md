# Wave 26 — Principle Synergy / Transversality Certificate

Status: **CLOSED / CLEAN**

Authority run: `34663346633`
Authority compute commit: `3be1faae1edf18192e74621de15b466bcb63769b`
Preregistration commit: `98fdfb826ef18831d0c2797e0cf2bb8b4daeea7e`
Judge: `protocol/PARENT_LAW_ACCEPTANCE_PROTOCOL_V1.json`
Frozen exam: `holdouts/WAVE22_FROZEN_BANK.json`

## Result

All seven primary jobs and the fail-closed aggregator completed successfully. All eight preregistered signals were true.

### Conditional rank synergy

For the frozen rank-3 Ward proxy `W` and rank-`6-r` fixed-point constraint proxy `A_r`:

- canonical transverse `r=1`: combined rank 6, nullity 0;
- `r=2`: combined rank 6, nullity 0;
- `r=3`: combined rank 6, nullity 0;
- `r=4`: combined rank 5, nullity 1.

Across 500 seeded random orthogonal orientations per case, the rank-6 closure fractions were:

- `r=1`: 1.0;
- `r=2`: 1.0;
- `r=3`: 1.0;
- `r=4`: 0.0.

### Non-universality counterexamples

Valid aligned/redundant rank-`6-r` constraint spaces were also constructed:

- `r=1`: residual nullity 1;
- `r=2`: residual nullity 2;
- `r=3`: residual nullity 3.

Thus closure is generic in the finite random-orientation proxy for `r<=3`, but it is not guaranteed by the abstract principle labels. A model-specific same-realization transversality statement is required.

### Ward + positivity

The exact Ward nullspace intersected with the frozen positivity ellipsoid retained maximum frozen-bank prediction width `0.13078735519238505`, above the inherited `0.05` nonuniqueness threshold.

## Scientific verdict

Wave 26 establishes **conditional rank synergy**, not a unique known-principle parent law. The missing scientific object is now localized more sharply: a concrete same-realization microscopic-to-RQIR Jacobian/tangent map proving that UV/fixed-point constraints act transversely on the already-quotiented residual directions without double counting gauge/Ward consistency.

At principle-class level PL1 remains `BLOCKED_PENDING_SAME_REALIZATION_TRANSVERSALITY_MAP`. No known-principle combination tested here earns parent-law credit.

## Governance

Wave-22 holdouts and Parent-Law Acceptance Protocol v1 remain immutable. No KMQGB/polygon candidate equations or architecture were imported.
