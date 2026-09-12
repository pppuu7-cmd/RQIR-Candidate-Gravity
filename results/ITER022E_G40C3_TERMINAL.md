# ITER022E / G40-C3 — terminal strict-search calibration classification

Run: `34708885346`
Head: `af8f23f7970d90d904914c938a8828d1cf847651`
Aggregate job: `103593923157`
Summary artifact: `10302603412`
Digest: `sha256:a2eda672b6c3a8e581a081b30e9d278619a0bf71356eb6587dbe8ac26f428845`

All 8 prospectively filtered-search calibration lanes passed.

- Sobol: 4/4 support; worst strict-candidate recovery gap `1.7318444583154354e-15`; minimum strict-candidate BLP `0.022161811061062853`; at least one strict candidate in every lane.
- LHS: 4/4 support; worst strict-candidate recovery gap `9.367643243488307e-16`; minimum strict-candidate BLP `0.022161811061063297`; at least one strict candidate in every lane.
- Frozen recovery tolerance: `<0.002`.
- Frozen fixed-witness filter: BLP total positive trace-distance increment `>0.02`.

Classification: `FIXED_WITNESS_STRICT_BLP_FILTERED_SEARCH_CALIBRATED`.

This result calibrates only the changed search/filter rule. It does not compare RCG-002. It authorizes the separately preregistered G40-A toy-trajectory adversarial gate. Scope remains the finite hidden-classical RTN family restricted by this fixed witness; it is not a rotation-covariant statement about all BLP-capable channels.
