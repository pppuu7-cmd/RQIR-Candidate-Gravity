# C5 Witness G3 — Closed-system unitarity and reduced-channel complete positivity

**Status:** STRUCTURAL WITNESS  
**Comparator:** C5 perturbative quantum GR/EFT  
**Purpose:** certify the RQIR G3/G3a/G3b requirement in the controlled low-energy domain without claiming UV completion.

## 1. Closed low-energy system

Take the regulated low-energy matter+graviton EFT in a domain below its cutoff, with a Hermitian effective Hamiltonian `H_EFT` acting on the retained physical state space after gauge constraints are treated consistently.

The exact evolution within that regulated effective description is

\[
U(t)=\exp\left(-\frac{i}{\hbar}H_{EFT}t\right),
\qquad
U^\dagger U=1.
\]

The EFT need not be ultraviolet complete for this to be the correct low-energy consistency condition.

## 2. Perturbative statement

Scattering and correlation functions are organized order by order in the EFT expansion. Perturbative truncation is valid only inside the declared power-counting domain; apparent violations caused by using the truncation beyond its validity are not physical predictions of C5.

The optical-theorem/unitarity relations constrain the absorptive parts of amplitudes and the cuts of loop diagrams order by order.

## 3. Reduced dynamics

Partition the retained Hilbert space into an observed subsystem `S` and unobserved gravitational/matter environment `E`. For an initially specified joint state `rho_SE`, evolution is

\[
\rho_{SE}(t)=U(t)\rho_{SE}(0)U^\dagger(t).
\]

For the standard product-state channel construction

\[
\rho_{SE}(0)=\rho_S\otimes\rho_E,
\]

the reduced map is

\[
\mathcal E_t(\rho_S)
=\mathrm{Tr}_E\left[U(t)(\rho_S\otimes\rho_E)U^\dagger(t)\right].
\]

By the Stinespring form, `E_t` is completely positive and trace preserving.

This is exactly the structure used explicitly in `C5_WITNESS_Q1_Q4_RELATIONAL_CLOCK_CHANNEL_001.md`.

## 4. Initial correlations caveat

If the system and environment are initially correlated, a CPTP map on an arbitrary independently variable `rho_S` need not exist without specifying an assignment map/domain. RQIR must therefore declare the preparation class rather than silently demanding a universal CP map where the preparation semantics do not support one.

This is a general open-quantum-system issue, not a C5-specific inconsistency.

## 5. Truncation caveat

A naive finite-order expansion of a CPTP channel can fail to look CP term-by-term even when the underlying reduced evolution is physical. Therefore gate testing must distinguish:

1. failure of the underlying C5 dynamics; from
2. a non-CP perturbative representation produced by inconsistent truncation.

The witness claim here concerns the existence of a consistent low-energy unitary dilation, not every algebraic truncation scheme.

## 6. Gate effect

Within the declared EFT domain:

- closed retained dynamics admits a unitary realization;
- reduced product-preparation dynamics admits a CPTP Stinespring representation;
- positivity/CP failures caused only by uncontrolled truncation are excluded from the claimed domain;
- preparation correlations must be declared explicitly.

Thus G3/G3a/G3b do not currently provide a C5 obstruction.
