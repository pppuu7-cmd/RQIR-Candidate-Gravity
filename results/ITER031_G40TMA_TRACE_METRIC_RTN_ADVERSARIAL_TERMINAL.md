# Iter031 / G40-TM-A terminal — trace-metric RTN adversarial gate

- Run: `34716863840`
- Aggregate job: `103616629784`
- Summary artifact: `10305770549`
- Summary digest: `sha256:7ece1af4ca748acc2a0597b1c5f900e58e805de2cfdf2d01a7f2cc6fed1d3a4b`
- Terminal classification: `G40TMA_FROZEN_SUPPORT_RULE_NOT_MET`

All eight lanes were structurally valid, strict-BLP admissible and individually produced nonzero gaps. However the prospectively frozen cross-method agreement requirement `|gap_Sobol-gap_LHS| <= 0.002` failed in all four shards:

- shard 0: gaps `0.584587750080894` vs `0.5645527888886369`, difference `0.020034961192257117`;
- shard 1: `0.5724941626871984` vs `0.5956234047396675`, difference `0.023129242052469023`;
- shard 2: `0.6202745310136775` vs `0.6254485196619471`, difference `0.005173988648269678`;
- shard 3: `0.7127958876013898` vs `0.7053745396559433`, difference `0.007421347945446466`.

Therefore prospective RTN comparator support is **not established**. This is not a universal physical FAIL of RTN, and it is not evidence that RTN reproduces or cannot reproduce RCG-002 generally. The failure is specifically the frozen method-robustness condition. No threshold weakening, post-hoc optimizer tuning, or rerun may retroactively convert this gate to PASS.
