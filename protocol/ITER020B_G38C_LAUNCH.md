# Iter020B / G38-C preregistration and launch

Frozen before result inspection on 2026-09-12.

Prerequisite: G38-P terminal implementation/provenance PASS. At a single final time the OU channel depends on colored-noise parameters only through integrated phase variance and is therefore equivalent to the already tested shared Gaussian phase-noise family. To add nonredundant information, G38-C is explicitly a three-time trajectory calibration at `T = [0.25, 0.5, 1.0]`.

Family: stationary OU scalar classical noise `C(t,s)=sigma2 exp(-|t-s|/tau)` coupled through one fixed `F=cA A⊗I+cB I⊗B`. The exact state at each observation time uses `v(T)=2 sigma2 tau [T-tau(1-exp(-T/tau))]`.

Frozen positive controls: six hidden in-family trajectories, including four interior controls plus prospectively fixed short- and long-correlation controls. Hidden coordinates are never optimizer starts. Two independent designs, Sobol-LSQ and Latin-hypercube-LSQ, use the same frozen bounds and bounded least-squares refinement.

Scientific PASS requires maximum per-time trace-distance recovery `<0.002` for all 12 method/control lanes. No thresholds or family definitions may change after inspection.

PASS authorizes only a separate multi-time RCG-002 adversarial trajectory gate. It does not itself establish non-Markovianity in the information-backflow sense or any general classical/semiclassical no-go.