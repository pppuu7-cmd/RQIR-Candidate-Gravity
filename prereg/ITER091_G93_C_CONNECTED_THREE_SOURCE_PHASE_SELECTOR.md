# Iter091 / G93 — C connected three-source phase selector prerequisite — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN BEFORE IMPLEMENTATION / BEFORE SUBSTANTIVE RESULT**
Programme readiness entering gate: **66%**
Theory established entering gate: **0%**

## HYPOTHESIS
The highest-information candidate-owned nonlinear selector currently available in principle is the connected three-source branch phase obtained by extending the RCG-002 controlled-phase quotient to three relationally addressed binary probes. It is admissible as a selector for cubic nonlinear completion freedom only if:
1. it exactly cancels all inherited constant, one-body and pairwise phase information;
2. current RQIRCG authority supplies an explicit candidate-owned nonlinear source/dynamics map from at least two independent C-type cubic completion directions into this observable for physically defined source protocols;
3. the resulting selector Jacobian has invariant rank under admissible invertible coefficient reparameterizations;
4. null/false-positive controls do not fake rank.

If the operational connected phase is well defined but the nonlinear candidate-owned phase map is absent, the result is **BLOCKED_MISSING_CANDIDATE_OWNED_DATUM**, not selector rank zero.

## Exact candidate object
For three binary relational branch labels `a,b,c in {0,1}` and branch phase `phi_abc`, freeze the connected quotient

`chi_ABC = phi_111 - phi_110 - phi_101 - phi_011 + phi_100 + phi_010 + phi_001 - phi_000`.

This is the direct third finite difference of the same branch-phase object whose two-source quotient is already authoritative in RCG-002/G52-H. Defining the quotient introduces no nonlinear dynamics and no preferred completion coefficient.

## Completion space before test
The C branch has at least a two-dimensional **cubic completion freedom witness** from G86/G90. G92 qualifies the exact Ricci-only G90 pair as off-shell witnesses because they vanish on the frozen leading Ricci-flat shell. Therefore this gate does **not** treat `R^3` and `R Ricci2` as established on-shell physical directions. It asks whether current RQIRCG authority supplies any explicit candidate-owned map from two independent C-type cubic completion coordinates `theta=(theta1,theta2)` into `chi_ABC` across physical source protocols.

No coefficient value is authorized entering the gate.

## Genuinely new datum
`chi_ABC` is higher-order operational information because it annihilates every phase expressible as a sum of constant, one-body and pairwise branch contributions. A nonzero value therefore cannot be reconstructed from the frozen two-probe controlled phases alone. This algebraic property must be proved exactly in lane A/D before any selector interpretation.

## Frozen source authority for map-existence audit
The authoritative chain to be inspected after preregistration is frozen to:
- `candidates/RCG_002_RELATIONAL_CONTROLLED_PHASE_CHANNEL.md`
- `candidates/RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md`
- `results/ITER048_G52H_WEAK_FIELD_HAMILTONIAN_QUOTIENT_TERMINAL.md`
- `results/ITER055_G57P_CONSTITUTION_PREREQUISITE_AUDIT_TERMINAL.md`
- `results/ITER067_G69_CANDIDATE_OWNED_NOVELTY_PREREQUISITE_TERMINAL.md`
- `results/ITER084_G86_C_NONLINEAR_COMPLETION_NONUNIQUENESS_TERMINAL.md`
- `results/ITER086_G88_C_INHERITED_CONSTRAINT_SELECTION_SUFFICIENCY_TERMINAL.md`
- `results/ITER088_G90_C_COVARIANT_CUBIC_LIFT_TERMINAL.md`
- `results/ITER090_G92_LEADING_VACUUM_SHELL_WITNESS_AUDIT_TERMINAL.md`
- `recovery/CURRENT_FRONT.md`
- `research_log/RQIRCG_RESEARCH_LEDGER.md`

A valid candidate-owned map must explicitly define nonlinear source/geometry/dynamics dependence of `phi_abc` or `chi_ABC` on at least two independent completion coordinates and at least two source protocols. A mere operator family, covariance statement, reduced jet, abstract rank table, synthetic response vector, or statement that such a map should exist is **not** a map.

## Expected selection rank
If an explicit map exists, freeze `J_{p i}=d chi_ABC^(p) / d theta_i` at its stated reference point for the frozen physical protocols `p` supplied by that map.
- `rank(J)>=2`: `SELECTOR_RANK_SUFFICIENT` within the exact stated family/protocol scope.
- `rank(J)=1`: `SELECTOR_PARTIAL_RANK`; preserve the one-dimensional residual nullspace explicitly.
- `rank(J)=0`: `SELECTOR_RANK_ZERO`.
- rank that disappears under an admissible invertible coefficient reparameterization: `SELECTOR_REDUNDANT_UNDER_REPARAMETERIZATION` / implementation invalidity depending on cause.
- no explicit map or no physical protocol: `BLOCKED_MISSING_CANDIDATE_OWNED_DATUM`.

