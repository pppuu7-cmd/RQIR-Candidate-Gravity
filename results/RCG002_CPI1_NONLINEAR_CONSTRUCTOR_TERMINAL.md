# RCG002-CPI1: nonlinear constructor and adversarial phase-integrability result

Date: 2026-09-14. Status: TERMINAL, SCOPED STRUCTURAL RESULT; PHYSICAL MAP BLOCKED.

## STATE_READ

The controlling project is `pppuu7-cmd/RQIR-Candidate-Gravity`, not another candidate programme. The user brief was treated as subordinate to live repository authority. Read the construction contract, original RCG-002 seed, linearized covariant baseline, clean ledger, recovery, G72 construction/code, G81/G83/G89 qualifications, G92/G93 terminal notes, and the G94 preregistration, executed implementation, Actions jobs and aggregate. While this run was underway G94 became terminal and recovery was synchronized by the other repository writer. No duplicate G93/G94 run was launched. The later overlapping G93 run 34788311792 remains quarantined.

CPI1 source input is the immutable commit `fcecaf0108576c0ab17b5dc3a94eeb3a8cc6dd96`. Its own prospective contract is commit `7be8d9f08eefb38caafe6718a367e5f43f3517e3`, file `prereg/RCG002_CPI1_CTP_PHASE_INTEGRABILITY_CONSTRUCTOR_AUDIT.md`. This is an orthogonal structural test, not a competing G94 inventory verdict.

G94 run 34789599885 and all five artifact ZIP files were downloaded through the authorized connector. Their SHA256 values were independently recomputed in the working container and matched the recorded values. Each of the four raw JSON payloads exactly matches its embedded copy in the aggregate. This establishes artifact consistency, not the truth of a dynamical theorem.

## CURRENT_FRONT

G94 remains `BLOCKED_D_CUBIC_CTP_OBJECT_LACKS_NATIVE_THREE_SOURCE_SOURCE_TO_PHASE_BRIDGE_SCOPED`. CPI1 adds a mathematical obstruction to one possible shortcut: interpreting the existing real one-Delta cubic response as a complete, exact, noiseless influence kernel on freely variable histories.

G94 review qualification: its B/D classifications are assigned after checks for limitation phrases in earlier documents. The implementation reproduces a documented inventory; it does not perform a constructive existence search or prove that no nonlinear principle can exist. Its text about different possible embeddings must not be read as evidence that those embeddings are physically consistent gravitational theories. Preserve the result, but consume it only with this narrower interpretation.

## CORE_PROBLEM

The pairwise seed defines a coherence-sensitive channel, not a nonlinear source law. The missing bridge is not just a coefficient or a choice of units. It must provide physical preparations, source coupling, state/evolution, a positive influence kernel, and an operational readout. A retarded response tensor does not automatically provide consistent branch phases.

## PHYSICAL_NONLINEAR_COMPLETION_SPACE

The physical space is not yet defined. Formally it would be the admissible source/state/dynamics/readout tuples modulo consistently transformed gauge, field-redefinition and boundary equivalences. Neither a complete underlying nonlinear object nor its physical source domain is specified by current RCG-002 authority, so its dimension and coordinate basis cannot be asserted.

G86-G91 demonstrate freedom within particular off-shell or reduced witness families. G92 qualifies the Ricci-only pairs on the frozen leading vacuum shell, but it does not supply a matter-coupled field-redefinition quotient. In a laboratory source problem, transforming an action without its source couplings and readout is not a proof of physical equivalence. The standard EFT discussion in Criado and Perez-Victoria, arXiv:1811.09413, section 2, equations (2.1)-(2.2), explicitly keeps the transformed source terms and Jacobian. No Weyl operator or other replacement is selected here.

## CANDIDATE_OWNED_DYNAMICAL_OBJECT

For the phase-preserving operational sector, the minimum evaluable object is a preparation map `b -> P_b`, `b=(a,b,c)`, together with a normalized positive influence kernel

