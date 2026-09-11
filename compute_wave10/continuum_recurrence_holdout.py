#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

# Uniform continuum moments m_n=1/(n+1). Fit order-r linear recurrences using exactly 2r design moments,
# then predict untouched moments. A true fixed finite recurrence would continue to close; a continuum should not.
m=np.array([1.0/(n+1) for n in range(80)],float)
records=[]
for r in [2,3,4,5,6,8,10]:
    # recurrence m_{n+r}=sum_{j=0}^{r-1} c_j m_{n+j}; solve using n=0..r-1 (2r moments)
    A=np.array([[m[n+j] for j in range(r)] for n in range(r)],float)
    b=np.array([m[n+r] for n in range(r)],float)
    c=np.linalg.solve(A,b)
    design_err=float(np.max(np.abs(A@c-b)))
    seq=list(m[:2*r])
    # recursively predict 12 untouched moments
    for n in range(r, r+12):
        idx=n+r
        val=float(sum(c[j]*seq[n+j] for j in range(r)))
        if idx < len(seq):
            seq[idx]=val
        else:
            seq.append(val)
    pred=np.array(seq[2*r:2*r+12])
    true=m[2*r:2*r+12]
    err=np.abs(pred-true)
    records.append({
      "recurrence_order":r,
      "design_moment_count":2*r,
      "coefficients":c.tolist(),
      "design_max_error":design_err,
      "holdout_max_abs_error":float(err.max()),
      "holdout_rms_error":float(np.sqrt(np.mean(err**2))),
      "first_holdout_error":float(err[0]),
      "last_holdout_error":float(err[-1])
    })

out={
 "test":"finite recurrence fitted to continuum moments and tested prospectively",
 "continuum_moments":"m_n=1/(n+1) for rho(x)=1 on [0,1]",
 "records":records,
 "every_finite_order_has_nonzero_holdout_error":all(q['holdout_max_abs_error']>1e-14 for q in records),
 "higher_order_can_approximate_better_without_exact_closure":records[-1]['holdout_max_abs_error']<records[0]['holdout_max_abs_error'],
 "conclusion":"For a genuine continuum moment sequence, any chosen finite recurrence can interpolate a finite design window but fails untouched higher moments. Increasing order can improve the approximation, yet there is no fixed finite recurrence that becomes exact. This distinguishes finite-data Padé/Prony compression from an exact continuum parent law.",
 "scope":"uniform-continuum moment proxy; floating-point conditioning worsens at large recurrence order, so only the qualitative nonzero-holdout pattern is used."
}
Path('wave10_results').mkdir(exist_ok=True)
Path('wave10_results/continuum_recurrence_holdout.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
