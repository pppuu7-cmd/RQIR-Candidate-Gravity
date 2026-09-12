import numpy as np
from common import W, write_result
rows=[]
for r in [1,2,3,4]:
    A=np.eye(6)[:6-r]
    M=np.vstack([W,A])
    rank=int(np.linalg.matrix_rank(M,tol=1e-10))
    rows.append({'r':r,'rank_A':int(np.linalg.matrix_rank(A)),'combined_rank':rank,'nullity':6-rank})
s1=all(x['combined_rank']==6 for x in rows if x['r']<=3)
s2=next(x for x in rows if x['r']==4)['combined_rank']==5
write_result('canonical_transverse',{'cases':rows,'canonical_transverse_examples_close_for_r_le_3':s1,'r4_cannot_close_by_dimension_count':s2})
