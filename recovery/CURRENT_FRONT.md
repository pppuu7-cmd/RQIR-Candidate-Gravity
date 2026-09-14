# RQIR-Candidate-Gravity current front

Updated: 2026-09-14
Phase: `G97_CLOSED_TOTAL_SOURCE_PREPARATION_PASS / NCP1_POSITIVITY_RESTRICTIONS_TERMINAL / NP1_CONNECTED_EXTENSION_UNDERDETERMINATION_TERMINAL / CM1_CLOSED_MEDIATOR_NONUNIQUENESS_TERMINAL / NEW_CANDIDATE_VERSION_PRINCIPLE_FRONTIER`

## Canonical status
- Active seed: `RCG-002 Relational controlled-phase channel`.
- Programme readiness: **66%**; theory established: **0%**. These are bookkeeping labels, not probabilities.
- Scientific authority: newest `main`, this recovery file, dedicated RQIR-CG ledger/addenda, terminal notes, and validated Actions artifacts.
- Latest clean-ledger addendum: `research_log/RQIRCG_RESEARCH_LEDGER_CM1_ADDENDUM.md`.
- Legacy mixed-project ledgers are not scientific authority. `recovery/state.json` remains absent.
- Independence lock remains active: no QGR/MSQGR/CRQN/KMQGB/RQIR/ISQGR candidate dynamics or preferred coefficients may be imported as selection principles.

## Latest terminal — CM1 closed sequential mediator realization

Classification: `NONUNIQUENESS_SURVIVES_CLOSED_SEQUENTIAL_MEDIATOR_SCOPED`.
Overall physical status: `RCG002_REQUIRES_NEW_NONLINEAR_PRINCIPLE`.
Physical selector rank: `UNDEFINED_PHYSICAL_MAP_MISSING`.

Authority:
- preregistration `1e1c6556b42769cb1d0ce67e964c7f151351ec1c`;
- implementation `74caef5d4bba0a6a7106f68ab2efc3f44a543744`;
- production `6f45a31a3259000a3e3b832f616c03d74563767b`;
- run `34861269613`, attempt 1;
- jobs A/B/C/D/aggregate `104033804455 / 104033804121 / 104033804463 / 104033804464 / 104033938938`;
- artifacts A/B/C/D/aggregate `10355225608 / 10354464514 / 10354769236 / 10354469412 / 10354769307`;
- raw summary commit `391c4920438900414a3d885c4ac03882eb65fc72`, `results/raw/RCG002_CM1_RAW_SUMMARY.json`;
- terminal commit `ed446b2accee10a7d417df5d6580926a42d97126`, `results/RCG002_CM1_CLOSED_SEQUENTIAL_MEDIATOR_TERMINAL.md`;
- clean-ledger addendum `b0563468e593b5080aa5c6650b8a62793ea68b57`.

Verified artifact ZIP SHA256:
- A `c3546d9d8260833c60dc14dad171b1c9e72621b7f67f3401997ca801ecd57d08`;
- B `05e02a2cc84a36745404b952f771c411346ca988a8f19df22cc48c2f1a06f0b3`;
- C `45a24e7ed51af79045d90cf61e91acfbddc3bdaa3b63aec96905d74d16ba014e`;
- D `cb9e3eb013d71125f06fc9da774e124448c14a5f6bcdc0b8525a0212b67a3b7d`;
- aggregate `3a042de0435f945d54f446732562d15cbd042a80cbeb3f36333ecbf9bc927c02`.

All four individual raw lane JSON objects equal their aggregate copies. Green CI was not used as scientific classification.

### CM1 exact result

Use three binary internal source labels and a four-level bus initially in `|0>`. With cyclic bus shift `S`, each source X=A,B,C acts only through the two-body source-bus controlled shift

`V_X = |0><0|_X tensor I_M + |1><1|_X tensor S_M`.

The frozen sequence is

`V_A -> V_B -> V_C -> P_lambda -> V_C^-1 -> V_B^-1 -> V_A^-1`,

with bus-only `P_lambda=diag(1,1,1,exp(i lambda))`.

For every branch `(a,b,c)` and every real symbolic `lambda`, exact computation gives

`U |abc>|0>_M = exp(i lambda a b c) |abc>|0>_M`.

Therefore:
- mediator reset is exact for all eight branches;
- no final which-branch record remains in the mediator;
- no direct A-B/A-C/B-C or primitive three-source gate is used;
- every coordinate lower face `a=0`, `b=0`, `c=0` is exactly identity;
- the connected Boolean third finite difference is `lambda`;
- every constant/one-/two-body phase basis term has connected third finite difference zero;
- omitting any one source interaction kills the connected phase;
- moving the phase gate before the C interaction kills the connected phase;
- putting the phase on bus level 2 contaminates lower two-source faces and is rejected.

The source-bus primitives and bus phase are exactly unitary. If labels/bus are spatial-translation neutral, the operations commute with the inherited G97 total translation generator by tensor-factor separation.

