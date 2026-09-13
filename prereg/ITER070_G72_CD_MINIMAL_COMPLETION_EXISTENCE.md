# Iter070 / G72 — C/D minimal completion existence tests

Status: PREREGISTERED BEFORE IMPLEMENTATION
Date: 2026-09-13

## Purpose
G71 narrowed the architecture Pareto set to C (Gaussian CTP) and D (non-Gaussian cubic CTP) but left orthogonal blockers. G72 does **not** select either architecture. It asks whether explicit minimal mathematical completions exist that close each blocked property without changing the already-frozen supported properties.

Every extra object introduced here is labeled HYPOTHESIS/CONSTRUCTION, not DERIVED RCG-002 physics.

## Frozen independent streams
### C1 — covariant transverse embedding existence
Construct a frozen linear response kernel
`K_C(k) = P_T(k) * d_R(k)`
where `P_T=P2+P0` is the exact conserved symmetric-source projector used in the G65 geometry and `d_R(k)` is a scalar retarded factor. Test exact Ward annihilation for frozen non-null momenta and held-out symmetric sources. Negative control removes the transverse projector and must fail Ward annihilation for at least one source.

### C2 — pole inventory under a frozen pole-free scalar factor
Use the prospective hypothesis `d_R(z)=exp(-ell2*z)` with exact `ell2>0` symbols/rationals only as a construction witness. Test exact nonzero/zero-set facts establishing no finite zeros of the multiplicative entire factor. Do not infer a full causal propagator or quantum gravity model. Deliberately polynomial control `1+a z` must exhibit a finite zero for nonzero a.

### D1 — retarded cubic support existence
Construct a finite discrete-time cubic CTP kernel with support only when the response/Delta time is not earlier than both Sigma times: `t_Delta >= max(t_Sigma1,t_Sigma2)`, symmetric under interchange of the two Sigma legs. Test exact support, Sigma-leg permutation symmetry, and CTP normalization `Gamma3[Delta=0]=0`. Negative control includes one advanced-support entry and must be detected.

### D2 — compatibility with G71 Hessian result
For the D1 retarded-support cubic functional, recompute the exact Hessian at zero/background and require it to vanish, while a deliberately quadratic retarded control has nonzero Hessian. This verifies that adding the causal support construction does not silently alter the G71 no-new-linear-poles conclusion.

## Frozen interpretation
A lane PASS proves only existence of the specified minimal mathematical completion witness. It does not prove uniqueness, physical correctness, nonlinear general covariance, unitarity, measure closure or empirical validity.

If C1+C2 pass: allowed statement `C_MINIMAL_WARD_POLEFREE_COMPLETION_EXISTS_SCOPED`.
If D1+D2 pass: allowed statement `D_MINIMAL_RETARDED_CUBIC_COMPLETION_EXISTS_SCOPED`.
If both pass: aggregate classification `CD_ORTHOGONAL_MINIMAL_COMPLETIONS_EXIST_NO_UNIQUE_SELECTION_SCOPED`.
If exactly one passes scientifically while controls are valid: report the corresponding one-sided result without post-hoc repair.
Technical invalidity/control failure is INFRASTRUCTURE_OR_GATE_INVALID, not scientific FAIL.

## Claim locks
No candidate architecture selection; no NEW_PHYSICS_FOUND; no FULL_QUANTUM_GRAVITY; no ghost/unitarity theorem; no readiness increase from existence witnesses alone. Programme readiness stays 66%; theory established stays 0%.
