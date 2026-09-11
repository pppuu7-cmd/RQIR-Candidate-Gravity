import numpy as np
from common import projectors, conserved_tensor, contract, write_result

# Shared physical transverse kernel with two unknown finite-q slopes.
# f2(x)=1+a x, f0(x)=-1/2+b x. Frozen RQIR+IR normalization do not set a,b.
k=np.array([0.3,0.5,-0.8,0.6])
P,theta,_=projectors(k)
rng=np.random.default_rng(1706)
T1=conserved_tensor(rng,theta); U1=conserved_tensor(rng,theta)
T2=conserved_tensor(rng,theta); U2=conserved_tensor(rng,theta)
A1=contract(T1,P['P2'],U1); B1=contract(T1,P['P0s'],U1)
A2=contract(T2,P['P2'],U2); B2=contract(T2,P['P0s'],U2)

x_design=0.18; x_hold=0.62
# Design gradient wrt [a,b]
g=np.array([x_design*A1,x_design*B1],float)
J=g.reshape(1,2)
rank=int(np.linalg.matrix_rank(J,tol=1e-12)); nullity=2-rank
_,_,Vt=np.linalg.svd(J)
null=Vt[-1]; null=null/np.linalg.norm(null)
h=np.array([x_hold*A2,x_hold*B2],float)
hold_sensitivity=float(abs(h@null))

# Construct two candidates exactly identical on design observable by moving along null direction.
base=np.array([0.08,-0.04])
amp=0.35
cands=[base-amp*null,base+amp*null]
def obs(par,x,A,B):
    a,b=par
    return (1+a*x)*A + (-0.5+b*x)*B
vals=[]
for par in cands:
    vals.append({'parameters':par.tolist(),'design':float(obs(par,x_design,A1,B1)),'holdout':float(obs(par,x_hold,A2,B2))})
design_width=max(v['design'] for v in vals)-min(v['design'] for v in vals)
hold_width=max(v['holdout'] for v in vals)-min(v['holdout'] for v in vals)

out={
 'test':'prospective tensor finite-q holdout after conserved-source and IR gates',
 'design_contractions':{'spin2':A1,'spin0':B1,'x':x_design},
 'holdout_contractions':{'spin2':A2,'spin0':B2,'x':x_hold},
 'design_rank':rank,
 'design_nullity':nullity,
 'design_null_vector_ab':null.tolist(),
 'holdout_gradient_sensitivity_to_design_null':hold_sensitivity,
 'candidate_pair':vals,
 'design_width':design_width,
 'holdout_width':hold_width,
 'same_design_different_tensor_holdout_exists': design_width<1e-10 and hold_width>1e-4 and hold_sensitivity>1e-4,
 'conclusion':'Even after the tensor Ward reduction and exact GR IR normalization, a finite-q calibration can leave a transverse shape null direction that an untouched source geometry/momentum holdout resolves. The residual freedom is physically observable, not gauge.'
}
write_result('tensor_holdout',out)
