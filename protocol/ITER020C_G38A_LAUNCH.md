# Iter020C / G38-A preregistration and launch

Frozen before result inspection on 2026-09-12.

Prerequisite: terminal G38-C positive-control trajectory calibration PASS (`34704210632`), with all 12 hidden in-family three-time controls recovered under frozen `max_t trace distance < 0.002`.

Scientific question: can the exact calibrated OU colored-classical-noise trajectory family reproduce the four prospectively fixed RCG-002 toy trajectories?

Frozen target convention: for each base RCG-002 shard angle `theta`, use the existing controlled-phase toy target at three times as `target(theta*T)` for `T=[0.25,0.5,1.0]`. This is explicitly only linear scaling of the toy-channel phase parameter with toy evolution time and is not asserted to be the full continuum gravity-time dynamics.

Frozen optimizer: exact G38-C OU trajectory Sobol-LSQ/LHS-LSQ construction, parameter bounds, start counts and bounded least-squares refinement; no post-calibration retuning.

Frozen acceptance per shard:
- both calibrated methods must retain `max_T trace_distance > 1e-4`;
- the per-time trace-distance vectors from Sobol/LHS must agree to `<=0.002` componentwise;
- their maximum trajectory gaps must agree to `<=0.002`;
- all eight lanes must be finite and structurally valid.

Scope ceiling: stationary OU finite-correlation scalar classical noise with one fixed local-sum coupling, evaluated on this three-time toy trajectory. PASS is not a no-go theorem for all non-Markovian, classical, or semiclassical mediators and cannot establish full quantum gravity or new physics by itself.