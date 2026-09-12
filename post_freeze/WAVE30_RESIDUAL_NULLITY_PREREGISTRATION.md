# Wave 30 — Residual Nullity Lower-Bound / Baseline-Quotient Audit

Status: **PREREGISTERED BEFORE GITHUB COMPUTE**

## Frozen authorities

- Wave-22 finite proxy bank remains immutable with parameter order `[c3,d3,e4,f4,s2,s0]`.
- Wave-29 certificate is frozen and supplies the central F2 rank statements.
- Wave-28 UV-derivative/J8/J9 contract remains separate and unchanged.
- No polygon-derived QGR equations or architecture may enter this wave.

## Question

Within the low-energy finite truncations already frozen in Wave 29, what is the minimum unresolved dimension of the six-dimensional Wave-22 proxy space after quotienting the generalized-EH/baseline sector rather than automatically crediting it as new residual physics?

This is a rank/codimension theorem audit. It does not claim that the full nonlocal F2 form factors are finite-dimensional objects. It applies only to the declared low-energy finite proxy truncations used for matching to the six frozen Wave-22 coordinates.

## Rank identity

For a latent parameter vector `z in R^k`, an embedding `P: R^k -> R^6`, and frozen probe matrix `H: R^6 -> R^m`,

`rank(H P) <= rank(P) <= k`.

Therefore the codimension of the latent image in the six-dimensional proxy target obeys

`codim(Im P) = 6 - rank(P) >= 6-k`.

Adding more observable rows to `H` cannot violate this bound.

## Scenarios

### S30-A constants-only quadratic sector

Wave 29: `k <= 2`.

Predeclared bound: residual codimension >= 4.

### S30-B constants + first slopes, generalized-EH baseline-quotiented

Wave 29: `k <= 4`.

Predeclared bound: residual codimension >= 2.

### S30-C one additional independently justified generalized-EH residual coefficient

Optimistic finite scenario: `k <= 5`.

Predeclared bound: residual codimension >= 1. Thus one additional generalized-EH scalar coefficient still cannot close six independent directions.

### S30-D two or more additional residual directions

With `k=6`, rank-six closure becomes mathematically possible only if all six columns are independent and the added directions are transverse to the F2 quadratic image. Wave 30 does not grant that physical premise; it only records the necessity.

## Tests

1. Recompute the frozen Wave-22 probe-matrix rank from the bank.
2. Verify codimension lower bounds analytically and over random full-column-rank embeddings for k=2,4,5.
3. Verify that composing with the full frozen probe matrix cannot raise latent rank.
4. Test the optimistic one-extra-EH scenario and show maximum observable rank 5.
5. Stress random embeddings/perturbations to distinguish generic saturation of the rank cap from actual six-dimensional closure.
6. Verify information firewall.

## Predeclared signals

- `wave22_probe_matrix_rank_is_6`
- `constants_only_residual_codimension_ge_4`
- `first_slope_baseline_quotiented_residual_codimension_ge_2`
- `one_extra_EH_coefficient_residual_codimension_ge_1`
- `one_extra_EH_coefficient_cannot_close_six_dimensions`
- `at_least_two_additional_independent_residual_directions_required_beyond_four_parameter_quadratic_truncation`
- `probe_composition_cannot_raise_latent_rank`
- `generic_transversality_can_saturate_rank_cap_but_not_exceed_it`
- `six_dimensional_closure_requires_explicit_extra_directions_and_transversality`
- `information_firewall_pass`

## Claim boundary

A PASS means that, in the declared finite low-energy projection problem, the current F2 quadratic central manifold is provably too low-dimensional for six-direction closure unless at least two additional independent residual directions are supplied beyond the four-coefficient first-slope truncation. It does not prove that the full F2 nonlocal action has only four degrees of freedom, and it does not identify which Wave-22 coordinates span the unresolved complement.