`rho_out[b,b'] = F[P_b,P_b'] rho_in[b,b']`,

`F[b,b]=1`, `F[b,b']=conjugate(F[b',b])`, `F >= 0`.

A possible dilation represents it as

`F[b,b'] = Tr_M(U[P_b] rho_M U[P_b']^dagger)`.

This representation explains what must be specified, rather than introducing an RCG-002 mediator, Hamiltonian or initial state. For a finite Schur channel, positivity and unit diagonal are necessary and sufficient for complete positivity and trace preservation: factorize F into Gram vectors to obtain diagonal Kraus operators. A relativistic theory must additionally define a compatible kernel on its physical source family and satisfy causality and conservation; an arbitrary positive 8-by-8 matrix does not do that.

The trace representation is the standard CTP starting point; see Gao, Glorioso and Liu, arXiv:1803.10778v1, equation (2.1). It is used as a consistency template, not as newly derived candidate dynamics.

Candidate ownership classification: the need for a normalized phase-preserving channel and for the validated weak-field limit is DERIVED_FROM_RCG002. The unspecified preparation, nonlinear U, mediator state and full F are REQUIRES_NEW_PRINCIPLE. Choosing any particular one remains ALLOWED_BUT_NOT_SELECTED at best until the full contract is tested.

## DERIVATION

### A. Phase cocycle and positive-kernel obstruction

A normalized positive matrix has a unit-vector Gram representation. If every matrix element has modulus one, equality in Cauchy-Schwarz makes all Gram vectors collinear. Thus F has rank one and

`F[x,y] = exp(i(Phi(x)-Phi(y)))`,

`F[x,y] F[y,z] F[z,x] = 1`.

Conversely this factorization gives a diagonal-unitary channel. On a continuous real history neighborhood, the corresponding real phase obeys the local cocycle identity, not merely diagonal normalization and exchange oddness.

Consider the prospectively frozen scalar control

`Gamma_k(x,y)=k(x-y)((x+y)/2)^2 = k d s^2`,

with `d=x-y`, `s=(x+y)/2`. It is zero at x=y and odd under x/y exchange. Nevertheless,

`Gamma(x,y)+Gamma(y,z)+Gamma(z,x)=k(x-y)(x-z)(y-z)/4`.

For histories 0,1,2, the cycle is `-k/2`; the associated normalized 3-by-3 influence matrix has

`det F = 2 cos(k/2)-2 = -4 sin(k/4)^2`.

This is negative for small nonzero k. More strongly, for any nonzero k one can scale the histories by a sufficiently small nonzero epsilon to obtain

`det F = -k^2 epsilon^6/4 + O(epsilon^12) < 0`.

It therefore cannot be the exact noiseless Schur kernel on an open freely variable history domain. It even maps the equal superposition of these three labels to a nonpositive matrix F/3.

A positive control, not an adopted repair, is `Phi(x)=k x^3/3`. Its exact difference is

`Phi(s+d/2)-Phi(s-d/2)=k d s^2 + k d^3/12`.

The missing term is structural; changing an overall phase normalization does not fix it. This example does not authorize adding that term to RCG-002. The determinant obstruction is sixth order in history amplitude, so it does not by itself invalidate an EFT known only through third order with unspecified higher terms.

Noise also changes the question. For three coherence magnitudes r1,r2,r3 and phase cycle Theta, positivity requires

`1-r1^2-r2^2-r3^2+2 r1 r2 r3 cos(Theta) >= 0`.

A noisy kernel can have a nonzero cycle. This minor is necessary, not sufficient for positivity of the full eight-branch kernel. No general noisy D realization is excluded.

### B. Integrability versus the actual retarded kernel

For `Gamma_3=d_i K_ijk s_j s_k`, with K symmetric in its last two indices, a coherent phase difference on an open history domain requires

`V_i(s)=partial Gamma_3/partial d_i at d=0 = partial Phi/partial s_i`.

Consequently

