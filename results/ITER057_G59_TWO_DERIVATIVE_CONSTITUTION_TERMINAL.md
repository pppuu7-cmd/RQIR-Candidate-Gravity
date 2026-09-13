# Iter057 / G59 — two-derivative constitution freedom audit

Date: 2026-09-13

## Terminal scientific classification

`TWO_DERIVATIVE_LINEARIZED_LOCAL_CONSTITUTION_UNIQUE_UP_TO_NORMALIZATION_SCOPED`

This is a **SCOPED DERIVED/PROVEN result** for the preregistered class only: one symmetric rank-2 field on 4D Minkowski space, local Lorentz-invariant quadratic action, exactly two derivatives, and linear gauge symmetry. It is not a no-go theorem for higher-derivative, nonlocal, additional-field, nonlinear, semiclassical, or quantum-gravity constructions.

## Authority

- Preregistration commit: `be227eed76829992739e6ba6b757d0fff15b6cba`
- Implementation commit: `723009b10963223a6ca274cdb3fd6eac9906891c`
- Production head: `73c3018430ac9a4f4296bdeab74b237dade81cfc`
- Workflow run: `34753280230`
- Aggregate job: `103713350380`
- Aggregate artifact: `10316797122`
- Aggregate digest: `sha256:085f4fec69424d6ae00a137f94b16d7bf631d6a0c0e3f93b3424443ad09c7a68`

Raw lanes:
- A job `103713309803`; artifact `10315947991`; digest `sha256:2a154c86ad57b7a0b4ec928fe3da0e9b5ab5cd6382a8f3aafc6f1b0bd3b378a3`
- B job `103713309848`; artifact `10315799938`; digest `sha256:63757ac7bbc9d2d83c31f20d8c4d4c4bc69652050adcc9f5a48a56fca0a88451`
- C job `103713309863`; artifact `10316503144`; digest `sha256:86659fdf2a9a5aa35e5117608bd3bc97b57fb762d8196fa1bac6f17d34724154`
- D job `103713309722`; artifact `10316124093`; digest `sha256:cc89d4aa20fd02371c26b24be7602ab36afeb39d24764212443eaa941cff00d8`

## Frozen evidence consumed

All four raw artifacts and the frozen aggregate were consumed; green CI alone was not used as scientific evidence.

- **Stream A:** exact constraint matrix rank `3`, nullity `1`; unique projective coefficient ray represented by `(-1, 2, -2, 1)`, equivalent to the preregistered reference ray up to overall normalization/sign convention.
- **Stream B:** `18/18` held-out gauge/Bianchi tests are exact zero on the allowed ray; the deliberately wrong ray is rejected in `18/18` cases.
- **Stream C:** `10/10` conserved-source response tests pass; the wrong trace coefficient is rejected in `10/10` cases.
- **Stream D:** all `3 x 4` basis/sample robustness checks pass and the deliberately rank-deficient diagnostic is detected (`bad_nullity=3`).
- Frozen aggregate: A/B/C/D all PASS and returns the terminal classification above.

## Interpretation

Within the sharply frozen local, linear, two-derivative, single symmetric-tensor class, the constitution is unique up to overall normalization. Together with G58-B, this means that an independently motivated RQIR-CG novelty cannot be obtained merely by retuning coefficients while remaining inside that same class. Any future candidate-owned deformation must leave at least one frozen assumption (for example derivative order, locality, field content, or linear regime) and must be independently motivated and prospectively tested.

This result does **not** establish nonlinear GR equivalence, a complete gravity theory, quantization, a measure, or new physics. No physical ansatz/result from RQIR, KMQGB, or QGR was imported.

## Readiness

- Candidate-model/programme readiness: **66%** (unchanged; G59 closes a structural prerequisite but does not close a separately scored constitution rubric).
- Theory established: **0%**.

## Next authorized scientific direction

Map candidate-independent escape space beyond the frozen two-derivative class before adopting any deformation. A prospectively preregistered higher-derivative linearized gauge-invariant operator-basis audit may be used to determine whether nontrivial local four-derivative directions exist and how they alter source response/pole structure. Such a gate is structural only and cannot itself authorize a candidate action or raise `THEORY_ESTABLISHED`.