# Iter019C / G37-C2 preregistration and launch

Frozen before result inspection on 2026-09-12.

Protocol correction: inspection of the already-launched G37-A revealed that the preceding 18-dimensional G37-C family did not mathematically contain the shared-noise-only family. K=2 measurement-feedback channel weights always sum to one, so its MF component could not be switched off. Therefore the G37-A frozen nesting rule against the shared-noise parent was invalid as a family-containment test. G37-A remains a diagnostic run and must not be promoted under that nesting rule.

G37-C2 corrects the family prospectively by adding one explicit amplitude `lambda_MF in [0,1]` and defining `L = L_MF(lambda_MF * theta) + L_shared`. Hence `lambda_MF=0` exactly contains the G36 shared-noise family, while `cA=cB=0` exactly contains the calibrated K=2 measurement-feedback family.

Frozen calibration controls: eight hidden in-family targets × two independent Sobol/LHS designs: four interior controls, one exact MF-only boundary, one exact shared-noise-only boundary, one strong-shared interior control, and one near-shared boundary. Hidden target coordinates are never optimizer starts. Four independent admissibility lanes additionally test TP/CP/PSD/trace/Hermiticity.

Scientific PASS requires all 16 positive-control lanes to recover trace distance `<0.002` and all four admissibility lanes to pass their frozen numerical thresholds. No post-result changes to thresholds, bounds or family definition are allowed.

Only terminal G37-C2 PASS can authorize a corrected nested-family RCG-002 adversarial gate. This correction is methodological and does not prejudge RCG-002.