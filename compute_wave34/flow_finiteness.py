import numpy as np
from common import X_TABLE,flows,write
rng=np.random.default_rng(3401)
points=[X_TABLE.copy()]
scales=np.array([0.01,0.01,0.01,0.03,0.03])
for _ in range(250):
    x=X_TABLE+rng.normal(size=5)*scales
    if 1+x[0]>0 and x[3]>0 and x[4]>0:
        points.append(x)
finite=[]; norms=[]
for x in points:
    try:
        b=flows(x); ok=bool(np.all(np.isfinite(b)))
    except Exception:
        ok=False; b=None
    finite.append(ok)
    if ok: norms.append(float(np.linalg.norm(b,np.inf)))
signals={
 'shared_F1_F5_implementation_is_finite_near_table_point':all(finite),
 'neighbourhood_contains_at_least_200_valid_points':len(norms)>=200,
}
out={'test':'flow_finiteness','n_points':len(points),'n_finite':sum(finite),'rounded_point_flow':flows(X_TABLE),'residual_inf_norm_median':float(np.median(norms)),'residual_inf_norm_max':float(np.max(norms)),'signals':signals}
write('wave34_flow_finiteness.json',out); assert all(signals.values())
