# RCG-006 — symbolic-Lambda bulk companion terminal

Date: 2026-09-17
Status: **TERMINAL SCOPED SUBGATE**

Scientific preregistration: `fc3ff1f49c56f2befc039e09ebd8f388833dbff1`.
Canonical workflow run: `35250843261`, head `56c0b6c2614f99c5cffb84bc99d2e56b45a84e05`.

Jobs:
- Constructor `105302505383` — success;
- independent Critic `105302504869` — success;
- aggregate `105304473446` — success.

Canonical aggregate artifact: `10509439632`, digest `sha256:2a672e6b9e2cfdb0fe6f972ab0a8f14e51a1cebf43933e0c350559821fbde5d7`.
Full provenance: `results/raw/RCG006_SYMBOLIC_LAMBDA_CANONICAL.json`.

Classification:

**`PASS_SCOPED_RCG006_SYMBOLIC_LAMBDA_BULK_COMPANION`**.

## Exact result

The mechanically reconstructed parity-even curvature-squared scalar bulk companion has

**`dim Q_dim4_companion = 2`**

after quotienting the exact four-dimensional pointwise scalar span by the Euler/Gauss-Bonnet topological direction.

For the frozen algebraic generator family,

**`rank(Lambda leakage_ALG)=2`**.

Including all derivative generators does not increase the bulk leakage:

**`rank(Lambda leakage_FULL)=2`**.

The exact leakage rowspace SHA256 is
`a30969d15f4abd011e951825192c1aea3f8caf3444441d0cbca915902d4cdae5`.

Every frozen DER trace contributes zero to the bulk companion and is recorded as a boundary-sensitive total divergence.

## Interpretation

The symbolic-`Lambda` stratum therefore has a nonzero two-dimensional `Lambda * Q_dim4_companion` bulk sector that is distinct from the original eight-dimensional dimension-six L0 parent. It is tracked explicitly rather than silently projected away.

This does not change the already-terminal L0 result `rank(M_FR)=7` or `dim Q_EFT=1`.

The boundary-sensitive divergence statement is not a boundary-observable equivalence theorem.

## Ceiling

This is first-order local pure-metric bulk-action equivalence. No conclusion is promoted to matter couplings, boundary observables, global solution spaces, causal structures, quantum measures or nonperturbative transformations.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
