# C5 Witness G10 — Renormalized and smeared source hierarchy

**Status:** EXPLICIT CONVENTION / STRUCTURAL WITNESS  
**Comparator:** C5 perturbative quantum GR/EFT  
**Purpose:** close the RQIR requirement that stress-energy products entering mean/noise/response/higher objects are not treated as unsmeared bare coincident operators.

## 1. Renormalized stress tensor

Let

\[
T^{\rm ren}_{\mu\nu}(x)
\]

be the renormalized stress-energy operator in the declared QFT/EFT scheme. The precise counterterm basis and subtraction prescription are part of the model convention and must be kept fixed across all ordered objects.

For curved-spacetime implementations, acceptable realizations include covariant point-splitting/Hadamard subtraction plus the required local geometric counterterms, or an equivalent EFT renormalization prescription.

## 2. Operational smearing

For any smooth compactly supported tensor test function `f^{mu nu}(x)`, define

\[
T[f]
=\int d^4x\,\sqrt{-g}\,f^{\mu\nu}(x)T^{\rm ren}_{\mu\nu}(x).
\]

Detector-facing observables use finite spacetime support/resolution through such test functions or an explicitly equivalent response kernel. This avoids treating coincident composite-operator products as ordinary finite numbers.

## 3. One-convention source hierarchy

Define

\[
J[f]=\langle T[f]\rangle,
\]

\[
\delta T[f]=T[f]-J[f],
\]

\[
N[f,g]
=\frac12\langle\{\delta T[f],\delta T[g]\}\rangle,
\]

\[
D[f,g]
=\frac{1}{2i}\langle[\delta T[f],\delta T[g]]\rangle,
\]

and

\[
\chi^R[f,g]
=\frac{i}{\hbar}\,\theta_{fg}\,
\langle[T[f],T[g]]\rangle
\]

with the precise causal ordering functional `theta_fg` replaced by the unsmeared retarded distribution before smearing in an explicit spacetime calculation.

Higher connected objects are defined by the same renormalized generating functional and then smeared with the chosen detector/test functions.

## 4. Consistency rule

The renormalization scheme may shift local contact terms and EFT Wilson coefficients, but it may not be changed independently between `J`, `N`, `D`, `chi^R` and higher connected functions to manufacture a discriminator.

Any scheme dependence must cancel from a properly defined observable after the EFT coefficients and measurement map are transformed consistently.

## 5. Conservation / Ward condition

The chosen renormalization prescription must respect the relevant covariant conservation/Ward identities, modulo declared anomalies where physically applicable:

\[
\nabla^\mu T^{\rm ren}_{\mu\nu}=0
\]

inside the anomaly-free sector used for the witness construction.

Smearing then gives the corresponding integrated identities after boundary terms are controlled by the test-function support.

## 6. Relation to metric fluctuations

The matter-induced metric covariance in

`C5_WITNESS_Q5_Q6_METRIC_COVARIANCE_001.md`

is understood distributionally as

\[
N_h^{\rm induced}[F,G]
=\kappa^2\,N_T[G_R^TF,G_R^TG],
\]

where `F,G` are finite detector/geometry test functions and the retarded Green map transfers them to admissible source smearings.

This makes the provenance formula finite at the operational level without introducing a new stochastic law.

## 7. Gate effect

This file supplies an explicit C5-compatible convention for G10/G10a:

- renormalized composite stress tensor;
- common scheme across the full ordered hierarchy;
- finite smearing/response functions;
- covariant conservation/Ward requirement;
- no independent tuning of contact terms between orders.

No C5 obstruction appears.
