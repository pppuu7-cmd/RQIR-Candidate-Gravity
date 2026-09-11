# Compute Wave 15 — Cross-Sector Kernel Results

**Authoritative branch:** `post-freeze-cross-sector-kernel-wave15`  
**Authoritative GitHub Actions run:** `34657544494`  
**Status:** COMPLETE / 6 PRIMARY JOBS + AGGREGATOR SUCCESS

## Aggregate verdict

All seven predeclared signals were true:

- one shared kernel predicts spectral and dispersive holdouts;
- sharing removes a parameter null direction present in an unlinked sector-by-sector description;
- the unlinked null direction changes a prospective dispersive holdout;
- cross-sector holdouts detect a positive continuum direction invisible to spectral design moments;
- a same-realization gate rejects sector-specific parameter/scheme switching;
- generic causal/soft/normalization kernel axioms leave shape freedom;
- the cross-sector architecture is not by itself new QG physics.

The aggregator therefore set:

- `shared_kernel_cross_sector_architecture_validated = true`;
- `same_realization_gate_required = true`;
- `generic_structural_axioms_uniquely_fix_kernel = false`;
- `independent_qg_specific_kernel_origin_required = true`;
- `candidate_new_QG_primitive_found = false`.

## Shared-kernel cross-sector closure

Synthetic kernel equation:

`u=1+alpha int_0^x u(y)dy + beta int_0^x (x-y)u(y)dy`,

with `rho proportional rho0*u`.

True parameters:

`(alpha,beta)=(-0.65,2.35)`.

Using only spectral design moments

`m1=0.43155279610524533`,
`m2=0.2372585409819496`,

recovered

`alpha=-0.6499999999999854`,
`beta=2.3499999999999672`,

with

`parameter_max_error = 3.2862601529e-14`.

Without any sector-specific retuning:

- spectral/Wilson holdout m3...m8 max error: `4.1633363423e-17`;
- nonlocal dispersion holdout max error over Q^2 = 0.02,0.1,0.5,2,10: `1.3322676296e-15`.

This validates the shared-kernel architecture only; the kernel is synthetic.

## Shared versus unlinked parameter rank

Shared design Jacobian for `(m1,m2,F(Q^2=0.3))` had

- parameter rank `2`;
- parameter nullity `0`.

An unlinked four-parameter copy `(p_spectral,p_dispersion)` had

- rank `3`;
- nullity `1`.

The normalized surviving null vector was approximately

`(0,0,-0.3726093,0.9279883)`.

A scan along this nearly design-null direction produced

- max design drift `3.59493e-05`;
- prospective `F(Q^2=0.02)` holdout width `0.0137000056`.

Thus cross-sector sharing removes genuine predictive freedom rather than only reducing notation.

## Spectral-design null detected cross-sector

A positive q3 deformation was constructed orthogonal to `1,x,x^2` under the actual shared-kernel density.

Across epsilon = -0.8...0.8:

- `max_design_change_m0_m1_m2 = 3.8857805862e-16`;
- `m3_width = 0.0028740019913`;
- dispersion holdout widths were
  - Q^2=0.02: `0.28184120395`;
  - Q^2=0.1: `0.07171430308`;
  - Q^2=1: `0.000683600150`;
  - Q^2=10: `2.39545e-07`.

All scanned densities remained positive.

Therefore cross-sector nonlocal observables carry substantial information against directions completely invisible to the spectral design moments.

## Same-realization consistency

A deliberately inconsistent construction used

- spectral source parameters `(-0.65,2.35)`;
- dispersion source parameters `(-1.15,3.10)`.

Each sector fits exactly if separate parameter copies are permitted. Forcing one shared realization gives best-fit parameters

`(-1.9000046,4.9692904)`

but residuals remain, with

- max absolute residual `0.00185776835`;
- L2 residual `0.00263373056`.

Thus sector switching can fake individual closure, and a same-realization gate is mandatory.

## Generic kernel-axiom rank

Polynomial causal kernel basis:

`K(x,y)=sum c_ij x^i y^j`, i,j=0..2 on `0<=y<=x<=1`, giving 9 coefficients.

Generic structural conditions:

- causal triangular support (domain);
- `K(x,0)=0`;
- `K(x,x)=0`.

These homogeneous conditions have

- rank `7`;
- shape nullity `2`.

Fixing overall normalization `integral_triangle K = 1` raises rank to `8`, but still leaves

`shape_nullity_after_normalization = 1`.

Scanning that exact constraint-null direction changes untouched kernel functionals while preserving the declared constraints to ~1e-14:

- `integral x*K` width `0.0012270169564`;
- `integral y*K` width `0.0006135084782`.

This is a generic operator-origin proxy, not an RQIR-specific result and not a positivity theorem.

## Scientific conclusion

Cross-sector functional closure is substantially stronger than sector-by-sector fitting, and same-realization consistency must be part of the frozen validation funnel. However, generic causal/soft/normalization principles do not uniquely determine even a small finite kernel basis.

The remaining question is therefore sharply localized: **which operator constraint follows independently from original frozen RQIR and removes the residual kernel direction without importing QGR-P/polygon information or merely reproducing a known comparator?**

## Wave 16 target

Perform an RQIR provenance-first operator reconstruction:

1. extract explicit frozen RQIR requirements relevant to composition, observability, same-realization consistency and interface reconstruction;
2. map each requirement to an operator/kernel constraint only when the mapping is logically justified;
3. label provenance for every constraint: RQIR / established physics / mathematical necessity / optional modelling choice;
4. quantify incremental rank added by each allowed requirement on a finite kernel basis;
5. reserve cross-sector spectral/dispersion observables as holdouts;
6. enforce a contamination firewall: no condition may be imported solely from QGR-P, KMQGB failure fixes, or a known comparator solution;
7. if nullity remains, report the exact unsolved degree of freedom instead of inventing a closure axiom.
