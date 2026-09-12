import numpy as np
from common import W, write_result
I=np.eye(6)
examples={
 1:np.vstack([W,I[3],I[4]]),
 2:np.vstack([W,I[3]]),
 3:W.copy()
}
rows=[]
for r,A in examples.items():
    rankA=int(np.linalg.matrix_rank(A,tol=1e-10))
    combined=int(np.linalg.matrix_rank(np.vstack([W,A]),tol=1e-10))
    rows.append({'r':r,'required_rank_A':6-r,'rank_A':rankA,'combined_rank':combined,'residual_nullity':6-combined})
signal=all(x['rank_A']==x['required_rank_A'] and x['residual_nullity']>0 for x in rows)
write_result('aligned_redundancy',{'cases':rows,'aligned_redundancy_counterexamples_prevent_universal_closure':signal})