`partial_l V_i - partial_i V_l = 2 sum_k (K_ilk-K_lik) s_k = 0`.

This requires symmetry between the response index and a source index; together with the existing last-two-index symmetry it requires full permutation symmetry. On distinct finite-grid times, full symmetry and support `t_i >= max(t_j,t_k)` force every nonzero triple to have equal times. A smallest-time index can otherwise be moved into the response position and would violate the support rule. Strict latest-time support forces the fully symmetric tensor to vanish.

The exact G72 D1 kernel was reconstructed, preserving its original sequential rational symmetrization. It still has 26 nonzero entries and satisfies its original support and Sigma symmetry. It fails coherent-potential integrability: for example

`V_0=s0^2`, `V_1=-3 s0^2-s0 s1+s1^2`,

`partial_1 V_0-partial_0 V_1=6 s0+s1`.

All six independent curls are nonzero polynomials; the raw payload records all entries and 34 ordered response-index-swap violations. Since `K_000=1`, restricting actual D1 histories to `(x,0,0,0)` gives the scalar obstruction above directly, without identifying D1 with the separate D2 surrogate.

The D2 reduced polynomial independently gives curl `2 s0`. Adding a homogeneous term cubic in d cannot fix either nonzero first-Delta response curl, because its first derivative vanishes at d=0.

These statements do NOT demand that a physical retarded susceptibility be a conservative history-space gradient. Ordinary open influence functionals need not have this property. They exclude only promoting this tensor to a single coherent phase potential on unrestricted histories. Noisy evolution, a retained mediator, restricted closed-loop physical source protocols, and continuum derivative-contact distributions require their own analysis and remain outside the exclusion.

## THREE_SOURCE_PROTOCOL

A concrete protocol specification, not a realizability result, uses three massive probes with internal two-level labels coherently correlated with two spatial wavepackets per probe. Define each trajectory, separation and recombination event relative to one laboratory/reference system. Use split-hold-recombine trajectories in the weak-field, slow-motion regime, with separated packets and a reference proper-time duration. Include traps, splitting/recombination controls, reference bodies and their momentum exchanges in the total source.

For four conditional experiments prepare B,C in labels b,c and A in |+>. Keep the same calibrated apparatus and initial environment rule. Measure both Pauli quadratures of A. A proposed realization must establish nonzero visibility, control over unwanted apparatus phases, and either a common coherent mediator final state or a justified noise/phase separation. Slow or long-duration evolution alone does not prove mediator closure.

No numerical geometry or duration is optimized here: there is no candidate response function from which a physical sensitivity could be calculated. This is a falsifiable specification of what a source map must deliver, not a claim that a gravitational three-source experiment has already been realized.

## MAP_TO_EIGHT_PHASES

A phase map exists in the exact coherent case when `F[b,b']=u_b conjugate(u_b')`, with `u_b=exp(i phi_b)`. In a pure-state dilation this means `U[P_b]|Omega>=exp(i phi_b)|Omega_final>` with the same final mediator state for every branch. Only then can seven independent relative phases reconstruct all eight phases up to an irrelevant common offset. The seed's known real local dephasing can be treated separately; an arbitrary complex noisy kernel cannot automatically be factored this way.

When this factorization and calibrated readout apply, define

`q_bc=<X_A>_bc+i<Y_A>_bc = v_bc exp(i(phi_1bc-phi_0bc))`, `v_bc>0`.

Then the desired observable is obtained without an absolute phase:

`exp(i chi_ABC) = q_11 q_00 conjugate(q_10) conjugate(q_01) / |q_11 q_00 conjugate(q_10) conjugate(q_01)|`.

Thus four conditional phase differences suffice for this one contrast; a phase-unwrapping convention is needed beyond modulo 2 pi. For a nonlinear state-dependent semiclassical rule, four separately prepared experiments need not represent coherences of one common eight-branch channel. The equivalence needs the common linear channel/preparation assumptions, or additional process validation. It is not silently assumed for every hybrid model.

