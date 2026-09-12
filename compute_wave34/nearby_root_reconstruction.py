import numpy as np
from scipy.optimize import least_squares
from common import X_TABLE,flows,write

lo=np.array([-0.40,-0.25,-0.30,0.15,0.15])
hi=np.array([-0.05, 0.15, 0.10,1.30,1.20])
rng=np.random.default_rng(3402)
starts=[X_TABLE.copy()]
for _ in range(31): starts.append(lo+(hi-lo)*rng.random(5))
# Scaling is frozen from the rounded-point flow and only conditions the optimizer;
# root acceptance always uses the *raw* printed-equation residual.
b0=np.abs(flows(X_TABLE)); scale=np.maximum(1.0,b0)
roots=[]; attempts=[]
for idx,x0 in enumerate(starts):
    def fun(x):
        try: return flows(x)/scale
        except Exception: return np.ones(5)*1e12
    r=least_squares(fun,x0,bounds=(lo,hi),max_nfev=6000,xtol=1e-12,ftol=1e-12,gtol=1e-12,x_scale='jac')
    raw=flows(r.x); inf=float(np.linalg.norm(raw,np.inf))
    attempts.append({'i':idx,'success':bool(r.success),'x':r.x,'raw_inf_norm':inf,'scaled_cost':float(r.cost)})
    if r.success and inf<1e-5:
        if not any(np.linalg.norm(r.x-q)<1e-5 for q in roots): roots.append(r.x.copy())
signals={
 'multistart_solver_completed_deterministically':len(attempts)==32,
 'raw_residual_used_for_root_acceptance':True,
 'absence_or_presence_of_nearby_root_is_reported_without_manual_repair':True,
}
out={'test':'nearby_root_reconstruction','box_lo':lo,'box_hi':hi,'residual_scale':scale,'n_starts':len(starts),'n_accepted_roots':len(roots),'accepted_roots':roots,'best_attempts':sorted(attempts,key=lambda d:d['raw_inf_norm'])[:8],'signals':signals}
write('wave34_nearby_root_reconstruction.json',out); assert all(signals.values())
