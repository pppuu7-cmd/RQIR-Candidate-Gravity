# Compute Wave 9 — Minimal Defect Results

**Source branch:** `post-freeze-minimal-defect-wave9`  
**GitHub Actions run:** `34655251232`  
**Status:** COMPLETE / 5 PRIMARY JOBS + AGGREGATOR SUCCESS

## Aggregate verdict

All six predeclared signals were true:

- `known_proxy_constraints_reduce_to_one_higher_derivative_defect = true`;
- `finite_spectral_recurrence_can_predict_dispersive_Wilson_tower = true`;
- `without_rank_axiom_next_Wilson_remains_ambiguous = true`;
- `prospective_holdout_discriminates_closure_order = true`;
- `nonzero_residual_defect_maps_to_finite_onset_scale = true`;
- `known_constraints_localize_but_do_not_derive_defect = true`.

The aggregator set:

- `minimal_defect_localized = true`;
- `spectral_to_amplitude_closure_architecture_demonstrated = true`;
- `physical_rank_or_recurrence_derived = false`;
- `candidate_new_QG_primitive_found = false`.

## A — localization to one residual higher-derivative datum

A five-dimensional bookkeeping parameter space

`q=(g2,g3,g4,cx,cy)`

was constrained by:

1. `g2=g3`;
2. `g3=g4`;
3. one operational Newton normalisation `g2=0.62`;
4. one leading Regge/contact input `cx=0.14`.

The constraint matrix had:

- rank `4`;
- residual nullity `1`;
- singular values approximately `1.80194, 1.24698, 1.0, 0.44504`;
- null basis exactly `(0,0,0,0,1)`.

Thus in this finite proxy all unresolved freedom is localized to the single higher-derivative/contact datum `cy`.

This is localization, not a derivation of `cy`.

## B — spectral recurrence to dispersive Wilson tower

A three-atom positive spectral proxy in inverse-mass-squared coordinates

- support `x=(0.1,0.3,0.7)`;
- weights `(0.25,0.50,0.25)`

was used. For the twice-subtracted expansion

`A_disp(s)=s^2 sum_i w_i x_i^2/(1-s x_i)`,

the coefficient of `s^(2+n)` is the moment `m_(n+2)`.

The rank-3 recurrence inferred from `m0...m5` was approximately

`m_(n+3) = 0.021 m_n - 0.31 m_(n+1) + 1.10 m_(n+2)`.

It reconstructed the computed Wilson/Taylor tower with maximum error `3.30e-17`.

However, keeping the same finite positive moments `m0...m5` while **not** imposing the rank-3 law left the next `s^6` coefficient in an interval:

- true synthetic coefficient: `0.029777`;
- positive-measure minimum: `0.0297770000027`;
- maximum: `0.0298821875`;
- width: `1.05187497e-4`.

So the algebraic propagation works once a recurrence is given; the missing physics is the derivation of the recurrence/rank itself.

## C — prospective closure-order holdout

Both rank-2 and rank-3 closure laws were constructed using only the first six moments as design data.

Rank-2 fit:

- coefficients approximately `(-0.133412, 0.866361)`;
- design recurrence residual `1.0873e-3`;
- maximum error on untouched `m6...m10`: `1.60246e-3`.

Rank-3 law:

- coefficients approximately `(0.021,-0.31,1.10)`;
- design residual `1.39e-17`;
- maximum error on untouched `m6...m10`: `3.30e-17`.

Thus an assumed closure order can be tested prospectively rather than selected after seeing the holdouts. This is the validation protocol required for any future physical recurrence proposal.

## D — residual defect as a finite onset scale

For a curvature-cubic-like correction with four additional derivatives relative to the Einstein cubic seed, the schematic ratio was taken as

`|delta A/A_EH| ~ |alpha| E^4`.

A nonzero residual coefficient therefore introduces an onset scale

`E_* ~ |alpha|^(-1/4)`.

This maps the remaining unknown datum into a potentially falsifiable scale, but does not determine its magnitude.

## E — comparator firewall

Known ingredients used to reduce the defect are not new Candidate Gravity physics:

- effective universality of dynamical Newton-coupling avatars is known in asymptotic-safety computations;
- generic soft-graviton structure contains theory-dependent higher-order pieces beyond the universal terms;
- CEMZ constrains sizeable higher-derivative graviton three-point deviations in its regime;
- Regge/dispersion constraints are established amplitude technology;
- choosing a finite-pole or finite-rank spectral recurrence is a known reconstruction ansatz unless its order and coefficients are independently derived.

## Scientific synthesis

The post-freeze search has now localized the missing finite information very sharply:

> known proxy constraints can reduce the finite theory space to one higher-derivative/contact defect, and a finite spectral recurrence would mathematically predict that defect together with an all-order dispersive Wilson tower.

But no physical principle has yet derived the recurrence/rank. Therefore this does **not** justify claiming a new QG law.

## New frontier — test the finite-rank premise itself

Current Lorentzian quantum-gravity spectral calculations report a massless one-graviton peak together with a multi-graviton continuum. An exact finite atomic spectral rank would therefore be suspicious as a law for the full graviton spectral function.

Wave 10 tests:

1. exact Hankel-rank saturation for a finite atomic measure versus non-saturation for a genuine continuum;
2. the finite-dimensional state-space/rational realization implied by a finite recurrence;
3. how finite rational/atomic approximations converge to, but do not equal, a continuum Stieltjes transform;
4. whether finite-order recurrences fitted to continuum moments fail untouched higher-moment holdouts;
5. comparator/provenance implications for the current Lorentzian graviton spectral continuum literature.

If the continuum route wins, the parent-law target must change from **finite spectral rank** to a **finite generative equation for a continuum**.
