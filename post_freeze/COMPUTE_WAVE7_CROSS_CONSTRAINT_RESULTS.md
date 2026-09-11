# Compute Wave 7 — Cross-Constraint Results

**Source branch:** `post-freeze-cross-constraint-wave7`  
**GitHub Actions run:** `34654569955`  
**Status:** COMPLETE / 5 PRIMARY JOBS + AGGREGATOR SUCCESS

## Aggregate verdict

All required artifacts were present. The aggregator returned:

- `naive_same_field_normalized_KL_and_q4_scaling_need_extra_structure = true`;
- `RG_relevant_coordinates_require_full_rank_operational_Jacobian = true`;
- `finite_spectral_rank_needs_exact_structural_protection = true`;
- `finite_low_energy_data_do_not_fix_UV_growth = true`;
- `positive_spectral_plus_fixed_point_is_known_comparator = true`;
- `new_methodological_gate_found = true`;
- `candidate_new_QG_primitive_found = false`.

The new methodological gate is:

> Scheme/field/normalization consistency must be explicit before combining RG fixed-point scaling with spectral positivity; RG relevant coordinates must be operationally identifiable with full-rank prospective observables.

## A — normalized KL proxy versus naive q^-4 scaling

A positive normalized Euclidean Källén–Lehmann proxy was used,

`D(Q^2)=sum_i w_i/(Q^2+m_i^2)`, with `w_i >= 0` and `sum_i w_i = 1`.

At the largest sampled momentum,

- `Q^2 D(Q^2) = 0.99999997472`, approaching the expected normalized KL limit `1`;
- the comparison soft target `1/[Q^2(1+Q^2/M^2)]` gave `Q^2 D_soft = 9.999999e-8`, approaching `0`.

Therefore a standard normalized positive KL representation and a naive `1/Q^4` asymptotic law should not be imposed simultaneously on the same renormalized field without extra structure or a scheme/field distinction.

This is **not** a no-go against asymptotic safety. Current Lorentzian functional-RG literature explicitly finds positive/normalisable graviton spectral functions while connecting the infrared GR regime to an asymptotically safe UV regime. The lesson is methodological: spectral normalisation, anomalous scaling, field definition, Ward identities and renormalisation scheme must be matched consistently before an apparent asymptotic conflict is interpreted physically.

## B — operational identifiability of RG relevant coordinates

Three relevant parameters were assumed locally. Several prospective-observable Jacobians were tested:

- one observable: rank 1, nullity 2;
- two independent observables: rank 2, nullity 1;
- three observables but linearly dependent: rank 2, nullity 1; smallest singular value `9.26e-18`;
- three independent observables: rank 3, nullity 0; singular values approximately `1.32765, 1.10585, 0.57180`;
- five overcomplete observables: rank 3, nullity 0; singular values approximately `1.34874, 1.31275, 0.93279`.

A deliberately ill-conditioned full-rank example had condition number approximately `3.0e6`.

Hence closure of an `m`-dimensional UV critical surface requires at least `m` operationally independent prospective observables, full column rank of the sensitivity map, and acceptable conditioning. Merely counting observables is insufficient.

## C — robustness of exact finite spectral rank

For an exact three-atom positive measure, a `5 x 5` Hankel moment matrix had singular values approximately

`1.4684, 0.14184, 0.0045953, 2.10e-17, 1.22e-17`,

so the exact rank is 3.

Adding arbitrarily small noise made estimated rank threshold-dependent:

- at noise `1e-12`, a relative threshold `1e-12` estimated rank 4 while thresholds `>=1e-10` returned rank 3;
- at noise `1e-10`, thresholds `1e-12, 1e-10, 1e-8` returned ranks `5,4,3` respectively;
- at noise `1e-6`, estimates ranged from rank 5 to rank 3 depending on threshold;
- at noise `1e-4`, estimates ranged from rank 5 to rank 4 across the tested thresholds.

Therefore an exact finite-rank spectral principle would be strong, but it cannot be justified merely by a numerically low-rank fit to finite noisy data. The rank needs exact structural protection or derivation.

## D — finite low-energy data versus UV growth

An analytic counterexample was used:

`f_e(z)=1/(1+z) + epsilon z^(K+1)` with `K=8`.

Every member of the family has exactly the same Taylor coefficients through order 8 at the origin, but the deformation changes the large-|z| behaviour arbitrarily strongly.

Thus finite low-energy matching does not determine UV growth. A genuine all-order parent law needs an independent asymptotic/growth axiom, recursion rule or equivalent global condition.

## E — current spectral/RG comparator firewall

The coexistence of a positive graviton spectral function and an asymptotically safe fixed point is already an active known research route, not Candidate-Gravity novelty by itself.

Representative current literature anchors:

- Fehre, Litim, Pawlowski & Reichert, arXiv:2111.13232;
- Pawlowski, Reichert & Wessely, arXiv:2507.22169;
- Assant, Litim & Reichert, arXiv:2606.19321.

The 2025 work reports a self-consistent positive graviton spectral function with a massless peak and continuum and, in its physical on-shell scheme, unit total spectral weight. The 2026 work includes improved Ward-identity treatment and interpolation between classical GR and an asymptotically safe UV fixed point.

## Scientific synthesis

Wave 7 did not produce a new microscopic law. It did sharpen the admissibility architecture:

1. the same field/scheme/normalisation convention must be used across spectral and RG gates;
2. all RG-relevant directions must be prospectively identifiable by an independent operational Jacobian;
3. any claimed finite spectral rank needs structural protection, not numerical rank fitting;
4. finite low-energy data cannot substitute for a global growth/analyticity law;
5. spectral+RG coexistence is comparator territory unless RQIR produces a genuinely new quantitative cross-relation.

## Wave 8 target

The next step is a joint-closure test using gravitational dispersion/Regge information:

- quantify the finite subtraction/contact data left by a two-subtraction dispersion structure;
- impose a Regge-growth bound on crossing-symmetric local contact terms and count what freedom survives;
- compare an unlinked multi-sector parameterisation against a single finite latent primitive shared by RG, spectral and amplitude observables;
- fit only design observables and require a genuine holdout prediction;
- keep loop-induced running in the dispersive bookkeeping so that naive coefficient-sign tests are not mistaken for scale-invariant positivity statements.

External amplitude anchor: Häring & Zhiboedov, *Gravitational Regge bounds*, arXiv:2202.08280, which under stated assumptions derives gravitational dispersion relations with two subtractions and a schematic local growth bound not faster than `s^2`.
