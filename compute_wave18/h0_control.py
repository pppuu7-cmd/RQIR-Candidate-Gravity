import numpy as np
from common import write_result, X_DESIGN, X_HOLD

# Control: two independent physical transverse slopes after Wave-17 gates.
# O(x)=A f2(x)+B f0(x), f2=1+a x, f0=-1/2+b x.
A,B=-0.33089440785040997,-1.2145566246797788
J=np.array([[X_DESIGN*A,X_DESIGN*B]])
_,_,vt=np.linalg.svd(J,full_matrices=True)
rank=int(np.linalg.matrix_rank(J)); nullity=2-rank
n=vt[-1]; n=n/np.linalg.norm(n)
base=np.array([0.08,-0.04]); amp=0.35
pairs=[base-amp*n,base+amp*n]
def obs(p,x):
    a,b=p
    return (1+a*x)*A+(-0.5+b*x)*B
vals=[{'p':p.tolist(),'design':float(obs(p,X_DESIGN)),'holdout':float(obs(p,X_HOLD))} for p in pairs]
dw=max(v['design'] for v in vals)-min(v['design'] for v in vals)
hw=max(v['holdout'] for v in vals)-min(v['holdout'] for v in vals)
out={
 'hypothesis':'H0 no-extra-hypothesis control',
 'design_rank':rank,'design_nullity':nullity,
 'null_vector':n.tolist(),'candidates':vals,
 'design_width':dw,'holdout_width':hw,
 'undertermination_survives':dw<1e-10 and hw>1e-4,
 'novelty_credit':False,
 'conclusion':'Frozen RQIR + tensor Ward/gauge + GR IR gates alone leave a physical transverse design-null direction, providing the control against which extra hypotheses are judged.'
}
write_result('h0_control',out)
