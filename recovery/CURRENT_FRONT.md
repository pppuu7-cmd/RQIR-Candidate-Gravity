# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active gates: `ITER027 / G43-A held-out multichart coverage` + `ITER028 / G44-P basis-invariant PSD trace-ball representation` + `ITER029 / G40-TM-C trace-metric RTN calibration`
Phase: `INDEPENDENT_RQIR_DERIVATION / BROAD_CLASSICAL_COMPARATOR_ATTACK`

## Canonical status

- Candidate-model/programme readiness: **61%**.
- Theory established: **0%**.
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Independent-from-QGR construction contract: **FROZEN**.
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`.
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**.

Readiness is programme completion, not a probability of physical correctness. `60% -> 61%` comes only from terminal closure of the scoped G42-A bounded boundary-PSD adversarial gate. Calibration, implementation, identifiability and coordinate-coverage gates do not raise readiness by themselves.

## Closed Iter026 authority

### G42-A bounded boundary-PSD adversarial — scoped support

Run `34712491707`, head `f7f48725a3d57398426f8ac9341a1d11b9cc591f`, aggregate `103605124717`, artifact `10304400253`, digest `sha256:002bea19226bd9b7283a08b36db3e72715762e074f10c40b7114d1e35ac3903c`.

All 8 lanes valid/admissible and all four frozen shard-pairs passed. Gaps Sobol/LHS: s0 `0.03700325124270668 / 0.03701733499594546`; s1 `0.1463716306513109 / 0.14637041941069723`; s2 `0.5276672796201998 / 0.5276813340757002`; s3 `0.8197294896504166 / 0.819101112669069`. Classification `DERIVED_SCOPED_BOUNDARY_PSD_COMPARATOR_SUPPORT`.

Scope ceiling: the frozen bounded 21-coordinate real-PSD 6x6 Markovian classical random-Hamiltonian Kossakowski chart only. This closure produced readiness `60% -> 61%`; it is not a universal classical/semiclassical no-go.

### G42-R held-out replication — PASS

Run `34712524241`, aggregate `103604804647`, artifact `10303143301`, digest `sha256:81fa588873316be4c243657cf7e2ac2f0aa08f092de05c969188c39d70c20f10`. All 12/12 new positive controls across effective ranks 1–6 passed; worst trace gap `3.9203174236860917e-07`, worst relative Kossakowski error `7.245639283979663e-06`, rank recovery 12/12. Classification `PSD_BOUNDARY_HELDOUT_CALIBRATION_REPLICATED`.

### G42-BC basis/chart audit — coverage limit

Run `34712857575`, aggregate `103606238137`, artifact `10304851327`, digest `sha256:e171c028ed31cd28fd19b1a1f1fd3a1dd91d9aa93a6be641bbfe580ad5b47e4c`. Local-basis covariance passed 24/24 at ~`1e-16`, but only 14/24 rotated controls remained inside the single frozen Cholesky box; 10/24 exited. Classification `BOUNDED_CHART_ROTATION_COVERAGE_LIMIT_FOUND`.

Durable terminal package: `results/ITER026_G42A_G42R_G42BC_TERMINAL.md`.

## Active gate 1 — Iter027 / G43-A finite multichart atlas

Protocol `protocol/ITER027_G43A_HELDOUT_MULTICHART_BASIS_COVERAGE.md`; launch/head `b69524b9fe8c33ff2f433f1d9dbc6ce54f8e4a06`; run `34715739668`.

36 response-blind lanes = ranks 1–6 × six held-out local basis rotations, using a five-chart atlas frozen before production. No RCG-002 target enters the gate.

Frozen classifier: all 36 covered -> `HELDOUT_MULTICHART_BASIS_COVERAGE_PASS`; validity/covariance clean but one or more uncovered -> `HELDOUT_MULTICHART_BASIS_COVERAGE_PARTIAL_LIMIT`; structural/covariance failure -> `MULTICHART_IMPLEMENTATION_OR_VALIDITY_FAIL`.

Current response-blind evidence already rules out full atlas PASS: rank-5/panel-3 is structurally valid and basis-covariant (`2.892896804343598e-16`) but uncovered by all five charts; best violation score `0.023092545915790297`. Therefore, if remaining lanes stay structurally/covariantly valid, terminal classification can be at most `HELDOUT_MULTICHART_BASIS_COVERAGE_PARTIAL_LIMIT`. No post-hoc chart may be added.

Latest sampled job state: at least 28 of the first 30 visible matrix jobs were terminal success, one in progress and one queued; GitHub API total matrix count is 36. Aggregate not yet terminal at this update.

## Active gate 2 — Iter028 / G44-P basis-invariant PSD trace-ball

Preregistration: `protocol/ITER028_G44P_BASIS_INVARIANT_TRACE_BALL_PSD.md`, commit `dceaba1889fa190b915c22f8ad57c63f81591207`.
Implementation: `scripts/iter028_g44p_basis_invariant_trace_ball_psd.py`, commit `a70f579a61639af6a8426e7c8bf3f01950aab463`.
Launch/head: `daf40fca9e5e6dc6f98b7673d5c2d34a4cc75552`.
Run: `34716135086`.

Frozen family is `C=A^2`, `A=A^T`, `||A||_F<=2`, equivalently real PSD `tr(C)<=4`. It is orthogonally basis-invariant. The complete old G42 Cholesky box is analytically nested because its maximum `||B||_F^2 = 3.51 < 4`.

24 response-blind representation/covariance lanes = ranks 1–6 × four new local-basis rotations. No RCG-002 target/result enters this pre-gate. PASS only authorizes a separately preregistered optimizer calibration in the exact same trace-ball family.

At this update 2/24 lanes are terminal and both have `scientific_support=true`: rank-1/panel-1 covariance error `3.4007321070588515e-16`, rank-1/panel-3 `3.5932216402041614e-16`; square-root reconstruction errors are ~`1e-16`, ranks preserved, and both rotated controls remain inside the trace ball. This is non-terminal evidence only.

## Active gate 3 — Iter029 / G40-TM-C trace-metric RTN calibration

Preregistration: `protocol/ITER029_G40TMC_TRACE_METRIC_CALIBRATION.md`, commit `466b649cf1929fefb3cbc28305115fb9afcb9934`.
Implementation: `scripts/iter029_g40tmc_trace_metric_rtn_calibration.py`, commit `423cc1c5bec5019c29a4d539273b16de31662d61`.
Launch/head: `aff54cae0954eb06771337ab315672a049450923`.
Run: `34716161178`.

This preserves the terminal G40-RC-D2 nonrobustness result and calibrates a different, preregistered optimizer directly on the scientific max trace-distance metric. Eight response-blind lanes = Sobol/LHS-like QMC designs (`sobol_powell`, `lhs_powell`) × four eligible positive controls. Each uses 24 starts, refines best four with bounded Powell, and requires strict axis-covariant BLP `>0.02` plus max trace gap `<0.002`. Hidden coordinates are never injected as starts; no RCG-002 target is used.

At this update all 8 lanes are queued behind the active G43/G44 work. PASS would authorize only a separately preregistered RTN adversarial gate and cannot raise readiness itself.

## Stable scientific closures

- G35: finite K2/K3/K4 additive independent measurement-feedback scoped support.
- G36: one shared Gaussian classical-noise scoped support.
- G37: corrected nested MF + shared-noise finite scoped support.
- G38: OU finite-correlation toy comparator support.
- G39: finite rank2/rank3 multimode shared white-noise support.
- G40: prior RTN adversarial support unresolved due persistent optimizer/objective nonrobustness; no RTN physics PASS.
- G41: rank4/5/6 frame-indexed positive-rate scoped adversarial support.
- G42-J: full 21-param local identifiability PASS.
- G42-C/C2/C3/R: bounded PSD optimizer calibration and held-out replication ranks 1–6.
- G42-A: scoped bounded boundary-PSD adversarial comparator support.
- G42-BC: basis covariance PASS plus single-chart rotation coverage limitation.

## Open scientific layers

- terminal G43-A finite-atlas coverage verdict;
- G44-P basis-invariant trace-ball representation/covariance, then only on PASS a separate optimizer calibration and later prospective adversarial gate;
- G40-TM-C robust trace-metric RTN optimization, then only on PASS a separate prospective RTN adversarial gate;
- broader non-Markovian/classically correlated comparator layers;
- externally anchored observables/holdouts;
- continuum/full candidate-gravity dynamics and any constitution gate for an actual gravity theory.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, all-classical/all-semiclassical no-go claims, green-CI-as-scientific-PASS, post-hoc threshold/family/witness/chart weakening, or importing QGR/KMQGB/RQIR physical assumptions/results.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_61_PERCENT + THEORY_ESTABLISHED_0 + G42A_SCOPED_BOUNDED_PSD_SUPPORT + G42BC_SINGLE_CHART_COVERAGE_LIMIT + G43A_PARTIAL_LIMIT_ALREADY_OBSERVED_PENDING_TERMINAL + G44P_RUNNING + G40TMC_QUEUED`.
