# ITER022F / G40-A — fixed-witness strict-BLP RTN adversarial gate

Authorized only after terminal G40-C2 optimizer calibration PASS and G40-C3 strict-filtered-search calibration PASS. This is the first RCG-002 comparison in the G40 branch.

Frozen before results:
- same 8-parameter hidden-classical RTN family, bounds, Sobol/LHS start designs, 16 starts, top-4 least-squares refinement, fixed times `[0.35,0.80,1.60,3.00]`, six product probes and max_nfev as G40-C2/C3;
- identical fixed-witness strict filter: only candidates with BLP total positive trace-distance increment `>0.02` are admissible;
- target is the controlled-phase toy trajectory `U(t)=exp[-i theta*t (Z⊗Z)]` on the same times/probes, with the four pre-existing `CASES` theta shards; this target convention is frozen before results;
- both methods must produce at least one strict candidate on every shard;
- best strict-candidate gap must be `>1e-4` under both methods;
- Sobol/LHS gap disagreement must be `<=0.002` per shard;
- no result-dependent threshold, witness, probe, time-grid, family, target or optimizer changes.

PASS, if obtained, is only scoped evidence against this calibrated finite **fixed-witness BLP>0.02** hidden-classical RTN subset for the controlled-phase toy trajectory. It is not a rotation-covariant statement about every BLP-capable RTN channel, not a no-go for all classical/non-Markovian mediators, and not evidence of full quantum gravity or new physics.
