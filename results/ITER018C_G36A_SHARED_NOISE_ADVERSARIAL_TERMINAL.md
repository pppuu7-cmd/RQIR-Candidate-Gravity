# Iter018C / G36-A terminal result

Authoritative run `34703779268`, head `15ba7c90fd4794d3d31e41a5a08ee35511284faf`, aggregate job `103580126265`, summary artifact `10301491686`, digest `sha256:2a75483c5ed8261e62466581b7a00046dd5d7a81ddffc5e49e38e819f81832ce`.

All 8 prospectively frozen adversarial lanes were structurally valid. For each of four RCG-002 shards, both G36-C-calibrated methods retained a trace-distance gap above `1e-4` and agreed within the frozen `0.002` cross-method scale.

Gap pairs (Sobol-LSQ, LHS-LSQ):
- shard 0: `(0.025499008832948887, 0.025499011169133425)`;
- shard 1: `(0.10036159822213998, 0.10036158741640057)`;
- shard 2: `(0.3587370385387613, 0.35873703839655824)`;
- shard 3: `(0.5980266528346264, 0.5980268730784868)`.

Classification: `DERIVED_SCOPED_SHARED_NOISE_CALIBRATED_COMPARATOR_SUPPORT`.

Scope ceiling: one shared Gaussian classical Hamiltonian-noise process coupled to two local Pauli axes, represented as a convex mixture of product unitaries. This is not a no-go theorem for all classical or semiclassical mediators. The stronger combined measurement-feedback + shared-noise family remains a separate open gate.