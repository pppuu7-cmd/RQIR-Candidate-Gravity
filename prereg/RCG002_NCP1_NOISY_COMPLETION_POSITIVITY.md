# RCG002-NCP1: positivity of noisy nonlinear completions

Status: PROSPECTIVE; frozen before implementation/execution.
Date: 2026-09-14. Base: 446852d1675042b09a465e5eae32d482d78afe54.

## Purpose and authority
CPI1 excluded an exact noiseless interpretation of the G72 cubic response, but explicitly left noisy completions and omitted higher-order terms open. G95/G96 tested a finite noiseless polynomial class; G97 closed only classical total-source momentum bookkeeping. NCP1 tests a genuinely different, potentially fatal prerequisite for any proposed nonlinear state/evolution law: can noise complete the cubic response while preserving its specified lower-order jet? This is NOT a new gravitational law, duplicate CPI1/G95/G96, or selector fit. The main physical evolution frontier remains blocked until an independently motivated source/state/evolution law is supplied.

Inputs: original RCG-002 seed; construction contract; G72 D1 script; CPI1 terminal; current recovery; clean ledger and G95/G96/G97 addendum. No other candidate programme contributes physics. General probability/kernel mathematics is allowed as a consistency theorem, not as a candidate selection rule.

## HYPOTHESIS
A nonintegrable cubic phase cannot be made into a positive normalized influence kernel by arbitrary higher-order damping that leaves the quadratic coherent sector unchanged. A finite Gaussian-plus-cubic log kernel may fail even when some low-order minors pass. Exact noisy positive completions may exist but need not be uniquely fixed by the lower-order phase/noise jet. All three alternatives are to be tested, not presumed as a physical candidate verdict.

## Exact object and domains
For real freely variable scalar histories x,y let d=x-y, s=(x+y)/2, Gamma_k(x,y)=k*d*s^2 with real nonzero k. This is the CPI1 scalar control and the literal K000=1 restriction of G72 D1 up to an overall amplitude. The history-domain premise is explicit: no physical G97 source embedding onto this line is established.

Class I: normalized Hermitian smooth kernel with this leading cubic phase, triangular cycle Theta(epsilon)=-k*epsilon^3/2+O(epsilon^4) on histories (0,epsilon,2epsilon), and all three coherence losses 1-r_ij=O(epsilon^4). Determine whether arbitrary higher-order phase/damping terms can restore PSD. Also derive the necessary relation between noise order and cycle order; signed smooth source amplitude is assumed, not only epsilon>=0.

Class II: exact global scalar kernel F_nu,k(x,y)=exp(-nu*d^2+i*Gamma_k(x,y)), nu>=0. Analyze diagonal unitary congruence to a stationary kernel, distinguish a global theorem from any finite panel, and test exact derivative moment matrices. This is an exact ansatz, not an EFT truncation. The mathematical Marcinkiewicz theorem may be invoked only after verifying its hypotheses from a primary mathematical source.

Class III, explicitly nonphysical calibration family: centered Gaussian plus centered Poisson variable Z=sigma*G+a*(N-lambda), with independent standard normal G and Poisson N(lambda), lambda>0, sigma^2>=0. Define F(x,y)=exp(i*k*(x^3-y^3)/3)*E exp(i*Z*d). Require matching of the quadratic and cubic log jet of Class II; derive the whole higher-order tower and count surviving free parameters. This is a constructive counterexample to uniqueness of a positive kernel, not a candidate mediator or recommended rescue.

## Completion space before
No physical nonlinear quotient or selector Jacobian is defined. The formal classes above are nested test classes, not claimed complete physical RCG-002 families. k and nu are symbolic consistency coordinates, NOT selected physical coefficients. No reduction of the whole gravitational completion space may be inferred from a failure restricted to these classes.

## New information sought
An exact compatibility relation between nonlinear phase and decoherence, beyond diagonal CTP normalization/retarded support and beyond noiseless cocycle tests. A constructive pair of full positive kernels with identical lower-order jet would disprove the sufficiency of positivity for selecting the omitted nonlinear/noise tower.

