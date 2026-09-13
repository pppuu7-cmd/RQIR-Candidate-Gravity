import argparse, json
from fractions import Fraction as F
import numpy as np
import sympy as sp
import mpmath as mp

PANELS=[
    [F(1,3),F(2,3),F(5,4),F(7,3)],
    [F(1,5),F(3,5),F(4,3),F(9,4)],
    [F(2,7),F(5,6),F(7,5),F(11,3)],
]
RHOS=[F(0),F(1,10),F(-1,10),F(1,2),F(-1,2),F(-9,10),F(-99,100),F(-999,1000)]
APPROACH=[F(0),F(-1,2),F(-9,10),F(-99,100),F(-999,1000)]
GAINS=[F(1),F(1,10),F(1,100),F(1,1000),F(1,10000),F(1,100000),F(1,1000000)]
TOL=1e-12

ETA=[F(-1),F(1),F(1),F(1)]
PAIRS=[(i,j) for i in range(4) for j in range(i,4)]
KS=[(1,2,3,4),(2,-1,1,3),(3,1,-2,4)]
SEEDS=[21,23,29,31]


def exact_rank(rows): return sp.Matrix(rows).rank()
def science_rows(zs): return [[-z,z] for z in zs]
def refrow(rho,q): return [rho*q,q]
def npmat(rows): return np.array([[float(x) for x in r] for r in rows],dtype=float)
def metrics(rows):
    M=npmat(rows); s=np.linalg.svd(M,compute_uv=False)
    rank=int(np.sum(s>TOL)); return rank,float(s[-1]),float(s[0]),float(s[0]/s[-1]) if s[-1]>0 else float('inf')
def strictly_dec(xs): return all(xs[i+1]<xs[i] for i in range(len(xs)-1))
def strictly_inc(xs): return all(xs[i+1]>xs[i] for i in range(len(xs)-1))

def mpv(x):
    if isinstance(x,F): return mp.mpf(x.numerator)/x.denominator
    return mp.mpf(str(x))
def high_sv(rows):
    mp.mp.dps=80
    g=[[mp.mpf('0'),mp.mpf('0')],[mp.mpf('0'),mp.mpf('0')]]
    for r in rows:
        a,b=mpv(r[0]),mpv(r[1]); g[0][0]+=a*a; g[0][1]+=a*b; g[1][0]+=a*b; g[1][1]+=b*b
    vals,_=mp.eigsy(mp.matrix(g)); vals=[max(mp.mpf('0'),v) for v in vals]
    return mp.sqrt(vals[0]),mp.sqrt(vals[-1])

# exact projector helpers inherited from G82
def zmat(): return [[F(0) for _ in range(4)] for __ in range(4)]
def eye(): return [[F(int(i==j)) for j in range(4)] for i in range(4)]
def mm(A,B): return [[sum(A[i][r]*B[r][j] for r in range(4)) for j in range(4)] for i in range(4)]
def tr(A): return [[A[j][i] for j in range(4)] for i in range(4)]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(4)] for i in range(4)]
def scale(A,c): return [[c*A[i][j] for j in range(4)] for i in range(4)]
def sym_seed(n):
    A=zmat()
    for q,(i,j) in enumerate(PAIRS):
        v=F(((n+2)*(q+3)+q*q+1)%17-8); A[i][j]=A[j][i]=v
    return A
def geom(k0):
    k=[F(x) for x in k0]; kup=[ETA[i]*k[i] for i in range(4)]; k2=sum(k[i]*kup[i] for i in range(4))
    if k2==0: raise ValueError('null momentum')
    tm=eye(); tc=zmat(); tu=zmat()
    for i in range(4):
        for a in range(4): tm[i][a]-=k[i]*kup[a]/k2
        for j in range(4): tc[i][j]=F(int(i==j))*ETA[i]-k[i]*k[j]/k2; tu[i][j]=F(int(i==j))*ETA[i]-kup[i]*kup[j]/k2
    return k,kup,k2,tm,tc,tu
def ptrans(T,g): return mm(mm(g[3],T),tr(g[3]))
def theta_trace(T,g): return sum(g[5][i][j]*T[i][j] for i in range(4) for j in range(4))
def p0(T,g): return scale(g[4],F(1,3)*theta_trace(T,g))
def p2(T,g): return sub(ptrans(T,g),p0(T,g))
def projected(T,g):
    A=p2(T,g); B=p0(T,g); return [[A[i][j]+B[i][j] for j in range(4)] for i in range(4)]
def ward_zero(PT,g):
    kup=g[1]; left=[sum(kup[i]*PT[i][j] for i in range(4)) for j in range(4)]; right=[sum(PT[i][j]*kup[j] for j in range(4)) for i in range(4)]
    return all(x==0 for x in left+right)
def norm2(T): return sum(x*x for row in T for x in row)

