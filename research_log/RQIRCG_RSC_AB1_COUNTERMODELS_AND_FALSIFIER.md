# RQIRCG RSC-AB1 — adversarial falsifier and countermodels

Status: PASS B under preregistration `80962231e55adbf96d7d24f47aeb9cd382d2e0a6`.

Purpose: attack every strongest Constructor candidate for hidden model content, residual freedom, representation dependence, circularity, or conditional external premises. No connected RCG-002 observable is computed.

## Falsifier lemma — admissibility is not selection

For a target model-definition slot `X`, suppose an axiom `A` is satisfied by two inequivalent realizations `M1` and `M2` that also satisfy the inherited frozen requirements, but `X(M1)` and `X(M2)` are not in an already-proven physical equivalence class. Then `A` is not a Level-III selector for `X`, even if `A` is independently physically motivated.

AB1 uses this only as decision logic, not as a claim about the dimension of physical theory space.

## A — attack on CSRC

Candidate: `Closed Same-Realization Source Completeness`.

### Exact counterfamily

Assume a complete closed source realization with covariant action `S_closed[g,Psi]` exists. For any scalar functional `F(Psi)` allowed by the same field content and any dimensionless `xi`, form the synthetic family

`S_xi = S_closed - (xi/2) Integral sqrt(-g) R F(Psi)`.

On an exactly flat calibration background `R=0`, choose the same closed preparation histories. The added term can vanish in the frozen preparation equations while metric variation changes the flat-background local source by the familiar conserved-improvement structure involving `(eta_mn Box - partial_m partial_n)F`.

Every member can include exactly the same probe, apparatus/support/control/binding fields and therefore satisfy CSRC's completeness demand. Yet the local source supplied to the carrier is not selected by CSRC alone.

This is a synthetic sufficiency countermodel, not a claim that RCG-002 matter possesses this operator.

### Hidden freedom

CSRC decides *which physical sectors must not be omitted*, but not what those sectors are microscopically nor which action/coupling they obey.

NO_SMUGGLING_TEST: PASS for the structural completeness rule itself; FAIL if it is silently upgraded to `therefore use a unique Hilbert source`.

INDEPENDENCE_TEST: PASS as an independently anchored requirement; selection test fails.

FALSIFIER VERDICT: `PARTIALLY_ANCHORED`; Level II only.

RESIDUAL FREEDOM: FUNCTIONAL + OPERATOR + field-ontology freedom.

## B — attack on EWU / equivalence-principle selection

Candidate: `Empirically WEP-Constrained Universal Coupling`.

### Measurement-kernel counterargument

MICROSCOPE constrains a specific differential-acceleration observable. Let `M` denote the map from future microscopic source/coupling parameters to the measured Eötvös ratio in that experimental domain. The datum constrains `M(theta)` near zero; it does not make `M` injective.

Any two candidate constitutions `theta_1 != theta_2` in the same experimental-equivalence fibre `M(theta_1)=M(theta_2)` satisfy the same WEP result. Such fibres necessarily remain undefined until a physical ontology and source-to-observable map are supplied; current RQIRCG has neither.

In particular, common-mode modifications, operators inactive in the tested regime, and curvature/improvement directions not mapped to differential free fall cannot be assigned coefficients from the WEP datum alone.

### Why `minimal coupling` does not follow

The experiment does not define the microscopic field basis, elementary/composite ontology, allowed curvature operator basis, or improvement quotient. Therefore `xi=0` or an analogous minimal-coupling prescription cannot be inferred from WEP without an additional model-dependent bridge.

NO_SMUGGLING_TEST: the empirical bound passes; converting it into a unique curvature action fails.

INDEPENDENCE_TEST: PASS as external datum, FAIL as Level-III selector.

FALSIFIER VERDICT: `PARTIALLY_ANCHORED`; Level I–II.

RESIDUAL FREEDOM: UNDEFINED before ontology; generically FINITE_PARAMETER/FUNCTIONAL afterwards.

## C — attack on CGD2

Candidate: `Consistent Gauge Deformation of the Two-Derivative Spin-2 Carrier`.

### Steelman that survives

The Boulanger–Damour–Gualtieri–Henneaux theorem is real selection power, not a GR analogy. Inside its hypothesis class, local perturbative gauge-consistent deformations of Pauli–Fierz massless spin-2 actions with at most two derivatives are extremely constrained.

### Premise audit

Current RQIRCG authority independently supplies:

- a linearized massless spin-2-type carrier variable and gauge law;
- weak-field source equation and retarded baseline;
- V2P1/RSC motivation for no extra carrier fields/scales, local two-derivative classical equations, gauge/constraint consistency and exact weak-field recovery.

Current authority does **not** independently supply:

- a prospectively selected local nonlinear carrier action principle;
- an exact off-shell Pauli–Fierz action representation as the physical ontology rather than merely an equivalent linearized equation/gauge presentation;
- a theorem that all admissible RQIRCG carrier dynamics must lie in the BRST/Lagrangian perturbative deformation class;
- a complete source/matter action with which the carrier deformation must be coupled.

Thus the external uniqueness theorem has the logical form

