# RCG003B operator-obstruction postmortem

Date: 2026-09-17
Status: **RETROSPECTIVE DESCRIPTIVE ANALYSIS OF AN ALREADY-TERMINAL RCG003B RESULT**

This record does **not** define RCG004, change the frozen RCG003B classifier, refit `(7,-36,36)`, or add model content. It decomposes the already-authorized and already-falsified RCG003-v0 ray into its three frozen Ricci-cubic operator contributions.

Parent terminal:
`72f9ab2ab5ad85259a18fc1f368777c431a56324`.

Parent classification:
`FAIL_SCOPED_RCG003B_AXISYMMETRIC_HIGHER_DERIVATIVE_SURVIVOR_FALSIFIED`.

Reproducibility script:
`scripts/rcg003b_operator_obstruction_postmortem.py`.

Script commit:
`0daac3f8e7d182c52e2edf61d2f836881673cc2c`.

Raw exact record:
`results/raw/RCG003B_OPERATOR_OBSTRUCTION_POSTMORTEM.json`.

Raw commit:
`b214b5db6cd693f68f2a0617e94bcc8649c98454`.

Payload SHA256:
`cb8b356739230e11af13f9bb1368255fa0fa2ccaeba8e5ea7765766d29192bdb`.

## Frozen operator contributions in `(a,b)` variables

The production deformation remains exactly

`7 R^3 - 36 R R_{mu nu}R^{mu nu} + 36 R_mu^nu R_nu^rho R_rho^mu`.

After removing the common nonzero density `exp(a+2b)`, the weighted acceleration-Hessian contributions are:

### `7 R^3`

`H_aa = 336*(ua + 2*ub + va^2 + 2*va*vb + 3*vb^2)`

`H_ab = 672*(ua + 2*ub + va^2 + 2*va*vb + 3*vb^2)`

`H_bb = 1344*(ua + 2*ub + va^2 + 2*va*vb + 3*vb^2)`.

Its isotropic pullback contribution is

`9072*(u + 2*v^2)`.

### `-36 R Ricci^2`

`H_aa = -288*(3*ua + 4*ub + 3*va^2 + 4*va*vb + 5*vb^2)`

`H_ab = -288*(4*ua + 7*ub + 4*va^2 + 5*va*vb + 9*vb^2)`

`H_bb = -288*(7*ua + 18*ub + 7*va^2 + 10*va*vb + 25*vb^2)`.

Its isotropic pullback contribution is

`-5184*(3*u + 5*v^2)`.

### `36 Tr(Ricci^3)`

`H_aa = 432*(ua + ub + va^2 + va*vb + vb^2)`

`H_ab = 432*(ua + 2*ub + va^2 + 2*vb^2)`

`H_bb = 432*(2*ua + 5*ub + 2*va^2 + va*vb + 6*vb^2)`.

Its isotropic pullback contribution is

`1296*(5*u + 6*v^2)`.

The three isotropic pullback pieces cancel exactly:

`9072*(u+2v^2) - 5184*(3u+5v^2) + 1296*(5u+6v^2) = 0`.

This recovers the earlier conformal cancellation without changing its scope.

## Volume/shear coordinates expose the mechanism

Introduce the exact invertible change of variables

`a = sigma + 2 beta`,

`b = sigma - beta`.

Thus `sigma` is the common volume/isotropic direction and `beta` is the axisymmetric shear direction.

For the complete frozen ray, the transformed acceleration Hessian is

`H_sigma_sigma = 0`,

`H_sigma_beta = -1296*(u_beta + 3*v_beta*v_sigma)`,

`H_beta_beta = 1296*(u_beta - u_sigma - 2*v_beta^2 + 3*v_beta*v_sigma - v_sigma^2)`.

The strongest explanatory fact is therefore:

**the conformal/volume acceleration direction has `H_sigma_sigma = 0` identically, while the discarded shear directions carry the obstruction.**

This is stronger and more precise than merely saying that the axisymmetric Hessian is nonzero.

## Operator anatomy in volume/shear variables

The individual weighted contributions are:

### `7 R^3`

`H_sigma_sigma = 9072*(u_sigma + v_beta^2 + 2*v_sigma^2)`

`H_sigma_beta = 0`

`H_beta_beta = 0`.

Thus this operator contributes only to the volume-volume acceleration Hessian in this representation.

### `-36 R Ricci^2`

`H_sigma_sigma = -5184*(3*u_sigma + 4*v_beta^2 + 5*v_sigma^2)`

`H_sigma_beta = -2592*(u_beta + 3*v_beta*v_sigma)`

`H_beta_beta = -2592*(u_sigma + v_beta^2 + 2*v_sigma^2)`.

### `36 Tr(Ricci^3)`

`H_sigma_sigma = 1296*(5*u_sigma + 9*v_beta^2 + 6*v_sigma^2)`

`H_sigma_beta = 1296*(u_beta + 3*v_beta*v_sigma)`

`H_beta_beta = 1296*(u_beta + u_sigma + 3*v_beta*v_sigma + 3*v_sigma^2)`.

The frozen coefficients therefore cancel the complete `sigma-sigma` channel exactly, but they do **not** cancel the mixed and shear channels.

## Isotropic background versus conformal restriction

Set the background shear jet to zero:

`v_beta = 0`, `u_beta = 0`.

Then

`H_sigma_sigma = 0`,

`H_sigma_beta = 0`,

but

`H_beta_beta = -1296*(u_sigma + v_sigma^2)`.

Therefore even on an isotropic background, an anisotropic acceleration perturbation sees a generically nonzero Hessian. The conformal calculation passed because it **removed the shear degree of freedom from the configuration space**, not because the full two-field acceleration Hessian vanished on isotropic histories.

This gives a precise mechanism for the RCG003 -> RCG003B transition:

`CONFORMAL CANCELLATION = exact cancellation in the volume direction`

while

`AXISYMMETRIC FAIL = surviving shear/mixed higher-derivative obstruction`.

## Scientific interpretation lock

This postmortem does not weaken or strengthen the terminal classifier; it explains it.

The scoped dimension accounting remains

`3 -> 1 -> 0`

inside the frozen RCG003-v0 family and frozen conformal + axisymmetric derivative-order tests.

No conclusion here applies to a broader Riemann-containing cubic class because RCG004 formation remains unauthorized.

No coefficient search was performed.
No new operator was added.
No source change was made.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED`.
`THEORY_ESTABLISHED = 0%`.
