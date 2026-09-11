#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from scipy.optimize import linprog

# Target positive spectral measure with three atoms.
x_true=np.array([0.18,0.47,0.83])
w_true=np.array([0.22,0.51,0.27])
max_n=10
mom=np.array([np.sum(w_true*x_true**n) for n in range(max_n+1)])

# If a rank-3 recurrence is postulated, first six moments determine the recurrence coefficients.
# m_{n+3}=c0*m_n+c1*m_{n+1}+c2*m_{n+2}
A=[]; b=[]
for n in range(3):
 A.append([mom[n],mom[n+1],mom[n+2]])
 b.append(mom[n+3])
coef=np.linalg.solve(np.array(A),np.array(b))
pred=[]
seq=list(mom[:6])
for n in range(3,8):
 val=float(coef[0]*seq[n]+coef[1]*seq[n+1]+coef[2]*seq[n+2])
 if n+3 < len(seq):
  seq[n+3]=val
 else:
  seq.append(val)
 pred.append(val)
recurrence_error=max(abs(pred[i]-mom[i+6]) for i in range(len(pred)))

# Without fixing the finite-rank recurrence ansatz, match only finitely many moments on a denser positive support.
grid=np.linspace(0.05,0.95,19)
results=[]
for K in [2,3,4,5,6]:
 Aeq=np.vstack([grid**n for n in range(K+1)])
 beq=mom[:K+1]
 objective=grid**(K+1)
 lo=linprog(objective,A_eq=Aeq,b_eq=beq,bounds=[(0,None)]*len(grid),method='highs')
 hi=linprog(-objective,A_eq=Aeq,b_eq=beq,bounds=[(0,None)]*len(grid),method='highs')
 if lo.success and hi.success:
  vmin=float(lo.fun)
  vmax=float(-hi.fun)
  results.append({"matched_moment_order":K,"next_moment_min":vmin,"next_moment_max":vmax,"width":vmax-vmin,"unique":abs(vmax-vmin)<1e-10})
 else:
  results.append({"matched_moment_order":K,"lp_success":False,"lo":lo.message,"hi":hi.message})

out={
 "test":"finite spectral data versus finite-rank recurrence closure",
 "true_support":x_true.tolist(),
 "true_weights":w_true.tolist(),
 "rank3_recurrence_coefficients":coef.tolist(),
 "rank3_recurrence_max_error":float(recurrence_error),
 "finite_moment_positive_measure_ranges":results,
 "closure_requires_rank_assumption":True,
 "conclusion":"A finite-rank recurrence can turn finite data into an all-order sequence, but the recurrence rank/form is extra microscopic information; positivity plus finitely many moments alone leaves alternative positive measures.",
 "scope":"finite Stieltjes-moment/atomic-measure proxy, not a theorem for the full graviton spectral measure"
}
Path('wave6_results').mkdir(exist_ok=True)
Path('wave6_results/spectral_recurrence_closure.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
