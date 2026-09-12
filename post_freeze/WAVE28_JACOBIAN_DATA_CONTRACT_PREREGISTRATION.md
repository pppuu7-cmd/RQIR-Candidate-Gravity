# Wave 28 — Same-Realization Jacobian Data-Availability / Derivation Contract Audit

Status: **PREREGISTERED BEFORE GITHUB COMPUTE**

## Frozen authorities

- Wave-22 holdout bank is immutable.
- Parent-Law Acceptance Protocol v1 is immutable.
- Wave-27 blocker is frozen as `BLOCKED_MISSING_SAME_REALIZATION_UV_TO_RQIR_SIX_DIRECTION_JACOBIAN_WITH_PROPAGATED_UNCERTAINTY`.
- The only target lineage in this wave is the F1+F2 `fluctuation_vertex` lineage. E1/L1 or KMQGB/polygon numerical objects may not fill missing F1+F2 data.

## Scientific question

Does the frozen public F1+F2 record expose enough numerical information to construct, reproducibly and without cross-lineage splicing,

`J_ai = d Delta_a^RQIR / d u_i`,

where `a=1..6` corresponds to `[c3,d3,e4,f4,s2,s0]` and `u_i` are the independent UV-relevant trajectory coordinates?

F1 reports three attractive/relevant directions in the audited vertex truncation. Therefore the first local target is a 6x3 sensitivity matrix.

## Frozen evidence statements

1. F1 publishes a non-Gaussian UV fixed point, critical exponents, stability/truncation comparisons, and UV-finite trajectories to a classical-GR IR regime.
2. F2 publishes fully momentum-dependent three- and four-graviton information in the physical limit and Appendix H provides analytic fit functions with numerical best-fit coefficients; the fits reproduce the numerical data to a few-percent level.
3. In the frozen public search, no article-level Data Availability statement, Supplemental-data link, or paper-specific public source repository containing the underlying trajectory/vertex arrays was identified for F2.
4. The frozen public record inspected here does not expose a set of same-realization trajectories independently displaced along each of the three UV-relevant directions and propagated to the F2 physical-limit observables.
5. F2 supplies a mapping from graviton scattering couplings to diffeomorphism-invariant effective-action structures, but no frozen publication supplies the additional explicit projection from those structures to all six Wave-22 RQIR residual proxy coordinates.
6. F1 contains truncation/identification stability studies and F2 quotes fit accuracy, but the frozen public record does not propagate these variations through a six-output UV-to-RQIR Jacobian/covariance.

These are data-availability statements for the frozen evidence set, not claims that unpublished author data do not exist.

## D28 gates

### D28-1 Central physical-limit representation
PASS if reusable numerical arrays or explicit analytic fits exist for the needed physical-limit vertex/form-factor functions.

Predeclared status: `PASS_ANALYTIC_FITS_AVAILABLE` based on F2 Appendix H.

### D28-2 UV-coordinate basis
PASS requires explicit numerical relevant eigendirections/eigenvectors in the same trajectory coordinate basis used for downstream integration. Critical exponents alone are insufficient.

Predeclared status: `BLOCKED_EXPLICIT_RELEVANT_EIGENVECTOR_BASIS_NOT_FROZEN`.

### D28-3 Trajectory ensemble for derivatives
For `r=3`, a one-sided first-order Jacobian needs at least `1+r=4` same-realization trajectories (central plus one independent displacement per direction). A symmetric central-difference Jacobian needs `1+2r=7` trajectories.

PASS requires a published/reproducible ensemble sufficient to perturb each independent UV direction while keeping the realization/truncation fixed.

Predeclared status: `BLOCKED_MISSING_SAME_REALIZATION_TRAJECTORY_ENSEMBLE`.

### D28-4 Six-output projection
PASS requires an explicit deterministic map from the physical F1/F2 output basis into all six frozen RQIR residual directions, with conventions fixed before fitting.

Predeclared status: `BLOCKED_MISSING_F1F2_TO_SIX_RQIR_PROJECTION`.

### D28-5 J9 uncertainty propagation
PASS requires regulator/truncation/scheme variants propagated through the same J8 map to a six-output covariance/envelope.

Predeclared status: `BLOCKED_MISSING_PROPAGATED_SIX_OUTPUT_COVARIANCE`.

### D28-6 Reproducible machine-readable source object
PASS requires raw arrays, machine-readable fit coefficients, or code sufficient to reproduce the required central and displaced trajectories. Central analytic fits count only for the central-output subgate, not for the displaced-trajectory ensemble.

Predeclared status: `PARTIAL_CENTRAL_FITS_BUT_NO_FROZEN_DISPLACED_DATASET`.

### D28-7 Anti-splice
E1's C3 bridge, L1 Lorentzian spectral data, or KMQGB/polygon objects cannot be used to manufacture missing F1/F2 Jacobian columns.

Predeclared status: PASS firewall.

## Executable derivation contract

If the missing data become available, J8 shall be computed prospectively as follows:

1. freeze UV coordinate vector `u=(u1,u2,u3)` and its numerical eigenvector basis;
2. freeze central trajectory `u0`;
3. run symmetric displacements `u0 +/- h_i e_i`, `i=1..3`, in the identical truncation/regulator;
4. propagate each trajectory to the same k=0 physical 2/3/4-point representation;
5. apply the frozen six-output projection `P_RQIR`;
6. estimate columns `J[:,i]=(Delta(u0+h_i e_i)-Delta(u0-h_i e_i))/(2 h_i)`;
7. repeat at a second step size to diagnose finite-difference nonlinearity;
8. repeat across preregistered regulator/truncation variants and propagate the ensemble to a covariance on J and on the six predicted residual outputs;
9. only then test combined Ward+J transversality/rank against frozen Wave-22 observables.

## Aggregate signals

- central_physical_fits_available
- critical_exponents_do_not_substitute_eigenvectors
- minimum_one_sided_trajectory_count_is_4
- minimum_symmetric_trajectory_count_is_7
- public_same_realization_derivative_ensemble_missing
- explicit_six_output_projection_missing
- propagated_six_output_covariance_missing
- central_fit_availability_does_not_close_J8
- anti_splice_firewall_pass

If all signals are true, the next blocker is sharpened to:

`BLOCKED_MISSING_F1F2_UV_EIGENVECTOR_BASIS_PLUS_DISPLACED_TRAJECTORY_ENSEMBLE_PLUS_SIX_OUTPUT_PROJECTION_AND_COVARIANCE`.
