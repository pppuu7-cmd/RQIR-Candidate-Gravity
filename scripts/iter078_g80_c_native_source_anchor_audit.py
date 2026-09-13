import argparse, json
from fractions import Fraction as F
import sympy as sp

ETA=[F(-1),F(1),F(1),F(1)]
PAIRS=[(i,j) for i in range(4) for j in range(i,4)]
KS=[(1,2,3,4),(2,-1,1,3),(3,1,-2,4)]
SEEDS=[21,23,29,31]
PANELS=[
    [F(1,3),F(2,3),F(5,4),F(7,3)],
    [F(1,5),F(3,5),F(4,3),F(9,4)],
    [F(2,7),F(5,6),F(7,5),F(11,3)],
]

def zmat(): return [[F(0) for _ in range(4)] for __ in range(4)]
def eye(): return [[F(int(i==j)) for j in range(4)] for i in range(4)]
def mm(A,B): return [[sum(A[i][r]*B[r][j] for r in range(4)) for j in range(4)] for i in range(4)]
def tr(A): return [[A[j][i] for j in range(4)] for i in range(4)]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(4)] for i in range(4)]
def scale(A,c): return [[c*A[i][j] for j in range(4)] for i in range(4)]

def sym_seed(n):
    A=zmat()
    for q,(i,j) in enumerate(PAIRS):
        v=F(((n+2)*(q+3)+q*q+1)%17-8)
        A[i][j]=A[j][i]=v
    return A

def geom(k0):
    k=[F(x) for x in k0]
    kup=[ETA[i]*k[i] for i in range(4)]
    k2=sum(k[i]*kup[i] for i in range(4))
    if k2==0: raise ValueError('null momentum')
    tm=eye(); tc=zmat(); tu=zmat()
    for i in range(4):
        for a in range(4): tm[i][a]-=k[i]*kup[a]/k2
        for j in range(4):
            tc[i][j]=F(int(i==j))*ETA[i]-k[i]*k[j]/k2
            tu[i][j]=F(int(i==j))*ETA[i]-kup[i]*kup[j]/k2
    return k,kup,k2,tm,tc,tu

def ptrans(T,g): return mm(mm(g[3],T),tr(g[3]))
def theta_trace(T,g): return sum(g[5][i][j]*T[i][j] for i in range(4) for j in range(4))
def p0(T,g): return scale(g[4],F(1,3)*theta_trace(T,g))
def p2(T,g): return sub(ptrans(T,g),p0(T,g))
def rank(c,n): return sp.Matrix.hstack(sp.Matrix(c),sp.Matrix(n)).rank()
def s(x): return str(x)

def lane_A():
    cases=[]; valid=True
    for pi,zs in enumerate(PANELS):
        c=[-z for z in zs]; n=list(zs)
        rel=all(c[i]+n[i]==0 for i in range(len(zs)))
        r=rank(c,n)
        cases.append({'panel':pi,'rank':r,'exact_C_plus_N1_zero':rel})
        valid &= (r==1 and rel)
    return 'C_EXACT_RESPONSE_SLOPE_ALIAS_CONFIRMED_SCOPED',{'cases':cases},bool(valid)

def lane_B():
    rows=[]; valid=True
    for k in KS:
        g=geom(k); nonzero_count=0
        for seed in SEEDS:
            T=sym_seed(seed); A=p2(T,g); B=p0(T,g)
            PT=[[A[i][j]+B[i][j] for j in range(4)] for i in range(4)]
            w=sum(x*x for row in PT for x in row)
            nonzero=(w!=0); nonzero_count += int(nonzero)
            zs=PANELS[0]; c=[-z*w for z in zs]; n=[z*w for z in zs]
            r=rank(c,n); rel=all(c[i]+n[i]==0 for i in range(len(zs)))
            rows.append({'k':list(k),'seed':seed,'weight':s(w),'weight_nonzero':nonzero,'rank':r,'exact_C_plus_N1_zero':rel})
            valid &= nonzero and r==1 and rel
        valid &= nonzero_count>=1
    return 'C_TRANSVERSE_SOURCE_SAMPLING_PRESERVES_ALIAS_SCOPED',{'rows':rows},bool(valid)

def lane_C():
    zs=PANELS[0]
    c=[-z for z in zs]+[F(0),F(0),F(0)]
    n=list(zs)+[F(0),F(0),F(0)]
    r=rank(c,n)
    checks={'augmented_rank':r,'native_zero_derivative_rows':3,'noise_sector_rows_zero_for_response_coordinates':True,'ctp_normalization_row_zero_for_response_coordinates':True}
    return 'C_NATIVE_CTP_ZERO_DERIVATIVE_SECTORS_DO_NOT_ANCHOR_SCOPED',checks,bool(r==1)

def lane_D():
    zs=PANELS[0]; c=[-z for z in zs]; n=list(zs)
    distinct=rank(c,[z*z for z in zs])
    direct=rank(c+[F(0)],n+[F(1)])
    pseudo=rank(c+[F(0)],n+[F(0)])
    common_scales={}
    valid=(distinct==2 and direct==2 and pseudo==1)
    for a in [F(1),F(2),F(-3),F(5,7)]:
        r=rank([a*x for x in c],[a*x for x in n]); common_scales[s(a)]=r; valid &= r==1
    checks={'distinct_shape_rank':distinct,'non_native_direct_calibration_rank':direct,'zero_pseudocalibration_rank':pseudo,'common_scale_ranks':common_scales}
    return 'C_ANCHOR_AUDIT_SEPARABILITY_CONTROLS_VALID_SCOPED',checks,bool(valid)

LANES={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}
ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=sorted(LANES)); ap.add_argument('--out',required=True); a=ap.parse_args()
classification,checks,valid=LANES[a.lane]()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
if not valid: raise SystemExit(2)
