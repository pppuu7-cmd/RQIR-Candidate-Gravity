# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active gate: `ITER023A / G40-D witness-panel diagnostic`
Phase: `INDEPENDENT_RQIR_DERIVATION / FINITE_COMPARATOR_VALIDITY_AND_WITNESS_ROBUSTNESS`

## Canonical status

- Candidate-model/programme readiness: **59%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

Readiness is an internal construction metric, not a probability of physical correctness. The 58→59 increase records terminal closure of the corrected truly nested G37-A3 comparator gate only. G40 calibration/diagnostic work does not itself raise readiness.

## Newly closed

### G37-A3 — terminal scoped PASS

Run `34708041385`, head `28d6fa6343dabb068aba5a462f6026d8ec1a6a4f`, aggregate `103594427577`, artifact `10302623647`, digest `sha256:5b50793fe136cc30ce7aa60fae05a7be60b7895794686a2f35a5ca82feb2de63`.

All 8 lanes passed the frozen exact-parent-embedding, boundary-preserving nesting, nonzero-gap and Sobol/LHS agreement rules. Classification: `DERIVED_SCOPED_TRULY_NESTED_MF_PLUS_SHARED_BOUNDARY_PRESERVING_COMPARATOR_SUPPORT`. Scope is only the calibrated finite K2-MF + one shared Gaussian Markovian-noise family. Durable note: `results/ITER019F_G37A3_TERMINAL.md`.

### G40-C2 and G40-C3 — calibration PASS

G40-C2 run `34708550582` is terminal PASS for the corrected eligible hidden controls. G40-C3 run `34708885346`, head `af8f23f7970d90d904914c938a8828d1cf847651`, aggregate `103593923157`, artifact `10302603412`, digest `sha256:a2eda672b6c3a8e581a081b30e9d278619a0bf71356eb6587dbe8ac26f428845`, calibrated the unchanged fixed-witness BLP>0.02 filtered-search rule. These are calibration authority only.

### G40-A — terminal frozen support-rule failure

Run `34708971194`, head `dab6418075f5f7122e72444c61c7d3554a0002fb`, aggregate `103594269913`, artifact `10302404036`, digest `sha256:5f299a2a08e228894b1cb52cb2059f4f1c961c387f0e30e0842307a1d8eafe52`.

All 8 lanes were structurally valid, but the preregistered all-shards support rule failed. Shards 0 and 1 produced no admissible fixed-witness BLP>0.02 candidate in either method. Shard 2 gave consistent scoped separation (`~0.631699`). Shard 3 produced admissible nonzero gaps but Sobol/LHS disagreement exceeded `0.002` (`0.747283...` vs `0.749535...`). Classification: `NEGATIVE_RESULT / G40A_FROZEN_SUPPORT_RULE_NOT_MET`.

This is not evidence that RTN fits RCG-002 and not a no-go against RTN. G40-A remains failed and cannot be retroactively promoted. Durable note: `results/ITER022F_G40A_TERMINAL.md`.

## Active G40-D diagnostic

Preregistered diagnostic: `protocol/ITER023A_G40D_WITNESS_PANEL_DIAGNOSTIC.md`.
Launch commit: `89dc08a4f31a76851e5b12c970aaf8b4b81eaa1b`.
Run: `34709706322`.

Frozen purpose: test whether G40-A's fixed-witness exclusions are fragile under a prospectively fixed four-element local basis/witness panel. Same family, targets, optimizer, start designs and thresholds are retained. This diagnostic cannot promote G40-A or support an all-BLP/all-classical claim.

## Stable closed finite-comparator layers

- G35/G35-R: K2/K3/K4 additive independent measurement-feedback calibration, scoped adversarial support and held-out optimizer robustness.
- G36-P/C/A: one shared Gaussian classical-noise implementation/calibration/scoped support.
- G37-C2/A3: corrected truly nested MF + shared-noise calibration and scoped boundary-preserving support.
- G38-P/C/A: OU finite-correlation three-time toy-trajectory implementation/calibration/scoped support.
- G39-P/C/A2: finite rank2/rank3 multimode shared classical white-noise implementation/calibration/scoped support.
- G40-P: strict classical RTN information-backflow implementation/witness validation.

## Open scientific layers

- G40-D witness/basis fragility diagnostic and, only if scientifically justified afterward, a separately calibrated rotation-covariant strict-BLP gate;
- higher-rank/general positive-Kossakowski classical comparator beyond finite G39 rank;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and any actual gravity-theory constitution gate.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, treating green CI as scientific PASS, post-hoc threshold/family/witness weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_59_PERCENT + THEORY_ESTABLISHED_0 + FINITE_COMPARATOR_SUPPORT_ONLY + G37A3_SCOPED_PASS + G40C2_C3_CALIBRATED + G40A_FROZEN_FAIL + G40D_RUNNING_DIAGNOSTIC`.
