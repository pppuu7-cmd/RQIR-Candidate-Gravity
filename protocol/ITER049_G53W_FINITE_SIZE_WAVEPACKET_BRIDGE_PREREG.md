# ITER049 / G53-W — finite-size Gaussian wavepacket weak-field bridge (preregistration)

This protocol is frozen **before implementation and before production output**.

## Question

Does the point-particle weak-field branch interaction used by RCG-002 admit a controlled finite-size extension for isotropic Gaussian wavepackets, with a verified analytic/numerical bridge and the correct point-particle limit?

For two normalized isotropic Gaussian packets with per-coordinate widths `sigma_A`, `sigma_B`, relative width `s=sqrt(sigma_A^2+sigma_B^2)` and centre separation `R`, the frozen analytic kernel is

`K_gauss(R,s) = erf(R/(sqrt(2)*s))/R`.

An independent Fourier-space quadrature uses

`K_num = (2/pi) integral_0^infinity exp(-x^2/2) sinc(x R/s) dx / s`.

## Frozen panel and rules

Eight deterministic `R/s` controls are fixed: `{1, 1.5, 2, 3, 4, 6, 8, 12}`. In every lane:

1. Numerical Fourier quadrature vs analytic Gaussian kernel relative discrepancy `<=1e-10`.
2. Kernel is positive and finite.
3. Point-particle ratio `K_gauss / (1/R) = erf(R/(sqrt(2)s))` is in `(0,1]` and increases toward one over the ordered frozen ratio panel.
4. For `R/s >= 8`, point-particle relative discrepancy must be `<=1e-12`.
5. On the fixed four-branch geometry `(0.45,0.62,0.57,0.48) m`, using `s=min(d_ij)/(R/s)`, the finite-size cross-difference must converge to the point cross-difference; at `R/s>=8` relative discrepancy `<=1e-10`.
6. Equal-distance four-branch geometry is an exact nonlocal-phase null control to absolute error `<=1e-12`.
7. No comparator fitting, no target-conditioned choice of width, and no post-hoc threshold changes.

## Frozen classification

All 8 lanes valid and the aggregate monotonic/point-limit rules pass:

`FINITE_SIZE_GAUSSIAN_WAVEPACKET_WEAK_FIELD_BRIDGE_VALIDATED`

Otherwise:

`G53W_FROZEN_RULE_NOT_MET`

## Readiness rule frozen before output

G53-W alone cannot change readiness. Programme readiness may move `64% -> 65%` only if **both** G52-H and G53-W terminate PASS under their respective preregistered rules, closing one combined microscopic weak-field bridge rubric. Any FAIL/BLOCKED leaves readiness at 64%.

## Interpretation lock

A PASS validates only this Gaussian finite-size weak-field toy bridge and its point-particle limit. It is not a covariant continuum quantum-gravity dynamics, does not derive the gravitational field measure, and does not establish new physics.
