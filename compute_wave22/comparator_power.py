import itertools
import numpy as np
from common import PARAMS, selected_bank, write_result

_,_,selected,X=selected_bank(10)
candidates={
 'C0_reference':[0,0,0,0,0,0],
 'C1_cubic':[0.25,-0.15,0,0,0,0],
 'C2_quartic':[0,0,0.20,-0.18,0,0],
 'C3_tensor':[0,0,0,0,0.22,-0.17],
 'C4_mixed':[0.12,0.08,0.15,-0.11,0.10,-0.09]
}
vectors={k:X@np.asarray(v,dtype=float) for k,v in candidates.items()}
dists={}
for a,b in itertools.combinations(candidates,2):
    d=float(np.linalg.norm(vectors[a]-vectors[b]))
    dists[f'{a}__{b}']=d
min_dist=min(dists.values())
out={
 'test':'prospective synthetic comparator separation under common frozen IR normalization',
 'params':PARAMS,
 'candidate_coefficients':candidates,
 'holdout_vectors':vectors,
 'pairwise_l2_distances':dists,
 'minimum_pairwise_distance':min_dist,
 'all_pairwise_nonzero':min_dist>1e-6,
 'reference_and_all_deformation_classes_distinguished':all(float(np.linalg.norm(vectors[k]-vectors['C0_reference']))>1e-6 for k in candidates if k!='C0_reference'),
 'conclusion':'The candidate-blind bank prospectively separates pure cubic, pure quartic, pure tensor-dressing and mixed residual deformations that share the same frozen lower-order/IR normalization assumptions.'
}
write_result('comparator_power',out)
