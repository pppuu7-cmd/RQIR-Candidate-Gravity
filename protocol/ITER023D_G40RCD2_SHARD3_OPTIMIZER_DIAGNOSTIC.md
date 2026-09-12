# ITER023D / G40-RC-D2 — preregistered shard-3 optimizer-convergence diagnostic

Purpose: diagnose the sole frozen failure of terminal G40-RC-A without changing its family, witness, target, or thresholds. G40-RC-A remains failed regardless of this diagnostic.

Observed preregistration trigger:
- G40-RC-A shard 3: Sobol best trace gap `0.7472831704713611`, residual norm `3.6144624457524848`; LHS best trace gap `0.7495355611279814`, residual norm `3.4575367787725106`;
- both candidates are strongly axis-covariant-BLP admissible, but their gap difference `0.0022523906566203067` exceeds the frozen `0.002` agreement rule;
- the opposite ordering of trace gap and least-squares residual motivates an optimizer/objective-geometry diagnostic, not a threshold change.

Frozen diagnostic:
- only the unchanged G40-RC-A shard-3 target (`theta=1.4`);
- identical 8-parameter RTN family, parameter bounds, trajectory times, six product probes, axis-frame-covariant BLP witness, BLP filter `>0.02`, and trace-distance metric;
- four new deterministic independent start designs: scrambled Sobol, Latin hypercube, Halton, and pseudorandom uniform;
- 64 starts per design; rank starts by the unchanged least-squares residual; refine the best 12 with bounded least squares, `max_nfev=900`;
- hidden/previous best coordinates are never injected as starts;
- among refined BLP-admissible candidates, each method's reported winner is selected by the scientific maximum trace-distance gap, not residual norm;
- all numerical diagnostics must be finite.

Frozen interpretation:
- if all four independent best gaps lie within `0.002` of each other, classify `DEEP_SEARCH_CONVERGENCE_PASS / ORIGINAL_SHARD3_SEARCH_NONROBUSTNESS_DIAGNOSED`; this may authorize a separately preregistered repaired adversarial run using the deeper search rule on all four shards;
- otherwise classify `PERSISTENT_OPTIMIZER_OR_OBJECTIVE_GEOMETRY_NONROBUSTNESS`; no repaired physics verdict is authorized;
- this diagnostic itself cannot turn G40-RC-A into PASS and cannot change readiness.
