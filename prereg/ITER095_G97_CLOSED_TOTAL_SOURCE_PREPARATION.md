# ITER095 / G97 — closed probe+apparatus total-source preparation

Status: PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION

Purpose: construct and audit a minimal closed preparation/source model that includes probe plus support/apparatus and satisfies exact finite-dimensional conservation. This closes only the source-preparation prerequisite of the post-G96 frontier. It does NOT define RCG-002 nonlinear gravity dynamics.

Frozen model: two 1D probe coordinates x1,x2 and apparatus coordinate X with translationally invariant Lagrangian L = sum_a m_a qdot_a^2/2 - V1(x1-X)-V2(x2-X)-W(x1-x2), with symbolic differentiable potentials. Branch preparation offsets are implemented as internal equal-and-opposite impulses between each probe and apparatus, never as external holding forces.

Lanes:
A — exact Euler-Lagrange/Noether proof that total momentum P=m1 x1dot+m2 x2dot+M Xdot is conserved for arbitrary differentiable V1,V2,W.
B — exact force-balance decomposition showing probe-only momentum is generically not conserved while apparatus contribution cancels it; frozen omitted-apparatus control must fail.
C — branch-preparation impulse map: verify exact total-momentum preservation for independent internal impulses I1,I2 and exact invertibility back to pre-kick state.
D — adversarial external-hold control: add Uext=lambda X and show total momentum acquires nonzero source -lambda; verify lambda=0 restores closure. Also test invariance under common coordinate translation.

Terminal ceiling: `PASS_CLOSED_TOTAL_SOURCE_PREPARATION_CONSERVATION_SCOPED` if all exact identities and controls pass. This is classical preparation/source bookkeeping only. It is not a nonlinear gravitational law, not Bianchi closure, and not a claim of new physics. Readiness remains 66%; theory established 0%.
