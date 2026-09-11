# C5 Premise-Witness Audit 001

**Comparator:** C5 — perturbative quantum gravity / low-energy quantum GR as EFT  
**Domain:** weak-field / sub-cutoff regime in which the gravitational EFT is controlled  
**Status:** THIRD STRUCTURAL AUDIT; explicit weak-field/gauge/CP witnesses added  
**Independence:** no polygon-QGR input.

## 1. Purpose

`RQIR-CG-NG-003` shows that if even one C5 realization satisfies the same premise set used for a proposed RQIR-only theorem, that theorem cannot exclude the full C5 comparator family.

This audit asks whether frozen RQIR contains a genuine theory-level premise that C5 cannot satisfy.

Status vocabulary:

- `SUPPORTED` — this repository now has either a direct witness construction or standard C5 machinery directly supplies the required object/limit;
- `SUPPORTED-IN-PRINCIPLE` — no structural conflict is known, but a full explicit sector certificate has not yet been written here;
- `APPARATUS-OPEN` — depends on a detector/process realization and is not a foundational inconsistency;
- `CONFLICT` — no C5 witness is possible under the stated domain and assumptions.

## 2. Observable-channel audit Q1-Q7

| RQIR channel | C5 witness route | Status | Repository witness |
|---|---|---|---|
| Q1 quantum clocks / proper time | relational proper-time phase of a quantum clock in weak gravity | SUPPORTED | `C5_WITNESS_Q1_Q4_RELATIONAL_CLOCK_CHANNEL_001.md`; gauge completion in `C5_WITNESS_G1_RELATIONAL_GAUGE_COMPLETION_001.md` |
| Q2 superposed sources | ordinary quantum superposition in matter+graviton Hilbert space / density operator | SUPPORTED | same clock-channel witness retains coherent source branches |
| Q3 one source/backreaction rule | one action/path integral / Schwinger-Keldysh generating functional | SUPPORTED | `C5_WITNESS_Q5_Q6_METRIC_COVARIANCE_001.md` |
| Q4 gravity-mediated quantum information | reduced CPTP channel obtained from joint unitary evolution and partial trace | SUPPORTED in witness sector | `C5_WITNESS_Q1_Q4_RELATIONAL_CLOCK_CHANNEL_001.md`; CP structure in `C5_WITNESS_G3_UNITARITY_CP_001.md` |
| Q5 geometry fluctuations | intrinsic graviton covariance + matter-induced covariance propagated by `G_R` | SUPPORTED | `C5_WITNESS_Q5_Q6_METRIC_COVARIANCE_001.md` |
| Q6 causal/process structure | retarded Green map / causal SK response | SUPPORTED in linearized witness sector | `C5_WITNESS_Q5_Q6_METRIC_COVARIANCE_001.md` |
| Q7 low-energy QG EFT | GR treated as quantum EFT with cutoff/power counting and low-energy predictions | SUPPORTED | native domain of C5; see `CONDITIONAL_MINIMAL_COMPLETION_001.md` |

### Q-channel verdict

No `CONFLICT` is present. All seven frozen observable-channel semantics now have C5 witness realizations in the declared low-energy domain.

## 3. Consistency-gate audit G0-G13