## Frozen lanes
### Lane A — connected-phase algebra
Prove exactly that `chi_ABC` annihilates the general multilinear phase
`k + A a + B b + C c + AB ab + AC ac + BC bc`
and returns exactly `T` for an added genuine connected term `T abc`. Also verify invariance under arbitrary added one-body and pairwise phase terms.

Required classification if valid:
`RCG002_THREE_SOURCE_CONNECTED_PHASE_IS_GENUINELY_BEYOND_PAIRWISE_SCOPED`.

### Lane B — candidate-owned nonlinear map existence/provenance
Inspect only the frozen source authority above. Require exact file presence and source-lock markers. Determine whether an explicit candidate-owned nonlinear `theta -> chi_ABC` map satisfying the definition exists.

Possible outcomes:
- map present and structurally explicit: `CANDIDATE_OWNED_THREE_SOURCE_NONLINEAR_PHASE_MAP_PRESENT_SCOPED`;
- map absent while authority explicitly retains missing nonlinear dynamics/selector locks: `BLOCKED_CANDIDATE_OWNED_THREE_SOURCE_NONLINEAR_PHASE_MAP_NOT_DEFINED_SCOPED`;
- provenance/source mismatch: `INVALID_PROVENANCE`.

### Lane C — rank/reparameterization calibration only
This lane is a pipeline control, not physical evidence. Use exact synthetic maps:
- rank-two control `[(theta1+2 theta2), (3 theta1-theta2)]`;
- rank-one control `[(theta1+theta2), (2 theta1+2 theta2)]`;
- zero control `[0,0]`.
Require exact ranks 2,1,0 and preservation of the rank-two result under frozen invertible coefficient transforms
`[[1,1],[0,1]]`, `[[2,0],[1,1]]`, `[[-1,2],[1,1]]`.

Required classification:
`THREE_SOURCE_SELECTOR_RANK_PIPELINE_CALIBRATED_SCOPED`.

### Lane D — inherited-data / false-positive adversarial controls
Require exactly:
- arbitrary sums of pairwise RCG-002-like controlled phases give `chi_ABC=0`;
- local branch rephasings give `chi_ABC=0`;
- a proportional duplicate source protocol cannot raise selector rank;
- an invertible coefficient basis change cannot change true rank;
- a deliberately inserted `T abc` term is detected as nonzero.

Required classification:
`THREE_SOURCE_SELECTOR_INHERITED_AND_FALSE_POSITIVE_CONTROLS_SCOPED`.

## Frozen aggregate rule
All lane artifacts must be structural-valid and consumed exactly once.

If A/C/D are valid and B reports map absent, aggregate classification is:
`BLOCKED_MISSING_CANDIDATE_OWNED_NONLINEAR_THREE_SOURCE_PHASE_MAP_SCOPED`
with `selection_rank = UNDEFINED_MAP_MISSING`.

If B reports an explicit map, the aggregate must compute its exact Jacobian rank without changing protocols/coordinates after inspection and classify only as:
- `C_CONNECTED_THREE_SOURCE_PHASE_SELECTOR_RANK_TWO_SCOPED`,
- `C_CONNECTED_THREE_SOURCE_PHASE_SELECTOR_PARTIAL_RANK_SCOPED`,
- `C_CONNECTED_THREE_SOURCE_PHASE_SELECTOR_RANK_ZERO_SCOPED`, or
- `C_CONNECTED_THREE_SOURCE_PHASE_SELECTOR_REDUNDANT_UNDER_REPARAMETERIZATION_SCOPED`.

Any missing frozen source, malformed lane, changed criterion, or provenance mismatch => `INFRASTRUCTURE_OR_GATE_INVALID` / `INVALID_PROVENANCE` as appropriate.

## PASS
Only exact rank >=2 from an explicit RQIRCG-derived nonlinear source/phase map, with frozen physical protocols and invariant rank, permits the scoped statement that this connected phase reduces the tested two-dimensional C-type completion freedom.

## FAIL / PARTIAL / ZERO
An explicit map with rank 1 or 0 is a scientific result. Do not change protocols or coefficients post hoc. Preserve the residual nullspace for rank 1; preserve full tested completion freedom for rank 0.

## BLOCKED
If the nonlinear candidate-owned map is absent, record the missing object exactly. Do not invent a phenomenological map, import another project's dynamics, or reinterpret the synthetic calibration as physical evidence.

## INVALID
Any post-hoc selector/source choice, missing prereg chronology, authority-file mismatch, artifact corruption, or coefficient-basis-dependent fake rank invalidates the gate.

## Interpretation ceiling
This gate can establish only the existence/nonexistence and local selection rank of one connected three-source operational selector within the frozen C-type cubic completion scope. It cannot prove unique gravity, complete field-redefinition equivalence, nonlinear Bianchi/diffeomorphism closure, source realizability beyond the supplied protocols, quantization/measure closure, experimental confirmation, or new physics.

Readiness remains **66%**. `THEORY_ESTABLISHED=0%` remains locked.