def lane_A():
    cases=[]; valid=True
    for pi,zs in enumerate(PANELS):
        sci=science_rows(zs); base=exact_rank(sci); valid &= base==1
        rr={}
        for rho in RHOS:
            r=exact_rank(sci+[refrow(rho,F(1))]); rr[str(rho)]=r; valid &= r==2
        boundary=exact_rank(sci+[refrow(F(-1),F(1))]); valid &= boundary==1
        cases.append({'panel':pi,'science_rank':base,'nonboundary_ranks':rr,'boundary_rank':boundary})
    return 'C_EXACT_REFERENCE_LEAKAGE_BOUNDARY_SCOPED',{'cases':cases},bool(valid)

def lane_B():
    sci=science_rows(PANELS[0]); cases=[]; smins=[]; conds=[]; valid=True
    for rho in APPROACH:
        r,smin,smax,cond=metrics(sci+[refrow(rho,F(1))]); cases.append({'rho':str(rho),'rank':r,'smin':smin,'smax':smax,'condition':cond}); smins.append(smin); conds.append(cond); valid &= r==2
    boundary=exact_rank(sci+[refrow(F(-1),F(1))]); valid &= strictly_dec(smins) and strictly_inc(conds) and boundary==1
    return 'C_REFERENCE_CONDITIONING_DEGRADES_TO_SAME_SHAPE_LIMIT_SCOPED',{'cases':cases,'exact_boundary_rank':boundary},bool(valid)

def lane_C():
    sci=science_rows(PANELS[0]); rho=F(-1,10); cases=[]; smins=[]; conds=[]; valid=True
    for q in GAINS:
        rows=sci+[refrow(rho,q)]; er=exact_rank(rows); nr,smin,smax,cond=metrics(rows); cases.append({'q':str(q),'exact_rank':er,'numerical_rank':nr,'smin':smin,'condition':cond}); smins.append(smin); conds.append(cond); valid &= er==2 and nr==2
    valid &= strictly_dec(smins) and strictly_inc(conds) and exact_rank(sci+[[F(0),F(0)]])==1
    science_source=[]
    for k in KS:
        g=geom(k)
        for seed in SEEDS:
            PT=projected(sym_seed(seed),g); w=norm2(PT); wz=ward_zero(PT,g)
            rows=[[-z*w,z*w] for z in PANELS[0]]
            ranks={str(r):exact_rank(rows+[refrow(r,F(201559,448))]) for r in RHOS}
            science_source.append({'k':list(k),'seed':seed,'weight':str(w),'ward_zero':wz,'ranks':ranks})
            valid &= w!=0 and wz and all(x==2 for x in ranks.values())
    gr=geom((1,2,3,4)); qref=norm2(projected(sym_seed(37),gr)); refward=ward_zero(projected(sym_seed(37),gr),gr)
    valid &= qref==F(201559,448) and refward
    return 'C_REFERENCE_GAIN_AND_WARD_SOURCE_ROBUSTNESS_SCOPED',{'gain_cases':cases,'source_cases':science_source,'q_ref':str(qref),'reference_ward_zero':refward},bool(valid)

def lane_D():
    sci=science_rows(PANELS[0]); checks=[]; valid=True
    tests=[(F(0),F(1)),(F(-9,10),F(1)),(F(-999,1000),F(1)),(F(-1,10),F(1,1000000))]
    for rho,q in tests:
        rows=sci+[refrow(rho,q)]; _,smin,smax,_=metrics(rows); hsmin,hsmax=high_sv(rows)
        e1=float(abs(mp.mpf(str(smin))-hsmin)/max(abs(hsmin),mp.mpf('1e-300'))); e2=float(abs(mp.mpf(str(smax))-hsmax)/max(abs(hsmax),mp.mpf('1e-300')))
        checks.append({'rho':str(rho),'q':str(q),'smin_relerr':e1,'smax_relerr':e2}); valid &= e1<1e-8 and e2<1e-8
    q=F(1); same=exact_rank(sci+[[-q,q]]); zero=exact_rank(sci+[[F(0),F(0)]]); candidate=exact_rank(sci+[[q,F(0)]])
    science_copy=[list(r) for r in sci]; unchanged=(science_copy==sci)
    valid &= same==1 and zero==1 and candidate==2 and unchanged
    out={'precision_cases':checks,'same_shape_rank':same,'zero_rank':zero,'candidate_only_rank':candidate,'candidate_only_is_accepted_reference':False,'science_rows_unchanged':unchanged}
    return 'C_REFERENCE_PRECISION_AND_FALSE_REFERENCE_CONTROLS_SCOPED',out,bool(valid)

LANES={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}
ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=sorted(LANES)); ap.add_argument('--out',required=True); a=ap.parse_args()
classification,checks,valid=LANES[a.lane]()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True,allow_nan=False)
if not valid: raise SystemExit(2)
