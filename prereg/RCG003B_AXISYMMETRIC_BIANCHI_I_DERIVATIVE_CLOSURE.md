# RCG-003B — axisymmetric Bianchi-I held-out derivative-closure gate (FROZEN)

Date: 2026-09-17
Status: **PROSPECTIVELY FROZEN BEFORE ANY RCG003B PRODUCTION EVALUATION**
Parent scientific terminal: `ded5a44078c57909aeb6592b88bdac5c0917f85d`
Parent formation preregistration: `0bba0ea6e1d4e13635f70f3b5056e131afba6c7d`
Parent workflow run: `35152559990`

## Purpose

RCG003-v0 reduced the prospectively frozen three-dimensional cubic-Ricci coefficient family to one exact ray under the homogeneous conformal no-extra-time-derivative condition:

`(lambda,mu,nu) proportional to (7,-36,36)`.

RCG003B is the highest-information next discriminator because it tests that **fixed held-out survivor** on the smallest anisotropic homogeneous geometry that can distinguish isotropic/conformal cancellation from genuine multi-degree-of-freedom derivative closure.

No coefficient refit, family enlargement, source replacement, or post-outcome basis change is allowed.

## Frozen scientific question

For the exact fixed deformation

`O_* = 7 R^3 - 36 R R_{mu nu}R^{mu nu} + 36 R_mu^nu R_nu^rho R_rho^mu`,

does the axisymmetric Bianchi-I homogeneous reduction have Euler-Lagrange equations for both independent scale variables with no third- or fourth-time derivatives for arbitrary off-shell histories?

This is a **necessary structural derivative-order test only**. It is not full nonlinear constraint closure, hyperbolicity, causality, stability, uniqueness, phenomenology, or quantum gravity.

## Frozen model inheritance

No RCG003-v0 model content is changed.

Inherited exactly:

- one Lorentzian metric `g_{mu nu}`;
- local 4D metric action representation;
- vacuum physical source `T_{mu nu}=0` only;
- no matter coupling in this gate;
- no quantum state or measure;
- no observable/prediction map;
- derivative-dependent field redefinitions forbidden in the current v0 quotient;
- historical Einstein-Hilbert term is `REFERENCE / CONTROL`, not a derived RQIRCG law;
- `chi_ABC = UNAUTHORIZED_NOT_COMPUTED`;
- theory established = **0%**.

The deformation coefficient ray is **DERIVED_SCOPED_FROM_RCG003**, while its overall nonzero amplitude/length scale remains symbolic and physically unresolved.

## Held-out geometry

Freeze the unit-lapse axisymmetric Bianchi-I ansatz

`ds^2 = -dt^2 + exp(2 a(t)) dx^2 + exp(2 b(t)) [dy^2 + dz^2]`.

The histories `a(t), b(t)` are arbitrary smooth off-shell functions. Unit lapse is a **frozen sector choice** for this derivative-order discriminator; no inference about the full lapse/constraint algebra is permitted.

The isotropic diagonal `a=b=sigma` is a positive recovery control only. Production classification must use the full independent `(a,b)` history space and may not impose `a=b`.

## Frozen generator

Use only the RCG003 deformation density

`L_*(a,b,adot,bdot,addot,bddot) = sqrt(|g|) O_*`

for the production derivative-order decision. The Einstein-Hilbert density may be evaluated separately only as a positive reference control.

The evaluator must derive the metric, Christoffel symbols, Ricci tensor/scalar and the three cubic invariants directly from the frozen ansatz using exact symbolic/rational algebra. It must not insert a precomputed anisotropic answer from GR/EFT literature or another project.

## Exact fourth-derivative criterion

Let

`q_1=a`, `q_2=b`, `v_i=dot q_i`, `u_i=ddot q_i`.

Construct the exact acceleration Hessian

`H_ij = partial^2 L_* / (partial u_i partial u_j)`.

A necessary and, together with the frozen third-derivative condition below, sufficient condition for the two reduced Euler-Lagrange equations to contain no derivatives above second order is

`H_ij == 0`

identically for all independent off-shell variables.

The evaluator must expand each independent Hessian entry as an exact polynomial/rational expression and collect all coefficients. No finite sampling may substitute for the symbolic identity test.

## Exact third-derivative criterion

If and only if `H_ij == 0`, the reduced density is at most linear in accelerations:

`L_* = A_a(a,b,adot,bdot) addot + A_b(a,b,adot,bdot) bddot + B`.

For such a second-derivative Lagrangian the coefficients of third derivatives in the Euler-Lagrange equations are controlled by the velocity-space curl

`C_ab = partial A_a / partial bdot - partial A_b / partial adot`.

