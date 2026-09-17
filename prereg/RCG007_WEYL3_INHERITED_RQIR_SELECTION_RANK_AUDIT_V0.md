# RCG-007 — inherited-RQIR selection-rank audit for the unique Weyl-cubed EFT coefficient v0

Date: 2026-09-17
Status: **PROSPECTIVELY FROZEN BEFORE ANY RCG007 SELECTION-RANK OUTCOME**

Programme-selection terminal:
`results/RCG007_PROGRAMME_DIRECTION_SELECTION_TERMINAL.md`, commit `ee8c606b5a1c5baa2f6547500b9675c70f469be6`.

Selected direction:
`WEYL3_INHERITED_RQIR_SELECTION_RANK_AUDIT`.

Parent RCG006 terminal:
`results/RCG006_FIELD_REDEFINITION_EQUIVALENCE_AUDIT_TERMINAL.md`, commit `e3a567d37911c1d86c5a98e3e9febc4938384731`.

Unique-class identity bridge:
`results/RCG006C_UNIQUE_EFT_CLASS_WEYL_CUBED_TERMINAL.md`, commit `d072cabcc4f5ccf46af382e16b7dbe62c935f3c4`.

Inherited selection-gap authorities:
- G88 terminal `results/ITER086_G88_C_INHERITED_CONSTRAINT_SELECTION_SUFFICIENCY_TERMINAL.md`, commit `9ecc7947d3a5e53e72acfbe9297e5dbc23cf155e`;
- G88/G89 synthesis `results/G88_G89_SELECTION_PRINCIPLE_GAP_SYNTHESIS.md`, commit `2204951424f37705f7031a122fda3cfcb1a18f00`;
- G90/G91 covariant-underdetermination synthesis `results/G90_G91_COVARIANT_UNDERDETERMINATION_SYNTHESIS.md`, commit `cf2463bbb2236a20c98dda5e50cdd620c8def8a7`.

Cross-architecture exclusion authority:
- G89 prereg `b4a0a867f937da0e4a557bcc07fc93ce7d567f02` explicitly freezes its cubic/three-point data as **D-specific**, acting only on quartic completion coefficients above the frozen D cubic representative.

Candidate-owned-control exclusion:
- `candidates/RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md`, commit `59e45f3503b677158827626b04d26e75479f2e82`, explicitly labels its nonlinear/covariant embedding as a **hypothesis / baseline embedding only**. It may be used as a control/reference but not as inherited candidate-independent RQIR evidence selecting the RCG007 coefficient.

## Scientific question

Let the already-terminal unique nonredundant local parity-even pure-metric bulk EFT direction be represented by

`S_alpha = S_ref + alpha * I_C3`,

where `I_C3` is the terminal RCG006C parity-even Weyl-cubed class.

Does the **already-frozen, admissible inherited RQIR information that predates this coefficient question** have nonzero exact selection rank on the single symbolic coefficient `alpha`?

This gate does **not** solve for `alpha`. It only audits structural sensitivity/rank.

## Frozen object identity

The coefficient space is exactly one-dimensional:

`A = span{alpha}`.

No second operator, field, kernel or coefficient may be added.

`I_C3` is not reconstructed by choosing a remembered operator list; its identity is inherited only from the terminal RCG006C bridge.

## Admissible inherited selector set

Only the following information may contribute rows to the scientific selector matrix:

### R1 — inherited flat-background lower jet through quadratic order
From G88: equality of value, gradient and Hessian at the flat background / preservation of the already-frozen quadratic/two-point data.

### R2 — inherited CTP lower-order identities
From G88: equal-history normalization, branch-exchange oddness and zero doubled-background Hessian, restricted to information already frozen before the cubic coefficient question.

### R3 — inherited quadratic Ward/projected-source sector
From G88: the already-frozen quadratic Ward-compatible response / projected-source sector. Only its pre-existing quadratic equations may act as selectors.

### R4 — bare general covariance / local scalar-density status
From G90/G91 synthesis: covariance itself is an inherited structural requirement, but it can select `alpha` only if exact covariance produces a nontrivial equation in `alpha`; otherwise it contributes rank zero.

No additional lower-order datum may be invented after outcome.

## Explicitly non-admissible as scientific selector rows

### X1 — G89 D cubic/retarded/CTP kernel
It is **D-specific** by its own preregistration and constrains quartic completion above a frozen D cubic representative. It is not an RCG007 pure-metric gravity observable/interface object. Without a separately frozen D-to-RCG007 bridge it is excluded from the scientific rank matrix.

