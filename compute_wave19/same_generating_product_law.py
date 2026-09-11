import numpy as np
from common import write_result

# Restricted same-generating-law proxy.
# Two-point dressing E(x)=exp(-lambda x) is assumed from the preregistered Wave-18 H2 finite class.
# Add a stronger cross-order hypothesis: the reduced 3-point dressing is the product of the same E
# on the three legs, V(x,y,z)=E(x)E(y)E(z). No new vertex parameter is allowed.
xd=0.25; target=0.90
lam=-np.log(target)/xd
def E(x): return float(np.exp(-lam*x))
def V(x,y,z): return float(E(x)*E(y)*E(z))
triples=[(0.1,0.2,0.3),(0.25,0.25,0.25),(0.4,0.55,0.7)]
vals=[{'kinematics':[x,y,z],'V':V(x,y,z)} for x,y,z in triples]
# test multiplicative leg factorisation identities
res=[]
for x,y,z in triples:
    res.append(abs(V(x,y,z)-E(x)*E(y)*E(z)))
out={
 'test':'restricted same-generating-law/product closure across two-point and three-point sectors',
 'two_point_rate':lam,'two_point_design':E(xd),'two_point_target':target,
 'three_point_predictions':vals,
 'max_factorisation_residual':max(res),
 'new_three_point_parameters':0,
 'cross_order_predictive_inside_restricted_product_class':max(res)<1e-14,
 'physical_uniqueness_established':False,
 'conclusion':'If one adds the strong product-law hypothesis that the same exponential dressing independently multiplies all three external legs, the two-point design fixes a parameter-free three-point prediction. This demonstrates the kind of cross-order law needed for predictivity, but the product rule is an additional modeling postulate and is not derived from frozen RQIR or Ward identities.'
}
write_result('same_generating_product_law',out)
