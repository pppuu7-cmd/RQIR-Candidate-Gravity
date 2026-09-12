# RCG-001 — Relational quantum response kernel

Status: `SEED`
Date: 2026-09-12

## Motivation from frozen RQIR only

RQIR requires one framework to address means, fluctuations, correlations/coherence and causal observables without identifying the interface with the expectation value `<T_mu nu>` alone. The smallest operational extension is therefore a response map with both a retarded coherent kernel and a positive fluctuation kernel.

This is not claimed to be a UV theory.

## Minimal variables

Work around a controlled background `gbar` and use relationally completed test functionals so that coordinate labels are not themselves observables.

Let `tau_a` denote a finite set of source observables obtained by smearing the renormalized stress tensor with conserved relational probes. Let `x_i` denote a finite set of gravity-side relational observables (clock phase, relative acceleration, curvature smear, channel phase, etc.).

The seed interface is

`x = x_GR + G R tau + sqrt(G*hbar) xi`,

with

- `R`: real retarded response matrix/kernel;
- `xi`: zero-mean quantum/interface fluctuation with covariance `N >= 0`;
- `Cov(x) = G*hbar N + G^2 R Cov(tau) R^T` at leading seed order.

For quantum information channels, source coherences are retained through the characteristic map

`Phi(k) = exp(i k^T G R tau - 1/2 G*hbar k^T N k)`

for the Gaussian seed. `N` is not assumed to be classical noise; operationally identical classical stochastic realizations must be quotiented out before any quantum claim.

## Why this is a useful seed rather than a conclusion

It is the lowest-complexity object that can simultaneously represent:

- Q1 clock/proper-time phase response via rows of `R`;
- Q2 superposed-source conditional response via source coherences;
- Q3 source rule through the dependence on the full source state rather than only its mean;
- Q4 gravity-mediated quantum channel through off-diagonal characteristic-function response;
- Q5 geometry fluctuations through `N`;
- Q6 causal structure through retarded support of `R`;
- Q7 EFT matching through the low-frequency/momentum expansion of `R` and `N`.

## Frozen seed gates for Iteration 001

G1. `G -> 0`: both coherent and fluctuation corrections vanish.

G2. `hbar -> 0`: intrinsic interface fluctuations vanish; the coherent response may remain classical and must reduce to the declared GR baseline after comparator subtraction.

G3. Positivity: `N` is positive semidefinite and total observable covariance has no negative eigenvalues.

G4. Causality: a discrete retarded implementation must be strictly lower-triangular (or equal-time convention explicitly frozen).

G5. Multi-channel identifiability: data from at least three non-collinear observable channels must be able to distinguish a coherent-response deformation from a pure additive-noise deformation under the frozen synthetic design.

G6. Comparator warning: if all surviving residuals can be reproduced by an ordinary classical stochastic kernel in the same domain, status remains `DEGENERATE`, not quantum gravity.

## Deliberately unresolved

- microscopic ontology;
- nonlinear completion;
- exact diffeomorphism constraints;
- strong-curvature regime;
- whether `N` is intrinsically quantum;
- whether any residual survives stochastic/hybrid comparator quotient.

These are promotion blockers, not assumptions to be filled by hand.
