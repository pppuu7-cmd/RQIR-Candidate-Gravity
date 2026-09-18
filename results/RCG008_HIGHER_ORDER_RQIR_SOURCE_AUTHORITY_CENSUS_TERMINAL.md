# RCG-008 — higher-order RQIR source-authority census — TERMINAL

Date: 2026-09-18

Status: **TERMINAL**

Classification:

`BLOCKED_SCOPED_RCG008_NO_EXISTING_APPLICABLE_HIGHER_ORDER_RQIR_DATUM_IN_CURRENT_AUTHORITY`

## Frozen authority and execution chain

- Scientific preregistration: `a802ee303cccce73f0a8c974f4c73915ebae40c0`.
- Frozen RCG008 prereg blob: `8316d3f484cef5217065177450c79566371f9485`.
- Authority base commit: `1a53979ea1f684d6acdc35c789c0bf8c86e8f6b0`.
- Frozen corpus manifest: `data/RCG008_FROZEN_CORPUS_MANIFEST_V0.json`, blob `f10edc81b28d9feaeeecb2537a2c74d0916ad135`.
- Initial implementation commit: `702891f1db5d10604db63a02ec3fe3ddc042bdec`.
- Outcome-independent auditor correction before execution: `60ac01fd4743af9bc85a054f44ddfbd7e234d46d`.
- Initial execution freeze: `b01f237d9d50601805ca2dc8e84cc63db427f491`.
- Initial run `35367595336` was **pre-science infrastructure failure only**: identity verification passed, Constructor and Critic stopped on the same literal G90 wording guard, and aggregate/auditor were skipped. It carries no RCG008 scientific classification.
- Prospectively frozen execution-only wording/plumbing repair: `07f51a9a5b9ba86a30183dd48e27b1672da93f7d` and `b127f7adbe20101c1d3ff91c1c10c7a98b61f854`. Corpus, object set, ownership/order/domain decisions, positive controls, aggregate classifier and terminal taxonomy were unchanged.
- Repaired execution freeze / canonical scientific head: `7831e3f9f6067d38df524fb72c4dfa5f20a8d41d`.
- Canonical repaired Actions run: `35367838160` — **success**.

## Immutable Actions artifacts

| Artifact | ID | Digest |
|---|---:|---|
| `rcg008-constructor` | 10557556425 | `sha256:8e587fc07cadddc1f4b154672d95cb6acfa02b64bc8b5d8b2bc6ea51cd40f466` |
| `rcg008-critic` | 10557047022 | `sha256:db512efc9e725236f9caa419ce24cd3230d4381c727e2426f0d71a0d468b0a0a` |
| `rcg008-aggregate` | 10557401819 | `sha256:a41183338ddc78d3598c67208f54b1fbfcc382eb955969e7ff32f109074e5791` |
| `rcg008-independent-audit` | 10557251975 | `sha256:c8babccab20aee7bda5aedffa9ffa3ecc657f97119328b6fb366c9da56e9b819` |

Canonical JSON copies are frozen under `results/raw/RCG008_*.json`.

## Corpus and independent reconstruction

Constructor:
- `corpus_valid=true`;
- object count `12`;
- qualifying count `0`.

Independent Critic:
- `corpus_valid=true`;
- object count `12`;
- qualifying count `0`.

Aggregate:
- Constructor/Critic disagreements: `0`;
- `controls_ok=true`;
- `provenance_ok=true`.

The Constructor and Critic independently reconstruct the same complete frozen inventory and the same per-object qualification outcome.

## Mandatory positive controls

- G88: `FOUND_BUT_TOO_LOW_ORDER_FOR_ALPHA`.
- G89: `FOUND_BUT_D_SPECIFIC_UNBRIDGED`.
- RCG007 genuine-cubic synthetic sensitivity control: `FOUND_BUT_SYNTHETIC_CONTROL`.

All mandatory controls pass. Therefore the census is not invalidated by coverage failure.

## Exact candidate inventory

