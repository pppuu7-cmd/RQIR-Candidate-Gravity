# RCG002-NCP1: noisy nonlinear completion positivity — TERMINAL

Date: 2026-09-14. One prospective structural consistency gate; physical nonlinear evolution remains BLOCKED.

## STATE_READ / ACTIVE_FRONT
Frozen starting main: `446852d1675042b09a465e5eae32d482d78afe54`. Read recovery, clean ledger, its G95/G96/G97 addendum, and G97 preregistration. G97 run `34791265992` is terminal. Its aggregate `10327777470` was independently downloaded, inspected, and its ZIP SHA256 `7f906cad27023f582530c8eb7f90fd449f11902fdd6d455cf54eec0ae69facba` verified. Individual G97 artifacts were not redownloaded or the gate rerun in this review.

G97 is a closed classical two-probe-plus-apparatus momentum-conservation construction, NOT nonlinear gravity, Bianchi closure, or a quantum influence kernel. G95/G96 are finite noiseless ansatz qualifications. CPI1's exact noiseless obstruction leaves noisy kernels and higher-order terms open. No preceding verdict is weakened or replaced here. No dynamics from another candidate project enters NCP1.

## TARGET / WHY_HIGH_INFORMATION
NCP1 tests whether the still-open noisy continuation can preserve the specified lower-order source response and remain a positive quantum channel. This is a fatal prerequisite for a proposed source/state/evolution law, not a selected law, new covariant lift, rank-table variant, or competing CPI1/G95/G96 run. The physical frontier remains native nonlinear causal evolution on the G97 closed-source system.

The new information is an exact relation between phase-cycle defects and necessary coherence loss, a global restriction on exact polynomial log kernels, and a constructive nonuniqueness witness for complete positive kernels sharing a lower-order jet. None is a new physical measured datum.

## PREREGISTRATION / EXECUTION
Contract: `prereg/RCG002_NCP1_NOISY_COMPLETION_POSITIVITY.md`, commit `a796519c7859c33eb1f590740860cf7f388563e1`.
Implementation: `scripts/rcg002_ncp1.py`, commit `5fa99c16b9b6e7d81fb338e22d1daf9c8886efe0`.
Production: `2c761add0d4f4b055f426701a8fec76bbb2c667c`, run `34792497014`, attempt 1.
Jobs A/B/C/D/aggregate: `103819223716 / 103819223521 / 103819223656 / 103819223630 / 103819266588`.
Four independent matrix jobs, `max-parallel=4`, `fail-fast=false`, one aggregate after all lanes. There was no competing production run and no post-hoc extension of the moment cutoff. All 21 production control predicates passed (A5/B4/C6/D6). These are computational controls, not 21 physical model successes or four independent researchers.

Python 3.12.14; SymPy 1.14.0.
Code SHA256: `a013741d687cd3f0d474d6091d856fc9f891d05f94355aa0f064c13e0d6676fc`.
Preregistration SHA256: `c76d10b4d3d41278feac87a4e6fc7c6f79e2b90b79ba5ae233a2f681556da4a4`.
Original G72 script blob verified in CI: `8f67e57e3399b37f5e2ddb79d756932f7ce3200e`.

## 1. Local phase/noise compatibility — exact result
Write `d=x-y`, `s=(x+y)/2`, `Gamma_k=k*d*s^2`. The original G72 D1 ray with only coordinate zero nonzero has this scalar form because K000=1, up to symbolic amplitude k. This does not establish a physical G97 embedding onto that ray; D2 is not substituted for D1.

For a normalized Hermitian three-history kernel with coherence magnitudes r1,r2,r3 and triangle phase Theta,

`det F=1-r1^2-r2^2-r3^2+2*r1*r2*r3*cos(Theta)`.

Let delta_i=1-r_i. The zero-cycle part is exactly

`2*(delta1*delta2+delta1*delta3+delta2*delta3)-(delta1^2+delta2^2+delta3^2)-2*delta1*delta2*delta3`.

The remaining term is `2*product(1-delta_i)*(cos(Theta)-1)`. Consequently losses `O(epsilon^p)` and a nonzero leading cycle `c*epsilon^q`, with p>q, imply `det F=-c^2*epsilon^(2q)+o(epsilon^(2q))<0`.

On the frozen histories `(0,epsilon,2*epsilon)`, Theta is `-k*epsilon^3/2+O(epsilon^4)`. If all losses start at fourth order or later, then

`det F=-k^2*epsilon^6/4+O(epsilon^7)<0`.

Lane A independently parameterized all three quartic losses and a quartic phase correction and verified this coefficient. No higher-order-only damping can remove it. This result does not exclude pre-existing quadratic decoherence, nonanalytic losses, a modified cubic phase, or restricted physical histories. Smoothness on signed amplitudes is part of the preregistered interpretation; there is no all-noisy-kernel no-go.