Current RCG-002 does not supply the nonlinear U/F needed to evaluate these phases.

## CHI_ABC_PREDICTION

There is no established nonlinear numerical prediction. The inherited independent-source Gaussian/pairwise sector gives zero, but it is not the full nonlinear candidate prediction.

A conditional structural formula can be derived before choosing any dynamics. Suppose coherent factorization supplies a real action-valued functional W and the physical source preparations really are affine and independent:

`J_abc=J0+a A+b B+c C`, `phi_abc=W[J_abc]/hbar`.

Repeated use of the fundamental theorem of calculus yields

`hbar chi_ABC = integral_[0,1]^3 D^3 W[J0+u A+v B+w C](A,B,C) du dv dw`.

This is not a formula for a generic retarded in-in kernel: the coherent W assumption is essential. For the symmetric expansion

`W[J]=W1[J]+W2[J,J]/2+W3[J,J,J]/6+W4[J,J,J,J]/24`,

it gives exactly, within this quartic polynomial,

`hbar chi_ABC = W3[A,B,C] + W4[J0,A,B,C]`

`                  + (W4[A,A,B,C]+W4[A,B,B,C]+W4[A,B,C,C])/2`.

In zero background the cubic and quartic terms scale as q^3 and q^4 when source differences scale by q. In a fixed nonzero background the quartic term `W4[J0,A,B,C]` also scales as q^3. Therefore a three-source contrast does not isolate a cubic vertex universally, and amplitude scaling does not automatically separate cubic and quartic physics. W3 and W4 have not been derived or chosen for RCG-002.

## CONSERVATION_CHECK

For a zero-source flat background, expand consistent contravariant source components as `g=eta+epsilon h1+epsilon^2 h2`, `T=epsilon T1+epsilon^2 T2`. Covariant conservation requires

`partial_mu T1^{mu nu}=0`,

`partial_mu T2^{mu nu}=-Gamma1^mu_{mu lambda} T1^{lambda nu}-Gamma1^nu_{mu lambda} T1^{mu lambda}`.

The linear condition is insufficient. An exact control uses the external metric `ds^2=-N(x)^2 dt^2+dx^2+dy^2+dz^2`, `N=exp(epsilon f(x))`, and held dust `T^{00}=epsilon rho/N^2`, all other components zero. Its flat divergence is zero, but

`nabla_mu T^{mu x}=epsilon^2 rho f'(x)`.

This is an external-metric consistency counterexample, not a self-consistent gravitational solution. A held source needs supporting forces/stress. Source preparation and apparatus cannot be discarded from the nonlinear map. Conservation for an actual nonlinear RCG-002 realization remains BLOCKED, not demonstrated FAIL of an already specified candidate law.

## BIANCHI/DIFF_CHECK

Conditionally, an Einstein-baseline expansion would require `G_lin[h2]+G_quad[h1,h1]=kappa T2`, with the expanded Bianchi identity and consistent matter/apparatus equations. RCG-002 has not specified the nonlinear left-hand side, source evolution or constraint system needed to establish compatibility, constraint propagation, or absence of overdetermination. The displayed equation locates the missing obligation; it is not imported as the new candidate law.

## CTP/RETARDED_CHECK

Original G72 support/normalization facts survive. The extra exact noiseless coherent promotion fails as above. A physical noisy influence kernel or retained-mediator construction remains possible in principle but unconstructed. Full spacetime causal support and nonlinear quantum consistency are not implied by the four-time tensor.

## GAUGE_INVARIANCE_CHECK

The connected contrast cancels global, one-probe and prescribed pairwise phase additions algebraically. This is not full diffeomorphism invariance of a laboratory phase. A coordinate or field change must transform the source, apparatus, clock, boundary conditions and readout together. An arbitrary entangling rephasing proportional to abc is not a removable local gauge choice relative to fixed physical readouts. No full nonlinear gauge-independent phase map is established.

## BASELINE_DEGENERACY_CHECK

