# Iter043 / G50-P — Four-state hidden-classical switching provenance and memory qualification

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION**
Date: 2026-09-13

## Purpose
Qualify a strictly broader response-blind hidden-classical memory family than terminal G47-P/G47-A: a four-state continuous-time classical Markov chain switching among two-qubit **local-sum Hamiltonians only**. This gate does not use the RCG-002 response and cannot establish target separation.

## Frozen family
For each shard `0..5`:
- hidden state space has exactly 4 classical states;
- generator `Q` has strictly positive deterministic off-diagonal rates, column convention `rates[to,from]`, diagonal fixed by exact column conservation;
- hidden initialization is the stationary distribution of `Q`;
- conditional Hamiltonian in hidden state j is exactly `H_j = H_A,j ⊗ I + I ⊗ H_B,j` with deterministic response-blind Pauli-field vectors;
- visible channel is obtained by evolving the joint classical-quantum block generator and summing hidden states.

No RCG-002 target, fitted response, optimizer, imported QGR/KMQGB/RQIR physical assumption, or post-hoc family modification is allowed in this gate.

## Frozen witnesses and controls
Times: `(0.12, 0.35, 0.75, 1.25)`.
Factorization steps: `(0.05, 0.17)`.
Reduced semigroup witness: `t=s=0.35`.
Product-input panel: the same 16 local product states generated from `|0>, |1>, |+>, |+i>` per qubit.

A lane is structurally valid only if all reported numerical quantities are finite.

Classical/provenance qualification requires simultaneously:
1. every off-diagonal CTMC rate `>= -1e-12`;
2. max absolute Q column-sum residual `<= 1e-12`;
3. stationary probabilities `>= -1e-12`, normalization error `<= 1e-12`, stationary residual `||Q pi|| <= 1e-10`;
4. max conditional product-unitary factorization Frobenius error `<= 1e-11`;
5. max visible trace-preservation residual `<= 1e-10`;
6. minimum visible Choi eigenvalue `>= -1e-8`;
7. max output trace error on product panel `<= 1e-10`;
8. max output negativity on the product panel at the designated witness time `<= 1e-9`.

Memory qualification additionally requires reduced semigroup defect
`||E(t+s)-E(t)E(s)||_F > 1e-4`.

## Frozen aggregate rule
Run six independent shards with `fail-fast:false`.

- If all 6 lanes are structurally valid, all 6 satisfy provenance controls, and all 6 satisfy the memory witness: `FOUR_STATE_CLASSICAL_SWITCHING_PROVENANCE_MEMORY_QUALIFIED`.
- If structurally valid but any provenance or memory condition fails: `G50P_FROZEN_QUALIFICATION_RULE_NOT_MET`.
- If any lane is structurally invalid or implementation cannot evaluate the frozen predicates: classify as implementation/numerical failure, not scientific failure.

## Interpretation lock
A PASS qualifies only this explicit finite four-state stationary hidden-classical switching/product-unitary family as a valid broader-memory comparator family for a later separately preregistered calibration/adversarial transport gate. It is not evidence for or against RCG-002, not a universal classical-memory theorem, and not a gravity-theory result.

Programme readiness remains 63% until a genuinely new rubric/gate is terminally closed.