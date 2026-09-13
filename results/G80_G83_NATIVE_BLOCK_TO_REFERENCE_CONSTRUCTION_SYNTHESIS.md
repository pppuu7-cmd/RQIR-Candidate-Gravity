# G80–G83 native-anchor to reference-channel synthesis

Date: 2026-09-13
Status: **RETROSPECTIVE SYNTHESIS OF FOUR TERMINAL, PROSPECTIVELY FROZEN GATES**
New scientific gate: **NO**
Programme readiness: **66%**
Theory established: **0%**

## Independent terminal inputs
- G80: `BLOCKED_C_NATIVE_SOURCE_OBJECT_DOES_NOT_BREAK_EXACT_SLOPE_ALIAS_SCOPED`.
- G81: `BLOCKED_D_NATIVE_SOURCE_OBJECT_DOES_NOT_BREAK_EXACT_CUBIC_CALIBRATION_ALIAS_SCOPED`.
- G82: `C_SINGLE_SOURCE_REFERENCE_CALIBRATION_BREAKS_SLOPE_ALIAS_WITHOUT_MODIFYING_C_FUNCTIONAL_SCOPED`.
- G83: `D_SINGLE_RETARDED_SOURCE_REFERENCE_CALIBRATION_BREAKS_CUBIC_GAIN_ALIAS_WITHOUT_MODIFYING_D_FUNCTIONAL_SCOPED`.

## Joint reading allowed by the terminal scope ceilings
The already-frozen C and D source-functionals do not themselves contain the independent information required to calibrate away their exact same-shape nuisance aliases. This is a BLOCKED native-information result, not an architecture failure.

For each architecture separately, one explicitly added candidate-blind nuisance-reference channel is algebraically sufficient to restore the corresponding local rank while leaving the frozen candidate functional and inherited Ward/retarded/CTP/jet constraints unchanged in the finite constructions.

Thus the structural requirement exposed by G80–G83 is not merely "more rows" but an information channel whose response is linearly independent of the candidate direction and whose role is external calibration/reference rather than a relabelled native sector.

## What remains open
The G82/G83 reference channels are construction hypotheses. No terminal result establishes that they can be physically prepared, isolated, kept sufficiently candidate-blind, calibrated with adequate precision, or coupled without changing the candidate dynamics.

## Next admissible frontier
Before any physical-realizability claim, test the construction under prospectively frozen imperfect-decoupling families: candidate leakage into the reference channel, reference-gain uncertainty, and near-loss of nuisance sensitivity. C and D must remain independent sibling gates. PASS at that layer can establish robustness of the construction only; physical realizability remains open without externally grounded source/preparation physics.

## Claim lock
No readiness increase, architecture selection, candidate-owned nonlinear law, experimental detectability claim or new physics follows from this synthesis. `THEORY_ESTABLISHED=0%` remains unchanged.
