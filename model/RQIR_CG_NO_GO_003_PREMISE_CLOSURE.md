# RQIR-CG-NG-003 — Premise-closure no-go for a C5-distinct theorem

**Status:** ACTIVE NEGATIVE RESULT  
**Scope:** frozen RQIR v1.0; independent `rqir-derived-model-v0` branch; no polygon-QGR input.

## 1. Question

Can a sector-specific L4/L5 relation be derived only from frozen RQIR plus auxiliary assumptions that are themselves satisfied by perturbative low-energy quantum GR/EFT (C5), and nevertheless exclude C5?

## 2. Setup

Let

\[
P_D = P_{RQIR}(D) \cup A(D)
\]

be the declared premise set in domain `D`, where `P_RQIR` is the frozen theory-level RQIR requirement set and `A` contains any explicitly declared auxiliary physical assumptions.

Let `C5(D)` denote the relevant perturbative quantum-GR/EFT comparator family after allowed state, Wilson-coefficient, calibration and nuisance choices have been specified.

Call `c_5` a **C5 witness** for `P_D` if

\[
c_5 \in C5(D), \qquad c_5 \models P_D.
\]

## 3. Premise-closure proposition

Assume the inference system used for the candidate derivation is sound. If a C5 witness `c_5` exists for `P_D`, then for every consequence `F` satisfying

\[
P_D \models F,
\]

we necessarily have

\[
c_5 \models F.
\]

Therefore `F` cannot, by itself, be a discriminator against the whole C5 comparator family.

Equivalently,

\[
\boxed{
\exists c_5\in C5(D): c_5\models P_D
\quad\Longrightarrow\quad
\text{no theorem of }P_D\text{ alone can exclude all of C5(D)}
}
\]

This is a logical closure statement, not a claim that C5 is ultraviolet complete.

## 4. Comparator consequence

RQIR novelty requires a prediction that survives the comparator quotient. If even one allowed C5 realization reproduces the candidate relation after the same baseline transformation and nuisance/calibration profiling, the relation is not C5-distinct.

Thus a universal consistency identity shared by a C5 witness can tighten the admissible equivalence class but cannot establish `QG-007` novelty.

## 5. Concrete L4/L5 candidates checked

### 5.1 Soft/BMS/Ward hierarchy

Soft-graviton relations and gravitational memory are consequences of gravitational gauge/asymptotic symmetry and are explicitly realized in standard gravity amplitudes and in-in correlators. They are therefore valuable RQIR consistency checks but not C5-exclusion relations.

Representative references: Cachazo & Strominger, arXiv:1404.4091; Hamada & Shiu, arXiv:1801.05528; De Luca, Khoury & Wong, arXiv:2412.12273 / Phys. Rev. D 112, 024032 (2025).

### 5.2 Nonlinear fluctuation-dissipation / KMS constraints

When equilibrium/KMS assumptions are added, Schwinger-Keldysh effective theory relates fluctuations and nonlinear response at higher order. But these are general quantum-statistical constraints and are naturally implemented by ordinary QFT/SK dynamics, including gravitational open-system constructions. They do not select a C5-distinct gravity law.

Representative references: Haehl, Loganayagam & Rangamani, arXiv:1610.01940 and arXiv:1803.11155; Hu & Verdaguer, arXiv:0802.0658.

### 5.3 Positivity / dispersive bounds

Positivity constrains EFT Wilson-coefficient regions under assumptions such as unitarity, causality, analyticity/locality and Lorentz invariance. In gravity, the massless graviton introduces additional subtleties and the result is a bound/allowed region, not a unique higher-order closure. A C5 EFT can satisfy the same bounds.

Representative reference: Tokuda, Aoki & Hirano, arXiv:2007.15009.

### 5.4 Gravitational dressing / non-factorization

Gauge-invariant gravitational observables require dressing and exhibit nonlocal algebra/subsystem subtleties already in perturbative quantum gravity. This is structurally important for RQIR relational observables, but it is a feature of C5 rather than an obstruction to it.

Representative references: Donnelly & Giddings, Phys. Rev. D 94, 104038 (2016); Giddings & Kinsella, arXiv:1802.01602.

### 5.5 Gravity-mediated entanglement witnesses

Under locality/information-theoretic assumptions, gravity-mediated entanglement can exclude a purely classical mediator. This helps distinguish C0/C3-like comparators, but a quantum gravitational mediator in C5 is precisely capable of such nonclassical mediation. It is not a C5 discriminator.

Representative references: Marletto & Vedral, Phys. Rev. Lett. 119, 240402 (2017); Phys. Rev. D 102, 086012 (2020).

## 6. The only escape routes

A C5-distinct result can arise only if at least one of the following occurs:

1. **C5 gate obstruction:** prove that no C5 realization satisfies one or more frozen RQIR premises in the claimed domain;
2. **Extra hypothesis:** add a physical postulate `A_*` that excludes every relevant C5 realization — this must be labeled `EXTRA-HYPOTHESIS`, not `RQIR-FORCED`;
3. **Empirical exclusion:** data reject the C5 prediction after proper nuisance/profile treatment;
4. **Domain exit:** work outside the controlled C5 EFT domain, in which case RQIR alone still does not determine the replacement UV theory.

## 7. Consequence for issue #4

The search for a C5-distinct L4/L5 relation is logically reduced to one decisive task:

> determine whether C5 is in fact a witness model of the full theory-level frozen RQIR premise set in the declared weak-field/EFT domain.

If yes, continued theorem hunting inside the same premise set cannot produce `QG-007` novelty. The correct RQIR-only output remains `RQIR-Derived Gravity-Interface Equivalence Class v0`.

## 8. Current verdict

The presently known universal L4/L5 structures tested above all fall on the C5-compatible side of the premise-closure proposition. No C5-specific obstruction has been found.

Therefore the next authority task is **C5 premise-witness certification**, not invention of another cross-order closure relation.
