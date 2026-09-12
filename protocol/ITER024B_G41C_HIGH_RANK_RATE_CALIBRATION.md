# ITER024B / G41-C — preregistered high-rank classical-rate calibration

Authorized only after G41-P implementation/provenance PASS. This gate calibrates optimization on a finite nested subfamily; it does not claim calibration of arbitrary PSD 6x6 Kossakowski orientation.

Frozen family:
- ranks K=4,5,6;
- for each `(K, shard)` use exactly the deterministic orthonormal coefficient frame `V` from G41-P, independent of RCG-002;
- optimize only positive mode rates `kappa_k` in frozen bounds `[0.02,0.25]`;
- generator remains `L=sum_k kappa_k D[F_k]`, so every candidate retains explicit classical random-Hamiltonian provenance;
- hidden positive controls are the G41-P deterministic rates `0.055+0.018*j+0.004*K`, which lie strictly inside the bounds.

Frozen calibration design:
- ranks 4/5/6 × four shards × two independent start constructions (`sobol_lsq`, `lhs_lsq`) = 24 lanes;
- trajectory times `(0.2,0.7,1.3)` and the six product probes already used in the RTN calibration layer;
- 16 starts per lane; refine the best 4 with bounded least squares; `max_nfev=400`;
- scientific metric is maximum state trace distance across all times/probes;
- recovery tolerance `<0.002`;
- all diagnostics must be finite; exact hidden coordinates are never inserted as optimizer starts.

Frozen support rule:
- each lane supports calibration iff the best recovered max trace-distance gap is `<0.002`;
- each rank requires 4/4 support for both Sobol and LHS;
- overall PASS requires all ranks and methods to pass.

Interpretation lock:
- PASS calibrates only the positive-rate search on these frozen high-rank mode frames and may authorize a separate prospective adversarial rate-family gate;
- PASS does not calibrate arbitrary mode orientations or arbitrary PSD Kossakowski matrices;
- FAIL is retained exactly; no bounds, hidden controls, start counts, probes, times or tolerance changes inside the run;
- no RCG-002 target is used here and readiness does not increase from calibration alone.
