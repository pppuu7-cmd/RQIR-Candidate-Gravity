# ITER019F / G37-A3 — boundary-preserving repaired adversarial gate

Triggered only after G37-A2-N established exact shared-parent embedding to machine precision but exposed a surrogate-objective failure: unconstrained LSQ refinement can worsen the final trace-distance metric.

This is a new prospective test. No earlier G37-A2 result is retroactively promoted.

Frozen before G37-A3 results:
- same G37-C2 comparator family, RCG-002 targets, parameter bounds, Sobol/LHS designs and science thresholds;
- preserve all original G37-A2 combined-family starts/refinements;
- reproduce and embed the calibrated G36 shared-noise parent exactly at `lambda_MF=0`;
- reproduce and embed the calibrated G34 K2 measurement-feedback parent exactly at `lambda_MF=1` and `cA=cB=0`;
- both exact parent boundary points remain candidates even if LSQ refinement worsens them;
- add LSQ refinements from both boundary seeds, but rank all candidates by final trace distance;
- exact embedding and nesting tolerance: `1e-10`;
- adversarial nonzero gap: `>1e-4` under both methods;
- cross-method agreement: `<=0.002` per shard;
- no threshold/family changes after results.

PASS, if obtained, is only scoped evidence against this finite truly nested Markovian MF + one shared classical-noise family. It is not a no-go theorem for all classical or semiclassical mediators and is not evidence of full quantum gravity.
