# Iter032 / G44-A — terminal result

Run `34718045811`, launch/head `fbb9305039bc44086e100ba23fe4c90e2a13cd97`.
Aggregate job `103620135891`; summary artifact `10305246941`; digest `sha256:6b872735ae3fc2ad3512c44cda92b1567f413242d81f43cee09f7687d6a1f5d8`.

Frozen family: basis-invariant real-PSD Markovian classical random-Hamiltonian trace ball `C=A^2`, `A=A^T`, `tr(C)<=4`. Frozen target convention is the same four RCG-002 toy trajectories used by G42-A. Two prospectively fixed QMC methods were required per shard; each lane required gap `>1e-4`, structural/admissibility validity, and each pair required absolute gap disagreement `<=0.002`.

All 8/8 lanes were structurally valid, admissible and individually supporting. Pair results:

- shard 0: Sobol/LHS gaps `0.037007977715339695`, `0.0370079787290966`; difference `1.0137569048107586e-09`;
- shard 1: `0.14632856614507492`, `0.14632854102560847`; difference `2.511946645133989e-08`;
- shard 2: `0.5275494416263767`, `0.5275492466713227`; difference `1.9495505398925417e-07`;
- shard 3: `0.6620257715176718`, `0.6628923292652587`; difference `0.0008665577475868158`.

All four frozen pair rules pass. Classification:

`DERIVED_SCOPED_BASIS_INVARIANT_TRACE_BALL_PSD_COMPARATOR_SUPPORT`

This closes the bounded basis-invariant `tr(C)<=4` Markovian real-PSD comparator layer and authorizes a programme-readiness review from 61% to 62% under the stable rubric.

## Scope ceiling

This is a finite bounded-family toy-trajectory result only. It is not an unbounded-PSD result, not an arbitrary non-Markovian result, not an LOCC or semiclassical-gravity no-go, and not evidence that all classical mediators fail. `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, and universal no-go claims remain forbidden.
