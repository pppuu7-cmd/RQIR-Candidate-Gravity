# ITER022E / G40-C3 — strict-BLP filtered-search calibration

Authorized only after corrected G40-C2 terminal calibration PASS. This new gate calibrates a changed search rule before any RCG-002 target is used.

Frozen before results:
- underlying RTN family, parameter bounds, Sobol/LHS designs, 16 starts, top-4 refinement, fixed four trajectory times, six product probes and max_nfev are unchanged from G40-C2;
- only candidates whose fixed-witness BLP total positive trace-distance increment is `>0.02` are scientifically admissible;
- the best admissible candidate must recover each G40-C2 hidden control with maximum trajectory trace distance `<0.002`;
- both Sobol and LHS must pass all four controls;
- if a lane produces no strict candidate, that lane fails calibration;
- no RCG-002 target is used and no result-dependent threshold or family change is allowed.

PASS authorizes only a separate prospective adversarial test against this **fixed-witness strict-BLP subset**. It does not establish a rotation-covariant characterization of all BLP-capable RTN channels, does not exclude all classical mediators, and is not novelty evidence.
