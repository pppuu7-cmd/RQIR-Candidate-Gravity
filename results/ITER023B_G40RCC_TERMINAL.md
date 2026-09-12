# Iter023B / G40-RC-C terminal result

- Run: `34710049387`
- Head: `1f79d9c7e1ceb97ba0dc3273ef25d2c8664d42e6`
- Aggregate job: `103597100244`
- Summary artifact: `10303335725`
- Digest: `sha256:6b3d446be11880ae79cad0a55b74ccfff0cdf33a55f1045e04b27d6752f56f74`
- Classification: `AXIS_FRAME_COVARIANT_RTN_SEARCH_CALIBRATED`

Frozen positive-control calibration passed 4/4 Sobol and 4/4 LHS lanes. All hidden controls were eligible under the candidate-axis-frame covariant witness. Minimum hidden/recovered axis-covariant BLP was about `0.8471377488`, versus the frozen `>0.02` threshold. Worst recovery gaps were `1.7318444583e-15` (Sobol) and `9.3676432435e-16` (LHS), well below `<0.002`.

Scope: this calibrates the finite symmetric hidden-classical RTN search with a witness co-rotated to the candidate's local noise axes. It is family-axis covariant, not a global optimization over all BLP state pairs. PASS authorizes only the separately preregistered prospective G40-RC-A adversarial gate.
