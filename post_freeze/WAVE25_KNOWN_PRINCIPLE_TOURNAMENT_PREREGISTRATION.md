# Wave 25 — Known-Principle Tournament under Parent-Law Acceptance Protocol v1

Status: PREREGISTERED BEFORE COMPUTE

## Frozen authorities

- `protocol/PARENT_LAW_ACCEPTANCE_PROTOCOL_V1.json` is the judge.
- `holdouts/WAVE22_FROZEN_BANK.json`, blob `c32bd52edd003589ef65e0240c757475f215f55f`, remains immutable.
- RQIR action-level endpoint v1 remains frozen.
- No KMQGB/polygon candidate equations or architecture may be imported.

## Purpose

Screen established physical principle classes against the already-frozen parent-law gate. The tournament does **not** ask which literature programme is “correct”. It asks the narrower prospective question: does the named principle, *by itself and without hidden extra input*, close the six-dimensional RQIR residual proxy and earn all five parent-law gates?

## Literature provenance anchors

### K1 Soft/Ward consistency
- Cachazo & Strominger, arXiv:1404.4091: universal leading soft graviton behavior and a subleading soft relation tied to conservation/gauge structure.
- Classification rule: established consistency relation, not a new microscopic parent law.

### K2 Gravitational positivity / dispersion
- Tokuda, Aoki & Hirano, arXiv:2007.15009.
- Hamada, Kuramochi, Loges & Nakajima, arXiv:2301.01999.
- Classification rule: bounds allowed EFT data under assumptions; a bounded region is not a unique microscopic point.

### K3 Causality / UV-completion consistency
- Camanho, Edelstein, Maldacena & Zhiboedov, arXiv:1407.5597.
- Classification rule: causality constrains higher-derivative graviton couplings and can imply additional UV structure, but the consistency condition alone does not specify the complete UV parent data.

### K4 Asymptotic-safety fixed-point scaling
- Eichhorn, arXiv:2606.21522 (2026 review).
- Gubitosi, Ripken & Saueressig, review of asymptotically safe QG scales/hierarchies.
- Classification rule: an interacting UV fixed point with a finite UV-critical surface can make infinitely many couplings dependent, but coefficients along relevant directions remain free trajectory data unless fixed by additional input. Therefore the fixed-point principle alone is not zero-nullity when at least one relevant direction exists.

### K5 Double copy / color-kinematics
- White, arXiv:1708.07056.
- Bern et al., arXiv:2203.13013.
- Classification rule: double copy is a powerful conditional construction from gauge-theory parent data and generates a web of gravity theories; the relation alone does not uniquely select the upstream gauge parents.

## Frozen finite diagnostics

### K1 soft/Ward proxy
Use the same six-dimensional residual coordinates as Wave 24 and a frozen rank-3 Ward-like matrix. Gate: rank = 3, residual nullity = 3, hence PL1 closure FAIL.

### K2 positivity proxy
Sample `20,000` points with seed `2502` inside a fixed ellipsoid `sum((theta_i/b_i)^2) <= 1`, with `b=[0.20,0.18,0.15,0.12,0.10,0.09]`. Gate: frozen-bank maximum prediction width >= `0.05`, hence admissibility region remains nonunique.

### K3 causality/UV proxy
One higher-derivative coefficient `c` is constrained to `[-0.95,0.95]`, while a separate positive UV-scale proxy `m` lies in `[1,4]`. Sample a frozen grid and map to a two-observable vector `[0.4*c/m^2, 0.25*c^2/m^4]`. Gate: more than one distinct allowed prediction and Euclidean prediction diameter >= `0.05`.

### K4 asymptotic-safety critical-surface proxy
For `r=0,1,2,3,4` relevant directions, fixed-point conditions set `6-r` directions while `r` trajectory constants remain free. Gate: for every `r>=1`, residual nullity = `r`; only the special `r=0` case is unique from fixed-point conditions alone. Tournament classification uses `r>=1` because the cited fixed-point framework explicitly permits relevant free directions.

### K5 double-copy conditional-parent proxy
Use two preregistered gauge-parent vectors `A1,B1` and `A2,B2` with a frozen bilinear map `g=[a0*b0,a1*b1,a0*b1+a1*b0,a2*b2,a0*b2+a2*b0,a1*b2+a2*b1]`. Gate: different allowed parent choices produce gravity vectors whose frozen-bank predictions differ by L2 >= `0.05`; the map therefore does not itself select a unique parent input.

## Frozen PL1–PL5 classification before compute

The literature/provenance classification is fixed before numerical diagnostics:

- K1 soft/Ward: PL1 FAIL; PL2 PASS; PL3 FAIL (known generic consistency relation); PL4 PASS; PL5 PASS.
- K2 positivity/dispersion: PL1 FAIL; PL2 PASS; PL3 FAIL (known consistency/bound machinery); PL4 FAIL as point-predictivity; PL5 PASS.
- K3 causality/UV consistency: PL1 FAIL; PL2 PASS; PL3 FAIL as a standalone parent law; PL4 FAIL without specifying UV parent data; PL5 PASS.
- K4 asymptotic safety: PL1 FAIL for any `r>=1`; PL2 PASS; PL3 PASS as a UV hypothesis distinct from low-energy C5; PL4 PASS in principle through irrelevant directions; PL5 PASS at the level of a finite relevant critical surface. This does not assert that the complete nonperturbative theory is already established.
- K5 double copy: PL1 FAIL because upstream parent data remain unselected; PL2 PASS; PL3 FAIL for this tournament because it is an already-known generic construction rather than a newly derived microscopic selector; PL4 PASS conditional on selected parents; PL5 FAIL as a standalone parent selector because parent-choice freedom remains upstream.

No K1–K5 class is preregistered to pass all five gates.

## Aggregate signals

- soft_ward_leaves_residual_nullity
- positivity_region_nonunique
- causality_uv_region_nonunique
- asymptotic_fixed_point_with_relevant_directions_nonunique
- double_copy_is_conditional_on_parent_choice
- literature_gate_matrix_has_no_full_pass
- no_known_principle_tested_here_earns_new_parent_law_credit
- future_candidate_information_firewall_pass

## Claim boundary

Failure to earn all five gates does not falsify any named research programme. It only means the named principle, taken alone in the declared role and finite proxy, is insufficient to serve as the unique new RQIR parent law without additional physical input.