## Four independent lanes
A: derive the general three-by-three Hermitian correlation determinant in magnitudes r12,r23,r31 and cycle Theta. Expand Class I using three independent symbolic quartic losses and a symbolic quartic phase correction. Test zero-cycle controls and the low-noise Taylor obstruction. Independently derive the first nontrivial stationary moment inequality in variance, third and fourth central moments.
B: prove the phase-congruence identity for Class II. Generate moments by two independent methods: cumulant recurrence and formal exponential coefficient recurrence. For fixed k=1 and nu in {1/10,1/2,1,2}, test Hankel matrices H_n=(m_(i+j)) for n=1,...,32 in ascending order, stopping only at the first strictly negative exact Schur pivot or determinant; preserve first-negative certificates. Zero pivots without a negative certificate are INCONCLUSIVE, not a scientific FAIL. k=0 Gaussian controls must pass all tested orders. Finite arithmetic does not prove a global statement; the independently checked theorem supplies that statement in its exact domain.
C: derive the exact Class III characteristic function from independence and the defining Poisson series. Match the jet symbolically. Fixed illustrations: k=1, nu=1, a in {1/2,1}; derive lambda and sigma^2, compare cumulants through order 8 and exhibit distinct fourth cumulants despite identical first three. Check PSD by the exact expectation/Gram construction, not a finite sample alone. No member is selected. The random-unitary integral must be normalized and trace preserving.
D: adversarial scope checks. Verify phase congruence preserves PSD, source-coordinate rescaling preserves the obstruction/nonuniqueness, and relational scalar Q=x1-X commutes with total translation generator P=p1+p2+P_X, while Q=x1 alone fails the closed-source test. This demonstrates that the G97 total-momentum requirement alone cannot select between positive scalar calibration channels. It is not Bianchi closure, a causal gravitational dilation or physical source realizability. Reconfirm K000 from the pinned G72 implementation independently of D2. Record which requirements remain untested, including actual spacetime causal support, state preparation, nonlinear conservation and source/readout mapping.

## Controls and fixed execution policy
All substantive predicates use exact symbolic/rational arithmetic. No numeric tolerance or hand-picked successful panel decides a verdict. Independent lanes may execute as GitHub Actions matrix jobs with max-parallel=4 and fail-fast=false; a single aggregate consumes exactly one result for every required lane only after all are terminal. No duplicate production run or post-hoc parameter changes. Python/SymPy versions, source/code/prereg hashes and raw outputs must be retained. Local runs, if used, are explicit implementation verification, not competing authorities.

## Outcomes
PASS_STRUCTURAL_NCP1: the exact identities and controls agree; record the actual scoped obstructions and any surviving formal family.
FAIL_HIGHER_ORDER_ONLY_NOISE_RESCUE_SCOPED: Class I has a strictly negative leading principal-minor coefficient for nonzero cubic cycle.
FAIL_EXACT_GAUSSIAN_CUBIC_LOG_KERNEL_SCOPED: Class II violates positive-definite-kernel requirements under the verified theorem and/or exact finite certificates, with domains distinguished.
POSITIVE_NOISY_COMPLETIONS_NONUNIQUE_SCOPED: two fully positive Class III examples match the first three cumulants and differ above them.
BLOCKED_PHYSICAL_EVOLUTION: no physical source/state/evolution map is supplied; rank remains UNDEFINED_PHYSICAL_MAP_MISSING.
INVALID: transcription, proof, control or provenance failure. Infrastructure errors are not scientific failures. No threshold, model, outcome criterion or selected coefficient may be changed after seeing results.

## Interpretation ceiling
No quantum gravity, candidate uniqueness, all-noisy-kernel no-go, experiment, physical nonlinear selector, full source/Bianchi closure, or readiness increase. A global exact-polynomial obstruction does not outlaw perturbative effective descriptions, finite physical history sets, restricted protocols, or nonpolynomial kernels. Poisson/Gaussian controls do not become RCG-002 dynamics. The next physical gate remains independently motivated causal nonlinear evolution on the closed total-source system, with a full positive influence kernel and matching to the weak-field baseline. NCP1 supplies necessary restrictions to that gate rather than replacing it.
