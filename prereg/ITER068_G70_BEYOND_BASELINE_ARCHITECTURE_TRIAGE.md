# Iter068 / G70 — beyond-baseline architecture triage (FROZEN)

Prospectively preregistered on 2026-09-13 before implementation/production.

## Purpose
G69 terminally found `BLOCKED_CANDIDATE_OWNED_BEYOND_BASELINE_DYNAMICS_NOT_YET_DEFINED`. G70 is therefore a **theory-construction triage**, not a validation gate and not a novelty claim. It asks which mathematical architecture classes remain structurally viable enough to justify a separately preregistered candidate construction.

No class may be selected by a weighted score chosen after results. The output is a Pareto-style matrix of frozen structural properties and unresolved obligations.

## Frozen baseline locks
Every architecture is judged relative to the already closed standard layers:
- G58 standard linearized massless-spin-2 baseline;
- G68 standard local curvature-squared quadratic-gravity baseline.

A class is not 'new physics' merely because it lies outside those two baselines. Literature novelty and experimental novelty require later independent audits.

## Frozen common properties
For each stream report, without post-hoc relaxation:
1. `LOW_ENERGY_RECOVERY`: deformation tends to the baseline at the frozen expansion point `z=0`.
2. `WARD_COMPATIBLE_LINEAR_RESPONSE`: conserved-source transverse response can be maintained without adding longitudinal source dependence.
3. `NO_NEW_FINITE_LINEAR_POLES`: the frozen linear response does not introduce additional finite propagator poles relative to the massless baseline.
4. `RETARDED_CAUSAL_RULE_EXPLICIT`: an explicit retarded prescription is part of the architecture rather than merely desired.
5. `FIELD_LEVEL_QUANTUM_RULE_EXPLICIT`: the architecture contains an explicit field/influence-functional quantum rule rather than only a two-probe operational channel.
6. `BASELINE_DISTINCT_DISCRIMINATOR_EXPLICIT`: at least one mathematical discriminator from G58/G68 is specified before future data/results.

Each property is one of `SUPPORTED`, `NOT_SUPPORTED`, `UNRESOLVED`. `UNRESOLVED` is not converted to PASS.

## Stream A — local six-derivative polynomial extension
Frozen representative linear response modifier:
`F_A(z)=1+c1*z+c2*z^2`, with `c2 != 0`, so the inverse response is proportional to `1/[z F_A(z)]`.
Coefficient panel: `(c1,c2)={(0,1),(1,1),(-1,1),(2,-1),(3,2),(-2,3)}`.
Required calculation: exact roots/discriminants and low-z expansion. `NO_NEW_FINITE_LINEAR_POLES` is SUPPORTED only if **every** frozen nonzero-`c2` lane has no finite root; otherwise NOT_SUPPORTED. This stream does not infer ghosts/unitarity from roots.

## Stream B — pole-free entire form-factor extension
Frozen representative:
`F_B(z)=exp[(z/M^2)^2]`, `M>0`; inverse response `1/[z F_B(z)]`.
Frozen dimensionless `x=z/M^2` panel: `{-4,-2,-1,-1/2,0,1/2,1,2,4}` plus the exact symbolic facts `F_B(0)=1` and `exp(w) != 0` for finite complex `w`.
Report low-energy recovery and absence of new finite zeros/poles as structural properties. A Lorentzian retarded realization is **UNRESOLVED** unless the stream itself constructs one; do not infer causality from entire analyticity alone.

## Stream C — Gaussian CTP/influence-functional architecture
Frozen schematic source functional:
`Gamma_CTP = DeltaT * D_R * SigmaT + (i/2) DeltaT * N * DeltaT`, with `D_R` retarded and `N` real PSD.
Frozen finite kernel panel uses 4x4 retarded lower-triangular rational matrices and PSD noise matrices `N=L L^T` generated from deterministic integer `L` seeds `{2,3,5,7}`.
Required checks: CTP normalization at `DeltaT=0`, retarded support of `D_R`, symmetry/PSD of `N`, baseline recovery when `N=0` and `D_R=D_R^baseline`, and a prospective baseline-distinct discriminator `N != 0`. This is an architecture test only; do not claim standard-vs-novel literature status here.

## Stream D — non-Gaussian CTP cumulant extension
Frozen representative adds a cubic connected source functional
`DeltaGamma_3 = kappa3 * sum_abc K3_abc * DeltaT_a * SigmaT_b * SigmaT_c`
with symmetric `K3` in `(b,c)` and deterministic rational held-out tensors from seeds `{11,13,17,19}`.
Required checks: exact vanishing at `DeltaT=0`, baseline recovery at `kappa3=0`, nonzero third functional derivative/discriminator for `kappa3!=0`, and conservation compatibility when all source legs are first projected to the frozen transverse conserved-source subspace. Positivity/unitarity/complete field-measure consistency is **UNRESOLVED** unless derived, not assumed.

## Stream E — relational source-dependent transverse-kernel extension
Frozen representative linearized-in-output but source-dependent kernel:
`D_eff[T] = D_R * [1 + lambda * I(T)]`, where `I(T)=S(T,P2 T)+S(T,P0 T)` is the exact conserved-source scalar from the G65 projectors and `lambda` is a frozen deformation parameter.
Frozen `lambda={-1/5,1/7,1/3}` and G65 momenta/seeds `{10,11,12,13}`.
Required checks: exact conservation/Ward compatibility after projection, baseline recovery at `lambda=0`, nonzero prospective source-amplitude dependence for every nonzero lambda on at least one frozen source, and exchange/basis-scalar invariance of `I(T)` over the frozen discrete-Lorentz panel. A full nonlinear covariant action, retarded prescription and quantum measure remain **UNRESOLVED** unless explicitly constructed.

## Aggregate / selection rule
The aggregate returns the complete property matrix. A class is `STRUCTURALLY_DOMINATED` only if another class is at least as strong on every frozen common property (SUPPORTED > UNRESOLVED > NOT_SUPPORTED) and strictly stronger on at least one, **without** using literature novelty or subjective weights.

Allowed aggregate labels:
- `BEYOND_BASELINE_ARCHITECTURE_TRIAGE_COMPLETE_NO_UNIQUE_SELECTION`
- `BEYOND_BASELINE_ARCHITECTURE_TRIAGE_COMPLETE_PARETO_<classes>`
- `INFRASTRUCTURE_OR_ARTIFACT_INVALID`
- `EVIDENCE_AUDIT_INCONCLUSIVE_<streams>`

Even a Pareto-leading class is only a construction route. It is not validated gravity, new physics, or full quantum gravity.

Programme readiness remains **66%** and theory established remains **0%**. G70 cannot change either number.