| Object | Order/domain role | Ownership | RCG008 status | Qualifies |
|---|---|---|---|---|
| G88 | lower-than-cubic inherited | inherited RQIR | `FOUND_BUT_TOO_LOW_ORDER_FOR_ALPHA` | no |
| G89 | cubic retarded/CTP, D-specific | inherited D architecture | `FOUND_BUT_D_SPECIFIC_UNBRIDGED` | no |
| G90 | cubic covariant completion family | gravity-candidate-generated | `FOUND_BUT_CANDIDATE_OWNED` | no |
| G91 | quartic covariant completion family | gravity-candidate-generated | `FOUND_BUT_CANDIDATE_OWNED` | no |
| G92 | higher-curvature diagnostic | candidate audit | `FOUND_BUT_NOT_SELECTOR_DATUM` | no |
| G93 | connected three-source operational form | RCG002 candidate-owned | `FOUND_BUT_CANDIDATE_OWNED` | no |
| G94 | cubic D bridge audit | D candidate-owned / D-specific | `FOUND_BUT_D_SPECIFIC_UNBRIDGED` | no |
| G95 | cubic finite-history ansatz | candidate ansatz | `FOUND_BUT_CANDIDATE_OWNED` | no |
| G96 | cubic-ansatz diagnostic | candidate diagnostic | `FOUND_BUT_NOT_SELECTOR_DATUM` | no |
| G97 | classical source preparation | candidate source bookkeeping | `FOUND_BUT_NOT_HIGHER_ORDER_SELECTOR` | no |
| RCG002 linearized baseline | linearized | RCG002 candidate-owned | `FOUND_BUT_CANDIDATE_OWNED` | no |
| RCG007 synthetic cubic control | cubic synthetic | synthetic control | `FOUND_BUT_SYNTHETIC_CONTROL` | no |

## Aggregate result

- `CANDIDATE_OBJECT_COUNT = 12`.
- `QUALIFYING_DATUM_COUNT = 0`.
- `REJECTED_CANDIDATE_OWNED_COUNT = 5`.
- `REJECTED_TOO_LOW_ORDER_COUNT = 1`.
- `REJECTED_DOMAIN_COUNT = 2`.
- `REJECTED_UNBRIDGED_COUNT = 2`.
- `BRIDGE_AUTHORIZED = NO`.
- `CURRENT_SELECTOR_RANK_BEFORE = 0`.
- `CURRENT_SELECTOR_RANK_AFTER_RCG008 = 0`.

The rejection counters are classifier summaries and are not intended to partition all 12 objects into mutually exclusive exhaustive bins; diagnostic, bookkeeping and synthetic-control records retain their own exact status codes.

## Independent Selector Auditor

Independent reconstruction classification:

`BLOCKED_SCOPED_RCG008_NO_EXISTING_APPLICABLE_HIGHER_ORDER_RQIR_DATUM_IN_CURRENT_AUTHORITY`

Verdict:

`CONFIRMED_SCOPED`

Auditor facts:
- `controls_ok=true`;
- `provenance_ok=true`;
- `qualifying_datum_count=0`;
- aggregate and independent classifications are identical.

## Scientific interpretation

Within the prospectively frozen RCG008 corpus and authority rules, the durable repository contains **zero** existing candidate-independent genuinely higher-order RQIR data that are already legally applicable, or already supplied with a legitimate bridge target, for testing the unique Weyl-cubed coefficient `alpha`.

This is a scoped source-authority absence result. It does **not** prove that no such RQIR datum can ever be derived or supplied. It does not falsify Weyl-cubed, and it does not authorize expansion of the gravity model class.

RCG008 is an information-supply census, not a coefficient-selection gate. Therefore:
- `A = span{alpha}`;
- `alpha = UNSELECTED`;
- inherited selector rank remains `0`;
- no RCG008 bridge is authorized.

## Claim locks

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.

`THEORY_ESTABLISHED = 0%`.

No `alpha=0`, coefficient determination, Weyl-cubed confirmation as gravity, unique gravity theory, full quantum gravity, or new-physics claim is authorized.

## Next admissible frontier

RCG008 is terminal. No RCG009/bridge/alpha-solving gate is executed here.

The next highest-information **prospective** question is upstream and source-first:

`CAN_THE_MISSING_HIGHER_ORDER_RQIR_DATUM_BE_DERIVED_FROM_EXISTING_RQIR_PRINCIPLES_WITHOUT_IMPORTING_CANDIDATE_PHYSICS?`

Any later gate must first define and freeze the candidate-independent source object and its ownership/domain before deriving a value, bridge or alpha sensitivity.
