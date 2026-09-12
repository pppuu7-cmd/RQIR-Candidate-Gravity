# ITER027 / G43-A — terminal held-out multichart coverage result

Run: `34715739668`
Head: `b69524b9fe8c33ff2f433f1d9dbc6ce54f8e4a06`
Aggregate job: `103614423827`
Summary artifact: `10304965236`
Summary digest: `sha256:7b45a058f3ab45cc93f869a151b5f6dd4c9f32567964d8aaa7eaa170747cb4a9`

## Frozen result

All 36 response-blind rank × basis-rotation lanes were structurally valid and satisfied the frozen local-basis generator-covariance check. The fixed five-chart atlas covered **25/36** lanes and left **11/36** uncovered.

Coverage by effective rank:

- rank 1: 6/6
- rank 2: 6/6
- rank 3: 6/6
- rank 4: 3/6
- rank 5: 1/6
- rank 6: 3/6

Worst covariance errors stayed around `4.34e-16`; worst chart reconstruction error was `2.145501964580735e-13`. Uncovered lanes therefore represent finite-atlas coordinate coverage limits, not a failure of PSD validity or basis covariance.

Terminal classification:

`HELDOUT_MULTICHART_BASIS_COVERAGE_PARTIAL_LIMIT`

## Scientific interpretation lock

This is a response-blind diagnostic of the preregistered finite five-chart atlas. It does not alter the exact bounded-chart G42-A comparator result, does not establish a basis-invariant full-PSD result, and does not raise programme readiness.

No chart or coordinate bound may be added post hoc to convert this terminal partial-coverage result into PASS. The appropriate prospective route is a separately preregistered basis-invariant family/parameterization such as G44, with its own representation validation, optimizer calibration and only then an adversarial test.
