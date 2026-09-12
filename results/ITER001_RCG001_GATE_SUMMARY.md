# Iteration 001 — RCG-001 gate summary

Date: 2026-09-12
Status: `COMPLETED / ADMISSIBLE_SCOPED / QUANTUM-DEGENERATE`

GitHub Actions run: `34666139742`.

All 15 numerical jobs plus the static independence/claim-lock audit completed successfully.

## Frozen results

- G1/G2 limits: PASS. Coherent response scales linearly with `G`; intrinsic covariance scales linearly with `hbar` in the frozen seed implementation.
- G3 covariance positivity: PASS across seeds `17,41,73`.
- G4 retarded causality: PASS across seeds; the tested future/equal-time block norm is zero under the frozen strict-retarded convention.
- G5 three-channel coherent/noise identifiability: PASS across seeds; the frozen synthetic design has rank 2 and is well conditioned.
- G6 stochastic comparator: **DEGENERATE** by construction and by exact representation. A Gaussian seed with PSD covariance has an ordinary classical Gaussian stochastic representation at the level of the tested characteristic function / first two moments.

Representative consumed artifacts:

- seed 17 positivity: `min_eig_N = 0.0019619971919147576`, `min_eig_total = 0.00010068323193689444`;
- seed 17 limits: `G_half_coherent_ratio = 0.5`, `hbar_quarter_noise_ratio = 0.25`;
- seed 17 causality: `future_or_equal_norm = 0.0`;
- seed 17 identifiability: rank `2`, condition number `1.3443230791551917`;
- seed 17 stochastic comparator: `classical_gaussian_representation_exists = true`.

## Scientific decision

RCG-001 is retained as a useful baseline response/noise layer but is **not** promoted as quantum-specific gravity.

Classification:

`ADMISSIBLE_SCOPED_GAUSSIAN_RESPONSE_LAYER__QUANTUM_SPECIFIC_NOVELTY_BLOCKED_BY_EXACT_CLASSICAL_STOCHASTIC_REPRESENTATION`.

No parameter is retuned to evade G6.

## Next permitted construction

The minimal next extension must be coherence-sensitive and comparator-resistant in a preregistered domain. We therefore move from a Gaussian one-system characteristic kernel to a two-probe relational channel whose decisive witness is entanglement generation from a product input. The comparator class is frozen *before* computation as arbitrary correlated mixtures of local phase unitaries; such a class cannot create entanglement from a separable input.

This next step is an operational channel discriminator, not a microscopic UV theory and not a claim that gravity is quantum.