Important qualification: the controlled shifts commute, so reversing only the uncompute order leaves the operation unchanged. Thus CM1 establishes only `FINITE_ORDERED_CIRCUIT_CAUSALITY_ONLY`, not relativistic microcausality or spacetime retardation.

### Scientific interpretation

CM1 strengthens NP1: even a single finite mediator, only two-body source-mediator controls, exact mediator closure, exact lower-face recovery, unitary primitives, finite circuit ordering, and inherited total-translation bookkeeping still leave a continuum of connected phases parametrized by arbitrary `lambda`.

Therefore **existence of a mediator, mediator closure, and circuit-level causal ordering are not sufficient RCG-002 nonlinear selection principles**.

The bus is an adversarial calibration object, not gravity. Its bus-only phase `P_lambda` is exactly the additional unfixed dynamical information; current RCG-002 principles do not derive it.

CM1 does NOT establish a physical source-history map, relativistic locality, energy/nonlinear stress-energy conservation, nonlinear Bianchi/diffeomorphism closure, a physical influence kernel, or a physical completion-space dimension.

## Retained NP1 terminal

NP1 remains authoritative and unchanged:
`RCG002_CURRENT_PRINCIPLES_ALLOW_CONTINUUM_CONNECTED_CHANNEL_EXTENSIONS_SCOPED`, overall `RCG002_REQUIRES_NEW_NONLINEAR_PRINCIPLE`.

NP1 showed that CPTP/positivity, exact lower-face recovery, lower-body phase quotient, G97 total translation, and abstract finite-time evolution leave at least two independent operational directions in its frozen family: connected phase and connected dephasing. That `>=2` lower bound is NOT a physical gravitational completion-space dimension.

Terminal note: `results/RCG002_NP1_CONNECTED_CHANNEL_EXTENSION_TERMINAL.md`; production run `34816931926`.

## Retained NCP1 terminal

NCP1 remains authoritative and unchanged:
- `FAIL_HIGHER_ORDER_ONLY_NOISE_RESCUE_SCOPED`;
- `FAIL_EXACT_GAUSSIAN_CUBIC_LOG_KERNEL_SCOPED`;
- `POSITIVE_NOISY_COMPLETIONS_NONUNIQUE_SCOPED`;
- overall `BLOCKED_PHYSICAL_EVOLUTION`.

Production run `34792497014`; terminal note `results/RCG002_NCP1_NOISY_COMPLETION_TERMINAL.md`.

## Retained G97 prerequisite

`PASS_CLOSED_TOTAL_SOURCE_PREPARATION_CONSERVATION_SCOPED`, run `34791265992`.
G97 closes classical probe+apparatus total-momentum preparation bookkeeping only. It is not nonlinear gravity, energy conservation, or Bianchi closure.

## Physical nonlinear completion space

**Undefined.**

G90/G91 witness coordinates, G92 shell qualifications, NCP1 noise coordinates, NP1 lambda/gamma coordinates, and the CM1 bus `lambda` are not automatically physical gravitational degrees of freedom. No physical field/source/readout equivalence quotient has been derived.

Therefore do not declare a physical dimension or selector rank from these formal coordinates.

## Exact next admissible fundamental gate

**NEW CANDIDATE VERSION PRINCIPLE GATE.**

The current RCG-002 version has reached a genuine model-definition boundary. CM1 removes another structural escape: merely postulating a mediator, demanding pairwise source-mediator couplings, exact mediator reset, or finite ordered-circuit causality cannot fix the connected response.

The next admissible substantive step is exactly one independently motivated candidate-owned physical source/state/evolution principle, frozen before its connected-phase outcome is inspected. A prospective new version must specify in one realization:

1. physical field/state degrees of freedom;
2. source preparation and G97 closed total-source -> physical field/history map;
3. nonlinear evolution equation or influence/state rule;
4. nonlinear conservation and Bianchi/constraint compatibility;
5. spacetime retarded/microcausal structure appropriate to its scope;
6. positive influence kernel or justified coherent/noisy factorization;
7. recovery of the validated pairwise weak-field branch;
8. connected phase/noise observables derived without fitting `lambda`, `gamma`, a mediator phase, or an equivalent free connected coefficient.

Do not run another arbitrary channel scan, mediator variant, ancilla dimension scan, cumulant scan, rank table, or covariance lift as a substitute for this missing physical principle.

If no independently motivated RCG-002 principle can be supplied, terminalize the current version as `RCG002_CURRENT_VERSION_NONLINEAR_DYNAMICS_UNDERDETERMINED`. Any added law must then be labelled a prospectively new candidate version, not a retroactive repair.

## Open layers and locks

Still open: candidate-owned nonlinear dynamics; nonlinear stress-energy/Bianchi/constraint closure; physical source-to-history map; spacetime causality; physical completion quotient; state/measure completion; externally anchored prediction.

Forbidden claims remain `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, established nonlinear RCG-002, universal classical/semiclassical/noisy no-go, family-wide uniqueness, or green-CI-as-physics. Historical G72-G97/CPI1/NCP1/NP1 results and duplicate-G93 quarantine remain intact.
