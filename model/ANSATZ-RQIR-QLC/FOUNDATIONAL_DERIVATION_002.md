# Foundational Derivation 002 — sector split and Gaussian-dilation no-go

**Model:** `ANSATZ-RQIR-QLC` v0.1  
**Status:** NEGATIVE / STRUCTURAL RESULT  
**Purpose:** determine whether the one-mode QLC complete-positivity saturation law is itself a model-specific gravity discriminator.

## 1. Frozen RQIR constraint from the static sector

Frozen RQIR already contains `RQIR-NG-001`: for non-overlapping source branches with a gravitational coupling/readout diagonal in the mass-configuration basis, relative phase is invisible to all static density-derived gravitational observables.

Therefore a static Newtonian potential is not an admissible place to manufacture a quantum-gravity discriminator merely by assigning it an independent canonical output algebra. The QLC construction must distinguish:

1. a **constraint/static sector**, where Newtonian potential and related clock shifts are sourced constraint/relational observables; and
2. a **dynamical/radiative sector**, where genuine gravitational quantum modes can possess a nontrivial canonical commutator algebra.

This prevents an artificial `Omega_Y` from being assigned to a nondynamical static potential solely to generate a CP noise floor.

## 2. Constraint/static sector

At weak field and low frequency the mean response remains

\[
\nabla^2\Phi=4\pi G\rho.
\]

For a density-diagonal source/readout, RQIR-NG-001 implies that source coherence invisible to the diagonal density statistics remains invisible to the static gravitational readout.

Hence:

\[
\boxed{\text{static density transfer is not the QLC quantum discriminator}}
\]

without an additional noncommuting/unequal-time structure derived from the dynamics.

A detector phase or clock readout may still be quantum, but that does not make the constrained Newtonian potential an independent quantum oscillator.

## 3. Dynamical canonical sector

Now take one physical input/output canonical mode block with

\[
\Omega_X=\Omega_Y=\Omega,
\qquad
K=\sqrt\eta\,I_2,
\qquad
0\le\eta\le1.
\]

QLC derivation 001 gave the minimum CP-compatible added covariance

\[
Y_{\min}=\frac{\hbar}{2}(1-\eta)I_2.
\]

The question is whether this relation is special to QLC.

## 4. Pure-environment unitary dilation

Introduce one environment mode `E` in a minimum-uncertainty vacuum state,

\[
V_E=\frac{\hbar}{2}I_2.
\]

Consider the canonical two-mode unitary/symplectic mixing

\[
\mathbf R_Y
=\sqrt\eta\,\mathbf R_X
+\sqrt{1-\eta}\,\mathbf R_E.
\]

Tracing over the unobserved complementary output gives

\[
\mathbf d_Y=\sqrt\eta\,\mathbf d_X,
\]

and

\[
V_Y
=\eta V_X+(1-\eta)V_E
=\eta V_X+\frac{\hbar}{2}(1-\eta)I_2.
\]

Thus

\[
\boxed{Y_G=\frac{\hbar}{2}(1-\eta)I_2=Y_{\min}}
\]

exactly.

For an amplifying canonical block, a two-mode-squeezing dilation analogously produces

\[
Y_G=\frac{\hbar}{2}(\eta-1)I_2,
\qquad \eta\ge1,
\]

again saturating the QLC bound.

## 5. Consequence

The QLC one-mode law

\[
y_{\min}=\frac{\hbar}{2}|1-\eta|
\]

is therefore a generic **quantum-limited Gaussian-channel consistency law**, not by itself a gravity-specific dynamical prediction.

A conventional quantized mediator with a pure Gaussian environment can realize exactly the same input-output relation. In a perturbative quantum-gravity/C5 setting, a selected linearized graviton sector with unitary matter-gravity dynamics can in principle supply precisely such a unitary dilation in regimes where the Gaussian mode reduction is valid.

The last statement is a comparator possibility, not yet a proof that every physical GR mode projection realizes the simple attenuator/amplifier normal form.

## 6. QG-007 discriminator no-go

The following candidate discriminator is rejected:

> `CP saturation / minimum added Gaussian noise alone distinguishes RQIR-QLC from conventional low-energy quantized gravity.`

It does not.

Formally,

\[
\boxed{
\text{QLC CP saturation}
\not\Rightarrow
\text{new gravity dynamics}
}
\]

because the same relation follows from an ordinary pure-environment Gaussian unitary dilation.

QG-007 therefore remains unresolved for the model; the previously proposed CP-floor relation cannot serve as its comparator-relative discriminator.

## 7. What RQIR says to test next

Paper-I closure gives the relevant direction. At second order,

\[
G^>=N+iD,
\qquad
G^<=N-iD,
\]

and equality of mean source data and symmetrized noise `N` does not in general imply equality of the ordered/commutator sector `D` or retarded response `chi^R`.

The next candidate discriminator must therefore involve a **joint transfer law for ordered information**, not merely covariance:

\[
(J,N,D,\chi^R,\ldots)_{\rm source}
\longrightarrow
(\text{relational gravity observables})_{\rm output}.
\]

The question is whether the interface transmits `D/chi^R` in a way that cannot be reproduced by C1/C2/C3/C5/C6 after the same calibration quotient.

## 8. New construction constraint

For all subsequent RQIR-derived candidates:

- a static density-only signal is insufficient by `RQIR-NG-001`;
- nonzero noise is insufficient by G12;
- CP saturation is insufficient by this derivation;
- entanglement alone is insufficient by frozen RQIR;
- a claimed new discriminator must survive a **joint mean + noise + ordered-response + comparator audit**.

## 9. Scientific status

This result does not reject `ANSATZ-RQIR-QLC` as an operational representation. It rejects its first proposed novelty mechanism.

The branch can remain useful as a channel-language representation of low-energy gravity, but a new-theory claim requires an additional RQIR-forced relation beyond generic Gaussian complete positivity.

## 10. Next task

Construct an ordered-response transmission matrix

\[
\mathcal K_{RQIR}: (J,N,D,\chi^R)\mapsto(\mu_Y,V_Y,R_Y,\ldots)
\]

from one coherent interface law and ask whether frozen RQIR plus conservation/causality/limits constrain this map more strongly than C5 and C3 already do.
