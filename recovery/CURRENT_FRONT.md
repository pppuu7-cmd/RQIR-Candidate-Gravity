# RQIR-Candidate-Gravity current front

Updated: 2026-09-14
Phase: `G97_CLOSED_TOTAL_SOURCE_PREPARATION_PASS / NCP1_POSITIVITY_RESTRICTIONS_TERMINAL / NP1_CONTINUUM_CONNECTED_EXTENSION_UNDERDETERMINATION_TERMINAL / NEW_CANDIDATE_VERSION_PRINCIPLE_FRONTIER`

## Canonical status
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Programme readiness: **66%**; theory established: **0%**. These are bookkeeping labels, not probabilities.
- Scientific authority: newest `main`, this recovery file, dedicated RQIR-CG ledger and addenda, terminal notes, validated Actions artifacts.
- Latest clean-ledger addendum: `research_log/RQIRCG_RESEARCH_LEDGER_NP1_ADDENDUM.md`.
- Legacy mixed-project ledgers are not scientific authority. `recovery/state.json` remains absent.
- Independence lock remains active: no QGR/MSQGR/CRQN/KMQGB/RQIR/ISQGR candidate dynamics or preferred coefficients may be imported as selection principles.

## Latest terminal — NP1 connected-channel extension nonuniqueness
Preregistration: `1c63d49ccfbc0978c0d791fabd335a00186fa4f4`.
Implementation: `85f858b693d2d97ff3ba5c6f2adce733b1bb5c94`, `scripts/rcg002_np1_connected_extension.py`.
Production: `aec4224051ec7858a5ac47e4c6f2b5cde2ddbcf2`; run `34816931926`, attempt 1.
Jobs A/B/C/D/aggregate: `103889466939 / 103889467028 / 103889466952 / 103889466721 / 103889592848`.
Raw archive: `772ca5b3d8c82fc3f303d48dea40023e1f42fbe6`, `results/raw/RCG002_NP1_RAW_BUNDLE.json`.
Terminal note: `71d9fff2d3354c2ee5e4cba50a4ace1234f54977`, `results/RCG002_NP1_CONNECTED_CHANNEL_EXTENSION_TERMINAL.md`.
Clean-ledger addendum: `a2294263c5a15168e96e8bd4964426c9a5d04acc`.

Artifacts A/B/C/D/aggregate: `10335754857 / 10336587388 / 10337465262 / 10337395169 / 10337205608`.
Verified ZIP SHA256 values:
- A `d0a9d337dbf14718f48872b11d623b04dff64b7cf5f0b0def3ee6ecf24a944fc`;
- B `18e295ca9f62796f30ce8dc250ca60685473d1496b8b3b0f4b4cb6f8c6507ac8`;
- C `d57f661fe66f993ab0cc8ad04f099fed5802f9500cb5886643b8945db21adb26`;
- D `14f6d95f92695fbf967b51604412a93e2836beda2490cc2a026242c56a2bc3d0`;
- aggregate `4b0b7d101410d21824400b13e4f14a5797e4336545659b05a5281602d29728c1`.
All raw lane JSON files exactly equal their aggregate copies. Scientific criteria were frozen before implementation and production; no competing NP1 production run or post-hoc threshold/parameter choice was used.

### NP1 theorem
On the three-bit branch cube define `q(a,b,c)=abc`. For any normalized PSD base Schur kernel `F0` reproducing the frozen lower coordinate faces, the multiplier

`C_lambda,gamma(x,y)=exp(i lambda [q(x)-q(y)]) exp(-gamma [q(x)-q(y)]^2)`, `gamma>=0`,

defines another normalized PSD Schur channel through `F=F0 .* C`.

Reason: seven vertices have q=0 and one has q=1. With `r=exp(-gamma)` the nonzero q-sector block is `[[7,sqrt(7)r],[sqrt(7)r,1]]`, with determinant `7(1-r^2)>=0`; the lambda factor is a diagonal unitary congruence. The Schur product theorem preserves PSD.

On every lower coordinate face `a=0`, `b=0`, or `c=0`, q vanishes and `C=1` exactly. Thus all frozen one-/two-source face channels survive unchanged.

The connected phase has exact third finite difference `lambda`, while every constant/one-body/two-body phase has third difference zero. Lambda therefore survives the lower-body rephasing quotient measured by the connected phase contrast. Gamma independently changes connected coherence magnitude. In `(connected phase, connected log-magnitude)` coordinates the exact Jacobian with respect to `(lambda,gamma)` is `diag(1,-1)`.

