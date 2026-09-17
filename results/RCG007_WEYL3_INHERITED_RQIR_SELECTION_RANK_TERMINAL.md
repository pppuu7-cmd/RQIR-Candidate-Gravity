# RCG-007 — inherited-RQIR selection rank on the unique Weyl-cubed coefficient

Date: 2026-09-17
Status: **TERMINAL SCOPED BLOCKER**

Programme-selection terminal: `results/RCG007_PROGRAMME_DIRECTION_SELECTION_TERMINAL.md`, commit `ee8c606b5a1c5baa2f6547500b9675c70f469be6`.
Scientific preregistration: `prereg/RCG007_WEYL3_INHERITED_RQIR_SELECTION_RANK_AUDIT_V0.md`, commit `85d6e8ef6a29ffac2ba1481fc6213e5f6f67abb4`.
Parent unique-class authority: `results/RCG006C_UNIQUE_EFT_CLASS_WEYL_CUBED_TERMINAL.md`, commit `d072cabcc4f5ccf46af382e16b7dbe62c935f3c4`.

The initial workflow run `35254221385` produced no scientific verdict because its aggregate was INVALID. Constructor and Critic both computed rank zero diagnostically, but a case-sensitive source-wording guard caused `constructor_valid=false`. The prospective wording-only execution repair is recorded in `results/RCG007_SELECTION_RANK_EXECUTION_ONLY_REPAIR.md`, commit `e61f2ce8e7bf0d34c07de3e74539cd9f30c61988`; the frozen science object, rows and classifiers were unchanged.

Canonical repaired run: `35254418803`, head `93d30d975dd086c44fa3154deb912d3d7689d0a7`.

Jobs:
- Constructor `105314409714` — success;
- independent Critic `105314409546` — success;
- aggregate `105314514104` — success.

Artifacts:
- Constructor `10512052772`, digest `sha256:4e5301404823485969eba82780683cb3d4cd24278f128f58b2033b2822be5832`;
- Critic `10511567926`, digest `sha256:c7419db8479a6549090a29b83fc22e6f9dcf33096a118cfdad6148f48f59edbf`;
- aggregate `10512137824`, digest `sha256:bf84320221cf83a6e6aa49c40524828b421d865902c28da2554725d2ac15bbf5`.

Canonical raw/provenance: `results/raw/RCG007_WEYL3_SELECTION_RANK_CANONICAL.json`.

## Terminal classification

**`BLOCKED_SCOPED_RCG007_INHERITED_RQIR_SELECTION_RANK_ZERO_FOR_WEYL3_COEFFICIENT`**

This is a scientific blocker, not a failure of the Weyl-cubed class and not a statement that its coefficient is zero.

## Exact result

The one-dimensional coefficient space is

`A = span{alpha}`

for the already-terminal unique nonredundant parity-even Weyl-cubed bulk EFT class.

The prospectively frozen admissible inherited selector set contains **22 exact rows** drawn only from:
- G88 flat-background value/gradient/Hessian information through quadratic order;
- G88 lower-order CTP equal-history, branch-exchange and doubled-background Hessian identities;
- the 12 G88 quadratic Ward/projected-source cases;
- bare general covariance as inherited structural information from G90/G91.

Constructor and independent Critic agree exactly that

**`rank(J_RQIR)=0`**

and therefore

**`residual coefficient dimension = 1`.**

Thus the already-frozen admissible inherited RQIR information is exactly blind to `alpha`.

`alpha = UNSELECTED`.

## Why this is not a limitation of the rank machinery

The mechanically constructed Weyl-cubed correction is nonzero and begins at cubic perturbative order. A frozen genuinely cubic synthetic selector has nonzero `alpha` sensitivity and exact rank `1` in both independent lanes.

Therefore the audit would detect a genuine cubic datum if one were legally present. The zero scientific rank is not caused by a broken rank calculation or by Weyl-cubed being the zero operator.

An explicit post-hoc condition `alpha=0` also has rank one as a control but is excluded from the scientific matrix by preregistration. Missing information is not interpreted as zero coefficient.

## Ownership firewall

The G89 cubic/retarded kernel is explicitly **D-specific** by its own preregistration and acts on quartic completion freedom above architecture D. It is not imported into the pure-metric Weyl-cubed problem without a separately frozen bridge.

The RCG002 covariant linearized baseline is explicitly candidate-owned hypothesis/control and is not promoted to inherited candidate-independent evidence selecting `alpha`.

No `chi_ABC`, source representative, new observable or coefficient condition was invented.

## Scientific consequence

The present bottleneck is no longer enumeration of local dimension-six pure-metric operators or field-redefinition redundancy. Those are closed in RCG006/RCG006C.

The bottleneck is now precise:

**a genuinely cubic or higher-order candidate-independent RQIR observable/constraint/selection principle applicable to gravity is missing from the admissible inherited authority set.**

Until such an object is sourced and prospectively bridged, the unique Weyl-cubed coefficient cannot be selected by the current RQIR information.

This does not imply `alpha=0`, does not falsify Weyl-cubed, and does not authorize adding dimension-eight operators, new fields or nonlocal kernels as a rescue.

## Interpretation ceiling

This gate establishes scoped structural underdetermination of one coefficient by the audited inherited RQIR information. It does not prove that no future RQIR selector exists and does not establish or falsify a complete gravity theory.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.

## Highest-information next front

Before expanding the gravity model class, perform a prospectively bounded **RQIR higher-order observable/source-authority census**: determine whether the repository already contains any candidate-independent genuinely cubic/third-variation observable or interface datum that can legally be bridged to the Weyl-cubed coefficient. If none exists, terminally record the missing-object blocker. If one exists, freeze its exact identity and a separate bridge before using it as a selector.
