# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active gates: `ITER023C / G40-RC-A axis-covariant adversarial` and `ITER024B / G41-C high-rank rate calibration`
Phase: `INDEPENDENT_RQIR_DERIVATION / FINITE_COMPARATOR_VALIDITY_AND_WITNESS_ROBUSTNESS`

## Canonical status

- Candidate-model/programme readiness: **59%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

Readiness is an internal construction metric, not a probability of physical correctness. The 58→59 increase records terminal closure of the corrected truly nested G37-A3 comparator gate only. G40 witness/calibration diagnostics and G41 implementation/calibration work do not themselves raise readiness.

## Newly closed

### G37-A3 — terminal scoped PASS

Run `34708041385`, head `28d6fa6343dabb068aba5a462f6026d8ec1a6a4f`, aggregate `103594427577`, artifact `10302623647`, digest `sha256:5b50793fe136cc30ce7aa60fae05a7be60b7895794686a2f35a5ca82feb2de63`.

Classification: `DERIVED_SCOPED_TRULY_NESTED_MF_PLUS_SHARED_BOUNDARY_PRESERVING_COMPARATOR_SUPPORT`. Scope is only the calibrated finite K2-MF + one shared Gaussian Markovian-noise family. Durable note: `results/ITER019F_G37A3_TERMINAL.md`.

### G40-A — terminal frozen support-rule failure

Run `34708971194`, head `dab6418075f5f7122e72444c61c7d3554a0002fb`, aggregate `103594269913`, artifact `10302404036`, digest `sha256:5f299a2a08e228894b1cb52cb2059f4f1c961c387f0e30e0842307a1d8eafe52`.

Classification: `NEGATIVE_RESULT / G40A_FROZEN_SUPPORT_RULE_NOT_MET`. Shards 0/1 produced no admissible fixed-witness strict candidate; shard 2 was consistent; shard 3 violated frozen Sobol/LHS agreement. G40-A remains failed and cannot be retroactively promoted.

### G40-D — terminal witness fragility diagnostic

Run `34709706322`, head `89dc08a4f31a76851e5b12c970aaf8b4b81eaa1b`, aggregate `103596229487`, artifact `10301928780`, digest `sha256:35d4dba7b5aea572e33b7ba6c067a5f4695b8d18fb84455e958ed2cde25a2383`.

Classification: `FIXED_WITNESS_FRAGILE_ON_PANEL`. The prospectively frozen four-element local witness panel produced admissible escape candidates on shards 0/1 where the original fixed witness found none. This diagnostic does not promote G40-A; it shows that a stable successor must use a separately calibrated family/basis-covariant witness rule. Durable note: `results/ITER023A_G40D_TERMINAL.md`.

### G40-RC-C — terminal axis-frame-covariant calibration PASS

Run `34710049387`, head `1f79d9c7e1ceb97ba0dc3273ef25d2c8664d42e6`, aggregate `103597100244`, artifact `10303335725`, digest `sha256:6b3d446be11880ae79cad0a55b74ccfff0cdf33a55f1045e04b27d6752f56f74`.

Both independently seeded methods passed 4/4 hidden controls. Minimum axis-frame-covariant BLP was `~0.8471377488 > 0.02`; worst recovery gaps were `~1.73e-15` and `~9.37e-16`. Classification: `AXIS_FRAME_COVARIANT_RTN_SEARCH_CALIBRATED`. This is calibration authority only; the witness is family-axis covariant, not globally BLP-optimal. Durable note: `results/ITER023B_G40RCC_TERMINAL.md`.

### G41-P — terminal high-rank classical implementation PASS

Run `34710097236`, head `e6c74225814d4627945d3edbeda9620e4e4a57c2`, aggregate `103597226535`, artifact `10303101144`, digest `sha256:a189c87f4cb786e3fd2f5324e3bb54e3813d55f7f7ac959ff263747b811c185f`.

All 12 rank-4/5/6 implementation/admissibility lanes passed. Classification: `HIGH_RANK_CLASSICAL_KOSSAKOWSKI_IMPLEMENTATION_VALIDATED`. Provenance is explicit classical shared Gaussian random-Hamiltonian noise; no RCG-002 target was used. Durable note: `results/ITER024A_G41P_TERMINAL.md`.

## Active gate 1 — G40-RC-A

Preregistered protocol: `protocol/ITER023C_G40RC_A_AXIS_COVARIANT_ADVERSARIAL.md`.
Launch commit: `3e31a9faa8b05a9bf5d6971a4ca4d94e6386b633`.
Run: `34710216045`.

Prospective adversarial test of the same finite symmetric hidden-classical RTN family using exactly the axis-frame-covariant witness/search calibrated in G40-RC-C. Frozen thresholds remain nonzero gap `>1e-4`, Sobol/LHS agreement `<=0.002`, axis-covariant BLP `>0.02`. A PASS, if obtained, remains finite-family scoped only.

## Active gate 2 — G41-C

Preregistered protocol: `protocol/ITER024B_G41C_HIGH_RANK_RATE_CALIBRATION.md`.
Launch commit: `2bac531b1c68d0fc735b8135b579662b1318fe52`.
Run: `34710257380`.

Positive-control optimizer calibration only: ranks 4/5/6 × four shards × Sobol/LHS, optimizing positive rates on the frozen G41-P classical mode frames. Recovery threshold `<0.002`. This does not calibrate arbitrary PSD Kossakowski orientations and contains no RCG-002 target.

## Stable closed finite-comparator layers

- G35/G35-R: K2/K3/K4 additive independent measurement-feedback calibration, scoped adversarial support and held-out optimizer robustness.
- G36-P/C/A: one shared Gaussian classical-noise implementation/calibration/scoped support.
- G37-C2/A3: corrected truly nested MF + shared-noise calibration and scoped boundary-preserving support.
- G38-P/C/A: OU finite-correlation three-time toy-trajectory implementation/calibration/scoped support.
- G39-P/C/A2: finite rank2/rank3 multimode shared classical white-noise implementation/calibration/scoped support.
- G40-P/C2/C3: strict RTN implementation and fixed-witness search calibration; G40-A itself failed and G40-D diagnosed fixed-witness fragility.
- G40-RC-C: axis-frame-covariant RTN search calibration; adversarial verdict pending G40-RC-A.
- G41-P: high-rank classical Kossakowski implementation/provenance; optimizer calibration pending G41-C.

## Open scientific layers

- terminal prospective G40-RC-A verdict;
- G41-C calibration and then only a separately preregistered finite high-rank adversarial subfamily if calibrated;
- arbitrary-orientation/general PSD Kossakowski calibration remains open even if G41-C passes;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and any actual gravity-theory constitution gate.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, treating green CI as scientific PASS, post-hoc threshold/family/witness weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_59_PERCENT + THEORY_ESTABLISHED_0 + FINITE_COMPARATOR_SUPPORT_ONLY + G37A3_SCOPED_PASS + G40A_FROZEN_FAIL + G40D_FIXED_WITNESS_FRAGILE + G40RCC_CALIBRATED + G40RCA_RUNNING + G41P_IMPLEMENTATION_VALIDATED + G41C_QUEUED_OR_RUNNING`.
