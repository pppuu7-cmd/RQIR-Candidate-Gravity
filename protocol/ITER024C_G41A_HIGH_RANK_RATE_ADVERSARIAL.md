# ITER024C / G41-A — preregistered high-rank classical-rate adversarial gate

Authorized only by terminal G41-C calibration PASS (run `34710257380`). This is a prospective RCG-002 toy-trajectory comparator gate.

Frozen family/search:
- ranks K=4,5,6;
- for each `(rank, target shard)`, use exactly the deterministic G41-P/G41-C classical coefficient frame for the same `(rank, shard)`; frames were constructed independently of RCG-002;
- optimize only positive mode rates `kappa_k` in the calibrated bounds `[0.02,0.25]`;
- identical Sobol/LHS start constructions, 16 starts, top-4 bounded least-squares refinements, `max_nfev=400`, trajectory times `(0.2,0.7,1.3)`, and six product probes as G41-C;
- target is the RQIR-CG internal controlled-phase toy trajectory `U(t)=exp[-i theta t Z⊗Z]`, with the same four target-shard `theta` values used in earlier prospective comparator gates;
- exact target-dependent rates/coordinates are never injected as starts.

Frozen scientific rule:
- per lane, the reported winner is selected by maximum state trace-distance gap across the frozen times/probes;
- nonzero comparator gap threshold `>1e-4`;
- for each `(rank, shard)`, Sobol/LHS best-gap agreement must be `<=0.002`;
- overall finite-family support requires all 12 rank×shard cells to satisfy both rules;
- no cross-rank nesting rule is imposed because the frozen rank-4/5/6 mode frames are independently constructed and are not nested subspaces.

Scope/claim lock:
- PASS, if obtained, is only scoped support against the finite rate-only rank-4/5/6 frame-indexed classical random-Hamiltonian families;
- this does not test arbitrary mode orientations or arbitrary PSD 6x6 Kossakowski matrices;
- it is not an all-classical, all-Markovian, or gravity-theory no-go and does not establish new physics/full quantum gravity;
- FAIL is retained exactly; no bounds, frames, starts, targets, times, probes, thresholds or budgets may change inside this run.