It may be recorded only as a counterfactual control showing that genuinely cubic data could in principle have nonzero sensitivity.

### X2 — RCG002 covariant baseline hypothesis
The RCG002 linearized metric dynamics/retarded Green function is candidate-owned baseline structure, not inherited RQIR evidence. It may verify lower-order consistency but cannot select `alpha` in this gate.

### X3 — post-hoc coefficient conditions
`alpha=0`, naturalness/minimality, UV preference, stability, unitarity, phenomenology, observational fitting, or any chosen numerical value are forbidden unless they already existed as frozen candidate-independent RQIR constraints before this preregistration. None is imported here.

### X4 — `chi_ABC`
`chi_ABC` remains unauthorized and is not computed.

## Exact perturbative-order test

Introduce a formal flat-background scaling parameter `epsilon` with

`g = eta + epsilon h`.

Mechanically verify, using the exact Weyl-cubed construction already used in RCG006C or an independent equivalent construction, that the correction has no terms below cubic perturbative order:

`Delta S_alpha(epsilon) = alpha * epsilon^3 * W3 + O(epsilon^4)`

with a nonzero cubic coefficient polynomial `W3` on a generic exact curvature configuration.

Consequences are **not** assumed before execution; they are tested by exact derivatives at `epsilon=0`.

## Scientific selector matrix

For each admissible inherited constraint `F_i(alpha)=0`, extract the exact coefficient sensitivity

`J_i = d F_i / d alpha`.

Stack these into the exact one-column matrix

`J_RQIR(alpha)`.

Report:
- exact rows and their source authority category;
- exact rank;
- residual coefficient-space dimension `1-rank`;
- whether any admissible row is genuinely higher-order/cubic information rather than inherited lower-order structure.

No float/SVD/tolerance.

## Independent lanes

### Constructor
1. verify source/ownership census above;
2. mechanically certify the lowest perturbative order of `I_C3`;
3. construct the exact admissible selector rows from R1–R4;
4. compute exact rank.

### Critic
Independently:
1. audit admissibility/ownership and attempt to find an inherited nonzero selector missed by Constructor;
2. derive perturbative-order sensitivity by a different route (for example homogeneity/variation counting rather than importing Constructor rows);
3. test whether G89 D cubic information or RCG002 baseline could legally enter without a bridge;
4. reproduce rank or issue INVALID/BLOCKED if object identity differs.

## Positive controls

The gate machinery must detect:
1. a synthetic genuinely cubic datum proportional to the third derivative of the correction, whose sensitivity to `alpha` is nonzero on a frozen nonzero Weyl-cubed witness — rank one;
2. an explicit equation `alpha=0` as rank one **but flagged EXTERNAL_POST_HOC and excluded** from scientific rank;
3. a zero datum as rank zero.

These controls cannot contribute to the scientific selector rank.

## Frozen classifications

### `BLOCKED_SCOPED_RCG007_INHERITED_RQIR_SELECTION_RANK_ZERO_FOR_WEYL3_COEFFICIENT`
iff:
- all required source/object checks are valid;
- the admissible inherited selector set is nonempty;
- every admissible selector row is exactly `alpha`-blind;
- `rank(J_RQIR)=0` and residual coefficient dimension is `1`;
- positive controls demonstrate that the selector machinery would detect genuine cubic information.

This means current inherited RQIR information does not select the coefficient. It does **not** mean `alpha=0`.

### `PASS_SCOPED_RCG007_INHERITED_RQIR_NONZERO_SELECTION_RANK_FOUND`
iff at least one legally admissible inherited RQIR row has exact nonzero sensitivity and source/object identity is valid.

This gate still does not solve for `alpha`; a separate prospective coefficient-solving/falsification gate would be required.

### `BLOCKED_RCG007_MISSING_APPLICABLE_INHERITED_OBJECT`
iff the source audit shows that no admissible inherited object exists to instantiate the selected scientific question at all.

### `INVALID_RCG007_SELECTION_RANK_AUDIT_*`
for source/provenance mismatch, cross-architecture leakage, candidate-owned evidence promoted to inherited evidence, post-hoc selector inclusion, wrong Weyl-cubed object, or implementation disagreement.

## Interpretation ceiling

A rank-zero terminal result localizes the blocker to missing genuinely cubic/higher-order candidate-independent RQIR information. It does not prove no future selector exists and does not authorize setting `alpha`, adding dimension-eight operators, adding fields, or choosing nonlocality automatically.

A nonzero-rank result would only identify existing information capable of constraining the coefficient; it would not establish physical truth or a preferred theory.

No candidate theory is established by either branch.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
