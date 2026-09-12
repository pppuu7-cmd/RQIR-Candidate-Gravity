import numpy as np
from common import X_TABLE,flows,jacobian,write
rng=np.random.default_rng(3403)
# Half-units implied by displayed decimals: 2,3,2,2,2 decimal places.
half=np.array([0.005,0.0005,0.005,0.005,0.005])
N=1200
res=[]; cond=[]
for _ in range(N):
    x=X_TABLE+rng.uniform(-1,1,size=5)*half
    b=flows(x); J=jacobian(x,3e-6); s=np.linalg.svd(J,compute_uv=False)
    res.append(float(np.linalg.norm(b,np.inf))); cond.append(float(s[0]/s[-1]))
res=np.array(res); cond=np.array(cond)
signals={
 'full_decimal_rounding_cell_sampled':len(res)==N,
 'residual_spread_due_to_published_rounding_is_nonzero':float(np.ptp(res))>0,
 'conditioning_spread_is_reported_without_retuning':bool(np.all(np.isfinite(cond))),
}
out={'test':'rounding_sensitivity','n_samples':N,'half_widths':half,'residual_inf_min':float(res.min()),'residual_inf_median':float(np.median(res)),'residual_inf_max':float(res.max()),'residual_inf_width':float(np.ptp(res)),'condition_min':float(cond.min()),'condition_median':float(np.median(cond)),'condition_max':float(cond.max()),'signals':signals}
write('wave34_rounding_sensitivity.json',out); assert all(signals.values())
