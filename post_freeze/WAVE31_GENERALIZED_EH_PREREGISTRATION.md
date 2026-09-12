# Wave 31 — Generalized-EH Residual-Rank / Baseline-Quotient Audit

Status: **PREREGISTERED BEFORE GITHUB COMPUTE**

## Frozen authorities

- RQIR Core v1.0 remains frozen.
- Wave-22 six-coordinate proxy bank remains immutable.
- Wave-29 F2 quadratic-rank certificate remains frozen.
- Wave-30 codimension theorem remains frozen: the four-coefficient first-slope quadratic truncation needs at least two additional independent residual directions for possible six-dimensional closure.
- Wave-31 evidence is frozen in `evidence/WAVE31_GENERALIZED_EH_EVIDENCE.json`.
- Wave-28 J8/J9 displaced-trajectory requirement remains separate and unchanged.

## Scientific question

Does the same-lineage published F2 generalized-Einstein-Hilbert sector justify at least two additional independent **bulk residual** directions beyond the four-coefficient quadratic truncation after the classical-GR baseline is quotiented out?

## Distinctions

Three objects must not be conflated:

1. a classical EH normalization `G_N`;
2. a momentum-dependent coefficient multiplying a term linear in curvature;
3. genuinely nonlinear curvature dependence in `Rcal(Delta,R)`.

The first is baseline. For the second, under the declared boundary/asymptotic conditions, analytic positive powers of the covariant Laplacian acting on a single curvature scalar integrate to boundary terms and therefore do not automatically add bulk local residual directions. The third can be nontrivial, but arbitrary functional freedom cannot be counted as finite RQIR rank without an explicit reconstruction/projection.

## W31-1 Linear-curvature bulk quotient

For

`S_lin = integral sqrt(g) [a0 + a1 Delta + ... + aN Delta^N] R`,

with the declared boundary conditions, verify symbolically/algebraically that all `n>=1` terms are integrated covariant Laplacians of scalars and are boundary contributions. After quotienting the classical `a0 R` EH term, the local bulk residual rank of this analytic linear-curvature sector is zero.

Signals:
- `linear_curvature_positive_laplacian_powers_are_boundary_terms_under_declared_conditions`
- `linear_curvature_analytic_bulk_residual_rank_after_EH_quotient_is_0`

Claim boundary: nonanalytic kernels, boundaries, and nonlinear curvature dependence are not removed by this result.

## W31-2 Published F2 generalized-EH identifiability

Read the frozen evidence table. F2 identifies the classical linear curvature content and gives IR/UV consistency requirements for `Rcal`, but the frozen public evidence does not provide a unique finite low-energy two-direction residual basis after baseline subtraction.

Signals:
- `F2_generalized_EH_not_frozen_as_two_independent_residual_coefficients`
- `IR_UV_consistency_does_not_define_unique_two_direction_projection`

## W31-3 No double counting with quadratic sector

The already-counted `R^2` and `Ricci^2` form factors and their first slopes cannot be recounted as generalized-EH directions.

Signal:
- `quadratic_form_factor_directions_not_recounted_as_generalized_EH`

## W31-4 Functional-freedom identifiability stress

Construct several inequivalent finite projections of a hypothetical nonlinear `Rcal` function into the two missing complement directions while keeping the same IR and UV endpoint constraints. Demonstrate that endpoint consistency alone permits inequivalent residual embeddings.

Signals:
- `endpoint_constraints_allow_inequivalent_residual_embeddings`
- `functional_freedom_without_projection_does_not_establish_finite_rank_closure`

This is a logical identifiability test, not a model for the true `Rcal`.

## W31-5 Optimistic closure counterfactual

Add two arbitrary transverse residual columns to a rank-4 quadratic image and verify that rank 6 can be achieved. Then classify this only as a **counterfactual mathematical possibility**, because the frozen F2 generalized-EH record has not supplied those two independently reconstructed columns.

Signals:
- `two_transverse_extra_columns_can_close_rank6_mathematically`
- `counterfactual_closure_does_not_count_as_F2_physical_evidence`

## W31-6 Exclusion gates

- no p6/R3 import;
- no cross-lineage splice;
- no polygon-QGR information.

Signals:
- `p6_R3_not_used_to_rescue_generalized_EH_rank`
- `information_firewall_pass`

## Aggregate decision

If all signals pass, the Wave-31 verdict is:

`BLOCKED_NO_TWO_INDEPENDENT_PUBLISHED_GENERALIZED_EH_BULK_RESIDUAL_DIRECTIONS_AFTER_GR_BASELINE_QUOTIENT`

This means central-projection closure is parked for the currently frozen F2 public object. It does not falsify the full generalized-EH sector. The next active route returns to Wave 28: obtaining or reconstructing the missing same-realization UV eigenvector/displaced-trajectory ensemble needed for the physical 6x3 J8 Jacobian.
