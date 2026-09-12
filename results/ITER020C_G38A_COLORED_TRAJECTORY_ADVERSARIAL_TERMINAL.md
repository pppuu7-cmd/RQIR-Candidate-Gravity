# Iter020C / G38-A terminal result

Authoritative run `34704373278`, workflow head `493da45d6a9b88e5cee32fca598fb657ea7a2ce4`, aggregate job `103581860728`, summary artifact `10301542445`, digest `sha256:ed9a0728c9288e696e6ed62fba176b848a46790c5ec7fe2faad9dbf04d26aa00`.

All 8 prospectively frozen adversarial lanes were structurally valid. For each of four RCG-002 toy-trajectory shards, both G38-C-calibrated methods retained `max_T` trace-distance gap above `1e-4`; Sobol/LHS per-time gap vectors and their maximum gaps agreed within the frozen `0.002` scale at `T=[0.25,0.5,1.0]`.

Maximum trajectory-gap pairs (Sobol-LSQ, LHS-LSQ):
- shard 0: `(0.025545074758564972, 0.0255450797621222)`;
- shard 1: `(0.10046306945014429, 0.1004630806848435)`;
- shard 2: `(0.35877357179426705, 0.3587736163604044)`;
- shard 3: `(0.5996899264483135, 0.5996899101531477)`.

Per-time trace-distance vectors also agreed tightly between methods on every shard. The frozen target convention was the existing controlled-phase toy target `target(theta*T)` at `T=[0.25,0.5,1.0]`; this is only linear toy-time phase scaling and is not asserted to be continuum gravity-time dynamics.

Classification: `DERIVED_SCOPED_OU_COLORED_TRAJECTORY_COMPARATOR_SUPPORT`.

Scope ceiling: stationary OU finite-correlation scalar classical noise with one fixed local-sum coupling, evaluated on this three-time toy trajectory. This closes a colored finite-correlation trajectory comparator subgate only. It is not a no-go theorem for all colored, non-Markovian, classical or semiclassical mediators and does not establish information-backflow non-Markovianity, new physics, or full quantum gravity.