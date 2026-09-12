# Iter025C / G42-C2 terminal result

## Provenance

- Run: `34710953936`
- Head / launch commit: `858ad4b6848362bf430eaab849fb0ed4166f9cde`
- Aggregate job: `103600409310`
- Summary artifact: `10303587123`
- Summary artifact digest: `sha256:d71af618510d0d61fbac14a3db91e9bf713822f657cfd985cc54e96fbf2ac94e`

## Frozen gate

Boundary-capable bounded real-PSD 6x6 classical random-Hamiltonian Kossakowski calibration with direct lower-triangular Cholesky coordinates `C=B B^T`, diagonal coordinates `[0,0.60]`, off-diagonal coordinates `[-0.30,0.30]`. Positive controls had intended ranks 2/4/5/6. Sobol/LHS, 32 starts, top-6 bounded least-squares refinements. Each lane required trace recovery `<0.002`, relative Kossakowski error `<0.02`, exact recovered effective rank at eigenvalue threshold `1e-5`, and PSD validity.

## Raw aggregate classification

All 8/8 lanes passed.

- Sobol: 4/4 support; worst trace gap `4.2824978732075346e-10`; worst relative Kossakowski error `3.3388943747698924e-09`; rank match 4/4.
- LHS: 4/4 support; worst trace gap `1.9221941865034614e-10`; worst relative Kossakowski error `1.9289529867904655e-09`; rank match 4/4.

Classification: **`PSD_BOUNDARY_OPTIMIZER_CALIBRATED`**.

## Interpretation

This is positive-control optimizer calibration for ranks 2/4/5/6 only. It does not use RCG-002 and is not a physics comparator result. Together with G42-C3 it may authorize a separately preregistered adversarial gate using the same bounded boundary-capable chart and search rules. It does not establish calibration of an unbounded mathematical PSD family.
