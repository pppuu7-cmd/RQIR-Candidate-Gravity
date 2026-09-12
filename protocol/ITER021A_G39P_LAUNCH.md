# Iter021A / G39-P preregistration and launch

Frozen before result inspection on 2026-09-12.

Purpose: validate the next broader classical comparator ingredient without using RCG-002. The finite family is `L = sum_k kappa_k D[F_k]` with rank `K=2` or `K=3`, positive rates, and `F_k=cA_k A_k⊗I+cB_k I⊗B_k` for local Pauli-axis observables. Distinct local axes are prospectively forced to include a noncommuting pair, so this is not merely the one-axis G36 channel duplicated.

Physical scope: each mode is classical Hamiltonian white noise. On every stochastic trajectory the Hamiltonian remains `H_A(t)⊗I + I⊗H_B(t)`, hence the trajectory factorizes into local unitaries even when local axes at different times/modes do not commute. The averaged channel is therefore a correlated local-random-unitary classical channel.

Frozen 12-lane checks: TP `<1e-10`; Choi minimum eigenvalue `>-1e-8`; outputs from 10 prospectively sampled product inputs PSD above `-1e-8`, trace error `<1e-10`, negativity `<1e-10`; mode-order generator invariance `<1e-12`; exact single-mode reduction `<1e-12`; first two local-A axes must have commutator norm `>1e-2`.

This is implementation/admissibility validation only. PASS authorizes a separate optimizer-calibration gate before any RCG-002 adversarial search. It is a finite low-rank positive-Kossakowski decomposition, not the most general classical or semiclassical mediator.