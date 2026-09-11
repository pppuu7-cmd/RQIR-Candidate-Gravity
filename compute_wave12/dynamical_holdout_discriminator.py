#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from scipy.linalg import expm,eigvals

a,b=1.7,2.4
x=np.array([0.1,0.3,0.5,0.7,0.9])
pi=x**(a-1)*(1-x)**(b-1); pi=pi/pi.sum()
patterns={"uniform":[1,1,1,1],"center_heavy":[0.5,2,2,0.5],"alternating":[2,0.5,2,0.5]}

def makeQ(cs):
    Q=np.zeros((5,5))
    for i,c in enumerate(cs):
        Q[i,i+1]=c/pi[i]; Q[i+1,i]=c/pi[i+1]
    for i in range(5): Q[i,i]=-Q[i].sum()
    ev=np.sort(np.maximum(np.real(eigvals(-Q)),0.0)); gap=ev[ev>1e-9][0]
    return Q/gap

g=x-float(np.dot(pi,x))
times=[0.15,0.5,1.5,4.0]
records=[]
for name,cs in patterns.items():
    Q=makeQ(cs)
    vals=[]
    for t in times:
        P=expm(t*Q)
        vals.append(float(np.dot(pi*g,P@g)))
    records.append({"pattern":name,"autocovariance_holdouts":vals})
widths=[]
for j,t in enumerate(times):
    vv=[r['autocovariance_holdouts'][j] for r in records]
    widths.append(float(max(vv)-min(vv)))
out={
 "test":"prospective time-domain holdouts distinguish generators left degenerate by stationary data and first gap",
 "observable":"stationary autocovariance of x",
 "times":times,
 "records":records,
 "holdout_widths":widths,
 "max_holdout_width":float(max(widths)),
 "dynamical_holdouts_discriminate_surviving_family":bool(max(widths)>1e-4),
 "conclusion":"Stationary density plus leading relaxation time does not close the dynamics. Untouched time-domain correlation observables distinguish generators that pass the same semigroup, positivity, detailed-balance and unit-gap gates."
}
Path('wave12_results').mkdir(exist_ok=True)
Path('wave12_results/dynamical_holdout_discriminator.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
