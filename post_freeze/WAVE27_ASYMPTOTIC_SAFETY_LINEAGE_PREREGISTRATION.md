# Wave 27 — Asymptotic-Safety Same-Realization Lineage / Jacobian Audit

Status: **PREREGISTERED BEFORE GITHUB COMPUTE**

## Frozen inputs

- Wave-22 prospective bank remains immutable.
- Parent-Law Acceptance Protocol v1 remains immutable.
- Wave-26 establishes that abstract Ward + fixed-point constraints can be rank-transverse but PL1 remains blocked without a concrete same-realization microscopic-to-RQIR map.
- No KMQGB/polygon candidate equations or architecture may be imported. KMQGB metadata/blocker language may be compared only after the independent Wave-27 verdict is frozen.

## Scientific question

Does the published asymptotic-safety literature, as of 2026-09-12, already contain a **single auditable realization/lineage** supporting the chain

`UV fixed point/eigendirections -> integrated RG trajectory -> physical k=0 2/3/4-point objects -> Lorentzian/on-shell observable representation -> explicit map into the six frozen RQIR residual directions -> propagated truncation/regulator uncertainty`?

Wave 27 audits provenance and completeness. It does not numerically fit a candidate theory and does not infer missing maps from adjacent papers.

## Required nodes J0–J9

- J0: realization/truncation/regulator identity is explicit.
- J1: interacting UV fixed point is explicit.
- J2: relevant eigendirections/critical-surface coordinates are explicit.
- J3: the corresponding RG trajectory is integrated toward the physical IR.
- J4: physical-limit two-point information is explicit.
- J5: physical-limit three-point information is explicit.
- J6: physical-limit four-point information is explicit.
- J7: diffeomorphism-invariant Lorentzian or on-shell observable/effective-action representation is explicit enough for detector/amplitude matching.
- J8: an explicit same-realization Jacobian/sensitivity map from independent UV trajectory coordinates to **all six** frozen RQIR residual directions `[c3,d3,e4,f4,s2,s0]` exists.
- J9: truncation/regulator/scheme uncertainty is propagated through that map to the six residual outputs.

A complete lineage must satisfy all J0–J9 without splicing incompatible realizations.

## Frozen literature rows

The evidence table is frozen in `evidence/WAVE27_ASYMPTOTIC_SAFETY_LINEAGES.json` and contains these source families:

1. **F1 — Denz, Pawlowski, Reichert (2018), arXiv:1612.07315 / EPJC 78, 336.** Systematic fluctuation/vertex expansion through the graviton four-point function; UV fixed point and IR trajectories toward classical GR.
2. **F2 — Pawlowski, Tränkle (2024), Phys. Rev. D 110, 086011.** Fully momentum-dependent three- and four-graviton couplings at the physical cutoff; reconstruction of the quantum effective action/form factors and black-hole equations.
3. **L1 — Assant, Litim, Reichert (2026), arXiv:2606.19321.** Lorentzian graviton spectral functions interpolating between classical GR and an asymptotically safe UV fixed point; effective action to quadratic curvature and form factors.
4. **E1 — Del Porro et al. (2026), DOI 10.1002/prop.70101.** Essential six-derivative truncation containing Newton and Goroff–Sagnotti `C^3`; one relevant direction, explicit separatrix and an IR Wilson-coefficient extraction under two regulator prescriptions.
5. **C1 — Knorr (2026), arXiv:2602.21285.** Explicit scattering calculation showing that a fixed point alone does not guarantee amplitude boundedness and that derivative/RG-improvement approximations can fail for Wilson coefficients/momentum dependence; used as a methodological guard, not as a lineage-completion source.

## Predeclared audits

### A27-1 Single-lineage completeness

Evaluate each declared lineage separately. Gate: no lineage may be marked complete unless all J0–J9 are supported inside that lineage.

Predeclared signal: `no_single_published_lineage_closes_J0_J9`.

### A27-2 Anti-splice graph

Compute union coverage across all rows and compare it with maximum same-lineage coverage. Even if a cross-lineage union covers many nodes, it may not be promoted to a same-realization chain.

Predeclared signal: `cross_lineage_union_cannot_substitute_same_realization_chain`.

### A27-3 Explicit Jacobian gate

Search the frozen evidence rows for a literal support state for J8 and J9. Partial 2-point form factors, a single `C^3` Wilson coefficient, or full momentum 3/4-point functions do not count as a six-direction UV-to-RQIR Jacobian.

Predeclared signals:
- `explicit_six_direction_jacobian_missing`;
- `propagated_six_direction_uncertainty_missing`.

### A27-4 Goroff–Sagnotti partial-chain diagnostic

E1 is allowed to count as a genuine **partial positive bridge**: fixed point -> relevant eigendirection -> unique separatrix (after unit scale fixing) -> one higher-curvature IR Wilson coefficient.

It must not be generalized to six residual directions. Its two reported regulator prescriptions preserve the positive sign but give substantially different coefficient magnitudes; therefore the audited status is `PARTIAL_DIRECTION_WITH_SCHEME_SENSITIVITY`, not quantitative six-direction closure.

Predeclared signals:
- `C3_partial_UV_to_IR_bridge_exists`;
- `C3_sign_robust_but_magnitude_scheme_sensitive`.

### A27-5 Full-momentum vertex partial-chain diagnostic

F1+F2 may count as the strongest physical 2/3/4-point lineage, including k=0 momentum-dependent three/four-graviton information and reconstructed effective-action form factors. It receives no J8/J9 credit unless the frozen evidence includes sensitivity derivatives from UV relevant coordinates to all six residual outputs.

Predeclared signal: `full_momentum_vertices_exist_but_UV_to_RQIR_sensitivity_map_missing`.

### A27-6 Lorentzian partial-chain diagnostic

L1 may count as a strong Lorentzian 2-point/quadratic-curvature bridge. It cannot supply missing 3/4-point RQIR directions merely by being Lorentzian.

Predeclared signal: `lorentzian_quadratic_bridge_exists_but_higher_point_closure_missing`.

## Aggregate decision

If all preregistered signals are true, classify the missing object as:

`BLOCKED_MISSING_SAME_REALIZATION_UV_TO_RQIR_SIX_DIRECTION_JACOBIAN_WITH_PROPAGATED_UNCERTAINTY`.

This is stronger and narrower than saying “asymptotic safety has no predictions.” The audit explicitly recognizes existing UV-to-IR and 2/3/4-point progress while refusing to splice incompatible truncations into an artificial full theory.

## Claim boundary

Wave 27 cannot prove that the required Jacobian does not exist unpublished or cannot be derived. It audits the frozen public evidence set above and identifies what must be produced next for a prospective PL1 decision.
