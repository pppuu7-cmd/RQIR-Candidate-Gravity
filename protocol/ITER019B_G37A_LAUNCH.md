# Iter019B / G37-A preregistration and launch

Frozen before result inspection on 2026-09-12.

Prerequisite: terminal G37-C scientific PASS (`34703787083`), which calibrated the exact combined finite Markovian family on 12/12 hidden positive controls and 4/4 admissibility lanes under unchanged thresholds.

Scientific question: can the exact G37-C combined comparator — calibrated K=2 additive independent single-axis measurement-feedback GKSL plus one shared Gaussian classical Hamiltonian-noise process — reproduce the four prospectively fixed RCG-002 target states?

Frozen optimizer: exact G37-C Sobol-LSQ/LHS-LSQ 18-dimensional construction and bounds, no post-calibration retuning.

Frozen acceptance per shard:
- both calibrated methods must retain trace-distance gap `>1e-4`;
- Sobol/LHS gaps must agree within `0.002`;
- combined-family best gap must not be worse than the best exact calibrated parent-family minimum (G34 K2 measurement-feedback or G36-A shared noise) by more than `0.002` nesting slack;
- all eight lanes must be finite and structurally valid.

Scope ceiling: this exact finite combined Markovian family only. PASS is not a no-go theorem for all classical/semiclassical mediators and cannot establish new physics or full quantum gravity.