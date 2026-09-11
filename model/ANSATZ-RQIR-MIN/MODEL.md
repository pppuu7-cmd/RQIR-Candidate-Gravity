# ANSATZ-RQIR-MIN — RQIR-Minimal Covariant Quantum Interface

**Version:** 0.1  
**Status:** DRAFT / TESTING  
**Origin:** frozen RQIR Core v1.0 + minimum-complexity construction rule  
**Novelty claim:** none at v0.1. The ansatz is deliberately allowed to collapse onto the C5 perturbative-QG/EFT comparator. That collapse is a scientific result, not a failure of the construction exercise.

## 0. Construction principle

This ansatz asks a constrained inverse question:

> What is the least-structured matter–gravity dynamics capable of representing the full frozen RQIR ordered source hierarchy with one coherent dynamics, while preserving relativistic gauge/constraint structure and controlled low-energy limits?

No model-specific information from the separately developed polygon-derived QGR candidate is used.

## 1. Declared domain

The first version is intentionally restricted to a controlled low-energy, weak-field regime on a globally hyperbolic background.

Write

\[
g_{\mu\nu}=\bar g_{\mu\nu}+\kappa\,\hat h_{\mu\nu},
\qquad
\kappa^2=32\pi G,
\]

with `bar g` a declared reference solution/background and `h` a perturbative gravitational degree of freedom.

The ansatz does **not** claim a UV completion and does not extrapolate through singular/Planckian regimes.

## 2. Physical state space — QG-001 target

At the perturbative level the kinematical structure is

\[
\mathcal H_{\rm kin}=\mathcal H_{\rm matter}\otimes\mathcal H_{h},
\]

with the physical sector obtained after imposing the applicable diffeomorphism/gauge constraints (equivalently, in a BRST formulation, by passing to the physical cohomology).

The density operator is defined on the physical algebra/subspace,

\[
\rho_{\rm phys}\ge 0,\qquad {\rm Tr}\,\rho_{\rm phys}=1.
\]

### Matter variables

Quantum fields collectively denoted `psi`, with renormalized stress tensor `T_mn[psi,g]`.

### Gravity variables

Perturbative metric field `h_mn`; gauge-dependent components are not themselves declared observables.

### Observable rule

RQIR-facing observables must be relational/gauge-completed smeared functionals. Gauge-fixed propagators may be used internally for computation, but detector-facing claims must be gauge/relationally meaningful.

### Current limitation

A complete relational construction for every Q1/Q5/Q6 observable is not yet supplied. This is a cross-gate blocker, not permission to treat coordinate components as observables.

## 3. Primary dynamics — QG-002 target

The minimum local generally covariant low-energy action is taken as

\[
S_{\rm MIN}[g,\psi]
=
S_{\rm EH}[g]
+S_{\rm matter}[g,\psi]
+S_{\rm EFT}[g]
+S_{\rm ct}[g,\psi],
\]

where

\[
S_{\rm EH}
=
\frac{2}{\kappa^2}
\int d^4x\sqrt{-g}\,(R-2\Lambda),
\]

and `S_EFT` is the symmetry-allowed low-energy curvature expansion truncated at a declared order, schematically

\[
S_{\rm EFT}
=
\int d^4x\sqrt{-g}
\left(c_1R^2+c_2R_{\mu\nu}R^{\mu\nu}+\cdots\right).
\]

The coefficients are Wilson coefficients of the declared EFT and are **not** free knobs to be tuned to RQIR observables after the fact.

Expanding minimal metric coupling gives the leading interaction

\[
S_{\rm int}
=
-\frac{\kappa}{2}
\int d^4x\sqrt{-\bar g}\,
\hat h_{\mu\nu}\hat T^{\mu\nu}
+O(\kappa^2),
\]

up to the declared metric/sign convention.

This single action, not separately selected detector kernels, is the authority for the model-facing source hierarchy.

## 4. CTP parent object

Use a closed-time-path generating object

\[
Z[J_+,J_-]
=
{\rm Tr}\left(U[J_+]\rho_{\rm phys}U[J_-]^\dagger\right),
\qquad
W=-i\hbar\ln Z.
\]

Functional derivatives in one declared convention generate the ordered matter and gravity correlators required by RQIR.

This is essential: `J`, `N`, `D/chi^R`, higher cumulants, detector covariance and response are projections of the same dynamics, not independently adjustable ingredients.

## 5. RQIR source hierarchy derived from the same dynamics

Define

\[
J_{\mu\nu}(x)=\langle\hat T_{\mu\nu}(x)\rangle,
\]

\[
N_{\mu\nu\rho\sigma}(x,y)
=
\frac12\left\langle
\{\delta\hat T_{\mu\nu}(x),\delta\hat T_{\rho\sigma}(y)\}
\right\rangle,
\]

\[
D_{\mu\nu\rho\sigma}(x,y)
=
\frac{1}{2i}\left\langle
[\delta\hat T_{\mu\nu}(x),\delta\hat T_{\rho\sigma}(y)]
\right\rangle,
\]

and

\[
\chi^R_{\mu\nu\rho\sigma}(x,y)
=
\frac{i}{\hbar}\theta(x^0-y^0)
\langle[\hat T_{\mu\nu}(x),\hat T_{\rho\sigma}(y)]\rangle
\]

with the final sign convention frozen before numerical work.

All local composite operators require explicit renormalization and/or spacetime smearing before detector-facing use.

