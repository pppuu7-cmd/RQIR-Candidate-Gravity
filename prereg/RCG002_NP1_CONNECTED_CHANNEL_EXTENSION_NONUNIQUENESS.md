# RCG002-NP1 — connected-channel extension nonuniqueness theorem

Status: PROSPECTIVELY FROZEN BEFORE SYMBOLIC EXECUTION
Date: 2026-09-14
Frozen base main: `94467fdacc93f65102333fa01b7a34bb0d857a79`

## Purpose
Test whether the already-authoritative RCG-002 operational channel requirements, NCP1 positivity constraints, and G97 closed-source translation/conservation structure are sufficient to fix a nonlinear connected three-source extension, or whether a continuum of inequivalent normalized CPTP extensions remains.

This gate does NOT propose a gravitational interaction, import another candidate programme, or select any coefficient. It is a sufficiency/underdetermination theorem for the current RCG-002 operational architecture.

## Frozen object
Branch set `B={0,1}^3`. Write `b=(a,b,c)` and define the connected indicator `q(b)=a*b*c`.

Let `F0` be any normalized positive-semidefinite Schur kernel on `B` whose restrictions to every coordinate face (`a=0`, `b=0`, or `c=0`) reproduce the already-fixed lower-order RCG-002 channel on that face. No explicit microscopic formula for `F0` is assumed.

For real `lambda` and `gamma>=0`, define

`C_{lambda,gamma}(x,y)=exp(i*lambda*(q(x)-q(y))) * exp(-gamma*(q(x)-q(y))^2)`

and the extension

`F_{lambda,gamma}=F0 .* C_{lambda,gamma}`

(entrywise/Schur product).

The family is a mathematical adversarial completion, not candidate-owned physics.

## Frozen questions
1. Is `C_{lambda,gamma}` normalized PSD for all real lambda and gamma>=0?
2. Therefore, by the Schur product theorem, is `F_{lambda,gamma}` normalized PSD whenever `F0` is?
3. Are all one-/two-source coordinate-face restrictions exactly unchanged?
4. Does lambda shift the genuine three-source phase finite difference while every <=2-body rephasing has zero third finite difference?
5. Does gamma change connected coherence magnitudes while leaving every coordinate face unchanged, providing an independent nonunitary direction?
6. Do both directions commute with the G97 total translation generator when branch labels are internal and spatial translations act only on source/apparatus coordinates?
7. Can the same operational family be generated over a finite laboratory time by a time-local branch Hamiltonian plus a random-unitary connected dephasing factor, showing that ordinary finite-time normalized evolution alone does not select lambda or gamma? This is NOT a relativistic locality/Bianchi claim.
8. Does current RCG-002 authority contain an independent principle fixing or eliminating lambda/gamma without inspecting the desired connected-phase outcome?

## Independent lanes
A — exact PSD/CPTP construction. Prove `C` is a Gram/characteristic-function kernel and prove normalized Schur-product preservation. Positive control gamma=0 must reduce to a diagonal unitary. Negative control: replace the damping factor by an explicitly non-positive 3x3 correlation minor and verify failure.

B — exact face/Moebius theorem. Verify `C=1` on every coordinate face; derive the third finite difference of the connected phase and show every polynomial phase of total degree <=2 has zero third finite difference. Verify lambda cannot be removed by lower-body rephasing. Verify gamma changes only coherences crossing the `q=1` vs `q=0` partition and is independent of lambda.

C — G97 symmetry and finite-time operational dilation. Model total translation generator `P_tot` acting on source/apparatus coordinates and connected projector `Q=|111><111|` acting on internal branch labels; verify `[P_tot,Q]=0`. Derive a finite-time unitary `exp(i lambda Q)` from any real time profile with fixed integral and derive Gaussian random-unitary dephasing `E_X[e^{i X Q} rho e^{-i X Q}]` with `Var(X)=2 gamma`. This lane establishes only abstract finite-time CPTP evolution and translation compatibility, not spacetime microcausality or gravity.

D — candidate-ownership and anti-rescue audit. Read the RCG-002 seed, construction contract, current recovery, G93/G97/NCP1 terminal authority, and candidate-owned baseline. Search only RQIR-CG authority for a rule that prospectively fixes connected phase/noise hierarchy. Classify every relevant requirement as `DERIVED_FROM_RCG002`, `ALLOWED_BUT_NOT_SELECTED`, or `REQUIRES_NEW_PRINCIPLE`. No external theory may be used as the selecting rule.

## Frozen classifications
- `PASS_CURRENT_PRINCIPLES_FIX_CONNECTED_EXTENSION_SCOPED` only if an already-authoritative RCG-002 principle eliminates all nontrivial lambda/gamma freedom without adding new dynamics and A-C remain consistent.
- `RCG002_CURRENT_PRINCIPLES_ALLOW_CONTINUUM_CONNECTED_CHANNEL_EXTENSIONS_SCOPED` if A-C prove at least two independent face-preserving CPTP directions and D finds no already-authoritative selector.
- Overall physical classification in that case: `RCG002_REQUIRES_NEW_NONLINEAR_PRINCIPLE`.
- `INVALID_IMPLEMENTATION` if exact controls fail or the implemented family does not match this freeze.
- `BLOCKED_AUTHORITY_AMBIGUITY` if repository authority is internally inconsistent about whether a selector has already been adopted.

## Interpretation ceiling
A nonuniqueness result proves insufficiency of the current operational/channel/source-conservation principles, not nonexistence of a future nonlinear RCG-002 theory. The family itself is not a gravitational theory. Translation invariance is not Bianchi closure. Finite-time time-local evolution is not relativistic microcausality. Operational CPTP is not diffeomorphism invariance. No claim about all classical, semiclassical, stochastic, EFT or quantum-gravity models is authorized.

Readiness remains 66%; theory established remains 0%.

## Exact downstream rule
If continuum nonuniqueness survives, do not fit lambda/gamma and do not launch another rank/cumulant scan. The next admissible step is a candidate-version decision: identify an independently motivated new nonlinear source/state/evolution principle, prospectively freeze it, and then test conservation/Bianchi/causality/observable recovery in one realization. If no such principle exists, current RCG-002 remains an operational weak-field/interface architecture rather than a physically determined nonlinear theory.
