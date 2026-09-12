# ITER023C / G40-RC-A — preregistered axis-covariant RTN adversarial gate

Authorized only by terminal G40-RC-C calibration PASS (run 34710049387). This is a new prospective gate; G40-A remains terminally failed and is not reinterpreted.

Frozen before results:
- identical finite 8-parameter hidden-classical symmetric RTN family, parameter bounds, TIMES, six product probes, Sobol/LHS designs, 16 starts, top-4 least-squares refinements, `max_nfev=600`, and candidate-axis-frame covariant BLP witness used in G40-RC-C;
- identical strict admissibility filter: axis-covariant BLP `>0.02`;
- target is the RQIR-CG internal controlled-phase toy trajectory `U(t)=exp[-i theta t Z⊗Z]` on the same four target shards/`theta` values already used by G40-A; no target-dependent family or witness construction;
- per-lane support requires an axis-covariant-BLP-admissible candidate and residual trace-distance gap `>1e-4`;
- per-shard scientific support additionally requires Sobol/LHS best-gap agreement `<=0.002`;
- all four shards must satisfy those rules for overall scoped support;
- no thresholds, target shards, starts, family bounds, witness rule or refinement budget may be changed after launch.

Scope/claim lock:
- this tests only the finite symmetric hidden-classical RTN family under a candidate-axis-frame covariant BLP witness;
- the witness is family-covariant, not the globally optimized BLP measure over every state pair;
- PASS is finite-family scoped comparator support only, not a no-go for all non-Markovian/classical mediators and not evidence of full quantum gravity;
- FAIL is retained exactly and cannot be repaired inside this run.