Standard GR already has non-additive three-body structure. In the conventional first-post-Newtonian N-body Lagrangian, the velocity-independent term is

`L_G2=-(G^2/(2 c^2)) sum_i sum_(j!=i) sum_(k!=i) m_i m_j m_k/(r_ij r_ik)`.

For three distinct bodies its distinct-index part is `-G^2 m_A m_B m_C/c^2` times `1/(r_AB r_AC)+1/(r_AB r_BC)+1/(r_AC r_BC)`. Source: Dubeibe, Lora-Clavijo and Gonzalez, arXiv:1607.00433v2, equation (1), PDF page 2. This is a standard-coordinate baseline action term, not by itself a gauge-independent laboratory phase prediction. Motion, supporting apparatus, reference time and all terms at the retained order must be included before a measurable subtraction is claimed.

The conditional phase contrast alone consequently does not establish quantization of gravity. The seed's correlated-local-phase comparator has a narrower entanglement constraint, but exclusion of that class cannot be generalized to every classical, semiclassical, stochastic or hybrid realization. Their quantitative discrimination would need specified state/coherence/causal predictions that are currently absent. No distinct RCG-002 scaling or coherence signature was derived.

## SELECTOR_RANK

`UNDEFINED_PHYSICAL_MAP_MISSING`.

One scalar cannot locally identify more than one independent continuous parameter without further information. For a known d-dimensional physical quotient, at least d independent scalar protocols are necessary for full Jacobian rank, but not sufficient. Here d is unknown; the off-shell two-coordinate examples do not authorize declaring two physical protocols sufficient. The four Ramsey settings are measurements of one scalar, not four independent nonlinear selector directions.

## ADVERSARIAL_COUNTEREXAMPLES

At the purely operational level, `U_lambda=U_pair exp(i lambda |111><111|)` is unitary for every real lambda and preserves the zero-branch two-probe faces. It changes chi by lambda. This proves the operational lower-order data do not fix the connected phase; it is not a family of established causal, covariant gravity completions, and lambda is not selected.

A second counterexample is a nominally pairwise phase evaluated on spectator-dependent preparations: `phi=a b (1+eta c)`. Its binary third contrast equals eta, even though the instantaneous interaction may be pairwise in its own physical source variables. Hence the independent-preparation premise is indispensable. This does not contradict G93's exact theorem about truly pairwise functions of independent binary labels.

Further attacks retained above are the exact negative positive-kernel minor, the actual G72 response curl, the held-dust conservation counterexample, the fixed-background quartic/cubic scaling degeneracy, and the ordinary GR baseline. Positive controls do not become candidate mechanisms.

## RESULT

The run produced an evaluable specification of the minimum missing bridge and an exact obstruction to an attractive but invalid shortcut. It did not construct candidate-owned nonlinear gravitational dynamics. Current principles determine necessary operational constraints and the weak-field benchmark, but do not fix the physical source/state/evolution object required for a nonlinear prediction.

## CLASSIFICATION

`PASS_STRUCTURAL_CPI1` for the exact identities and counterexamples.

`FAIL_SCOPED_UNRESTRICTED_HISTORY_NOISELESS_KERNEL` for the naive exact one-Delta-only promotion.

`BLOCKED_REQUIRES_NEW_NONLINEAR_SOURCE_STATE_EVOLUTION_PRINCIPLE` for the physical RCG-002 map.

These concern different propositions and are not contradictory. They do not constitute a general impossibility theorem for D, RCG-002, or quantum gravity.

## NEW_SCIENTIFIC_FACT

The gap is sharper than missing normalization: the existing retarded cubic construction has neither the phase-cocycle positivity required for a complete noiseless history kernel nor the integrable response needed for a single coherent history potential. Supplying a source embedding alone does not automatically cure either problem. A full influence/state/evolution rule, or a physically justified restricted closed-mediator protocol, is required before eight phases can be predicted. This is new within the programme; no claim of literature novelty is made.

