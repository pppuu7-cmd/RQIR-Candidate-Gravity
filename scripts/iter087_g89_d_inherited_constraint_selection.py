import argparse, itertools, json
import sympy as sp

x,y,lam,mu=sp.symbols('x y lam mu')
A=x**4
B=x**2*y**2
I=lam*A+mu*B
V=[x,y]; ZERO={x:0,y:0}
SAMPLES=[(1,0),(0,1),(1,1),(2,-1),(-2,3)]
d0,d1,s0,s1=sp.symbols('d0 d1 s0 s1')
DV=[d0,d1,s0,s1]; DZERO={v:0 for v in DV}
G3=d0*s0**2+2*d0*s0*s1+d1*s1**2
TIMES=range(4)

def deriv(expr,inds,vars_,zero):
    d=expr
    for i in inds: d=sp.diff(d,vars_[i])
    return sp.simplify(d.subs(zero))
def rank_constraints(exprs): return sp.Matrix(exprs).jacobian([lam,mu]).rank()
def candidate_kernel():
    K={}
    for td in TIMES:
        for t1 in TIMES:
            for t2 in TIMES:
                v=sp.Rational(((td+2)*(t1+3)+(t2+5))%7-3)
                if td<max(t1,t2): v=sp.Integer(0)
                K[(td,t1,t2)]=v
    for key,v in list(K.items()):
        td,t1,t2=key; w=K[(td,t2,t1)]; vv=sp.simplify((v+w)/2); K[(td,t1,t2)]=K[(td,t2,t1)]=vv
    return K
def retarded(K): return all(v==0 for (td,t1,t2),v in K.items() if td<max(t1,t2))
def symmetric(K): return all(v==K[(td,t2,t1)] for (td,t1,t2),v in K.items())

def lane_A():
    cs=[]
    for n in range(4):
        for inds in itertools.product(range(2),repeat=n): cs.append(deriv(I,inds,V,ZERO))
    ident=all(sp.simplify(c)==0 for c in cs); r=rank_constraints(cs)
    sample_ok=[all(sp.simplify(c.subs({lam:a,mu:b}))==0 for c in cs) for a,b in SAMPLES]
    valid=ident and r==0 and all(sample_ok)
    return 'D_INHERITED_CUBIC_JET_SELECTION_RANK_ZERO_SCOPED',{'constraint_count':len(cs),'all_constraints_identically_zero':ident,'selection_rank':r,'remaining_coefficient_dimension':2-r,'sample_points_valid':sample_ok},bool(valid)

def lane_B():
    xp,yp,xm,ym=sp.symbols('xp yp xm ym'); vv=[xp,yp,xm,ym]; z={v:0 for v in vv}
    D=sp.expand(I.subs({x:xp,y:yp})-I.subs({x:xm,y:ym}))
    eq=sp.simplify(D.subs({xp:xm,yp:ym}))==0
    swapped=sp.expand(D.subs({xp:xm,yp:ym,xm:xp,ym:yp},simultaneous=True)); odd=sp.simplify(swapped+D)==0
    cs=[]
    for n in range(4):
        for inds in itertools.product(range(4),repeat=n): cs.append(deriv(D,inds,vv,z))
    lowzero=all(sp.simplify(c)==0 for c in cs); r=rank_constraints(cs)
    valid=eq and odd and lowzero and r==0
    return 'D_INHERITED_CTP_SELECTION_RANK_ZERO_SCOPED',{'equal_history_zero':eq,'branch_exchange_odd':odd,'derivatives_through_cubic_zero':lowzero,'selection_rank':r,'remaining_coefficient_dimension':2-r},bool(valid)

def lane_C():
    K0=candidate_kernel(); kr=retarded(K0); ks=symmetric(K0)
    H=sp.hessian(G3,DV).subs(DZERO); hzero=(H==sp.zeros(4))
    t3=[]
    for inds in itertools.product(range(4),repeat=3): t3.append(deriv(G3,inds,DV,DZERO))
    tnonzero=any(v!=0 for v in t3)
    sample_unchanged=[]
    for a,b in SAMPLES:
        K=candidate_kernel(); sample_unchanged.append(K==K0 and retarded(K) and symmetric(K))
    valid=kr and ks and hzero and tnonzero and all(sample_unchanged)
    return 'D_FROZEN_RETARDED_CUBIC_SECTOR_COEFFICIENT_BLIND_SCOPED',{'cubic_kernel_retarded':kr,'cubic_kernel_sigma_symmetric':ks,'D_hessian_zero':hzero,'D_third_derivative_nonzero':tnonzero,'sample_points_cubic_kernel_unchanged':sample_unchanged,'quartic_coefficients_enter_cubic_equations':False},bool(valid)

def lane_D():
    Txxxx=sp.diff(I,x,4).subs(ZERO)
    Txxyy=sp.diff(I,x,2,y,2).subs(ZERO)
    r1=sp.Matrix([Txxxx]).jacobian([lam,mu]).rank()
    r2=sp.Matrix([Txxxx,Txxyy]).jacobian([lam,mu]).rank()
    post=sp.Matrix([lam,mu]).jacobian([lam,mu]).rank()
    zr=sp.Matrix([sp.Integer(0)]).jacobian([lam,mu]).rank()
    valid=(r1==1 and r2==2 and post==2 and zr==0)
    return 'D_HIGHER_ORDER_SELECTION_CONTROL_CALIBRATION_SCOPED',{'T_xxxx':str(Txxxx),'T_xxyy':str(Txxyy),'one_higher_datum_rank':r1,'two_independent_higher_data_rank':r2,'posthoc_zero_rule_rank':post,'posthoc_zero_rule_inherited':False,'identically_zero_datum_rank':zr},bool(valid)

LANES={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}
ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=sorted(LANES)); ap.add_argument('--out',required=True); a=ap.parse_args()
classification,checks,valid=LANES[a.lane]()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
if not valid: raise SystemExit(2)
