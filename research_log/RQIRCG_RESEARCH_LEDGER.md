# RQIR-CG research ledger

This is the clean scientific authority ledger for `RQIR-Candidate-Gravity`. Legacy mixed-project ledgers are not scientific authority.

## Scope contract
RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, funnel/gate discipline and general mathematical tools, but not imported physical assumptions, ansatz coefficients, results or desired conclusions. Green CI is never automatically scientific PASS. Frozen criteria/families/witnesses/charts are never weakened post hoc.

## Canonical readiness
- Internal programme readiness: **63%**.
- Theory established: **0%**.
- `58% -> 59%`: corrected G37-A3 scoped comparator closure.
- `59% -> 60%`: G41-A finite high-rank positive-rate comparator closure.
- `60% -> 61%`: G42-A bounded boundary-PSD adversarial comparator closure.
- `61% -> 62%`: G44-A basis-invariant real-PSD `tr(C)<=4` comparator closure.
- `62% -> 63%`: G47-A explicit finite hidden-classical memory comparator closure.
- G46-A, G48-C, G48-A, G49-C, G49-A, G50-P and G50-C deepen/qualify comparator layers without closing a new target-separation rubric, so they do not add readiness points.

## Authoritative recent gates
| Gate | Run / head | Terminal classification | Scope ceiling |
|---|---|---|---|
| G40-TM-A | `34716863840` | `G40TMA_FROZEN_SUPPORT_RULE_NOT_MET` | Finite RTN robustness nonclosure. |
| G44-A | `34718045811` | `DERIVED_SCOPED_BASIS_INVARIANT_TRACE_BALL_PSD_COMPARATOR_SUPPORT` | Bounded real-PSD Markovian `tr(C)<=4`. |
| G45-P | `34718225194` | complex-PSD provenance boundary | Provenance only. |
| G47-A | `34719377641` | `DERIVED_SCOPED_THREE_STATE_CLASSICAL_SWITCHING_COMPARATOR_SUPPORT` | Frozen bounded stationary 3-state/12D family only. |
| G46-A | `34719458597` | `DERIVED_SCOPED_EXTENDED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP8_CAP16` | Fixed caps 8/16. |
| G48-C | `34721391489` | `CAP32_CAP64_TRACE_BALL_PSD_OPTIMIZER_CALIBRATED` | Calibration only. |
| G48-A | `34724106251` | `DERIVED_SCOPED_TRACE_BALL_PSD_COMPARATOR_SUPPORT_CAP32_CAP64` | Finite caps 32/64 only. |
| G49-C | `34726705385` | `CAPFREE_DIRECT_PSD_OPTIMIZER_CALIBRATED` | Direct-PSD numerical calibration only. |
| G49-A | `34729309699` / `1d7154fb...` | `DERIVED_SCOPED_CAPFREE_DIRECT_PSD_COMPARATOR_SUPPORT` | Frozen four-shard RCG-002 direct real-PSD Markovian comparator only. |
| G50-P | `34734173762` / `c2a0eeb2...` | `FOUR_STATE_CLASSICAL_SWITCHING_PROVENANCE_MEMORY_QUALIFIED` | Response-blind finite four-state stationary hidden-classical CTMC switching family only. |
| G50-C | `34734256210` / `4528497f...` | `FOUR_STATE_CLASSICAL_SWITCHING_OPTIMIZER_CALIBRATED` | Response-blind calibration only for exact 20D four-state family. |

## G49-A terminal authority
Preregistration `67c57014859408175d235059db305e56991b23c5`; implementation `f9a71c862cd44e55a14d4cfd183a8d56161b2dc2`; workflow `5f1d33dd24c11454c0bd801d7c78e37b114cbf9c`; head `1d7154fb328f514bc5e10c8e1dc192b56d3cafd3`. Run `34729309699`; aggregate job `103649277540`; summary artifact `10308168184`; digest `sha256:023e41b5f450b0f59f92aac147ae2e4fbff4cc1127ce28f076bb8c2fc0b55a0f`.

All 8 lane artifacts are structurally valid. For shards 0..3, Sobol/LHS gap differences are `2.809541814474681e-09`, `1.0420698909330284e-07`, `2.473286330184621e-07`, `7.682030067623913e-08`, all <= frozen `0.002`. Direct-PSD best gaps are respectively `0.037007977391801956`, `0.14632859139860127`, `0.5275494552953647`, `0.6663865960376764`, and every shard passes consistency against terminal cap64 +0.002. Classification: `DERIVED_SCOPED_CAPFREE_DIRECT_PSD_COMPARATOR_SUPPORT`.

