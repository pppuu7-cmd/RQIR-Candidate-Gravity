# Iter020A / G38-P preregistration and launch

Frozen before result inspection on 2026-09-12.

Purpose: validate implementation/provenance for the next independent comparator ingredient, stationary Ornstein-Uhlenbeck finite-correlation classical Gaussian Hamiltonian noise coupled through one fixed sum of local Pauli-axis observables.

For `C(t,s)=sigma2 exp(-|t-s|/tau)`, the integrated phase is Gaussian with exact variance `v(T)=2 sigma2 tau [T-tau(1-exp(-T/tau))]`. Every realization factorizes into a product unitary because the two local terms commute.

Frozen 12-lane checks:
- TP residual `<1e-10`;
- Choi minimum eigenvalue `>-1e-8`;
- evolved-state minimum eigenvalue `>-1e-8`, trace error `<1e-10`;
- analytic channel vs 80-point Gaussian random-unitary quadrature trace distance `<1e-10`;
- product-unitary factorization error `<1e-12`;
- output negativity from the fixed product input `<1e-10`;
- sampled OU covariance matrix minimum eigenvalue `>-1e-10`;
- non-semigroup finite-correlation signature `|v(2T)-2v(T)|/v(2T) > 0.02`.

Scope/claim lock: this is colored finite-correlation classical noise and a non-semigroup channel family. It is not yet an RCG-002 adversarial test and is not claimed to be non-Markovian in the stricter information-backflow sense.