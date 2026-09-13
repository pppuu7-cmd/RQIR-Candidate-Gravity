# Iter064 / G66 — conserved-source gauge-sector independence / Ward audit (FROZEN)

Prospectively preregistered on 2026-09-13 before implementation or production output.

## Question
Within the already-qualified G65 full conserved-source linearized response, do arbitrary frozen longitudinal gauge-sector additions vanish exactly on conserved sources, so that the G61–G65 source response is independent of these gauge-sector choices?

## Frozen object
Use `eta=diag(-1,1,1,1)`, the same momenta `k1=(1,2,3,4)`, `k2=(2,-1,1,3)`, `k3=(3,1,-2,4)`, and exact rational arithmetic. For a covariant symmetric source `T`, define `V_n=k^a T_an` and `S=k^a k^b T_ab`. Frozen longitudinal contamination family:
`Q_mn(alpha,beta,gamma)=alpha(k_m V_n+k_n V_m)+beta k_m k_n S/k2+gamma eta_mn S`.
For a truly conserved source `V=0`, hence every member of the frozen family must vanish exactly.

Gauge-parameter panel: `(0,0,0),(1,2,-1),(-3,1,4),(5,-2,3),(1/2,-3/2,5/3),(-7/3,2/5,11/4)`.
Use the G65 coefficient rays and `z={1/5,2/3,5/4}` for non-singular physical-response lanes.

## A — exact Ward annihilation
For all three momenta and at least 10 deterministic transverse-projected held-out symmetric sources, require exact conservation and exact `Q=0` for every frozen gauge-parameter tuple.

## B — held-out response invariance
For every non-singular frozen `(a,b,z)` lane and every gauge tuple, require exact equality between the G65 physical response and `physical response + Q` on the same held-out conserved sources. No fitting or retuning.

## C — discrete Lorentz covariance
Using the G65 metric-preserving signed-spatial permutation/time-reversal panel, require exact covariance of `Q` and exact preservation of its zero action on transformed conserved sources.

## D — controls
Require all controls to be detected: (1) generic nonconserved sources produce nonzero `Q` for at least one nonzero gauge tuple; (2) an intentionally wrong non-longitudinal contamination `Qwrong_mn=eta_mn * theta^{ab}T_ab` does not generically vanish on conserved sources; (3) using covariant `k_m` instead of contravariant `k^m` in the conservation test is caught by at least one frozen source/momentum case.

## Aggregate
PASS iff A/B/C/D are all valid and pass. Allowed PASS classification only:
`FOUR_DERIVATIVE_LINEARIZED_CONSERVED_SOURCE_GAUGE_SECTOR_INDEPENDENCE_SCOPED`.
A valid predicate violation is `SCIENTIFIC_FAIL`; malformed artifacts are `INFRASTRUCTURE_OR_ARTIFACT_INVALID`.

## Claim ceiling
PASS is only an exact linearized Ward/gauge-sector robustness result for the frozen conserved-source response. It does not establish physical ghosts, instability, unitarity failure, coefficient selection, nonlinear consistency, or a global no-go theorem. Readiness remains 66%; theory established remains 0% unless separately authorized.
