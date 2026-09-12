import numpy as np
from common import L3, write_result
rank=int(np.linalg.matrix_rank(L3)); nullity=6-rank
out={'principle':'K1_soft_ward','rank':rank,'residual_nullity':nullity,'soft_ward_leaves_residual_nullity':bool(rank==3 and nullity==3),'PL1':'FAIL','PL2':'PASS','PL3':'FAIL','PL4':'PASS','PL5':'PASS'}
write_result('soft_ward',out)
