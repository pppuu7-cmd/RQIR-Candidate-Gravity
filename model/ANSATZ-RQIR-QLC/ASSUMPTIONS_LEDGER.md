# Assumptions Ledger — ANSATZ-RQIR-QLC v0.1

| ID | Assumption | Role | Failure consequence | Status |
|---|---|---|---|---|
| QLC-A01 | A finite relational mode sector can be isolated in the weak-field regime | domain reduction | branch BLOCKED for sectors where no such reduction exists | ACTIVE |
| QLC-A02 | The selected mode algebra is Gaussian/c-number-CCR to the working order | channel closure | non-Gaussian extension required; do not force Gaussian fit | BLOCKED-CERTIFICATE |
| QLC-A03 | Mean transfer `K` is fixed by retarded GR response on the physical quotient | GR limit | failure rejects the realization | ACTIVE |
| QLC-A04 | The interface is CPTP in the declared finite mode sector | quantum consistency | failure rejects v0.1 | ACTIVE |
| QLC-A05 | No excess interface noise exists beyond the minimum required by CP and symmetries | model postulate | empirical excess defines falsification or a new model version | ACTIVE-HYPOTHESIS |
| QLC-A06 | CP-minimizing noise is unique after physical/symplectic normalization, or any residual degeneracy is prediction-equivalent | predictivity | unresolved inequivalent minima block the model | BLOCKED-CERTIFICATE |
| QLC-A07 | Output commutator/noise normalization admits a physical `G -> 0` residual limit | decoupling | failure rejects the physical realization | BLOCKED-CERTIFICATE |
| QLC-A08 | Retarded transfer plus noise does not enable superluminal signalling | causality | failure rejects v0.1 | BLOCKED-CERTIFICATE |
| QLC-A09 | Stress-energy/source modes are renormalized and smeared consistently | operator definition | undefined modes block all claims | BLOCKED-CERTIFICATE |
| QLC-A10 | Comparator performance is not used to choose among inequivalent CP minima | anti-overfit | violation invalidates independence experiment | ACTIVE |

## Rule

`QLC-A05` is the distinctive physical hypothesis. The other assumptions define the domain and consistency requirements needed to test it.