Freeze the no-third-derivative condition

`C_ab == 0`

identically for arbitrary off-shell histories.

The evaluator must verify the identity by exact symbolic coefficient collection. A cancellation seen only after imposing isotropy, an equation of motion, or a special trajectory is a FAIL for this gate.

## Frozen classifier

Prerequisite controls and provenance must all be valid.

- `PASS_SCOPED_RCG003B_AXISYMMETRIC_SECOND_ORDER_DERIVATIVE_CLOSURE` iff all independent `H_ij` vanish identically **and** `C_ab` vanishes identically.
- `FAIL_SCOPED_RCG003B_AXISYMMETRIC_HIGHER_DERIVATIVE_SURVIVOR_FALSIFIED` iff provenance/controls are valid and at least one exact anisotropic Hessian or curl coefficient is nonzero.
- `BLOCKED_SCOPED_RCG003B_SYMBOLIC_REDUCTION_UNDEFINED` only if the frozen geometric object cannot be constructed without adding a new substantive assumption.
- `INVALID_RCG003B` for chronology violation, post-outcome coefficient/family change, source substitution, basis change, fitted cancellation, imported successor result masquerading as derivation, malformed exact algebra, or contaminated Critic lane.

A FAIL is a terminal scientific falsification of the **remaining nonzero deformation ray inside the current bounded RCG003-v0 family** under this held-out necessary test. It is not a no-go theorem for arbitrary nonlinear gravity.

A PASS leaves the one-dimensional ray alive; it does not establish a complete theory.

## Frozen dimension accounting

Input physical coefficient-ray dimension after RCG003 conformal closure: **1** (overall ray amplitude remains symbolic).

- If RCG003B FAIL: residual admissible nonzero ray dimension inside RCG003-v0 becomes **0** for the combined conformal + axisymmetric derivative-order requirements.
- If RCG003B PASS: residual admissible ray dimension remains **1**; the next gate must attack a different unresolved structural axis rather than refit coefficients.

No broader EFT field-redefinition quotient is introduced here.

## Prospectively frozen controls

1. **Isotropic recovery control:** substitute `a=b=sigma` into the independently derived anisotropic expressions. The fixed ray must recover the RCG003 conformal result: zero acceleration Hessian and no higher-derivative obstruction in that one-field sector.
2. **Perturbed-ray negative control:** use exactly `(lambda,mu,nu)=(8,-36,36)` only as a negative control. Its conformal acceleration Hessian must be nonzero, reproducing sensitivity to a one-unit mutation of the first coefficient.
3. **Einstein-Hilbert reference control:** its axisymmetric reduced equations must have no fourth-time-derivative Hessian obstruction. This is REFERENCE/CONTROL only.
4. **`R^2` sensitivity control:** the same held-out anisotropic machinery must detect a nonzero acceleration Hessian for `sqrt(|g|) R^2` on a generic anisotropic history/polynomial identity.
5. **Axis-label duplicate control:** swapping the singled-out spatial axis with an equivalent relabelling before imposing the two-equal-axis convention must not create a new physical coefficient ray; derivative-order classification must agree.
6. **Off-shell lock:** evaluator must reject any attempted use of equations of motion, `a=b`, constant Hubble rates, or a special trajectory in the production identity test.
7. **Source provenance:** only `VACUUM_ZERO` is admitted as production source; any unregistered external `T_{mu nu}` is rejected before evaluation.

## Independent Critic

After production outcome, an independent Critic must rederive the anisotropic highest-derivative test by a method not calling/importing the Constructor implementation and check:

- exact parent ray `(7,-36,36)` was used without refit;
- parent prereg/terminal chronology;
- no hidden Einstein/GR equation was used as a production identity;
- no isotropy or on-shell condition entered the production decision;
- Hessian and, when applicable, velocity-curl criteria are mathematically sufficient for the stated reduced derivative-order claim;
- source lock and successor firewall;
- controls distinguish positive/negative cases;
- no claim exceeds the axisymmetric homogeneous vacuum sector.

Critic may invalidate or narrow the result, but may not modify the family after seeing the outcome.

## Claim locks

Regardless of PASS or FAIL, this gate cannot establish:

- GR/Einstein dynamics as derived;
- full nonlinear diffeomorphism constraint closure;
- hyperbolicity or causal well-posedness;
- stability/unitarity;
- matter/source completion;
- global uniqueness or a no-go theorem outside the frozen family;
- quantum theory/quantum gravity;
- experimental confirmation;
- `chi_ABC`;
- new physics.

`chi_ABC = UNAUTHORIZED_NOT_COMPUTED` and theory established = **0%**.
