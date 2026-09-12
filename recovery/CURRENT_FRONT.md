# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active iteration: `ITER019A`
Phase: `INDEPENDENT_RQIR_DERIVATION / COMBINED_CLASSICAL_COMPARATOR_CALIBRATION`

## Canonical status

- Candidate-model/programme readiness: **56%**
- Theory established: **0%**
- Active seed: `RCG-002 Relational controlled-phase channel`
- Independent-from-QGR construction contract: **FROZEN**
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`

Readiness is an internal construction metric, not a probability that the candidate is correct. The move from 55% to 56% records closure of one additional scoped adversarial comparator layer, shared Gaussian classical Hamiltonian noise. It does not imply a general no-go theorem and it does not score the still-running combined-family calibration.

## Iter017 / G35 terminal — K=3/K=4 measurement-feedback comparator

Run `34697766107`, head `fbc71768da3cec0d6ea5a8cbb755a29036b16726`, aggregate job `103578278887`, summary artifact `10301201162`, digest `sha256:7e07e47311db7a279e2de47502d64a36cf31623c10c0da67f062ee8817bac199`.

All 24 frozen lanes were structurally valid. K=3 and K=4 each passed all four RCG-002 shards under both calibrated methods with nonzero gap `>1e-4`, cross-method agreement `<=0.002`, nesting sanity, and 4/4 admissibility. Classification: `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT`.

Scope ceiling remains the finite additive independent single-axis Markovian measurement-feedback GKSL family. Durable note: `results/ITER017_G35_CALIBRATED_K3K4_TERMINAL.md`.

## Iter017R / G35-R terminal — held-out optimizer robustness

Run `34702384573`, head `1b93cbf14b4705ae2699f559523d1c1b1ae28be5`, aggregate job `103580063685`, summary artifact `10300682102`, digest `sha256:5724519f32faf1e10d011e97d10df283fa6225facdfdb9ad8b14e82577557b13`.

All 18 new held-out positive controls passed for K=2/K=3/K=4 and both Sobol-LSQ/LHS-LSQ designs. Worst trace-distance recovery gap was `5.6435139378164e-13` versus frozen `<0.002`. Classification: `HELDOUT_OPTIMIZER_ROBUSTNESS_PASS_K2_K3_K4`. This is methodology robustness only. Durable note: `results/ITER017R_G35R_HELDOUT_OPTIMIZER_REPLICATION_TERMINAL.md`.

## Iter018A / G36-P terminal — shared-noise implementation

Run `34702575861`, head `270a26300117aeebe23af126dd4e6c53c96cf3f9`, aggregate job `103576905242`, artifact `10300760790`, digest `sha256:3a03b7462ccf026c6cc7cdef88fbe0c9f4710c3040f467a5caf9fa5e3e4d228d`.

12/12 frozen implementation/provenance checks passed for shared Gaussian classical Hamiltonian noise represented as a convex mixture of product unitaries. Classification: `CLASSICAL_SHARED_NOISE_IMPLEMENTATION_VALIDATED`.

## Iter018B / G36-C terminal — shared-noise optimizer calibration

Run `34703606707`, head `95335aa32e92dcd1cc76762cd6fd3717754a1057`, aggregate job `103579641822`, summary artifact `10301561148`, digest `sha256:5f82bf2eb2b74bf0ac2f2bbc6e5f252898da97420fa5e0da1f1fd91f6e5f5f0c`.

All 12 hidden in-family positive-control lanes passed with both independently defined Sobol-LSQ and Latin-hypercube-LSQ constructions. Worst trace-distance recovery gap was `5.288760714311301e-15` versus frozen `<0.002`. Classification: `POSITIVE_CONTROL_METHOD_CALIBRATED_SHARED_NOISE`. Durable note: `results/ITER018B_G36C_SHARED_NOISE_CALIBRATION_TERMINAL.md`.

## Iter018C / G36-A terminal — shared-noise RCG-002 adversarial comparator

Run `34703779268`, head `15ba7c90fd4794d3d31e41a5a08ee35511284faf`, aggregate job `103580126265`, summary artifact `10301491686`, digest `sha256:2a75483c5ed8261e62466581b7a00046dd5d7a81ddffc5e49e38e819f81832ce`.

All 8 frozen adversarial lanes were structurally valid. For all four RCG-002 shards both calibrated methods retained nonzero gaps and agreed within `0.002`. Gap pairs (Sobol,LHS) were approximately `(0.025499009,0.025499011)`, `(0.100361598,0.100361587)`, `(0.358737039,0.358737038)`, `(0.598026653,0.598026873)`.

Classification: `DERIVED_SCOPED_SHARED_NOISE_CALIBRATED_COMPARATOR_SUPPORT`.

Scope ceiling: one shared Gaussian classical Hamiltonian-noise process coupled to local Pauli axes, represented as a convex mixture of product unitaries. This is not a no-go theorem for all classical/semiclassical mediators. Durable note: `results/ITER018C_G36A_SHARED_NOISE_ADVERSARIAL_TERMINAL.md`.

## Active gate — Iter019A / G37-C combined comparator calibration

Run `34703787083`, launch head `59cf94512a65a54a37eba05ae3093b7ee85bead0`.

The prospectively frozen combined family is the calibrated K=2 additive independent single-axis measurement-feedback GKSL generator plus the validated shared Gaussian classical Hamiltonian-noise generator. This gate is positive-control calibration only and does not inspect RCG-002 adversarial performance.

Frozen controls: six hidden in-family states × two independent optimizer designs, including four interior combined controls, one exact measurement-feedback-only boundary control, and one strong shared-noise control; plus four independent TP/CP/PSD/trace/Hermiticity admissibility lanes. Positive-control recovery must be `<0.002` in all 12 lanes; all four admissibility lanes must pass their frozen thresholds.

Latest checked live state: **14/16 scientific lanes terminal success; 2/16 in progress** (`positive sobol_lsq shard 4` and `positive lhs_lsq shard 4`). Aggregate is blocked until both finish. No scientific PASS is inferred from green individual jobs before aggregate inspection.

Only terminal G37-C scientific PASS may authorize a separate combined-family RCG-002 adversarial gate. A calibration failure is retained and blocks adversarial interpretation; no threshold/family rescue is allowed post hoc.

## Open layers after current gate

- combined measurement-feedback + shared-classical-noise adversarial comparator: blocked pending G37-C terminal PASS;
- broader correlated/general positive-Kossakowski classical-channel comparators: open;
- non-Markovian/colored-noise comparator layer: open;
- externally anchored observable/holdout programme: open;
- full candidate-gravity dynamics / continuum completion: open.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, any claim that all classical/semiclassical mediators are excluded, green-CI-as-science, post-hoc threshold weakening, retroactive promotion of G30/G31 minima, or importing physical assumptions/results from QGR/KMQGB/RQIR.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + K2_K3_K4_SCOPED_CALIBRATED_MEASUREMENT_FEEDBACK_SUPPORT + HELDOUT_OPTIMIZER_ROBUSTNESS_PASS + SHARED_NOISE_IMPLEMENTATION_AND_OPTIMIZER_CALIBRATED + SHARED_NOISE_SCOPED_CALIBRATED_COMPARATOR_SUPPORT + G37C_COMBINED_CALIBRATION_RUNNING`.
