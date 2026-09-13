# Iter063 / G65 — full conserved-source projector audit

Date: 2026-09-13

## Terminal classification
`FOUR_DERIVATIVE_LINEARIZED_FULL_CONSERVED_SOURCE_PROJECTOR_DECOMPOSITION_SCOPED`

## Frozen authority
- Initial preregistration: `dca4bd77c2fac5850f4d012c05b00fee34ccfea9`
- Pre-implementation Minkowski-covariant correction: `56a04b8823a11eb551ea9ded4444c320edd224a8`
- Implementation: `ecad1751103e5fa9b5b09f309688f52be189a610`
- Production/workflow head: `5cac0018f39a9c6fc001e937fc763da15e421a7c`
- Run: `34770109680`
- Aggregate job/artifact: `103758047952 / 10321651327`
- Aggregate digest: `sha256:8644579d8835b8cac803ec74015a3ff39515397968078a9a1432ff68d02fab5c`

Raw lanes:
- A `103758027280 / 10321836874`, digest `sha256:fb06edb695dae8afbd0bffb1340b6d242989cbdbaad79efabbf6e9a97a690ba3`
- B `103758027346 / 10321567477`, digest `sha256:0bc3f3fb89f1f441e4bc599db9b98f0664b615a1b5d5cfada2c12e241f7ef411`
- C `103758027306 / 10321787046`, digest `sha256:bb14ac7df3e67ea9b6f845b4ae8b15623f71be5b1c6cfdc826089b171ecd710c`
- D `103758027204 / 10320779979`, digest `sha256:67e1fafa454f9d245a3237051bb6b6a576adf9bb6e1c7e07993c8e4a4e98927f`

## Raw scientific result
- A: for all three frozen non-null Minkowski covectors, exact projector algebra passes with ranks `rank(P2)=5`, `rank(P0)=1`, `rank(P2+P0)=6`, exact idempotence, orthogonality and transversality.
- B: 576 exact held-out reconstruction/response checks pass with no fitting or retuning.
- C: 82 exact discrete-Lorentz covariance checks pass.
- D: all preregistered false-positive controls are detected: nonconserved source, malformed `P0`, omitted scalar sector and omitted spin-2 sector.
- Aggregate classifies A/B/C/D all PASS.

## Scientific interpretation
The G61–G64 algebraic two-sector structure is not an artifact of choosing one TT and one scalar representative: within the frozen 4D Minkowski linearized local four-derivative class, the exact conserved symmetric-source space decomposes into the rank-5 transverse traceless and rank-1 transverse scalar projectors, and the frozen sector response reconstructs the full conserved-source response.

This remains a linearized conserved-source statement only. It does **not** establish a physical ghost, instability, quantum-unitarity failure, nonlinear inconsistency, coefficient choice or global higher-derivative no-go theorem.

Programme readiness remains **66%**. Theory established remains **0%**.
