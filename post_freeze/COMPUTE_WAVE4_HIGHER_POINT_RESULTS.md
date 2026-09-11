# Compute Wave 4 — Higher-Point Rigidity Results

**Branch:** `post-freeze-higher-point-wave4`  
**GitHub Actions run:** `34653297949`  
**Status:** COMPLETE / ALL FOUR PRIMARY JOBS + AGGREGATOR SUCCESS

## Aggregate signals

- `no_extra_local_DOF_selects_EH_point_in_scanned_metric_quadratic_basis = true`;
- `finite_soft_order_leaves_higher_contact_nullspace = true`;
- `GR_two_point_does_not_close_higher_point_local_family = true`;
- `higher_derivative_cubic_has_finite_onset_scale = true`.

## M — local metric quadratic-curvature state cost

Control basis:

`EH + alpha R^2 + beta R_{mu nu}R^{mu nu}`

in 4D, modulo the Gauss-Bonnet/topological basis redundancy.

Standard metric quadratic-gravity particle-content logic was used:

- `beta != 0` carries an extra massive spin-2 mode which is ghost-like in the ordinary metric quantization;
- the scalar mode disappears on the structural line `3 alpha + beta = 0` (up to normalization conventions);
- eliminating both the extra spin-2 and scalar in this simple local metric basis forces `alpha=beta=0`.

The finite grid scan therefore selected the EH point as the only no-extra-local-DOF point in the tested basis.

This is consistent with the known metric quadratic-gravity spectrum; it does not cover torsionful/Riemann-Cartan extensions, fakeons, nonlocal models or other enlarged state spaces.

## N — finite soft-order constraints leave contact freedom

Crossing-symmetric four-point contact proxy with `s+t+u=0` was expanded in generators `sigma2` and `sigma3`.

Under uniform soft scaling, a monomial `sigma2^a sigma3^b` scales with degree `2a+3b`.

Fixing all contact information only through any finite soft/derivative degree `P` leaves all higher-degree directions free as the EFT cutoff `D` is raised.

This is a scalarized algebraic control, not a helicity-resolved graviton soft theorem. Its purpose is narrower:

> finite-order soft data do not logically imply all-order contact closure.

## O — GR two-point does not close higher-point local interactions

Once the quadratic action is frozen to the GR two-point sector, curvature-cubic and higher layers remain available because curvature starts at `O(h)`.

The script used only one schematic coefficient per curvature power, deliberately undercounting the real EFT operator basis. Even this minimum count grows monotonically with the maximum curvature power.

Therefore exact two-point spectral purity is insufficient to define a full microscopic theory.

## P — onset scale for a six-derivative graviton cubic correction

For dimensional bookkeeping we used

`Delta_3(E) ~ c6 (E/M)^4`

as the relative size of a six-derivative `R^3`-like cubic correction to a two-derivative Einstein interaction.

For fixed `c6`, a chosen target deviation `delta` occurs at

`E/M = (delta/c6)^(1/4)`.

This calculation is only dimensional bookkeeping. The nontrivial causality input is external:

- Camanho, Edelstein, Maldacena & Zhiboedov show that higher-derivative corrections to the graviton three-point coupling face causality constraints in weakly coupled gravity and that the problem cannot be repaired by a finite set of conventional particles with spin `J<=2`; an infinite tower of massive higher-spin states is the identified cure in their regime.
- Later dispersive/partial-wave studies bound gravitational Wilson coefficients in terms of the scale of new higher-spin states.

Thus a sizeable higher-point deviation is not generically an isolated low-energy Wilson coefficient with no UV cost.

## Synthesis after Waves 1-4

The search now has a much sharper structure:

1. generic CP/positivity/finite moments/crossing do not select a unique completion;
2. GR pole + positive spectral corrections still leaves a family unless an all-order spectral law is supplied;
3. the cheapest local `q^4` TT deformation is unhealthy in the standard pole interpretation;
4. no-new-state local quadratic-curvature rigidity returns to the EH root;
5. leaving the GR propagator untouched moves freedom to higher-point EFT coefficients;
6. finite-order soft constraints do not close that higher-point family;
7. sizeable higher-derivative graviton three-point corrections carry an additional causality/UV-completion burden in the CEMZ regime.

## Next high-value frontier

The next calculation should test **constructibility** rather than another low-order coefficient scan:

- assume the minimal two-derivative massless spin-2 three-point seed;
- impose factorization/unitarity and a boundary-free recursion condition;
- determine whether the tree S-matrix is then fixed to GR;
- identify exactly which boundary/contact datum reappears when higher-derivative seeds are allowed;
- keep loop/EFT renormalization as a separate layer because tree constructibility is not a UV-completion theorem.

This is the most promising remaining route to a finite upstream rule, and it is independently motivated by known BCFW/constructibility results rather than by comparator performance.