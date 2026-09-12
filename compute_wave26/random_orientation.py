import numpy as np
from common import W, write_result
rng=np.random.default_rng(2602)
rows=[]
for r in [1,2,3,4]:
    hits=0
    trials=500
    for _ in range(trials):
        Q,_=np.linalg.qr(rng.normal(size=(6,6)))
        A=Q.T[:6-r]
        rank=int(np.linalg.matrix_rank(np.vstack([W,A]),tol=1e-10))
        hits += int(rank==6)
    frac=hits/trials
    rows.append({'r':r,'trials':trials,'closure_fraction':frac})
signal=all(x['closure_fraction']>=0.99 for x in rows if x['r']<=3) and next(x for x in rows if x['r']==4)['closure_fraction']==0.0
write_result('random_orientation',{'cases':rows,'random_orientation_closure_fraction_ge_0_99_for_r_le_3':signal})
