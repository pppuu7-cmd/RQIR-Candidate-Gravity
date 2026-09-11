#!/usr/bin/env python3
import json
from pathlib import Path

OUT=Path("wave3_results")
OUT.mkdir(exist_ok=True)

# Formal perturbative bookkeeping around flat space:
# curvature Riemann/Ricci/scalar begins at O(h): R = eps R1 + eps^2 R2 + ... .
# Therefore a local invariant cubic in curvature begins at O(h^3) and cannot
# modify the quadratic propagator. This is an exact order-counting statement,
# independent of the detailed tensor contractions (modulo invariants that vanish
# identically/topologically in a chosen dimension).

# polynomial represented by exponent->formal coefficient labels; we only need powers.
def multiply_support(A,B,max_order=12):
    out=set()
    for a in A:
        for b in B:
            if a+b<=max_order:
                out.add(a+b)
    return out

curv_support={1,2,3,4,5,6}
records=[]
for n in range(1,7):
    support={0}
    for _ in range(n):
        support=multiply_support(support,curv_support)
    support=sorted(support)
    records.append({
        "curvature_power":n,
        "minimum_h_order":min(support),
        "affects_two_point_quadratic_action":2 in support,
        "first_possible_n_point_vertex":min(support),
        "orders_through_12":support,
    })

summary={
 "test":"perturbative visibility of curvature-power operators around flat space",
 "curvature_expansion":"Riemann/Ricci/R = O(h)+O(h^2)+...",
 "records":records,
 "key_result":"Curvature-cubic operators start at O(h^3): they can change three- and higher-point gravity vertices while leaving the two-point propagator untouched.",
 "implication":"Even if spectral purity/positivity uniquely fixes the physical two-point TT pole to GR, it does not fix the full interacting theory. Higher-curvature EFT Wilson coefficients remain an independent higher-point layer unless another principle fixes them.",
 "comparator_note":"Such curvature-cubic and higher local operators already belong to the ordinary low-energy gravitational EFT/C5 framework; their existence is not by itself new quantum gravity.",
 "scope":"order counting only; does not enumerate independent 4D on-shell curvature invariants or compute helicity amplitudes"
}
(OUT/"higher_point_visibility.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
