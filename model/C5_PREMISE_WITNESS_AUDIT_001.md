# C5 Premise-Witness Audit 001

**Comparator:** C5 — perturbative quantum gravity / low-energy quantum GR as EFT  
**Domain:** weak-field / sub-cutoff regime in which the gravitational EFT is controlled  
**Status:** FIRST STRUCTURAL AUDIT; detector-specific certificates remain separate  
**Independence:** no polygon-QGR input.

## 1. Purpose

`RQIR-CG-NG-003` shows that if even one C5 realization satisfies the same premise set used for a proposed RQIR-only theorem, that theorem cannot exclude the full C5 comparator family.

This audit therefore asks whether frozen RQIR contains a genuine theory-level premise that C5 cannot satisfy.

Status vocabulary:

- `SUPPORTED` — standard C5 machinery directly supplies the required object/limit;
- `SUPPORTED-IN-PRINCIPLE` — no structural conflict is known, but this repository has not yet supplied the full explicit sector calculation;
- `APPARATUS-OPEN` — depends on a detector/process realization and is not a foundational inconsistency;
- `CONFLICT` — no C5 witness is possible under the stated domain and assumptions.

## 2. Observable-channel audit Q1-Q7

| RQIR channel | C5 witness route | Status | Present assessment |
|---|---|---|---|
| Q1 quantum clocks / proper time | relational/dressed observables; quantized matter clock coupled to weak metric perturbations | SUPPORTED-IN-PRINCIPLE | perturbative gravity admits gauge-invariant gravitational dressing/relational constructions; an apparatus-specific clock map is still to be written |
| Q2 superposed sources | ordinary quantum superposition in matter+graviton Hilbert space / density operator | SUPPORTED | C5 does not require replacing coherent source preparations by classical mixtures |
| Q3 one source/backreaction rule | one action/path integral / Schwinger-Keldysh generating functional | SUPPORTED | mean, symmetrized noise, commutator/retarded response and higher connected functions arise from the same dynamics |
| Q4 gravity-mediated quantum information | reduced channel obtained by unitary matter+graviton evolution followed by partial trace/measurement | APPARATUS-OPEN | quantum mediation is structurally available; a benchmark-specific reduced channel is required for a repository PASS |
| Q5 geometry fluctuations | graviton correlators plus matter-induced metric fluctuations/loop contributions | SUPPORTED-IN-PRINCIPLE | provenance can be tracked diagrammatically or with influence-functional methods; explicit mode decomposition remains sector-specific |
| Q6 causal/process structure | retarded Green functions, causal SK response, ordinary unitary process composition | SUPPORTED-IN-PRINCIPLE | no structural causality conflict identified; explicit relational process object remains to be instantiated |
| Q7 low-energy QG EFT | GR treated as quantum EFT with cutoff/power counting and low-energy predictions | SUPPORTED | this is the native domain of C5 |

### Q-channel verdict

No `CONFLICT` is present. The open entries concern explicit relational/apparatus realizations, not an incompatibility of C5 with the frozen semantic requirement.

## 3. Consistency-gate audit G0-G13

| Gate | C5 witness route | Status |
|---|---|---|
| G0 dimensions | EFT operator basis with dimensionful Newton coupling and Wilson coefficients | SUPPORTED |
| G1 gauge/relational observables | BRST/gauge-fixed amplitudes plus gravitationally dressed/relational observables | SUPPORTED-IN-PRINCIPLE |
| G2 conservation/Bianchi/Ward | diffeomorphism invariance and associated Ward/Slavnov-Taylor identities | SUPPORTED |
| G3/G3a/G3b unitarity/positivity/CP | perturbative unitarity of closed theory; exact partial trace gives CP reduced dynamics | SUPPORTED-IN-PRINCIPLE |
| G4/G4a causal support | retarded propagators/response and causal in-in formulation | SUPPORTED |
| G5 `hbar -> 0` | classical stationary-phase / loop suppression limit | SUPPORTED |
| G6 `G -> 0` | gravitational interaction decouples | SUPPORTED |
| G7 flat limit | expansion about Minkowski / local flat limit | SUPPORTED |
| G8 Newtonian/weak field | Einstein-Hilbert normalization yields Poisson/Newtonian limit | SUPPORTED |
| G9 EFT/power counting | defining structure of low-energy quantum GR | SUPPORTED |
| G10/G10a stress-energy renormalization | QFT in curved spacetime/EFT renormalization and composite-operator prescriptions | SUPPORTED-IN-PRINCIPLE |
| G11 precision-test consistency | leading theory is GR; EFT corrections are suppressed in-domain | SUPPORTED-IN-PRINCIPLE |
| G12/G12a degeneracy audit | comparator analysis is external to C5 dynamics and can be performed | SUPPORTED-IN-PRINCIPLE |
| G13 detector observability | requires chosen experiment, likelihood and resource map | APPARATUS-OPEN |

### Gate verdict

Again, no theory-level `CONFLICT` has been identified. `G13` cannot serve as a C5-specific obstruction because failure of a particular detector to identify a prediction is an experimental/resource limitation, not proof that the underlying C5 dynamics violates RQIR.

## 4. Higher-order / L4-L5 witness checks

The principal candidates considered after the Gaussian/L3 no-go also remain C5-compatible:

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
\text{no frozen RQIR theory-level requirement has yet been shown incompatible with C5}
}
\]

This is not a proof that every detector-specific C5 calculation is complete. It is the narrower and decisive statement that the present RQIR premise set has not produced a C5 contradiction.

Accordingly, `RQIR-CG-NG-003` applies provisionally: universal consequences of the presently shared premise set cannot establish `QG-007` novelty against C5.

## 7. Remaining certification work

To upgrade this from first structural audit to a closed witness certificate, the repository still needs explicit examples for:

1. Q1/G1: one relational quantum-clock observable in a weak-field C5 calculation;
2. Q4: one matter-matter reduced quantum channel mediated by perturbative gravity;
3. Q5: one explicit separation of intrinsic graviton versus matter-induced geometry covariance;
4. Q6: one causal relational process/retarded-kernel construction;
5. G10: one explicit renormalized/smeared stress-tensor hierarchy convention;
6. G13: only for any later detector-specific claim, not for the foundational witness proposition.

Unless one of items 1-5 produces a contradiction rather than merely technical work, the C5 witness survives.
