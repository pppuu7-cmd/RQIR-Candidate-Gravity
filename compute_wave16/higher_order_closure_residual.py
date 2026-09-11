#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

# Proxy hierarchy: low-order RQIR-facing data h=(J,N,D) are generated from a
# common two-parameter latent dynamics p. Higher connected structures contain
# additional coefficients q unless an extra closure law is supplied.
A=np.array([[1.0,0.0],[0.4,1.0],[-0.3,0.8]])
B=np.array([[1.0,0.2],[0.1,1.0]])
# Design map y=(A p); extended map z=(A p, B p + q) with q in R^2.
Jlow=A
Jext=np.block([
 [A, np.zeros((3,2))],
 [B, np.eye(2)]
])
rank_low=int(np.linalg.matrix_rank(Jlow))
rank_ext=int(np.linalg.matrix_rank(Jext))
null_low=2-rank_low
null_ext=4-rank_ext
# If only the low-order hierarchy is used as design data, q is completely free.
Jdesign=np.block([A,np.zeros((3,2))])
rank_design=int(np.linalg.matrix_rank(Jdesign))
null_design=4-rank_design
# two prospective higher-order holdouts directly see q
hold=np.array([[0,0,1,0],[0,0,0,1]],float)
U,S,Vh=np.linalg.svd(Jdesign,full_matrices=True)
null_basis=Vh[rank_design:].T
hold_rank=int(np.linalg.matrix_rank(hold@null_basis,tol=1e-12))
out={
 "test":"ordered low-order hierarchy does not supply a universal higher-order closure map",
 "authority":"RQIR_DERIVED_EQUIVALENCE_CLASS_V0 residual-freedom statement; frozen RQIR requires higher objects at claimed order but no universal closure law",
 "low_order_parameter_rank":rank_low,
 "low_order_parameter_nullity":null_low,
 "extended_parameter_count":4,
 "design_rank_using_J_N_D_only":rank_design,
 "design_nullity_after_J_N_D_only":null_design,
 "higher_order_holdout_rank_on_design_nullspace":hold_rank,
 "higher_order_freedom_survives_without_extra_law":bool(null_design>=2 and hold_rank>=2),
 "candidate_new_closure_law_present":False,
 "conclusion":"One coherent dynamics can generate the ordered low-order hierarchy while still leaving higher connected/response structures undetermined unless the microscopic dynamics itself supplies an additional closure relation. This mirrors the frozen RQIR equivalence-class result and prevents low-order interface constraints from being promoted to a unique all-order kernel."
}
Path('wave16_results').mkdir(exist_ok=True)
Path('wave16_results/higher_order_closure_residual.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
