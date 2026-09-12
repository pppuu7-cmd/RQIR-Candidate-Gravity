# RQIR-CG research ledger

This is the clean scientific authority ledger for `RQIR-Candidate-Gravity`. Legacy mixed-project ledgers are not scientific authority.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, funnel/gate discipline and general mathematical tools, but not imported physical assumptions, ansatz coefficients, results or desired conclusions. Green CI is never automatically scientific PASS.

## Canonical readiness

- Internal programme readiness: **59%**.
- Theory established: **0%**.
- The 58→59 increment is attributed only to terminal closure of corrected G37-A3.
- G40 witness/calibration diagnostics and G41 implementation/calibration work do not by themselves raise readiness.

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
| Iter022F | G40-A | `34708971194` / `dab64180...` | `NEGATIVE_RESULT / G40A_FROZEN_SUPPORT_RULE_NOT_MET` | Fixed-witness finite RTN subset only; no general verdict. |
| Iter023A | G40-D | `34709706322` / `89dc08a4...` | `FIXED_WITNESS_FRAGILE_ON_PANEL` | Diagnostic only; G40-A remains failed. |
| Iter023B | G40-RC-C | `34710049387` / `1f79d9c7...` | `AXIS_FRAME_COVARIANT_RTN_SEARCH_CALIBRATED` | Family-axis-covariant witness calibration only. |
| Iter023C | G40-RC-A | `34710216045` / `3e31a9fa...` | `RUNNING` | Prospective finite RTN adversarial with calibrated axis-frame witness. |
| Iter024A | G41-P | `34710097236` / `e6c74225...` | `HIGH_RANK_CLASSICAL_KOSSAKOWSKI_IMPLEMENTATION_VALIDATED` | Rank-4/5/6 implementation/provenance only. |
| Iter024B | G41-C | `34710257380` / `2bac531b...` | `QUEUED / RUNNING` | Positive-rate optimizer calibration on frozen high-rank frames only. |

## Decisive current results

### G37-A3

Run `34708041385`, aggregate `103594427577`, artifact `10302623647`, digest `sha256:5b50793fe136cc30ce7aa60fae05a7be60b7895794686a2f35a5ca82feb2de63`. All 8 lanes passed exact parent embedding, nesting, nonzero-gap and Sobol/LHS agreement. Durable note: `results/ITER019F_G37A3_TERMINAL.md`.

### G40-A / G40-D

G40-A run `34708971194` failed its frozen support rule and remains a negative/inconclusive finite-family result. G40-D run `34709706322`, aggregate `103596229487`, artifact `10301928780`, digest `sha256:35d4dba7b5aea572e33b7ba6c067a5f4695b8d18fb84455e958ed2cde25a2383`, demonstrated `FIXED_WITNESS_FRAGILE_ON_PANEL`: shards 0/1 admitted panel witnesses where the single fixed witness admitted none. Durable notes: `results/ITER022F_G40A_TERMINAL.md`, `results/ITER023A_G40D_TERMINAL.md`.

### G40-RC-C calibration

Run `34710049387`, aggregate `103597100244`, artifact `10303335725`, digest `sha256:6b3d446be11880ae79cad0a55b74ccfff0cdf33a55f1045e04b27d6752f56f74`. Both Sobol and LHS passed 4/4 corrected hidden controls. Minimum hidden/recovered axis-frame-covariant BLP was `~0.8471377488`; worst recovery was `~1.73e-15`. This authorizes only the separately preregistered G40-RC-A run `34710216045`. Durable note: `results/ITER023B_G40RCC_TERMINAL.md`.

### G41-P implementation

Run `34710097236`, aggregate `103597226535`, artifact `10303101144`, digest `sha256:a189c87f4cb786e3fd2f5324e3bb54e3813d55f7f7ac959ff263747b811c185f`. All 12 rank-4/5/6 lanes passed the frozen classical Kossakowski rank, TP/CPTP, product-unitary factorization and zero-product-entanglement checks. This is implementation/provenance only and authorizes only a calibrated finite optimizer subfamily. Durable note: `results/ITER024A_G41P_TERMINAL.md`.

## Active frontier

1. **G40-RC-A**, run `34710216045`: prospective adversarial test under exactly the G40-RC-C axis-frame-covariant witness/search rule. Frozen nonzero gap `>1e-4`, method agreement `<=0.002`, axis-covariant BLP `>0.02`.
2. **G41-C**, run `34710257380`: ranks 4/5/6 × four shards × Sobol/LHS positive-control rate calibration on deterministic G41-P mode frames. Frozen recovery `<0.002`. No RCG-002 target. Even PASS does not calibrate arbitrary PSD Kossakowski orientations.

## Stable readiness rubric

Closed: independent scope discipline; coherent RCG-002 toy seed; finite MF K2/K3/K4 calibration/scoped comparator; one-mode shared Gaussian noise; corrected truly nested MF+shared finite comparator; OU three-time toy comparator; rank3 multimode shared white-noise comparator; strict RTN implementation; fixed-witness fragility diagnosed; axis-frame-covariant RTN search calibrated; rank-4/5/6 classical Kossakowski implementation validated.

Not closed: terminal G40-RC-A adversarial verdict; high-rank classical optimizer/adversarial gate; arbitrary-orientation/general PSD Kossakowski comparator; externally anchored observables/holdouts; continuum/full candidate-gravity dynamics; any constitution gate for an actual gravity theory.

## Claim locks

Never promote finite-family gaps to all-classical/semiclassical no-go claims. Green CI alone is not scientific PASS. Do not weaken frozen `0.002`, `1e-4`, BLP `0.02`, family, witness or target rules post hoc. Invalid G30/G31/G37/G39/G40 results stay invalid. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions.
