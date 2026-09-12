# Iter024A / G41-P terminal result

- Run: `34710097236`
- Head: `e6c74225814d4627945d3edbeda9620e4e4a57c2`
- Aggregate job: `103597226535`
- Summary artifact: `10303101144`
- Digest: `sha256:a189c87f4cb786e3fd2f5324e3bb54e3813d55f7f7ac959ff263747b811c185f`
- Classification: `HIGH_RANK_CLASSICAL_KOSSAKOWSKI_IMPLEMENTATION_VALIDATED`

All 12 prospectively frozen implementation/admissibility lanes passed for Kossakowski ranks 4, 5 and 6. Across the run, the largest TP residual was `4.1597644481e-16`, the worst product-unitary factorization error was `2.2791605939e-16`, and maximum output negativity from the seeded product inputs was exactly `0.0`. Rank-4/5 minimum Kossakowski eigenvalues were numerical roundoff (`~-1e-17`); rank 6 minimum was positive (`0.079`). Choi minima were positive in all rank groups.

Scope: explicit classical shared Gaussian random-Hamiltonian noise on the six local Pauli generators, with finite ranks 4/5/6. This is implementation/provenance authority only. No RCG-002 target was used, and readiness is not increased by this result alone. It authorizes a separately calibrated optimizer subfamily before any adversarial use.
