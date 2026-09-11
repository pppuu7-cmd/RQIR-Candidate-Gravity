# Assumptions Ledger — ANSATZ-RQIR-MIN v0.1

| ID | Assumption | Type | Why currently used | Removal / falsification test | Status |
|---|---|---|---|---|---|
| A01 | Four-dimensional Lorentzian spacetime in the working regime | domain | matches the RQIR low-energy GR/QFT baseline | generalize dimension/signature only if a frozen requirement forces it | ACTIVE |
| A02 | Globally hyperbolic reference background for the first CTP/retarded construction | technical/domain | permits a clean initial-value and causal Green-function formulation | test curved backgrounds and boundary dependence later | ACTIVE |
| A03 | Metric perturbation is the only gravitational mediator introduced at v0.1 | minimality | avoids adding unforced degrees of freedom | relax only after a documented RQIR obstruction/residual | ACTIVE |
| A04 | General covariance/diffeomorphism symmetry is retained | structural | required by GR limit and RQIR gauge discipline | failure rejects the ansatz rather than being tuned away | ACTIVE |
| A05 | Matter couples minimally to the metric at leading order | minimality/EP | least-structured universal coupling | compare against allowed nonminimal EFT operators at higher order | ACTIVE |
| A06 | Low-energy EFT expansion is valid in the claimed domain | approximation | model explicitly disclaims UV completion | quantify expansion parameter before numerical claims | OPEN-CERTIFICATE |
| A07 | CTP formalism faithfully represents ordered response/noise in the working regime | representation | matches frozen RQIR hierarchy | derive equivalent operator/channel description as a cross-check | ACTIVE |
| A08 | No detector-facing kernel is fundamental independently of the action | anti-overfit | frozen RQIR single-dynamics rule | any exception defines a new model version | ACTIVE |
| A09 | Renormalized/smeared stress-tensor products exist for chosen test sectors | technical | needed for `N,D,chiR` | explicit regulator/smearing calculation required | BLOCKED |
| A10 | Relational/gauge-completed Q1/Q5/Q6 observables can be constructed in-domain | technical/physical | coordinate components alone are not acceptable | explicit constructions required | BLOCKED |

## Rule

An assumption may not be silently promoted to a derived result. Removing an ACTIVE foundational assumption in a way that changes the dynamics creates a new ansatz version/branch.
