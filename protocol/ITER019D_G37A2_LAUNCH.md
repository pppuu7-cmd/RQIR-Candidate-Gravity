# Iter019D / G37-A2 preregistration and launch

Frozen before result inspection on 2026-09-12.

Prerequisite: terminal G37-C2 calibration PASS (`34704249235`), with 16/16 positive-control lanes and 4/4 admissibility lanes passing. Crucially, exact MF-only and shared-noise-only boundary controls were recovered far below the frozen `0.002` tolerance.

Scientific question: can the exact corrected G37-C2 truly nested finite Markovian comparator reproduce the four prospectively fixed RCG-002 target states?

Family and optimizer are unchanged from G37-C2: `L = L_MF(lambda_MF*theta)+L_shared`, with `lambda_MF in [0,1]`. Therefore `lambda_MF=0` contains shared-noise-only and `cA=cB=0` contains the calibrated K2 measurement-feedback parent.

Frozen acceptance per shard:
- both Sobol-LSQ and LHS-LSQ must retain trace-distance gap `>1e-4`;
- their gaps must agree within `0.002`;
- because both parents are exact boundaries of this corrected family, the combined best gap must be no worse than the better exact terminal parent minimum (G34 K2 MF or G36-A shared noise) by more than `0.002` nesting slack;
- all eight lanes must be finite and structurally valid.

No post-result threshold, bound, family or optimizer change is allowed. PASS is only scoped support against this exact finite combined Markovian family; it is not a general classical/semiclassical no-go and cannot establish new physics or full quantum gravity.