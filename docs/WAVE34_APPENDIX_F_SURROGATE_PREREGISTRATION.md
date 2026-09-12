# Wave 34 — Appendix-F Analytic Surrogate Reconstruction

**Status:** PREREGISTERED BEFORE COMPUTE  
**Classification:** `SURROGATE_NOT_J8`

## Scientific question

How much of the Truncation-4 local/analytic FRG stability information can be reconstructed reproducibly from the printed Appendix-F equations F1–F5, the published closure `lambda5=lambda6=lambda3`, `g5=g6=g4`, and `eta_phi=0`, without silently promoting this lower-quality surrogate to the full momentum-dependent F1 realization?

## Frozen source facts

- coordinate order: `(mu, lambda3, lambda4, g3, g4)`;
- Truncation 4 has `eta_phi_i=0`;
- `g3,g4` are computed by a derivative expansion at `p^2=0`;
- higher-coupling closure is `lambda_{n>4}=lambda3`, `g_{n>4}=g4`;
- rounded Table-3 fixed point: `(-0.23,-0.060,-0.11,0.64,0.55)`;
- published first stability approximation spectrum: `(-3.0,-1.9±1.6i,1.7,3.4)`;
- printed Appendix-F equations are F1–F5;
- the paper explicitly warns that the local projection can introduce large error and uses this system for qualitative behaviour.

## Fail-closed design

Wave 34 does **not** assume that substituting the rounded Table-3 point into very stiff printed equations must produce a small raw residual. The calculation must distinguish:

1. source transcription fidelity;
2. rounding/conditioning sensitivity;
3. existence of a nearby numerical fixed point under the frozen printed equations;
4. stability of numerical differentiation with step size;
5. proximity of any reconstructed eigenspectrum to the published Truncation-4 spectrum;
6. whether the reconstruction is numerically well enough conditioned to serve as a machinery surrogate.

No coefficient may be altered to improve agreement with Table 3 after seeing results.

## Predeclared primary tests

### W34-1 Source/closure gate
Confirm the exact frozen coordinate order, zero anomalous dimensions, higher-coupling identifications, Table-3 values and permanent `SURROGATE_NOT_J8` label.

### W34-2 Printed-flow implementation self-consistency
Evaluate F1–F5 through one shared implementation and verify all outputs remain finite in a predeclared neighbourhood of the rounded Table-3 point. This is a numerical implementation gate, not a physical accuracy claim.

### W34-3 Rounded-point conditioning audit
Quantify flow residuals and the numerical Jacobian singular values at the rounded Table-3 point. Large residuals or condition numbers are retained as results and are not repaired by hand.

### W34-4 Nearby-root reconstruction
Attempt a bounded multi-start solve in a frozen neighbourhood of the rounded point. Record all converged roots and residual norms. PASS semantics: the solver completes deterministically and reports its result; it is **not** required that a root exist or match Table 3.

### W34-5 Step-size stability
For every retained numerical root, compute central-difference Jacobians at a frozen geometric sequence of steps and compare spectra/subspaces. If no root is retained, apply this test to the rounded point and explicitly mark it diagnostic-only.

### W34-6 Published-spectrum comparison
Compare reconstructed eigenvalues to the published `bar` spectrum with an assignment that is permutation/conjugation invariant. Report the mismatch; do not tune the flow to reduce it.

### W34-7 Rounding sensitivity
Sample a deterministic cloud inside the decimal-rounding cell implied by the published two/three-digit fixed-point table and quantify the spread of flow residuals/Jacobians. This tests whether Table-3 rounding alone prevents direct residual validation.

### W34-8 Surrogate firewall
A good spectrum match may only receive `SURROGATE_RECONSTRUCTION_SUPPORTED`; a poor match receives `SURROGATE_RECONSTRUCTION_INCONCLUSIVE`. Neither state changes physical J8.

### W34-9 Information firewall
No polygon/KMQGB-derived QGR inputs are allowed.

## Promotion rule

Wave 34 can improve only the status of the Appendix-F **surrogate computation path**. Physical J8 remains blocked until the full/best-realization same-closure 5x5 stability matrix or normalized right eigenbasis is available.

## Next-step rule

- If reconstruction is stable and matches the published surrogate spectrum reasonably: use it only as a `SURROGATE_NOT_J8` end-to-end trajectory/Jacobian test in Wave 35.
- If reconstruction is ill-conditioned or inconsistent: freeze the discrepancy and move directly to obtaining/recomputing a same-realization orientation object rather than fitting Appendix-F coefficients.
