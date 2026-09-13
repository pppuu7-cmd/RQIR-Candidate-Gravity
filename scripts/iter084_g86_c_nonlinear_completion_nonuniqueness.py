import argparse, itertools, json
import sympy as sp

x,y=sp.symbols('x y')
V=[x,y]
ZERO={x:0,y:0}
Q=x**2+2*y**2
A=x**3
B=x*y**2
LAMBDAS=[sp.Integer(-2),sp.Integer(1),sp.Integer(3)]
RS=[
    sp.Matrix([[1,1],[0,1]]),
    sp.Matrix([[2,0],[1,1]]),
    sp.Matrix([[1,-1],[1,2]]),
    sp.Matrix([[-1,2],[1,1]]),
]

def jet(expr,order,vars_=V,zero=None):
    if zero is None: zero={v:0 for v in vars_}
    out={}
    for n in range(order+1):
        vals=[]
        for inds in itertools.product(range(len(vars_)), repeat=n):
            d=expr
            for i in inds: d=sp.diff(d,vars_[i])
            vals.append(sp.simplify(d.subs(zero)))
        out[n]=vals
    return out

def tensor(expr,n,vars_=V,zero=None): return jet(expr,n,vars_,zero)[n]
def flat_rank(expr,n,vars_=V,zero=None):
    t=tensor(expr,n,vars_,zero); m=len(vars_)
    M=sp.Matrix([[t[i*(m**(n-1))+j] for j in range(m**(n-1))] for i in range(m)])
    return M.rank(),M

def proportional(a,b):
    va=sp.Matrix(a); vb=sp.Matrix(b)
    return sp.Matrix.hstack(va,vb).rank()<=1

def lane_A():
    base=jet(Q,3); cases=[]; valid=True
    H=sp.hessian(Q,(x,y)).subs(ZERO)
    valid &= (H==sp.diag(2,4))
    for name,I in [('A3',A),('B3',B)]:
        for lam in LAMBDAS:
            J=jet(Q+lam*I,3)
            low=(J[0]==base[0] and J[1]==base[1] and J[2]==base[2])
            third_changed=(J[3]!=base[3] and any(v!=0 for v in tensor(lam*I,3)))
            cases.append({'shape':name,'lambda':str(lam),'lower_jet_identical':low,'third_tensor_changed':third_changed})
            valid &= low and third_changed
    return 'C_CUBIC_ADDITIONS_PRESERVE_FROZEN_QUADRATIC_JET_SCOPED',{'hessian':[[str(v) for v in row] for row in H.tolist()],'cases':cases},bool(valid)

def lane_B():
    ra,_=flat_rank(A,3); rb,_=flat_rank(B,3)
    ta=tensor(A,3); tb=tensor(B,3)
    nonprop=not proportional(ta,tb)
    transforms=[]; valid=(ra==1 and rb==2 and nonprop)
    u,v=sp.symbols('u v')
    for k,R in enumerate(RS,1):
        det=sp.simplify(R.det()); valid &= det!=0
        sub={x:R[0,0]*u+R[0,1]*v,y:R[1,0]*u+R[1,1]*v}
        At=sp.expand(A.subs(sub)); Bt=sp.expand(B.subs(sub))
        rAt,_=flat_rank(At,3,[u,v],{u:0,v:0}); rBt,_=flat_rank(Bt,3,[u,v],{u:0,v:0})
        transforms.append({'R':k,'det':str(det),'A_rank':rAt,'B_rank':rBt})
        valid &= rAt==1 and rBt==2
    return 'C_DISTINCT_CUBIC_JET_SHAPES_LINEAR_COORDINATE_ROBUST_SCOPED',{'A_rank':ra,'B_rank':rb,'tensors_nonproportional':nonprop,'transforms':transforms},bool(valid)

def ctp_checks(I):
    xp,yp,xm,ym=sp.symbols('xp yp xm ym'); vv=[xp,yp,xm,ym]; zero={z:0 for z in vv}
    plus=I.subs({x:xp,y:yp}); minus=I.subs({x:xm,y:ym}); D=sp.expand(plus-minus)
    eq=sp.simplify(D.subs({xp:xm,yp:ym}))==0
    swapped=sp.expand(D.subs({xp:xm,yp:ym,xm:xp,ym:yp}, simultaneous=True))
    odd=sp.simplify(swapped + D)==0
    H=sp.hessian(D,vv).subs(zero); hzero=(H==sp.zeros(4))
    t3=tensor(D,3,vv,zero); nonzero=any(z!=0 for z in t3)
    return eq,odd,hzero,nonzero

def lane_C():
    cases={}; valid=True
    for name,I in [('A3',A),('B3',B)]:
        eq,odd,hzero,nonzero=ctp_checks(I)
        cases[name]={'equal_history_zero':eq,'branch_exchange_odd':odd,'flat_hessian_zero':hzero,'third_derivative_nonzero':nonzero}
        valid &= eq and odd and hzero and nonzero
    return 'C_CUBIC_CTP_NORMALIZATION_BRANCH_STRUCTURE_SCOPED',cases,bool(valid)

def lane_D():
    H0=sp.hessian(Q,(x,y)).subs(ZERO); Hbad=sp.hessian(Q+x**2,(x,y)).subs(ZERO)
    quadratic_detected=(Hbad!=H0)
    same_family=proportional(tensor(A,3),tensor(2*A,3))
    zero_nonlin=any(z!=0 for z in tensor(sp.Integer(0),3))
    singular=sp.Matrix([[1,2],[2,4]])
    singular_rejected=(singular.det()==0)
    valid=quadratic_detected and same_family and (not zero_nonlin) and singular_rejected
    checks={'quadratic_addition_changes_hessian':quadratic_detected,'A3_and_2A3_same_shape_family':same_family,'zero_addition_has_nonzero_third_tensor':zero_nonlin,'singular_transform_rejected':singular_rejected}
    return 'C_NONLINEAR_NONUNIQUENESS_ADVERSARIAL_CONTROLS_SCOPED',checks,bool(valid)

LANES={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}
ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=sorted(LANES)); ap.add_argument('--out',required=True); a=ap.parse_args()
classification,checks,valid=LANES[a.lane]()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
if not valid: raise SystemExit(2)
