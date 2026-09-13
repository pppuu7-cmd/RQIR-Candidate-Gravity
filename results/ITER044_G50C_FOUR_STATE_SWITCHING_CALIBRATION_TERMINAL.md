# Iter044 / G50-C — Four-state switching calibration terminal

## Terminal classification
`FOUR_STATE_CLASSICAL_SWITCHING_OPTIMIZER_CALIBRATED`

## Authority
- Preregistration: `0de6cd29346ce68888c68ed1965ea0c7af224fb8`
- Implementation: `1eed19071661ec143bf6e3feb350374031dab557`
- Workflow: `a48d0386277de272ffa3b564c3c3d0674ef68492`
- Authoritative head: `4528497f9b34add2bff84bc55db399673ca07c8f`
- Run: `34734256210`
- Aggregate job: `103662830407`
- Summary artifact: `10310302963`
- Summary digest: `sha256:c600d52b399ca493b537b65507696dda6193be17a3f155f78cbcc85ca8573bba`

## Frozen gate
Response-blind calibration only for the terminally qualified finite 20D four-state stationary hidden-classical CTMC switching family. Matrix: Sobol/LHS x four deterministic hidden in-family controls; 32 starts/lane; 6 refinements; 800 max evaluations. Frozen thresholds: train max trace gap `<0.002`, held-out-time max trace gap `<0.003`, normalized parameter error `<0.10`, physical provenance, and Sobol/LHS train-gap agreement `<=0.002` per control.

## Raw artifact consumption
All 8/8 raw lane artifacts were consumed and are structurally valid with `scientific_support=true`.

Across all raw lanes:
- worst train max trace gap: `6.1950671201431e-12`
- worst held-out max trace gap: `4.109242107956982e-12`
- worst normalized parameter error: `1.7639089906452824e-10`
- worst TP residual: `1.776516304761236e-15`
- minimum Choi eigenvalue: `5.956647395842122e-11`

Sobol/LHS train-gap differences by controls 0..3:
- `3.5660541684399162e-12`
- `7.034200708641959e-13`
- `2.5531430413522786e-12`
- `1.386020869958981e-13`

All are far below the frozen cross-method tolerance `0.002`.

## Scientific interpretation
This is a strong positive optimizer calibration result: the prescribed search recovers hidden members of the exact 20D family on both training and prospectively held-out times, while preserving the family provenance/physicality checks. It therefore authorizes a separately prospectively preregistered RCG-002 adversarial transport against this exact family.

It is **not** evidence that RCG-002 is separated from this family, and it is not a no-go theorem for arbitrary classical memory, semiclassical gravity, or any other comparator class.

## Scope / claim locks
`NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, all-classical/all-semiclassical no-go claims, and any imported QGR/KMQGB/RQIR physical premise remain forbidden. `THEORY_ESTABLISHED = 0%`.