## 2. Exact Gaussian-plus-cubic log kernel — global theorem and finite certificates
For the exact class

`F_nu,k(x,y)=exp(-nu*(x-y)^2+i*Gamma_k(x,y))`, nu>=0,

the identity `Gamma_k=k*(x^3-y^3)/3-k*(x-y)^3/12` gives diagonal-unitary congruence to the stationary kernel

`f(t)=exp(-nu*t^2-i*k*t^3/12)`.

If F were positive on every finite subset of the real line, f would be continuous, normalized and positive definite. Bochner's theorem would make it a probability characteristic function. Marcinkiewicz's theorem then excludes its genuine cubic polynomial logarithm for k!=0. Thus no finite Gaussian damping strength makes this exact global ansatz positive. k=0 is the Gaussian control.

Source verification: Bochner in DeCorte, de Oliveira Filho and Vallentin, Mathematical Programming 191 (2022), equation (20), https://doi.org/10.1007/s10107-020-01562-6 ; Marcinkiewicz in arXiv:2107.08469v3, Theorem 2.1 and Appendix A, https://arxiv.org/html/2107.08469v3 . Both read in HTML. Only their mathematical theorems are inputs; no candidate physics is imported. The matrix-cone meaning of complete positivity in the first paper is not used as a quantum-channel theorem.

For the hypothetical probability distribution, kappa2=2*nu, kappa3=k/2 and kappa_n=0 for n>=4. Moments were obtained by two independent exact methods through moment 64: cumulant recurrence and formal exponential coefficients. All agreed. Hankel moment matrices H_n=(m_(i+j)) must be PSD because every real polynomial has nonnegative E[p^2]. The frozen ascending LDL search, n=1,...,32, gave:

| k | nu | First negative degree | Matrix size | Negative quadratic form |
|---|---|---|---|---|
| 1 | 1/10 | 2 | 3 | -117/100 |
| 1 | 1/2 | 4 | 5 | -519/29 |
| 1 | 1 | 10 | 11 | -900630550751754749177647308759525 / 772258272806804637403918 |
| 1 | 2 | None through 32 | Through 33 | FINITE_TEST_INCONCLUSIVE |

For nu=1/10 the explicit witness is `p(z)=z^2-(5/2)*z-1/5`, with formal E[p^2]=-117/100. All exact witness vectors are in the raw archive. Post-terminal independent reconstruction verified their quadratic forms and determinant ratios. The nu=2 panel does NOT supply a finite negative certificate and is NOT a physical PASS; the independently sourced global theorem applies to the exact global model. The cutoff was not increased after seeing this result. Gaussian k=0 controls passed the full frozen range for all four nu values.

Lane A also derived the necessary central-moment inequality `V*M4-T^2-V^3>=0`, where V is variance and T the third central moment. For V>0 this becomes `kappa4>=T^2/V-2*V^2`. It constrains, but does not fix, higher-order noise. Neither this one minor nor a finite run proves global positivity.

## 3. Complete positive noisy kernels are nonunique
Consider only as a calibration counterexample

`Z=sigma*G+a*(N-lambda)`,

where G is standard normal and N is independent Poisson(lambda). From the defining Poisson series and Gaussian integral,

`E exp(i*t*Z)=exp(-sigma^2*t^2/2+lambda*(exp(i*a*t)-1-i*a*t))`.

With `lambda=k/(2*a^3)` and `sigma^2=2*nu-k/(2*a)`, the first three log orders are `-nu*t^2-i*k*t^3/12`. For nu>0, sign(a)=sign(k) and abs(a)>=abs(k)/(4*nu) give admissible nonnegative parameters. This is an allowed continuum of control completions, not parameter fitting.

Define `F_a(x,y)=exp(i*k*(x^3-y^3)/3)*E exp(i*Z*(x-y))`. For any finite history family and vector v,

`v^*F_a v=E abs(sum_i conjugate(v_i)*exp(i*k*x_i^3/3+i*Z*x_i))^2>=0`.

F_a has unit diagonal and is an average of diagonal unitaries, hence a normalized completely positive Schur channel. Its log agrees with Class II through cubic order but includes higher even damping AND higher odd phase terms. It is not a rescue preserving the exact cubic-only phase at every order.

Frozen examples k=nu=1:
- a=1/2: lambda=4, sigma^2=1; cumulants 1..4 are `(0,2,1/2,1/4)`.
- a=1: lambda=1/2, sigma^2=3/2; cumulants 1..4 are `(0,2,1/2,1/2)`.

Both exact full kernels are positive; their lower-order expansions agree and their fourth cumulants differ. Lane C checked the full symbolic matching and cumulants through order eight. Generally kappa_n=k*a^(n-3)/2 for n>=3. No member is selected or proposed as RCG-002 physics. This proves positivity plus the matching jet is insufficient to choose a full influence kernel. It does not prove nonuniqueness of an already specified gravitational theory.