## 6. Gravity response skeleton

At leading perturbative order, the metric response has the schematic operator solution

\[
\hat h
=
\hat h_{\rm hom}
+\frac{\kappa}{2}\,G_R\!\ast\!\hat T
+O(\kappa^2),
\]

where `G_R` is the appropriate retarded graviton Green object after constraint/gauge treatment.

Therefore the same dynamics gives, schematically,

\[
\langle\hat h\rangle
=
\langle\hat h_{\rm hom}\rangle
+\frac{\kappa}{2}G_R\!\ast\!J+\cdots,
\]

while connected metric covariance contains both an intrinsic/homogeneous gravity contribution and a sourced matter contribution,

\[
C_{hh}
=
C_{hh}^{\rm intrinsic}
+
\frac{\kappa^2}{4}
G_R\!\ast\!N\!\ast\!G_A
+\cdots.
\]

Ordered/retarded response is likewise constrained by the same propagator and source commutator structure.

The exact tensor projectors, gauge completion, counterterms and coefficients are derivation tasks; the important v0.1 rule is that the mean/noise/response sectors are not independently fitted.

## 7. Why this is the minimum RQIR-compatible root

The frozen RQIR hierarchy requires a candidate capable, in principle, of carrying more information than a mean source alone. The minimum branch selected here is therefore a dynamical quantum matter + gravitational mediator construction with:

- one coherent state space;
- one covariant dynamics;
- ordered quantum source information;
- causal retarded propagation;
- intrinsic and source-induced gravitational correlation sectors;
- a route to channel/process observables.

No extra scalar, vector, preferred frame, arbitrary memory kernel, collapse parameter, stochastic field, or nonlinear state-dependent source rule is introduced at v0.1 because RQIR itself has not yet forced such an addition.

## 8. Required limits

The ansatz must satisfy, within its declared domain:

### Gravity-off

\[
G\to0\quad\Rightarrow\quad
\mathcal H_{\rm matter}\text{ evolves as ordinary QFT/QM on the declared background.}
\]

### Classical/semiclassical coarse limit

Appropriate states/coarse graining must recover classical GR or the controlled semiclassical source equation at the level where fluctuations/commutators are operationally unresolved.

### Flat-space limit

\[
\bar g_{\mu\nu}\to\eta_{\mu\nu}
\]

must recover the declared flat-QFT + perturbative graviton limit.

### Newtonian weak-field limit

The static nonrelativistic sector must recover the Poisson/Newton potential with the correct coupling normalization.

### EFT limit

Predictions are only claimed at energies/curvatures where omitted operators are parametrically controlled.

## 9. Gauge, conservation and causality obligations

General covariance supplies the structural origin of Bianchi/Ward consistency, but explicit perturbative checks are still required for the truncated calculation.

The source must satisfy the applicable renormalized conservation law,

\[
\nabla_\mu\langle\hat T^{\mu\nu}\rangle=0,
\]

with the corresponding Ward identities for correlators.

Retarded response must have support compatible with the declared causal structure.

## 10. Comparator expectation before calculation

No novelty is claimed merely from quantizing `h_mn`.

The v0.1 expectation is:

- C0 classical GR: potentially distinct in fluctuation/quantum-information sectors;
- C1 semiclassical mean gravity: potentially distinct beyond `J`;
- C2 stochastic gravity: distinction is not assumed; requires ordered/response/channel audit;
- C3 hybrid/classical channel: distinction is not assumed;
- C4 ordinary quantum mediators: apparatus-specific nuisance audit required;
- C5 perturbative quantum gravity / low-energy quantum GR: **likely degenerate by construction at v0.1**;
- C6 full-QFT source + classical interface: distinction requires demonstrating gravity-side quantum information beyond source statistics.

If the C5 audit confirms exact/controlled degeneracy, `ANSATZ-RQIR-MIN` is retained as the root/control solution and is **not** advertised as a new theory.

## 11. First model-specific discriminator — intentionally not yet claimed

RQIR requires the discriminator to be derived only after foundational dynamics are frozen. Therefore QG-007 remains `BLOCKED/NOT_TESTED` in v0.1.

The next task is not to invent a signal. It is to propagate the frozen dynamics through Q1–Q7 and C0–C6 and identify the first surviving residual, if any.

## 12. Falsification / rejection conditions

Reject this model version if any mandatory condition fails within the domain it claims:

- inconsistent gauge/constraint structure;
- violation of Ward/Bianchi/conservation requirements;
- nonunitary or nonpositive probability structure not explained by a controlled open-system reduction;
- acausal retarded support;
- failure of Newtonian/GR/flat-QFT limits;
- uncontrolled EFT expansion;
- undefined renormalized/smeared RQIR observables;
- detector-facing claims that depend on coordinate/gauge artifacts.

Exact degeneracy with C5 is **not** a consistency rejection; it is a novelty rejection.

## 13. Immediate derivation targets

1. Freeze conventions and derive the linearized constraint/projector structure.
2. Derive the Newtonian limit and coupling normalization.
3. Derive the CTP map from the action to `J,N,D,chi^R`.
4. Split intrinsic gravity covariance from matter-sourced covariance without double counting.
5. Construct at least one relational Q1/Q5 observable.
6. Run the C5 degeneracy audit before proposing any new term.
7. Only if a frozen RQIR requirement remains structurally unrepresented should a v0.2 deformation be introduced.
