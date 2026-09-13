# Iter073 / G75 — C/D minimal nuisance-anchor augmentation — TERMINAL

Date: 2026-09-13

Classification: `CD_MINIMAL_TWO_INDEPENDENT_ANCHOR_DIRECTIONS_RESTORE_LOCAL_IDENTIFIABILITY_SCOPED`

## Authority
- preregistration: `b8d7b0e98d9b2115985e1531925ed0920d84ae1b`
- implementation: `107e4d40c5634d8a697ad8f97c7ea642b2535745`
- production head: `7a2d00ef584c1b1ff9819856395bdd476947e37e`
- run: `34782200622`
- jobs: A `103791126550`, B `103791126673`, C `103791126624`, D `103791126701`, aggregate `103791160399`
- artifacts/digests:
  - A `10325725024`, `sha256:9ae83d56ea49bf1046ab537f7dfe8d8826d55407c1f798e3bf122f71c26b0b13`
  - B `10324629959`, `sha256:c5b1ce00513b9dacd86ecb229167d87c9d9555363a7d61f4b1712c3091a52ea2`
  - C `10324448657`, `sha256:81e13cf9fb5c2621971c56e3adbacd4f6eb3f57067be8be5472d5136a7f57763`
  - D `10325004317`, `sha256:22d5b4fd1cf1c04c4a8d2ee0239d3f0977df8fa0cf0d7aafedfcf638bb10dfe7`
  - aggregate `10325528374`, `sha256:d8c3fa8f6b26bcd9a531468adc5be1994cb36c609b47831e5e31924e57295f6d`

## Frozen result
All four raw streams were consumed and the frozen aggregate validated the preregistered classifications.

- A `DIRECT_TWO_ANCHOR_MINIMALITY_SCOPED`: baseline four-parameter design rank is 2; either independent nuisance anchor alone raises rank to 3; both raise rank to 4.
- B `DISTINCT_RESPONSE_TWO_AUGMENTATION_RESTORES_RANK_SCOPED`: one distinct quadratic-response row or one distinct cubic-response row alone raises rank to 3; both together raise rank to 4; same-shape controls do not break the corresponding aliases.
- C `HELDOUT_PANEL_AND_REPARAMETERIZATION_ROBUSTNESS_SCOPED`: the 2→3→4 minimality pattern holds on all three frozen held-out rational momentum panels and full anchored rank remains 4 under all three frozen invertible parameter reparameterizations.
- D `ADVERSARIAL_MINIMALITY_AND_FALSE_POSITIVE_CONTROLS_SCOPED`: duplicated one-sided anchors, zero anchors, and same-shape pseudo-anchors do not falsely produce full rank; breaking only one alias gives rank 3, not 4.

## Scientific interpretation
Within the exact G74 tangent model, two independent information directions are individually necessary and jointly sufficient to break the two exact nuisance aliases and restore four-column local algebraic identifiability. These can be represented by direct nuisance calibrations or by two added observables with linearly distinct quadratic and cubic responses in the frozen constructions.

This does not establish that physically realizable anchors exist, does not select C or D, does not fit physical coefficients, and does not define candidate-owned RCG-002 dynamics. Exact rank also does not guarantee numerical/statistical robustness; that is the next allowed robustness layer.

Programme readiness remains 66%; theory established remains 0%.
