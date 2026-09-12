# RQIR-CG research ledger

This file is the clean authority ledger for `RQIR-Candidate-Gravity` only. The pre-existing `research_log/RESEARCH_ACTIVITY_LEDGER.md` contains legacy material from another research line and must not be used as scientific evidence for RQIR-CG.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, gate discipline and mathematical tools, but not imported physical assumptions, ansatz coefficients or desired conclusions.

## Latest authoritative results

| Iteration | Gate | Run / head | Classification | Result ceiling |
|---|---|---|---|---|
| Iter010 | G28 full-Bloch comparator audit | run `34692403874`, head `3d8d3f969a22c22c1526b00f42377c2d41f87a04` | `DERIVED_SCOPED_NEGATIVE_COMPARATOR_RESULT` | Finite single-axis Markovian family only. |
| Iter011 | G29 robustness suite | run `34694101699`, head `c4c6f0d35e4e57a2105facafee2bdddc8036a52f` | `DERIVED_SCOPED_ROBUSTNESS_SUPPORT` | 24/24 structural valid/support in finite single-axis family. |
| Iter012 | G30 additive multi-channel comparator | run `34694264478`, head `fa9be36b422b84614b03f96de7c37660059f2d74` | `FINITE_SEARCH_DIAGNOSTIC` | Historical K=2/K=3 gaps cannot be treated as nearest distances after later calibration failure. |
| Iter013 | G31 global-search calibration | run `34695076098`, head `f32ecf1949f1e7d6c577b201b73c517d4605fdb7` | `SCIENTIFIC_CALIBRATION_FAIL / GLOBAL_OPTIMIZER_NOT_VALIDATED` | Positive K=2 recovery failed; adversarial minima diagnostic only. |
| Iter014 | G32 positive-control optimizer diagnosis | run `34695441883`, head `ea54a3ae9694366c13b775af44d46833` | `POSITIVE_CONTROL_OPTIMIZER_FAIL / LOCAL_BASIN_GEOMETRY_OR_CONDITIONING` | Exact representability/plumbing pass; direct trace-distance search unreliable. |
| Iter014B | G32-J positive-control Jacobian | run `34695478444`, head `706245fa183845556aa020bc99d2a4d86e4e3060` | `FULL_LOCAL_RANK / STRONGLY_ILL_CONDITIONED_DIAGNOSTIC` | Rank 11/11; condition number up to ~4034. |
| Iter015 | G33 smooth positive-control calibration | run `34695662002`, head `d15d633f58fa63d378a85d6e5409c4bb0735a97e` | `POSITIVE_CONTROL_METHOD_CALIBRATED_K2` | Sobol-LSQ and LHS-LSQ each recover all four hidden K=2 targets far below frozen 0.002 tolerance. |
| Iter016 | G34 calibrated multichannel comparator | run `34695835216`, head `09d729764ca38a0d83f11b81dc59f157cd0cb734` | `DERIVED_SCOPED_K2_CALIBRATED_COMPARATOR_SUPPORT + POSITIVE_CONTROL_METHOD_CALIBRATED_K3_K4` | K=2 prospective gaps supported inside finite additive independent-channel family; K=3/K=4 adversarial reruns newly authorized. |
| Iter017 | G35 calibrated K=3/K=4 comparator | run `34697766107`, head `fbc71768da3cec0d6ea5a8cbb755a29036b16726` | `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT` | 24/24 structural valid; K=3 and K=4 each pass four-shard nonzero-gap, cross-method, nesting and admissibility gates. Same finite additive independent-channel family only. |
| Iter018A | G36-P shared-classical-noise implementation pre-gate | run `34702575861`, head `270a26300117aeebe23af126dd4e6c53c96cf3f9` | `CLASSICAL_SHARED_NOISE_IMPLEMENTATION_VALIDATED` | Implementation/provenance only; 12/12 frozen checks pass. No RCG-002 adversarial claim. |
| Iter018B | G36-C shared-noise optimizer calibration | run `34703606707`, head `95335aa32e92dcd1cc76762cd6fd3717754a1057` | `RUNNING / FROZEN_PROSPECTIVE_CALIBRATION` | Six hidden in-family targets × Sobol/LHS. Frozen recovery `<0.002`; no adversarial interpretation until terminal calibration. |

## Iter017 / G35 terminal aggregate

Aggregate job `103578278887`, aggregate artifact `10301201162`, digest `sha256:7e07e47311db7a279e2de47502d64a36cf31623c10c0da67f062ee8817bac199`.