If the connected projector `Q=|111><111|` acts on internal branch labels, it commutes with the G97 total spatial translation generator. A finite-time time-local/random-unitary operational realization also exists. This demonstrates that normalized CPTP evolution plus lower-face recovery plus G97 total-translation compatibility still does not fix lambda or gamma. It does NOT establish relativistic microcausality, stress-energy conservation, Bianchi closure or gravity.

### Terminal classification
`RCG002_CURRENT_PRINCIPLES_ALLOW_CONTINUUM_CONNECTED_CHANNEL_EXTENSIONS_SCOPED`.

Overall physical classification:
`RCG002_REQUIRES_NEW_NONLINEAR_PRINCIPLE`.

Operational connected-extension dimension lower bound: **>=2** within the frozen NP1 family (`lambda_connected_phase`, `gamma_connected_dephasing`). This is NOT the dimension of the physical gravitational completion space.

Physical selector rank remains `UNDEFINED_PHYSICAL_MAP_MISSING`, not zero.

### Scientific interpretation
NP1 converts the main gap from an informal missing-coefficient problem into a scoped exact underdetermination theorem. Current requirements jointly fail to determine nonlinear RCG-002 evolution even after imposing:
1. lower-order controlled-phase data;
2. normalized CPTP Schur evolution;
3. exact recovery of all frozen one-/two-source faces;
4. invariance against lower-body phase rephasings;
5. G97 total-translation compatibility;
6. an abstract finite-time normalized evolution.

Thus another rank/cumulant/positivity/lower-face test of the same architecture cannot by itself create the missing physical law. The current RCG-002 object is an underdetermined nonlinear interface architecture until a genuinely new candidate-owned principle is supplied.

## Prior terminal — NCP1
NCP1 remains authoritative and unchanged. It established:
- `FAIL_HIGHER_ORDER_ONLY_NOISE_RESCUE_SCOPED`;
- `FAIL_EXACT_GAUSSIAN_CUBIC_LOG_KERNEL_SCOPED`;
- `POSITIVE_NOISY_COMPLETIONS_NONUNIQUE_SCOPED`;
- overall `BLOCKED_PHYSICAL_EVOLUTION`.
Production run `34792497014`; terminal note `results/RCG002_NCP1_NOISY_COMPLETION_TERMINAL.md`.
NCP1 does not select a noisy completion; NP1 strengthens the underdetermination directly at the three-source channel-extension level.

## G97 retained prerequisite
`PASS_CLOSED_TOTAL_SOURCE_PREPARATION_CONSERVATION_SCOPED`, run `34791265992`.
G97 closes only classical source-preparation momentum bookkeeping. Probe-only momentum imbalance is exactly cancelled by apparatus, internal branch kicks preserve total momentum, and an external hold supplies a nonzero source. It is not nonlinear gravity or Bianchi closure.

## Physical nonlinear completion space
**Undefined.** G90/G91 finite off-shell witness coordinates, G92 on-shell qualifications, NCP1 noise parameters and NP1 operational lambda/gamma coordinates are not automatically physical gravitational degrees of freedom. A field/source/readout equivalence quotient has not been derived.

Therefore do not declare a physical dimension or selector rank from any of these formal coordinate counts.

## Exact next admissible fundamental gate
**NEW CANDIDATE VERSION PRINCIPLE GATE.**

The current version has reached a genuine model-definition boundary. The next admissible substantive step is not to choose lambda/gamma. It is to state exactly one independently motivated candidate-owned nonlinear source/state/evolution principle before looking at its connected-phase outcome.

A prospective new version must freeze, in one realization:
- physical field/state degrees of freedom;
- source preparation and source-to-history map on the closed G97 system;
- nonlinear evolution equation or influence/state rule;
- conservation and nonlinear Bianchi/constraint compatibility;
- retarded/spacetime causal structure;
- positive influence kernel or justified coherent/noisy factorization;
- recovery of the validated lower-order weak-field branch;
- prediction of connected phase/noise observables without fitting them.

The new principle must dynamically fix or derive the NP1 continuum freedom. It may not import another candidate programme or promote an NP1/NCP1 calibration construction into physics merely because it passes consistency checks.

If no independent RCG-002 motivation can be given, terminalize the current version as `RCG002_CURRENT_VERSION_NONLINEAR_DYNAMICS_UNDERDETERMINED`. Any extra law would then be a prospectively new version, not a retroactive completion of the old seed.

## Open layers and locks
Still open: native nonlinear dynamics; nonlinear stress-energy/Bianchi/constraint closure; physical source-to-history map; spacetime causality; physical completion quotient; state/measure completion; externally anchored prediction.

Forbidden claims remain `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, established nonlinear RCG-002, universal classical/semiclassical/noisy no-go, family-wide uniqueness, or green-CI-as-physics. Historical G72-G97/CPI1/NCP1 results and duplicate-G93 quarantine remain intact.
