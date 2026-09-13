# Iter054 / G56-F2 — robust Gaussian continuum field-closure replacement preregistration

Date frozen: 2026-09-13
Status: **FROZEN BEFORE IMPLEMENTATION/PRODUCTION**

## Historical lock
Iter052 / G56-F remains terminal `G56F_FROZEN_CONTINUUM_FIELD_CLOSURE_RULE_NOT_MET`. Iter053 / G56-D diagnosed a local blind interval in its single-point wrong-width control. G56-F2 is a **new replacement gate**, not a retry/rescore/rescue of G56-F. No Iter052 threshold, lane, result, or classification is altered.

Programme readiness is 66% before this gate and **cannot increase above 66% from G56-F2 alone**. Theory established remains 0%.

## Objective
Prospectively test the RCG-002 isotropic Gaussian weak-field source/kernel closure on a new held-out numerical panel using three independent streams:
1. Cartesian/radial real-space differential identities;
2. independent Fourier-space reconstruction of the kernel/source relation;
3. global profile-level negative controls that cannot be defeated by a single radial density crossing.

This is a mathematical weak-field continuum closure gate only. It is not a generally covariant gravity theory, relativistic dynamics, an action, a quantum measure/path integral, or complete QG.

## Frozen definitions
`K_s(r) = erf(r/(sqrt(2)s))/r`

`rho_s(r) = (2*pi*s^2)^(-3/2) exp[-r^2/(2s^2)]`

Expected identities:
`laplacian K_s = -4*pi*rho_s`

`-r^2 dK_s/dr = M_s(<r)`

where `M_s(<r)=erf(u/sqrt(2))-sqrt(2/pi) u exp(-u^2/2)`, `u=r/s`.

Fourier convention:
`Ktilde_s(k)=4*pi exp[-s^2 k^2/2]/k^2`,
so
`s K_s(su) = (2/(pi*u)) Integral_0^infinity exp(-x^2/2) sin(u x)/x dx`.

## Stream R — new held-out real-space panel
Frozen eight lanes:
`u=[0.27,0.58,0.97,1.47,2.18,2.87,3.56,4.43]`
`s=[0.089,0.131,0.197,0.269,0.347,0.431,0.523,0.619]`

These are distinct from the Iter052 and Iter053-D3 panels. Use the same three fixed Cartesian orientations as G56-F and five-point stencils with frozen `h=0.012*s`.

Each lane must satisfy:
- worst Cartesian Laplacian relative error `<=2e-5`;
- orientation spread in `s^3 laplacian K_s` `<=2e-7`;
- radial Gauss-flux absolute error `<=2e-8`;
- source normalization on `[0,12s]` absolute error `<=2e-10`;
- scale-collapse errors for `sK`, `s^3 rho`, `s^3 laplacian` each `<=2e-12`;
- wrong-sign source control relative discrepancy `>=1.5`;
- positivity/range/finite checks.

All 8 lanes must pass.

## Stream S — independent spectral reconstruction
On the same frozen eight `u` values, independently of Stream R finite differences, numerically evaluate
`Q_spec(u)=(2/(pi*u)) Integral_0^12 exp(-x^2/2) sin(u*x)/x dx`
with adaptive quadrature `epsabs=epsrel=1e-13` and the continuous `x->0` integrand limit `u`.

Require for all eight values:
- `|Q_spec(u) - erf(u/sqrt(2))/u| <=2e-11`;
- spectral source multiplier identity `x^2 * [4*pi exp(-x^2/2)/x^2] = 4*pi exp(-x^2/2)` on frozen `x=[0.13,0.37,0.79,1.31,2.07,3.11,4.29,5.33]` with relative error `<=2e-14`;
- wrong-sign spectral source control relative discrepancy `>=1.5` at every x;
- all values finite.

## Stream G — global non-degenerate width controls
Freeze alternative width factors `q=1.3` and `q=0.77`. Define dimensionless radial source profile
`p_q(u)=4*pi*u^2 exp[-u^2/(2q^2)] / [(2*pi)^(3/2) q^3]`.

Using adaptive quadrature on `[0,10]`, require for each q:
- normalization within `2e-10` of unity;
- global L1 separation `Integral |p_q-p_1| du >=0.25`;
- second-moment ratio agrees with exact `q^2` to absolute error `<=2e-9`;
- `|q^2-1| >=0.30`;
- profiles positive where `u>0` and all values finite.

These controls are global by construction and do not depend on choosing a radial point away from an equality crossing.

## Aggregate rule
Exactly three structural-valid artifacts, one from each stream R/S/G, are required. Every frozen predicate must be true.

PASS label: `RCG002_GAUSSIAN_CONTINUUM_SOURCE_KERNEL_CLOSURE_VALIDATED_ROBUST_REPLACEMENT_SCOPED`.

FAIL label: `G56F2_FROZEN_ROBUST_CONTINUUM_FIELD_CLOSURE_RULE_NOT_MET`.

Technical/runtime/serialization failures are not scientific FAIL and may receive only minimal implementation repair with all science criteria frozen.

## Interpretation ceiling
A PASS would close only the isotropic Gaussian weak-field source/kernel continuum mathematics with real-space, spectral, and global-control redundancy. It would not establish general covariance, a metric field equation, nonlinear GR dynamics, quantization/measure closure, experiment, new physics, or full quantum gravity.

After terminal G56-F2 classification, the next scientifically distinct layer may be a separately preregistered gravity-theory constitution/covariance gate. Only that later rubric may be eligible to move programme readiness above 66%.

Scope lock: no physical assumptions/results imported from QGR/KMQGB/RQIR; methodology and generic mathematical tools only.