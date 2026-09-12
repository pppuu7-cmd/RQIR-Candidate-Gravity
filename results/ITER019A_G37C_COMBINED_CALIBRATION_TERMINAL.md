# Iter019A / G37-C terminal result

Authoritative run `34703787083`, head `59cf94512a65a54a37eba05ae3093b7ee85bead0`, aggregate job `103580407237`, summary artifact `10301501728`, digest `sha256:513b51731f843e36597d9bbd4a026dda6137871b7a0096b4144920b19e8befbe`.

All 16 prospectively frozen artifacts were structurally valid. The combined finite Markovian comparator consists of the calibrated K=2 additive independent single-axis measurement-feedback GKSL generator plus the validated shared Gaussian classical Hamiltonian-noise generator.

Positive-control calibration:
- Sobol-LSQ: 6/6 PASS, worst trace-distance recovery `5.408859603136766e-10`;
- LHS-LSQ: 6/6 PASS, worst trace-distance recovery `2.1105501726665736e-05`;
- frozen recovery tolerance remained `<0.002`.

The six controls included four interior combined targets, one exact measurement-feedback-only boundary target and one strong shared-noise target. Hidden source coordinates were not optimizer starts.

Admissibility: 4/4 PASS under the frozen TP/CP/PSD/trace/Hermiticity thresholds.

Classification: `POSITIVE_CONTROL_METHOD_CALIBRATED_COMBINED_MF_SHARED_NOISE`.

This PASS authorizes a separate prospective RCG-002 adversarial search in this exact combined family. It does not itself provide adversarial support or a general no-go result.