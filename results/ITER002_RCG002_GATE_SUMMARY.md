# ITER002 — RCG-002 coherence/comparator gate

Date: 2026-09-12
Scientific run: `34668984008`
Scientific head: `8db5036718a48bb3877589bd4e8532721211da16`
Summary artifact: `10290595952`
Summary digest: `sha256:a0c103597d3aa0c0681fe9b69ec34c7818a0d64ae9054d0ea5af742bfd34c044`

## Frozen result

All 22 numerical lanes and aggregate completed successfully.

- G7 channel consistency: 3/3 PASS.
- G8 comparator-resistant entanglement: 9/9 PASS.
- G9 parameter-free holdout `N=|sin(chi/2)|/2`: 3/3 PASS; maximum absolute error `2.7755575615628914e-16`.
- G10 dephasing robustness: 5/5 preregistered checks PASS. Negativity at `chi=1.11` decreases from `0.2634716501` at `eta=1` to `0.0569301551` at `eta=0.70`, and reaches zero at `eta=0.50` as expected by the frozen survival criterion.
- G11 zero-interaction null: 2/2 PASS.

Across comparator lanes, the largest correlated-local-phase stochastic comparator negativity was exactly `0.0`; the minimum nonzero RCG-002 negativity in the tested comparator set was `0.09197326676402057`.

## Classification

`DISTINGUISHABLE_SCOPED_FROM_CORRELATED_LOCAL_PHASE_STOCHASTIC_COMPARATOR`

This is a scoped quantum-channel result only. It does **not** establish that gravity is quantum, that RCG-002 is realized in nature, or that all classical mediator models are excluded. The interaction phase `chi` was still operational rather than microscopically derived in ITER002.

## Next gate

Derive a causal source-dependent `chi` from a frozen weak-field relational interaction geometry, test its mass/time/distance scaling and retarded onset, and broaden the comparator quotient from random local phases to the full separable/LOCC channel class at the entanglement-generation level.