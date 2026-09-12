# RQIR-CG research ledger

This is the clean scientific authority ledger for `RQIR-Candidate-Gravity`. Legacy mixed-project ledgers are not scientific authority.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, funnel/gate discipline and general mathematical tools, but not imported physical assumptions, ansatz coefficients, results or desired conclusions. Green CI is never automatically scientific PASS.

## Canonical readiness

- Internal programme readiness: **60%**.
- Theory established: **0%**.
- `58% -> 59%`: terminal closure of corrected G37-A3.
- `59% -> 60%`: terminal closure of G41-A finite high-rank positive-rate comparator layer.
- Calibration, implementation, identifiability and diagnostic gates do not themselves raise readiness.

## Authoritative recent gate ledger

| Iteration | Gate | Run / head | Classification | Scope ceiling |
|---|---|---|---|---|
| Iter017 | G35 | `34697766107` / `fbc71768...` | `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT` | Finite additive independent MF. |
| Iter017R | G35-R | `34702384573` / `1b93cbf1...` | `HELDOUT_OPTIMIZER_ROBUSTNESS_PASS_K2_K3_K4` | Method robustness only. |
| Iter018A-C | G36-P/C/A | `34702575861`, `34703606707`, `34703779268` | shared-noise implementation/calibration/scoped support | One shared Gaussian classical mode. |
| Iter019C-F | G37-C2/A3 | `34704249235`, `34708041385` | calibrated corrected nested family + `DERIVED_SCOPED_TRULY_NESTED_MF_PLUS_SHARED_BOUNDARY_PRESERVING_COMPARATOR_SUPPORT` | Finite K2-MF + one shared Markovian mode. |
| Iter020A-C | G38-P/C/A | `34704060723`, `34704210632`, `34704373278` | OU implementation/calibration/scoped support | Three-time OU toy trajectory. |
| Iter021A-E | G39-P/C/A2 | `34704548004`, `34704727102`, `34707920572` | rank2/rank3 implementation/calibration/scoped support | Finite rank3 multimode shared white noise. |
| Iter022A-F | G40-P/C/A | `34708162180`, `34708550582`, `34708971194` | RTN implementation/calibration; adversarial frozen support rule not met | Fixed-witness finite RTN. |
| Iter023A-D | G40-D/RC-C/RC-A/RC-D2 | `34709706322`, `34710049387`, `34710216045`, `34710444349` | fixed-witness fragility; axis-frame calibration; adversarial rule not met; persistent optimizer nonrobustness | No RTN physics PASS. |
| Iter024A | G41-P | `34710097236` / `e6c74225...` | `HIGH_RANK_CLASSICAL_KOSSAKOWSKI_IMPLEMENTATION_VALIDATED` | Rank4/5/6 implementation/provenance. |
| Iter024B | G41-C | `34710257380` / `2bac531b...` | `HIGH_RANK_RATE_OPTIMIZER_CALIBRATED` | Positive-rate search on frozen frames only. |
| Iter024C | G41-A | `34710491309` / `766ea138...` | `DERIVED_SCOPED_HIGH_RANK_RATE_COMPARATOR_SUPPORT` | Frame-indexed rank4/5/6 positive-rate families only. |
| Iter025A | G42-J | `34710643103` / `ec3d1a5e...` | `FULL_LOCAL_RANK_IDENTIFIABILITY_PRE_GATE` | Full 21-param real-PSD local identifiability only. |
| Iter025B | G42-C | `34710744967` / `7ebc18df...` | `FULL_PSD_OPTIMIZER_CALIBRATED` with scope correction | Strictly SPD-interior chart only; boundary excluded. |
| Iter025C | G42-C2 | `34710953936` / `858ad4b6...` | `PSD_BOUNDARY_OPTIMIZER_CALIBRATED` | Bounded PSD chart, ranks 2/4/5/6 controls. |
| Iter025D | G42-C3 | `34711048394` / `35f719fd...` | `PSD_BOUNDARY_RANK_COMPLETION_CALIBRATED` | Same bounded PSD chart, ranks 1/3 controls. |
| Iter026 | G42-A | `34712491707` / `f7f48725...` | **RUNNING** | Prospective bounded 21-coordinate real-PSD Markovian adversarial gate. |
| Iter026R | G42-R | `34712524241` / `3b53451c...` | **RUNNING** | Held-out optimizer replication only. |

## Decisive terminal results

### G40 RTN branch

G40-RC-A run `34710216045` failed the frozen all-shards support rule on shard 3: Sobol/LHS gap difference `0.0022523906566203067 > 0.002`. G40-RC-D2 run `34710444349` then used four independent 64-start searches on the unchanged shard-3 family/witness/target; best gaps were `0.7495354861`, `0.7450136685`, `0.7450127676`, `0.7450127451`, spread `0.0045227410 > 0.002`. Classification `PERSISTENT_OPTIMIZER_OR_OBJECTIVE_GEOMETRY_NONROBUSTNESS`. No RTN adversarial physics PASS exists.

### G41-A high-rank finite comparator

G41-A run `34710491309`, aggregate `103598462910`, artifact `10303600848`, digest `sha256:fe89d973dc1f24fe50fba09542e1b1b8e1d1fbae5e9cb1f33165b7213764dea7`: all 12 rank×shard cells passed frozen nonzero-gap and cross-method agreement. Classification `DERIVED_SCOPED_HIGH_RANK_RATE_COMPARATOR_SUPPORT`. This finite frame-indexed closure produced readiness `59% -> 60%`.

