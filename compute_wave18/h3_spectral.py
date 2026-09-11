import numpy as np
from common import write_result, X_DESIGN, X_HOLD, TARGET

# H3: positive normalized Stieltjes/spectral family.
# E(x)=sum_i w_i/(1+x/m_i), w_i>=0, sum w_i=1.
# Normalization + one design datum are exact; remaining positive spectral-shape freedom is tested prospectively.
m=np.array([0.4,1.5,6.0,20.0])
v=1/(1+X_DESIGN/m)
A=np.vstack([np.ones(4),v])
b=np.array([1.0,TARGET])
rank=int(np.linalg.matrix_rank(A)); nullity=4-rank
# Positive base: reserve 0.1 on endpoints, solve middle pair exactly.
w=np.zeros(4); w[0]=0.1; w[3]=0.1
rhs=np.array([0.8,TARGET-w[0]*v[0]-w[3]*v[3]])
M=np.array([[1,1],[v[1],v[2]]])
w[1:3]=np.linalg.solve(M,rhs)
# Nullspace and positivity-preserving excursion.
_,_,vt=np.linalg.svd(A,full_matrices=True)
n=vt[2]; n=n/np.linalg.norm(n)
pos=[]; neg=[]
for wi,ni in zip(w,n):
    if ni>1e-14: neg.append(wi/ni)
    elif ni<-1e-14: pos.append(wi/(-ni))
tmax=min(pos) if pos else 1.0
tmin=-min(neg) if neg else -1.0
amp=0.45*min(tmax,-tmin)
ws=[w-amp*n,w+amp*n]
def E(weights,x): return float(np.sum(weights/(1+x/m)))
vals=[{'weights':q.tolist(),'min_weight':float(q.min()),'design':E(q,X_DESIGN),'holdout':E(q,X_HOLD)} for q in ws]
dw=max(z['design'] for z in vals)-min(z['design'] for z in vals)
hw=max(z['holdout'] for z in vals)-min(z['holdout'] for z in vals)
out={
 'hypothesis':'H3 positive normalized Stieltjes/spectral closure',
 'physical_motivation':'analyticity/positive spectral representation for a physical transverse dressing',
 'spectral_masses':m.tolist(),'constraint_rank':rank,'weight_nullity':nullity,
 'base_weights':w.tolist(),'candidates':vals,
 'design_width':dw,'holdout_width':hw,
 'all_weights_nonnegative':all(z['min_weight']>=-1e-12 for z in vals),
 'spectral_positivity_and_one_design_do_not_close_shape':nullity>0 and dw<1e-10 and hw>1e-5 and all(z['min_weight']>=-1e-12 for z in vals),
 'novelty_credit':False,
 'conclusion':'A positive normalized spectral/Stieltjes representation with an exact low-q design value remains non-unique: positive spectral-weight directions survive and change an untouched finite-q prediction. This reproduces the finite-constraint lesson in a transverse-form-factor setting.'
}
write_result('h3_spectral',out)
