# G82–G85 reference-channel construction robustness synthesis

Date: 2026-09-13
Status: **RETROSPECTIVE SYNTHESIS OF FOUR TERMINAL, PROSPECTIVELY FROZEN GATES**
New scientific gate: **NO**
Programme readiness: **66%**
Theory established: **0%**

## Terminal inputs
- G82: `C_SINGLE_SOURCE_REFERENCE_CALIBRATION_BREAKS_SLOPE_ALIAS_WITHOUT_MODIFYING_C_FUNCTIONAL_SCOPED`.
- G83: `D_SINGLE_RETARDED_SOURCE_REFERENCE_CALIBRATION_BREAKS_CUBIC_GAIN_ALIAS_WITHOUT_MODIFYING_D_FUNCTIONAL_SCOPED`.
- G84: `C_REFERENCE_CONSTRUCTION_REMAINS_IDENTIFIABLE_UNDER_FROZEN_LEAKAGE_UNTIL_SAME_SHAPE_LIMIT_SCOPED`.
- G85: `D_REFERENCE_CONSTRUCTION_REMAINS_IDENTIFIABLE_UNDER_FROZEN_LEAKAGE_UNTIL_SAME_SHAPE_LIMIT_SCOPED`.

## Joint reading allowed by the scope ceilings
For each surviving architecture independently, one explicit external nuisance-reference direction is sufficient to break the exact same-shape alias without modifying the frozen candidate functional. The construction remains locally identifiable under the prospectively frozen imperfect-decoupling families, but its numerical conditioning degrades continuously as the reference response approaches the science-shape direction or the reference gain vanishes.

C and D reach this conclusion through different inherited constraints: C preserves the transverse/Ward projected-source structure; D preserves retarded support, Sigma symmetry, CTP normalization and the frozen cubic jet.

## What this does not establish
No G82–G85 result demonstrates an actual source-preparation mechanism, experimental reference channel, candidate-blind physical probe, achievable leakage bound or calibration precision. The reference channel remains an external construction hypothesis.

## Research implication
The identifiability branch is now sufficiently characterized that further abstract rank/leakage scans have diminishing value. The highest-value unresolved blocker remains G69: candidate-owned nonlinear dynamics. The next admissible work should therefore test whether the frozen C and D perturbative data uniquely determine any nonlinear generally covariant completion, rather than choosing one by fiat.

## Claim lock
No readiness increase, architecture selection, nonlinear-law establishment, experimental detectability claim or new physics follows. `THEORY_ESTABLISHED=0%` remains unchanged.
