# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active gate: `ITER027 / G43-A held-out response-blind multichart basis coverage`
Phase: `INDEPENDENT_RQIR_DERIVATION / BROAD_CLASSICAL_COMPARATOR_ATTACK`

## Canonical status

- Candidate-model/programme readiness: **61%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

Readiness is programme completion, not a probability of physical correctness. `60% -> 61%` comes only from terminal closure of the scoped G42-A bounded boundary-PSD adversarial gate. Calibration/diagnostic/chart-coverage gates do not raise readiness by themselves.

## Newly terminal — Iter026 package

### G42-A bounded boundary-PSD adversarial — scoped support

Run `34712491707`, head `f7f48725a3d57398426f8ac9341a1d11b9cc591f`, aggregate job `103605124717`, artifact `10304400253`, digest `sha256:002bea19226bd9b7283a08b36db3e72715762e074f10c40b7114d1e35ac3903c`.

All 8 lanes were structurally valid/admissible. Frozen all-shard rule passed:

- shard 0 gaps `0.03700325124270668 / 0.03701733499594546`, method difference `1.4083753238774976e-05`;
- shard 1 `0.1463716306513109 / 0.14637041941069723`, difference `1.2112406136688403e-06`;
- shard 2 `0.5276672796201998 / 0.5276813340757002`, difference `1.4054455500400742e-05`;
- shard 3 `0.8197294896504166 / 0.819101112669069`, difference `0.0006283769813475448`.

Classification: `DERIVED_SCOPED_BOUNDARY_PSD_COMPARATOR_SUPPORT`.
Scope: bounded 21-coordinate real-PSD 6x6 Markovian classical random-Hamiltonian Kossakowski family only. Not a full-PSD theorem and not a universal classical/semiclassical no-go.

### G42-R held-out calibration replication — PASS

Run `34712524241`, head `3b53451c192c8bcaedd39105d1c9b9b3ae3aa6e6`, aggregate job `103604804647`, artifact `10303143301`, digest `sha256:81fa588873316be4c243657cf7e2ac2f0aa08f092de05c969188c39d70c20f10`.

All 12/12 held-out controls across effective ranks 1–6 passed; worst trace gap `3.9203174236860917e-07`, worst relative Kossakowski error `7.245639283979663e-06`, rank recovery 12/12. Classification `PSD_BOUNDARY_HELDOUT_CALIBRATION_REPLICATED`. Method robustness only.

### G42-BC response-blind basis/chart audit — coverage limit

Run `34712857575`, head `11b5a0604ada235a4504990966b89f8f89857471`, aggregate job `103606238137`, artifact `10304851327`, digest `sha256:e171c028ed31cd28fd19b1a1f1fd3a1dd91d9aa93a6be641bbfe580ad5b47e4c`.

All 24/24 local-basis covariance checks passed with generator errors around `4.8e-16`, but only 14/24 rotated controls remained in the frozen single Cholesky box; 10/24 exited. Classification `BOUNDED_CHART_ROTATION_COVERAGE_LIMIT_FOUND`.

This does not alter the bounded-chart G42-A number, but blocks basis-invariant interpretation for the entire mathematical real-PSD family.

Durable terminal note: `results/ITER026_G42A_G42R_G42BC_TERMINAL.md`.

## Active frontier — Iter027 / G43-A

Protocol: `protocol/ITER027_G43A_HELDOUT_MULTICHART_BASIS_COVERAGE.md`.
Preregistration commit: `cb289ca11da5885e5bf4a04bcbbd1a9b4f44c7e7`.
Implementation commit: `67329b2397792b351817f7effa06ed35fe200a30`.
Workflow commit: `8e2e8ea076fa85b4e184ff6d6a342268f252a9c4`.
Launch/head: `b69524b9fe8c33ff2f433f1d9dbc6ce54f8e4a06`.
Run: `34715739668`.

G43-A is response-blind. It uses six new hidden positive controls (ranks 1–6), six held-out local basis rotations and a five-chart atlas frozen before production: identity plus the four G42-BC basis charts. Total: 36 independent lanes.

Frozen classification:

- `HELDOUT_MULTICHART_BASIS_COVERAGE_PASS` iff all 36 validity/covariance checks pass and all 36 held-out rotated controls are covered by at least one frozen chart;
- `HELDOUT_MULTICHART_BASIS_COVERAGE_PARTIAL_LIMIT` iff validity/covariance passes but one or more lanes remain uncovered;
- `MULTICHART_IMPLEMENTATION_OR_VALIDITY_FAIL` for structural/covariance failure.

No chart, bound or threshold may be added/changed after seeing production results. PASS would still be finite-panel calibration only and would not authorize full-PSD or basis-invariant physics claims by itself.

## Stable scientific closures

- G35: finite K2/K3/K4 additive independent measurement-feedback scoped support.
- G36: one shared Gaussian classical-noise scoped support.
- G37: corrected nested MF + shared-noise finite scoped support.
- G38: OU finite-correlation toy comparator support.
- G39: finite rank2/rank3 multimode shared white-noise support.
- G40: RTN calibration succeeded but adversarial support unresolved due persistent optimizer/objective nonrobustness; no RTN physics PASS.
- G41: rank4/5/6 frame-indexed positive-rate scoped adversarial support.
- G42-J: full 21-param local identifiability PASS.
- G42-C/C2/C3/R: bounded PSD optimizer calibration and held-out replication across effective ranks 1–6.
- G42-A: scoped bounded boundary-PSD adversarial comparator support.
- G42-BC: implementation covariance PASS plus single-chart rotation-coverage limitation.

## Open scientific layers

- finite-atlas held-out basis/chart coverage (G43-A);
- genuinely basis-invariant/unbounded PSD parameterization if G43-A leaves uncovered lanes;
- robust RTN trace-metric-aligned optimization;
- broader non-Markovian/classically correlated comparator layers;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and any actual gravity-theory constitution gate.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, treating green CI as scientific PASS, post-hoc threshold/family/witness/chart weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_61_PERCENT + THEORY_ESTABLISHED_0 + FINITE_COMPARATOR_SUPPORT_ONLY + G40_RTN_UNRESOLVED_OPTIMIZER_NONROBUSTNESS + G42A_SCOPED_BOUNDED_PSD_SUPPORT + G42BC_SINGLE_CHART_COVERAGE_LIMIT + G43A_RUNNING_OR_QUEUED`.
