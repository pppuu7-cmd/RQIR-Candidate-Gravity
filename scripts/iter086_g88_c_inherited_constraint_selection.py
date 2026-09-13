import argparse, itertools, json
import sympy as sp

x,y,lam,mu=sp.symbols('x y lam mu')
Q=x**2+2*y**2
A=x**3
B=x*y**2
F=sp.expand(Q+lam*A+mu*B)
V=[x,y]; ZERO={x:0,y:0}
SAMPLES=[(1,0),(0,1),(1,1),(2,-1),(-2,3)]
ETA=[sp.Rational(-1),sp.Rational(1),sp.Rational(1),sp.Rational(1)]
PAIRS=[(i,j) for i in range(4) for j in range(i,4)]
KS=[(1,2,3,4),(2,-1,1,3),(3,1,-2,4)]
SEEDS=[21,23,29,31]

def deriv(expr,inds,vars_=V,zero=ZERO):
    d=expr
    for i in inds: d=sp.diff(d,vars_[i])
    return sp.simplify(d.subs(zero))

def lower_constraints():
    out=[]
    for n in range(3):
        for inds in itertools.product(range(2),repeat=n): out.append(sp.simplify(deriv(F-Q,inds)))
    return out

def rank_constraints(exprs):
    M=sp.Matrix(exprs).jacobian([lam,mu])
    return M.rank(),M

def zmat(): return [[sp.Rational(0) for _ in range(4)] for __ in range(4)]
def eye(): return [[sp.Rational(int(i==j)) for j in range(4)] for i in range(4)]
def mm(A,B): return [[sum(A[i][r]*B[r][j] for r in range(4)) for j in range(4)] for i in range(4)]
def tr(A): return [[A[j][i] for j in range(4)] for i in range(4)]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(4)] for i in range(4)]
def scale(A,c): return [[c*A[i][j] for j in range(4)] for i in range(4)]
def sym_seed(n):
    T=zmat()
    for q,(i,j) in enumerate(PAIRS):
        v=sp.Rational(((n+2)*(q+3)+q*q+1)%17-8); T[i][j]=T[j][i]=v
    return T
def geom(k0):
    k=[sp.Rational(v) for v in k0]; kup=[ETA[i]*k[i] for i in range(4)]; k2=sum(k[i]*kup[i] for i in range(4))
    tm=eye(); tc=zmat(); tu=zmat()
    for i in range(4):
        for a in range(4): tm[i][a]-=k[i]*kup[a]/k2
        for j in range(4): tc[i][j]=sp.Rational(int(i==j))*ETA[i]-k[i]*k[j]/k2; tu[i][j]=sp.Rational(int(i==j))*ETA[i]-kup[i]*kup[j]/k2
    return k,kup,k2,tm,tc,tu
def ptrans(T,g): return mm(mm(g[3],T),tr(g[3]))
def theta_trace(T,g): return sum(g[5][i][j]*T[i][j] for i in range(4) for j in range(4))
def p0(T,g): return scale(g[4],sp.Rational(1,3)*theta_trace(T,g))
def projected(T,g):
    A2=sub(ptrans(T,g),p0(T,g)); B0=p0(T,g); return [[sp.simplify(A2[i][j]+B0[i][j]) for j in range(4)] for i in range(4)]
def ward_zero(PT,g):
    kup=g[1]; vals=[sum(kup[i]*PT[i][j] for i in range(4)) for j in range(4)]+[sum(PT[i][j]*kup[j] for j in range(4)) for i in range(4)]
    return all(sp.simplify(v)==0 for v in vals)

def lane_A():
    cs=lower_constraints(); r,_=rank_constraints(cs); ident=all(sp.simplify(c)==0 for c in cs)
    sample_ok=[]
    for a,b in SAMPLES: sample_ok.append(all(sp.simplify(c.subs({lam:a,mu:b}))==0 for c in cs))
    valid=ident and r==0 and all(sample_ok)
    return 'C_INHERITED_LOWER_JET_SELECTION_RANK_ZERO_SCOPED',{'constraint_count':len(cs),'all_constraints_identically_zero':ident,'selection_rank':r,'remaining_coefficient_dimension':2-r,'sample_points_valid':sample_ok},bool(valid)

def lane_B():
    xp,yp,xm,ym=sp.symbols('xp yp xm ym'); vv=[xp,yp,xm,ym]; z={v:0 for v in vv}
    I=lam*(x**3)+mu*(x*y**2)
    D=sp.expand(I.subs({x:xp,y:yp})-I.subs({x:xm,y:ym}))
    eq=sp.simplify(D.subs({xp:xm,yp:ym}))==0
    swapped=sp.expand(D.subs({xp:xm,yp:ym,xm:xp,ym:yp},simultaneous=True)); odd=sp.simplify(swapped+D)==0
    H=sp.hessian(D,vv).subs(z); hzero=(H==sp.zeros(4))
    cs=list(H); r,_=rank_constraints(cs); valid=eq and odd and hzero and r==0
    return 'C_INHERITED_CTP_SELECTION_RANK_ZERO_SCOPED',{'equal_history_zero':eq,'branch_exchange_odd':odd,'doubled_hessian_zero':hzero,'selection_rank':r,'remaining_coefficient_dimension':2-r},bool(valid)

def lane_C():
    H=sp.hessian(F,(x,y)).subs(ZERO); H0=sp.hessian(Q,(x,y)).subs(ZERO); hind=(H==H0 and all(sp.diff(H[i,j],p)==0 for i in range(2) for j in range(2) for p in [lam,mu]))
    cases=[]; valid=hind
    for k in KS:
        g=geom(k)
        for seed in SEEDS:
            PT=projected(sym_seed(seed),g); wz=ward_zero(PT,g)
            samples_identical=all(H.subs({lam:a,mu:b})==H0 for a,b in SAMPLES)
            cases.append({'k':list(k),'seed':seed,'ward_zero':wz,'quadratic_response_coefficient_blind':samples_identical})
            valid &= wz and samples_identical
    return 'C_FROZEN_QUADRATIC_WARD_SECTOR_COEFFICIENT_BLIND_SCOPED',{'hessian_coefficient_independent':hind,'source_cases':cases},bool(valid)

def lane_D():
    Txxx=sp.diff(lam*A+mu*B,x,3).subs(ZERO)
    Txyy=sp.diff(lam*A+mu*B,x,y,2).subs(ZERO)
    r1=sp.Matrix([Txxx]).jacobian([lam,mu]).rank()
    r2=sp.Matrix([Txxx,Txyy]).jacobian([lam,mu]).rank()
    post=sp.Matrix([lam,mu]).jacobian([lam,mu]).rank()
    zr=sp.Matrix([sp.Integer(0)]).jacobian([lam,mu]).rank()
    valid=(r1==1 and r2==2 and post==2 and zr==0)
    return 'C_HIGHER_ORDER_SELECTION_CONTROL_CALIBRATION_SCOPED',{'T_xxx':str(Txxx),'T_xyy':str(Txyy),'one_higher_datum_rank':r1,'two_independent_higher_data_rank':r2,'posthoc_zero_rule_rank':post,'posthoc_zero_rule_inherited':False,'identically_zero_datum_rank':zr},bool(valid)

LANES={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}
ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=sorted(LANES)); ap.add_argument('--out',required=True); a=ap.parse_args()
classification,checks,valid=LANES[a.lane]()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
if not valid: raise SystemExit(2)
