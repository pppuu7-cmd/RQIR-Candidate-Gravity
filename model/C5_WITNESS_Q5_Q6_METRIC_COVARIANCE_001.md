# C5 Witness Q5/Q6 — Intrinsic vs induced metric covariance and causal response

**Status:** EXPLICIT LINEARIZED STRUCTURAL WITNESS  
**Comparator:** C5 perturbative quantum GR/EFT  
**Purpose:** test Q3, Q5, Q6 and parts of G2/G3/G4/G10 without claiming novelty.

## 1. Linear response setup

Work in a controlled weak-field sector after gauge fixing / projection to a declared physical or relational observable. Write the linearized gravitational equation schematically as

\[
\mathcal L h = \kappa T,
\]

where `L` is the gauge-fixed linearized gravity operator, `T` is the renormalized matter stress tensor projected into the same sector, and `kappa` denotes the gravitational coupling in the chosen convention.

Let `G_R` satisfy

\[
\mathcal L G_R = 1
\]

with retarded boundary conditions. Then

\[
h = h_{\rm hom}+\kappa G_R*T.
\]

This is the causal decomposition into free/intrinsic gravitational data plus the source-induced field.

## 2. Mean field

Taking the expectation value gives

\[
\langle h\rangle
=\langle h_{\rm hom}\rangle
+\kappa G_R*J,
\qquad
J=\langle T\rangle.
\]

Thus the same dynamics that defines the metric response also fixes the mean source map; there is no independently fitted mean-source law.

## 3. Fluctuation decomposition

Define

\[
\delta h=h-\langle h\rangle,
\qquad
\delta T=T-J.
\]

Then

\[
\delta h
=\delta h_{\rm hom}+\kappa G_R*\delta T.
\]

The symmetrized metric covariance is

\[
N_h(x,y)
=\frac12\langle\{\delta h(x),\delta h(y)\}\rangle.
\]

Substitution gives

\[
N_h
=N_h^{\rm intrinsic}
+N_h^{\rm induced}
+N_h^{\rm cross},
\]

with

\[
N_h^{\rm intrinsic}
=\frac12\langle\{\delta h_{\rm hom},\delta h_{\rm hom}\}\rangle,
\]

\[
N_h^{\rm induced}
=\kappa^2\,G_R*N_T*G_R^T,
\]

and

\[
N_T(x,y)
=\frac12\langle\{\delta T(x),\delta T(y)\}\rangle.
\]

`N_h^cross` contains initial graviton-matter correlations. For an initially factorized state in the linearized approximation it vanishes; if the initial state is correlated, it must be retained rather than hidden in an effective noise parameter.

This is an explicit provenance decomposition demanded by Q5.

## 4. Ordered source information and retarded response

Define the stress-tensor commutator object

\[
D_T(x,y)=\frac{1}{2i}\langle[\delta T(x),\delta T(y)]\rangle.
\]

The matter retarded susceptibility is

\[
\chi_T^R(x,y)
=\frac{i}{\hbar}\theta(x^0-y^0)
\langle[T(x),T(y)]\rangle
\]

up to the repository's final sign convention.

In the coupled theory, self-energy/polarization corrections dress the bare gravitational retarded propagator,

\[
G_R\rightarrow G_R^{\rm dressed},
\]

but the causal support remains encoded by the retarded prescription inside the domain in which the EFT is valid.

Thus mean, noise and response arise from one matter+gravity dynamics rather than separate phenomenological choices.

## 5. Causal support

Because `G_R(x,y)=0` outside the allowed causal past of `x` in the chosen relativistic sector,

\[
\delta h_{\rm induced}(x)
=\kappa\int d^4y\,G_R(x,y)\delta T(y)
\]

depends only on causally admissible source support.

The instantaneous-looking Newtonian potential is recovered as the constrained/quasi-static limit of the relativistic field equations and is not used here as a fundamental superluminal process law.

## 6. Higher connected hierarchy

At nonlinear order, the same Schwinger-Keldysh / in-in generating functional produces

\[
J,\quad N_T,\quad D_T,\quad \chi_T^R,\quad
C_T^{(3)},\quad C_T^{(4)},\ldots
\]

and the gravity sector propagates/couples these through the same EFT vertices. RQIR may use these objects to test a specific model, but their existence is not itself a C5 discriminator.

## 7. Renormalization and smearing

`T(x)` is a composite operator. Coincident products must not be treated as finite bare observables. A full implementation must specify a renormalized stress tensor and, for detector-facing quantities, finite spacetime smearing/test functions or an equivalent operational resolution.

The external stochastic-gravity/influence-functional literature provides explicit examples in which the renormalized stress-tensor noise kernel sources induced metric fluctuations while causal dissipation/response is derived from the same closed-time-path structure.

## 8. RQIR gate effect

This construction supplies the required structural witness for:

- Q3: one dynamics generating mean/noise/response hierarchy;
- Q5: explicit intrinsic vs matter-induced geometry covariance with cross-term bookkeeping;
- Q6: retarded causal process kernel;
- G2: conservation/Ward consistency is inherited from the covariant matter-gravity dynamics after proper gauge treatment;
- G4/G4a: causal retarded support is explicit;
- G10/G10a: the need for renormalized/smeared stress-tensor products is explicit.

A full numerical detector certificate remains a separate task and is not needed to establish absence of a foundational contradiction.

## 9. Novelty verdict

The decomposition

\[
\boxed{
N_h=N_h^{\rm intrinsic}
+\kappa^2G_R*N_T*G_R^T
+N_h^{\rm cross}
}
\]

is exactly the kind of structure RQIR requires for provenance, but it is compatible with conventional low-energy quantum gravity/open-system methods.

Therefore Q5/Q6 also fail to provide a C5 obstruction.
