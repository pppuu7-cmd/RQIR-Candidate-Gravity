# Iter068 / G70 terminal result — beyond-baseline architecture triage

Date: 2026-09-13

Frozen preregistration: `protocol/ITER068_G70_BEYOND_BASELINE_ARCHITECTURE_TRIAGE.md`.

Authoritative scientific stream run: `34772158456` at head `8944998e6f799ef28ca0e26cf41efb7988a2bf24`.
All five frozen streams A-E completed successfully and produced valid immutable artifacts. The original aggregate job failed for infrastructure only (`sympy` missing in aggregate environment); no stream science was rerun or changed.

Analysis-only recovery aggregate: run `34772248100`, job `103763840814`, aggregate artifact `10322650703`, digest `sha256:a4c97a45ebfa26ddfb707614c9817f0c8d2f9a8303616664517399dc635d8f0a`.

Frozen classification:

`BEYOND_BASELINE_ARCHITECTURE_TRIAGE_COMPLETE_NO_UNIQUE_SELECTION`

## Frozen property matrix

| stream | low-energy | Ward-compatible linear response | no new finite linear poles | retarded causal rule explicit | field-level quantum rule explicit | baseline-distinct discriminator |
|---|---|---|---|---|---|---|
| A local 6-derivative polynomial | SUPPORTED | SUPPORTED | NOT_SUPPORTED | UNRESOLVED | UNRESOLVED | SUPPORTED |
| B entire/pole-free | SUPPORTED | SUPPORTED | SUPPORTED | UNRESOLVED | UNRESOLVED | SUPPORTED |
| C Gaussian CTP/influence functional | SUPPORTED | UNRESOLVED | UNRESOLVED | SUPPORTED | SUPPORTED | SUPPORTED |
| D non-Gaussian CTP cubic cumulant | SUPPORTED | SUPPORTED | UNRESOLVED | UNRESOLVED | SUPPORTED | SUPPORTED |
| E relational source-dependent transverse kernel | SUPPORTED | SUPPORTED | SUPPORTED | UNRESOLVED | UNRESOLVED | SUPPORTED |

Under the preregistered ordinal Pareto rule, A is dominated by B. The non-dominated set is `{B,C,D,E}`. No weighted score was introduced post hoc and no unique architecture is selected.

Programme readiness remains **66%** and theory established remains **0%**. G70 is construction triage only; no stream is thereby a validated gravity theory, a novelty theorem, new physics, or full quantum gravity.

Next admissible work must attack unresolved properties prospectively and independently: especially causal/quantum closure for B/E; Ward and finite-pole structure for C; finite-pole and causal structure for D. Do not select one of B/C/D/E by preference before those discriminators are tested.