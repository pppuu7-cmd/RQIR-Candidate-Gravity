# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active gates: `ITER026 / G42-A bounded-PSD adversarial` + `ITER026R / G42-R held-out calibration replication` + `ITER026B / G42-BC basis/chart audit`
Phase: `INDEPENDENT_RQIR_DERIVATION / BROAD_CLASSICAL_COMPARATOR_ATTACK`

## Canonical status

- Candidate-model/programme readiness: **60%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

Readiness is programme completion, not a probability of physical correctness. `59% -> 60%` came only from terminal G41-A scoped adversarial closure. Calibration/diagnostic/identifiability gates do not raise readiness by themselves.

## Newly closed calibration authority

### G42-C2 PSD-boundary calibration — PASS

Run `34710953936`, head `858ad4b6848362bf430eaab849fb0ed4166f9cde`, aggregate `103600409310`, artifact `10303587123`, digest `sha256:d71af618510d0d61fbac14a3db91e9bf713822f657cfd985cc54e96fbf2ac94e`.

All 8/8 rank-2/4/5/6 positive-control lanes passed. Sobol worst trace gap `4.2824978732075346e-10`, worst relative-C error `3.3388943747698924e-09`; LHS worst gap `1.9221941865034614e-10`, worst relative-C error `1.9289529867904655e-09`. Classification `PSD_BOUNDARY_OPTIMIZER_CALIBRATED`. Durable note: `results/ITER025C_G42C2_TERMINAL.md`.

### G42-C3 rank-completion calibration — PASS

Run `34711048394`, head `35f719fdad8af1e2f8fdd71727c84abec3857c2a`, aggregate `103601042911`, artifact `10303627020`, digest `sha256:a9fa4ccaa8f6f79540311deb3f8a42be74661e2793d6dc7e5092570a7e52e3d1`.

All 8/8 positive-control lanes covering missing effective ranks 1 and 3 passed. Sobol worst trace gap `4.2872736979461425e-07`, worst relative-C error `8.398809261492516e-06`; LHS worst gap `7.34537126692358e-07`, worst relative-C error `1.5813386032144557e-05`. Classification `PSD_BOUNDARY_RANK_COMPLETION_CALIBRATED`. Durable note: `results/ITER025D_G42C3_TERMINAL.md`.

Joint interpretation: C2+C3 calibrate the frozen optimizer across effective PSD ranks 1–6 **within the bounded Cholesky chart** `diag∈[0,0.60]`, `offdiag∈[-0.30,0.30]`. This is not an unbounded mathematical full-PSD theorem.

## Primary active gate — G42-A

Protocol: `protocol/ITER026_G42A_BOUNDARY_PSD_ADVERSARIAL.md`.
Launch/head: `f7f48725a3d57398426f8ac9341a1d11b9cc591f`.
Run: `34712491707`.

Eight prospective adversarial lanes = Sobol/LHS × four frozen RCG-002 target shards. Same 21-coordinate boundary-capable bounded real-PSD 6x6 Markovian classical random-Hamiltonian Kossakowski chart calibrated by C2+C3. Frozen scientific rule per shard: both methods admissible, each gap `>1e-4`, absolute Sobol/LHS gap difference `<=0.002`; all four shards required.

Early non-terminal check only: shard 3 Sobol gap `0.8197294896504166`, LHS gap `0.819101112669069`, difference `0.0006283769813476 < 0.002`; both maps passed PSD/TP/Choi/state/trace admissibility. This is not a terminal gate classification.

## Independent active gate — G42-R

Protocol: `protocol/ITER026R_G42R_HELDOUT_PSD_CALIBRATION.md`.
Launch/head: `3b53451c192c8bcaedd39105d1c9b9b3ae3aa6e6`.
Run: `34712524241`.

Twelve held-out positive-control lanes = new hidden controls ranks 1–6 × Sobol/LHS with seeds disjoint from C2/C3. Same bounded PSD chart/search/recovery rules. Methodology robustness only; cannot alter G42-A thresholds/verdict or raise readiness by itself.

Latest live state before this front update: 11/12 terminal; only rank-1/LHS remained in progress.

## Independent response-blind gate — G42-BC

Protocol: `protocol/ITER026B_G42BC_BASIS_CHART_AUDIT.md`.
Launch/head: `11b5a0604ada235a4504990966b89f8f89857471`.
Run: `34712857575`.

Twenty-four response-blind lanes = effective ranks 1–6 × four fixed local `SO(3)_A×SO(3)_B` basis rotations. No RCG-002 target/result is used. Frozen questions: (1) does the implemented generator obey local-basis covariance to relative error `<1e-10`; (2) do rotated PSD controls remain inside the same production Cholesky coordinate box after canonical semidefinite factorization?

If implementation covariance passes but any rotated control exits the box, classification is `BOUNDED_CHART_ROTATION_COVERAGE_LIMIT_FOUND`. That does not alter the exact bounded-chart G42-A number, but forbids interpreting it as basis-invariant evidence for the entire mathematical PSD family. At launch all 24 lanes were queued behind active heavy optimization work.

## Stable scientific closures

- G35: finite K2/K3/K4 additive independent measurement-feedback scoped support.
- G36: one shared Gaussian classical-noise scoped support.
- G37: corrected nested MF + shared-noise finite scoped support.
- G38: OU finite-correlation toy comparator support.
- G39: finite rank2/rank3 multimode shared white-noise support.
- G40: RTN calibration succeeded but adversarial support unresolved due persistent optimizer/objective nonrobustness; no RTN physics PASS.
- G41: rank4/5/6 frame-indexed positive-rate scoped adversarial support; readiness `59% -> 60%`.
- G42-J: full 21-param local identifiability PASS.
- G42-C/C2/C3: SPD interior + boundary rank1–6 optimizer calibration; no readiness increment.

## Open scientific layers

- terminal G42-A bounded boundary-capable arbitrary-orientation PSD adversarial verdict;
- G42-R held-out optimizer replication;
- G42-BC response-blind basis/chart coverage audit;
- basis/chart/bound-coverage closure before any stronger PSD-family interpretation;
- broader non-Markovian/classically correlated comparator layers;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and any actual gravity-theory constitution gate.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, treating green CI as scientific PASS, post-hoc threshold/family/witness weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_60_PERCENT + THEORY_ESTABLISHED_0 + FINITE_COMPARATOR_SUPPORT_ONLY + G40_RTN_UNRESOLVED_OPTIMIZER_NONROBUSTNESS + G41A_SCOPED_HIGH_RANK_RATE_PASS + G42C2_C3_BOUNDARY_RANK1_TO_6_CALIBRATED + G42A_RUNNING + G42R_RUNNING + G42BC_QUEUED`.
