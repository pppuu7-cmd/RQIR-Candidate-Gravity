# ITER025B / G42-C — preregistered full-PSD classical Kossakowski optimizer calibration

Authorized only after G42-J terminal `FULL_LOCAL_RANK_IDENTIFIABILITY_PRE_GATE` PASS. No RCG-002 target is used.

Frozen family/coordinates:
- full real-PSD 6x6 classical random-Hamiltonian Kossakowski family `C=L L^T` in the same 21 real Cholesky coordinates used by G42-J;
- six log-diagonal coordinates bounded in `[-2.0,-0.5]`; fifteen strict-lower coordinates bounded in `[-0.12,0.12]`;
- four hidden positive controls are exactly the deterministic G42-J controls and lie strictly inside those bounds;
- exact hidden coordinates are never used as optimizer starts.

Frozen observable/search design:
- times `(0.15,0.45,0.9,1.4)` and the same six product-state probes as G42-J;
- two independent start constructions: scrambled Sobol and Latin hypercube;
- 32 starts per lane; rank starts by the unchanged Frobenius/least-squares trajectory residual; refine the best 6 with bounded least squares;
- `max_nfev=1000`, fixed tolerances `ftol=xtol=gtol=1e-10`;
- scientific recovery metric is maximum state trace distance over all frozen times/probes;
- recovery tolerance `<0.002`;
- all diagnostics finite and every recovered Kossakowski matrix must remain positive definite by construction.

Frozen support rule:
- each lane supports calibration iff its best recovered candidate has max trace-distance gap `<0.002`;
- each method must pass all four hidden controls;
- overall calibration PASS requires 4/4 Sobol and 4/4 LHS support.

Interpretation lock:
- PASS calibrates only this full-PSD 21-coordinate positive-control search and may authorize a separately preregistered RCG-002 adversarial gate using exactly the same family/bounds/times/probes/start designs/refinement budget;
- FAIL is retained exactly; no bounds, controls, starts, probes, times, budgets, objective or tolerance changes inside this run;
- calibration alone does not increase programme readiness and does not imply any all-classical/no-go result.
