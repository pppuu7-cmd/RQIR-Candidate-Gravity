# ITER022D / G40-C2 — terminal calibration classification

Run: `34708550582`
Head: `2221f481e1ac98dc9a1f16ea8e4c81411d6ba834`
Aggregate job: `103593383979`
Summary artifact: `10302681897`
Digest: `sha256:6b29d3bb8e2759ab39e72fd5d9e0b6c38e772791b6e9eb9805386c4db8b6f38e`

All 8 corrected positive-control lanes passed the unchanged frozen rules.

- Sobol: 4/4 support; worst max trajectory trace gap `1.7318444583154354e-15`; minimum recovered fixed-pair BLP total positive increment `0.022161811061062853`.
- LHS: 4/4 support; worst max trajectory trace gap `9.367643243488307e-16`; minimum recovered BLP `0.022161811061063297`.
- Frozen recovery tolerance: `<0.002`.
- Frozen fixed-witness BLP criterion: `>0.02`.

Classification: `POSITIVE_CONTROL_METHOD_CALIBRATED_FIXED_WITNESS_STRICT_BLP_RTN`.

This is calibration only. It does not compare RCG-002 and does not raise programme readiness by itself. It authorizes calibration of any changed strict-subset search rule before a separate adversarial test.
