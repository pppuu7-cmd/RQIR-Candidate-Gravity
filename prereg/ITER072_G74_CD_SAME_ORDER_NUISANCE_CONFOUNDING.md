# Iter072 / G74 — C/D same-order nuisance confounding

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION/RESULTS**
Date: 2026-09-13

## Scope
G73 established exact local rank-two identifiability of the frozen C quadratic/two-point and D cubic/three-point hypothesis directions only when both perturbative orders are observed. G74 asks whether that rank survives plausible same-order nuisance tangent directions. This is an identifiability-robustness gate, not architecture selection and not candidate-owned dynamics.

Frozen momentum panel: `z={1/3,2/3,5/4,7/3}`.
Frozen C tangent on quadratic rows: `C=(-z_i,0_cubic)`.
Frozen D tangent: `D=(0,0,0,0,1)`.
Frozen nuisance tangents:
- `N0=(1,1,1,1,0)` constant quadratic normalization;
- `N1=(z_i,0)` same-shape quadratic slope nuisance;
- `N2=(z_i^2,0)` distinct quadratic curvature nuisance;
- `N3=(0,0,0,0,1)` same-shape cubic calibration nuisance.

## Independent streams
A — baseline confirmation: exact rank(C,D)=2; adding N0 gives rank 3 and C remains outside span(D,N0).
B — C confounding: exact rank(C,N1)=1 with proportionality `C=-N1`; adding N2 instead gives rank(C,N2)=2 on the frozen nonzero panel.
C — D confounding: exact rank(D,N3)=1; with N0 or N2 only, D remains independent.
D — combined audit and controls: full columns (C,D,N0,N2) have rank 4; adding N1 and N3 cannot increase identifiable C/D content because C lies in span(N1) and D lies in span(N3). Control with a deliberately different cubic nuisance row in an auxiliary second cubic observable must restore independence from D.

## Frozen aggregate rule
All streams valid => `CD_IDENTIFIABILITY_REQUIRES_SAME_ORDER_NUISANCE_ANCHORS_SCOPED`.
Any failed scientific predicate => `SCIENTIFIC_FAIL_FROZEN_NUISANCE_CONFOUNDING_PREDICATE`.
Missing/invalid controls/artifacts => `INFRASTRUCTURE_OR_GATE_INVALID`.

## Interpretation ceiling
PASS means only that G73 identifiability is not nuisance-robust against exact same-shape same-order nuisance tangents; independent nuisance anchors or additional shape/order observables are required. It does not invalidate C or D, select an architecture, fit a coefficient, define RCG-002 dynamics, or establish new physics. Readiness stays 66%; theory established stays 0%.
