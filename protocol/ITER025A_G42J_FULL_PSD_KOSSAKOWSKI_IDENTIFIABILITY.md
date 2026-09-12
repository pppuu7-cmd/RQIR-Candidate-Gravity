# ITER025A / G42-J — preregistered full-PSD classical Kossakowski identifiability pre-gate

Purpose: test whether the current finite multi-time/product-probe observable design locally identifies a general real-symmetric positive-definite 6x6 classical random-Hamiltonian Kossakowski matrix before any full-orientation optimizer calibration or RCG-002 adversarial use.

Family/provenance lock:
- local Hermitian basis `G=(X_A,Y_A,Z_A,X_B,Y_B,Z_B)`;
- full real PSD Kossakowski matrix `C = L L^T`, with real lower-triangular Cholesky factor `L`;
- 21 real coordinates: six log-diagonal Cholesky coordinates and fifteen strict-lower-triangular coordinates;
- any real PSD `C` admits `C=sum_k kappa_k v_k v_k^T`, hence the generator is a convex Gaussian white-noise average of local-sum Hamiltonians `F_k=sum_i v_{ki}G_i`; this remains explicit classical shared random-Hamiltonian noise, not arbitrary nonlocal Lindblad noise.

Frozen observable design:
- four deterministic positive-definite hidden controls, seeded independently of RCG-002;
- times `(0.15,0.45,0.9,1.4)`;
- same six product-state probes used in the calibrated finite comparator layers;
- observable vector contains real and imaginary parts of all output density-matrix entries at every time/probe;
- no RCG-002 target is used.

Frozen derivative/rank checks:
- central finite-difference Jacobian with steps `h=1e-6` and `h/2=5e-7` in the 21 Cholesky coordinates;
- effective singular-value rank threshold `s > 1e-7 * s_max`;
- required effective rank `21/21` at both steps;
- retained-subspace condition number must be `<1e7`;
- relative Jacobian two-step difference `||J_h-J_h2||/max(||J_h2||,1e-15) < 5e-5`;
- all diagnostics finite;
- admissibility cross-check at hidden controls: TP residual `<1e-10`, Choi minimum `>-1e-8` at the frozen times.

Interpretation lock:
- PASS (`FULL_LOCAL_RANK_IDENTIFIABILITY_PRE_GATE`) authorizes only a separately preregistered positive-control optimizer calibration for the 21-parameter full-PSD family;
- rank deficiency/ill-conditioning is retained exactly and must be addressed by richer observables or parameterization before optimization; no rank threshold or probe/timing set changes inside this run;
- this gate cannot provide RCG-002 comparator evidence and cannot change programme readiness.
