import numpy as np
from common import write_result, X_DESIGN, X_HOLD, TARGET

# H1: independently motivated no-new-pole/common-form-factor proxy.
# The GR tensor structure is multiplied by one shared zero-free entire factor E(x)=exp(g(x)),
# g(x)=c1 x+c2 x^2+c3 x^3. This is stronger than Wave 17 but still leaves functional shape.
xd=X_DESIGN; xh=X_HOLD; y=np.log(TARGET)
row=np.array([xd,xd**2,xd**3])
# minimum-norm particular solution to row.c=y
part=row*y/(row@row)
_,_,vt=np.linalg.svd(row.reshape(1,3),full_matrices=True)
null=vt[1:]
rank=1; nullity=2
# move along a predeclared first null direction while preserving design exactly
n=null[0]/np.linalg.norm(null[0])
amp=0.9
cs=[part-amp*n,part+amp*n]
def E(c,x):
    return float(np.exp(c[0]*x+c[1]*x*x+c[2]*x*x*x))
vals=[{'coefficients':c.tolist(),'design':E(c,xd),'holdout':E(c,xh)} for c in cs]
dw=max(v['design'] for v in vals)-min(v['design'] for v in vals)
hw=max(v['holdout'] for v in vals)-min(v['holdout'] for v in vals)
out={
 'hypothesis':'H1 shared zero-free entire transverse form factor',
 'physical_motivation':'no additional finite propagator poles plus one common dressing of the GR transverse tensor structure',
 'parameterization':'E(x)=exp(c1 x+c2 x^2+c3 x^3)',
 'design_constraint':'E(0.25)=0.90',
 'design_rank':rank,'shape_nullity':nullity,
 'candidates':vals,'design_width':dw,'holdout_width':hw,
 'zero_free_by_construction':True,
 'common_entire_factor_reduces_but_does_not_close_shape': dw<1e-10 and hw>1e-4 and nullity>0,
 'novelty_credit':False,
 'conclusion':'A shared entire dressing removes cross-sector freedom and extra finite poles by construction, but a single common analytic function still contains shape freedom. This is a known nonlocal-gravity type comparator structure, not a unique new parent law.'
}
write_result('h1_common_entire',out)
