# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active iteration: `ITER018B`
Phase: `INDEPENDENT_RQIR_DERIVATION / SHARED_CLASSICAL_NOISE_OPTIMIZER_CALIBRATION`

## Canonical status

- Candidate-model/programme readiness: **55%**
- Theory established: **0%**
- Active seed: `RCG-002 Relational controlled-phase channel`
- Independent-from-QGR construction contract: **FROZEN**
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`

Readiness is an internal construction metric, not a probability that the model is correct. The move from 52% to 55% records closure of the prospectively calibrated K=3/K=4 adversarial-comparator rubric item. No readiness is awarded merely for running G36-C.

## Iter017 / G35 terminal result

Authoritative run `34697766107`, head `fbc71768da3cec0d6ea5a8cbb755a29036b16726`, aggregate job `103578278887`, aggregate artifact `10301201162`, digest `sha256:7e07e47311db7a279e2de47502d64a36cf31623c10c0da67f062ee8817bac199`.

All 24 required artifacts were present and structurally valid. Frozen rules were unchanged: nonzero adversarial gap `>1e-4`, cross-method agreement `<=0.002`, nesting slack `0.002`, plus TP/CPTP/PSD/trace admissibility controls.

K=3: all 4 shards passed both calibrated methods, nonzero-gap, cross-method-agreement and nesting gates. Gap pairs by shard were approximately `(0.0260708350,0.0260708246)`, `(0.1046270502,0.1046280224)`, `(0.4030775755,0.4030776193)`, `(0.5324536720,0.5324529975)` for Sobol/LHS. Admissibility 4/4 PASS.

K=4: all 4 shards passed both calibrated methods, nonzero-gap, cross-method-agreement and nesting gates. Gap pairs were approximately `(0.0260708432,0.0260708403)`, `(0.1046282559,0.1046276363)`, `(0.4030776192,0.4030775230)`, `(0.5324520837,0.5324521216)`. Admissibility 4/4 PASS.

Classification: `DERIVED_SCOPED_K3_K4_CALIBRATED_COMPARATOR_SUPPORT`.

Scope ceiling: finite additive independent single-axis Markovian measurement-feedback GKSL comparator family only. This is not a no-go theorem for all classical/semiclassical mediators or quantum-gravity alternatives. Historical G30/G31 minima remain non-authoritative diagnostics.

Durable note: `results/ITER017_G35_CALIBRATED_K3K4_TERMINAL.md` committed at `ad1a6bf689740f3af2997df601a516b3b0a6334c`.

## Parallel methodology robustness — Iter017R / G35-R

Run `34702384573`, head `1b93cbf14b4705ae2699f559523d1c1b1ae28be5`.

Held-out optimizer calibration robustness remains methodology-only and cannot alter the already frozen G35 physics verdict. Latest checked state: 17/18 lanes terminal success; K=3 Sobol shard 0 still in progress; aggregate pending.

## Iter018A / G36-P terminal result

Run `34702575861`, head `270a26300117aeebe23af126dd4e6c53c96cf3f9`, aggregate job `103576905242`, aggregate artifact `10300760790`, digest `sha256:3a03b7462ccf026c6cc7cdef88fbe0c9f4710c3040f467a5caf9fa5e3e4d228d`.

Classification: `CLASSICAL_SHARED_NOISE_IMPLEMENTATION_VALIDATED`.

This validates the implementation/provenance of a shared Gaussian Hamiltonian-noise channel represented as a convex mixture of product unitaries. It is not an RCG-002 adversarial result.

## Active gate — Iter018B / G36-C

Authoritative launch commit `95335aa32e92dcd1cc76762cd6fd3717754a1057`; run `34703606707`.

Purpose: prospectively calibrate the optimizer for the finite shared-classical-noise comparator before any RCG-002 adversarial use.

Frozen rules before result inspection:

- six hidden in-family targets;
- hidden source coordinates are not supplied as optimizer starts;
- independent Sobol-LSQ and Latin-hypercube-LSQ global designs;
- final trace-distance recovery `<0.002` for every method/shard lane;
- all outputs finite/structurally valid;
- no post-result threshold/model tuning.

Twelve scientifically useful lanes are launched (`6 shards × 2 methods`, `fail-fast:false`). PASS only calibrates this finite comparator family and authorizes a separate adversarial RCG-002 test; it does not prejudge that test.

## Claim locks

Forbidden: `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `RQIR_REQUIRES_RCG002`, any claim that all classical/semiclassical mediators are excluded, green-CI-as-science, post-hoc threshold weakening, or importing physical assumptions/results from QGR/KMQGB/RQIR.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + K2_K3_K4_OPTIMIZER_CALIBRATED + K2_K3_K4_SCOPED_CALIBRATED_COMPARATOR_SUPPORT + G35R_HELDOUT_CALIBRATION_RUNNING + G36P_CLASSICAL_SHARED_NOISE_IMPLEMENTATION_VALIDATED + G36C_SHARED_NOISE_OPTIMIZER_CALIBRATION_RUNNING`.
