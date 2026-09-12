# ITER029 / G40-TM-C — terminal trace-metric RTN optimizer calibration

Run: `34716161178`
Head: `aff54cae0954eb06771337ab315672a049450923`
Aggregate job: `103614850103`
Summary artifact: `10305010398`
Summary digest: `sha256:1578827bf3cdc8a441eda3ed54bf4d5a9db51a69ebbf903f90420676c79c8ad5`

## Frozen result

All 8 response-blind positive-control lanes passed the preregistered scientific rule: direct optimization of maximum trace-distance trajectory gap recovered strict axis-covariant-BLP RTN controls with gap `<0.002` and BLP `>0.02`.

Per control shard, the two independent designs produced:

- shard 0 gaps `5.14579397690643e-07`, `5.604191780162829e-07`; cross-method difference `4.583978032563995e-08`; minimum recovered BLP `1.44397840803744`.
- shard 1 gaps `1.1471567720610074e-06`, `5.049937285663751e-06`; difference `3.902780513602744e-06`; minimum BLP `0.8471408689985623`.
- shard 2 gaps `2.2304845879978284e-05`, `6.549630042085553e-07`; difference `2.1649882875769727e-05`; minimum BLP `1.9828388138332529`.
- shard 3 gaps `1.5141031505223785e-07`, `3.1775278598088463e-07`; difference `1.6634247092864677e-07`; minimum BLP `1.2483830837470578`.

Terminal classification:

`TRACE_METRIC_ALIGNED_RTN_OPTIMIZER_CALIBRATED`

## Interpretation lock

This is optimizer calibration only. It does not alter historical G40-RC-A / G40-RC-D2 terminal results and does not raise programme readiness.

PASS authorizes the separately preregistered Iter031 / G40-TM-A prospective RTN adversarial gate using the identical RTN family, bounds, axis-covariant BLP witness, direct max-trace objective and frozen RCG-002 toy target shards. Any G40-TM-A conclusion remains finite-family scoped.
