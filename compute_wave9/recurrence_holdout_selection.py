#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

x=np.array([0.1,0.3,0.7])
w=np.array([0.25,0.50,0.25])
m=np.array([np.sum(w*x**n) for n in range(12)])

# Same first six moments are the design data.
design=m[:6].copy()

# Rank-2 recurrence fitted in least squares to all recurrence relations available inside m0..m5.
A2=np.array([[m[n],m[n+1]] for n in range(4)])
b2=np.array([m[n+2] for n in range(4)])
c2=np.linalg.lstsq(A2,b2,rcond=None)[0]
design_resid2=float(np.max(np.abs(A2@c2-b2)))
seq2=list(design)
for n in range(4,9):
    seq2.append(float(c2[0]*seq2[n]+c2[1]*seq2[n+1]))
hold2=np.array(seq2[6:11])

# Rank-3 recurrence exactly determined by the same m0..m5 design data.
A3=np.array([[m[n],m[n+1],m[n+2]] for n in range(3)])
b3=np.array([m[n+3] for n in range(3)])
c3=np.linalg.solve(A3,b3)
design_resid3=float(np.max(np.abs(A3@c3-b3)))
seq3=list(design)
for n in range(3,8):
    seq3.append(float(c3[0]*seq3[n]+c3[1]*seq3[n+1]+c3[2]*seq3[n+2]))
hold3=np.array(seq3[6:11])
true_hold=m[6:11]

out={
 "test":"recurrence order selection by untouched dispersive/spectral holdouts",
 "design_moments_m0_to_m5":design.tolist(),
 "rank2_coefficients":c2.tolist(),
 "rank2_design_recurrence_residual":design_resid2,
 "rank2_holdout_m6_to_m10":hold2.tolist(),
 "rank2_holdout_max_error":float(np.max(np.abs(hold2-true_hold))),
 "rank3_coefficients":c3.tolist(),
 "rank3_design_recurrence_residual":design_resid3,
 "rank3_holdout_m6_to_m10":hold3.tolist(),
 "true_holdout_m6_to_m10":true_hold.tolist(),
 "rank3_holdout_max_error":float(np.max(np.abs(hold3-true_hold))),
 "rank3_passes_holdout":float(np.max(np.abs(hold3-true_hold)))<1e-12,
 "rank2_fails_holdout":float(np.max(np.abs(hold2-true_hold)))>1e-5,
 "conclusion":"Untouched higher moments/Wilson coefficients can discriminate an assumed closure order. In this synthetic rank-3 system the rank-3 law predicts five holdouts to numerical precision, while a rank-2 closure fitted to the same first six moments fails. This is the prospective validation pattern required of any proposed physical recurrence law.",
 "scope":"synthetic finite-rank moment model; not evidence that gravity has rank-3 spectral closure"
}
Path('wave9_results').mkdir(exist_ok=True)
Path('wave9_results/recurrence_holdout_selection.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
