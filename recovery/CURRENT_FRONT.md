# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active iterations: `ITER019C / G37-C2` and `ITER021A / G39-P`
Phase: `INDEPENDENT_RQIR_DERIVATION / NESTED_COMBINED_AND_MULTIMODE_CLASSICAL_COMPARATORS`

## Canonical status

- Candidate-model/programme readiness: **57%**
- Theory established: **0%**
- Active seed: `RCG-002 Relational controlled-phase channel`
- Independent-from-QGR construction contract: **FROZEN**
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**

Readiness is an internal construction metric, not a probability that RCG-002 is physically correct. The increase from 56% to 57% records closure of the finite three-time OU colored-classical-noise trajectory comparator subgate. The strict information-backflow/non-Markovian layer, broader classical-channel families, externally anchored observables and continuum gravity dynamics remain open.

## Established scoped comparator results

### Measurement-feedback K=2/K=3/K=4

G34 run `34695835216` and G35 run `34697766107` prospectively calibrated and reran the finite additive independent single-axis Markovian measurement-feedback family. G35 aggregate job `103578278887`, artifact `10301201162`, digest `sha256:7e07e47311db7a279e2de47502d64a36cf31623c10c0da67f062ee8817bac199` passed all K=3/K=4 adversarial, nesting and admissibility rules. Classification: `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT`.

Held-out optimizer replication G35-R run `34702384573`, artifact `10300682102`, digest `sha256:5724519f32faf1e10d011e97d10df283fa6225facdfdb9ad8b14e82577557b13`, passed 18/18 new K2/K3/K4 controls. Classification: `HELDOUT_OPTIMIZER_ROBUSTNESS_PASS_K2_K3_K4`.

### Shared Gaussian classical noise

G36-P run `34702575861` validated the convex-mixture-of-product-unitaries implementation. G36-C run `34703606707`, artifact `10301561148`, calibrated 12/12 hidden controls. G36-A run `34703779268`, aggregate job `103580126265`, artifact `10301491686`, digest `sha256:2a75483c5ed8261e62466581b7a00046dd5d7a81ddffc5e49e38e819f81832ce`, retained nonzero RCG-002 gaps on all four shards under both calibrated methods. Classification: `DERIVED_SCOPED_SHARED_NOISE_CALIBRATED_COMPARATOR_SUPPORT`.

### OU colored finite-correlation trajectory comparator

G38-P run `34704060723`, aggregate job `103580959913`, artifact `10301152567`, digest `sha256:8642947c6b1c03689c35ed472ed994fe1cca2b3724c9320e07108dff4f4e0980`, passed 12/12 implementation checks. At one final time this OU channel depends only on integrated phase variance, so a single-time adversarial test would be redundant with G36.

G38-C run `34704210632`, aggregate job `103581251810`, artifact `10300863359`, digest `sha256:bd16f6d2fb356285d29725b2275fe3f1ca93b4bbb8287c2815e52a755f12cf2f`, calibrated 12/12 three-time trajectories at `T=[0.25,0.5,1.0]`.

G38-A run `34704373278`, workflow head `493da45d6a9b88e5cee32fca598fb657ea7a2ce4`, aggregate job `103581860728`, summary artifact `10301542445`, digest `sha256:ed9a0728c9288e696e6ed62fba176b848a46790c5ec7fe2faad9dbf04d26aa00`, passed the frozen four-shard × two-method toy-trajectory adversarial rule. Maximum trajectory-gap pairs (Sobol,LHS):
- shard 0: `(0.025545074758564972, 0.0255450797621222)`;
- shard 1: `(0.10046306945014429, 0.1004630806848435)`;
- shard 2: `(0.35877357179426705, 0.3587736163604044)`;
- shard 3: `(0.5996899264483135, 0.5996899101531477)`.

Classification: `DERIVED_SCOPED_OU_COLORED_TRAJECTORY_COMPARATOR_SUPPORT`. The target convention is only the controlled-phase toy trajectory `target(theta*T)`, not continuum gravity-time dynamics. This is not an information-backflow non-Markovian no-go.

