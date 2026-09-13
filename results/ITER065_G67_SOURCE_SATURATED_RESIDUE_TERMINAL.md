# Iter065 / G67 — source-saturated pole/residue viability audit — TERMINAL

Terminal classification: `FOUR_DERIVATIVE_LINEARIZED_SOURCE_SATURATED_OPPOSITE_RESIDUE_COUPLING_SCOPED`

## Frozen provenance
- preregistration: `757ad475331bee15efec66ef73623e1e484be291`
- implementation: `416d486329d8832ffa113a792359bd36d7160c87`
- production head / launch: `4e0251d5ab6eb95c1873cff8c9412cd5a626d4b2`
- run: `34770704574`
- aggregate job: `103759759785`
- aggregate artifact: `10321956604`
- aggregate digest: `sha256:1fa501166026e2d8d3ab13ae29353c8c3a763e40afb59b4230acf2a8c0cd5061`

The preregistration preceded implementation and production output. No frozen source panel, coefficient ray, evaluation point, control or criterion was changed after production.

## Raw streams consumed
- A TT source saturation: job `103759656367`; artifact `10321358931`; digest `sha256:c8af46f1cc98d3db22941c168c48e5f89a893674300dc85b30d65ac629973e35`. Result: 96/96 exact residue checks PASS; all 12 frozen pure-TT source numerators were nonzero.
- B scalar source saturation: job `103759656324`; artifact `10321507146`; digest `sha256:57fbcad676b30be1285ea2f3df81b984cf0f6e971d211faa7bab87713c5acc58`. Result: 96/96 exact residue checks PASS; all 12 frozen pure-scalar source numerators were nonzero.
- C generic conserved-source reconstruction: job `103759656319`; artifact `10321986471`; digest `sha256:fd400a77507db8d33c23bfe01ab933ba553c94ceee175e4f5a75975b270f934b`. Result: 384/384 exact direct-vs-partial-fraction source-saturated amplitudes PASS; `invalid_frozen_lanes=0`.
- D discrete-Lorentz saturation invariance: job `103759656190`; artifact `10321528337`; digest `sha256:9786dccd3c7c5f70b62c9996bd7129ae046a695c1a2ecdd8d6a0cc9e66d48f79`. Result: 2448/2448 exact checks PASS; `invalid_or_failed_lanes=0`.
- E exceptional/false-positive controls: job `103759656288`; artifact `10321568315`; digest `sha256:014fa5a889d29493271a6479a436f84896926c676016aea2ad2e7929890421de`. All six controls PASS: TT exceptional `b=0`, scalar exceptional `3a+b=0`, pure-scalar no-TT, pure-TT no-scalar, nonconserved-source guard, and incorrect Euclidean saturation convention rejected. Example contraction mismatch: frozen Minkowski `-123/56` versus Euclidean `108887/1568` for `k=(1,2,3,4)`, seed 10.

Aggregate consumed all five structural-valid raw streams and returned A/B/C/D/E=`true`.

## Scientific interpretation
Within the frozen local linearized four-derivative class, the additional poles and opposite relative residues identified in G61–G62 are not merely artifacts of one TT/scalar representative and do not disappear after exact saturation with the complete G65 conserved symmetric-source response. Nonzero pure-sector sources couple to both simple-pole residues with exact relative ratio `-1`; generic conserved-source amplitudes reconstruct exactly from the frozen TT and scalar partial fractions; the statement is stable under the frozen discrete-Lorentz panel and respects the exceptional coefficient lines.

This result is deliberately narrower than a physical-ghost statement. It does **not** establish negative-norm states, instability, quantum nonunitarity, coefficient exclusion, nonlinear inconsistency, a global gravity no-go theorem, new physics, or full quantum gravity. Those require additional assumptions and separate gates.

Programme readiness remains **66%**. Theory established remains **0%**.
