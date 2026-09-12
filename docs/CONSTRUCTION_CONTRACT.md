# RQIR-CG construction contract v0.1

Date: 2026-09-12
Status: FROZEN FOR ITERATION 001

## Independence rule

This repository constructs a candidate directly from frozen RQIR Core v1.0 observable and consistency requirements. It must not import equations, ontology, coefficients, or successful patches from `Quantum-Gravity-Reconstruction` or other candidate repositories during construction.

Cross-comparison is permitted only after a result has been frozen here.

## Required gates

A candidate is not promoted merely because it fits one observable. It must satisfy, where applicable:

1. explicit GR/QFT/EFT null baseline;
2. `G -> 0` decoupling;
3. `hbar -> 0` classical limit;
4. gauge/relational observable discipline;
5. positive physical covariance / no negative variance;
6. normalized quantum-state evolution at the operational level;
7. no superluminal signalling introduced by the effective response map;
8. simultaneous map to at least three distinct RQIR channels;
9. degeneracy audit against semiclassical and stochastic gravity;
10. at least one held-out observable or parameter-free relation before any novelty claim.

## Search order

`RQIR requirements -> formal constraints -> minimal degrees of freedom -> minimal dynamics -> observable map -> consistency gates -> comparator quotient -> holdout`.

No gate may be weakened after seeing a result. Failed and degenerate branches remain recorded.

## Promotion labels

- `SEED`: mathematically specified but not yet gated.
- `ADMISSIBLE_SCOPED`: passed current local gates only.
- `DISTINGUISHABLE_SCOPED`: survives the declared comparator quotient in a stated domain.
- `CANDIDATE`: survives all currently frozen construction gates and a holdout.
- `NEW_PHYSICS`: forbidden unless an independently derived, non-baseline prediction survives comparator and holdout tests.

`BLOCKED != FAIL` and `workflow success != scientific PASS`.