### G42-J identifiability

Run `34710643103`, aggregate `103598755854`, artifact `10303316491`, digest `sha256:07a895f0fb309a6e642cd6eb5429e368ddcad0c78367571cfa59b7c7bce8ea9e`: all four controls had Jacobian rank `21/21`, worst condition `5.905925058`, maximum two-step relative mismatch `1.262474e-9`, CPTP clean. Classification `FULL_LOCAL_RANK_IDENTIFIABILITY_PRE_GATE`.

### G42-C scope correction

Run `34710744967`, aggregate `103599128599`, artifact `10302903611`, digest `sha256:daa9c9f1ac0bf70094fd47783c7b0dece89243593348befff801054f799e258a`: 8/8 controls passed, but log-Cholesky diagonal bounds made every candidate strictly positive definite. Authority is SPD-interior calibration only, not PSD-boundary calibration. No adversarial gate was launched from this result alone.

### G42-C2 boundary calibration

Run `34710953936`, head `858ad4b6848362bf430eaab849fb0ed4166f9cde`, aggregate `103600409310`, artifact `10303587123`, digest `sha256:d71af618510d0d61fbac14a3db91e9bf713822f657cfd985cc54e96fbf2ac94e`.

All 8/8 positive-control lanes for effective ranks 2/4/5/6 passed frozen trace-recovery `<0.002`, relative Kossakowski error `<0.02`, correct rank recovery and PSD validity. Sobol worst trace gap `4.2824978732075346e-10`, worst relative-C error `3.3388943747698924e-09`; LHS worst gap `1.9221941865034614e-10`, worst relative-C error `1.9289529867904655e-09`. Classification `PSD_BOUNDARY_OPTIMIZER_CALIBRATED`.

Durable note: `results/ITER025C_G42C2_TERMINAL.md`.

### G42-C3 rank completion

Run `34711048394`, head `35f719fdad8af1e2f8fdd71727c84abec3857c2a`, aggregate `103601042911`, artifact `10303627020`, digest `sha256:a9fa4ccaa8f6f79540311deb3f8a42be74661e2793d6dc7e5092570a7e52e3d1`.

All 8/8 rank-1/rank-3 completion lanes passed. Sobol worst trace gap `4.2872736979461425e-07`, worst relative-C error `8.398809261492516e-06`; LHS worst gap `7.34537126692358e-07`, worst relative-C error `1.5813386032144557e-05`. Classification `PSD_BOUNDARY_RANK_COMPLETION_CALIBRATED`.

Together C2+C3 prospectively calibrate the optimizer across effective PSD ranks 1–6 **within the frozen bounded Cholesky chart** `diag∈[0,0.60]`, `offdiag∈[-0.30,0.30]`. They do not establish an unbounded full-PSD optimization theorem and do not raise readiness.

Durable note: `results/ITER025D_G42C3_TERMINAL.md`.

## Active frontier

### G42-A — primary physics gate

Protocol `protocol/ITER026_G42A_BOUNDARY_PSD_ADVERSARIAL.md`; run `34712491707`; head `f7f48725a3d57398426f8ac9341a1d11b9cc591f`.

Eight prospective lanes = Sobol/LHS × four frozen RCG-002 target shards. Same boundary-capable bounded 21-coordinate real-PSD 6x6 Markovian classical random-Hamiltonian Kossakowski chart calibrated by C2+C3. Frozen per-shard rule: both methods admissible, each scientific trace gap `>1e-4`, and Sobol/LHS gap difference `<=0.002`; all four shards required.

Early non-terminal result only: shard 3 Sobol gap `0.8197294896504166`, LHS `0.819101112669069`, difference `0.0006283769813476`; both maps pass PSD/TP/Choi/state/trace admissibility. No overall scientific classification before aggregate.

### G42-R — independent held-out calibration replication

Protocol `protocol/ITER026R_G42R_HELDOUT_PSD_CALIBRATION.md`; run `34712524241`; head `3b53451c192c8bcaedd39105d1c9b9b3ae3aa6e6`.

Twelve new hidden-control lanes = effective ranks 1–6 × Sobol/LHS, with seeds disjoint from C2/C3. Same bounded PSD chart/search/recovery/rank rules. Methodology robustness only: cannot modify G42-A thresholds/verdict and cannot raise readiness by itself.

## Stable readiness rubric

Closed: independent scope discipline; coherent RCG-002 toy seed; finite MF K2/K3/K4; shared Gaussian finite layers; corrected nested MF+shared comparator; OU finite-correlation toy comparator; finite rank2/rank3 multimode shared noise; finite rank4/5/6 frame-indexed positive-rate comparator; full 21-param local identifiability; bounded PSD optimizer calibration across effective ranks 1–6.

Not closed: terminal G42-A bounded arbitrary-orientation PSD adversarial comparator; basis/chart/bound robustness needed before stronger PSD-family interpretation; robust RTN trace-metric-aligned optimization; broader non-Markovian/classically correlated comparators; externally anchored observables/holdouts; continuum/full candidate-gravity dynamics; any constitution gate for an actual gravity theory.

## Claim locks

Never promote finite/bounded-family gaps to all-classical/semiclassical no-go claims. Green CI alone is not scientific PASS. Do not weaken frozen thresholds/families/witnesses post hoc. Invalid or nonrobust historical gates remain invalid. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions.
