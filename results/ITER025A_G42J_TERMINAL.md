# Iter025A / G42-J terminal result

- Run: `34710643103`
- Head: `ec3d1a5e407d149ebf39d44968bf1bf1085db8d7`
- Aggregate job: `103598755854`
- Summary artifact: `10303316491`
- Digest: `sha256:07a895f0fb309a6e642cd6eb5429e368ddcad0c78367571cfa59b7c7bce8ea9e`
- Classification: `FULL_LOCAL_RANK_IDENTIFIABILITY_PRE_GATE`

All four prospectively frozen full-PSD hidden controls passed. The 768x21 trajectory Jacobian had effective rank `21/21` at both central-difference steps for every control. Worst retained condition number was only `5.905925058022569`; maximum relative two-step Jacobian difference was `1.2624740304766223e-09`. Maximum TP residual was `4.003929019533592e-16`; minimum Choi eigenvalue was positive (`0.0002842406118803434`).

Interpretation: the frozen four-time/six-product-probe observable design is locally full-rank and well-conditioned for the full 21-parameter Cholesky representation of a real-PSD 6x6 classical random-Hamiltonian Kossakowski matrix at these controls. This is an identifiability/admissibility pre-gate only: no RCG-002 target, no comparator evidence, no readiness increase. It authorizes a separately preregistered positive-control optimizer calibration.
