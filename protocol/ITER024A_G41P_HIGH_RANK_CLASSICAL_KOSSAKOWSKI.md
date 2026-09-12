# ITER024A / G41-P — preregistered high-rank classical Kossakowski implementation pre-gate

Purpose: validate a broader *classical random-Hamiltonian* white-noise comparator ingredient beyond the finite rank-3 G39 layer, before any optimizer calibration or RCG-002 adversarial use.

Family/provenance lock:
- local Hermitian operator basis `G=(X_A,Y_A,Z_A,X_B,Y_B,Z_B)`;
- choose K independent real coefficient vectors `v_k` and positive rates `kappa_k>0`;
- `F_k = sum_i v_{k i} G_i = A_k⊗I + I⊗B_k` is a local-sum Hermitian Hamiltonian;
- generator `L = sum_k kappa_k D[F_k]` with `D[F]rho = F rho F - 1/2{F^2,rho}`;
- equivalently, the 6x6 Kossakowski matrix is `C = sum_k kappa_k v_k v_k^T >= 0`;
- every stochastic Hamiltonian realization is a sum of local Hamiltonians and therefore its unitary factorizes as `U_A⊗U_B`. This is explicit classical shared Gaussian Hamiltonian noise, not arbitrary nonlocal Lindblad noise.

Frozen design:
- Kossakowski ranks K = 4,5,6;
- four deterministic independent shards per rank;
- positive rates are frozen deterministic functions of K and mode index; coefficient frames come from seeded real QR constructions and are not selected against RCG-002;
- no RCG-002 target, comparator distance, or novelty claim is used here.

Frozen checks:
- intended Kossakowski numerical rank equals K using eigenvalue threshold `1e-10`;
- Kossakowski minimum eigenvalue `>-1e-10`;
- trace-preservation residual `<1e-10` on maps at frozen times 0.1, 0.5, 1.0;
- Choi minimum eigenvalue `>-1e-8` at the same times;
- product-unitary factorization error for a deterministic simultaneous Gaussian-mode realization `<1e-12`;
- maximum output negativity from 16 seeded product inputs at t=0.7 `<1e-9`;
- all diagnostics finite.

Interpretation lock:
- PASS validates implementation/provenance only and may authorize a separate positive-control optimizer calibration for a finite high-rank classical family;
- it is not evidence for RCG-002 separation and does not raise programme readiness by itself;
- FAIL is retained exactly; no rates/rank thresholds/admissibility tolerances are changed inside this run.
