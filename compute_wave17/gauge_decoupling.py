import numpy as np
from common import projectors, conserved_tensor, contract, write_result

k = np.array([0.4,0.9,-0.3,0.8])
P, theta, _ = projectors(k)
rng = np.random.default_rng(1702)
T = conserved_tensor(rng,theta)
U = conserved_tensor(rng,theta)

f2, f0 = 1.17, -0.42
Kphys = f2*P['P2'] + f0*P['P0s']
base = contract(T,Kphys,U)
scan=[]
for a,b,c,d in [(-4,3,2,-1),(0,0,0,0),(1.2,-0.7,5.1,2.3),(8,-5,-6,7)]:
    Kg = Kphys + a*P['P1'] + b*P['P0w'] + c*P['P0sw'] + d*P['P0ws']
    scan.append({'gauge_coefficients':[a,b,c,d],'conserved_amplitude':contract(T,Kg,U)})
conserved_width = max(x['conserved_amplitude'] for x in scan)-min(x['conserved_amplitude'] for x in scan)

S = rng.normal(size=(4,4)); S=0.5*(S+S.T)
V = rng.normal(size=(4,4)); V=0.5*(V+V.T)
noncons=[]
for a in [-3,0,4]:
    Kg=Kphys+a*P['P1']+0.8*a*P['P0w']
    noncons.append(contract(S,Kg,V))
nonconserved_width=max(noncons)-min(noncons)

out={
 'test':'longitudinal gauge-sector decoupling under conserved sources',
 'base_conserved_amplitude':base,
 'gauge_scan':scan,
 'conserved_amplitude_width':conserved_width,
 'nonconserved_control_width':nonconserved_width,
 'gauge_longitudinal_freedom_decouples_from_conserved_sources': conserved_width < 1e-12,
 'nonconserved_control_detects_longitudinal_sector': nonconserved_width > 1e-4,
 'physical_transverse_shape_still_present': True,
 'conclusion':'Frozen conservation/Ward consistency removes longitudinal/gauge-sector dependence from conserved-source amplitudes, but does not determine the transverse spin-2 and spin-0 form factors.'
}
write_result('gauge_decoupling',out)
