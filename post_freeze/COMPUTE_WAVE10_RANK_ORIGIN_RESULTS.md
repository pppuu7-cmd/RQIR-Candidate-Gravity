# Compute Wave 10 — Rank-Origin / Continuum Results

**Source branch:** `post-freeze-rank-origin-wave10`  
**GitHub Actions run:** `34655488993`  
**Status:** COMPLETE / 5 PRIMARY JOBS + AGGREGATOR SUCCESS

## Aggregate verdict

All predeclared signals were true:

- `finite_atomic_measure_has_fixed_Hankel_rank = true`;
- `positive_continuum_has_no_fixed_finite_Hankel_rank = true`;
- `finite_recurrence_implies_finite_rational_realization_in_proxy = true`;
- `finite_rational_rank_can_approximate_but_not_equal_continuum = true`;
- `finite_recurrence_fits_fail_continuum_holdouts = true`;
- `current_graviton_spectral_comparator_contains_continuum = true`.

The aggregator set:

- `exact_finite_atomic_rank_viable_as_generic_full_graviton_spectrum_target = false`;
- `finite_rank_still_useful_as_approximation_or_reduced_sector = true`;
- `candidate_new_QG_primitive_found = false`.

## Atomic versus continuum Hankel rank

For the three-atom positive measure with support `(0.1,0.3,0.7)` and weights `(0.25,0.50,0.25)`, the moment Hankel matrices saturated at exact rank 3. For example, at size `N=4`, the singular values were approximately

`1.1750, 0.08725, 0.0016199, 1.12e-17`,

and all larger scanned matrices kept only three non-negligible singular directions.

For the positive continuum `rho(x)=1` on `[0,1]`, the moment matrix is the Hilbert/Gram matrix

`H_ij = int_0^1 x^(i+j) dx = 1/(i+j+1)`.

Analytically it is strictly positive definite for every finite size because

`v^T H v = int_0^1 |p_v(x)|^2 dx > 0`

for every nonzero polynomial `p_v`. Hence its exact rank is full for every finite `N` and never saturates at a fixed finite value.

Numerically, the continuum singular values remain nonzero but become strongly ill-conditioned at large `N`, which is why the structural conclusion is based on the exact Gram argument rather than a floating-point rank threshold.

## Finite recurrence as a finite realization

The same three-atom sequence admits an exact three-dimensional linear realization

`m_n = c^T A^n b`

with diagonal `A=diag(0.1,0.3,0.7)`. Its characteristic polynomial gives the constant-coefficient rank-3 recurrence used in Wave 9.

Thus exact fixed spectral rank corresponds, in this proxy, to a finite rational/state-space realization. This is a genuine compression mechanism but an additional structural assumption.

## Finite rational approximation versus continuum

For the continuum Stieltjes transform

`F(Q^2)=int_0^1 dx/(Q^2+x)=log((Q^2+1)/Q^2)`,

finite Gauss-Legendre atomic approximants were evaluated at increasing rank. They approximate the Euclidean continuum increasingly well, but every finite approximation remains rational with finitely many simple poles, whereas the exact analytic continuation has logarithmic branch-point/cut structure.

Hence an excellent finite rational fit to finite data is not evidence for exact finite spectral rank.

## Finite-recurrence holdouts on continuum moments

Finite constant-coefficient recurrences of increasing order were fitted to exact continuum moments `m_n=1/(n+1)` using finite design windows and then tested on untouched higher moments.

Every finite order retained nonzero prospective holdout error. Larger orders improve the approximation but do not produce an exact fixed recurrence.

This cleanly distinguishes finite Prony/Padé-style compression from a genuine continuum-generating law.

## Current graviton spectral comparator

Recent Lorentzian quantum-gravity spectral calculations report a positive graviton spectral function with a massless one-graviton peak and a multi-graviton/scattering continuum:

- Fehre, Litim, Pawlowski & Reichert, arXiv:2111.13232;
- Pawlowski, Reichert & Wessely, arXiv:2507.22169;
- Assant, Litim & Reichert, arXiv:2606.19321.

The 2025 work explicitly uses the full nonperturbative scattering continuum in the self-consistent diagrams, and the 2026 work adds improved Ward-identity treatment and normalisable spectral functions across the GR-to-UV interpolation.

Therefore an exact finite-atomic spectral law is not an attractive generic target for the **full** graviton spectral function. This does not exclude finite rational approximations, finite-dimensional reduced sectors, or other quantum-gravity completions with different spectral organisation.

## Scientific synthesis

The search target changes:

> do not look for an exact finite list of graviton poles or a fixed finite Hankel rank; look for a **finite generative equation** whose solution is a positive continuum and that predicts all-order spectral/dispersion data.

This preserves the finite-parent-law objective while remaining compatible with continuum analytic structure.

## Wave 11 target

Wave 11 tests the architecture of such a continuum generator:

1. a finite differential law that generates a positive continuum density;
2. the induced non-constant-coefficient moment recurrence, which can close infinitely many moments without finite Hankel rank;
3. prospective Stieltjes/dispersion holdouts after fitting only finite design moments;
4. explicit deformations showing that the same finite low moments do not themselves derive the generator;
5. comparator firewall against FRG, Schwinger-Dyson, spectral bootstrap and standard parametric-density constructions.
