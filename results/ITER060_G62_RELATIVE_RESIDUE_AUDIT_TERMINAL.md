# Iter060 / G62 terminal result — relative-residue algebraic audit

Date: 2026-09-13

## Frozen gate
`ITER060_G62_RELATIVE_RESIDUE_ALGEBRAIC_AUDIT`

Preregistration: `10fbc58c547e7baea13094025177a6fa459037d5`
Implementation: `b4999df69ca913b4045fcb3e25522331bd709cee`
Production head: `7e8baad8b6055b0546363682c56d786a6138e90e`
Authoritative run: `34761167760`
Aggregate job/artifact: `103734184486 / 10319241003`
Aggregate digest: `sha256:cc40a09a46f3791672b857e5559acac0f601bd3200781d3db75ab9cf847efdfa`

Raw lanes consumed:
- A job/artifact `103734145769 / 10318788758`, digest `sha256:aef5c242cd95b74d49219badf6786e875dfe9cb07290643d4d4db0a606c08e31`
- B `103734145831 / 10318524473`, digest `sha256:0d4b5964e09757e56f531fbf4b8ee2c0c3c22b5f24a6a4d886ab2589dcf31017`
- C `103734145812 / 10318883090`, digest `sha256:4011b9ed8a153452405d195611ced54b97c475c1705e9985f726aeac557dc106`
- D `103734145853 / 10319400418`, digest `sha256:c9c1a85be2dae99362cf40a522ceb39d3d4a2ae92e50b84a31b099832620ecba`

## Raw results
- A: exact TT residues `(-1/2,+1/2)` and scalar residues `(+1/6,-1/6)`; valid/pass.
- B: 12 frozen non-exceptional rational rays; both sectors have exact residue ratio `-1` whenever the additional simple root exists.
- C: 144/144 quotient/basis covariance checks pass.
- D: 24 non-exceptional held-out cases; 96/96 scale checks pass; TT and scalar exceptional-line controls pass; deliberately wrong same-sign residue control rejected 24/24.

## Scientific classification
`FOUR_DERIVATIVE_LINEARIZED_SECTOR_RELATIVE_RESIDUE_OPPOSITION_SCOPED`

This establishes only an exact algebraic relative-residue opposition for the two frozen conserved-sector representatives of the candidate-independent local four-derivative linearized quotient. It does **not** establish a physical ghost, unitarity violation, instability, or a global higher-derivative no-go theorem. It selects no coefficient ray.

Programme readiness remains **66%**. Theory established remains **0%**.
