# Iter019A / G37-C preregistration and launch

Frozen before result inspection on 2026-09-12.

Purpose: calibrate a broader finite Markovian comparator that combines the already calibrated K=2 additive independent single-axis measurement-feedback GKSL generator with the G36-P validated shared Gaussian classical Hamiltonian-noise generator.

This is positive-control calibration only. It does not inspect RCG-002 adversarial performance.

Frozen controls: six hidden in-family states, including four interior combined controls, one exact measurement-feedback-only boundary control with shared coefficients zero, and one strong shared-noise control. Hidden coordinates are never optimizer starts. Two independent optimizer constructions are used: 128-start scrambled Sobol and 128-start Latin hypercube, each scoring all starts and refining the best 16 with bounded least-squares, max 1000 evaluations/refinement.

Frozen scientific acceptance: final trace distance `<0.002` for every one of the 12 method/control lanes, plus 4/4 independently sampled admissibility lanes satisfying TP `<1e-10`, Choi minimum eigenvalue `>-1e-8`, evolved-state minimum eigenvalue `>-1e-8`, trace error `<1e-10`, Hermiticity error `<1e-10`. No post-result threshold or family changes.

PASS authorizes a later RCG-002 adversarial search in this combined finite family. FAIL is retained as calibration failure and blocks that adversarial interpretation.
