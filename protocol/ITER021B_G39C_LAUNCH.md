# Iter021B / G39-C preregistration and launch

Frozen before result inspection on 2026-09-12.

Prerequisite: G39-P terminal implementation/admissibility PASS (`34704548004`) for finite rank-2/rank-3 multimode shared-classical-white-noise channels with noncommuting local axes.

Purpose: calibrate adversarial-search optimizers before any RCG-002 interpretation. Rank 2 and rank 3 are tested separately. Each mode has arbitrary local Pauli axes, local coefficients and nonnegative rate `kappa in [0,1.2]`; exact zero rates are allowed so rank K contains the lower-rank boundary.

Frozen positive controls: four hidden in-family targets per rank × two independent methods. Controls include two interior cases, one exact lower-rank boundary and one strong multimode case. Hidden source coordinates are never optimizer starts.

Frozen optimizer construction: scrambled Sobol or Latin-hypercube design with 64 starts; score all starts by smooth density-matrix residual; refine the best 12 using bounded least-squares with maximum 1200 evaluations. Final authority remains trace distance `<0.002`.

Rank K is calibrated only if both methods recover all four rank-K controls below `0.002`. No threshold, parameter range or optimizer construction may change after result inspection. Only a calibrated rank may proceed to a separate RCG-002 adversarial gate. PASS remains scoped to this finite low-rank classical-noise family.