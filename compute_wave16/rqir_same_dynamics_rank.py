#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

# Generic linearized proxy. Two sectors each have a two-parameter local copy if
# allowed to float independently. RQIR's frozen single-dynamics rule identifies
# those copies as one common parameter vector.
As=np.array([[1.0,0.2],[0.35,1.0]])
Ad=np.array([[0.8,-0.45]])

Jshared=np.vstack([As,Ad])
Junlinked=np.block([
 [As, np.zeros((2,2))],
 [np.zeros((1,2)),Ad]
])
rank_shared=int(np.linalg.matrix_rank(Jshared,tol=1e-12))
rank_unlinked=int(np.linalg.matrix_rank(Junlinked,tol=1e-12))
null_shared=2-rank_shared
null_unlinked=4-rank_unlinked
_,S,Vh=np.linalg.svd(Junlinked,full_matrices=True)
nv=Vh[-1]/np.linalg.norm(Vh[-1])
# Untouched second dispersive functional sensitive to the independent-sector null.
hold_row=np.array([0.0,0.0,0.25,0.95])
hold_response=float(hold_row@nv)
out={
 "test":"rank effect of frozen RQIR single-dynamics/same-parameter-convention rule",
 "authority":"pinned RQIR MASTER_TABLE single-dynamics rule + MODEL_TO_RQIR_CONTRACT contract principle",
 "shared_design_jacobian":Jshared.tolist(),
 "shared_rank":rank_shared,
 "shared_nullity":null_shared,
 "unlinked_design_jacobian":Junlinked.tolist(),
 "unlinked_rank":rank_unlinked,
 "unlinked_nullity":null_unlinked,
 "unlinked_null_vector":[float(v) for v in nv],
 "prospective_holdout_sensitivity_to_unlinked_null":hold_response,
 "single_dynamics_removes_sector_copy_nullity":bool(null_shared==0 and null_unlinked==1 and abs(hold_response)>1e-3),
 "does_not_fix_internal_kernel_shape":True,
 "conclusion":"RQIR's single-dynamics rule has real constraining power: it forbids independent sector copies and removes the corresponding parameter null direction. But this identification acts across sector realizations; it does not specify the internal functional shape of the common operator/kernel."
}
Path('wave16_results').mkdir(exist_ok=True)
Path('wave16_results/rqir_same_dynamics_rank.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
