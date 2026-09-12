# ITER022A / G40-P — strict classical information-backflow pre-gate

Independent of active G37/G39 repaired adversarial gates. This gate validates a new comparator ingredient only and cannot change their verdicts.

Physical mechanism: a symmetric hidden classical two-state random-telegraph process `xi(t)=±1` drives the additive local Hamiltonian `H=nu*(cA Z_A + cB Z_B)`. Each hidden-noise trajectory is a product of local unitaries. The reduced system channel can nevertheless exhibit BLP trace-distance revival after the hidden classical state is ignored.

Frozen before results:
- four strong-coupling RTN controls must each have total positive trace-distance increment `>0.02` on the fixed 241-point `t∈[0,12]` grid;
- four weak-coupling controls must each have total positive increment `<1e-6`;
- reduced-map TP error `<1e-10`;
- Choi minimum eigenvalue `>-1e-8`;
- conditioned product-unitary factorization error `<1e-12`;
- output negativity from sampled product inputs `<1e-9`;
- no result-dependent parameter or threshold changes.

PASS validates implementation plus a strict BLP information-backflow witness for this finite hidden-classical RTN ingredient. It does not compare RCG-002, is not a no-go theorem and does not imply full quantum gravity or new physics.
