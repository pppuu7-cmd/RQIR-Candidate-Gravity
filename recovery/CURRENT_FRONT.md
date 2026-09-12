# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active gates: `ITER019F / G37-A3` and `ITER022D / G40-C2`
Phase: `INDEPENDENT_RQIR_DERIVATION / BOUNDARY_PRESERVING_AND_STRICT_INFORMATION_BACKFLOW_COMPARATORS`

## Canonical status

- Candidate-model/programme readiness: **58%**
- Theory established: **0%**
- Active seed: `RCG-002 Relational controlled-phase channel`
- Independent-from-QGR construction contract: **FROZEN**
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**

Readiness is an internal construction metric, not a probability of physical correctness. The increase from 57% to 58% records terminal closure of G39-A2 only. Implementation, eligibility, or calibration gates alone do not raise readiness.

## Closed scoped comparator layers

- G35/G35-R: finite K2/K3/K4 additive independent measurement-feedback calibration, adversarial scoped support, and held-out optimizer robustness closed.
- G36-P/C/A: one shared Gaussian classical-noise implementation, calibration and scoped adversarial support closed.
- G38-P/C/A: OU finite-correlation three-time toy-trajectory implementation/calibration/scoped support closed. This is not strict information-backflow evidence.
- G39-P/C/A2: finite rank-2/rank-3 multimode shared classical white-noise implementation, calibration and boundary-preserving scoped adversarial support closed.

## G37 truly nested MF + one shared-noise family

G37-C2 run `34704249235` calibrated the corrected truly nested finite family. G37-A2 run `34704659119` failed optimizer nesting validity; G37-A2-N run `34707889631`, artifact `10302207524`, digest `sha256:fcd02773fc689b03a1564b1f04eeb8c5b28570e645b83aa644902c7242120e44`, proved exact shared-parent embedding to `1.11e-16` but exposed LSQ-surrogate refinement worsening trace distance by up to `0.003282498938826206`. Classification: `EXACT_PARENT_EMBEDDING_VALID + SURROGATE_OBJECTIVE_REFINEMENT_FAIL`, not physics.

### Active G37-A3 boundary-preserving repair

Run `34708041385`, launch head `28d6fa6343dabb068aba5a462f6026d8ec1a6a4f`.

The original 19D Sobol/LHS combined search is retained. Exact G36 shared-only and G34 K2-MF-only parent points remain legal candidates regardless of LSQ refinement; all candidates are ranked by final trace distance. Frozen rules: both parent embeddings exact `<=1e-10`, combined best no worse than best parent by `1e-10`, nonzero gap `>1e-4`, Sobol/LHS agreement `<=0.002`.

Latest checked state: **2/8 terminal success = 25%**, six lanes still in progress. This is the main current physics bottleneck.

## G39 rank-3 multimode shared classical-noise family — CLOSED SCOPED GATE

Original G39-A run `34704846612` remains `NUMERICAL_OPTIMIZER_SEARCH_MISS / NESTING_VIOLATION`. G39-A-N run `34706674297` proved exact rank2→rank3 containment and diagnosed the miss.

G39-A2 repaired run `34707920572`, head `da65199d56e1cb1be5bff232f97230611dd9ef2e`, aggregate job `103592063859`, summary artifact `10302591508`, digest `sha256:bf8ac5713ec242ab494e501dde0d56f34db362b6d2a6e58b6c5a576dfac9557d`, passed all frozen rules on all 4 shards × 2 methods.

Rank-3 gaps (Sobol,LHS):
- shard 0: `(0.025499011417598586, 0.025499051947386945)`;
- shard 1: `(0.10036160336652522, 0.10036159991946002)`;
- shard 2: `(0.35873703855020184, 0.3587370386123476)`;
- shard 3: `(0.5982327597417393, 0.598232759851799)`.

Classification: `DERIVED_SCOPED_MULTIMODE_RANK3_BOUNDARY_PRESERVING_COMPARATOR_SUPPORT`. Scope is only the calibrated finite rank-3 multimode shared classical white-noise family.

## G40 strict classical information-backflow layer

### G40-P — implementation/witness PASS

