# RQIR → Candidate Gravity Requirements Matrix

Authority: frozen **RQIR Core v1.0** (freeze 2026-09-09), pinned in `docs/RQIR_V1_AUTHORITY_SNAPSHOT.md`.

The purpose of this matrix is not to fit a model to named benchmark outcomes. It converts frozen RQIR semantics into construction constraints before a concrete ansatz is promoted.

## A. Observable-channel requirements

| ID | Frozen RQIR channel | Construction translation | Required model output | Use | Status |
|---|---|---|---|---|---|
| Q1 | Quantum clocks / proper time | Model must define relational timing/phase observables when matter paths or internal clocks are quantum controlled. | Gauge/relational clock observable and controlled weak-field limit. | validation-facing | OPEN |
| Q2 | Superposed sources | Source preparations may be coherent superpositions; the gravitational map may not silently replace the state by a classical mixture unless that follows from the dynamics. | State-preparation map and gravitational response to coherent sources. | design | ACTIVE |
| Q3 | Backreaction / source rule | The source rule must be derived, not chosen separately for mean, noise and response. | One dynamics generating `J`, `N`, `D/chi^R` and any higher objects. | design | ACTIVE |
| Q4 | Gravity-mediated quantum information | If the candidate claims quantum mediation, it must generate a channel-level prediction, not merely an entanglement slogan. | Reduced channel/process observable and comparator audit. | holdout-heavy | OPEN |
| Q5 | Geometry fluctuations | Intrinsic gravitational fluctuations must be separable from matter-induced and technical noise at the level of predicted covariance/correlators. | Metric/curvature correlation functions with provenance. | design | ACTIVE |
| Q6 | Causal/process structure | Retarded response and any nonclassical causal claim require explicit causal support. | Retarded kernel/process object; no-signalling or declared causal analogue. | holdout-heavy | OPEN |
| Q7 | Low-energy QG EFT | Candidate must possess a controlled low-energy regime and state whether it reduces to or departs from perturbative quantum GR/EFT. | Power counting, cutoff/domain and C5 comparator map. | design + validation | ACTIVE |

## B. Ordered source hierarchy

The candidate must derive, in one convention,

\[
J_{\mu\nu}(x)=\langle \hat T_{\mu\nu}(x)\rangle,
\]

\[
N_{\mu\nu\rho\sigma}(x,y)=\frac12\langle\{\delta\hat T_{\mu\nu}(x),\delta\hat T_{\rho\sigma}(y)\}\rangle,
\]

\[
D_{\mu\nu\rho\sigma}(x,y)=\frac{1}{2i}\langle[\delta\hat T_{\mu\nu}(x),\delta\hat T_{\rho\sigma}(y)]\rangle,
\]

and a retarded response `chi^R` with declared sign convention. Higher connected objects are required at whatever order the model claims.

**Constraint:** these objects may not be independently tuned to manufacture a discriminator.

## C. Frozen consistency gates translated into construction constraints

| RQIR gate | Construction constraint |
|---|---|
| G0 | Every term and coupling has explicit dimensions. |
| G1 | Claimed observables are relational/gauge invariant or supplied with a gauge-completion argument. |
| G2 | Matter-gravity dynamics is compatible with conservation/Bianchi/Ward identities. |
| G3/G3a/G3b | Closed dynamics is unitary, or open dynamics is positive/CP as appropriate; covariance/spectral identities are valid. |
| G4/G4a | Retarded objects have causal support compatible with the declared spacetime/process structure. |
| G5 | Controlled `hbar -> 0` limit is stated. |
| G6 | Controlled `G -> 0` decoupling limit is stated. |
| G7 | Flat-spacetime limit is stated. |
| G8 | Newtonian/weak-field limit is derived in-domain. |
| G9 | EFT/power-counting domain is explicit. |
| G10/G10a | Stress-energy products are smeared/renormalized with an explicit prescription. |
| G11 | Known precision-test regime must not be contradicted without a declared excluded domain. |
| G12/G12a | Classical, stochastic, hybrid and full-QFT-source degeneracies are audited. |
| G13 | Detector-facing observability/estimability must eventually be supplied. |

## D. Candidate-gravity gates

Construction proceeds in the frozen order:

`QG-001 state space -> QG-002 dynamics -> QG-003..006 consistency/limits -> QG-007 discriminator -> QG-008 finite propagation -> QG-009 nuisance-profiled identifiability -> QG-010 resources`.

No detector-level advantage is allowed to feed backward into the choice of foundational dynamics during v0 construction.

## E. Comparator requirements

Every claimed novelty is bounded by the weakest unresolved comparator:

- C0 classical GR/Newtonian;
- C1 semiclassical gravity;
- C2 stochastic gravity;
- C3 classical-channel/hybrid/postquantum gravity;
- C4 ordinary quantum/technical mediators;
- C5 perturbative quantum gravity / low-energy quantum GR;
- C6 full-QFT source + classical interface.

## F. Minimum-complexity objective

Among candidate structures that satisfy the frozen design requirements, prefer the construction minimizing unnecessary freedom,

\[
\mathcal C(M)=\alpha N_{\rm free\ parameters}+\beta N_{\rm arbitrary\ functions}+\gamma N_{\rm auxiliary\ assumptions},
\]

subject to all mandatory constraints.

This is a model-selection discipline, not a physical law and not a fitted likelihood.

## G. Anti-overfitting split

The fundamental state space and dynamics may use the frozen RQIR semantic requirements, but detailed Paper-I/II/III detector optimization and comparator-relative performance are not used to tune the foundational ansatz. Those stages function as validation/holdout layers after the dynamics is frozen.
