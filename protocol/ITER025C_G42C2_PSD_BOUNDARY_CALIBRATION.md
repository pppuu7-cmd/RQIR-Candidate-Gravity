# ITER025C / G42-C2 — preregistered PSD-boundary optimizer calibration

Purpose: calibrate a boundary-capable parameterization of the bounded real-PSD 6x6 classical random-Hamiltonian Kossakowski family before any arbitrary-orientation adversarial gate. This is required because G42-C used strictly positive log-Cholesky diagonals and therefore covered only the SPD interior.

Frozen family/coordinates:
- `C = B B^T` with real lower-triangular `B`;
- six direct Cholesky diagonal coordinates bounded in `[0,0.60]`, so rank-deficient PSD boundaries are included exactly;
- fifteen strict-lower coordinates bounded in `[-0.30,0.30]`;
- every candidate remains PSD by construction and has explicit classical random-Hamiltonian provenance;
- no RCG-002 target is used.

Frozen hidden controls:
- four deterministic controls of intended Kossakowski ranks `2,4,5,6`, one per shard;
- each control is generated independently of RCG-002 with nonzero active Cholesky pivots and seeded off-diagonal entries only in active columns; inactive columns are exactly zero;
- exact hidden coordinates are never used as optimizer starts.

Frozen observable/search design:
- times `(0.15,0.45,0.9,1.4)` and the same six product-state probes as G42-J/C;
- independent scrambled Sobol and Latin-hypercube constructions;
- 32 starts per lane; refine best 6 least-squares starts; `max_nfev=1000`; fixed `ftol=xtol=gtol=1e-10`;
- scientific recovery metric: maximum output-state trace distance across all frozen times/probes;
- trajectory recovery tolerance `<0.002`;
- parameter-space cross-check: relative Frobenius Kossakowski error `<0.02`;
- recovered effective Kossakowski rank at eigenvalue threshold `1e-5` must equal the hidden intended rank.

Frozen support rule:
- each lane must satisfy all three: trace-gap `<0.002`, relative Kossakowski error `<0.02`, recovered rank equals hidden rank;
- each method must pass all four rank controls;
- overall PASS requires 4/4 Sobol and 4/4 LHS support.

Interpretation lock:
- PASS calibrates this bounded boundary-capable PSD search and may authorize only a separately preregistered adversarial gate with identical coordinate bounds/search rules;
- FAIL is retained exactly; no rank threshold, bounds, controls, starts, probe/timing set, budget or recovery tolerances may change inside this run;
- PASS is calibration only and does not increase programme readiness or imply any all-classical/no-go result.