## G37 protocol correction

Old G37-C run `34703787083` calibrated its own 18-dimensional family, but code inspection showed that family was **not** a mathematical superset of shared-noise-only: normalized K=2 measurement-feedback weights could not switch the MF component fully off.

Old G37-A run `34704008252`, aggregate job `103581352127`, artifact `10301497283`, digest `sha256:26926f7123ad1f69f4d13d17354c5e02a48a817cf6028f4850acc03a5422c0ee`, returned a nesting failure on shards 1 and 2. Because the family did not actually contain the declared parent, this is classified `PROTOCOL_DESIGN_FAIL / NONNESTED_COMBINED_FAMILY`, not a scientific FAIL of RCG-002. No threshold was weakened and the old output remains diagnostic only. Durable note: `results/ITER019B_G37A_NONNESTED_PROTOCOL_FAIL_TERMINAL.md`.

## Active authoritative gate — Iter019C / G37-C2

Run `34704249235`, launch head `0852fe30aa6bb7542dbb5ff4ec17fe8fd6eb55c1`.

Corrected family adds an explicit `lambda_MF in [0,1]`:
`L = L_MF(lambda_MF * theta) + L_shared`.
Therefore `lambda_MF=0` exactly contains shared-noise-only, while `cA=cB=0` exactly contains the K=2 measurement-feedback boundary.

Frozen calibration: 8 hidden in-family controls × Sobol/LHS = 16 positive-control lanes, including exact MF-only and shared-only boundaries, plus 4 independent admissibility lanes. Every positive-control trace distance must be `<0.002`; all admissibility thresholds must pass.

Latest checked live state: **19/20 scientific lanes terminal success (95%)**. Only `positive (sobol_lsq, shard 4)` — the MF-only boundary — remains in progress. Aggregate is not authorized until it terminates. Only a terminal G37-C2 scientific PASS may authorize a corrected nested-family RCG-002 adversarial gate.

## Active independent pre-gate — Iter021A / G39-P

Run `34704548004`, head `995f3c60b7648afe7a7d1a9b6ebb4c9e609dbf20`.

Twelve lanes validate a broader finite rank-2/rank-3 positive-Kossakowski classical white-noise decomposition `L=sum_k kappa_k D[F_k]`, with multiple shared classical modes and prospectively noncommuting local axes. Each stochastic trajectory still has Hamiltonian `H_A(t)⊗I + I⊗H_B(t)` and therefore factorizes into local unitaries; the averaged channel is correlated local-random-unitary.

Frozen checks cover TP/CP/PSD/trace, zero output negativity over prospectively sampled product inputs, mode-order invariance, exact single-mode reduction, and explicit noncommuting-axis richness. Latest checked state: **12/12 validation lanes in progress**; aggregate pending. G39-P is implementation/admissibility only and cannot support an RCG-002 claim by itself.

## Open layers

- corrected truly nested MF + shared-noise adversarial comparator: blocked pending G37-C2 PASS;
- multimode shared-classical-noise optimizer calibration/adversarial search: blocked pending G39-P PASS;
- higher-rank/general positive-Kossakowski classical-channel comparator: open beyond finite G39 rank;
- strict information-backflow/non-Markovian comparator layer: open;
- externally anchored observable/holdout programme: open;
- full candidate-gravity dynamics / continuum completion: open.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, any claim that all classical/semiclassical mediators are excluded, treating green CI as scientific PASS, post-hoc threshold/family weakening, retroactive promotion of G30/G31 minima, or importing physical assumptions/results from QGR/KMQGB/RQIR.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + MEASUREMENT_FEEDBACK_K2_K4_SCOPED_SUPPORT + SHARED_NOISE_SCOPED_SUPPORT + OU_COLORED_THREE_TIME_SCOPED_SUPPORT + G37_OLD_PROTOCOL_FAIL_RETAINED + G37C2_NESTED_CALIBRATION_95_PERCENT + G39P_MULTIMODE_IMPLEMENTATION_RUNNING`.
