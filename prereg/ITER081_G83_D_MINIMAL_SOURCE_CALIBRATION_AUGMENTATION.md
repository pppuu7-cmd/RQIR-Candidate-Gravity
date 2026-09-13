# Iter081 / G83 — D minimal source-calibration augmentation

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/RESULTS**
Date: 2026-09-13
Parallel status: **D-SPECIFIC SIBLING OF G82-C; COMMON BASE IS POST-G81 MAIN**

## Scope
G81 established that the already-frozen D source-functional object does not natively break the exact D/N3 same-shape cubic calibration alias. G83 therefore permits exactly one new construction hypothesis: a **retarded source-labelled cubic reference calibration channel** that is candidate-blind but calibration-sensitive.

This channel is not claimed to exist physically. It is a minimal construction-sufficiency witness only. It must not modify the D candidate cubic functional, retarded support, Sigma-leg symmetry, CTP normalization, or the frozen zero-Hessian/nonzero-third-derivative jet structure.

## Frozen augmentation
The D science tangent and same-shape N3 calibration nuisance remain identical on the frozen G72 retarded symmetric cubic kernel `K3`.

Add one separate reference-channel row
`R_D(q)=(partial_D,partial_N3)=(0,q)`
with known nonzero source-tag amplitude `q`. The reference channel is defined outside the candidate D functional: it shares the calibration coordinate N3 but carries zero derivative with respect to the candidate D cubic-deformation coordinate.

Frozen direct strengths: `q in {1,2,5/3}`.

For the source-defined control, define a frozen symmetric retarded reference kernel on the G72 time grid `t in {0,1,2,3}` with equal nonzero entries at `(t_Delta,t_Sigma1,t_Sigma2)=(3,1,2)` and `(3,2,1)` and zero elsewhere. Its exact squared norm defines `q_ref`; `q_ref` must be nonzero. This reference kernel is a construction input, not an established physical signal.

## Independent streams
### A — one-channel algebraic sufficiency and minimality
Reconstruct all nonzero allowed entries of the frozen G72 D kernel. Using identical D/N3 science columns:
- science-only rank must be exactly one;
- appending `R_D(q)` for each frozen nonzero q must give exact rank two;
- `q=0` must leave rank one.

### B — retarded symmetric source-defined reference channel
Reconstruct both the candidate G72 kernel and the frozen reference kernel. Require:
- candidate kernel remains exactly retarded and Sigma-symmetric;
- reference kernel is exactly retarded and Sigma-symmetric;
- `q_ref` is nonzero;
- appending `(0,q_ref)` to the unchanged candidate science design restores exact rank two;
- no advanced-support entry is introduced into either candidate or accepted reference kernel.

### C — non-modification of the D candidate object and jet
The augmentation must be block-separate from the D candidate functional. Require:
- all candidate K3 entries before and after augmentation are algebraically identical;
- candidate CTP normalization remains exact;
- candidate Hessian at the frozen background remains zero;
- candidate third derivative remains nonzero;
- removing the reference row recovers the exact pre-G83 rank-one science design.

### D — adversarial false-anchor controls
Frozen controls:
1. same-kernel pseudo-reference `(q,q)` must leave rank one;
2. zero pseudo-reference `(0,0)` must leave rank one;
3. candidate-only row `(q,0)` must give rank two but is flagged as **not** an accepted calibration construction;
4. an advanced-support reference kernel with one nonzero forbidden entry must be detected and rejected;
5. every nonzero rational rescaling of accepted `(0,q)` in `{1,-2,3/5}` must preserve rank two.

## Frozen aggregate rule
All streams valid =>
`D_SINGLE_RETARDED_SOURCE_REFERENCE_CALIBRATION_BREAKS_CUBIC_GAIN_ALIAS_WITHOUT_MODIFYING_D_FUNCTIONAL_SCOPED`.

Any failed frozen scientific predicate => `SCIENTIFIC_FAIL_FROZEN_D_SOURCE_CALIBRATION_AUGMENTATION`.
Missing/invalid artifacts or controls => `INFRASTRUCTURE_OR_GATE_INVALID`.

## Interpretation ceiling
PASS means only that one explicitly added candidate-blind/source-labelled retarded reference channel is algebraically sufficient to break the exact D/N3 alias while leaving the frozen D construction unchanged in this finite audit. It does **not** show that such a reference channel is physically realizable, measurable, unique, natural, or candidate-owned. It does not select D, define nonlinear dynamics, or establish new physics.

Readiness remains 66%; theory established remains 0%.
