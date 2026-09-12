# Iter023D / G40-RC-D2 terminal result

- Run: `34710444349`
- Head: `ccf4274e73414d665a5c0d7f3501957760384c37`
- Aggregate job: `103598231631`
- Summary artifact: `10303515884`
- Digest: `sha256:da1e87331e79a9f6883b3827ca80400f35e364a672eaba0f0826aec94ac5286c`
- Classification: `PERSISTENT_OPTIMIZER_OR_OBJECTIVE_GEOMETRY_NONROBUSTNESS`

Frozen deeper-search shard-3 diagnostic used four independent 64-start constructions, top-12 least-squares refinements, unchanged RTN family/witness/target, and selected each final winner by the scientific maximum trace-distance gap.

Best gaps:
- Sobol64: `0.7495354861300184` (BLP `0.5971393993763672`)
- LHS64: `0.7450136684572843` (BLP `1.4168603756641471`)
- Halton64: `0.7450127675883661` (BLP `1.4168419897654947`)
- random64: `0.7450127451288935` (BLP `1.4168468568911297`)

Four-method spread: `0.00452274100112493 > 0.002`. Diagnostic support is therefore false. Three constructions converge tightly near `0.745013`, while Sobol64 remains in a distinct admissible basin near `0.749535`. This does not authorize a repaired adversarial physics gate and does not change readiness. A future RTN attempt would require a separately calibrated optimization method aligned more directly with the scientific trace-distance metric rather than further post-hoc start inflation.
