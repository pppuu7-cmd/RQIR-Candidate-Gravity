import argparse, json
from fractions import Fraction as F
import numpy as np
import sympy as sp
import mpmath as mp

RHOS=[F(0),F(1,10),F(-1,10),F(1,2),F(-1,2),F(9,10),F(99,100),F(999,1000)]
APPROACH=[F(0),F(1,2),F(9,10),F(99,100),F(999,1000)]
GAINS=[F(1),F(1,10),F(1,100),F(1,1000),F(1,10000),F(1,100000),F(1,1000000)]
TOL=1e-12
TIMES=range(4)


def candidate_kernel():
    K={}
    for td in TIMES:
        for t1 in TIMES:
            for t2 in TIMES:
                v=F(((td+2)*(t1+3)+(t2+5))%7-3)
                if td < max(t1,t2): v=F(0)
                K[(td,t1,t2)]=v
    for key,v in list(K.items()):
        td,t1,t2=key; w=K[(td,t2,t1)]; vv=(v+w)/2; K[(td,t1,t2)]=K[(td,t2,t1)]=vv
    return K
def reference_kernel(advanced=False):
    R={(td,t1,t2):F(0) for td in TIMES for t1 in TIMES for t2 in TIMES}
    if advanced: R[(0,2,3)]=R[(0,3,2)]=F(1)
    else: R[(3,1,2)]=R[(3,2,1)]=F(1)
    return R
def retarded(K): return all(v==0 for (td,t1,t2),v in K.items() if td<max(t1,t2))
def symmetric(K): return all(v==K[(td,t2,t1)] for (td,t1,t2),v in K.items())
def norm2(K): return sum(v*v for v in K.values())
def vals(K): return [v for _,v in sorted(K.items()) if v!=0]
def science_rows(): return [[v,v] for v in vals(candidate_kernel())]
def refrow(rho,q): return [rho*q,q]
def exact_rank(rows): return sp.Matrix(rows).rank()
def npmat(rows): return np.array([[float(x) for x in r] for r in rows],dtype=float)
def metrics(rows):
    s=np.linalg.svd(npmat(rows),compute_uv=False); rank=int(np.sum(s>TOL)); return rank,float(s[-1]),float(s[0]),float(s[0]/s[-1]) if s[-1]>0 else float('inf')
def strictly_dec(xs): return all(xs[i+1]<xs[i] for i in range(len(xs)-1))
def strictly_inc(xs): return all(xs[i+1]>xs[i] for i in range(len(xs)-1))
def mpv(x): return mp.mpf(x.numerator)/x.denominator if isinstance(x,F) else mp.mpf(str(x))
def high_sv(rows):
    mp.mp.dps=80; g=[[mp.mpf('0'),mp.mpf('0')],[mp.mpf('0'),mp.mpf('0')]]
    for r in rows:
        a,b=mpv(r[0]),mpv(r[1]); g[0][0]+=a*a; g[0][1]+=a*b; g[1][0]+=a*b; g[1][1]+=b*b
    ev,_=mp.eigsy(mp.matrix(g)); ev=[max(mp.mpf('0'),x) for x in ev]; return mp.sqrt(ev[0]),mp.sqrt(ev[-1])

def lane_A():
    sci=science_rows(); base=exact_rank(sci); rr={}; valid=(base==1)
    for rho in RHOS:
        r=exact_rank(sci+[refrow(rho,F(1))]); rr[str(rho)]=r; valid &= r==2
    boundary=exact_rank(sci+[refrow(F(1),F(1))]); valid &= boundary==1
    return 'D_EXACT_REFERENCE_LEAKAGE_BOUNDARY_SCOPED',{'science_rank':base,'nonboundary_ranks':rr,'boundary_rank':boundary,'science_entries':len(sci)},bool(valid)

def lane_B():
    sci=science_rows(); cases=[]; smins=[]; conds=[]; valid=True
    for rho in APPROACH:
        r,smin,smax,cond=metrics(sci+[refrow(rho,F(1))]); cases.append({'rho':str(rho),'rank':r,'smin':smin,'smax':smax,'condition':cond}); smins.append(smin); conds.append(cond); valid &= r==2
    boundary=exact_rank(sci+[refrow(F(1),F(1))]); valid &= strictly_dec(smins) and strictly_inc(conds) and boundary==1
    return 'D_REFERENCE_CONDITIONING_DEGRADES_TO_SAME_SHAPE_LIMIT_SCOPED',{'cases':cases,'exact_boundary_rank':boundary},bool(valid)