`[extra premises P] -> [strong restriction/Einstein-Hilbert deformation class]`,

not

`[current RQIRCG authority] -> P`.

Selecting `P` only because it unlocks the theorem would be model-content smuggling.

### Representation countercontrol

Barceló–Carballo-Rubio–Garay explicitly show that self-interaction conclusions can depend on the chosen free/off-shell gauge formulation, finding an entire self-coupling family and different GR/unimodular structures under different starting gauge formulations. AB1 does not import either theory; the result is used to show why the off-shell premise cannot be silently treated as representation-free.

### Countermodel status

No countermodel is asserted inside the full Boulanger theorem class: that would contradict the theorem. Instead the falsifier defeats Level-III *RQIRCG selection* by showing that membership in that theorem class is itself an unselected model datum at the current frontier.

NO_SMUGGLING_TEST: PASS for `preserve gauge/constraint consistency`; FAIL for promoting the full action/off-shell theorem class to inherited RQIRCG physics.

INDEPENDENCE_TEST: core consistency requirement PASS; Level-III dynamics selection FAIL.

FALSIFIER VERDICT: `PARTIALLY_ANCHORED`; conditional Level III, actual current Level II.

RESIDUAL FREEDOM: UNDEFINED outside the theorem class; source and quantum slots remain independent even inside it.

## D — attack on HSA and preferred-state rules

Candidate: `Hadamard State Admissibility`.

### Explicit inequivalent-state construction

Let `omega` be a Hadamard state of a linear field in a domain where the Hadamard framework applies. A coherent displacement by a sufficiently regular classical solution changes the one- and two-point functions by smooth terms while leaving the Hadamard singularity structure unchanged. The displaced state `omega_f` is physically distinct from `omega` for nonzero `f`, yet both satisfy the same Hadamard admissibility condition.

Thus HSA cannot select a unique state even in its cleanest domain.

### Preferred-state no-go control

Fewster–Verch further give a model-independent no-go against a generally covariant preferred-state assignment across all spacetimes for dynamically local theories under their stated assumptions. Therefore `choose the covariant vacuum` does not acquire selection authority merely by adding covariance language.

`pure`, `ground`, `no incoming`, `minimum entropy`, and `least decohering` also remain undefined or nonunique without a selected Hamiltonian/constraint, time/boundary structure, superselection sector and subsystem split.

NO_SMUGGLING_TEST: Hadamard admissibility PASS; `therefore choose this vacuum/state` FAIL.

INDEPENDENCE_TEST: PASS for admissibility, FAIL for unique state selection.

FALSIFIER VERDICT: `PARTIALLY_ANCHORED`; Level I–II.

RESIDUAL FREEDOM: STATE_SPACE + BOUNDARY_DATA + MEASURE.

## E — attack on CCR

Candidate: `Causal Completely-Positive Operational Reduction`.

### Existing exact counterfamily

RSC1 already supplies normalized positive random-unitary Schur kernels

`K_sigma(x,y)=exp(i(phi_x-phi_y)) exp[-(sigma^2/2)(f_x-f_y)^2]`

for `sigma >= 0`.

Different `sigma` values can share the same declared coherent phase and satisfy normalization/positivity. QCPT1/MAPF1 sharpen this further: exactly the same microscopic controlled unitary can yield different normalized positive reduced maps when the unobserved physical state changes, while lower-order data can remain identical.

Causal localization/no-signalling can restrict which such maps are admissible, but it does not specify the missing state, measure, subsystem split or interaction and therefore does not select one map from current authority.

Feynman–Vernon reduction likewise derives an influence functional after the external-system constitution/state/coupling are supplied; it is not a rule that selects those data.

NO_SMUGGLING_TEST: CPTP/causal requirements PASS; `trace the environment` as a complete prescription FAIL.

INDEPENDENCE_TEST: PASS as inherited structural requirement; Level-III selection FAIL.

FALSIFIER VERDICT: `PARTIALLY_ANCHORED`; Level II.

RESIDUAL FREEDOM: OPERATOR + STATE_SPACE + MEASURE + BOUNDARY_DATA.

## Cross-slot attack

Combining CSRC + EWU + CGD2 + HSA + CCR does not remove the residual freedoms:

- A still lacks a physical source ontology/action and allowed local operator basis;
- B cannot fix curvature coefficients until A supplies a bridge to the measured observable;
- C becomes near-unique only after an unselected action/off-shell premise is added;
- D leaves an actual state space;
- E leaves the reduction kernel undetermined until D and microscopic dynamics are fixed.

The MAPF1 source/state independence certificate prevents credit from being transferred between source and quantum slots. No compound package is therefore Level III under current authority.

## Strongest falsifier result

The strongest negative result is not `there are no physical anchors`. There **are** strong anchors.

It is instead:

> every independently supported anchor found in AB1 currently acts as an admissibility restriction or structural correlation, while the step that would turn it into model-definition selection requires at least one additional unanchored datum (ontology/operator basis, action/off-shell class, state/boundary choice, or reduction constitution).

This is precisely the distinction between `WHAT RQIRCG ACTUALLY FORCES` and `WHAT WOULD BE NEW MODEL CONTENT`.
