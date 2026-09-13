# Iter080 / G82 — C minimal source-calibration augmentation

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/RESULTS**
Date: 2026-09-13
Parallel status: **C-SPECIFIC SIBLING OF G83-D; COMMON BASE IS POST-G81 MAIN**

## Scope
G80 established that the already-frozen C source-functional object does not natively break the exact C/N1 response-slope alias. G82 therefore permits exactly one new construction hypothesis: a **source-labelled reference calibration channel** that is candidate-blind but nuisance-sensitive.

This channel is not claimed to exist physically. It is a minimal construction-sufficiency witness only. It must not modify the C candidate functional, its transverse/Ward embedding, Gaussian CTP sector structure, or the G72 pole-free response witness.

## Frozen augmentation
Science response coordinates remain exactly the G73/G74 pair
`C(z)=-z`, `N1(z)=+z`.

Add one separate reference-channel row
`R_C(q)=(partial_C,partial_N1)=(0,q)`
where `q` is a known nonzero source-tag response. The reference channel is defined outside the candidate C functional: it probes the same nuisance calibration coordinate N1 but carries zero derivative with respect to the candidate C deformation coordinate.

Frozen direct strengths: `q in {1,2,5/3}`.
Frozen primary panel: `{1/3,2/3,5/4,7/3}`.
Held-out panels: `{1/5,3/5,4/3,9/4}` and `{2/7,5/6,7/5,11/3}`.

For the source-defined control, reuse the exact G72 transverse projector construction at `k_ref=(1,2,3,4)` with a new frozen reference seed `37`; define `q_ref` as the exact squared norm of its projected transverse source. `q_ref` must be nonzero. This source tag is a construction input, not an observed physical apparatus.

## Independent streams
### A — one-channel algebraic sufficiency and minimality
For primary and both held-out panels:
- science-only `(C,N1)` rank must be exactly one;
- appending `R_C(q)` for each frozen nonzero `q` must give exact rank two;
- `q=0` must leave rank one.

### B — source-defined reference strength with inherited Ward projection
Reconstruct the exact G72 transverse projector `P_T=P2+P0` for the frozen G72 momenta/source seeds and for the new reference seed 37 at `k_ref`.
Require:
- all frozen science projected-source weights used in the audit are nonzero;
- `q_ref` is nonzero;
- multiplying both science columns by any common projected-source weight preserves science-only rank one;
- appending the separate candidate-blind reference row `(0,q_ref)` restores rank two;
- the original projected science tensors remain exactly transverse/Ward compatible.

### C — non-modification of the C candidate object
The augmentation must be block-separate from the C candidate functional. Frozen predicates:
- the science response rows before and after augmentation are byte-for-byte/algebraically identical;
- the native Gaussian CTP zero-derivative response-sector rows remain zero;
- the candidate response factor remains the same frozen `exp(-ell2 z)` witness and is not multiplied or shifted by `q`;
- removing the reference row recovers the exact pre-G82 rank-one science design.

### D — adversarial false-anchor controls
Frozen controls:
1. same-shape pseudo-reference `(-q,+q)` must leave rank one;
2. zero pseudo-reference `(0,0)` must leave rank one;
3. candidate-only row `(q,0)` must give rank two but is flagged as **not** an accepted nuisance-calibration construction;
4. every nonzero rational rescaling of the accepted `(0,q)` row in `{1,-2,3/5}` must preserve rank two.

## Frozen aggregate rule
All streams valid =>
`C_SINGLE_SOURCE_REFERENCE_CALIBRATION_BREAKS_SLOPE_ALIAS_WITHOUT_MODIFYING_C_FUNCTIONAL_SCOPED`.

Any failed frozen scientific predicate => `SCIENTIFIC_FAIL_FROZEN_C_SOURCE_CALIBRATION_AUGMENTATION`.
Missing/invalid artifacts or controls => `INFRASTRUCTURE_OR_GATE_INVALID`.

## Interpretation ceiling
PASS means only that one explicitly added, candidate-blind/source-labelled reference channel is algebraically sufficient to break the exact C/N1 alias while leaving the frozen C construction unchanged in this finite audit. It does **not** show that such a reference channel is physically realizable, measurable, unique, natural, or candidate-owned. It does not select C, define nonlinear dynamics, or establish new physics.

Readiness remains 66%; theory established remains 0%.
