# Iter018C / G36-A preregistration and launch

Frozen before result inspection on 2026-09-12.

Prerequisites: G36-P implementation validation PASS; G36-C prospective positive-control optimizer calibration PASS on all 12 lanes. The G36-C optimizer construction is reused without post-calibration retuning.

Scientific question: can the finite shared Gaussian classical Hamiltonian-noise family reproduce the four prospectively fixed RCG-002 target states?

Frozen acceptance per shard: both `sobol_lsq` and `lhs_lsq` must retain trace-distance gap `>1e-4`, and their gaps must agree within `0.002`. All eight outputs must be finite and structurally valid. Thresholds and family definition are not changed after inspection.

Scope ceiling: one shared Gaussian classical scalar process coupled to two local Pauli axes, a convex mixture of product unitaries. A PASS is only a scoped negative-comparator result for this finite family, not a no-go theorem for classical/semiclassical gravity.