Run `34708162180`, head `0297f33faabeede29e0cb81c3161b278c18be9c0`, aggregate `103592018677`, artifact `10302078122`, digest `sha256:720bc3d4a9c9841d1fd84bd7c00339fc6cbc9d6a37f9ba2bc24b7c8fd702e1c1`.

Four hidden-classical RTN lanes passed strict BLP/admissibility checks. Minimum strong-control BLP `0.5923274153651977`, maximum weak-control BLP `0.0`, TP `4.44e-16`, minimum Choi eigenvalue `-3.73e-16`, product-unitary factorization error `2.22e-16`, output negativity `0`. Classification: `STRICT_CLASSICAL_RTN_INFORMATION_BACKFLOW_IMPLEMENTATION_VALIDATED`. No RCG-002 inference.

### G40-C — terminal protocol-design failure

Run `34708292521`, head `80107b2d65c154d4e6a0cc52a2c1fffd8408dd8d`, aggregate `103592442138`, summary artifact `10302841233`, digest `sha256:d9a7f85a11c0178b2bd77b4700f43af4411ef7f2e654914197c4228941ce29c3`.

Eight lanes were structural, but frozen control shard 3 itself had BLP `~0.0090952917864 < 0.02`, so it was outside the declared strict-BLP subset. Sobol recovered that invalid target essentially exactly (`gap 6.97e-14`); LHS on the same invalid target additionally missed the basin (`gap 0.2337600986`). Classification: `PROTOCOL_DESIGN_FAIL / OUT_OF_FAMILY_POSITIVE_CONTROL + LHS_OPTIMIZER_MISS_ON_INVALID_CONTROL`. Durable note: `results/ITER022B_G40C_PROTOCOL_FAIL_TERMINAL.md`. No threshold was changed and no old successful lane is promoted.

### G40-C2-E — eligibility PASS

Run `34708494925`, head `1b52b4c50a4a7840109a92a4d593a9873afd7973`, aggregate job `103592871261`, summary artifact `10302253344`, digest `sha256:8beb6836a6a846243df916616ed5234cdf22935f51e7447ce13f8eb30739cf24`.

Before any new optimization, all four prospectively frozen targets were shown to lie inside the same bounds and have BLP `>0.02`: shard 0 `0.022161811061064185`, shard 1 `0.07584060292605893`, shard 2 `0.7778334797535692`, new shard 3 `0.16064058660706515`. This is eligibility only.

### Active G40-C2 corrected calibration

Run `34708550582`, launch head `2221f481e1ac98dc9a1f16ea8e4c81411d6ba834`.

Same G40-C family, bounds, 4 times, 6 probes, Sobol/LHS starts, 16 starts, top-4 LSQ refinement, max_nfev 600, recovery `<0.002`, recovered BLP `>0.02`. Controls 0/1/2 unchanged; only control 3 is the separately prevalidated eligible target. Latest checked state: **8/8 jobs queued**, because six G37-A3 heavy lanes currently occupy the available runner pool. A strict-BLP RCG-002 adversarial gate remains forbidden until terminal G40-C2 PASS.

## Open layers

- terminal G37-A3 classification;
- terminal G40-C2 optimizer calibration, then a separate prospective strict-BLP RCG-002 adversarial trajectory gate only if PASS;
- higher-rank/general positive-Kossakowski classical comparator beyond finite G39 rank;
- externally anchored observable/holdout programme;
- continuum/full candidate-gravity dynamics.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, any claim that all classical/semiclassical mediators are excluded, treating green CI as scientific PASS, post-hoc threshold/family weakening, or retroactive promotion of invalid G30/G31/G37/G39/G40 minima or controls.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + READINESS_58_PERCENT + THEORY_ESTABLISHED_0 + FINITE_COMPARATOR_SUPPORT_ONLY + G37A3_25_PERCENT + G39A2_SCOPED_RANK3_SUPPORT + G40P_STRICT_BLP_IMPLEMENTATION_PASS + G40C_PROTOCOL_FAIL_RETAINED + G40C2E_ELIGIBILITY_PASS + G40C2_QUEUED`.
