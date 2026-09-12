# Iter021C / G39-A preregistration and launch

Frozen before result inspection on 2026-09-12.

Prerequisite: terminal G39-C scientific calibration PASS (`34704727102`). Rank 2 and rank 3 each recovered all four hidden positive controls under both Sobol-LSQ and LHS-LSQ with frozen trace-distance tolerance `<0.002`.

Scientific question: can the exact calibrated finite rank-2/rank-3 multimode shared-classical-white-noise families reproduce the four prospectively fixed RCG-002 target states?

Frozen optimizer/family: exact G39-C rank-specific parameter bounds, 64-start Sobol/LHS designs, best-12 bounded least-squares refinement, unchanged after calibration.

Frozen acceptance per rank and shard:
- both calibrated methods retain trace-distance gap `>1e-4`;
- Sobol/LHS gaps agree within `0.002`;
- rank 3 best gap must not be worse than rank 2 best gap by more than `0.002`, because rank 3 contains rank 2 exactly through a zero third-mode rate;
- all 16 lanes must be finite and structurally valid.

No parent-nesting requirement to G36 is imposed because exact containment of the full G36 parameter domain inside the G39 bounds has not been established. No thresholds, bounds, family definitions or optimizer construction may change after result inspection.

PASS is scoped only to these finite rank-2/rank-3 positive-rate multimode classical-white-noise families. It is not a no-go theorem for all classical/semiclassical mediators and cannot establish new physics or full quantum gravity.