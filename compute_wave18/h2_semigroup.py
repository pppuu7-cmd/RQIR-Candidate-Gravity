import numpy as np
from common import write_result, X_DESIGN, X_HOLD, TARGET

# H2: multiplicative scale-composition law E(x+y)=E(x)E(y).
# For E=exp(g), this is additivity g(x+y)=g(x)+g(y). On a cubic log-basis,
# composition kills quadratic/cubic coefficients and leaves one rate; one design datum then fixes it.
pairs=[(0.1,0.2),(0.15,0.35),(0.2,0.4),(0.3,0.25)]
rows=[]
for x,y in pairs:
    rows.append([(x+y)-x-y,(x+y)**2-x**2-y**2,(x+y)**3-x**3-y**3])
C=np.asarray(rows,float)
rank=int(np.linalg.matrix_rank(C,tol=1e-12)); nullity=3-rank
s=np.linalg.svd(C,compute_uv=False)
rate=-np.log(TARGET)/X_DESIGN
# With c1=-rate, c2=c3=0, E=exp(-rate*x)
def E(x): return float(np.exp(-rate*x))
# independent composition residual scan
res=[]
for x,y in pairs:
    res.append(abs(E(x+y)-E(x)*E(y)))
out={
 'hypothesis':'H2 multiplicative scale-composition / semigroup law',
 'physical_motivation':'coarse-graining or finite-resolution composition acts by the same physical dressing in successive scale increments',
 'composition_matrix_rank_on_cubic_log_basis':rank,
 'shape_nullity_before_design':nullity,
 'composition_singular_values':s.tolist(),
 'fitted_rate_from_design':rate,
 'design_value':E(X_DESIGN),'target':TARGET,
 'prospective_holdout_x':X_HOLD,'prospective_holdout':E(X_HOLD),
 'max_composition_residual':max(res),
 'composition_plus_one_design_closes_this_finite_class': rank==2 and nullity==1 and abs(E(X_DESIGN)-TARGET)<1e-12 and max(res)<1e-12,
 'novelty_credit':False,
 'conclusion':'The semigroup law is strong enough to collapse a cubic log-form-factor family to an exponential one-parameter class, and one design datum then predicts the holdout. But scale composition by itself is not gravity-specific and exponential/common-form-factor structures have known comparator analogues; closure inside this ansatz is not yet a new QG primitive.'
}
write_result('h2_semigroup',out)
