#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from scipy.linalg import expm,eigvals

a,b=1.7,2.4
x=np.array([0.1,0.3,0.5,0.7,0.9])
pi=x**(a-1)*(1-x)**(b-1)
pi=pi/pi.sum()
patterns={
 "uniform":[1,1,1,1],
 "center_heavy":[0.5,2.0,2.0,0.5],
 "alternating":[2.0,0.5,2.0,0.5]
}

def makeQ(cs):
    Q=np.zeros((len(pi),len(pi)))
    for i,c in enumerate(cs):
        Q[i,i+1]=c/pi[i]
        Q[i+1,i]=c/pi[i+1]
    for i in range(len(pi)):
        Q[i,i]=-Q[i].sum()
    ev=np.sort(np.maximum(np.real(eigvals(-Q)),0.0))
    gap=ev[ev>1e-9][0]
    return Q/gap,float(gap)

records=[]
for name,cs in patterns.items():
    Q,gap=makeQ(cs)
    ev=np.sort(np.maximum(np.real(eigvals(-Q)),0.0))
    P03=expm(0.3*Q); P07=expm(0.7*Q); P10=expm(Q)
    sem=float(np.max(np.abs(P03@P07-P10)))
    records.append({
      "pattern":name,"raw_gap":gap,
      "scaled_eigenvalues":[float(v) for v in ev],
      "stationarity_error":float(np.max(np.abs(pi@Q))),
      "row_sum_error_t1":float(np.max(np.abs(P10.sum(axis=1)-1.0))),
      "minimum_transition_probability_t1":float(P10.min()),
      "semigroup_error_0p3_plus_0p7":sem
    })
second=[r['scaled_eigenvalues'][2] for r in records]
out={
 "test":"independent finite-state Markov-semigroup counterexample",
 "stationary_distribution":[float(v) for v in pi],
 "records":records,
 "higher_mode_width_after_unit_gap":float(max(second)-min(second)),
 "all_semigroup_checks_pass":all(r['semigroup_error_0p3_plus_0p7']<1e-10 for r in records),
 "all_positivity_normalization_stationarity_checks_pass":all(r['minimum_transition_probability_t1']>-1e-12 and r['row_sum_error_t1']<1e-10 and r['stationarity_error']<1e-10 for r in records),
 "semigroup_positivity_stationarity_and_gap_do_not_fix_generator":bool(max(second)-min(second)>1e-3),
 "conclusion":"Even outside the diffusion ansatz, multiple reversible continuous-time Markov generators can share the same stationary measure and unit spectral gap while satisfying exact semigroup composition, positivity and normalization, yet possess different higher relaxation modes."
}
Path('wave12_results').mkdir(exist_ok=True)
Path('wave12_results/semigroup_ctmc_counterexample.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
