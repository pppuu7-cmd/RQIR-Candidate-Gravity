# Wave 34 preregistration — Appendix-F partial projected Jacobian

Status: **FROZEN BEFORE COMPUTE**
Date: 2026-09-12
Branch: `appendix-f-projected-jacobian-wave34`

## Question

What is the maximum directional information that can be reconstructed from the published Appendix-F analytic equations without pretending that the missing full five-dimensional best-realization stability matrix has been recovered?

## Frozen subsystem

Use only published F1, F2, and F4 under the Table-3 Truncation-4 assumptions:

- active coordinates: `(mu, lambda3, g3)`;
- held coordinates: `lambda4=-0.11`, `g4=0.55`;
- `lambda5=lambda3`, `g5=g4`;
- anomalous dimensions set to zero;
- anchor: `(-0.23,-0.060,0.64)` in the active coordinates.

The `lambda3` flow is evaluated self-consistently with the F4 value of `partial_t g3/g3`.

## Predeclared tests

1. **anchor residual** — evaluate the three reconstructed beta functions at the rounded published anchor. A non-negligible residual blocks calling this three-equation restriction the published fixed point.
2. **conditional root** — with `lambda4,g4` held fixed, solve the three reconstructed equations for a nearby conditional root. Require numerical residual < `1e-8` and physical domain `mu>-1`, `g3>0`.
3. **projected Jacobian** — finite-difference the 3x3 conditional-flow Jacobian at the conditional root, report eigenvalues, rank, determinant and condition number.
4. **held-coordinate sensitivity** — perturb held `lambda4` and `g4` independently over ±5% and ±10%; re-solve the conditional root and quantify root/Jacobian/eigenvalue movement.
5. **embedding no-go** — prove by dimension and explicit counterexample that a 3x3 conditional Jacobian cannot determine the missing two rows/columns or the orientation of a 3D relevant subspace in the full 5D coupling space.
6. **published-spectrum mismatch diagnostic** — compare only at the level of counts/real parts; no matching or tuning to the published 5D spectrum is allowed.
7. **information firewall** — no polygon/KMQGB-derived QGR equation, architecture, fit or repair.

## Interpretation rule

A successful conditional root/Jacobian is useful **partial surrogate information only**. It cannot be promoted to `BEST_REALIZATION_J8` because freezing `(lambda4,g4)` removes feedback through F3/F5 and does not define an invariant subspace of the full flow.

Wave 34 PASS means the maximal honest partial reconstruction is reproducible and its limitations are quantified.
