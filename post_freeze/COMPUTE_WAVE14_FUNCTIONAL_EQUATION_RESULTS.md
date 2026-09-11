# Compute Wave 14 — Functional Equation Results

**Authoritative branch:** `post-freeze-functional-equation-wave14`  
**Authoritative GitHub Actions run:** `34657208658`  
**Status:** COMPLETE / 6 PRIMARY JOBS + AGGREGATOR SUCCESS

## Aggregate verdict

All six predeclared signals were true:

- a pointwise functional law detects the tested q3/q5 static null modes;
- a finite causal Volterra law can be unique and predict prospective holdouts;
- a finite nonlinear self-consistency equation can bifurcate into multiple positive branches;
- a functional identity has full rank on six low-moment-null directions;
- the same design observables do not identify the equation class;
- the tested equation architectures belong to known mathematical/comparator classes.

The aggregator therefore set:

- `functional_equation_architecture_can_remove_finite_static_nullspaces = true`;
- `finite_equation_alone_guarantees_predictive_closure = false`;
- `equation_class_selected_by_current_design_data = false`;
- `unique_solution_or_physical_branch_selection_required = true`;
- `qg_specific_operator_or_kernel_derivation_required = true`;
- `candidate_new_QG_primitive_found = false`.

## Pointwise differential-law nullspace test

The exact proxy law

`d log rho/dx = (a-1)/x - (b-1)/(1-x)`

has zero residual on the Beta base density. Every scanned positive q3/q5 deformation that preserves the finite static design constraints produced a nonzero residual.

The smallest deformed RMS residual was

`minimum_deformed_rms = 0.9955791686077565`.

Typical residuals were O(1)–O(6), with maximum pointwise residuals up to O(60). Thus the functional law removes the tested finite-moment null directions by a wide numerical margin rather than at floating-point threshold.

## Functional-identity rank

Six independent orthogonal polynomial null modes of degrees 3 through 8 are essentially invisible to the low moments m0,m1,m2:

`max_abs_low_moment_sensitivity = 1.27897692437e-13`.

The pointwise functional residual matrix on 250 collocation points had singular values

`[4.5399523, 3.5027476, 2.8441478, 2.3405008, 1.9036944, 1.4025567]`

and therefore

`functional_rank = 6 / 6`.

This demonstrates that a functional identity can impose independent constraints across directions completely missed by a finite moment checklist.

## Unique predictive Volterra architecture

Synthetic causal equation:

`u(x)=1+lambda integral_0^x (x-y)u(y)dy`, with `rho proportional rho0*u`.

Using only one design observable m1:

- true `lambda = 2.2`;
- recovered `lambda = 2.199999999999985`;
- parameter error `1.51e-14`.

Prospective predictions:

- moment-holdout max error `3.33e-16`;
- Stieltjes-holdout max error `3.55e-15`;
- Volterra equation residual max `2.22e-16`.

This validates the mathematical closure architecture for a unique linear Volterra equation, but the kernel was synthetic and provides no QG novelty.

## Nonlinear branch ambiguity

Synthetic nonlinear self-consistency equation:

`rho(x) proportional exp[lambda*m*(2x-1)]`,

`m=integral (2x-1)rho(x)dx`, with `lambda=5`.

It admitted three positive normalized self-consistent branches:

- `m=-0.7258819872`;
- `m=0`;
- `m=+0.7258819872`.

All self-consistency errors were ~1e-16, yet the untouched Stieltjes observable at Q^2=0.1 was

- `5.34298618`;
- `2.39789527`;
- `1.07282194`,

respectively.

Branch holdout spread:

`4.2701642469`.

Hence a finite nonlinear equation is not predictively closed without a uniqueness theorem or an independent physical branch-selection principle.

## Equation-class identifiability

Two structurally different finite generator classes were fitted to the same design moments m1,m2:

- Class A: local log-density ODE with `(theta1,theta2)=(-1,1.5)`;
- Class B: two-parameter causal Volterra law.

The design mismatch was only

`5.55111512313e-17`.

The fitted Volterra parameters were approximately

`alpha=-1.39051863396`, `beta=4.02492700026`.

Despite identical design moments, the models predicted

`m3_difference = 1.77582004025e-4`

and

`stieltjes_max_difference = 0.0165343812773`.

Therefore successful closure on the design observables does not identify the equation class.

## Scientific conclusion

Wave 14 establishes three distinct necessities for a viable continuum parent law:

1. **functional completeness** — the law must eliminate directions invisible to finite static constraints;
2. **unique solution or physical branch selection** — a finite equation alone is insufficient;
3. **equation-class identification** — different finite equations can fit the same design data and disagree on prospective holdouts.

Current spectral-FRG, Schwinger-Dyson and bootstrap/dispersion equations remain comparator classes. A new QG primitive must therefore be an independently derived gravitational operator/kernel, not merely another convenient functional equation.

## Wave 15 target

Require **cross-sector functional closure**: the same finite operator/kernel and the same parameter realization must simultaneously generate the spectral continuum and determine dispersive/Wilson data. Compare shared versus unlinked parameterizations, test kernel-null perturbations with frozen nonlocal holdouts, enforce same-realization consistency, and quantify how much of a finite kernel basis is actually fixed by generic structural axioms. Novelty remains fail-closed unless an independent QG-specific principle fixes the kernel/operator.