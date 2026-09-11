#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

# Start from the Wave-15 finite kernel proxy to ask a narrower question:
# once generic soft/normalization choices are added (not claimed as RQIR), one
# exact shape direction remained. Determine what *kind* of additional equation
# would remove it, without pretending RQIR supplies that equation.
pairs=[(i,j) for i in range(3) for j in range(3)]
rows=[]
for i in range(3):
    rows.append([1.0 if (ii,jj)==(i,0) else 0.0 for ii,jj in pairs])
for k in range(5):
    rows.append([1.0 if ii+jj==k else 0.0 for ii,jj in pairs])
integ=np.array([1.0/((j+1)*(i+j+2)) for i,j in pairs])
A=np.vstack([np.array(rows,float),integ])
U,S,Vh=np.linalg.svd(A,full_matrices=True)
rank=int(np.linalg.matrix_rank(A,tol=1e-12))
nv=Vh[-1]/np.linalg.norm(Vh[-1])
# Candidate additional linear functionals. These are diagnostics only.
functionals={
 "first_x_moment":np.array([1.0/((j+1)*(i+j+3)) for i,j in pairs]),
 "first_y_moment":np.array([1.0/((j+2)*(i+j+3)) for i,j in pairs]),
 "mixed_xy_moment":np.array([1.0/((j+2)*(i+j+4)) for i,j in pairs]),
}
sens={k:float(v@nv) for k,v in functionals.items()}
nonzero=[k for k,v in sens.items() if abs(v)>1e-8]
out={
 "test":"what mathematical type of extra principle would remove the residual Wave-15 kernel direction",
 "important_provenance_note":"Wave-15 endpoint/coincidence softness and normalization are proxy/modeling assumptions, not frozen-RQIR consequences; this test is diagnostic only.",
 "proxy_rank_before_extra_principle":rank,
 "proxy_nullity_before_extra_principle":len(pairs)-rank,
 "normalized_residual_null_vector":[float(v) for v in nv],
 "candidate_functional_sensitivities":sens,
 "number_of_independent_extra_scalar_equalities_needed_in_this_proxy":1,
 "at_least_one_candidate_functional_detects_null":len(nonzero)>0,
 "detecting_functionals":nonzero,
 "rqir_supplies_value_for_any_detecting_functional":False,
 "minimal_missing_physics_type":"one independent gravity-specific operator-shape relation in this finite proxy, or an equivalent functional/dynamical law in the continuum theory",
 "conclusion":"Mathematically, the already-strengthened Wave-15 proxy needs only one further independent shape relation to become unique. Scientifically, frozen RQIR does not provide the value or physical origin of such a relation. The residual direction therefore identifies the *type* of missing principle, not permission to choose one post hoc."
}
Path('wave16_results').mkdir(exist_ok=True)
Path('wave16_results/minimal_extra_principle.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
