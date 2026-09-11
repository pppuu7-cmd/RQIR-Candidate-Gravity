import numpy as np
from common import write_result, X_DESIGN, X_HOLD, TARGET

# H4: linearized UV-fixed-point trajectory proxy with three UV-attractive/relevant amplitudes.
# E(x)=E* + sum c_i (1+x)^(-theta_i). UV fixed point fixes E*, while amplitudes label critical-surface trajectories.
E_star=0.60
theta=np.array([0.7,1.4,2.2])
phi0=np.ones(3)
phid=(1+X_DESIGN)**(-theta)
A=np.vstack([phi0,phid])
b=np.array([1-E_star,TARGET-E_star])
rank=int(np.linalg.matrix_rank(A)); nullity=3-rank
part=np.linalg.lstsq(A,b,rcond=None)[0]
_,_,vt=np.linalg.svd(A,full_matrices=True)
n=vt[-1]/np.linalg.norm(vt[-1])
# choose a small symmetric excursion, reducing if positivity on [0,1.2] would fail
amp=0.25
grid=np.linspace(0,1.2,61)
def E(c,x): return float(E_star+np.sum(c*(1+x)**(-theta)))
while amp>1e-6:
    cs=[part-amp*n,part+amp*n]
    if all(min(E(c,x) for x in grid)>0 for c in cs): break
    amp*=0.5
vals=[{'amplitudes':c.tolist(),'IR':E(c,0.0),'design':E(c,X_DESIGN),'holdout':E(c,X_HOLD),'min_grid':min(E(c,x) for x in grid)} for c in cs]
dw=max(z['design'] for z in vals)-min(z['design'] for z in vals)
hw=max(z['holdout'] for z in vals)-min(z['holdout'] for z in vals)
out={
 'hypothesis':'H4 UV fixed-point / finite critical-surface trajectory proxy',
 'physical_motivation':'asymptotic-safety-style UV fixed point with a finite number of UV-attractive/relevant directions',
 'fixed_point_value':E_star,'critical_exponents':theta.tolist(),
 'constraint_rank':rank,'trajectory_nullity_after_IR_and_one_design':nullity,
 'candidates':vals,'design_width':dw,'holdout_width':hw,
 'UV_fixed_point_alone_does_not_select_trajectory':nullity>0 and dw<1e-10 and hw>1e-5,
 'novelty_credit':False,
 'conclusion':'A UV fixed point plus finitely many relevant directions improves predictivity but does not by itself select the physical trajectory. With three relevant amplitudes, GR IR normalization and one design datum still leave a direction that changes the prospective holdout. This is comparator-compatible RG behavior rather than a unique RQIR-derived law.'
}
write_result('h4_rg_fixed_point',out)
