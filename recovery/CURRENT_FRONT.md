# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active iteration: `ITER002`
Phase: `INDEPENDENT_RQIR_DERIVATION / COHERENCE_COMPARATOR_GATING`

## Canonical status

- Repository infrastructure readiness: **48%**
- Candidate-model readiness: **27%**
- Theory established: **0%**
- Baseline seed: `RCG-001 Relational quantum response kernel`
- Active seed: `RCG-002 Relational controlled-phase channel`
- RCG-001 promotion state: `ADMISSIBLE_SCOPED / QUANTUM-DEGENERATE`
- RCG-002 promotion state: `SEED / PREREGISTERED COMPARATOR TEST`
- Independent-from-QGR construction contract: **FROZEN**

Readiness is an internal construction metric, not a probability that the model is correct.

## Iter001 terminal result

GitHub Actions run `34666139742` completed all 15 numerical jobs plus the static contract audit.

- G1/G2 limits: PASS.
- G3 covariance positivity: PASS.
- G4 strict-retarded causality: PASS.
- G5 three-channel coherent/noise identifiability: PASS.
- G6 quantum-specific comparator: **DEGENERATE**.

The Gaussian seed has an exact ordinary classical Gaussian stochastic representation in the tested domain. No parameter was retuned to evade this result.

Terminal classification:

`ADMISSIBLE_SCOPED_GAUSSIAN_RESPONSE_LAYER__QUANTUM_SPECIFIC_NOVELTY_BLOCKED_BY_EXACT_CLASSICAL_STOCHASTIC_REPRESENTATION`.

Record: `results/ITER001_RCG001_GATE_SUMMARY.md`.

## RCG-002 active seed

The minimal next operational extension is a two-probe relational controlled-phase channel

`rho -> E_eta(U_chi rho U_chi^dagger)`,

`U_chi = diag(1,1,1,exp(i chi))`.

The comparator class was frozen before computation as arbitrary correlated mixtures of local phase unitaries. This scoped classical stochastic comparator cannot create entanglement from the frozen separable `|++>` input.

No microscopic formula for `chi` is asserted. Passing the current gate can establish only scoped distinguishability from this comparator class.

## Iter002 active computation

GitHub Actions run `34668952961` — `RCG Iter002 Coherence Comparator`.

22 parallel numerical lanes plus aggregate:

- G7 channel unitarity/CPTP/trace consistency;
- G8 entanglement negativity versus correlated local-phase stochastic comparator at three held-out phases and three comparator seeds;
- G9 parameter-free noiseless holdout identity `N = |sin(chi/2)|/2` at `chi = 0.37, 1.11, 2.03`;
- G10 frozen local-dephasing robustness map at `eta = 1.0, 0.95, 0.85, 0.70, 0.50`;
- G11 zero-interaction null.

Scientific head: `4450a0b94fbf7ddf9652a41903e5c3c6df66d229`.

## Promotion ceiling

Even a full Iter002 PASS permits at most:

`DISTINGUISHABLE_SCOPED_FROM_CORRELATED_LOCAL_PHASE_STOCHASTIC_COMPARATOR`.

It does not establish a microscopic gravity model because `chi` is still operational rather than derived.

## Next blockers

1. Consume Iter002 artifacts rather than workflow status alone.
2. If G8/G9 pass, derive a causal relativistic microscopic source for `chi` with explicit `G`, source, distance and time dependence.
3. Broaden comparator quotient beyond correlated local phases to semiclassical measurement-feedback and classical-channel mediator models.
4. Reconcile RCG-002 with the RCG-001 retarded-response/covariance layer without importing QGR structures.
5. Freeze an externally meaningful multi-channel holdout before any candidate promotion.

## Claim locks

Forbidden:

- `NEW_PHYSICS_FOUND`;
- `FULL_QUANTUM_GRAVITY`;
- `RQIR_REQUIRES_RCG002`;
- claim that gravity mediates entanglement in nature from the synthetic channel gate;
- claim that all classical mediator models are excluded by the scoped local-phase comparator;
- importing QGR structures to rescue a failed gate.

Current correct status:

`RCG001_LOCAL_GATES_PASS_BUT_GAUSSIAN_QUANTUM_NOVELTY_DEGENERATE + RCG002_PREREGISTERED_COHERENCE_COMPARATOR_TEST_RUNNING`.
