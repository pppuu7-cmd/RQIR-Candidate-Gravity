# RQIR-CG research ledger

This is the clean scientific authority ledger for `RQIR-Candidate-Gravity`. Legacy mixed-project ledgers are not scientific authority.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, funnel/gate discipline and general mathematical tools, but not imported physical assumptions, ansatz coefficients, results or desired conclusions. Green CI is never automatically scientific PASS.

## Canonical readiness

- Internal programme readiness: **58%**.
- Theory established: **0%**.
- Readiness is a construction metric, not a probability of physical correctness.
- The 57→58 increase is attributed only to terminal closure of G39-A2. Implementation/eligibility/calibration gates alone do not raise readiness.

## Authoritative result table

| Iteration | Gate | Run / head | Classification | Ceiling |
|---|---|---|---|---|
| Iter010 | G28 | `34692403874` / `3d8d3f969a22c22c1526b00f42377c2d41f87a04` | `DERIVED_SCOPED_NEGATIVE_COMPARATOR_RESULT` | Finite single-axis Markovian family. |
| Iter011 | G29 | `34694101699` / `c4c6f0d35e4e57a2105facafee2bdddc8036a52f` | `DERIVED_SCOPED_ROBUSTNESS_SUPPORT` | Same finite family. |
| Iter012 | G30 | `34694264478` / `fa9be36b422b84614b03f96de7c37660059f2d74` | `FINITE_SEARCH_DIAGNOSTIC` | Historical minima non-authoritative. |
| Iter013 | G31 | `34695076098` / `f32ecf1949f1e7d6c577b201b73c517d4605fdb7` | `SCIENTIFIC_CALIBRATION_FAIL / GLOBAL_OPTIMIZER_NOT_VALIDATED` | Diagnostic only. |
| Iter014 | G32 | `34695441883` | `POSITIVE_CONTROL_OPTIMIZER_FAIL / LOCAL_BASIN_OR_OBJECTIVE_GEOMETRY_FAIL` | Direct optimization unreliable. |
| Iter014B | G32-J | `34695478444` / `706245fa183845556aa020bc99d2a4d86e4e3060` | `FULL_LOCAL_RANK / STRONGLY_ILL_CONDITIONED_DIAGNOSTIC` | Rank full; strong conditioning. |
| Iter015 | G33 | `34695662002` / `d15d633f58fa63d378a85d6e5409c4bb0735a97e` | `POSITIVE_CONTROL_METHOD_CALIBRATED_K2` | Sobol/LHS method authority. |
| Iter016 | G34 | `34695835216` / `09d729764ca38a0d83f11b81dc59f157cd0cb734` | `DERIVED_SCOPED_K2_CALIBRATED_COMPARATOR_SUPPORT + POSITIVE_CONTROL_METHOD_CALIBRATED_K3_K4` | Finite additive independent MF family. |
| Iter017 | G35 | `34697766107` / `fbc71768da3cec0d6ea5a8cbb755a29036b16726` | `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT` | K3/K4 finite additive independent MF. |
| Iter017R | G35-R | `34702384573` / `1b93cbf14b4705ae2699f559523d1c1b1ae28be5` | `HELDOUT_OPTIMIZER_ROBUSTNESS_PASS_K2_K3_K4` | Method robustness. |
| Iter018A | G36-P | `34702575861` / `270a26300117aeebe23af126dd4e6c53c96cf3f9` | `CLASSICAL_SHARED_NOISE_IMPLEMENTATION_VALIDATED` | One shared Gaussian mode. |
| Iter018B | G36-C | `34703606707` | `POSITIVE_CONTROL_METHOD_CALIBRATED_SHARED_NOISE` | Calibration only. |
| Iter018C | G36-A | `34703779268` | `DERIVED_SCOPED_SHARED_NOISE_CALIBRATED_COMPARATOR_SUPPORT` | One shared Gaussian mode. |
| Iter019A | G37-C old | `34703787083` | `CALIBRATED_OWN_FAMILY / LATER_FOUND_NONNESTED` | Not shared-only superset. |
| Iter019B | G37-A old | `34704008252` | `PROTOCOL_DESIGN_FAIL / NONNESTED_COMBINED_FAMILY` | Diagnostic only. |
| Iter019C | G37-C2 | `34704249235` / `0852fe30aa6bb7542dbb5ff4ec17fe8fd6eb55c1` | `POSITIVE_CONTROL_METHOD_CALIBRATED_TRULY_NESTED_MF_PLUS_SHARED` | Corrected finite combined family. |
| Iter019D | G37-A2 | `34704659119` / `823587d7cea5fb0f673487edeb5f7f9e730ad129` | `NUMERICAL_OPTIMIZER_NESTING_VALIDITY_FAIL` | No physics verdict. |
| Iter019E | G37-A2-N | `34707889631` / `fd2eb2be2f7fc7184f83f6e629db5810bad7c317` | `EXACT_PARENT_EMBEDDING_VALID + SURROGATE_OBJECTIVE_REFINEMENT_FAIL` | Method diagnosis only. |
| Iter019F | G37-A3 | `34708041385` / `28d6fa6343dabb068aba5a462f6026d8ec1a6a4f` | `RUNNING / BOUNDARY_PRESERVING_REPAIR` | Prospective repaired combined adversarial gate. |
| Iter020A | G38-P | `34704060723` | `OU_COLORED_CLASSICAL_NOISE_IMPLEMENTATION_VALIDATED` | OU finite-correlation noise. |
| Iter020B | G38-C | `34704210632` | `POSITIVE_CONTROL_METHOD_CALIBRATED_OU_COLORED_TRAJECTORY` | Three-time calibration. |
| Iter020C | G38-A | `34704373278` | `DERIVED_SCOPED_OU_COLORED_TRAJECTORY_COMPARATOR_SUPPORT` | Three-time toy trajectory only. |
| Iter021A | G39-P | `34704548004` | `MULTIMODE_CLASSICAL_NOISE_IMPLEMENTATION_VALIDATED` | Finite rank2/rank3 shared white noise. |
| Iter021B | G39-C | `34704727102` / `389b8723f81c8e94f864fcf1b82de4503c329c7e` | `POSITIVE_CONTROL_METHOD_CALIBRATED_MULTIMODE_R2_R3` | Calibration only. |
| Iter021C | G39-A | `34704846612` / `8f011454324652076876b9b79821e40155d8c573` | `NUMERICAL_OPTIMIZER_SEARCH_MISS / NESTING_VIOLATION` | No physics verdict. |
| Iter021D | G39-A-N | `34706674297` / `30a3f202d21726f271cd874dc1afc3d27d54de14` | `RANK3_CONTAINMENT_VALID / ORIGINAL_SEARCH_MISS_DIAGNOSED` | Diagnostic only. |
| Iter021E | G39-A2 | `34707920572` / `da65199d56e1cb1be5bff232f97230611dd9ef2e` | `DERIVED_SCOPED_MULTIMODE_RANK3_BOUNDARY_PRESERVING_COMPARATOR_SUPPORT` | Calibrated finite rank3 multimode shared white-noise family only. |
| Iter022A | G40-P | `34708162180` / `0297f33faabeede29e0cb81c3161b278c18be9c0` | `STRICT_CLASSICAL_RTN_INFORMATION_BACKFLOW_IMPLEMENTATION_VALIDATED` | RTN implementation + BLP witness only. |
| Iter022B | G40-C | `34708292521` / `80107b2d65c154d4e6a0cc52a2c1fffd8408dd8d` | `PROTOCOL_DESIGN_FAIL / OUT_OF_FAMILY_POSITIVE_CONTROL + LHS_OPTIMIZER_MISS_ON_INVALID_CONTROL` | No calibration authority. |
| Iter022C | G40-C2-E | `34708494925` / `1b52b4c50a4a7840109a92a4d593a9873afd7973` | `STRICT_BLP_HIDDEN_CONTROL_ELIGIBILITY_PASS` | Eligibility only. |
| Iter022D | G40-C2 | `34708550582` / `2221f481e1ac98dc9a1f16ea8e4c81411d6ba834` | `QUEUED / CORRECTED_POSITIVE_CONTROL_CALIBRATION` | No RCG-002 inference unless terminal PASS. |

