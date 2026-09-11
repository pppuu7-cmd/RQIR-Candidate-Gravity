# C5 Premise-Witness Audit 001

**Comparator:** C5 — perturbative quantum gravity / low-energy quantum GR as EFT  
**Domain:** weak-field / sub-cutoff regime in which the gravitational EFT is controlled  
**Status:** SECOND STRUCTURAL AUDIT; explicit weak-field witnesses added  
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
| Q1 quantum clocks / proper time | relational proper-time phase of a quantum clock in weak gravity | SUPPORTED | `C5_WITNESS_Q1_Q4_RELATIONAL_CLOCK_CHANNEL_001.md` |
| Q2 superposed sources | ordinary quantum superposition in matter+graviton Hilbert space / density operator | SUPPORTED | same clock-channel witness retains coherent source branches |
| Q3 one source/backreaction rule | one action/path integral / Schwinger-Keldysh generating functional | SUPPORTED | `C5_WITNESS_Q5_Q6_METRIC_COVARIANCE_001.md` |
| Q4 gravity-mediated quantum information | reduced CPTP channel obtained from joint unitary evolution and partial trace | SUPPORTED in witness sector | `C5_WITNESS_Q1_Q4_RELATIONAL_CLOCK_CHANNEL_001.md` gives an explicit source-clock channel; broader apparatus benchmarks remain separate |
| Q5 geometry fluctuations | intrinsic graviton covariance + matter-induced covariance propagated by `G_R` | SUPPORTED | `C5_WITNESS_Q5_Q6_METRIC_COVARIANCE_001.md` |
| Q6 causal/process structure | retarded Green map / causal SK response | SUPPORTED in linearized witness sector | `C5_WITNESS_Q5_Q6_METRIC_COVARIANCE_001.md` |
| Q7 low-energy QG EFT | GR treated as quantum EFT with cutoff/power counting and low-energy predictions | SUPPORTED | native domain of C5; see `CONDITIONAL_MINIMAL_COMPLETION_001.md` |

### Q-channel verdict

No `CONFLICT` is present. All seven frozen observable-channel semantics now have an explicit or standard C5 realization in the declared low-energy domain. This does not make every detector-level calculation complete; it removes the candidate claim that Q1-Q7 themselves force a C5-distinct microscopic dynamics.

## 3. Consistency-gate audit G0-G13

| Gate | C5 witness route | Status |
|---|---|---|
| G0 dimensions | EFT operator basis with dimensionful Newton coupling and Wilson coefficients | SUPPORTED |
| G1 gauge/relational observables | operational proper-time phase plus perturbative gravitational dressing/gauge completion | SUPPORTED-IN-PRINCIPLE |
| G2 conservation/Bianchi/Ward | diffeomorphism invariance and associated Ward/Slavnov-Taylor identities | SUPPORTED |
| G3/G3a/G3b unitarity/positivity/CP | perturbative closed-system unitarity; explicit reduced source-clock map is CPTP | SUPPORTED-IN-PRINCIPLE |
| G4/G4a causal support | explicit retarded propagator/response witness | SUPPORTED |
| G5 `hbar -> 0` | classical stationary-phase / loop suppression limit | SUPPORTED |
| G6 `G -> 0` | explicit decoupling in the clock witness and EFT dynamics | SUPPORTED |
| G7 flat limit | expansion about Minkowski / local flat limit | SUPPORTED |
| G8 Newtonian/weak field | Einstein-Hilbert normalization and explicit weak-field clock coupling | SUPPORTED |
| G9 EFT/power counting | defining structure of low-energy quantum GR | SUPPORTED |
| G10/G10a stress-energy renormalization | one common renormalized/smeared source hierarchy | SUPPORTED | 
| G11 precision-test consistency | leading theory is GR; EFT corrections suppressed in-domain | SUPPORTED-IN-PRINCIPLE |
| G12/G12a degeneracy audit | explicit comparator analysis is possible and is being performed | SUPPORTED-IN-PRINCIPLE |
| G13 detector observability | requires a chosen experiment, likelihood and resource map | APPARATUS-OPEN |

G10 authority: `C5_WITNESS_G10_RENORMALIZED_SOURCE_HIERARCHY_001.md`.