## 4. Source symmetry, adversarial checks and limits
The G97 total translation generator is P=p1+p2+P_X. The relative Q=x1-X obeys [P,Q]=0, and any unitary function of Q preserves P. Both calibration families can thus preserve the same total translation generator. Absolute x1 fails the common-translation test. This closes no energy, Bianchi, stress-energy, autonomous-evolution or causal-dilation obligation: a translation-invariant abstract channel is not a physical nonlinear gravity law.

History rescaling gives k->k*r^3 and nu->nu*r^2 and leaves the restriction/nonuniqueness intact. With fixed histories/readout, reparameterizing the latent noise cannot identify two kernels with distinct fourth cumulants. No full field/source/readout equivalence quotient is available to claim anything stronger. The original scalar-source normalization is not physically fixed.

The finite moment result at nu=2 explicitly demonstrates why extra low-order numerical passes cannot establish a complete channel. Conversely, the positive nonpolynomial family explicitly defeats an overbroad claim that cubic response is impossible with any noise. Arbitrary physical history restrictions, noisy retarded mediators, or a proper EFT may lie outside the tested classes. Spacetime retardation, nonlinear conservation, Bianchi identities, physical preparation, and gauge-independent measured phases remain unestablished. No physical three-source prediction is computed.

## CLASSIFICATION / COMPLETION_SPACE_AFTER
`PASS_STRUCTURAL_NCP1` for the exact identities, controls and independently verified certificate/theorem application.
`FAIL_HIGHER_ORDER_ONLY_NOISE_RESCUE_SCOPED` for Class I.
`FAIL_EXACT_GAUSSIAN_CUBIC_LOG_KERNEL_SCOPED` for the exact global Class II, with finite-panel limitations retained.
`POSITIVE_NOISY_COMPLETIONS_NONUNIQUE_SCOPED` for Class III.
Overall: `BLOCKED_PHYSICAL_EVOLUTION`.
Selector rank: `UNDEFINED_PHYSICAL_MAP_MISSING`, not zero.

Two formal continuation classes are excluded in their frozen domains; a nonunique complete positive class survives. No reduction or dimension is asserted for the undefined physical gravitational completion quotient. Readiness remains 66%; theory established remains 0%. The work establishes necessary consistency restrictions, not a newly selected nonlinear gravitational dynamics.

## ARTIFACTS / PROVENANCE
All five NCP1 ZIP files were independently downloaded after terminal completion, SHA256 checked, and individual raw files compared byte-for-byte with the aggregate bundle copies. JSON payloads equal the embedded aggregate records.

| Artifact | ID | SHA256 |
|---|---|---|
| A | 10328810576 | b20db999f345cc837d18e392fa136922e567b063fbce219cc95e2f38144f7cd4 |
| B | 10328533762 | 200cf02c49614c65594a46d47753e3635aa81268e382599eb9a0d0e759496f7d |
| C | 10327644292 | 62807119814fd042c6766110badc46fce293a4b1ba262ef511d2efd1c16a8872 |
| D | 10328164412 | dfecf65ea1e325d9aac4b28a4ff905636cd438e37ef1ae7a462de7f2673f75b7 |
| Bundle | 10328693336 | b86d7ad7f1c4f9320bca8c79e929a7892018ee58a83f10affff194bcb1ad8b32 |

Durable raw archive: `results/raw/RCG002_NCP1_RAW_BUNDLE.json`, commit `8262b502b292b431863e2b862338679e324a767c`. Reconstruct the original summary with `json.dumps(archive,indent=2,sort_keys=True)+'\n'`; its SHA256 is `aa51d36abdfa222b4624ed1907a4ec99bf14c372db2758886a30bc45b47e012c`. Reconstruct individual lane files from `archive['lanes'][lane]` the same way and check the archived raw_sha256 mapping. Runtime timestamps are not expected to repeat on reproduction. Code and inputs preceded production; no partial values determined criteria or parameter panels.

## STILL_BLOCKED / EXACT_NEXT_ADMISSIBLE_STEP
The physical gate remains a native, independently motivated nonlinear causal source/state/evolution law on the closed G97 system. It must derive a full positive influence kernel, state and source mapping, recover the validated weak-field normalization and establish source/Bianchi/constraint compatibility within that same realization. NCP1 adds the requirement to specify compatible higher noise and phase terms together rather than assert an exact finite polynomial logarithm.

Do not run another arbitrary cumulant scan or increase the frozen moment cutoff as a substitute for that law. Do not adopt the Poisson/Gaussian controls, preferred coefficients, a reference channel or another programme's dynamics. Without a native new principle or physical datum fixing the hierarchy, retain `RCG002_REQUIRES_NEW_NONLINEAR_PRINCIPLE`. The scheduled-auto-research check found no active RQIRCG task; no automation was activated in this run.
