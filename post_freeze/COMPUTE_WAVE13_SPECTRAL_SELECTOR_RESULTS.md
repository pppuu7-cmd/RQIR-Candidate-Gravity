# Compute Wave 13 — Spectral Selector Results

**Authoritative branch:** `post-freeze-spectral-selector-wave13`  
**Authoritative GitHub Actions run:** `34656845857`  
**Status:** COMPLETE / 5 PRIMARY JOBS + AGGREGATOR SUCCESS

## Aggregate verdict

All five predeclared signals were true:

- positive unit-weight continuum with fixed endpoint exponents and low moments still has a nullspace;
- five exact linear spectral sum rules still leave a positive continuum nullspace;
- nonlocal Stieltjes/dispersion holdouts resolve that static nullspace;
- fixed IR and UV power laws do not remove interior continuum freedom;
- these static conditions are admissibility/comparator gates, not new dynamics.

The aggregator therefore set:

- `positivity_normalization_IR_UV_asymptotics_and_finite_sum_rules_sufficient_for_unique_continuum = false`;
- `genuine_dynamical_equation_or_kernel_required = true`;
- `candidate_new_QG_primitive_found = false`.

## Endpoint + low-moment nullspace

Base density: `Beta(1.7,2.4)`.

A degree-3 deformation `q3` was constructed orthogonal to `1,x,x^2` under the base spectral weight, and positive densities

`rho_e = rho_0 [1 + epsilon q3(x)]`

were scanned for `epsilon=-0.8,-0.5,0,0.5,0.8`.

The constraints `m0,m1,m2` were preserved to

`max_change_m0_m1_m2 = 4.4408920985e-16`,

while

`m3_width = 0.00244240125752`.

All scanned densities remained positive and retained the same endpoint power exponents.

## Five exact sum rules

A degree-5 deformation `q5` orthogonal to all polynomials of degree <=4 preserved five independent moment constraints `m0...m4`.

Numerical preservation:

`max_change_constrained_m0_to_m4 = 6.6613381478e-16`.

Yet the next moment remained free:

`m5_width = 6.9038283027e-05`.

All scanned densities remained positive.

Thus a finite number of exact linear Ward/sum-rule-type constraints is not functionally complete for an infinite-dimensional continuum.

## Nonlocal dispersion holdouts

For the q3 null family the untouched Stieltjes observable

`F(Q^2)=integral rho(x)/(Q^2+x) dx`

was evaluated at `Q^2=0.02,0.1,1,10`.

Holdout widths were:

- `0.24931691714` at `Q^2=0.02`;
- `0.06314531985` at `Q^2=0.1`;
- `0.000589620273` at `Q^2=1`;
- `2.04028165e-07` at `Q^2=10`.

Maximum holdout width:

`0.24931691714`.

So densities invisible to the finite static constraints can differ strongly in genuinely nonlocal dispersive observables.

## IR/UV asymptotics

Using `s=x/(1-x)` gives a Beta-prime-type continuum on `(0,infinity)` with expected exponents

- IR: `a-1 = 0.7`;
- UV: `-(b+1) = -3.4`.

Across the positive null deformations the measured slope widths were only

- `IR_slope_width = 1.3750417604e-05`;
- `UV_slope_width = 4.9001968795e-05`.

Thus fixing IR threshold behavior and UV power-law decay constrains endpoint structure but not the interior spectral density.

## Scientific conclusion

Lorentzian-QG-inspired static spectral properties — positivity, unit total weight, fixed IR/UV power laws and finitely many exact Ward/sum-rule moments — do not uniquely reconstruct the continuum.

The missing parent law therefore cannot be a finite checklist of static spectral properties. It must be a dynamical flow, integral equation, functional equation or kernel that fixes the interior continuum and makes prospective predictions.

## Wave 14 target

Compare finite functional-equation architectures under frozen criteria:

1. local differential law;
2. causal Volterra integral law;
3. nonlinear Fredholm/self-consistency law;
4. functional-identity suppression of q3/q5 null modes;
5. uniqueness/bifurcation audit and comparator firewall.

A finite equation is not sufficient by itself: Wave 14 must explicitly test solution uniqueness and retain nonlocal holdouts. Any equation equivalent to known spectral-FRG, Schwinger-Dyson or bootstrap/dispersion machinery remains a comparator, not new QG physics.
