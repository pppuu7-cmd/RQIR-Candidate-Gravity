# ITER094 / G96 terminal — attribution of the G95 structural obstruction

Classification: `G95_STRUCTURAL_OBSTRUCTION_ATTRIBUTED_SCOPED`

Authority:
- prereg `8995471a3e20dbdf5cf382c7773aacea0239348b`
- implementation `ab698da339f83dc1733157fcd547e8202ce0e22f`
- production/workflow head `4327baeb0ab2596647925a8ed75c3259e595af86`
- run `34791191689`
- jobs A/B/C/D/aggregate `103815604641 / 103815604582 / 103815604557 / 103815604433 / 103815641461`
- artifacts A/B/C/D `10328477143 / 10328487045 / 10327738686 / 10328616733`
- aggregate `10327927078`, digest `sha256:85bc13233b9a812b9d4114116e838e4729a34a31d3b210ecf5605525fd9ab17b`

All raw lane artifacts and aggregate were consumed before classification.

## Exact attribution
For the 10-dimensional G95 retarded cubic one-Delta basis:
- no added families: rank 0, nullity 10;
- C0 only: rank 6, nullity 4;
- C1 only: rank 5, nullity 5;
- P only: rank 3, nullity 7;
- C0+C1: rank 9, nullity 1;
- C0+P: rank 8, nullity 2;
- C1+P: rank 7, nullity 3;
- C0+C1+P: rank 10, nullity 0.

The unique minimal zero-nullity family set is the FULL triple `{C0,C1,P}`. Thus no single family alone, and no pair of families, causes structural emptiness; the obstruction is genuinely joint.

Leave-one-family-out spaces contain diagnostic connected directions (nullities 1,2,3 respectively), but lane C shows zero coherent/rank-one basis directions in every leave-one-out space on the frozen history set. Therefore simply dropping one structural family would not by itself produce a coherent noiseless completion.

Coordinate-transform controls preserve full-system rank exactly: 10/10/10.

## Scientific meaning
G95 is not being weakened. G96 identifies the obstruction as a three-way incompatibility inside the frozen finite ansatz, and separately shows that each single-family ablation still leaves only incoherent basis directions under the G95 noiseless cocycle test. No ablated direction is promoted to RCG-002 physics.

The next fundamental step remains a genuinely new, independently motivated physical source/state/evolution principle (potentially noisy, mediator-retaining, continuum, or protocol-restricted) with total-source conservation/Bianchi closure and pairwise normalization recovered in the same realization.

Programme readiness remains 66%; theory established remains 0%.
