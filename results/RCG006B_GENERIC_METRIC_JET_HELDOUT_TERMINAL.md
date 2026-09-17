# RCG-006B — exact generic metric-jet held-out terminal

Date: 2026-09-17
Status: **TERMINAL SCOPED VALIDATION SUBGATE**

Held-out preregistration: `43748579a78f40e0825d5ae01dc634d55ba7b928`.
Execution contract: `da1d1795a6ecf885a7f52a717d4979d962002240`.
Parent canonical L0 map: `12ca52947d1390a494634b7a6a2d98d9a7e4bf7d`.

Canonical workflow run: `35252660085`, head `55d2ddfe5d84a4e56857c9b7fd12719ca5e9dc43`.

Jobs:
- Constructor `105308517011` — success;
- independent Critic `105308516603` — success;
- aggregate `105309021032` — success.

Artifacts:
- Constructor `10512235030`, digest `sha256:3e2aae5e76a26e94b198fea87b0a71720f7c70df3e3ca07df371148195334fe7`;
- Critic `10511351333`, digest `sha256:88771fff0a384122d28998936256752e5666221731c481da0cbc3f32da63c815`;
- aggregate `10512270339`, digest `sha256:28ddcc30af07e038f757cf7cff643f60b0514bda3e6bdd87e1909d58258e375a`.

Canonical raw/provenance: `results/raw/RCG006B_HELDOUT_CANONICAL.json`.

Classification:

**`PASS_SCOPED_RCG006B_GENERIC_METRIC_JET_HELDOUT`**.

## Frozen exact banks

Constructor bank:
- seed `0x5243473030364341`;
- `32` samples;
- SHA256 `177a36c97b88420d7e24001403ea77a247e8c0b6be20f58246ac811c2eaa184e`.

Critic bank:
- seed `0x5243473030364352`;
- `32` samples;
- SHA256 `34f866a046f80cd38694fe0c28cca37597dd215b874078e6990523073347c23b`.

Final independent cross-route bank:
- seed `0x524347303036484f`;
- `16` samples;
- SHA256 `3dfffc6e2e29e4676e10681118271bd07ba81ab5c0684ae8db8607fd18c6500b`.

Coordinate manifests agree exactly:
- generic curvature coordinates: `20`, SHA256 `5ee3545c598d88d73925c8e3fb60240f30bc97a4b2be0dcf603eedd24e49730b`;
- fourth metric-jet coordinates: `350`, SHA256 `59060f106ee42b04f5831f511f6b1e84f4cacac2b89a48f15b30a5ec1fa3eb88`.

## Exact validation counts

Each 32-sample independent bank validated exactly:
- `288` frozen production-generator direct tensor comparisons;
- `18,720` alternate-generator relation evaluations;
- `288` first-order EH raw-image evaluations;
- `32` sample-derived final quotient-map combinations.

The common 16-sample final bank independently validated:
- `144` direct tensor comparisons;
- `9,360` alternate-representation relations;
- `144` first-order EH action images;
- `16` final quotient combinations.

Every comparison was exact rational equality; no tolerance or refit was used.

All frozen negative controls were detected in both lanes: wrong EH Ricci sign, perturbed M_FR column and perturbed generator coefficient.

The held-out independently retains the canonical M_FR SHA256
`7ac6ba6d1003c676899c0017409e3466a7f5e12fbb4114feee94580f1b0799bd`.

## Interpretation ceiling

This validates the frozen implementation on prospectively fixed exact rational banks. It does not turn finite held-out sampling into a universal tensor-identity theorem; universal identities remain supported by the exact coefficient/relation matrices of the parent gates.

The held-out introduces no new physical claim and does not reclassify RCG005.

With RCG006 generator completeness, L0 map, A_HD transport, symbolic-Lambda companion and this held-out all terminal, the frozen RCG006-v0 structural audit is now eligible for terminal assembly under its preregistered classifier.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
