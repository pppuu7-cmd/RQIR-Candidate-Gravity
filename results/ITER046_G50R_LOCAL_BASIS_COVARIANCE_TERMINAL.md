# ITER046 / G50-R — terminal local-basis covariance result

Status: **PASS under the prospectively frozen G50-R rule**.

## Provenance

- preregistration: `0ee31e39dacb0e2fb145fbe57345209f0c2ef878`
- implementation: `9965fb9631d62715acf2f713d3ef44f4a301512f`
- technical import-path correction: `5124907bb363f808c1c887c12f457fd46759292c`
- workflow: `dc9a5cdbb300c767d2002c300de39f37c517705b`
- launch/head: `1e0d0e669089b144be24399032330c4690f37a8b`
- run: `34739265637`
- aggregate job: `103676188542`
- summary artifact: `10312356700`
- summary digest: `sha256:34b9bee037a9fc28d664d4b5bc303e51c2478e3ee302206d801040a7fcbf3e34`

## Frozen aggregate

All 16/16 lanes are structurally valid and the frozen scientific-support rule is met.

- worst train/held-out gap-invariance delta: `2.1094237467877974e-15` (threshold `1e-9`)
- worst direct-vs-superoperator implementation discrepancy: `1.6378558132172463e-15` (threshold `1e-10`)
- worst trace residual: `4.885050610554785e-15` (threshold `1e-10`)
- minimum output-state eigenvalue: `-5.023393988398949e-16` (floor `-1e-10`)

Classification:

`DERIVED_SCOPED_G50A_LOCAL_BASIS_COVARIANT_SUPPORT`

## Scope lock

This result establishes only local-unitary basis covariance of the exact terminal G50-A finite-panel separation under the frozen deterministic rotation panel. It does **not** expand the comparator family, establish an all-classical no-go theorem, or establish a gravity theory.

This is a robustness qualification. Programme readiness remains **64%** and theory established remains **0%**.
