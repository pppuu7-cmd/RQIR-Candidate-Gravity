# RQIR-CG research ledger

This file is the clean authority ledger for `RQIR-Candidate-Gravity` only. The pre-existing `research_log/RESEARCH_ACTIVITY_LEDGER.md` contains legacy material from another research line and must not be used as scientific evidence for RQIR-CG.

## Scope contract

RQIR-CG is an independent candidate-gravity construction. RQIR/KMQGB/QGR may contribute methodology, gate discipline and mathematical tools, but not imported physical assumptions, ansatz coefficients or desired conclusions.

## Latest authoritative results

| Iteration | Gate | Run / head | Classification | Result ceiling |
|---|---|---|---|---|
| Iter010 | G28 full-Bloch comparator audit | run `34692403874`, head `3d8d3f969a22c22c1526b00f42377c2d41f87a04` | `DERIVED_SCOPED_NEGATIVE_COMPARATOR_RESULT` | 24/24 nonzero gaps; off-XZ improvement count 0; finite single-axis Markovian family only. |
| Iter011 | G29 robustness suite | run `34694101699`, head `c4c6f0d35e4e57a2105facafee2bdddc8036a52f` | `DERIVED_SCOPED_ROBUSTNESS_SUPPORT` | 24/24 structural valid and support; finite single-axis Markovian family only. |

### Iter010 aggregate

Summary artifact `10297865845`:

- 24/24 structural passes;
- 24/24 nonzero full-sphere gaps;
- 0/24 off-plane improvements over nested X-Z search at the frozen 1% criterion;
- maximum improvement versus X-Z `9.589850893877267e-16`;
- minimum full-sphere gap `0.012499674481709782`.

### Iter011 aggregate

Summary artifact `10297528599`, digest `sha256:b7f80fc91bba1b45371ec1cec1865ddbc9dab3a1ab7c4138a94d4a5064287356`:

- 24/24 structurally valid;
- 24/24 satisfy frozen scientific-support criterion;
- minimum continuous adversarial gap `0.02500020131464493`;
- minimum Choi eigenvalue `-7.229908172761597e-16`;
- minimum identifiability rank `6/6`;
- maximum finest RK4 cross-check error `1.0037722995948985e-11`.

## Infrastructure correction

Commits `86d740b6dd884cd49f401b526dbcb28dc6f5944d` and `2aef6779a8541e3beb4acf4e9be58dcb3ff1e2d7` removed broad `push: main` triggers from closed Iter003 and Iter009 workflows. Closed historical matrices no longer rerun on unrelated scientific commits.

## Current frontier

The single-axis Markovian comparator layer has now survived basis enlargement and the G29 robustness audit. The dominant scientific uncertainty is no longer angular grid density; it is comparator-family breadth.

Next gate: additive K=2/K=3 multi-channel GKSL measurement-feedback comparator, with prospectively frozen adversarial searches plus in-family null and CPTP/PSD controls.

## Claim locks

Do not promote finite-family gaps to claims that all semiclassical gravity, all classical mediators, or all alternatives to quantum gravity are excluded. Do not use green CI as a scientific verdict. Record scientific negative results even when CI is green.