## Decisive recent results

### G39-A2 terminal scoped PASS

Run `34707920572`, aggregate `103592063859`, artifact `10302591508`, digest `sha256:bf8ac5713ec242ab494e501dde0d56f34db362b6d2a6e58b6c5a576dfac9557d`. All 4 shards × 2 methods passed exact embedding, rank3<=rank2 nesting, nonzero gap `>1e-4`, Sobol/LHS agreement `<=0.002`, and parent-method agreement. Rank-3 gaps (Sobol,LHS): `(0.0254990114,0.0254990519)`, `(0.1003616034,0.1003615999)`, `(0.3587370386,0.3587370386)`, `(0.5982327597,0.5982327599)`. Durable note: `results/ITER021E_G39A2_TERMINAL.md`.

### G37-A2-N diagnosis and active G37-A3

G37-A2-N run `34707889631`, artifact `10302207524`, digest `sha256:fcd02773fc689b03a1564b1f04eeb8c5b28570e645b83aa644902c7242120e44`: exact shared-parent embedding agreement to `1.11e-16`, but LSQ surrogate refinement can worsen final trace distance by `0.003282498938826206`. G37-A3 therefore preserves exact shared and K2-MF parent candidates and ranks all candidates by trace distance. Latest checked state: **2/8 terminal, 6 in progress = 25%**.

