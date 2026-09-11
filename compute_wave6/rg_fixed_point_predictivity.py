#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

# Linearized UV fixed-point proxy: g_i(k)=g_i*+C_i (k/k0)^(-theta_i).
# theta>0 directions are UV-attractive/relevant in this convention and carry free amplitudes.
theta=np.array([3.2,1.7,0.4,-0.6,-1.3,-2.1,-3.2,-4.5],float)
relevant=np.where(theta>0)[0]
irrelevant=np.where(theta<0)[0]

# UV-complete critical surface sets the UV-repulsive amplitudes to their fixed values.
# The surviving trajectory is still parameterized by the relevant amplitudes.
M=np.array([
 [1.0,0.25,-0.15],
 [0.1,1.0,0.30],
 [-0.2,0.35,1.0],
 [0.5,-0.4,0.2],
],float)

samples=[]
for c0 in (-0.4,-0.2,0.0,0.2,0.4):
 for c1 in (-0.3,-0.15,0.0,0.15,0.3):
  for c2 in (-0.2,-0.1,0.0,0.1,0.2):
   c=np.array([c0,c1,c2])
   obs=M@c
   samples.append(obs.tolist())
arr=np.array(samples)
widths=(arr.max(axis=0)-arr.min(axis=0)).tolist()

# Three independent IR conditions can solve the three relevant amplitudes in this proxy.
M3=M[:3,:]
target=np.array([0.11,-0.07,0.04])
solution=np.linalg.solve(M3,target)
residual=float(np.max(np.abs(M3@solution-target)))

out={
 "test":"finite-dimensional UV critical surface: predictivity versus uniqueness",
 "critical_exponents":theta.tolist(),
 "relevant_direction_count":int(len(relevant)),
 "irrelevant_direction_count":int(len(irrelevant)),
 "uv_complete_trajectory_parameter_count":int(len(relevant)),
 "sampled_trajectory_count":int(len(samples)),
 "ir_observable_widths_over_critical_surface":widths,
 "unique_without_ir_boundary_data":False,
 "ir_conditions_needed_in_linear_proxy":int(len(relevant)),
 "example_ir_target":target.tolist(),
 "solved_relevant_amplitudes":solution.tolist(),
 "solve_residual_max_abs":residual,
 "conclusion":"A fixed point with finitely many relevant directions yields a finite predictive family, not a unique trajectory; uniqueness additionally needs the relevant parameters fixed by boundary/observational data or a deeper rule.",
 "scope":"linearized RG proxy; not a computation of the Reuter fixed point"
}
Path('wave6_results').mkdir(exist_ok=True)
Path('wave6_results/rg_fixed_point_predictivity.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
