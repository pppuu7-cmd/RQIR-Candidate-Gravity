# Wave 32 — F1 Relevant-Direction Basis Reconstructibility Audit

Status: **PREREGISTERED BEFORE GITHUB COMPUTE**

## Frozen authorities

- RQIR Core v1.0 remains frozen.
- Wave-22 six-coordinate bank remains immutable.
- Wave-28 J8/J9 contract remains the active target: three independent UV-relevant directions must seed displaced same-realization trajectories.
- Wave-31 parks central-F2 projection closure.
- F1 evidence is frozen in `evidence/WAVE32_F1_RELEVANT_BASIS_EVIDENCE.json`.
- No polygon/KMQGB-derived QGR information may enter.

## Question

Can the published F1 object supply a reusable numerical basis for the three UV-relevant directions needed by the Wave-28 displaced-trajectory Jacobian, or does the public record provide only spectra/dimension counts without orientation information?

## W32-1 Frozen evidence gate

Verify from the frozen evidence that the best displayed truncation uses five coordinates `(mu,lambda3,lambda4,g3,g4)`, reports three attractive real directions for the displayed closure, but does not publish a reusable numerical stability matrix or right-eigenvector basis.

Signals:
- `F1_best_truncation_dimension_is_5`
- `F1_displayed_relevant_real_dimension_is_3`
- `F1_public_record_lacks_reusable_numeric_relevant_eigenbasis`

## W32-2 Spectrum does not determine eigenvectors

Construct real 5x5 matrices with exactly the same real spectrum as the published `bar_B` exponents: one real attractive eigenvalue, one attractive complex-conjugate block, and two repulsive real eigenvalues. Apply random orthogonal similarity transforms. All matrices preserve the spectrum and attractive-subspace dimension while rotating the three-dimensional real attractive invariant subspace in five dimensions.

Measure principal angles between the attractive subspaces of independent draws.

Signals:
- `same_critical_exponents_allow_inequivalent_relevant_subspaces`
- `critical_exponents_alone_cannot_define_displacement_basis`

## W32-3 Approximation-A versus approximation-B ambiguity

Repeat the spectral construction for both published spectra `bar_B` and `tilde_B`. Show that even fixing the eigenvalues of each approximation leaves orientation unconstrained. The published difference between spectra therefore cannot be converted into a displacement-direction uncertainty without matrices/eigenvectors.

Signals:
- `both_published_spectra_are_orientation_nonidentifying`
- `spectral_difference_does_not_supply_basis_covariance`

## W32-4 Closure dependence

The full stability matrix is unavailable because higher-coupling flows are unknown. Across identification schemes, `bar_B` keeps three attractive directions while `tilde_B` can yield one or three. Record this as a dimensional/closure uncertainty, not an eigenbasis.

Signals:
- `full_stability_matrix_blocked_by_unknown_higher_coupling_flows`
- `closure_choice_changes_relevant_dimension_in_one_approximation`

## W32-5 Analytic-IR surrogate firewall

F1 section 6 uses analytic flow equations and sets anomalous dimensions to zero for IR trajectories. This is qualitatively related but not identical to the best full momentum-dependent realization. Therefore those analytic flows may be used for method development or a separately labelled surrogate study, but must not silently substitute for the best-realization J8 displacement basis.

Signals:
- `analytic_IR_flow_is_not_same_realization_as_best_F1_truncation`
- `analytic_surrogate_not_promoted_to_physical_J8_basis`

## W32-6 Minimum new FRG object

Freeze the minimal object sufficient to unblock displacement construction at the approximation level:

1. ordered five-coordinate convention;
2. fixed-point vector;
3. one explicit numerical 5x5 approximate stability matrix (`bar_B` or `tilde_B`) under a frozen closure, or equivalently its normalized right eigenvectors;
4. normalization/sign/phase convention for the one real and one complex-pair relevant modes;
5. beta-flow engine under the same closure for central and displaced trajectories;
6. regulator/truncation variants if J9 uncertainty is to be propagated.

Signals:
- `explicit_matrix_or_right_eigenvectors_are_minimum_orientation_object`
- `J8_displacement_coordinates_remain_blocked_without_orientation_object`

## W32-7 Information firewall

Signal: `information_firewall_pass`.

## Aggregate decision

If all preregistered signals pass:

`BLOCKED_MISSING_REUSABLE_F1_RELEVANT_EIGENVECTOR_BASIS_OR_NUMERIC_APPROXIMATE_STABILITY_MATRIX_IN_SAME_CLOSURE`

This is narrower than saying “F1 has no relevant directions”: F1 strongly supports the existence and approximate dimension of the UV critical surface. The missing object is the numerical orientation needed to perturb the actual flow in three independent directions.

## Next route

If Wave 32 closes cleanly, Wave 33 will build an executable FRG-basis ingest / displaced-trajectory specification and test the maximum same-lineage surrogate computation reproducible from Appendix-F analytic flows, explicitly labelled as surrogate and never promoted to the best-realization physical J8 result.