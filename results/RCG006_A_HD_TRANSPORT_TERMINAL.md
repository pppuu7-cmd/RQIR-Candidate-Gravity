# RCG-006 — higher-derivative discriminator transport terminal

Date: 2026-09-17
Status: **TERMINAL SCOPED SUBGATE**

Scientific preregistration: `fc3ff1f49c56f2befc039e09ebd8f388833dbff1`.
Parent L0 map terminal: `results/RCG006_MFR_L0_MAP_TERMINAL.md`, commit `12ca52947d1390a494634b7a6a2d98d9a7e4bf7d`.

Canonical workflow run: `35250686885`, head `7af702935db7db904f08a0e70e6f8187dc61d859`.

Jobs:
- Constructor `105301992374` — success;
- independent Critic `105301992123` — success;
- aggregate `105304230776` — success.

Canonical aggregate artifact: `10508814385`, digest `sha256:50f70b19724d8d0930ce8154f0f1c94221bac6493267b1e4467e08beb653b8af`.
Full provenance is persisted in `results/raw/RCG006_A_HD_TRANSPORT_CANONICAL.json`.

Classification:

**`PASS_SCOPED_RCG006_FIELD_REDEFINITION_DISCRIMINATOR_NONINVARIANT`**.

## Exact result

The frozen parent higher-derivative discriminator satisfies

**`rank(A_HD)=8`**

on the eight-dimensional RCG005 parent quotient, hence

**`ker(A_HD)={0}`**.

Canonical `A_HD` SHA256:
`a3a5759ba1fbf3fa7824e79c72776adb70aa98bd7679d262e869089c005e9907`.

For the canonical first-order field-redefinition image,

`rank(M_FR)=7`

and

**`rank(A_HD M_FR)=7`**,

with image-kernel dimension exactly `0`.

Canonical transported-map SHA256:
`c741af0c5bd243114fe5e6e782edf11d08e433720fcde9cf46d1f24754964f12`.

Frozen structural branch:

**`CASE_II_NONINVARIANT`**.

Therefore every nonzero admitted first-order EH field-redefinition image direction is nonzero under the frozen representative-level higher-derivative discriminator, despite being zero in the first-order EFT quotient.

The repository now has explicit examples of the preregistered structural status

`REPRESENTATIVE_NONZERO / EFT_QUOTIENT_ZERO`.

## Scientific interpretation

The RCG005 representative-level condition “this nonzero correction has higher-than-second-order reduced equations” is not invariant under the admitted first-order local perturbatively invertible metric field-redefinition orbits.

This does not invalidate or rewrite the RCG005 terminal: RCG005 remains a correct scoped classification under its frozen representative-level convention. RCG006 identifies a limitation of promoting that representative-level discriminator to an EFT-equivalence-class statement.

The quotient-aware frozen second-order space remains zero because `ker(A_HD)={0}`; field redefinition does not manufacture a nonzero second-order correction.

## Ceiling

This is a first-order local pure-metric bulk-action result. It establishes neither boundary-observable equivalence nor matter-coupled, causal, global-solution, quantum-measure or nonperturbative equivalence.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
