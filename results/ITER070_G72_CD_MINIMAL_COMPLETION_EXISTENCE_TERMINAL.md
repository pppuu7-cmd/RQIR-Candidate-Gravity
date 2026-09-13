# Iter070 / G72 — C/D minimal completion existence — terminal

Date: 2026-09-13

## Frozen gate
Preregistration: `7c4d928517b7695a647d1a10f1eb9a956a87666d`
Implementation: `330c9398c7e3f11cfbf28d1496932496e92ec86e`
Initial production head: `ac89c7ab9f4aa05551ad89c551cab5990be02a5e`
Initial run: `34773142384`

Frozen interpretation ceiling: existence witnesses only. No architecture selection and no candidate gravity law.

## Initial run classification
C1, D1 and D2 were scientifically valid scoped PASS lanes. C2 terminated before artifact upload because the implementation declared the momentum variable `z` positive, while the preregistered polynomial negative control `1+a z` requires the finite root `z=-1/a`. The frozen aggregate therefore returned `INFRASTRUCTURE_OR_GATE_INVALID`, not a scientific FAIL.

Validated initial raw artifacts:
- C1 job `103766296225`, artifact `10322009009`, digest `sha256:282869cec38e11e15b4e381caba4813642262deb82a53f4b805fb15483ad3c8f`: `C_MINIMAL_WARD_COMPLETION_EXISTS_SCOPED`.
- D1 job `103766296243`, artifact `10322492558`, digest `sha256:4adb59042704a71b0dc82119278d9af4c25b07566aa7894fdaefc36c8103785a`: `D_MINIMAL_RETARDED_CUBIC_SUPPORT_EXISTS_SCOPED`.
- D2 job `103766296127`, artifact `10322458302`, digest `sha256:56fd9c603f6ce7262e57a87974442b9621c01a2a0165d291bea2b6855c5da487`: `D_RETARDED_CUBIC_HESSIAN_COMPATIBLE_WITH_G71_SCOPED`.
- Initial aggregate job `103766330205`, artifact `10322841411`, digest `sha256:753f4bac8c35133f793a760feb40b66f9e5c635d2dbdbf82fa0e6575ee93fe06`: `INFRASTRUCTURE_OR_GATE_INVALID`, found C1/D1/D2 only.

## Control-only repair
Causal failure: SymPy domain assumption, not frozen science. Commit `e0d55cf86742cdba6198ad298f65fe565b7cf43e` removed only the erroneous positivity assumption on `z`; the preregistered target, factor, polynomial control, thresholds and interpretation rule were unchanged. Valid C1/D1/D2 artifacts were reused without recomputation.

Recovery workflow commits: `2a79aed687b25381b0ba4814d456e330c1e55b06`, launch head `332773ca1f4e7cb7e447b321f2816b199432e796`.
Recovery run: `34776292245`; job `103774910076`.

Recovered C2 artifact `10324140766`, digest `sha256:2e796de3c027e8350ac99217a01653385826514669815d91efa71f9739e7c3de`:
- `F(0)=1`;
- `exp(-ell2*z)` has empty finite complex zero set;
- polynomial control root is exactly `-1/a`;
- classification `C_MINIMAL_POLEFREE_FACTOR_COMPLETION_EXISTS_SCOPED`.

Frozen aggregate recovery artifact `10323627498`, digest `sha256:9dcee4947e89222c48247043cd3114b316371770a51b9a583edc42c599ae31a2`.

## Scientific classification
`CD_ORTHOGONAL_MINIMAL_COMPLETIONS_EXIST_NO_UNIQUE_SELECTION_SCOPED`

Both remaining G71 Pareto architectures admit the prospectively frozen minimal completion witnesses:
- C admits the tested transverse/Ward embedding and the tested entire pole-free factor witness;
- D admits the tested retarded cubic-support/CTP normalization construction and remains compatible with G71 zero-Hessian/nonzero-cubic structure.

This does **not** select C or D, does not establish either completion as the RCG-002 law, and does not establish nonlinear generally covariant dynamics, quantum measure closure or new physics.

Programme readiness remains **66%**. `THEORY_ESTABLISHED=0%`.
