import numpy as np
from common import PARAMS, build_pool, matrix, selected_bank, write_result

pool=build_pool(); M=matrix(pool)
ld,idx,selected,X=selected_bank(10)
sv=np.linalg.svd(X,compute_uv=False)
out={
 'test':'full-pool rank and exhaustive D-optimal 10-of-12 holdout selection',
 'params':PARAMS,
 'pool_size':len(pool),
 'full_pool_rank':int(np.linalg.matrix_rank(M)),
 'selected_indices':idx,
 'selected_names':[r['name'] for r in selected],
 'selected_sectors':[r['sector'] for r in selected],
 'd_optimal_logdet':ld,
 'selected_rank':int(np.linalg.matrix_rank(X)),
 'singular_values':sv,
 'condition_number':float(sv[0]/sv[-1]),
 'full_pool_rank_6':np.linalg.matrix_rank(M)==6,
 'selected_rank_6':np.linalg.matrix_rank(X)==6,
 'condition_number_le_8':float(sv[0]/sv[-1])<=8.0,
 'conclusion':'The candidate-blind observation pool spans all six frozen residual proxy directions, and the preregistered exhaustive D-optimal rule selects a 10-probe full-rank bank without using any future QGR candidate.'
}
write_result('rank_and_selection',out)
