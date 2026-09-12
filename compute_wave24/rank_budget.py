import numpy as np
from common import L1,L3,write_result

r1=int(np.linalg.matrix_rank(L1,tol=1e-12))
r3=int(np.linalg.matrix_rank(L3,tol=1e-12))
out={
 'test':'local information-rank budget on six-dimensional frozen residual space',
 'baseline_dimension':6,
 'S0_rank':0,
 'S0_nullity':6,
 'S1_rank':r1,
 'S1_nullity':6-r1,
 'S2_rank':r3,
 'S2_nullity':6-r3,
 'scalar_relation_leaves_nullity_5':r1==1 and 6-r1==5,
 'three_relation_class_leaves_nullity_3':r3==3 and 6-r3==3,
 'minimum_additional_independent_local_equalities_needed_after_S2':6-r3,
 'conclusion':'Partial consistency relations can reduce the residual class without selecting a unique theory. In this frozen proxy, one scalar relation leaves five directions and three independent relations leave three.'
}
write_result('rank_budget',out)
