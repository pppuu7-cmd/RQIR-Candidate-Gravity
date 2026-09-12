# ITER021E / G39-A2 — repaired parent-seeded adversarial gate

Authorized only after G39-A-N terminal diagnostic PASS established that the original G39-A rank3-vs-rank2 nesting violation was an optimizer/search miss.

Frozen before results:
- same rank-3 comparator family, RCG-002 targets, parameter bounds and science thresholds as G39-A;
- retain the complete original rank-3 Sobol/LHS multistart designs and bounded least-squares refinement;
- reproduce each method/shard rank-2 optimum, embed it exactly in rank 3 with third-mode rate = 0, and add that legal boundary point as one mandatory candidate/seed;
- exact embedding and rank3<=rank2 nesting tolerance: `1e-10`;
- adversarial nonzero gap: `>1e-4` for both methods;
- cross-method agreement: `<=0.002` per shard;
- no threshold/family changes after result inspection.

PASS is only scoped evidence against this calibrated finite rank-3 multimode shared classical white-noise family. It is not a no-go for all classical/semiclassical mediators and is not evidence of full quantum gravity.
