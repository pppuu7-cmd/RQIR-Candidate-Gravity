# RCG-004B — restored-lapse triaxial held-out gate (PREOUTCOME)

Date: 2026-09-17
Status: **PROSPECTIVELY FROZEN BEFORE PRIMARY RCG004 SURVIVOR INSPECTION**

Parent scientific preregistration:
- `prereg/RCG004_COMPLETE_PARITY_EVEN_ALGEBRAIC_CUBIC_CURVATURE_FAMILY_V0.md`
- commit `345213253f2ecf415af40cb4fbae47b4f58d8870`

Programme authority terminal:
`28781bc1873413b214f751eaa963cf1c51423e0b`.

## Purpose

This gate is a strict no-refit held-out test applied to the **entire** primary survivor subspace of RCG004-v0, if that subspace is nonzero. It is frozen before the primary quotient/kernel is computed or inspected and therefore may not be used to choose primary coefficients.

## Held-out geometry

Use fully triaxial off-shell Bianchi-I with restored lapse:

`ds^2 = -N(t)^2 dt^2 + exp(2a(t)) dx^2 + exp(2b(t)) dy^2 + exp(2c(t)) dz^2`.

`N(t), a(t), b(t), c(t)` are arbitrary independent smooth histories. Do not set `N=1` during held-out construction.

No isotropy, axisymmetry, equations of motion, constant-Hubble assumption, special trajectory, or GR ADM law may be imposed.

Source remains exactly `VACUUM_ZERO`.

## Input subspace lock

Let `K_primary` denote the exact full primary RCG004 survivor span from the unit-lapse triaxial Hessian+curl gate.

RCG004B acts only by restricting additional exact held-out constraints to `K_primary`. It may not:
- change the quotient basis;
- add operators;
- refit coefficients;
- select a preferred basis vector;
- use the held-out result to modify the primary calculation.

## Held-out objectives

For the full `K_primary` subspace derive directly from the restored-lapse metric:
- exact dependence on `N`;
- exact derivatives of `N` appearing in the reduced Lagrangian/equations;
- whether unit-lapse gauge fixing hid higher derivatives;
- lapse equation derivative order;
- acceleration/kinetic degeneracy involving `N,a,b,c`;
- candidate primary constraint direction(s) where identifiable;
- gauge-direction degeneracy;
- constraint preservation only where derivable without importing GR.

Primary discriminator: collect all forbidden higher-derivative coefficients into an exact linear restriction map on `K_primary`.

Persist exact:
- dimension of `K_primary`;
- held-out restriction rank;
- residual held-out survivor dimension;
- exact residual span.

## Held-out classifiers

If primary nullity is zero, this gate is `NOT_APPLICABLE_PRIMARY_NULLITY_ZERO` and no held-out computation is needed.

If primary nullity is positive:
- residual dimension `0` => `FAIL_SCOPED_RCG004_HELDOUT_RESTORED_LAPSE_FALSIFIES_ALL_PRIMARY_SURVIVORS`;
- residual dimension `>0` => `PASS_SCOPED_RCG004_HELDOUT_NONZERO_SURVIVOR_SUBSPACE_REMAINS` with the full residual span retained;
- any refit, basis change, source change, chronology break, imported GR constraint assumption, or implementation inconsistency => `INVALID_RCG004B`.

## Cross-checks and controls

- Setting `N=1` **after** deriving the held-out expressions must recover the primary unit-lapse structures on the same coefficient subspace.
- Axis permutations must agree.
- Embedded old RCG003 ray is a regression control only; where evaluated it must not falsely become fully second-order by lapse manipulation.
- No finite numerical tolerance is permitted.

## Claim ceiling

A held-out survivor remains only a structural candidate subspace. This gate does not establish GR, uniqueness, hyperbolicity, ghost freedom, stability, matter coupling, phenomenology, quantum gravity, or new physics.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.