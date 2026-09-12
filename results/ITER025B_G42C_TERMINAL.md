# Iter025B / G42-C terminal result

- Run: `34710744967`
- Head: `7ebc18df416b62784e85ce6090ba6e8836619d92`
- Aggregate job: `103599128599`
- Summary artifact: `10302903611`
- Digest: `sha256:daa9c9f1ac0bf70094fd47783c7b0dece89243593348befff801054f799e258a`
- Workflow classification: `FULL_PSD_OPTIMIZER_CALIBRATED`

All eight positive-control lanes passed the frozen recovery rule. Sobol worst recovery gap was `2.7772340303898642e-14`; LHS worst recovery gap was `1.0453541579862152e-15`; minimum recovered Kossakowski eigenvalue was `0.040841395415346496`.

## Scientific scope correction / ceiling

The workflow label is retained for provenance, but the actual frozen coordinates used log-Cholesky diagonals bounded in `[-2.0,-0.5]`. Therefore every candidate in this run is strictly positive definite: this calibrates the **interior bounded SPD subfamily**, not the rank-deficient PSD boundary. It cannot by itself authorize a claim about the entire PSD cone or an arbitrary-rank full-PSD adversarial gate.

A separate boundary-capable calibration using direct nonnegative Cholesky diagonals and explicit lower-rank hidden controls is required before any broader arbitrary-orientation PSD adversarial test. No readiness increase follows from this calibration alone.