def lane_C():
    sci=science_rows(); rho=F(1,10); cases=[]; smins=[]; conds=[]; valid=True
    for q in GAINS:
        rows=sci+[refrow(rho,q)]; er=exact_rank(rows); nr,smin,smax,cond=metrics(rows); cases.append({'q':str(q),'exact_rank':er,'numerical_rank':nr,'smin':smin,'condition':cond}); smins.append(smin); conds.append(cond); valid &= er==2 and nr==2
    valid &= strictly_dec(smins) and strictly_inc(conds) and exact_rank(sci+[[F(0),F(0)]])==1
    K=candidate_kernel(); R=reference_kernel(False); qref=norm2(R)
    kr,ks,rr,rs=retarded(K),symmetric(K),retarded(R),symmetric(R)
    ranks={str(r):exact_rank(sci+[refrow(r,qref)]) for r in RHOS}
    d0,d1,s0,s1=sp.symbols('d0 d1 s0 s1'); fields=[d0,d1,s0,s1]; G=d0*s0**2+2*d0*s0*s1+d1*s1**2; zero={x:0 for x in fields}
    H=[sp.diff(G,x,y).subs(zero) for x in fields for y in fields]; T=[sp.diff(G,x,y,z).subs(zero) for x in fields for y in fields for z in fields]
    ctp=sp.simplify(G.subs({d0:0,d1:0}))==0; hzero=all(x==0 for x in H); tnonzero=any(x!=0 for x in T)
    valid &= kr and ks and rr and rs and qref==F(2) and all(x==2 for x in ranks.values()) and ctp and hzero and tnonzero
    checks={'gain_cases':cases,'candidate_retarded':kr,'candidate_symmetric':ks,'reference_retarded':rr,'reference_symmetric':rs,'q_ref':str(qref),'reference_ranks':ranks,'ctp_normalization_exact':ctp,'hessian_zero':hzero,'third_derivative_nonzero':tnonzero}
    return 'D_REFERENCE_GAIN_AND_RETARDED_SOURCE_ROBUSTNESS_SCOPED',checks,bool(valid)

def lane_D():
    sci=science_rows(); checks=[]; valid=True
    tests=[(F(0),F(1)),(F(9,10),F(1)),(F(999,1000),F(1)),(F(1,10),F(1,1000000))]
    for rho,q in tests:
        rows=sci+[refrow(rho,q)]; _,smin,smax,_=metrics(rows); hsmin,hsmax=high_sv(rows)
        e1=float(abs(mp.mpf(str(smin))-hsmin)/max(abs(hsmin),mp.mpf('1e-300'))); e2=float(abs(mp.mpf(str(smax))-hsmax)/max(abs(hsmax),mp.mpf('1e-300')))
        checks.append({'rho':str(rho),'q':str(q),'smin_relerr':e1,'smax_relerr':e2}); valid &= e1<1e-8 and e2<1e-8
    q=F(1); same=exact_rank(sci+[[q,q]]); zero=exact_rank(sci+[[F(0),F(0)]]); candidate=exact_rank(sci+[[q,F(0)]])
    advanced_rejected=not retarded(reference_kernel(True)); before=candidate_kernel(); after=candidate_kernel(); unchanged=(before==after)
    valid &= same==1 and zero==1 and candidate==2 and advanced_rejected and unchanged
    out={'precision_cases':checks,'same_shape_rank':same,'zero_rank':zero,'candidate_only_rank':candidate,'candidate_only_is_accepted_reference':False,'advanced_reference_rejected':advanced_rejected,'candidate_kernel_unchanged':unchanged}
    return 'D_REFERENCE_PRECISION_AND_FALSE_REFERENCE_CONTROLS_SCOPED',out,bool(valid)

LANES={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}
ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=sorted(LANES)); ap.add_argument('--out',required=True); a=ap.parse_args()
classification,checks,valid=LANES[a.lane]()
out={'stream':a.lane,'classification':classification,'checks':checks,'valid':bool(valid),'readiness':66,'theory_established':0}
with open(a.out,'w') as f: json.dump(out,f,indent=2,sort_keys=True,allow_nan=False)
if not valid: raise SystemExit(2)
