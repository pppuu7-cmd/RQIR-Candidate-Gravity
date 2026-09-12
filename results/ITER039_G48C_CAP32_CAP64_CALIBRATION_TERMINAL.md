# Iter039 / G48-C terminal result — cap32/cap64 response-blind calibration

Date: 2026-09-13

## Authority

- Preregistration commit: `7899a0ab095f8256e25fbf976ad489eaf2db4db9`
- Implementation commit: `8e24f8cc9a7a5b534d1d432be1ab6ea5916ccdb9`
- Workflow commit: `e9c3605d5557bb391146d767dacb92cedeb840f0`
- Authoritative launch/head: `194db0cf51577a62080227a4f0ade3ed29f49a3a`
- Run: `34721391489`
- Aggregate job: `103628932444`
- Summary artifact: `10307000228`
- Artifact digest: `sha256:a31ba73467efeb83cb15c045f8928cc6e84c9dbf09a407e0052ac877b3a01ce9`

## Frozen gate

Response-blind positive-control calibration of the same basis-invariant real-PSD trace-ball optimizer at finite trace caps `{32,64}`, methods `{sobol_lsq,lhs_lsq}`, hidden effective ranks `1..6`, with the same hidden-control construction, optimizer settings and recovery/rank/PSD criteria inherited from the prospectively frozen G46-C calibration. The RCG-002 target was forbidden.

## Raw terminal result

All `24/24` lanes are structurally valid and satisfy their frozen scientific-support rule.

- cap32: `12/12` PASS; worst trajectory gap `2.8474088570401036e-11`; worst relative Kossakowski error `2.83680640607369e-10`; rank matches `12/12`.
- cap64: `12/12` PASS; worst trajectory gap `6.153799793735667e-10`; worst relative Kossakowski error `1.6423013282529114e-05`; rank matches `12/12`.

## Scientific classification

`CAP32_CAP64_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED`

This is a **calibration-only PASS**. It establishes that the frozen optimizer can recover target-free positive controls at caps 32 and 64 under the preregistered criteria. It does **not** establish comparator separation, an unbounded-PSD limit, a no-go theorem, or any candidate-gravity dynamics.

Readiness remains **63%**. Theory established remains **0%**.

## Next authorized dependent gate

A separately prospectively frozen cap32/cap64 adversarial transport against the existing RCG-002 toy target may now be implemented. It must retain the G46-A family, target convention, optimizer hyperparameters, nonzero-gap threshold, Sobol/LHS agreement tolerance `0.002`, and add explicit nesting checks against the already-terminal cap16 minima. Even a PASS remains finite-cap, scoped Markovian evidence only.