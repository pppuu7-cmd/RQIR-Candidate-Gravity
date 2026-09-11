# C5 Witness Q1/Q4 — Relational quantum clock channel in the weak-field domain

**Status:** EXPLICIT LOW-ENERGY WITNESS CONSTRUCTION  
**Comparator:** C5 perturbative quantum GR/EFT  
**Purpose:** test Q1, Q2, Q4, and parts of G1/G5/G6/G8 without claiming novelty.

## 1. Domain and metric

Use a controlled weak, slowly varying field and retain the standard Newtonian-order metric

\[
ds^2= -\left(1+\frac{2\Phi}{c^2}\right)c^2dt^2
+\left(1-\frac{2\Phi}{c^2}\right)d\mathbf x^2
+O(c^{-4}).
\]

For a clock approximately at rest along a worldline segment,

\[
d\tau
=dt\sqrt{1+2\Phi/c^2}
=dt\left(1+\frac{\Phi}{c^2}\right)+O(c^{-4}).
\]

The physical observable is not the coordinate value of `Phi` alone but a proper-time/phase comparison between clock histories whose endpoints and controls are specified relationally.

## 2. Internal clock coupling

Let the clock internal Hamiltonian be

\[
H_c=\sum_n E_n |n\rangle\langle n|.
\]

Evolution with respect to the reference coordinate time is, to Newtonian order,

\[
H_{c,\mathrm{eff}}
=H_c\left(1+\frac{\Phi}{c^2}\right),
\]

so the gravitational interaction is

\[
H_{\mathrm{int}}
=\frac{H_c\Phi}{c^2}.
\]

For a two-level clock with gap `Delta E = hbar omega_0`, the gravitational phase shift over duration `T` is

\[
\delta\varphi
=\omega_0\int_0^T dt\,\frac{\Phi(t)}{c^2}.
\]

This is the standard gravitational-redshift/proper-time coupling written as an operational clock phase.

## 3. Quantum source

In the C5 weak-field sector, the source state need not be replaced by a classical mixture. In a quasi-static branch basis `|s>` with branch-dependent Newtonian potential at the clock position,

\[
\hat\Phi(\mathbf x_c)|s\rangle
\simeq \Phi_s(\mathbf x_c)|s\rangle.
\]

For a localized source branch centered at `X_s`,

\[
\Phi_s(\mathbf x_c)\simeq -\frac{GM}{|\mathbf x_c-\mathbf X_s|}
\]

outside the source support.

The joint source-clock interaction is therefore

\[
H_{SC}
=\frac{H_c\otimes\hat\Phi(\mathbf x_c)}{c^2},
\]

which is linear in the quantum state at the fundamental Hilbert-space level; no nonlinear state-dependent source rule has been introduced.

## 4. Joint unitary and branch phases

For approximately constant branch potentials during `T`,

\[
U(T)
\simeq
\sum_s |s\rangle\langle s|\otimes
\exp\left[-\frac{iT}{\hbar}H_c
\left(1+\frac{\Phi_s}{c^2}\right)\right].
\]

For a source superposition

\[
|\psi_S\rangle=\sum_s a_s|s\rangle
\]

and an internal clock superposition, the final state is generally entangled:

\[
|\Psi(T)\rangle
=\sum_s a_s|s\rangle\otimes U_s(T)|\psi_c\rangle.
\]

Thus Q2 is realized directly: coherent source branches remain coherent in the underlying C5 dynamics.

## 5. Reduced clock channel

If the source is unobserved, tracing it out gives an explicit CPTP map

\[
\mathcal E_T(\rho_c)
=\mathrm{Tr}_S\left[U(T)(\rho_S\otimes\rho_c)U^\dagger(T)\right].
\]

For orthogonal quasi-static source branches with probabilities `p_s`,

\[
\mathcal E_T(\rho_c)
=\sum_s p_s U_s(T)\rho_c U_s^\dagger(T).
\]

For the two-level clock, the off-diagonal internal coherence acquires

\[
\rho_{ge}(T)
=e^{-i\omega_0T}\,\Gamma(T)\,\rho_{ge}(0),
\]

with

\[
\Gamma(T)
=\sum_s p_s
\exp\left[-i\omega_0T\frac{\Phi_s}{c^2}\right].
\]

This is a concrete channel-level prediction rather than an entanglement slogan. It is not claimed to be unique to C5; it is a C5 witness for the RQIR channel requirement.

If the source branches are not orthogonal or become dynamically recombined, the corresponding overlap/interference terms must be retained before the partial trace. The construction does not require classicalizing the source.

## 6. Relational/gauge statement

`Phi(x)` by itself is gauge-coordinate dependent outside the restricted Newtonian description. The operational quantity is the phase/proper-time difference between physically specified clock histories,

\[
\Delta\varphi
=\omega_0\left(\tau_A-\tau_B\right),
\]

with endpoints/interventions defined by physical worldlines or dressed relational observables. In perturbative gravity these may be implemented with gravitational dressing; the Newtonian expression above is the controlled gauge-fixed representation of that relational observable.

Therefore this file is not asserting that a bare local metric component is an observable.

## 7. Controlled limits

- `G -> 0`: `Phi -> 0`, so `Gamma -> 1` and gravity decouples.
- `hbar -> 0`: the quantum source/channel description reduces to classical branch dynamics when the source state is correspondingly classical/coarse grained; the proper-time law itself remains the classical GR result.
- weak field: valid for `|Phi|/c^2 << 1` and negligible higher post-Newtonian terms.
- classical source: a sharply localized source reduces the channel to one gravitational-redshift unitary.

## 8. RQIR gate effect

This explicit witness changes the C5 audit as follows:

- Q1 quantum clocks/proper time: **SUPPORTED in the declared weak-field sector**;
- Q2 superposed sources: **SUPPORTED**;
- Q4 reduced quantum channel: **SUPPORTED for this minimal clock-source channel**, while more elaborate detector benchmarking remains open;
- G1 relational/gauge: **SUPPORTED-IN-PRINCIPLE with an explicit operational phase and perturbative dressing requirement**;
- G5/G6/G8: controlled limits are explicit.

## 9. Novelty verdict

Nothing here is C5-distinct. On the contrary, the construction is an explicit witness that C5 can inhabit the RQIR quantum-clock and quantum-channel semantics.

Therefore Q1/Q4 do not provide the missing obstruction required to evade `RQIR-CG-NG-003`.
