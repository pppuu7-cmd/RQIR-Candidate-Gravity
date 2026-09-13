# Iter059 / G61 terminal result — four-derivative conserved-sector pole stratification

Date: 2026-09-13

## Authority
- Preregistration: `9c1df1ef18710ef40036d54d715c70bd73a05441`
- Implementation: `05433da22bf3ad450d05cce90c2e167c18fbca7e`
- Production head: `37cedcd5c592e6f9a8a85a543d94b9f28624bcef`
- Run: `34758458121`
- Aggregate job: `103726911539`
- Aggregate artifact: `10316894782`
- Aggregate digest: `sha256:8d63d54b742446d75214b8055fcef117071ce28d714b8faa5e57b36b08a511db`

Raw lanes consumed:
- A job `103726876575`, artifact `10317913163`, digest `sha256:d9cad64167b66e7b5eeb36cddb36aadb5509219d86ec7a9b63141e02345b8cdb`
- B job `103726876525`, artifact `10317868310`, digest `sha256:a21f0e020719c553ce668a3f294f868901805c14181c37e3bc15a53df4c71730`
- C job `103726876481`, artifact `10316914469`, digest `sha256:c73b736cf43069fc79d020489a41bb10be084ddc9607ad455592eade4bfb7a37`
- D job `103726876555`, artifact `10316994281`, digest `sha256:64c6dac60997955f2d3f2418bef334023741c74a74edfb3a0bf48fe966faf33a`

## Frozen-gate evidence
- Stream A derived exactly `P_TT=z*(b*z-4)/2` and `P_scalar=3*z*(3*a*z+b*z+2)` directly from the frozen tensor definitions.
- Stream B: all 10 frozen rational rays matched the preregistered exceptional-root classification. `b=0` removes the additional TT algebraic root; `3a+b=0` removes the additional scalar algebraic root; no nonzero frozen ray removes both.
- Stream C: 30/30 quotient-basis covariance checks passed under the three frozen invertible coordinate changes.
- Stream D: 24/24 held-out direct evaluations matched exactly; deliberately wrong scalar combination `2a+b` rejected on 6/6 held-out coefficient pairs and deliberately wrong TT coefficient `a` rejected on 6/6.
- Aggregate: A/B/C/D all valid and PASS.

## Scientific classification
`FOUR_DERIVATIVE_LINEARIZED_SECTOR_ADDITIONAL_ROOT_STRATIFICATION_SCOPED`

Within the frozen local four-derivative linearized quotient added to the G59 baseline, every nonzero `(a,b)` direction produces at least one additional algebraic root across the two canonical conserved representatives. Exact exceptional lines are `b=0` for TT and `3a+b=0` for scalar, with simultaneous removal only at `(0,0)`.

## Scope ceiling
This is an algebraic sector-root statement only. It does not establish physical masses, ghosts, instability, nonunitarity, a global higher-derivative no-go theorem, nonlinear completion, or quantum viability. No candidate coefficient ray is selected. Programme readiness remains 66%; `THEORY_ESTABLISHED=0%`.
