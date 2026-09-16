# RCG003B active execution marker

Date: 2026-09-17
Status: **CANONICAL SCIENTIFIC RUN EXISTS / ACTIONS QUEUED / NO DUPLICATE RUN AUTHORIZED**

Canonical gate:
`RCG003B_AXISYMMETRIC_BIANCHI_I_DERIVATIVE_CLOSURE`.

Frozen preregistration:
`dbb0b54465c628b533c646a5b3b74b8458eaf24e`.

Parent RCG003 terminal:
`ded5a44078c57909aeb6592b88bdac5c0917f85d`.

Frozen implementation commits:
- Constructor `f7353512a31bdee081e63dc832a675ec16987121`;
- independent Critic `49ea8d43f1dbca0e5212a67314cba9d5226a087c`;
- direct Euler–Lagrange cross-check `b8dbe1c00fc7ad32444f682309526b3116ca9ede`;
- frozen aggregate `7989f4ace99d5efc6432f8ac41a7cb42eb0c98b0`;
- workflow head `241a923523b2c770ffc8c48315d931af6e61846f`.

Canonical Actions run:
`35156147876`.

At the time this marker was written, Constructor, Critic and Euler cross-check jobs were all still `queued` and no workflow artifact existed. This is an infrastructure/provenance state only, not a scientific PASS/FAIL/BLOCKED/INVALID classification.

A separate nonterminal exact local reproduction is preserved at:
`results/RCG003B_PRETERMINAL_LOCAL_REPRODUCTION_PENDING_ACTIONS.md`, commit `ebceb96009770594c7dd3edb9ce168693d670d5a`.

That local reproduction identifies a candidate anisotropic higher-derivative obstruction, but it is explicitly noncanonical until the frozen Actions run and artifacts are consumed.

## Anti-duplicate lock

Do **not** create another RCG003B preregistration, workflow, or scientific run merely because run `35156147876` is queued.

Exact next action:

`CONSUME_EXISTING_RCG003B_RUN_35156147876_WHEN_TERMINAL_AND_APPLY_FROZEN_CLASSIFIER`.

No coefficient refit, family enlargement, source change, basis search, isotropic fallback, or downstream RCG003C gate is authorized before RCG003B terminalization.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
