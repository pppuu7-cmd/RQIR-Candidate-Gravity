# Wave 34 — Appendix-F Surrogate Audit Certificate

**Status:** PASS / RECONSTRUCTION INCONCLUSIVE / `SURROGATE_NOT_J8`  
**Authoritative run:** `34667338160`  
**Authoritative head:** `66fcb4f8f43e44ce5f1e51b34352edcde94887ea`  
**Branch:** `appendix-f-surrogate-wave34`

## Audit history

The first run failed only because two metadata/firewall scripts resolved repository-root files relative to `compute_wave34/`. Commits `cbe76f288c94f55ab97941010740e6e9ec2825f5` and `66fcb4f8f43e44ce5f1e51b34352edcde94887ea` fix path resolution only. No equation, coefficient, search box, threshold, root criterion or scientific signal was changed.

## Execution result

All nine primary jobs and the fail-closed aggregator passed. All **27** preregistered signals are true.

The source-faithful audit used the printed Appendix-F F1–F5 equations under the frozen Truncation-4 assumptions:

- `eta_phi_i = 0`;
- derivative-expansion gravitational couplings at `p^2=0`;
- `lambda5=lambda6=lambda3`;
- `g5=g6=g4`;
- displayed Table-3 point `(-0.23,-0.060,-0.11,0.64,0.55)`.

No printed coefficient was altered to improve agreement.

## Quantitative result

- accepted nearby raw-residual roots in the frozen multistart box: **0**;
- flow infinity norm at the rounded Table-3 point: **1,524,939,869.9257135**;
- numerical Jacobian condition number there: **82,528,594,368.20105**;
- permutation/conjugation-invariant mismatch to the published first stability spectrum: **2,750,428,028.180549**;
- residual-width induced across the frozen decimal-rounding cell: **119,325,281.72329617**.

The finite-difference and rounding scans completed successfully and the discrepancy was retained rather than tuned away.

## Scientific interpretation

The printed local/analytic Appendix-F system is useful for qualitative provenance and for documenting the published closure, but the present source-faithful reconstruction is **not numerically adequate as an end-to-end J8 surrogate**. In particular, the displayed rounded point plus printed equations do not provide a reusable stable orientation object from which physical displaced trajectories should be generated.

This is not evidence against the full momentum-dependent F1 calculation. The paper itself separates the local analytic projection from the higher-quality momentum-dependent computation and warns that local projection can incur large errors.

## Frozen status

`SURROGATE_PRINTED_SYSTEM_RECONSTRUCTION_INCONCLUSIVE_NO_RAW_RESIDUAL_ROOT_IN_FROZEN_BOX`

Physical J8 remains:

`BLOCKED_MISSING_BEST_REALIZATION_5X5_STABILITY_MATRIX_OR_RIGHT_EIGENVECTOR_BASIS`

## Route decision

Do **not** fit Appendix-F coefficients or silently replace the best realization with this surrogate.

Next priority:

1. search later same-lineage FRG vertex-expansion publications, supplementary data and public code for a reusable numerical stability matrix/right-eigenvector basis;
2. identify whether a later truncation publishes enough beta-function/Jacobian data to reconstruct the relevant subspace in the same realization;
3. if not, specify the minimal fresh FRG calculation required to generate the 5x5 orientation object and seven displaced trajectories.
