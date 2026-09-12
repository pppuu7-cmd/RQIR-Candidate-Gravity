# Iter019B / G37-A terminal classification

Authoritative run `34704008252`, head `e0288f6e5dc58c43f71c790d5402bdb7bb9561c9`, aggregate job `103581352127`, summary artifact `10301497283`, digest `sha256:26926f7123ad1f69f4d13d17354c5e02a48a817cf6028f4850acc03a5422c0ee`.

All 8 numerical lanes were structurally valid and Sobol/LHS gaps agreed within the frozen `0.002` scale. The frozen aggregate nevertheless returned `scientific_support=false` because the parent-nesting check failed on shards 1 and 2:

- shard 1 combined best `0.10462230580284927` versus declared best parent `0.10036158741640057`;
- shard 2 combined best `0.4030776004122033` versus declared best parent `0.35873703839655824`.

Before promoting this aggregate as a physical result, code inspection established that the G37-C/G37-A 18-dimensional family was not actually a superset of the shared-noise parent: the K=2 measurement-feedback channel weights are normalized to sum to one, so its measurement-feedback component cannot be switched off. Therefore comparing the old combined-family minimum to the shared-noise-only parent under a nesting requirement was mathematically invalid as a family-containment test.

Classification: `PROTOCOL_DESIGN_FAIL / NONNESTED_COMBINED_FAMILY`.

This is not a scientific falsification of RCG-002 and is not evidence for or against the corrected combined comparator. The numerical outputs remain diagnostic only. No threshold was weakened and the old family was not rescued post hoc. A prospectively corrected family, G37-C2, adds an explicit `lambda_MF in [0,1]` so that `lambda_MF=0` contains shared-noise-only and `cA=cB=0` contains measurement-feedback-only; only that corrected family can support a nesting-based adversarial verdict.