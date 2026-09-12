# Iter026R / G42-R — held-out PSD calibration replication

Status: **PREREGISTERED independently of G42-A production results**.

Purpose: test whether the G42-C2/C3 optimizer calibration transfers to new, previously unused positive controls spanning every effective PSD rank 1–6. This is methodology robustness only and cannot modify the frozen G42-A physics verdict.

## Frozen family/search

Identical boundary-capable comparator chart and optimizer rules as G42-C2/C3:

- `C = B B^T`, real lower-triangular B;
- diagonal `[0,0.60]`, off-diagonal `[-0.30,0.30]`;
- times `[0.15,0.45,0.9,1.4]` and the same six product probes;
- methods `sobol_lsq` and `lhs_lsq`;
- 32 starts, top 6 smooth-residual candidates, bounded least-squares, `max_nfev=1000`;
- hidden coordinates never inserted as starts.

Six new hidden controls have intended ranks 1,2,3,4,5,6 and use deterministic seeds disjoint from G42-C2/C3.

Each method×rank lane must satisfy simultaneously:

- max trace-distance recovery `<0.002`;
- relative Kossakowski error `<0.02`;
- recovered effective rank at eigenvalue threshold `1e-5` equals intended rank;
- minimum Kossakowski eigenvalue `> -1e-10`.

Aggregate PASS requires 12/12 lanes support. Classification `PSD_BOUNDARY_HELDOUT_CALIBRATION_REPLICATED`; otherwise `PSD_BOUNDARY_HELDOUT_CALIBRATION_NOT_REPLICATED`.

No RCG-002 target is used. No result may raise programme readiness by itself or alter G42-A thresholds/search/family.