## WHAT_IS_STILL_NOT_ESTABLISHED

Physical nonlinear completion space; candidate-owned W3/W4 or alternative nonlinear evolution; source-to-history embedding and dimensions; total-source conservation; Bianchi/constraint closure; physical source realizability and visibility; full spacetime causality; quantum state/measure completion; candidate-specific baseline discrimination; externally tested prediction. In particular `hbar -> 0` is not established by writing an action divided by hbar.

## CLAIM_CEILING

Programme readiness remains 66%; theory established remains 0%. These are inherited bookkeeping labels, not probabilities or percentages of solved physics. No new mechanism, coefficient, selected architecture, completed gravity theory, global classical no-go, or experiment is claimed. An exact-exponentiation obstruction is not a leading-order EFT failure. Source-history restrictions or noise may change the tested domain and require a new prospective gate, not retrospective alteration of CPI1.

## COMMITS / ARTIFACTS

Preregistration: `7be8d9f08eefb38caafe6718a367e5f43f3517e3`.
Executed code persisted: `eed477ca6b098c6953f9cbfe1f78e4e06edc3cc5`, `scripts/rcg002_cpi1_ctp_phase_integrability.py`.
Raw archive: `75abe9179f24f0c39b39138dbb9fa101bb429c48`, `results/raw/RCG002_CPI1_RAW_BUNDLE.json`.

Execution was local, not a new GitHub Actions run. Four independent process lanes ran concurrently with frozen inputs; all 28 checks passed (A:7, B:10, C:8, D:3). This is parallel computation and analytic self-review, not four independent human/AI reviewers. Exact identities control the verdict; two fixed eigenvalue examples are illustrations only. Python 3.13.5 and SymPy 1.14.0 were recorded. Code was committed after execution, but its contract was committed before execution; the archived executed bytes are identified by their digest.

Code SHA256: `b5ac9f9a0e60ca65aa401cdd58c457f989a718eb7b8cdc22bffa1baccd035e8f`.
Raw A/B/C/D SHA256 values, original timestamps, process IDs, exact kernel entries, checks and summary are retained in the bundle. Recreate each original JSON file using `json.dumps(payload,indent=2,sort_keys=True)+'\n'` in UTF-8 to verify the stored hashes. Re-execution changes only runtime metadata and possibly floating illustrative rounding; compare exact mathematical payloads rather than requiring runtime timestamps to repeat.

Primary outside sources, used only for consistency/baseline context:
- Gao, Glorioso, Liu: arXiv:1803.10778v1, equations (2.1), (2.4)-(2.8).
- Criado, Perez-Victoria: arXiv:1811.09413, section 2, equations (2.1)-(2.2), printed page 6; source transformation/Jacobian requirement visually checked.
- Dubeibe, Lora-Clavijo, Gonzalez: arXiv:1607.00433v2, equation (1), PDF page 2; mathematical expression checked in parsed full text. PDF screenshot retrieval for this paper and Ghostbusters failed, so no visual verification of those two pages is claimed.

## EXACT_NEXT_ADMISSIBLE_GATE

Exactly one next fundamental gate: **candidate-owned nonlinear source/state/evolution and conserved-source closure**. Before evaluating a connected phase, it must state an independently motivated physical preparation and total source, state and causal evolution rule, and derive the associated positive influence kernel (or demonstrate coherent factorization on the specified closed-mediator protocol). Verify nonlinear source/Bianchi/constraint compatibility within that same realization and recover the established pairwise weak-field normalization.

If the current seed supplies no such principle, record `RCG002_REQUIRES_NEW_NONLINEAR_PRINCIPLE` and define any proposed extension as a new prospective version. It can remain an extension of RCG-002 if the original operational sector and its limits survive; replacing those defining properties requires a distinct candidate. Neither adding a d^3 control term nor choosing a GR/EFT interaction is automatically authorized. Do not proceed directly to a selector fit, a measure, or quantum-gravity completion.
