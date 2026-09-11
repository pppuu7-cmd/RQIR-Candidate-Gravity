import numpy as np
from common import write_result, X_DESIGN, X_HOLD, TARGET

# Cross-class prospective comparison. Every class is calibrated only to the same design E(xd)=TARGET.
# No holdout value is used in fitting.

# H1 minimum-norm cubic-log entire representative.
row=np.array([X_DESIGN,X_DESIGN**2,X_DESIGN**3]); y=np.log(TARGET)
c=row*y/(row@row)
def E1(x): return float(np.exp(c[0]*x+c[1]*x*x+c[2]*x*x*x))

# H2 semigroup/exponential.
rate=-np.log(TARGET)/X_DESIGN
def E2(x): return float(np.exp(-rate*x))

# H3 positive Stieltjes base representative.
m=np.array([0.4,1.5,6.0,20.0]); v=1/(1+X_DESIGN/m)
w=np.zeros(4); w[0]=0.1; w[3]=0.1
rhs=np.array([0.8,TARGET-w[0]*v[0]-w[3]*v[3]])
w[1:3]=np.linalg.solve(np.array([[1,1],[v[1],v[2]]]),rhs)
def E3(x): return float(np.sum(w/(1+x/m)))

# H4 minimum-norm fixed-point trajectory satisfying IR and design.
E_star=0.60; theta=np.array([0.7,1.4,2.2])
A=np.vstack([np.ones(3),(1+X_DESIGN)**(-theta)])
b=np.array([1-E_star,TARGET-E_star]); crg=np.linalg.lstsq(A,b,rcond=None)[0]
def E4(x): return float(E_star+np.sum(crg*(1+x)**(-theta)))

models={'H1_common_entire':E1,'H2_semigroup':E2,'H3_stieltjes':E3,'H4_RG_fixed_point':E4}
vals={k:{'design':f(X_DESIGN),'holdout':f(X_HOLD)} for k,f in models.items()}
design_width=max(v['design'] for v in vals.values())-min(v['design'] for v in vals.values())
holdouts=[v['holdout'] for v in vals.values()]
holdout_width=max(holdouts)-min(holdouts)
out={
 'test':'equation-class identifiability after identical low-q design calibration',
 'design_x':X_DESIGN,'design_target':TARGET,'holdout_x':X_HOLD,
 'class_predictions':vals,
 'design_width':design_width,'holdout_width':holdout_width,
 'same_design_different_class_holdouts':design_width<1e-10 and holdout_width>1e-4,
 'equation_class_is_not_identified_by_low_q_fit':design_width<1e-10 and holdout_width>1e-4,
 'conclusion':'Mutually different extra-hypothesis classes can be calibrated to the same low-q datum yet predict different untouched finite-q behavior. A successful fit cannot select the parent law; prospective cross-class holdouts are mandatory.'
}
write_result('class_identifiability',out)
