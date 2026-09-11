# Post-Freeze Parallel Uniqueness Campaign v1

This compute campaign is deliberately separated from the frozen `rqir-derived-model-v0` reconstruction.

It tests four candidate closure ideas as **uniqueness problems** rather than fitting a new theory:

1. `channel_polytope.py` — whether CPTP + axial symmetry + a fixed low-order transfer selects a unique quantum channel;
2. `spectral_moment_problem.py` — whether positivity plus finitely many low-energy spectral moments selects a unique positive spectral measure on a finite proxy grid;
3. `cumulant_hierarchy.py` — whether positivity + symmetry + fixed L1-L3 moments fixes L4, and whether fixing L4 then fixes L6;
4. `crossing_eft_basis.py` — how much crossing-symmetric EFT polynomial freedom remains after fixing the leading low-energy term, including directions invisible in the forward limit.

These are controlled finite proxies, not proofs of quantum gravity. A negative uniqueness result strengthens the RQIR underdetermination diagnosis; a positive/near-unique result would identify a structure worth promoting to a deeper gravity-specific derivation.

The GitHub Actions workflow runs the four streams in parallel and then aggregates machine-readable artifacts.