# RCG-006B — generic exact metric-jet held-out for field-redefinition audit (PREOUTCOME)

Date: 2026-09-17
Status: **FROZEN BEFORE RCG006 GENERATOR/M_FR RANK OUTCOME**

Parent scientific preregistration:
`fc3ff1f49c56f2befc039e09ebd8f388833dbff1`

Purpose: no-refit validation of universal generator tensors, first-order EH images and quotient representatives. This held-out is a validation layer only; finite sampling is never accepted as the universal identity proof.

## Exact jet coordinates

At a normal-coordinate point use independent exact coordinates for:
- the 20-component generic 4D algebraic Riemann tensor used by the audit;
- symmetric fourth metric jets `h_(ab),(cdef)` with `(ab)` symmetric and `(cdef)` fully symmetric;
- optional lower normal-coordinate jets required by an independent Critic reconstruction.

All values are rational.

## Deterministic generator

Use the 64-bit recurrence

`x_{n+1} = (6364136223846793005*x_n + 1442695040888963407) mod 2^64`.

For each requested rational coordinate use two successive states and set

`num = ((x_n >> 16) mod 19) - 9`,
`den = [2,3,5,7,11][((x_{n+1} >> 24) mod 5)]`,
`value = num/den`.

Zero values are allowed; if an entire sample accidentally has all zero curvature coordinates, advance one state and regenerate that sample only. No other rejection or outcome-dependent resampling is allowed.

Frozen sample banks:
- Constructor validation bank: seed `0x5243473030364341`, 32 samples;
- independent Critic validation bank: seed `0x5243473030364352`, 32 samples;
- final cross-route held-out bank: seed `0x524347303036484f`, 16 samples.

Sample ordering is lexicographic in the frozen coordinate manifest produced by the implementation before any rank is read.

## Validation rules

For every bank compare exact rational evaluations of:
1. every deterministic generator-basis tensor reconstructed from the universal coefficient representation;
2. every first-order EH action image before and after reduction to frozen RCG005 coordinates;
3. every exact relation asserted between alternate generator representations;
4. the final quotient representative map.

All comparisons are exact equality. No tolerance is permitted.

If a held-out disagreement occurs, classify the audit INVALID until the implementation/reconstruction defect is resolved. Held-out failure may not be used to add a generator, change equivalence rules, choose a different pivot basis, or refit `M_FR`.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
