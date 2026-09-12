# Wave 24 — Parent-Law Strength / Anti-Retrofit Audit

Status: PREREGISTERED BEFORE COMPUTE

## Frozen inputs

- RQIR-only action-level endpoint v1 remains frozen.
- Wave-22 frozen holdout bank remains immutable: `holdouts/WAVE22_FROZEN_BANK.json`, blob `c32bd52edd003589ef65e0240c757475f215f55f`.
- Wave-23 robustness certificate remains descriptive only; no Wave-24 selector may modify the bank.

## Scientific question

What minimum local information rank and provenance must a new parent principle supply to reduce the six-dimensional RQIR residual proxy `[c3,d3,e4,f4,s2,s0]` to a unique candidate without becoming an arbitrary post-hoc selector?

## External provenance boundary

Established gravity consistency results motivate a distinction between **bounds/relations** and **unique parent dynamics**:

- Camanho, Edelstein, Maldacena, Zhiboedov, arXiv:1407.5597: causality constrains higher-derivative graviton three-point structures and can require additional UV degrees of freedom; it does not generically select one EFT point from low-energy data alone.
- Bern, Kosmopoulos, Zhiboedov, arXiv:2103.12728: unitarity/crossing of the four-graviton amplitude bound the `R^3` coefficient relative to higher-order data, again constraining rather than generically uniquely fixing all Wilson coefficients.

No numerical coefficient from these papers is imported into the finite proxy.

## Frozen selector classes

### S0 — baseline residual
No new law on the already-quotiented six-dimensional residual space. Expected local nullity: 6.

### S1 — one scalar equality
`L1 theta = 0`, with `L1=[1,1,1,1,1,1]`. Expected rank 1, nullity 5.

### S2 — three Ward-like independent equalities
Frozen matrix in `compute_wave24/common.py`. Expected rank 3, nullity 3.

### S3 — two-latent structured generator
`theta = B z`, `z in R^2`, with frozen `B` in `common.py`. Two frozen design probes (`P2_q0.65`, `P0_q0.75`) calibrate the two latent coordinates; the other eight Wave-22 probes are prospective holdouts.

Predeclared gates:
- design matrix rank = 2;
- for an in-family synthetic truth, max holdout prediction error <= `1e-12`;
- for a preregistered out-of-family truth, normalized holdout residual >= `0.05`;
- this class receives **no independent-physics or novelty credit by construction**; it demonstrates selector strength only.

### S4 — arbitrary full-rank equality selector
Two separate frozen invertible 6x6 matrices are used to select two distinct preregistered target points. Gate: each selector has rank 6, yet the two selected points yield Wave-22 prediction vectors separated by L2 distance >= `0.05`.

Interpretation: full mathematical closure alone is not evidence for the chosen law, because equally complex full-rank selectors can pick conflicting theories.

### S5 — minimum-complexity representative
`theta=0`. It is unique, but is classified as model-selection convention rather than independently derived microscopic dynamics.

### S6 — bounded/inequality consistency region
A frozen symmetric hyperrectangle around the origin is sampled with seed 2406. Gate: accepted samples produce nonzero holdout width >= `0.05`, demonstrating that inequality admissibility need not imply uniqueness.

### S7 — unconstrained single-function interpolation control
A claim of “only one function” is not counted as low microscopic freedom merely because it is named by one symbol. Define ten fixed probe coordinates `x_i = linspace(-1,1,10)` and the preregistered target vector

`y = [0.12,-0.05,0.18,-0.11,0.07,0.20,-0.16,0.09,0.14,-0.08]`.

Fit the unique degree-9 polynomial through all ten points. Predeclared gates:
- maximum interpolation error <= `1e-10`;
- polynomial coefficient count = 10;
- therefore an otherwise unconstrained function can encode the complete finite holdout vector and fails `no_hidden_functional_freedom`.

Interpretation: functional notation is not a compression theorem. A function earns low-freedom status only through independently justified dynamics, analyticity/spectral structure, a finite generative law, or other constraints that produce prospective predictions rather than pointwise interpolation.

## Parent-Law Acceptance Gate v1

A future selector receives scientific parent-law credit only if **all** are true:

1. `closure`: local residual nullity is zero after accounting for any latent parameters calibrated from declared design data;
2. `independent_provenance`: the law was motivated independently of the Wave-22 candidate holdout outcomes;
3. `comparator_novelty`: the law/predictions are not merely a C5/EFT reparameterization or an already-known generic factorisation;
4. `prospective_predictivity`: at least two frozen Wave-22 probes remain unused in calibration and are genuine predictions;
5. `no_hidden_functional_freedom`: arbitrary functions/pointwise knobs cannot reproduce any desired holdout vector.

Wave 24 does not preregister any tested selector as satisfying all five gates.

## Predeclared aggregate signals

- scalar_relation_leaves_nullity_5
- three_relation_class_leaves_nullity_3
- two_latent_generator_is_predictive_inside_class
- two_latent_generator_is_falsifiable_outside_class
- arbitrary_full_rank_selectors_can_choose_conflicting_unique_points
- minimality_is_unique_but_not_physical_law
- inequality_consistency_region_is_nonunique
- unconstrained_function_interpolates_arbitrary_finite_holdout
- no_tested_selector_earns_parent_law_credit
- future_candidate_information_firewall_pass

## Claim boundary

Passing Wave 24 localizes the missing ingredient to **independently justified full closure**, not merely algebraic rank or compact notation. It is not a proof that no such physical principle exists.
