# Iter019C / G37-C2 terminal result

Authoritative run `34704249235`, head `0852fe30aa6bb7542dbb5ff4ec17fe8fd6eb55c1`, aggregate job `103582186949`, summary artifact `10301617346`, digest `sha256:84a472e147298c9c3ffef7d5dd8543d32fc13c11374c477c629dc5d972473af8`.

All 20 prospectively frozen artifacts were structurally valid. The corrected family adds an explicit `lambda_MF in [0,1]` so that `lambda_MF=0` exactly contains shared-noise-only and `cA=cB=0` exactly contains the K=2 measurement-feedback boundary.

Positive-control calibration:
- Sobol-LSQ: 8/8 PASS; worst trace-distance recovery `5.926287948142953e-09`;
- LHS-LSQ: 8/8 PASS; worst trace-distance recovery `2.51679714564514e-09`;
- frozen recovery tolerance remained `<0.002`.

Exact parent-boundary controls were recovered:
- MF-only boundary shard 4: Sobol `5.926287948142953e-09`, LHS `2.51679714564514e-09`;
- shared-noise-only boundary shard 5: Sobol `5.2458766459254586e-14`, LHS `4.147024980815832e-15`.

Admissibility: 4/4 PASS under frozen TP/CP/PSD/trace/Hermiticity thresholds.

Classification: `POSITIVE_CONTROL_METHOD_CALIBRATED_TRULY_NESTED_MF_SHARED_NOISE`.

This closes calibration of the corrected truly nested finite Markovian family and authorizes a separate prospective RCG-002 adversarial gate with a now-valid parent-nesting check. It does not itself supply adversarial support or a general classical/semiclassical no-go.