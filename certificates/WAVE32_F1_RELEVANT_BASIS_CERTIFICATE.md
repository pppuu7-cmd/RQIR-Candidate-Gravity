# Wave 32 — F1 Relevant-Direction Basis Reconstructibility Certificate

Status: **FROZEN CLEAN RESULT**

Date: 2026-09-12

## Authority

- Branch: `f1-relevant-basis-wave32`
- Evidence commit: `b0514e579cf978139180f9969389579147cdd0e4`
- Preregistration commit: `20a0f8d8827831656dac25983be915bdcd473b3a`
- Compute commit: `7c1e7d7e88c88c69cc50a8af9198e7130c85b035`
- GitHub Actions run: `34665724676`
- Primary jobs: 7/7 SUCCESS
- Aggregator: SUCCESS
- All preregistered signals: TRUE

## Frozen F1 object

Best displayed truncation coordinates:

`(mu, lambda3, lambda4, g3, g4)`

Fixed point:

`(-0.45, 0.12, 0.028, 0.83, 0.57)`

Published critical-exponent spectra for the displayed closure:

- `bar_theta = (-4.7, -2.0 +/- 3.1 i, 2.9, 8.0)`
- `tilde_theta = (-5.0, -0.37 +/- 2.4 i, 5.6, 7.9)`

Both displayed spectra have a three-dimensional attractive real invariant sector. The paper explicitly states that the full stability matrix is unavailable because flows of higher couplings are unknown; the public object used here does not provide numerical approximate matrices or right eigenvectors.

## Numerical non-identifiability result

Using real 5x5 matrices with exactly the published `bar_theta` spectrum and random orthogonal similarity transforms:

- maximum principal angle between equally spectral three-dimensional attractive subspaces over the frozen stress test: **1.5700599956035182 rad** (~89.96 deg)
- median maximum principal angle: **1.2951612075091465 rad** (~74.21 deg)

Thus an identical critical-exponent spectrum can coexist with strongly different relevant-subspace orientations. Eigenvalues/dimension counts do not define physical displacement coordinates.

The same orientation non-identifiability holds separately for both published stability-matrix approximations.

## Same-realization boundary

F1 Section 6 uses analytic flow equations for simplicity and sets anomalous dimensions to zero. This is scientifically useful as a surrogate flow, but it is not the same best full momentum-dependent realization and is not promoted to physical J8 evidence.

## Minimum orientation object

To unblock the approximation-level displacement engine one needs, under one frozen closure:

1. ordered five-coordinate convention;
2. fixed-point vector;
3. explicit numerical 5x5 approximate stability matrix or equivalent normalized right-eigenvector basis;
4. normalization/sign/phase convention for one real relevant mode and the complex-pair real plane;
5. beta-flow engine under the same closure for central and displaced trajectories;
6. regulator/truncation/closure variants for J9 uncertainty.

## Scientific verdict

F1 strongly supports the existence and approximate dimension of a UV critical surface, but the frozen public record does not provide the numerical orientation object required by Wave 28 to launch three independent same-realization displacement directions. Critical exponents alone cannot substitute for that object.

## Blocking object

`BLOCKED_MISSING_REUSABLE_F1_RELEVANT_EIGENVECTOR_BASIS_OR_NUMERIC_APPROXIMATE_STABILITY_MATRIX_IN_SAME_CLOSURE`

## Next target

Wave 33: create an executable FRG basis/trajectory ingest contract and separately reconstruct the maximum Appendix-F analytic surrogate eigensystem that can be reproduced from published equations. The surrogate remains explicitly `SURROGATE_NOT_J8`.