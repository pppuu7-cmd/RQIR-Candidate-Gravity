# RQIR-CG Iter011 / G29 robustness summary

Date: 2026-09-12

## Provenance

- Workflow run: `34694101699`
- Head commit: `c4c6f0d35e4e57a2105facafee2bdddc8036a52f`
- Summary artifact: `rcg011-summary`, artifact id `10297528599`
- Artifact digest: `sha256:b7f80fc91bba1b45371ec1cec1865ddbc9dab3a1ab7c4138a94d4a5064287356`
- Matrix: 6 independent streams x 4 frozen shards = 24 scientific lanes, plus aggregate.

## Frozen scope

Finite two-qubit Markovian single-axis-per-site measurement-feedback comparator family with `Gamma_A * Gamma_B = chi^2`.

This gate is a robustness/validity audit of that finite family. It is **not** a no-go theorem against all semiclassical-gravity or classical-mediator models.

## Terminal result

All 24 lanes were structurally valid. All 24 satisfied their prospectively frozen scientific support criterion:

- basis covariance: 4/4;
- CPTP/PSD admissibility: 4/4;
- null / false-positive calibration: 4/4;
- independent RK4 convergence cross-check: 4/4;
- local identifiability / Jacobian rank: 4/4;
- multistart continuous adversarial nearest-comparator search: 4/4.

Aggregate diagnostics:

- minimum adversarial continuous gap: `0.02500020131464493`;
- minimum Choi eigenvalue: `-7.229908172761597e-16` (numerical zero at the frozen `-1e-8` admissibility floor);
- minimum local identifiability rank: `6/6`;
- maximum finest-grid RK4/eigendecomposition trace-distance discrepancy: `1.0037722995948985e-11`.

## Classification

`DERIVED_SCOPED_ROBUSTNESS_SUPPORT` for the declared single-axis Markovian comparator family.

The result strengthens the inference that the observed finite-family gap is not an artifact of local basis diagnostics, gross channel inadmissibility, false-positive calibration, the eigendecomposition propagator, local parameter rank loss, or a simple continuous angular/asymmetry optimization loophole.

## Promotion ceiling

Forbidden from this result alone:

- exclusion of all semiclassical gravity;
- exclusion of all LOCC/non-LOCC classical mediator constructions;
- a general quantum-gravity no-go theorem;
- `NEW_PHYSICS_FOUND` or `FULL_QUANTUM_GRAVITY`.

## Next admissible gate

Broaden the comparator itself. The next high-information test should embed the single-axis family inside an additive multi-channel GKSL measurement-feedback family and run adversarial K=2/K=3 searches with null and physical-admissibility controls. If that broader family closes the gap, G29 becomes a useful negative diagnostic of the single-axis restriction. If a gap survives, the claim may be promoted only to the explicitly tested multi-channel family.
