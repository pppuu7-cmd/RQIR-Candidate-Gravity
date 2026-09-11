# Compute Campaign 001 Results — Four-Stream Post-Freeze Uniqueness Audit

**Branch:** `post-freeze-parallel-compute-v1`  
**GitHub Actions run:** `34652336221`  
**Status:** COMPLETE / ALL PRIMARY JOBS SUCCESSFUL  
**Scientific role:** finite counterexample/uniqueness proxies after the frozen RQIR-v0 result; no modification of frozen v0 authority.

## Executive result

The four independent finite proxy calculations all found residual freedom after the advertised low-order/consistency constraints were imposed.

The workflow aggregator returned:

- `channel_nonunique_nontrivial_eta = true`;
- `spectral_finite_moments_nonunique = true`;
- `L4_not_closed = true`;
- `L6_not_closed_after_L4 = true`;
- `crossing_higher_order_freedom_grows = true`;
- `forward_blind_sector_exists = true`;
- `all_tested_closure_proxies_show_residual_freedom = true`.

This is **not** a no-go theorem for quantum gravity. It is a reproducible quantitative falsification of several naive claims that generic positivity/CP, a finite set of moments, low-order cumulants, or crossing plus a fixed leading term automatically give a unique completion.

## Stream A — CPTP channel polytope

Model: Pauli CPTP channel with axial symmetry

`lambda_x = lambda_y = lambda_perp`

and fixed longitudinal transfer `lambda_z = eta`.

Linear programming gave:

| eta | allowed lambda_perp interval | width |
|---:|---:|---:|
| 0.00 | [-0.500, +0.500] | 1.00 |
| 0.25 | [-0.625, +0.625] | 1.25 |
| 0.50 | [-0.750, +0.750] | 1.50 |
| 0.75 | [-0.875, +0.875] | 1.75 |
| 0.95 | [-0.975, +0.975] | 1.95 |
| 1.00 | [-1.000, +1.000] | 2.00 |

Every tested case is nonunique.

**Scoped interpretation:** CPTP + a fixed low-order transfer component + axial symmetry does not select one process even in a very small finite channel family. A gravity-specific closure must contain more information than those generic conditions.

Artifact id: `10284256548`.

## Stream B — positive spectral moment problem

Proxy spectral nodes:

`m^2 = {1,2,4,8,16,32}`

with nonnegative normalized weights. We fixed the first `r` inverse moments of an interior reference distribution and optimized the next inverse moment.

| fixed inverse moments r | affine nullity | next-moment range width |
|---:|---:|---:|
| 1 | 4 | 0.18603515625 |
| 2 | 3 | 0.0270538330078 |
| 3 | 2 | 0.00199556350708 |
| 4 | 1 | 0.0000650882720964 |

Even after four inverse moments plus normalization are fixed, the next moment remains nonunique on this six-node positive proxy.

**Important positive lesson:** the admissible range contracts rapidly as moments are added. Thus a sufficiently strong all-order spectral principle could in principle approach rigidity; finite low-energy data do not provide it by themselves.

Artifact id: `10283909368`.

## Stream C — L4/L6 cumulant hierarchy

Positive parity-symmetric distributions on

`x in {-3,-2,-1,0,1,2,3}`

were constrained by

- normalization;
- mean `0`;
- variance `1`;
- third moment `0`;
- exact parity symmetry.

The fourth cumulant remained in

`kappa_4 in [-2, 6]`,

with width `8`.

Then `E[x^4]=3` (`kappa_4=0`) was additionally fixed. The sixth cumulant still remained in

`kappa_6 in [-4, 6]`,

with width `10` (up to floating-point roundoff at the lower endpoint).

**Scoped interpretation:** fixing a complete low-order moment package and positivity does not automatically generate the next connected object. Even adding one higher-order condition need not close the following order.

Artifact id: `10284078949`.

## Stream D — crossing-symmetric EFT polynomial freedom

Scalarized control problem with `s+t+u=0` and symmetric generators

`σ2 = s^2+t^2+u^2`, degree 2,

`σ3 = s t u`, degree 3.

After fixing the leading `σ2` coefficient, the number of remaining symmetric polynomial directions grows with cutoff degree. Selected counts:

| max degree D | free after leading fix | forward-visible | forward-invisible |
|---:|---:|---:|---:|
| 2 | 0 | 0 | 0 |
| 3 | 1 | 0 | 1 |
| 6 | 5 | 2 | 3 |
| 10 | 12 | 4 | 8 |
| 14 | 22 | 6 | 16 |
| 18 | 35 | 8 | 27 |

At forward kinematics `t=0, u=-s`, `σ3=0`, so every direction carrying `σ3` is invisible to forward-only information.

**Scoped interpretation:** crossing plus a fixed leading low-energy term and forward-limit constraints do not generically close higher orders. This is a scalar algebraic control, not a graviton amplitude count.

Artifact id: `10283849387`.

## Aggregated decision

The first compute campaign therefore strengthens the post-freeze diagnosis:

`generic consistency + finite low-order information -> constrained family, not unique parent`.

The campaign does **not** justify a new Candidate Gravity term. Instead it raises the bar for the next step:

> any proposed upstream principle must supply a gravity-specific rigidity relation that survives a more physical spin-2/causal/spectral test, not merely generic CP, positivity, crossing or finite-moment information.

## Next computation wave

Wave 2 must be closer to gravity and should test, independently:

1. fixed massless spin-2 pole plus a positive massive spectral sector;
2. Ward-transverse conserved-source response and remaining form-factor freedom;
3. causal retarded rational/Stieltjes response after low-frequency GR normalization;
4. higher-curvature / extra-pole content under ghost/tachyon and decoupling constraints.

These tests remain candidate-principle falsifiers, not a search that tunes parameters to beat C5.