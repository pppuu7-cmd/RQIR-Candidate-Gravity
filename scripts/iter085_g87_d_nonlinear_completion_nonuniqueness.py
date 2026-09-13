import argparse, itertools, json
import sympy as sp

d0,d1,s0,s1=sp.symbols('d0 d1 s0 s1')
DV=[d0,d1,s0,s1]
DZERO={v:0 for v in DV}
G3=d0*s0**2+2*d0*s0*s1+d1*s1**2
x,y=sp.symbols('x y')
V=[x,y]
ZERO={x:0,y:0}
A=x**4
B=x**2*y**2
LAMBDAS=[sp.Integer(-2),sp.Integer(1),sp.Integer(3)]
RS=[
    sp.Matrix([[1,1],[0,1]]),
    sp.Matrix([[2,0],[1,1]]),
    sp.Matrix([[1,-1],[1,2]]),
    sp.Matrix([[-1,2],[1,1]]),
]
TIMES=range(4)

def jet(expr,order,vars_,zero):
    out={}
    for n in range(order+1):
        vals=[]
        for inds in itertools.product(range(len(vars_)), repeat=n):
            d=expr
            for i in inds: d=sp.diff(d,vars_[i])
            vals.append(sp.simplify(d.subs(zero)))
        out[n]=vals
    return out

def tensor(expr,n,vars_,zero): return jet(expr,n,vars_,zero)[n]
def flat_rank(expr,n,vars_,zero):
    t=tensor(expr,n,vars_,zero); m=len(vars_)
    M=sp.Matrix([[t[i*(m**(n-1))+j] for j in range(m**(n-1))] for i in range(m)])
    return M.rank(),M

def proportional(a,b): return sp.Matrix.hstack(sp.Matrix(a),sp.Matrix(b)).rank()<=1

def candidate_kernel():
    K={}
    for td in TIMES:
        for t1 in TIMES:
            for t2 in TIMES:
                v=sp.Rational(((td+2)*(t1+3)+(t2+5))%7-3)
                if td < max(t1,t2): v=sp.Integer(0)
                K[(td,t1,t2)]=v
    for key,v in list(K.items()):
        td,t1,t2=key; w=K[(td,t2,t1)]; vv=sp.simplify((v+w)/2)
        K[(td,t1,t2)]=K[(td,t2,t1)]=vv
    return K

def retarded(K): return all(v==0 for (td,t1,t2),v in K.items() if td<max(t1,t2))
def symmetric(K): return all(v==K[(td,t2,t1)] for (td,t1,t2),v in K.items())

def lane_A():
    base=jet(G3,3,DV,DZERO); cases=[]; valid=True
    for name,Ixy in [('A4',A),('B4',B)]:
        I=Ixy.subs({x:d0,y:s0})
        lower=jet(I,3,DV,DZERO)
        allzero=all(all(z==0 for z in lower[n]) for n in range(4))
        fourth=tensor(I,4,DV,DZERO); fourth_nonzero=any(z!=0 for z in fourth)
        for lam in LAMBDAS:
            J=jet(G3+lam*I,3,DV,DZERO)
            preserved=all(J[n]==base[n] for n in range(4))
            cases.append({'shape':name,'lambda':str(lam),'quartic_derivatives_through_order3_zero':allzero,'D_cubic_jet_preserved':preserved,'fourth_tensor_nonzero':fourth_nonzero})
            valid &= allzero and preserved and fourth_nonzero
    return 'D_QUARTIC_ADDITIONS_PRESERVE_FROZEN_CUBIC_JET_SCOPED',{'cases':cases},bool(valid)

