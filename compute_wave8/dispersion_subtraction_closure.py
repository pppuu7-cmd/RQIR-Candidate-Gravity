#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

# Twice-subtracted dispersion proxy with the absorptive/spectral part treated as known.
# A(s) = a0 + a1*s + s^2 * Sum_i r_i/[M_i^2 (M_i^2-s)]
M2=np.array([4.0,9.0,25.0])
r=np.array([0.8,0.5,0.3])

def disp(s):
    return float(s*s*np.sum(r/(M2*(M2-s))))

def amp(s,a0,a1):
    return a0+a1*s+disp(s)

true=np.array([0.17,-0.08])
design_s=np.array([-0.5,-1.25])
holdout_s=-2.0
y=np.array([amp(s,*true) for s in design_s])
# Subtract known dispersive part, solve two subtraction constants.
B=np.column_stack([np.ones_like(design_s),design_s])
rhs=y-np.array([disp(s) for s in design_s])
sol=np.linalg.solve(B,rhs)
holdout_true=amp(holdout_s,*true)
holdout_pred=amp(holdout_s,*sol)

# Without the two low-energy design conditions, scan subtraction constants.
vals=[]
for a0 in np.linspace(-0.5,0.5,41):
 for a1 in np.linspace(-0.3,0.3,41):
  vals.append(amp(holdout_s,a0,a1))

out={
 "test":"two-subtraction dispersion closure and untouched holdout",
 "spectral_masses_squared":M2.tolist(),
 "spectral_residues":r.tolist(),
 "subtraction_constant_count_before_low_energy_inputs":2,
 "design_points":design_s.tolist(),
 "design_amplitudes":y.tolist(),
 "recovered_subtraction_constants":sol.tolist(),
 "true_subtraction_constants":true.tolist(),
 "solve_error_max_abs":float(np.max(np.abs(sol-true))),
 "holdout_s":holdout_s,
 "holdout_true":float(holdout_true),
 "holdout_predicted":float(holdout_pred),
 "holdout_error_abs":float(abs(holdout_pred-holdout_true)),
 "holdout_width_without_subtraction_inputs":float(max(vals)-min(vals)),
 "conclusion":"A twice-subtracted dispersive representation leaves exactly two polynomial data in this proxy. Two independent low-energy inputs close them and then produce a genuine holdout prediction; the dispersion relation alone does not determine them.",
 "scope":"finite pole proxy for subtraction bookkeeping; not a full gravitational amplitude dispersion integral"
}
Path('wave8_results').mkdir(exist_ok=True)
Path('wave8_results/dispersion_subtraction_closure.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