All 24 required artifacts were structurally valid. Frozen gates were unchanged after inspection. K=3 and K=4 each passed all four shards for both calibrated methods, with every gap `>1e-4`, Sobol/LHS agreement `<=0.002`, and K-to-K nesting sanity within the fixed `0.002` slack. Admissibility was 4/4 for K=3 and 4/4 for K=4.

K=3 gap pairs (Sobol,LHS):

- shard 0 `(0.02607083500239983, 0.02607082455460381)`;
- shard 1 `(0.10462705021070003, 0.1046280224077526)`;
- shard 2 `(0.4030775755359582, 0.4030776193040029)`;
- shard 3 `(0.5324536720244457, 0.5324529974645373)`.

K=4 gap pairs:

- shard 0 `(0.026070843192707152, 0.026070840339822314)`;
- shard 1 `(0.1046282559394234, 0.10462763627815973)`;
- shard 2 `(0.40307761916005946, 0.40307752304763794)`;
- shard 3 `(0.5324520837003446, 0.5324521216247678)`.

Classification: `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT`. This remains a scoped result for the finite additive independent single-axis Markovian measurement-feedback GKSL comparator family only. It is not a general no-go theorem.

Durable result note: `results/ITER017_G35_CALIBRATED_K3K4_TERMINAL.md`, commit `ad1a6bf689740f3af2997df601a516b3b0a6334c`.

## Iter018A / G36-P

Run `34702575861`, head `270a26300117aeebe23af126dd4e6c53c96cf3f9`, aggregate job `103576905242`, aggregate artifact `10300760790`, digest `sha256:3a03b7462ccf026c6cc7cdef88fbe0c9f4710c3040f467a5caf9fa5e3e4d228d`.

All 12 prospectively frozen implementation lanes passed. Classification: `CLASSICAL_SHARED_NOISE_IMPLEMENTATION_VALIDATED`. The validated ingredient is shared Gaussian Hamiltonian noise represented as a convex mixture of product unitaries; this is deliberately narrower than an arbitrary nonlocal Lindblad channel.

## Active frontier — Iter018B / G36-C

Run `34703606707`, launch head `95335aa32e92dcd1cc76762cd6fd3717754a1057`.

G36-C is a prospective positive-control optimizer calibration for the finite shared-classical-noise comparator before any RCG-002 adversarial use. Twelve lanes cover six hidden in-family targets with two independent global designs, Sobol-LSQ and Latin-hypercube-LSQ. Hidden coordinates are not used as optimizer starts. Frozen scientific recovery is final trace distance `<0.002` on every lane. Structural/nonfinite failure is separated from scientific calibration failure.

Only terminal G36-C PASS may authorize the separate RCG-002 shared-noise adversarial comparator gate. A G36-C failure must be retained and diagnosed without weakening the threshold post hoc.

In parallel, G35-R run `34702384573` remains methodology robustness only and cannot change the frozen G35 physics verdict.

## Stable readiness rubric

- independent scope/claim discipline: closed
- weak-field coherent candidate construction: closed at toy-channel level
- basis/rotation robustness of finite comparator: closed
- CPTP/PSD and numerical robustness of finite comparator: closed at tested layers
- exact K=2 in-family representability/plumbing: closed
- K=2 smooth optimizer calibration: closed
- calibrated K=2 adversarial comparator rerun: closed
- K=3/K=4 optimizer calibration: closed
- calibrated K=3/K=4 adversarial comparator rerun: **closed G35**
- shared-classical-noise implementation/provenance: closed at pre-gate level
- shared-classical-noise optimizer calibration: **active G36-C**
- correlated/shared classical-noise comparator against RCG-002: blocked pending G36-C terminal PASS
- non-Markovian comparator layer: open
- externally anchored observable/holdout programme: open
- full candidate-gravity dynamics / continuum completion: open

Current internal programme readiness: **55%**. This is a construction/readiness metric, not a probability of physical correctness.

## Claim locks

Do not promote finite-family gaps to claims that all semiclassical gravity, all classical mediators, or all alternatives to quantum gravity are excluded. Do not use green CI as a scientific verdict. Do not weaken the frozen `2e-3` calibration/agreement criterion or `1e-4` nonzero-gap criterion after seeing results. Do not reuse G30/G31 adversarial minima as authority. Do not import physical assumptions or desired conclusions from QGR/KMQGB/RQIR.