| Gate | C5 witness route | Status | Repository witness |
|---|---|---|---|
| G0 dimensions | EFT operator basis with dimensionful Newton coupling and Wilson coefficients | SUPPORTED | EFT root construction |
| G1 gauge/relational observables | proper-time phase between physically defined worldlines; perturbative dressing/gauge completion | SUPPORTED | `C5_WITNESS_G1_RELATIONAL_GAUGE_COMPLETION_001.md` |
| G2 conservation/Bianchi/Ward | diffeomorphism invariance and associated Ward/Slavnov-Taylor identities | SUPPORTED | standard C5 structure |
| G3/G3a/G3b unitarity/positivity/CP | closed low-energy unitary dilation; reduced product-preparation dynamics CPTP | SUPPORTED | `C5_WITNESS_G3_UNITARITY_CP_001.md` |
| G4/G4a causal support | explicit retarded propagator/response witness | SUPPORTED | `C5_WITNESS_Q5_Q6_METRIC_COVARIANCE_001.md` |
| G5 `hbar -> 0` | classical stationary-phase / loop suppression limit | SUPPORTED | clock/EFT witnesses |
| G6 `G -> 0` | explicit gravitational decoupling | SUPPORTED | clock/EFT witnesses |
| G7 flat limit | expansion about Minkowski / local flat limit | SUPPORTED | C5 EFT construction |
| G8 Newtonian/weak field | Einstein-Hilbert normalization and explicit weak-field clock coupling | SUPPORTED | MIN + clock witness |
| G9 EFT/power counting | defining structure of low-energy quantum GR | SUPPORTED | C5 root |
| G10/G10a stress-energy renormalization | one common renormalized/smeared source hierarchy | SUPPORTED | `C5_WITNESS_G10_RENORMALIZED_SOURCE_HIERARCHY_001.md` |
| G11 precision-test consistency | leading theory is GR; EFT corrections suppressed in-domain | SUPPORTED-IN-PRINCIPLE | exact domain certificate still to be consolidated |
| G12/G12a degeneracy audit | explicit comparator analysis can be performed and is partially complete | SUPPORTED-IN-PRINCIPLE | final C0-C6 table still to be consolidated |
| G13 detector observability | requires a chosen experiment, likelihood and resource map | APPARATUS-OPEN | intentionally deferred to detector-facing claim |

### Gate verdict

No theory-level `CONFLICT` has been identified. G13 remains detector-specific and cannot by itself establish a foundational C5 inconsistency.

## 4. Higher-order / L4-L5 witness checks

The principal candidates considered after the Gaussian/L3 no-go remain C5-compatible:

1. soft/BMS/Ward relations;
2. higher-order KMS/fluctuation-dissipation relations;
3. positivity/dispersive constraints;
4. gravitational dressing and subsystem non-factorization;
5. gravity-mediated entanglement witnesses.

These structures can shrink or test the admissible class but do not exclude C5 when C5 satisfies the same premises.

## 5. Current witness conclusion

Within the declared weak-field/EFT domain,

\[
\boxed{
\text{no frozen RQIR theory-level requirement has been shown incompatible with C5}
}
\]

Q1-Q7, G1, G3, G4 and G10 now have explicit repository-level witness constructions. The remaining non-fully-certified theory-facing entries are G11 precision-domain consolidation and G12 final comparator bookkeeping; neither currently contains a physical contradiction.

Accordingly, `RQIR-CG-NG-003` is strongly activated: universal consequences of the presently shared premise set cannot establish `QG-007` novelty against C5.

## 6. Certification coverage metric

For progress bookkeeping only, assign weight 1 to `SUPPORTED`, 0.5 to `SUPPORTED-IN-PRINCIPLE`, and 0 to `APPARATUS-OPEN`. This is not a probability.

Across Q1-Q7 plus the fourteen grouped G0-G13 entries used above:

- fully supported entries: 18;
- supported-in-principle entries: 2;
- apparatus-open entries: 1;
- conflicts: 0.

Therefore

\[
\frac{18+0.5\times2}{21}=\frac{19}{21}\simeq0.905.
\]

The present C5 premise-witness certification is **about 90.5% complete by this bookkeeping metric**, with **zero discovered conflicts**.

## 7. Remaining work

1. consolidate the low-energy/precision validity certificate for G11;
2. finish the formal C0-C6 degeneracy table for G12;
3. leave G13 for a concrete detector/likelihood/resource claim.

Unless G11 or G12 exposes an actual contradiction rather than a documentation gap, the independent RQIR-only endpoint remains `RQIR-Derived Gravity-Interface Equivalence Class v0`.
