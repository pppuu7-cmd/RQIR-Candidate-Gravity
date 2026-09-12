# Iter024C / G41-A terminal result

- Run: `34710491309`
- Head: `766ea13802d62e75fd988ec79f55f6b251296d9c`
- Aggregate job: `103598462910`
- Summary artifact: `10303600848`
- Digest: `sha256:fe89d973dc1f24fe50fba09542e1b1b8e1d1fbae5e9cb1f33165b7213764dea7`
- Classification: `DERIVED_SCOPED_HIGH_RANK_RATE_COMPARATOR_SUPPORT`

All 24 lanes were structurally valid and all 12 `(rank, shard)` Sobol/LHS cells passed the frozen nonzero-gap and cross-method agreement rules. Best gaps by rank/shard ranged from about `0.08004` to `0.90799`; method differences were between exactly zero and about `5.2e-9`, all far below the frozen `0.002` tolerance.

Representative cells:
- rank4/shard0: `0.08003986038849543` vs `0.08003986038849557`;
- rank4/shard3: `0.9079915874060674` vs `0.9079915874060678`;
- rank5/shard2: `0.5539264464370438` vs `0.5539264413261396`;
- rank6/shard2: `0.5346770071399816` vs `0.5346770123225483`.

Scope ceiling: this is evidence only against the finite frame-indexed positive-rate rank-4/5/6 classical random-Hamiltonian families calibrated by G41-C. It does not test arbitrary mode orientations or the full real-PSD 6x6 Kossakowski family and cannot support an all-classical/no-go or full quantum-gravity claim.

Programme accounting: this closes a new stable adversarial comparator layer and supports the internal readiness update `59% -> 60%`. Theory established remains `0%`; readiness is a programme-completion metric, not a probability of physical correctness.
