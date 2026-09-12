import itertools
import numpy as np
from common import X_and_probes, write_result

X,probes=X_and_probes(); n=len(probes)
loo=[]
for i in range(n):
    keep=[j for j in range(n) if j!=i]
    r=int(np.linalg.matrix_rank(X[keep],tol=1e-10))
    loo.append({'dropped':probes[i]['name'],'rank':r})
lto=[]
for a,b in itertools.combinations(range(n),2):
    keep=[j for j in range(n) if j not in (a,b)]
    r=int(np.linalg.matrix_rank(X[keep],tol=1e-10))
    lto.append({'dropped':[probes[a]['name'],probes[b]['name']],'rank':r})
loo_frac=sum(x['rank']==6 for x in loo)/len(loo)
lto_frac=sum(x['rank']==6 for x in lto)/len(lto)
out={
 'test':'leave-one / leave-two probe deletion jackknife',
 'leave_one':loo,
 'leave_two_rank_histogram':{str(k):sum(x['rank']==k for x in lto) for k in sorted(set(x['rank'] for x in lto))},
 'leave_one_full_rank_fraction':loo_frac,
 'leave_two_full_rank_fraction':lto_frac,
 'all_leave_one_rank_6':loo_frac==1.0,
 'leave_two_full_rank_fraction_ge_0_80':lto_frac>=0.80,
 'conclusion':'Jackknife quantifies whether the frozen exam depends critically on one or two special probes rather than distributed cross-order information.'
}
write_result('jackknife',out)
