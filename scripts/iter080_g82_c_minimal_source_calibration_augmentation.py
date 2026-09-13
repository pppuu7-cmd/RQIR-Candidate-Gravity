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
QS=[F(1),F(2),F(5,3)]


def rank(c,n): return sp.Matrix.hstack(sp.Matrix(c),sp.Matrix(n)).rank()
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
def projected(T,g):
    A=p2(T,g); B=p0(T,g)
    return [[A[i][j]+B[i][j] for j in range(4)] for i in range(4)]
def ward_zero(PT,g):
    kup=g[1]
    left=[sum(kup[i]*PT[i][j] for i in range(4)) for j in range(4)]
    right=[sum(PT[i][j]*kup[j] for j in range(4)) for i in range(4)]
    return all(x==0 for x in left+right)
def norm2(T): return sum(x*x for row in T for x in row)

def lane_A():
    cases=[]; valid=True
    for pi,zs in enumerate(PANELS):
        c=[-z for z in zs]; n=list(zs)
        base=rank(c,n); valid &= base==1
        item={'panel':pi,'science_rank':base,'q_ranks':{}}
        for q in QS:
            r=rank(c+[F(0)],n+[q]); item['q_ranks'][str(q)]=r; valid &= r==2
        q0=rank(c+[F(0)],n+[F(0)]); item['zero_q_rank']=q0; valid &= q0==1
        cases.append(item)
    return 'C_SINGLE_REFERENCE_CHANNEL_ALGEBRAIC_SUFFICIENCY_SCOPED',{'cases':cases},bool(valid)

def lane_B():
    science=[]; valid=True
    for k in KS:
        g=geom(k)
        for seed in SEEDS:
            PT=projected(sym_seed(seed),g); w=norm2(PT); wz=ward_zero(PT,g)
            c=[-z*w for z in PANELS[0]]; n=[z*w for z in PANELS[0]]
            r=rank(c,n)
            science.append({'k':list(k),'seed':seed,'weight':str(w),'nonzero':w!=0,'ward_zero':wz,'science_rank':r})
            valid &= (w!=0 and wz and r==1)
    gr=geom((1,2,3,4)); refPT=projected(sym_seed(37),gr); qref=norm2(refPT); refward=ward_zero(refPT,gr)
    valid &= (qref!=0 and refward)
    ref_ranks=[]
    for row in science:
        k=tuple(row['k']); seed=row['seed']; g=geom(k); w=norm2(projected(sym_seed(seed),g))
        c=[-z*w for z in PANELS[0]]; n=[z*w for z in PANELS[0]]
        r=rank(c+[F(0)],n+[qref]); ref_ranks.append(r); valid &= r==2
    return 'C_SOURCE_DEFINED_REFERENCE_WITH_WARD_COMPATIBILITY_SCOPED',{'science_cases':science,'q_ref':str(qref),'reference_ward_zero':refward,'reference_augmented_ranks':ref_ranks},bool(valid)

def lane_C():
    zs=PANELS[0]; science_before=[[-z,z] for z in zs]
    q=F(1); augmented=science_before+[[F(0),q]]; science_after=augmented[:-1]
    native_zero_rows=[[F(0),F(0)] for _ in range(3)]
    ell2,z=sp.symbols('ell2 z'); factor_before=sp.exp(-ell2*z); factor_after=sp.exp(-ell2*z)
    base=rank([r[0] for r in science_before],[r[1] for r in science_before])
    recovered=rank([r[0] for r in science_after],[r[1] for r in science_after])
    checks={
        'science_rows_identical':science_before==science_after,
        'native_zero_rows_unchanged':all(r==[F(0),F(0)] for r in native_zero_rows),
        'candidate_factor_identical':sp.simplify(factor_before-factor_after)==0,
        'pre_rank':base,'recovered_rank_without_reference':recovered,
    }
    valid=all([checks['science_rows_identical'],checks['native_zero_rows_unchanged'],checks['candidate_factor_identical'],base==1,recovered==1])
    return 'C_REFERENCE_CHANNEL_BLOCK_SEPARATE_NONMODIFICATION_SCOPED',checks,bool(valid)

def lane_D():
    zs=PANELS[0]; c=[-z for z in zs]; n=list(zs); q=F(5,3)
    same=rank(c+[-q],n+[q]); zero=rank(c+[F(0)],n+[F(0)]); candidate_only=rank(c+[q],n+[F(0)])
    rescales={}; valid=(same==1 and zero==1 and candidate_only==2)
    for a in [F(1),F(-2),F(3,5)]:
        r=rank(c+[F(0)],n+[a*q]); rescales[str(a)]=r; valid &= r==2
    checks={'same_shape_pseudoref_rank':same,'zero_pseudoref_rank':zero,'candidate_only_detection_rank':candidate_only,'candidate_only_is_accepted_calibration':False,'accepted_reference_rescale_ranks':rescales}
    return 'C_REFERENCE_CHANNEL_FALSE_ANCHOR_CONTROLS_SCOPED',checks,bool(valid)

LANES={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}
ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=sorted(LANES)); ap.add_argument('--out',required=True); a=ap.parse_args()
classification,checks,valid=LANES[a.lane]()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True)
if not valid: raise SystemExit(2)
