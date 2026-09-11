# Wave 18 Methodological Correction 001

**Original run:** `34659178949`  
**Original branch:** `extra-hypothesis-wave18`  
**Correction branch:** `extra-hypothesis-wave18-correction`

## Defect

The original H0 no-extra-hypothesis control used the same spin-2/spin-0 source geometry for both its design observable and its supposed holdout, changing only the momentum-scale variable. The holdout gradient was therefore proportional to the design gradient. By construction, a parameter direction in the design nullspace remained invisible to that holdout.

This made the original boolean `H0_underdetermination_survives` incorrectly require a nonzero holdout width from an observable incapable of resolving the null direction.

## Correction rule

Do not modify H1-H4, their design point, or their prospective holdouts.

For H0 only, use the **independent source geometry already frozen in Wave 17** as the resolving holdout. Its coefficients were fixed before the Wave-18 H0 defect was observed, so this correction does not select a new observable from the failed result.

The corrected H0 pass condition is:

1. design rank remains deficient / nullity > 0;
2. candidate pair agrees at design to numerical precision;
3. the previously frozen independent-geometry holdout resolves that null direction.

## Governance

The original Wave-18 run and failed H0 signal remain retained. This document is a versioned methodological correction rather than a silent rewrite.

Regression jobs rerun H2 and the cross-class identifiability calculation unchanged to certify that the correction is local to H0.
