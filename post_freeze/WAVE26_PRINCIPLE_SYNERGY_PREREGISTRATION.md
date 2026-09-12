# Wave 26 — Known-Principle Synergy / Transversality Audit

Status: **PREREGISTERED BEFORE GITHUB COMPUTE**

## Frozen authorities

- Wave-22 prospective holdout bank remains immutable: `holdouts/WAVE22_FROZEN_BANK.json`, blob `c32bd52edd003589ef65e0240c757475f215f55f`.
- `protocol/PARENT_LAW_ACCEPTANCE_PROTOCOL_V1.json` remains the judge.
- Wave-25 individual-principle classifications are frozen by `certificates/WAVE25_KNOWN_PRINCIPLE_TOURNAMENT_CERTIFICATE.md`.
- No KMQGB/polygon candidate equations or architecture may be imported.

## Scientific question

Can combinations of independently established principle classes remove the six-dimensional RQIR residual nullspace, and if a finite proxy achieves rank six, is that closure a universal consequence of the named principles or conditional on an unverified independence/transversality assumption?

The central combination is K1 Soft/Ward + K4 asymptotic-safety fixed-point scaling. The purpose is **not** to claim that asymptotic safety is described by the finite matrices below. The matrices diagnose the logical rank requirement that would have to be supplied by a concrete same-realization fixed-point-to-RQIR map.

## Analytic rank identity

Let `W` be the frozen rank-3 Wave-24 Ward-like matrix and let `A_r` be a rank `6-r` fixed-point constraint matrix, where `r` is the number of relevant trajectory directions. If

`d = dim(Row(W) intersection Row(A_r))`,

then

`rank([W; A_r]) = 3 + (6-r) - d = 9-r-d`.

Full six-dimensional closure therefore requires:

- `r=1`: `d=2` exactly (the minimum dimension forced by dimension counting),
- `r=2`: `d=1` exactly,
- `r=3`: `d=0`,
- `r>=4`: impossible by rank count because `3 + (6-r) < 6`.

Any overlap larger than the minimum destroys full closure. Thus rank-six synergy is conditional on a model-specific transversality statement, not on the names of the two principles alone.

## Frozen diagnostics

### S26-1 Canonical transverse examples

For `r=1,2,3,4`, define `A_r` as the first `6-r` rows of the 6x6 identity and stack it with frozen `W`.

Predeclared signal:
- combined rank = 6 for `r=1,2,3`;
- combined rank = 5 for `r=4`.

This proves **existence** of finite orientations with closure; it does not establish universal closure.

### S26-2 Random-orientation stress

For each `r=1,2,3,4`, sample `500` Haar-like random orthogonal matrices with seed `2602`; take the first `6-r` rows as `A_r` and compute `rank([W;A_r])` at tolerance `1e-10`.

Predeclared signals:
- closure fraction >= `0.99` for `r=1,2,3`;
- closure fraction = `0` for `r=4`.

Interpretation: transversality is generic in the finite linear proxy for `r<=3`, but genericity is not a substitute for a same-realization physical derivation.

### S26-3 Aligned/redundant counterexamples

Construct allowed rank-`6-r` constraint spaces that intentionally contain as much of `Row(W)` as dimensions permit. Gate: at least one explicit valid `A_r` for each `r=1,2,3` leaves nonzero residual nullity after stacking with `W`.

This demonstrates that the principle labels alone do not logically guarantee independence.

### S26-4 Ward + positivity intersection

Use the frozen positivity ellipsoid from Wave 25 with semiaxes `[0.20,0.18,0.15,0.12,0.10,0.09]`. Sample `20,000` points in the exact nullspace of `W` with seed `2601`, rescaled to lie inside that ellipsoid. The `0.05` width threshold is inherited unchanged from Waves 24/25.

Predeclared signals:
- Ward residual nullity = 3;
- maximum frozen-bank prediction width of the Ward+positivity intersection >= `0.05`.

Therefore equality consistency plus bounded admissibility does not by itself select a unique theory.

### S26-5 Principle-level acceptance ledger

Because S26-1 and S26-3 exhibit both closing and non-closing realizations under the same abstract principle labels, PL1 at the **principle-class combination level** is preregistered as `BLOCKED_PENDING_SAME_REALIZATION_TRANSVERSALITY_MAP`, not PASS.

No combination receives PL3 novelty merely by intersecting already-known consistency conditions. A future concrete microscopic realization may change this classification only prospectively and must be tested against the unchanged Wave-22 bank.

## Aggregate signals

- canonical_transverse_examples_close_for_r_le_3
- r4_cannot_close_by_dimension_count
- random_orientation_closure_fraction_ge_0_99_for_r_le_3
- aligned_redundancy_counterexamples_prevent_universal_closure
- ward_positivity_intersection_nonunique
- principle_level_PL1_blocked_without_same_realization_transversality_map
- no_known_principle_combination_tested_here_earns_parent_law_credit
- future_candidate_information_firewall_pass

## Claim boundary

Passing Wave 26 would establish a conditional rank-synergy result, not a derivation of asymptotic safety or any other microscopic quantum-gravity theory. It would identify the next missing object more sharply: a same-realization map proving that the independently motivated microscopic constraints act transversely on the already-quotiented RQIR residual directions without double counting Ward/gauge consistency.
