# RQIR-Candidate-Gravity current front

Updated: 2026-09-12
Active iteration: `ITER016`
Phase: `INDEPENDENT_RQIR_DERIVATION / CALIBRATED_MULTICHANNEL_COMPARATOR`

## Canonical status

- Candidate-model/programme readiness: **48%**
- Theory established: **0%**
- Active seed: `RCG-002 Relational controlled-phase channel`
- Independent-from-QGR construction contract: **FROZEN**
- Legacy mixed-project ledger: **NOT SCIENTIFIC AUTHORITY**
- Clean authority ledger: `research_log/RQIRCG_RESEARCH_LEDGER.md`

Readiness is an internal construction metric, not a probability that the model is correct. The increase from 46% to 48% reflects closure of the K=2 positive-control optimizer-calibration subgate only; it does not promote any old adversarial gap to physics evidence.

## Iter013 / G31

Run `34695076098`, head `f32ecf1949f1e7d6c577b201b73c517d4605fdb7`, aggregate artifact `10297704949`, digest `sha256:cfe6a47700e929b4c3c515362db16e2b1618ca64723bfd96dbc38856d9522871`.

Classification: `SCIENTIFIC_CALIBRATION_FAIL / GLOBAL_OPTIMIZER_NOT_VALIDATED`. The positive in-family K=2 recovery control failed (`0.0604612 > 0.002`), so G31 adversarial minima remain diagnostics only.

## Iter014 / G32 and G32-J

G32 run `34695441883`, head `ea54a3ae9694366c3bebe06c13b775af44d46833`, aggregate artifact `10299010209`, digest `sha256:86035287985cc1b1793df8298b919b47067b81aa22b757a5a841df9245389638`.

- oracle replay 4/4 PASS with max gap `0.0`;
- K=2 channel-swap symmetry 4/4 PASS;
- direct trace-distance local/global recovery did not calibrate on all controls.

G32-J run `34695478444`, head `706245fa183845556aa020bc99d2a4d86e4e3060`, aggregate artifact `10298208349`, digest `sha256:e0a48b3cc49ab4ab3514b26de8c47cf2ad7b3e7fb72b7bb5c9e91e262a9490ee`.

- effective Jacobian rank `11/11` on all four K=2 controls;
- max finite-difference discrepancy `1.2393500576443816e-09`;
- max retained-subspace condition number `4033.8739690901716`.

These diagnostics isolated strong conditioning / optimizer-landscape difficulty rather than a basic representability or rank defect.

## Iter015 / G33 terminal result

Authoritative run `34695662002`, head `d15d633f58fa63d378a85d6e5409c4bb0735a97e`, aggregate artifact `10298088690`, digest `sha256:92f1d470f516bd6b85e7d475581762b10ca6871d3ec4c85fc0e73f218f0faa19`.

All 12 lanes were structurally valid. Hidden source coordinates were never optimizer initializers. Scientific acceptance remained the unchanged trace-distance recovery criterion `< 0.002`.

- `sobol_lsq`: **4/4 PASS**, worst trace-distance gap `1.6005292984593422e-12`;
- `lhs_lsq`: **4/4 PASS**, worst trace-distance gap `1.6222740678511114e-12`;
- `de_smooth_lsq`: 3/4 PASS, worst gap `0.012008310266765621`.

Classification: `POSITIVE_CONTROL_METHOD_CALIBRATED_K2`.

Authority methods for the next gate are the two independently calibrated constructions `sobol_lsq` and `lhs_lsq`. The failed `de_smooth_lsq` route is retained as a negative methodology result and is not used for adversarial authority.

Crucially, G33 does **not** retroactively validate G30/G31 gaps. Any RCG-002 adversarial claim must be recomputed prospectively using the calibrated method.

## Active authorized gate — Iter016 / G34

Run three independent scientific fronts in parallel:

1. **K=2 calibrated adversarial rerun:** rerun the four RCG-002 comparator targets with both G33-calibrated methods using the exact K=2 unit-box/smooth-residual/multistart constructions. Interpret only the newly computed G34 results. Require both calibrated methods to retain a nonzero gap and require cross-method agreement within the frozen `0.002` calibration scale before granting scoped K=2 comparator support.
2. **K=3 positive-control calibration:** generate four prospectively fixed in-family K=3 hidden targets and test both Sobol-LSQ and LHS-LSQ extensions. Hidden truth must not be used as an initializer. Scientific calibration still requires trace-distance `<0.002` on all four controls under the same method.
3. **K=4 positive-control calibration:** same discipline for K=4. No K=3/K=4 adversarial interpretation is allowed before its own positive-control calibration passes.

Frozen safeguards:

- final acceptance is always trace distance, even though optimization uses a smooth density-matrix residual;
- old G30/G31 minima cannot be reused as authority;
- no post-result threshold changes;
- K=3/K=4 calibrated-method extension must be fixed before result inspection;
- if K=3/K=4 calibrate, their adversarial RCG-002 reruns occur only in a subsequent gate;
- all conclusions remain restricted to the finite additive independent single-axis Markovian measurement-feedback GKSL comparator family.

## Claim locks

Forbidden:

- `NEW_PHYSICS_FOUND`;
- `FULL_QUANTUM_GRAVITY`;
- `RQIR_REQUIRES_RCG002`;
- claim that all classical/semiclassical mediators are excluded;
- treating green CI as scientific PASS;
- treating G30/G31 historical adversarial gaps as validated by G33;
- changing frozen thresholds after seeing results;
- importing physical assumptions or desired conclusions from QGR/KMQGB/RQIR.

Current correct status:

`RCG002_SCOPED_COHERENT_CANDIDATE + K2_OPTIMIZER_CALIBRATED + G34_CALIBRATED_K2_ADVERSARIAL_AND_K3K4_POSITIVE_CONTROLS_REQUIRED`.