# Wave 28 — Same-Realization Jacobian Data Contract Certificate

Status: **CLOSED / CLEAN**

Authority run: `34664039842`
Authority compute commit: `c2a62afca8446f76747efffb7175622534645b77`
Frozen evidence commit: `05c58db44c03c0495e87f7c6f865f4dd09b6e638`

## Result

All six primary jobs and the fail-closed aggregator completed successfully. All nine preregistered scientific signals and all three supporting executable-contract checks were true.

## Positive result

F2 is not plot-only. Its published Appendix-H analytic fits provide a reusable central physical-limit representation of the momentum-dependent vertex/form-factor data. Therefore the central-output subproblem is substantially closed.

## Remaining J8/J9 requirements

For the three UV-relevant directions reported in F1, the first local sensitivity target is a `6 x 3` Jacobian from UV trajectory coordinates to frozen RQIR residual outputs.

- minimum one-sided first-order ensemble: `4` same-realization trajectories (central + one displacement in each independent UV direction);
- minimum symmetric central-difference ensemble: `7` trajectories (central + +/- displacement in each of three directions).

The frozen public record audited here does not expose the required numerical relevant-eigenvector basis, direction-resolved displaced F1/F2 trajectory ensemble, explicit F1/F2-to-six-RQIR projection, or propagated six-output covariance.

A synthetic nonlinear contract test recovered the intended `6 x 3` shape and yielded the expected second-order central-difference convergence: halving the step reduced error by a factor `4.0000000000000675`. This validates the executable derivation contract only and is not counted as physical evidence.

## Additional literature confirmation after freeze

The F1 paper itself states that the full stability matrix is not available because flow equations of higher couplings are unknown; two approximations to the stability matrix are therefore used to obtain critical exponents. This independently reinforces the frozen D28-2 distinction between published critical exponents and the explicit same-coordinate relevant-eigenvector basis required by J8.

## Frozen blocker

`BLOCKED_MISSING_F1F2_UV_EIGENVECTOR_BASIS_PLUS_DISPLACED_TRAJECTORY_ENSEMBLE_PLUS_SIX_OUTPUT_PROJECTION_AND_COVARIANCE`

## Next target

Use published F2 analytic fits to reconstruct every same-lineage central quantity that can be derived without raw arrays or displaced trajectories. Freeze those central observables and their fit-level uncertainty separately, so any future author-released trajectory ensemble can be plugged directly into the already-tested J8/J9 contract without redefining the target.
