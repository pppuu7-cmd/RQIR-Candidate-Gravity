# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active iteration: `ITER001`
Phase: `INDEPENDENT_RQIR_DERIVATION / FIRST_SEED_GATING`

## Canonical status

- Repository infrastructure readiness: **35%**
- Candidate-model readiness: **18%**
- Theory established: **0%**
- Active seed: `RCG-001 Relational quantum response kernel`
- Promotion state: `SEED`
- Independent-from-QGR construction contract: **FROZEN**

Readiness is an internal construction metric, not a probability that the model is correct.

## RCG-001 seed

The minimal frozen operational seed is

`x = x_GR + G R tau + sqrt(G*hbar) xi`

with positive covariance kernel `N` and retarded response `R`. It is designed to span multiple frozen RQIR channels while keeping the baseline and stochastic comparator explicit.

## Iter001 active computation

GitHub Actions run `34666139742` — `RCG Iter001 Parallel Gates`.

Parallel matrix:

- G3 covariance positivity;
- G1/G2 `G -> 0` and `hbar -> 0` scaling;
- G4 discrete retarded causality;
- G5 three-channel coherent/noise identifiability;
- G6 exact Gaussian stochastic-comparator degeneracy control;
- three independent seeds `17,41,73`;
- independent static claim/independence contract audit.

The expected G6 outcome is deliberately negative for quantum-specific novelty: the Gaussian seed admits a classical Gaussian stochastic representation at the level currently tested. That result, if reproduced, is a scientific degeneracy result rather than an infrastructure failure.

## Next permitted gate

Only after consuming Iter001 artifacts:

1. freeze which local consistency gates pass;
2. if G6 remains degenerate, do **not** tune the Gaussian seed to force novelty;
3. derive the minimal non-Gaussian/coherence-sensitive extension from frozen RQIR Q2/Q4/Q5 requirements;
4. preregister a comparator-resistant held-out relation before computing it.

## Claim locks

Forbidden:

- `NEW_PHYSICS_FOUND`;
- `FULL_QUANTUM_GRAVITY`;
- `RQIR_REQUIRES_RCG001`;
- quantum interpretation of `N` merely from positivity;
- importing QGR structures to rescue a failed gate.

Current correct status:

`FIRST_INDEPENDENT_RQIR_DERIVED_SEED + PARALLEL_LOCAL_GATES_RUNNING + QUANTUM_SPECIFIC_NOVELTY_UNESTABLISHED`.
