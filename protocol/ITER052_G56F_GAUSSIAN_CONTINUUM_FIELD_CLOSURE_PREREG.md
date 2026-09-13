# Iter052 / G56-F — Gaussian continuum field-closure preregistration

Date frozen: 2026-09-13
Status: **FROZEN BEFORE IMPLEMENTATION/PRODUCTION**

## Objective
Test whether the already-qualified RCG-002 finite-size Gaussian kernel

`K_s(r) = erf(r/(sqrt(2)s))/r`

is internally consistent as a continuum weak-field source/kernel object, without importing a field equation, action, ansatz, coefficient, physical conclusion, or desired result from RQIR/KMQGB/QGR.

This is a mathematical/continuum closure prerequisite only. It is not a generally covariant gravity-theory gate.

## Frozen identities under test
For `r>0`, define

`rho_s(r) = (2*pi*s^2)^(-3/2) exp(-r^2/(2s^2))`.

The candidate kernel implies the exact source identity

`laplacian K_s(r) = -4*pi*rho_s(r)`

and the Gauss/enclosed-source identity

`-r^2 dK_s/dr = M_s(<r)`

with

`M_s(<r) = erf(r/(sqrt(2)s)) - sqrt(2/pi)*(r/s)*exp(-r^2/(2s^2))`.

These formulas are derived from the RCG-002 Gaussian kernel itself and are frozen before numerical production.

## Frozen panel
Six independent matrix lanes:
- `u=r/s = [0.35, 0.70, 1.20, 2.00, 3.00, 4.00]`;
- `s = [0.071, 0.113, 0.173, 0.257, 0.389, 0.541]` in deterministic lane pairing;
- three fixed unit-vector orientations per lane for independent Cartesian finite-difference Laplacians.

No panel element may be changed after result inspection.

## Frozen independent calculations and controls
Each lane must satisfy simultaneously:
1. analytic radial source identity exactly evaluated in double precision;
2. independent Cartesian five-point-per-axis finite-difference Laplacian of `K_s(|x|)` agrees with `-4*pi*rho_s` with relative error `<= 2e-5`;
3. the three Cartesian orientations agree in scaled Laplacian `s^3 laplacian K_s` within absolute spread `<= 2e-7`;
4. independent five-point radial derivative gives Gauss flux `-r^2 K_s'(r)` agreeing with analytic enclosed-source fraction within absolute error `<= 2e-8`;
5. independent numerical quadrature of `4*pi r^2 rho_s(r)` on `[0,12s]` gives normalization within absolute error `<= 2e-10` of unity;
6. `rho_s(r)>0`, `0<M_s(<r)<1`, and all reported values are finite;
7. scale collapse: `s*K_s(su)`, `s^3 rho_s(su)`, and the analytic scaled Laplacian depend on `u` only, checked against their dimensionless formulas to absolute error `<= 2e-12`;
8. wrong-sign source control must disagree with the numerical Laplacian by relative error `>= 1.5`;
9. wrong-width (`1.3s`) source control must disagree with the correct source at the lane point by relative difference `>= 0.05`.

Finite differences use frozen step `h=0.01*s`; Cartesian second derivatives use the standard five-point stencil independently along x,y,z. Radial first derivative uses the standard symmetric five-point stencil. Quadrature tolerances are `epsabs=1e-13`, `epsrel=1e-13`.

Aggregate requires exactly 6 structural-valid lanes and every frozen predicate true. Green CI alone is not PASS.

## Frozen interpretation
PASS label: `RCG002_GAUSSIAN_CONTINUUM_SOURCE_KERNEL_CLOSURE_VALIDATED_SCOPED`.
FAIL label: `G56F_FROZEN_CONTINUUM_FIELD_CLOSURE_RULE_NOT_MET`.
Technical/runtime/serialization failures are not scientific FAIL and may receive only minimal implementation repair with frozen science unchanged.

A terminal PASS qualifies only the smoothed isotropic weak-field continuum source/kernel relation already implicit in RCG-002. It does not establish a generally covariant field equation, relativistic dynamics, an action, a quantum measure/path integral, experiment, or complete quantum gravity. It does not raise programme readiness above 66% by itself; the next readiness point requires a separately preregistered constitution/covariance rubric.

## Next gate rule
Only after terminal G56-F classification may a dependent continuum/covariant constitution gate be defined. If G56-F fails scientifically, preserve the failure and localize the violated source/kernel identity; do not tune the kernel or thresholds to rescue PASS.