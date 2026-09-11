# Compute Wave 5 — Constructibility Results

**Branch:** `post-freeze-constructibility-wave5`  
**GitHub Actions run:** `34653531748`  
**Status:** COMPLETE / ALL FOUR PRIMARY JOBS + AGGREGATOR SUCCESS

## Aggregate signals

- `boundary_free_condition_removes_proxy_contact_data = true`;
- `tree_constructibility_not_loop_closure = true`;
- `higher_derivative_cubic_seed_is_independent_datum = true`;
- `minimal_seed_plus_boundary_free_can_isolate_tree_but_not_full_quantum_without_loop_rule = true`.

## Q — boundary/contact ambiguity

A crossing-symmetric polynomial contact proxy was used to represent independent local boundary data.

Under a generic constructible shift, a nonconstant polynomial boundary/contact term does not vanish at large complex deformation parameter. Therefore, **if** the pole/factorization part has the required falloff and the full amplitude is required to vanish at infinity, independent polynomial boundary contacts are removed in the proxy.

This is not a proof of graviton large-z behavior. The external authority is the known BCFW constructibility of GR tree amplitudes.

Scientific point:

> boundary-free recursion is a genuine extra rigidity condition. If it is relaxed, a growing local contact family immediately reappears.

## R — loop counterterm layer

Einstein-gravity EFT power counting gives a schematic local derivative layer

`d_counterterm = 2L + 2`

at loop order `L`.

The script separates this from the tree-level recursion problem.

Known physics supplies the important caution:

- four-dimensional pure gravity has special one-loop on-shell cancellations;
- at two loops a genuine curvature-cubic/Riemann-cubed counterterm occurs.

Therefore a tree S-matrix fixed by constructibility is **not** a UV-complete quantum theory and does not determine all renormalized higher-derivative data.

## S — cubic seed space

The research bookkeeping distinguishes at least two relevant massless spin-2 cubic layers:

1. `EH_2DER` — the two-derivative Einstein cubic seed, mixed-helicity sector;
2. `R3_6DER` — a six-derivative curvature-cubic seed, all-plus/all-minus sector in the standard 4D amplitude language.

The latter leaves the propagator unchanged but introduces an independent Wilson datum and, when sizeable in the weakly coupled regime, carries the CEMZ causality/UV-completion burden.

Thus recursion can only be unique **after the seed class itself is fixed**.

## T — constructibility decision matrix

The logical variables were:

- minimal two-derivative seed only;
- boundary-free recursion;
- an independent loop/all-order closure principle.

The matrix yields:

- `minimal seed + boundary-free` -> tree-level uniqueness in the proxy;
- removing either condition -> seed/contact freedom returns;
- even with tree uniqueness, full quantum uniqueness remains false unless an additional loop/all-order closure law is supplied.

## External constructibility authority

The computational scripts do not re-prove BCFW gravity.

The relevant external results are:

- Benincasa & Cachazo (2007): consistency conditions for constructible massless S-matrices;
- Benincasa, Boucher-Veronneau & Cachazo (2007): BCFW recursion for all GR tree graviton amplitudes;
- Arkani-Hamed & Kaplan (2008): large-complex-momentum behavior establishing gravity constructibility in the relevant setting.

## Main result

The strongest finite-parent structure found so far is:

`minimal massless spin-2 two-derivative seed`

`+ factorization/unitarity`

`+ boundary-free constructibility`

`-> GR-like all-tree S-matrix`.

This is important because it is genuinely more rigid than the earlier low-order RQIR constraints.

However it **returns to GR/C5 rather than producing a new theory**, and it does not close the loop/UV layer.

## New frontier

The remaining high-value problem is now sharply localized:

> Is there an independently motivated all-order/loop closure principle that fixes the quantum EFT/UV data without simply assuming a known UV completion and without reintroducing arbitrary functions?

Candidate directions must be tested against:

1. RG/fixed-point closure;
2. spectral/all-order sum-rule closure;
3. modular/state-selection closure;
4. higher-spin/string-like completion;
5. nonperturbative path-integral/state-space principles.

But each of these is already close to a known quantum-gravity school/comparator. A new Candidate Gravity can only be claimed if the principle itself is new or yields a comparator-orthogonal quantitative relation fixed prospectively.