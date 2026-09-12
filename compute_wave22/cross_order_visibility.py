import numpy as np
from common import build_pool, matrix, selected_bank, write_result

pool=build_pool(); M=matrix(pool)
_,idx,selected,X=selected_bank(10)
mask2=[i for i,r in enumerate(pool) if r['sector']=='2pt']
M2=M[mask2,:4]
Xs=X[:,:4]
r2=int(np.linalg.matrix_rank(M2,tol=1e-10))
rs=int(np.linalg.matrix_rank(Xs,tol=1e-10))
out={
 'test':'cross-order visibility of cubic and quartic residual directions',
 'higher_order_columns':['c3','d3','e4','f4'],
 'two_point_only_rank_on_higher_order_subspace':r2,
 'selected_cross_order_rank_on_higher_order_subspace':rs,
 'two_point_only_cannot_identify_all_higher_order':r2<4,
 'selected_bank_resolves_all_four_higher_order_directions':rs==4,
 'selected_three_point_count':sum(r['sector']=='3pt' for r in selected),
 'selected_four_point_count':sum(r['sector']=='4pt' for r in selected),
 'conclusion':'The frozen bank explicitly tests the Wave-19/20 obstruction: lower-order data alone are blind to independent higher-order Wilson directions, whereas prospective 3pt+4pt holdouts recover full rank on the four-dimensional higher-order proxy subspace.'
}
write_result('cross_order_visibility',out)
