# RQIR-CG research ledger

This is the clean scientific authority ledger for `RQIR-Candidate-Gravity`. Legacy mixed-project ledgers are not scientific authority.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, funnel/gate discipline and general mathematical tools, but not imported physical assumptions, ansatz coefficients, results or desired conclusions. Green CI is never automatically scientific PASS.

## Canonical readiness

- Internal programme readiness: **59%**.
- Theory established: **0%**.
- The 58→59 increment is attributed only to terminal closure of corrected G37-A3.
- G40 implementation, eligibility, calibration and diagnostics do not by themselves raise readiness.

## Authoritative recent gate ledger

| Iteration | Gate | Run / head | Classification | Scope ceiling |
|---|---|---|---|---|
| Iter017 | G35 | `34697766107` / `fbc71768...` | `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT` | Finite additive independent MF. |
| Iter017R | G35-R | `34702384573` / `1b93cbf1...` | `HELDOUT_OPTIMIZER_ROBUSTNESS_PASS_K2_K3_K4` | Method robustness only. |
| Iter018A-C | G36-P/C/A | `34702575861`, `34703606707`, `34703779268` | shared-noise implementation/calibration/scoped support | One shared Gaussian classical mode. |
| Iter019C | G37-C2 | `34704249235` / `0852fe30...` | `POSITIVE_CONTROL_METHOD_CALIBRATED_TRULY_NESTED_MF_PLUS_SHARED` | Corrected finite combined family. |
| Iter019D | G37-A2 | `34704659119` / `823587d7...` | `NUMERICAL_OPTIMIZER_NESTING_VALIDITY_FAIL` | No physics verdict. |
| Iter019E | G37-A2-N | `34707889631` / `fd2eb2be...` | `EXACT_PARENT_EMBEDDING_VALID + SURROGATE_OBJECTIVE_REFINEMENT_FAIL` | Method diagnosis only. |
| Iter019F | G37-A3 | `34708041385` / `28d6fa63...` | `DERIVED_SCOPED_TRULY_NESTED_MF_PLUS_SHARED_BOUNDARY_PRESERVING_COMPARATOR_SUPPORT` | Finite corrected MF + one shared Markovian noise family. |
| Iter020A-C | G38-P/C/A | `34704060723`, `34704210632`, `34704373278` | OU implementation/calibration/scoped support | Three-time OU toy trajectory. |
| Iter021A | G39-P | `34704548004` | `MULTIMODE_CLASSICAL_NOISE_IMPLEMENTATION_VALIDATED` | Finite rank2/rank3 shared white noise. |
| Iter021B | G39-C | `34704727102` / `389b8723...` | `POSITIVE_CONTROL_METHOD_CALIBRATED_MULTIMODE_R2_R3` | Calibration only. |
| Iter021C | G39-A | `34704846612` / `8f011454...` | `NUMERICAL_OPTIMIZER_SEARCH_MISS / NESTING_VIOLATION` | No physics verdict. |
| Iter021D | G39-A-N | `34706674297` / `30a3f202...` | `RANK3_CONTAINMENT_VALID / ORIGINAL_SEARCH_MISS_DIAGNOSED` | Diagnostic only. |
| Iter021E | G39-A2 | `34707920572` / `da65199d...` | `DERIVED_SCOPED_MULTIMODE_RANK3_BOUNDARY_PRESERVING_COMPARATOR_SUPPORT` | Calibrated finite rank3 family. |
| Iter022A | G40-P | `34708162180` / `0297f33f...` | `STRICT_CLASSICAL_RTN_INFORMATION_BACKFLOW_IMPLEMENTATION_VALIDATED` | RTN implementation + fixed BLP witness. |
| Iter022B | G40-C | `34708292521` / `80107b2d...` | `PROTOCOL_DESIGN_FAIL / OUT_OF_FAMILY_POSITIVE_CONTROL + LHS_OPTIMIZER_MISS_ON_INVALID_CONTROL` | No calibration authority. |
| Iter022C | G40-C2-E | `34708494925` / `1b52b4c5...` | `STRICT_BLP_HIDDEN_CONTROL_ELIGIBILITY_PASS` | Eligibility only. |
| Iter022D | G40-C2 | `34708550582` / `2221f481...` | `POSITIVE_CONTROL_METHOD_CALIBRATED_STRICT_RTN` | Corrected eligible-control calibration only. |
| Iter022E | G40-C3 | `34708885346` / `af8f23f7...` | `FIXED_WITNESS_STRICT_BLP_FILTERED_SEARCH_CALIBRATED` | Search-rule calibration only. |
| Iter022F | G40-A | `34708971194` / `dab64180...` | `NEGATIVE_RESULT / G40A_FROZEN_SUPPORT_RULE_NOT_MET` | Finite fixed-witness BLP>0.02 RTN subset only; no general verdict. |
| Iter023A | G40-D | `34709706322` / `89dc08a4...` | `RUNNING / WITNESS_PANEL_DIAGNOSTIC` | Diagnostic only; cannot promote G40-A. |

## Decisive current results

### G37-A3

Run `34708041385`, aggregate `103594427577`, artifact `10302623647`, digest `sha256:5b50793fe136cc30ce7aa60fae05a7be60b7895794686a2f35a5ca82feb2de63`. All 8 lanes passed exact parent embedding, nesting, nonzero-gap and Sobol/LHS agreement. Durable note: `results/ITER019F_G37A3_TERMINAL.md`.

### G40-C3 calibration

Run `34708885346`, aggregate `103593923157`, artifact `10302603412`, digest `sha256:a2eda672b6c3a8e581a081b30e9d278619a0bf71356eb6587dbe8ac26f428845`. All 8 hidden-control filtered-search lanes passed recovery `<0.002` and fixed-witness BLP `>0.02`. This authorizes only use of that exact filtered search rule.

### G40-A terminal failed support rule

Run `34708971194`, aggregate `103594269913`, artifact `10302404036`, digest `sha256:5f299a2a08e228894b1cb52cb2059f4f1c961c387f0e30e0842307a1d8eafe52`. All lanes were structural, but shards 0/1 yielded no admissible fixed-witness strict candidate, shard 2 gave consistent scoped separation, and shard 3 violated frozen Sobol/LHS agreement. Durable note: `results/ITER022F_G40A_TERMINAL.md`. G40-A stays failed; no retroactive promotion.

### Active G40-D

Preregistered in `protocol/ITER023A_G40D_WITNESS_PANEL_DIAGNOSTIC.md`. Run `34709706322`, launch head `89dc08a4f31a76851e5b12c970aaf8b4b81eaa1b`. It tests fixed-witness/basis fragility on a four-element local witness panel while preserving the G40-A family, targets, optimizer and thresholds. It is diagnostic-only.

## Stable readiness rubric

Closed: independent scope discipline; coherent RCG-002 toy seed; finite MF K2/K3/K4 calibration/scoped comparator; one-mode shared Gaussian noise; corrected truly nested MF+shared finite comparator; OU three-time toy comparator; rank3 multimode shared white-noise comparator; strict RTN implementation and fixed-witness filtered-search calibration.

Not closed: rotation/witness-robust strict information-backflow comparator; higher-rank/general classical comparator; externally anchored observables/holdouts; continuum/full candidate-gravity dynamics; any constitution gate for an actual gravity theory.

## Claim locks

Never promote finite-family gaps to all-classical/semiclassical no-go claims. Green CI alone is not scientific PASS. Do not weaken frozen `0.002`, `1e-4`, BLP `0.02`, family, witness or target rules post hoc. Invalid G30/G31/G37/G39/G40 results stay invalid. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions.
