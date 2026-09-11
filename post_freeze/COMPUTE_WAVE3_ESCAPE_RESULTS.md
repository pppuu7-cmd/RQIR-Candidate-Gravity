# Compute Wave 3 — Escape-Route Results

**Branch:** `post-freeze-escape-route-wave3`  
**GitHub Actions run:** `34652985909`  
**Status:** COMPLETE / ALL FOUR PRIMARY JOBS + AGGREGATOR SUCCESS  
**Scope:** post-freeze two-point/prescription/higher-point filters; not a UV-completion theorem.

## Aggregate result

All six predefined signals were true:

- spectral purity fixes the positive-spectral TT two-point to the GR pole;
- spectral purity does not fix higher-point interactions;
- exponential UV softening conflicts with a standard additive positive spectral correction at fixed GR pole residue;
- a time-symmetric response prescription has negative-time support;
- the retarded prescription has zero negative-time support in the proxy;
- curvature-cubic operators alter higher points without changing the quadratic propagator.

## I — positive spectral purity

Assume a physical TT Euclidean two-point function of the form

`D(Q^2)=1/Q^2 + sum_i w_i/(Q^2+M_i^2)`, with `w_i >= 0`,

and fix the unit-residue massless pole to the GR value.

If the extra spectral support is set to zero, all `w_i=0`, then

`D(Q^2)=1/Q^2`

exactly in this two-point sector.

Thus under ordinary positive spectral assumptions:

> a genuine two-point deviation from the pure GR pole requires additional positive spectral support — extra states, resonances or continuum — unless some other assumption is changed.

This is a useful two-point rigidity statement, but it does **not** determine higher-point vertices.

## J — exponential entire UV softening versus positive spectrum

Target proxy:

`D_entire(Q^2)=exp(-ell^2 Q^2)/Q^2`.

With the same unit GR massless pole and nonnegative additive spectral density,

`D_KL(Q^2)=1/Q^2 + integral rho(mu^2)/(Q^2+mu^2)`, `rho>=0`,

so for every `Q^2>0`

`D_KL(Q^2) >= 1/Q^2`.

But for every `ell>0`,

`D_entire(Q^2) < 1/Q^2`.

Therefore this exponentially softened target cannot be represented by the stated standard positive-spectral form with the same massless residue.

**Interpretation:** ghost-free-looking entire UV softening is not a free consequence of ordinary positive spectral physics. It requires changing at least one assumption — spectral representation, inner-product/pole interpretation, subtraction structure, or another microscopic ingredient.

This is a scoped statement about this proxy, not a universal no-go for nonlocal gravity.

## K — time-symmetric prescription support

Linear response proxy:

`G_R(t)=theta(t) sin(Omega t)/Omega exp(-epsilon |t|)`

and

`G_sym=(G_R+G_A)/2`.

Numerical result for `Omega=1`, `epsilon=0.03`:

- retarded negative-time L2 fraction: **0.0**;
- time-symmetric negative-time L2 fraction: **0.5000000000000006**;
- maximum negative-time absolute retarded response: **0.0**;
- maximum negative-time absolute symmetric response: **0.4771991**.

This does not model a full fakeon/Lee-Wick gravity construction. It quantifies the causal-support price of replacing a purely retarded linear response by a time-symmetric prescription.

Any such gravity mechanism must therefore pass RQIR Q6/G4 at the operational response level rather than treating its pole prescription as automatically causal.

## L — higher-point visibility with an unchanged propagator

Around flat space, curvature starts at `O(h)`.

Therefore an invariant with `n` powers of curvature starts at `O(h^n)`:

- curvature-squared can enter the quadratic action and alter the propagator;
- curvature-cubic starts at `O(h^3)` and can alter three- and higher-point vertices while leaving the two-point propagator unchanged;
- curvature-quartic starts at `O(h^4)`, etc.

Hence even an exactly GR-like two-point spectrum does **not** uniquely fix the interacting theory.

But this is not automatically new quantum gravity: curvature-cubic and higher operators are already part of ordinary gravitational EFT/C5 unless a new principle fixes their coefficients or relations.

## Escape-route synthesis

For a C5-distinct **two-point** deformation with the unit GR pole retained, the tested routes expose a no-free-lunch structure:

1. **ordinary positive spectrum:** add physical spectral support (new states/continuum);
2. **UV-softened/no-new-pole form factor:** depart from the standard positive additive spectral representation or add other microscopic structure;
3. **modified pole prescription:** pay a nontrivial causal/response-consistency burden;
4. **leave the two-point sector unchanged:** novelty moves to higher-point vertices, where ordinary C5 EFT already has coefficient freedom.

This does not prove these four routes exhaust all quantum gravity. It is the current RQIR-guided design map for the lowest-cost directions tested so far.
