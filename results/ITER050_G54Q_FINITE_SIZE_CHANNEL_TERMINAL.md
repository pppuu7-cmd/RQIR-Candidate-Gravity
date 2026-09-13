# Iter050 / G54-Q — finite-size controlled-phase channel integration

Date: 2026-09-13

## Terminal classification
`FINITE_SIZE_WEAK_FIELD_CONTROLLED_PHASE_CHANNEL_INTEGRATED_SCOPED`

## Authority
- Preregistration: `aa3efc459c43ccf9055b3d6ddf8fa32cc1ac06b0`
- Initial production head/run: `f38da18ae53026c422fd2f35bc5e1d9232a5aef8` / `34741756333`
- Initial run classification: `INFRASTRUCTURE/IMPLEMENTATION FAIL` before artifact publication because NumPy boolean scalars were not JSON serializable. No scientific classification is attached to that run.
- Serialization-only repair: `33efdabc9169d498eb90d32c1ebce3481df2df2e`
- Authoritative retry head/run: `d4f5b37ac0c00842aaf85344850ee99d46dacdff` / `34743980333`
- Aggregate job: `103688387613`
- Aggregate artifact: `10312897870`
- Aggregate digest: `sha256:554436be119b3a60cd7880b5cd2c6c5f70878afad91ac1ebfe8706df20b5d428`

## Frozen-rule result
All 8/8 raw lanes were consumed. All are structurally valid and all satisfy every frozen lane predicate. The frozen aggregate reports `scientific_support=true` and monotonic point-particle convergence.

Worst observed values:
- analytic-vs-Fourier kernel relative error: `4.223192517467175e-16`
- unitary factorization error: `2.710505431213761e-20`
- local-phase quotient absolute error: `7.01207755055e-17`
- A/B exchange relative error: `8.170269981347449e-16`
- TP residual: `2.220446049250313e-16`
- minimum Choi eigenvalue: `-8.86236951137628e-16` (inside the frozen `-1e-12` floor)
- high-ratio point-phase relative difference: `3.764201305131426e-15`

## Scientific scope
This establishes only the prospectively frozen finite weak-field isotropic-Gaussian controlled-phase channel integration. It is not a covariant continuum gravity theory, not a global theorem, and not experimental confirmation.

Per the preregistered roadmap rule, G54-Q does not independently raise programme readiness above 65%. `THEORY_ESTABLISHED` remains 0%.