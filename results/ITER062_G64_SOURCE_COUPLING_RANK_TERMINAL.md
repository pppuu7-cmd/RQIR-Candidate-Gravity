# Iter062 / G64 — source-coupling minimal-rank audit

Date: 2026-09-13

## Terminal classification
`FOUR_DERIVATIVE_LINEARIZED_TWO_MODE_SOURCE_COUPLING_RANK_TWO_SCOPED`

## Frozen authority
- Preregistration: `66dd0884a4e77500e76aaa2e9afe58d0bdf34b88` (before implementation)
- Implementation: `ea3e2cb2f69832be1b5c4286334bfaa113fc796c`
- Production head: `9e8db59a34d25ba3b6d9d9c6686da03d75652108`
- Run: `34767127085`
- Aggregate job/artifact: `103750064437 / 10320723301`
- Aggregate digest: `sha256:dfffd1e1832ff05dd8d1f7fac99f1323aff41a43dcbfb2f8809fbc80b4423ba6`

Raw lanes:
- A job/artifact `103749979026 / 10320957706`, digest `sha256:0a4253068d8abcfd1d0d7570583c711fe774acc249e987e2bfc40953210e595c`
- B job/artifact `103749979111 / 10320793178`, digest `sha256:b731afd8c6679718f52f3bbacdd09924463eced5518d36777e52e39e2b449e0b`
- C job/artifact `103749979132 / 10321067561`, digest `sha256:093ccb5d00980a98aebea035c104a295f4271577626c499b814e8f3afd0c8740`
- D job/artifact `103749979143 / 10321177212`, digest `sha256:4395e2dde98b6214a559c245ab8649c342077b49c401f389194750ca8708f176`

## Raw scientific result
- A: exact reconstruction valid; TT source-coupling rank = 2; scalar source-coupling rank = 2.
- B: all 12 frozen nonexceptional rational coefficient rays, in both TT and scalar sectors (24 sector cases), retain exact rank 2.
- C: all 16/16 frozen invertible real field-redefinition checks retain rank 2.
- D: exceptional one-pole cases reduce to rank 1 as required; zeroed-coupling rank loss is detected; duplicated-pole fake control is rejected.
- Frozen aggregate marks A/B/C/D all true and `valid=true`.

## Scientific interpretation
Within the already frozen local four-derivative linearized class and the same conserved TT/scalar sector responses used by G61–G63, both algebraic pole contributions are source-coupled and a rank-one realization does not reproduce the nonexceptional response. This is a scoped minimal-realization statement only.

It does **not** establish a physical ghost, instability, failure of quantum unitarity, a coefficient choice, a nonlinear completion, or a global higher-derivative no-go theorem. It also does not yet prove that the two special sector representatives exhaust the full conserved-source tensor space.

## Readiness
Programme readiness remains **66%**. Theory established remains **0%**.

## Next allowed gate
Prospectively test whether the G61–G64 two-sector conclusions extend to the complete conserved symmetric-source projector decomposition, with exact projector algebra, held-out conserved sources, basis/frame covariance and nonconserved false-positive controls. No physical viability claim is allowed before that gate is terminal.