### G40 strict information-backflow branch

G40-P run `34708162180`, aggregate `103592018677`, artifact `10302078122`, digest `sha256:720bc3d4a9c9841d1fd84bd7c00339fc6cbc9d6a37f9ba2bc24b7c8fd702e1c1`: implementation/witness PASS. Strong hidden-classical RTN controls have clear BLP revival while weak controls have zero revival; CPTP/factorization/negativity audits pass.

G40-C run `34708292521`, aggregate `103592442138`, artifact `10302841233`, digest `sha256:d9a7f85a11c0178b2bd77b4700f43af4411ef7f2e654914197c4228941ce29c3`: protocol-design FAIL because frozen target shard3 itself had BLP `~0.0090953 < 0.02`. Sobol recovered this invalid target nearly exactly; LHS also suffered a basin miss on it. Durable note: `results/ITER022B_G40C_PROTOCOL_FAIL_TERMINAL.md`. No threshold weakening and no retroactive lane promotion.

G40-C2-E run `34708494925`, aggregate `103592871261`, artifact `10302253344`, digest `sha256:8beb6836a6a846243df916616ed5234cdf22935f51e7447ce13f8eb30739cf24`: eligibility PASS before optimization. Target BLP values are shard0 `0.0221618111`, shard1 `0.0758406029`, shard2 `0.7778334798`, new shard3 `0.1606405866`; all are in unchanged bounds and >`0.02`. Durable note: `results/ITER022C_G40C2E_TERMINAL.md`.

G40-C2 run `34708550582` is a separately preregistered corrected calibration using the same optimizer/bounds/times/probes/thresholds; controls0/1/2 are unchanged and only control3 is the prevalidated replacement. Latest checked state: **8/8 jobs queued** behind active G37-A3 runner use. A strict-BLP RCG-002 adversarial gate is forbidden until terminal G40-C2 PASS.

## Stable readiness rubric

Closed: independent scope discipline; coherent RCG-002 toy seed; finite MF K2/K3/K4 calibration and scoped comparator; one-mode shared Gaussian classical noise; OU three-time toy trajectory; rank3 multimode shared classical white-noise comparator; strict hidden-classical RTN implementation plus BLP witness.

Not closed: repaired G37 combined adversarial classifier; corrected G40-C2 RTN optimizer calibration and any subsequent RCG-002 strict-BLP adversarial classifier; higher-rank/general classical comparator; externally anchored observables/holdouts; continuum/full candidate-gravity dynamics.

## Claim locks

Never promote finite-family gaps to all-classical/semiclassical no-go claims. Green CI alone is not scientific PASS. Do not weaken frozen `0.002` calibration/agreement or `1e-4` nonzero-gap rules post hoc. Invalid G30/G31/G37/G39/G40 minima/controls stay invalid. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions.
