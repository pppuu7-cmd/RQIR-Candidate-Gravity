# Compute Wave 11 — Continuum Generator Results

**Source branch:** `post-freeze-continuum-generator-wave11`  
**Authoritative GitHub Actions run:** `34655828349`  
**Status:** COMPLETE / 5 PRIMARY JOBS + AGGREGATOR SUCCESS

## Aggregate verdict

All predeclared signals were true:

- `finite_differential_law_can_generate_positive_continuum_and_all_order_moments = true`;
- `finite_generator_predicts_nonlocal_integral_holdouts = true`;
- `finite_low_moments_do_not_derive_continuum_generator = true`;
- `continuum_generator_can_close_Wilson_tower_without_finite_Hankel_rank = true`;
- `synthetic_continuum_generator_is_not_novel_physics = true`.

The aggregator set:

- `finite_continuum_generator_architecture_validated = true`;
- `generator_equation_physically_derived = false`;
- `candidate_new_QG_primitive_found = false`.

## A — finite differential law can generate a genuine continuum

Architecture proxy:

`d log rho/dx = (a-1)/x - (b-1)/(1-x)`

whose positive solution on `(0,1)` is a Beta continuum `rho(x) ~ x^(a-1)(1-x)^(b-1)`.

Synthetic truth:

- `a = 1.7`;
- `b = 2.4`.

Only two design moments were used:

- `m1 = 0.41463414634146345`;
- `m2 = 0.21951219512195128`.

Recovered parameters:

- `a = 1.6999999999999997`;
- `b = 2.3999999999999986`;
- maximum parameter error `1.33e-15`.

The untouched moments `m3...m13` were then predicted with maximum error `5.55e-17`.

The exact all-order rule is variable-coefficient rather than fixed-rank:

`m_(n+1) = (a+n)/(a+b+n) m_n`.

Its numerical recurrence error was zero in the run.

Thus **finite parent law != finite spectrum**. A finite differential law can generate a positive continuum and an infinite exact moment tower while having no fixed finite Hankel rank.

## B — nonlocal Stieltjes holdouts

The same generator parameters were fitted only from `m1,m2` and then used to predict the integral observable

`F(Q^2) = int_0^1 rho(x)/(Q^2+x) dx`.

Untouched holdouts were tested at

`Q^2 = 0.02, 0.05, 0.2, 1, 4, 20`.

Representative results:

- at `Q^2=0.02`: true `3.500612450212835`, predicted `3.5006124502128184`;
- at `Q^2=1`: true `0.7239038370055163`, predicted `0.7239038370055159`;
- at `Q^2=20`: true and predicted `0.048990048100206116`.

Maximum holdout absolute error: `1.64e-14`.

This validates the desired **design -> generator -> nonlocal holdout** architecture.

## C — low moments do not derive the generator

A positive continuum counterfamily was constructed:

`rho_e(x)=1+epsilon P3(2x-1)`

for `epsilon` from `-0.8` to `0.8`.

All scanned densities remained positive (`rho_min >= 0.2`). Because the shifted `P3` is orthogonal to degree `<=2` polynomials, `m0,m1,m2` stayed fixed up to quadrature error:

- maximum change among `m0,m1,m2`: `2.33e-9`.

Yet the next moment changed substantially:

- `m3` width across the positive family: `0.0114285764`.

Therefore finite low moments cannot be used to reverse-engineer the generator equation uniquely.

## D — continuum generator closes an infinite dispersive/Wilson tower

For a positive continuum written in inverse-mass-squared variable `x`, the dispersive coefficients are moments of the density. The Beta generator therefore induces an infinite tower with an `n`-dependent recurrence, rather than a fixed finite-rank recurrence.

This is exactly the architecture needed after Wave 10 showed that a full positive continuum should not be forced into a finite atomic Hankel rank.

## E — comparator firewall

The tested generator is deliberately synthetic and is **not** Candidate Gravity physics.

Finite continuum-generating differential/flow/integral equations already belong to broad known territories such as:

- functional/spectral RG;
- Schwinger–Dyson-type equations;
- spectral bootstrap / dispersion-integral equations;
- classical finite-parametric density/moment families.

A new QG primitive can only be claimed if an independently motivated RQIR/operational principle derives a specific continuum-generating equation or kernel and it then predicts untouched spectral, dispersive and apparatus-level observables.

## Scientific synthesis

Wave 11 resolves the architectural conflict exposed by Wave 10:

> finite microscopic information does **not** require finite spectral rank or a finite state count. The correct target can be a finite equation whose solution is an infinite-dimensional positive continuum.

But the physical origin of that equation remains open.

## Wave 12 target

Wave 12 asks whether RQIR-like operational composition principles are strong enough to derive the generator:

1. impose semigroup/composition exactly;
2. impose positivity and normalization;
3. optionally impose detailed balance / reversibility;
4. fix the leading IR relaxation scale;
5. test whether the generator is unique or whether a large family remains.

If a family remains, semigroup/composition is only a structural gate, not the missing parent law. The next physical principle must then fix the generator itself rather than merely require that one exists.
