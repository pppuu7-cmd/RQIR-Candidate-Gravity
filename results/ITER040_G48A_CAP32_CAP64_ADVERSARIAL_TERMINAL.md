# Iter040 / G48-A terminal result

Scientific classification: `DERIVED_SCOPED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP32_CAP64`.

Authoritative run: `34724106251` at head `235e807fbb9f5bf00de42e66a5aa07df90a21116`.
Aggregate job: `103636108319`.
Summary artifact: `10307232484`.
Artifact digest: `sha256:4e58ab8c40a07546e47ea48eec5ffec8ec265e7216869c94702eda0eb50cd5b8`.

Frozen gate: caps `{32,64}` x methods `{sobol_lsq,lhs_lsq}` x four RCG-002 shards = 16 lanes. Same target/family/optimizer/admissibility thresholds as G46-A; cross-method agreement <= `0.002`; cap32 nesting versus terminal cap16 and cap64 nesting versus cap32 within `0.002`.

Result: 16/16 structurally valid. All eight method-pairs support the frozen nonzero-gap rule. Cross-method differences range from `1.64e-08` to `3.70e-07`, far inside the frozen `0.002` tolerance. All four cap32-vs-cap16 and all four cap64-vs-cap32 nesting checks pass. Best gaps remain nonzero on every shard: cap32 approximately `[0.037007956, 0.146328573, 0.527549443, 0.666386391]`; cap64 approximately `[0.037007967, 0.146328131, 0.527549490, 0.666386335]`.

Scientific scope: this is finite-cap, basis-invariant real-PSD Markovian comparator support on the frozen RCG-002 toy trajectory panel only. It does not establish an unbounded-PSD limit and is not an all-classical/all-semiclassical no-go theorem. Readiness remains 63% because this deepens the already-counted Markovian-PSD robustness rubric rather than closing a new programme rubric.

Next admissible direction: do not extend caps mechanically. Prospectively test a cap-free/direct-PSD parameterization with explicit coordinate-bound inactivity and response-blind calibration before any RCG-002 production transport; independently continue broader finite hidden-memory and external holdout layers when source-faithful objects are available.