## G50-P terminal authority
Preregistration `a1df25626f4359e735b28d4f535620f73a97f827`; implementation `a4e36a0350d2fa33700892faf77d3be709cce418`; workflow `3c96e247f9ed8bac634c143ff64d9b02199c72ee`; head `c2a0eeb2e38649ca8b703b40a0d4e14cf2e6f1a3`. Run `34734173762`; aggregate job `103662473956`; summary artifact `10310930046`; digest `sha256:82892d4106bfed8adb28b146ee3910aeeb110187ceca3e28ddbb3479454fc8f3`.

All `6/6` raw lanes are structurally valid and pass the frozen provenance and non-semigroup memory conditions. Across lanes, max TP residual is `1.1329584524314835e-15`, min Choi eigenvalue `4.337030846198824e-12`, max product-output negativity `0.0`, max conditional product-unitary factorization error `3.5542838651085923e-16`, and semigroup defects span `0.7286785668895192..0.8228078204750715` against frozen threshold `1e-4`.

Interpretation is strictly scoped: this qualifies a broader finite four-state hidden-classical memory family for a separately preregistered response-blind calibration. It does not establish RCG-002 separation or any all-classical/no-go claim. Durable note: `results/ITER043_G50P_FOUR_STATE_CLASSICAL_SWITCHING_PROVENANCE_TERMINAL.md`.

## G50-C terminal authority
Preregistration `0de6cd29346ce68888c68ed1965ea0c7af224fb8`; implementation `1eed19071661ec143bf6e3feb350374031dab557`; workflow `a48d0386277de272ffa3b564c3c3d0674ef68492`; authoritative head `4528497f9b34add2bff84bc55db399673ca07c8f`. Run `34734256210`; aggregate job `103662830407`; summary artifact `10310302963`; digest `sha256:c600d52b399ca493b537b65507696dda6193be17a3f155f78cbcc85ca8573bba`.

All `8/8` raw lane artifacts were consumed and pass the prospectively frozen response-blind calibration rule. Worst train gap `6.1950671201431e-12`, worst held-out gap `4.109242107956982e-12`, worst normalized parameter error `1.7639089906452824e-10`, worst TP residual `1.776516304761236e-15`, minimum Choi eigenvalue `5.956647395842122e-11`. Sobol/LHS train-gap differences across controls are all `<=3.5660541684399162e-12`, far inside frozen `0.002`.

Classification: `FOUR_STATE_CLASSICAL_SWITCHING_OPTIMIZER_CALIBRATED`. Interpretation: optimizer calibration only. It authorizes target transport but is not RCG-002 separation. Durable note `results/ITER044_G50C_FOUR_STATE_SWITCHING_CALIBRATION_TERMINAL.md`, result-note commit `cb008662a4b432bd202885207c6d61590dc56349`.

## Active G50-A prospective transport
Iter045/G50-A was preregistered **before implementation/production** at commit `da2ed3bb190fcfc8b3e8225361b98490513630bf`. Implementation `c9fb66bb69ac27d1546f083aec6c95db2033a9e7`; workflow `1e689724050b8e7e9734c21395e453fae4da8f2d`; launch/head `2122211ff1c08c03ca637c42b8299fd3a9fd6806`; production run `34736777512`.

Frozen gate: Sobol/LHS x four pre-existing RCG-002 target shards, exact G50-C 20D family/bounds and optimizer budget. Scientific support requires admissible best candidates with train **and prospectively held-out** max probe gaps `>1e-4` in every lane, with Sobol/LHS agreement `<=0.002` on train and `<=0.003` held-out. No terminal classification before all raw artifacts and aggregate are consumed.

## Open scientific layers
- terminal Iter045/G50-A target transport against the qualified/calibrated four-state hidden-memory family;
- externally anchored held-out observables;
- continuum/full candidate-gravity dynamics and an actual gravity-theory constitution gate.

Do not repeat cap escalation. New production must target a genuinely unresolved layer rather than another coordinate variant of a saturated Markovian PSD comparator.

## Claim locks
Never promote finite/bounded-family or numerical gaps to all-classical/semiclassical no-go claims. Green CI alone is not scientific PASS. Do not weaken frozen thresholds/families/witnesses post hoc. Invalid/nonrobust historical gates remain invalid. Do not import QGR/KMQGB/RQIR physical assumptions or desired conclusions. `THEORY_ESTABLISHED` remains 0%.
