# ITER022B / G40-C — strict-BLP RTN optimizer calibration

Authorized only after terminal G40-P scientific PASS.

This gate does not use RCG-002. It calibrates a finite hidden-classical RTN comparator family with arbitrary local Pauli axes under two independent start constructions.

Frozen before results:
- family parameters: `r, nu, cA, cB, thetaA, phiA, thetaB, phiB`, with `gamma=r*nu*cA` and fixed prospective bounds in the code;
- all hidden controls are generated independently and are never inserted into optimizer starts;
- fixed trajectory times `[0.35,0.80,1.60,3.00]` and six fixed product-state probes;
- Sobol and LHS each use 16 starts; top 4 smooth-residual starts receive bounded least-squares refinement; max_nfev=600;
- scientific recovery metric is maximum trace distance over every frozen probe/time, required `<0.002`;
- each recovered control must independently retain BLP total positive trace-distance increment `>0.02` on the same frozen 241-point witness grid used by G40-P;
- both methods must recover all four controls;
- no result-dependent threshold, bounds, probe, time-grid or family changes.

PASS authorizes only a separate prospective RCG-002 adversarial trajectory gate using the same calibrated family/methods. It is not evidence of novelty, new physics, or a no-go theorem.
