# Wave 27 — Asymptotic-Safety Same-Realization Lineage Certificate

Status: **CLOSED / CLEAN**

Authority run: `34663711190`
Authority compute commit: `8d1a6e213d7884e204432bb929e9528b0267cc2f`
Frozen evidence commit: `476232a6c381d3aab81d0d76571578656676456a`

## Result

All seven primary lineage/integrity jobs and the fail-closed aggregator completed successfully. All preregistered scientific signals and the integrity firewall were true.

## Lineage completeness

The strongest frozen published lineage is `fluctuation_vertex` (F1+F2), supporting J0–J7 and therefore 8/10 required nodes. It lacks:

- J8 — explicit same-realization Jacobian/sensitivity map from independent UV trajectory coordinates to all six frozen RQIR residual directions `[c3,d3,e4,f4,s2,s0]`;
- J9 — propagated truncation/regulator/scheme uncertainty on those six outputs.

Other audited lineages are valuable but less complete:

- `lorentzian_spectral`: strong Lorentzian two-point/quadratic-curvature bridge, but no three/four-point closure and no J8/J9;
- `essential_C3`: genuine fixed-point/eigendirection/separatrix-to-one-Wilson-coefficient bridge, but not a six-direction map;
- `scattering_guard`: supports the anti-shortcut rule that fixed-point existence or naive RG improvement cannot substitute momentum-dependent observable calculations.

Even the cross-lineage union still lacks J8 and J9, and cross-lineage splicing is prohibited as same-realization evidence.

## C3 partial bridge

The two frozen regulator/prescription values for the dimensionless Goroff–Sagnotti coefficient are `0.0096` and `0.00000302`. Their ratio is `3178.8079470198672`. The positive sign is stable in the two audited treatments; the magnitude is not quantitatively scheme-closed.

## Frozen blocker

`BLOCKED_MISSING_SAME_REALIZATION_UV_TO_RQIR_SIX_DIRECTION_JACOBIAN_WITH_PROPAGATED_UNCERTAINTY`

## Cross-route metadata comparison

Only after freezing the independent Wave-27 verdict, KMQGB/main Iter209 metadata was compared. Its asymptotic-safety blocker is `STABLE_REPRODUCIBLE_SAME_REALIZATION_A4_PLUS_FULL_ERROR_COMPARATOR_CERTIFICATE`.

These blockers are not identical equations and do not authorize model-to-model convergence claims. They independently localize the missing evidence to the same class: a same-realization higher-point/observable mapping with explicit error propagation.

## Next target

Audit whether the F1+F2 fluctuation-vertex lineage exposes enough numerical trajectory/vertex data to construct J8 directly. If not, freeze an executable Jacobian derivation contract specifying exactly what new data must be published/computed instead of substituting another truncation.