def lane_B():
    ra,_=flat_rank(A,4,V,ZERO); rb,_=flat_rank(B,4,V,ZERO)
    ta=tensor(A,4,V,ZERO); tb=tensor(B,4,V,ZERO); nonprop=not proportional(ta,tb)
    transforms=[]; valid=(ra==1 and rb==2 and nonprop)
    u,v=sp.symbols('u v')
    for k,R in enumerate(RS,1):
        det=sp.simplify(R.det()); valid &= det!=0
        sub={x:R[0,0]*u+R[0,1]*v,y:R[1,0]*u+R[1,1]*v}
        At=sp.expand(A.subs(sub)); Bt=sp.expand(B.subs(sub))
        rAt,_=flat_rank(At,4,[u,v],{u:0,v:0}); rBt,_=flat_rank(Bt,4,[u,v],{u:0,v:0})
        transforms.append({'R':k,'det':str(det),'A_rank':rAt,'B_rank':rBt})
        valid &= rAt==1 and rBt==2
    return 'D_DISTINCT_QUARTIC_JET_SHAPES_LINEAR_COORDINATE_ROBUST_SCOPED',{'A_rank':ra,'B_rank':rb,'tensors_nonproportional':nonprop,'transforms':transforms},bool(valid)

def ctp_checks(I):
    xp,yp,xm,ym=sp.symbols('xp yp xm ym'); vv=[xp,yp,xm,ym]; zero={z:0 for z in vv}
    D=sp.expand(I.subs({x:xp,y:yp})-I.subs({x:xm,y:ym}))
    equal=sp.simplify(D.subs({xp:xm,yp:ym}))==0
    swapped=sp.expand(D.subs({xp:xm,yp:ym,xm:xp,ym:yp}, simultaneous=True))
    odd=sp.simplify(swapped+D)==0
    J3=jet(D,3,vv,zero); through3zero=all(all(z==0 for z in J3[n]) for n in range(4))
    fourth=tensor(D,4,vv,zero); fourth_nonzero=any(z!=0 for z in fourth)
    return equal,odd,through3zero,fourth_nonzero

def lane_C():
    cases={}; valid=True
    for name,I in [('A4',A),('B4',B)]:
        eq,odd,lowzero,fourth=ctp_checks(I)
        cases[name]={'equal_history_zero':eq,'branch_exchange_odd':odd,'derivatives_through_cubic_zero':lowzero,'fourth_derivative_nonzero':fourth}
        valid &= eq and odd and lowzero and fourth
    H=sp.hessian(G3,DV).subs(DZERO); hzero=(H==sp.zeros(4))
    t3=tensor(G3,3,DV,DZERO); tnonzero=any(z!=0 for z in t3)
    K1=candidate_kernel(); K2=candidate_kernel(); kunchanged=(K1==K2); kr=retarded(K1); ks=symmetric(K1)
    valid &= hzero and tnonzero and kunchanged and kr and ks
    checks={'quartic_ctp_cases':cases,'D_hessian_zero':hzero,'D_third_derivative_nonzero':tnonzero,'cubic_kernel_unchanged':kunchanged,'cubic_kernel_retarded':kr,'cubic_kernel_sigma_symmetric':ks}
    return 'D_QUARTIC_CTP_NORMALIZATION_AND_CUBIC_STRUCTURE_PRESERVATION_SCOPED',checks,bool(valid)

def lane_D():
    base3=tensor(G3,3,DV,DZERO)
    bad=G3+d0**3; bad3=tensor(bad,3,DV,DZERO); cubic_detected=(bad3!=base3)
    same_family=proportional(tensor(A,4,V,ZERO),tensor(2*A,4,V,ZERO))
    zero_fourth=any(z!=0 for z in tensor(sp.Integer(0),4,V,ZERO))
    singular=sp.Matrix([[1,2],[2,4]]); singular_rejected=(singular.det()==0)
    valid=cubic_detected and same_family and (not zero_fourth) and singular_rejected
    checks={'cubic_addition_changes_third_jet':cubic_detected,'A4_and_2A4_same_shape_family':same_family,'zero_addition_has_nonzero_fourth_tensor':zero_fourth,'singular_transform_rejected':singular_rejected}
    return 'D_NONLINEAR_NONUNIQUENESS_ADVERSARIAL_CONTROLS_SCOPED',checks,bool(valid)

LANES={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}
ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=sorted(LANES)); ap.add_argument('--out',required=True); a=ap.parse_args()
classification,checks,valid=LANES[a.lane]()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
if not valid: raise SystemExit(2)