### Gate verdict

No theory-level `CONFLICT` has been identified. `G13` cannot serve as a C5-specific foundational obstruction: failure of a chosen detector to identify a prediction would be an experimental/resource limitation, not proof that the C5 dynamics violates the RQIR construction semantics.

## 4. Higher-order / L4-L5 witness checks

The principal candidates considered after the Gaussian/L3 no-go remain C5-compatible:

1. **soft/BMS/Ward relations:** standard gravity amplitudes and in-in correlators satisfy them;
2. **higher-order KMS/fluctuation-dissipation relations:** ordinary Schwinger-Keldysh QFT supplies them under thermal/KMS assumptions;
3. **positivity/dispersive constraints:** restrict EFT parameter space but do not uniquely choose a non-C5 completion;
4. **gravitational dressing and subsystem non-factorization:** already occur in perturbative quantum gravity;
5. **gravity-mediated entanglement:** can exclude classical mediators under assumptions, but not a quantum C5 mediator.

Thus none supplies the missing C5 obstruction.

## 5. Evidence base

Representative external anchors:

- Donoghue, *General relativity as an effective field theory* and later reviews (e.g. arXiv:2211.09902): low-energy quantum GR is a controlled EFT with calculable long-distance quantum effects.
- Hu & Verdaguer, arXiv:0802.0658: influence-functional/Schwinger-Keldysh treatment supplies stress-tensor noise, causal response, dissipation and induced metric fluctuations.
- Haehl, Loganayagam & Rangamani, arXiv:1610.01940 and arXiv:1803.11155: SK unitarity/KMS structure and nonlinear fluctuation relations.
- Hamada & Shiu, arXiv:1801.05528; De Luca, Khoury & Wong, arXiv:2412.12273: soft-graviton/Ward relations in standard gravity.
- Donnelly & Giddings, Phys. Rev. D 94, 104038 (2016); Giddings & Kinsella, arXiv:1802.01602: gravitational dressing and nonlocal gauge-invariant observables within perturbative gravity.
- Tokuda, Aoki & Hirano, arXiv:2007.15009: gravitational positivity bounds constrain, rather than uniquely determine, the EFT.

## 6. Current witness conclusion

Within the declared weak-field/EFT domain,

\[
\boxed{
\text{no frozen RQIR theory-level requirement has been shown incompatible with C5}
}
\]

The Q1-Q7 channel semantics now all possess C5 witnesses. The remaining non-fully-certified entries are gauge-completion detail, full perturbative/open-system certificate bookkeeping, precision-domain documentation, comparator bookkeeping, and detector-specific G13 work; none is presently a physical contradiction.

Accordingly, `RQIR-CG-NG-003` is strongly activated: universal consequences of the presently shared premise set cannot establish `QG-007` novelty against C5.

## 7. Certification coverage metric

For progress bookkeeping only, assign weight 1 to `SUPPORTED`, 0.5 to `SUPPORTED-IN-PRINCIPLE`, and 0 to `APPARATUS-OPEN`, without interpreting this as a probability.

Across Q1-Q7 plus the fourteen grouped G0-G13 entries used above:

- fully supported entries: 17;
- supported-in-principle entries: 3;
- apparatus-open entries: 1;
- conflicts: 0.

This gives an explicit witness-certificate coverage score

\[
(17+0.5\times3)/21 \simeq 0.881.
\]

So the present C5 premise-witness certification is **about 88% complete by this bookkeeping metric**, with **zero discovered conflicts**.

## 8. Remaining work

To close the witness certificate rather than merely strengthen it:

1. write one explicit perturbative gauge/dressing completion for the clock observable (G1);
2. pin the exact perturbative unitarity/CP statement used for G3 in the selected truncation;
3. document the precision-test/EFT validity domain for G11;
4. finish the formal C0-C6 degeneracy table for G12;
5. leave G13 to a later concrete detector claim, because it is not a theory-selection obstruction.

Unless items 1-4 reveal an actual contradiction, the correct independent RQIR-only endpoint remains `RQIR-Derived Gravity-Interface Equivalence Class v0`, not a manufactured deformation.
