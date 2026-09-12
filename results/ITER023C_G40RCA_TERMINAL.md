# Iter023C / G40-RC-A terminal result

- Run: `34710216045`
- Head: `3e31a9faa8b05a9bf5d6971a4ca4d94e6386b633`
- Aggregate job: `103597733387`
- Summary artifact: `10302543565`
- Digest: `sha256:c86ad2349bd28c0ad7d031c34f4bed38ee4a4a3681d5c6b14199b80ae9db4f73`
- Classification: `G40RCA_FROZEN_SUPPORT_RULE_NOT_MET`

All eight lanes were structurally valid under the separately calibrated candidate-axis-frame covariant BLP witness/search rule.

Frozen shard results:
- shard 0: Sobol `0.6792484545959568`, LHS `0.6788240232951357`, difference `0.00042443130082114866` — support;
- shard 1: Sobol `0.7099207053256649`, LHS `0.7085507786775377`, difference `0.0013699266481271843` — support;
- shard 2: Sobol `0.6316999324090761`, LHS `0.6316992625732599`, difference `6.698358161472129e-07` — support;
- shard 3: Sobol `0.7472831704713611`, LHS `0.7495355611279814`, difference `0.0022523906566203067 > 0.002` — frozen agreement failure.

Both shard-3 candidates were strongly BLP-admissible (`~1.17953` and `~0.59713`), so the remaining failure is optimizer/objective robustness rather than witness eligibility. The run remains terminal FAIL/INCONCLUSIVE for scientific support; no threshold is changed and no readiness increase follows.
