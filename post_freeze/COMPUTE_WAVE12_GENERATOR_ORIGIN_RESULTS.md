# Compute Wave 12 — Generator Origin Results

**Authoritative branch:** `post-freeze-generator-origin-wave12-run`  
**Authoritative GitHub Actions run:** `34656602347`  
**Status:** COMPLETE / 5 PRIMARY JOBS + AGGREGATOR SUCCESS

## Aggregate verdict

All five predeclared signals were true:

- reversible diffusion family survives stationarity + detailed balance + unit gap;
- independent reversible CTMC semigroup counterexample confirms nonuniqueness;
- extra polynomial closure selects a unique generator within that restricted class;
- that selected generator is the known Jacobi/Wright–Fisher comparator;
- prospective dynamical holdouts discriminate the surviving family.

The aggregator therefore set:

- `semigroup_positivity_detailed_balance_gap_sufficient_to_derive_unique_generator = false`;
- `polynomial_closure_can_force_uniqueness_but_is_known_comparator = true`;
- `candidate_new_QG_primitive_found = false`.

## Reversible diffusion counterfamily

Stationary density: `Beta(1.7,2.4)`.

Mobility family:

`A_k(x)=x(1-x)[1+k x(1-x)]`, with `k>-4`.

Detailed-balance drift:

`B=A'+A d(log rho)/dx`.

Each member was rescaled so that the first nonzero eigenvalue is exactly 1. The next eigenvalues remained nonunique.

For `k=-2,-1,0,1,3`, the second nonzero eigenvalue was respectively

`2.8469967, 2.6235115, 2.4878049, 2.3940090, 2.2694029`.

Hence

- `lambda2_width_after_gap_fix = 0.5775938682`;
- `lambda3_width_after_gap_fix = 1.4364579215`.

So stationary continuum + positivity + reversibility + leading relaxation scale do not determine the higher spectrum.

## Independent CTMC semigroup counterexample

Three reversible five-state generators were constructed with the same stationary distribution. After rescaling all to unit gap, they satisfied:

- stationarity error at machine precision;
- row-sum normalization at machine precision;
- positive transition probabilities;
- semigroup composition `P(0.3)P(0.7)=P(1)` at machine precision.

Yet the next nonzero eigenvalue was approximately

- `3.06944` for uniform conductances;
- `2.96960` for center-heavy conductances;
- `5.99980` for alternating conductances.

Thus

`higher_mode_width_after_unit_gap = 3.0301943241`.

This confirms nonuniqueness independently of the diffusion ansatz.

## Polynomial closure

If one additionally assumes

- local second-order diffusion;
- `deg A <= 2` with `A(0)=A(1)=0`;
- `deg B <= 1`;
- Beta stationarity and detailed balance,

then

`A=kappa x(1-x)`

and

`B=kappa[a-(a+b)x]`.

Fixing the first gap to one gives `kappa=1/(a+b)` and the spectrum

`lambda_n = n(n+a+b-1)/(a+b)`.

This is the known Jacobi/Wright–Fisher diffusion. Therefore polynomial closure is mathematically sufficient inside that class but is not a new QG primitive.

## Prospective dynamical holdout

Using stationary autocovariance of the operational variable `x` at times `0.15,0.5,1.5,4`, the three unit-gap Markov generators remained distinguishable.

Holdout widths were

`0.00376231, 0.00394935, 0.00231533, 0.000201790`.

Maximum width:

`0.0039493539`.

Hence time-domain holdouts can distinguish generators that all pass the static/semigroup gates.

## Scientific conclusion

RQIR-like composition/semigroup, positivity, normalization, reversibility, fixed equilibrium continuum and fixed leading relaxation scale are structural consistency gates, not a derivation of the parent generator.

A strong extra polynomial closure selects a unique generator but collapses to an existing Jacobi/Wright-Fisher comparator.

The missing ingredient must therefore fix the mobility/kernel itself through genuinely QG-specific physics.

## Wave 13 target

Audit QG-motivated spectral selectors suggested by current Lorentzian-gravity work:

1. positivity;
2. unit total spectral weight;
3. fixed IR/UV endpoint asymptotics;
4. finite Ward/sum-rule constraints;
5. prospective nonlocal Stieltjes/dispersion holdouts.

The goal is to test whether these constraints determine a unique continuum or leave a functional nullspace. If a nullspace survives, a genuine dynamical flow/integral equation—not merely finitely many sum rules—is required.
