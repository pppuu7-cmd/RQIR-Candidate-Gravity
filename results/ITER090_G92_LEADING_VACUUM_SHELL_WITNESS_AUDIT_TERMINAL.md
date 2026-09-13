# Iter090 / G92 — leading Einstein-vacuum shell witness audit — TERMINAL

Date: 2026-09-14

## Terminal classification
`BLOCKED_G90_G91_RICCI_ONLY_COVARIANT_WITNESSES_VANISH_ON_FROZEN_LEADING_EINSTEIN_VACUUM_SHELL_SCOPED`

Scientific status: `BLOCKED_ON_SHELL_ROBUSTNESS_SCOPED`.

## Authority
- preregistration: `c496340c8ec85a89da6712f76dc1221f113ded3b`
- implementation: `80f544c64ebdf4f869a39991ce4b1d9e8fca3d4d`
- production head: `b82d58d3e016ef313873af57216d8f2fb103096b`
- run: `34785342844`
- aggregate job: `103799717386`
- aggregate artifact: `10326675920`
- aggregate digest: `sha256:cf9cebafd56a337428850d9641a4e65b1e3d739947259b1afc2696e32d023b20`

Raw artifacts consumed before classification:
- A `10326317970`, digest `sha256:e8bb055602b472f0b253773a3079bcfa4965956bff8e31c3a8b30e23b160786a`
- B `10325699864`, digest `sha256:6a2dda29e948e4ec062a9c65700980170a627f0080267f4505ae521a2f390c60`
- C `10326611062`, digest `sha256:ff89ae570dcefd7f3d5d1167f6dc1a0442ce701ce183b87e6f3ed53e54360fc6`
- D `10325968546`, digest `sha256:969c91df0cb9eeceeebb9622426825b7a5a5853656e3df8737639b37e6380e6a`

## Frozen-lane validation

### A — C shell projection
`J1=R^3` and `J2=R Ricci2` are exactly zero under `R=Ricci2=0`; all frozen nonzero linear combinations are also exactly zero. Classification:
`C_G90_RICCI_ONLY_WITNESSES_VANISH_ON_LEADING_EINSTEIN_VACUUM_SHELL_SCOPED`.

### B — D shell projection
`K1=R^4` and `K2=R^2 Ricci2` are exactly zero under the same shell; all frozen nonzero linear combinations are exactly zero. Classification:
`D_G91_RICCI_ONLY_WITNESSES_VANISH_ON_LEADING_EINSTEIN_VACUUM_SHELL_SCOPED`.

### C — independent curvature control
All frozen trace-free spectra have zero trace and nonzero `W3` and `W4`; the zero spectrum gives `W2=W3=W4=0`. Hence Ricci-flatness does not algebraically force all higher-curvature information to vanish inside this frozen control. Classification:
`RICCI_FLAT_SHELL_DOES_NOT_FORCE_ALL_ALGEBRAIC_WEYL_INVARIANTS_ZERO_SCOPED`.

### D — false-positive controls
Generic off-shell substitutions make both C and D witness families nonzero; `R=0` zeros the specific frozen Ricci-only families; a constant invariant remains nonzero on shell and is not falsely classified as shell-vanishing. Classification:
`VACUUM_SHELL_AUDIT_FALSE_POSITIVE_CONTROLS_SCOPED`.

## Scientific meaning
G90/G91 remain valid explicit **off-shell** local covariant underdetermination witnesses. G92 qualifies them: their exact Ricci-only invariant pairs do not furnish independent deformation directions after restriction to the frozen leading Einstein-vacuum shell. This strengthens the requirement that any next nonlinear selector/completion analysis use genuinely new candidate-owned information and not treat the G90/G91 Ricci-only pairs as physical on-shell directions.

The frozen Weyl-spectrum control shows only that non-Ricci higher-curvature information can remain algebraically nonzero on the same shell. It is not a 4D tensor-realizability theorem and does not select any Weyl/Riemann operator as RCG-002 dynamics.

## Interpretation ceiling
This result does **not** prove the full RQIRCG nonlinear shell is Ricci-flat, does not prove all Ricci-containing operators are physically redundant, does not establish S-matrix/field-redefinition equivalence, does not provide a complete operator quotient, and does not select a unique nonlinear law.

Readiness remains **66%**. `THEORY_ESTABLISHED=0%` remains locked.

## Next admissible scientific question
Do the candidate's own operational controlled-phase data supply a genuinely higher-order nonlinear selector at all? A high-information next gate should test a candidate-owned connected multi-source phase/observable that cancels inherited one- and two-body phase information, then require an explicit candidate-owned map from at least two nonlinear completion directions into that observable before any coefficient selection is authorized. If that map is absent, the correct result is `BLOCKED_MISSING_CANDIDATE_OWNED_DATUM`, not an invented selector.
