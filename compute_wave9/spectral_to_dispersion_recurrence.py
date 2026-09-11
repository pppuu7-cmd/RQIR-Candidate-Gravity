#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path
from scipy.optimize import linprog

# Positive atomic spectral proxy in x=1/M^2.
# For a twice-subtracted pole representation,
# A_disp(s)=s^2 Sum_i w_i x_i^2/(1-s x_i),
# so the coefficient of s^(2+n) is m_(n+2)=Sum_i w_i x_i^(n+2).
x=np.array([0.1,0.3,0.7])
w=np.array([0.25,0.50,0.25])
m=np.array([np.sum(w*x**n) for n in range(12)])

# Infer exact rank-3 recurrence from m0..m5.
A=np.array([[m[n],m[n+1],m[n+2]] for n in range(3)])
b=np.array([m[n+3] for n in range(3)])
coef=np.linalg.solve(A,b)
seq=list(m[:6])
for n in range(3,9):
    val=float(coef[0]*seq[n]+coef[1]*seq[n+1]+coef[2]*seq[n+2])
    if n+3<len(seq): seq[n+3]=val
    else: seq.append(val)
pred=np.array(seq)
err=float(np.max(np.abs(pred[:len(m)]-m[:len(pred)])))

# Wilson/Taylor coefficients c_{2+n}=m_{2+n}.
wilson_true={str(2+n):float(m[2+n]) for n in range(8)}
wilson_pred={str(k):float(pred[k]) for k in range(2,min(10,len(pred)))}

# Without the rank axiom, match m0..m5 with arbitrary positive weights on a dense grid
# and ask for the allowed next coefficient m6 (coefficient of s^6).
grid=np.linspace(0.05,0.95,19)
Aeq=np.vstack([grid**n for n in range(6)])
beq=m[:6]
obj=grid**6
lo=linprog(obj,A_eq=Aeq,b_eq=beq,bounds=[(0,None)]*len(grid),method='highs')
hi=linprog(-obj,A_eq=Aeq,b_eq=beq,bounds=[(0,None)]*len(grid),method='highs')
if not (lo.success and hi.success):
    raise RuntimeError('positive moment LP failed')
m6_min=float(lo.fun); m6_max=float(-hi.fun)

out={
 "test":"finite spectral recurrence predicts a dispersive Wilson/Taylor tower",
 "spectral_x_inverse_mass_squared":x.tolist(),
 "spectral_weights":w.tolist(),
 "rank3_recurrence_coefficients":coef.tolist(),
 "recurrence_reconstruction_error":err,
 "true_dispersion_coefficients_by_power_s":wilson_true,
 "predicted_dispersion_coefficients_by_power_s":wilson_pred,
 "matched_moments_without_rank_axiom":"m0 through m5",
 "next_dispersion_coefficient_s6_true":float(m[6]),
 "next_dispersion_coefficient_s6_min_without_rank_axiom":m6_min,
 "next_dispersion_coefficient_s6_max_without_rank_axiom":m6_max,
 "next_dispersion_coefficient_width_without_rank_axiom":m6_max-m6_min,
 "rank3_law_closes_Wilson_tower":err<1e-12,
 "finite_positive_moments_alone_leave_next_Wilson_ambiguous":m6_max-m6_min>1e-10,
 "conclusion":"A finite spectral recurrence can propagate directly into an all-order dispersive EFT/Wilson tower. But with the same finite positive moment data and no structural rank law, the next Wilson coefficient remains an interval. The missing parent principle is therefore precisely the derivation of the spectral recurrence/rank, not the algebra that follows from it.",
 "scope":"atomic positive spectral/dispersion Taylor proxy; not a full graviton helicity-amplitude sum rule"
}
Path('wave9_results').mkdir(exist_ok=True)
Path('wave9_results/spectral_to_dispersion_recurrence.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
