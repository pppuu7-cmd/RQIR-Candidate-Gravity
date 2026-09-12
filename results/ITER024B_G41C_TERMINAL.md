# Iter024B / G41-C terminal result

- Run: `34710257380`
- Head: `2bac531b1c68d0fc735b8135b579662b1318fe52`
- Aggregate job: `103597956597`
- Summary artifact: `10302238984`
- Digest: `sha256:567a1994b5892050379509066bf5075f1190831658638a77eaa26d36ef62ee82`
- Classification: `HIGH_RANK_RATE_OPTIMIZER_CALIBRATED`

All 24 positive-control lanes passed for ranks 4/5/6 × four deterministic shards × Sobol/LHS. Worst recovery gaps were approximately:
- rank 4: Sobol `1.0749272927261676e-16`, LHS `1.1188630228279524e-16`;
- rank 5: Sobol `1.4980206190880005e-16`, LHS `1.5021942079557e-16`;
- rank 6: Sobol `1.5593224665824852e-16`, LHS `1.5765954885368582e-16`.

Frozen recovery tolerance was `<0.002`. This calibrates only positive-rate optimization on the deterministic G41-P rank-4/5/6 classical mode frames. It does not calibrate arbitrary mode orientations or arbitrary PSD 6x6 Kossakowski matrices. No RCG-002 target was used and readiness does not increase from this calibration alone. The result authorizes only the separately preregistered G41-A finite rate-family adversarial gate.
