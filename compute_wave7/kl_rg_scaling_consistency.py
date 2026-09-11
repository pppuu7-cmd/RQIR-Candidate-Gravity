#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

# Standard Euclidean Kallen-Lehmann proxy with nonnegative normalized spectral weight.
# D(Q^2)=sum_i w_i/(Q^2+m_i^2), w_i>=0, sum w_i=1.
# Then Q^2 D(Q^2)->1 for Q^2->infinity for any finite normalized measure.
m2=np.array([0.0,0.8,2.5,7.0,20.0])
w=np.array([0.55,0.16,0.12,0.10,0.07])
assert abs(w.sum()-1)<1e-12
Q2=np.logspace(-2,8,220)
D=np.array([np.sum(w/(q+m2)) for q in Q2])
scaled=Q2*D

# Compare with a q^-4-type UV target normalized to match GR in the deep IR.
M2=10.0
D_soft=1.0/(Q2*(1.0+Q2/M2))
scaled_soft=Q2*D_soft

out={
 "test":"standard normalized positive KL proxy versus q^-4-type UV softening",
 "spectral_masses_squared":m2.tolist(),
 "spectral_weights":w.tolist(),
 "total_spectral_weight":float(w.sum()),
 "Q2D_at_largest_Q2":float(scaled[-1]),
 "Q2D_expected_limit":1.0,
 "soft_target_Q2D_at_largest_Q2":float(scaled_soft[-1]),
 "soft_target_expected_limit":0.0,
 "simultaneous_naive_conditions_compatible":False,
 "interpretation":"A standard positive normalized KL representation has 1/Q^2 asymptotics. Therefore one must not simultaneously impose that representation and a naive 1/Q^4 propagator scaling on the same renormalized field without additional structure or a scheme/field distinction.",
 "important_scope":"This is not a no-go against asymptotic safety. Modern Lorentzian FRG work reports positive graviton spectral functions; the point is that fixed-point anomalous scaling, spectral normalization, gauge/field definitions and renormalization scheme must be matched consistently rather than combined naively."
}
Path('wave7_results').mkdir(exist_ok=True)
Path('wave7_results/kl_rg_scaling_consistency.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
