# Iter020A / G38-P terminal result

Authoritative run `34704060723`, head `a1db86645204fd158057673e57518374e9434666`, aggregate job `103580959913`, summary artifact `10301152567`, digest `sha256:8642947c6b1c03689c35ed472ed994fe1cca2b3724c9320e07108dff4f4e0980`.

All 12 prospectively frozen implementation/provenance lanes were structurally valid and passed. Worst diagnostics:
- maximum TP residual `3.2265130554900103e-16`;
- minimum Choi eigenvalue `-7.571711465788335e-16`;
- minimum evolved-state eigenvalue `3.876781746185021e-10`;
- maximum trace error `2.220446049250313e-16`;
- maximum analytic-vs-Gaussian-quadrature trace distance `5.217356885430587e-16`;
- maximum product-unitary factorization error `1.3946387036943758e-14`;
- maximum negativity from the fixed product input `0.0`;
- minimum sampled OU covariance eigenvalue `9.221999867546514e-04`;
- minimum frozen non-semigroup defect fraction `0.17277287961612672` versus required `>0.02`.

Classification: `OU_COLORED_CLASSICAL_NOISE_IMPLEMENTATION_VALIDATED`.

Scope: stationary OU finite-correlation classical Gaussian Hamiltonian noise with one fixed sum of local Pauli observables. This validates a colored finite-correlation non-semigroup channel construction. It does not establish information-backflow non-Markovianity and does not test RCG-002.

Important identifiability note: at a single final time the channel depends on OU parameters only through the integrated phase variance `v(T)` and is therefore equivalent to the already-tested shared Gaussian phase-noise channel at that one time. Consequently the next nonredundant gate must be multi-time/trajectory based rather than another single-time adversarial search.