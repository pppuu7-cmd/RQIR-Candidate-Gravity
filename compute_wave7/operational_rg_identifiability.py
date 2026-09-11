#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

# Three RG-relevant amplitudes c. Operational observables O=J c near a reference trajectory.
# Local uniqueness requires rank(J)=3.
matrices={
 "one_observable":np.array([[1.0,0.2,-0.1]]),
 "two_independent":np.array([[1.0,0.2,-0.1],[0.1,1.0,0.3]]),
 "three_rank_deficient":np.array([[1.0,0.2,-0.1],[0.1,1.0,0.3],[1.1,1.2,0.2]]),
 "three_full_rank":np.array([[1.0,0.2,-0.1],[0.1,1.0,0.3],[-0.2,0.35,1.0]]),
 "five_overcomplete":np.array([[1.0,0.2,-0.1],[0.1,1.0,0.3],[-0.2,0.35,1.0],[0.7,-0.1,0.2],[0.2,0.4,-0.6]])
}
records=[]
for name,J in matrices.items():
    rank=int(np.linalg.matrix_rank(J,tol=1e-12))
    s=np.linalg.svd(J,compute_uv=False)
    nullity=3-rank
    records.append({
      "case":name,"observable_count":int(J.shape[0]),"rank":rank,"relevant_parameter_nullity":nullity,
      "singular_values":s.tolist(),"locally_identifiable":rank==3
    })

# Conditioning matters even at full rank.
eps=1e-6
J_bad=np.array([[1,0,0],[0,1,0],[1,1,eps]],float)
s_bad=np.linalg.svd(J_bad,compute_uv=False)
cond_bad=float(s_bad.max()/s_bad.min())

out={
 "test":"operational observables required to identify RG relevant coordinates",
 "relevant_parameter_count":3,
 "cases":records,
 "ill_conditioned_full_rank_condition_number":cond_bad,
 "criterion":"Local closure of m relevant coordinates requires at least m operationally independent observables and a full-column-rank, sufficiently conditioned sensitivity Jacobian.",
 "conclusion":"RQIR can only turn a finite-dimensional UV critical surface into a unique trajectory if its prospective observables span all relevant directions. Counting observables is insufficient; independence and conditioning are required.",
 "scope":"local linear identifiability criterion, not a computed gravitational FRG Jacobian"
}
Path('wave7_results').mkdir(exist_ok=True)
Path('wave7_results/operational_rg_identifiability.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
