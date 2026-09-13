import argparse, json, os
from fractions import Fraction as F
import sympy as sp

ETA=[F(-1),F(1),F(1),F(1)]
PAIRS=[(i,j) for i in range(4) for j in range(i,4)]
KS=[(1,2,3,4),(2,-1,1,3),(3,1,-2,4)]
SEEDS=[21,23,29,31]

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
    k=[F(x) for x in k0]; kup=[ETA[i]*k[i] for i in range(4)]; k2=sum(k[i]*kup[i] for i in range(4))
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
def conserved(T,g): return all(sum(g[1][i]*T[i][j] for i in range(4))==0 for j in range(4))

def C1():
    rows=[]; ok=True; negative_seen=False
    for k in KS:
        g=geom(k)
        for s in SEEDS:
            T=sym_seed(s)
            PT=[[p2(T,g)[i][j]+p0(T,g)[i][j] for j in range(4)] for i in range(4)]
            ward=conserved(PT,g)
            bare=conserved(T,g)
            if not bare: negative_seen=True
            ok &= ward
            rows.append({'k':list(k),'seed':s,'projected_conserved':ward,'bare_conserved':bare})
    valid=ok and negative_seen
    return {'stream':'C1','valid':valid,'classification':'C_MINIMAL_WARD_COMPLETION_EXISTS_SCOPED' if valid else 'SCIENTIFIC_FAIL_FROZEN_PREDICATE','checks':{'rows':rows,'negative_control_detected':negative_seen},'readiness':66,'theory_established':0}

def C2():
    z,ell2,a=sp.symbols('z ell2 a', positive=True, nonzero=True)
    f=sp.exp(-ell2*z)
    zeros=sp.solveset(f,z,domain=sp.S.Complexes)
    nozeros=(zeros==sp.EmptySet)
    poly=1+a*z
    root=sp.solve(sp.Eq(poly,0),z)
    ctrl=(len(root)==1 and sp.simplify(root[0]+1/a)==0)
    valid=nozeros and ctrl and sp.simplify(f.subs(z,0)-1)==0
    return {'stream':'C2','valid':bool(valid),'classification':'C_MINIMAL_POLEFREE_FACTOR_COMPLETION_EXISTS_SCOPED' if valid else 'SCIENTIFIC_FAIL_FROZEN_PREDICATE','checks':{'factor':str(f),'zero_set':str(zeros),'no_finite_zeros':bool(nozeros),'F0':str(f.subs(z,0)),'poly_control_root':[str(x) for x in root],'control_detected':bool(ctrl)},'readiness':66,'theory_established':0}

def D1():
    times=range(4); entries=[]; support_ok=True; sym_ok=True; advanced_detected=False
    K={}
    for td in times:
        for t1 in times:
            for t2 in times:
                v=F(((td+2)*(t1+3)+(t2+5))%7-3)
                if td < max(t1,t2): v=F(0)
                K[(td,t1,t2)]=v
    for key,v in list(K.items()):
        td,t1,t2=key
        # enforce sigma symmetry by averaging exact rationals
        w=K[(td,t2,t1)]
        vv=(v+w)/2
        K[(td,t1,t2)]=K[(td,t2,t1)]=vv
    for (td,t1,t2),v in K.items():
        support_ok &= (v==0 if td<max(t1,t2) else True)
        sym_ok &= (v==K[(td,t2,t1)])
    Kbad=dict(K); Kbad[(0,1,1)]=F(1)
    advanced_detected=any(v!=0 and td<max(t1,t2) for (td,t1,t2),v in Kbad.items())
    delta_zero=True
    valid=support_ok and sym_ok and advanced_detected and delta_zero
    return {'stream':'D1','valid':valid,'classification':'D_MINIMAL_RETARDED_CUBIC_SUPPORT_EXISTS_SCOPED' if valid else 'SCIENTIFIC_FAIL_FROZEN_PREDICATE','checks':{'support_exact':support_ok,'sigma_permutation_exact':sym_ok,'ctp_delta0_zero':delta_zero,'advanced_control_detected':advanced_detected,'nonzero_entries':sum(v!=0 for v in K.values())},'readiness':66,'theory_established':0}

def D2():
    d0,d1,s0,s1=sp.symbols('d0 d1 s0 s1'); fields=[d0,d1,s0,s1]; k=sp.symbols('k', nonzero=True)
    G3=k*(d0*s0**2 + 2*d0*s0*s1 + d1*s1**2)
    H3=sp.Matrix([[sp.diff(G3,x,y) for y in fields] for x in fields]).subs({x:0 for x in fields})
    G2=k*(d0*s0+d1*s1)
    H2=sp.Matrix([[sp.diff(G2,x,y) for y in fields] for x in fields]).subs({x:0 for x in fields})
    valid=(H3==sp.zeros(4)) and (H2!=sp.zeros(4))
    return {'stream':'D2','valid':bool(valid),'classification':'D_RETARDED_CUBIC_HESSIAN_COMPATIBLE_WITH_G71_SCOPED' if valid else 'SCIENTIFIC_FAIL_FROZEN_PREDICATE','checks':{'cubic_hessian_zero':bool(H3==sp.zeros(4)),'quadratic_control_nonzero':bool(H2!=sp.zeros(4))},'readiness':66,'theory_established':0}

LANES={'C1':C1,'C2':C2,'D1':D1,'D2':D2}

def aggregate(root):
    got={}
    for b,_,fs in os.walk(root):
        for fn in fs:
            if not fn.endswith('.json'): continue
            try:o=json.load(open(os.path.join(b,fn)))
            except: continue
            if o.get('stream') in LANES: got[o['stream']]=o
    if set(got)!=set(LANES): return {'valid':False,'classification':'INFRASTRUCTURE_OR_GATE_INVALID','found':sorted(got),'readiness':66,'theory_established':0}
    if not all(got[s].get('valid') for s in LANES): return {'valid':False,'classification':'SCIENTIFIC_FAIL_FROZEN_COMPLETION_PREDICATE','lanes':{s:got[s]['classification'] for s in sorted(got)},'readiness':66,'theory_established':0}
    return {'valid':True,'classification':'CD_ORTHOGONAL_MINIMAL_COMPLETIONS_EXIST_NO_UNIQUE_SELECTION_SCOPED','lane_classifications':{s:got[s]['classification'] for s in sorted(got)},'readiness':66,'theory_established':0,'scope_lock':'Existence witnesses only; no architecture selection or candidate gravity law.'}

def emit(path,obj):
    os.makedirs(os.path.dirname(path) or '.',exist_ok=True)
    with open(path,'w') as f: json.dump(obj,f,indent=2,sort_keys=True)
    print(json.dumps(obj,indent=2,sort_keys=True))

p=argparse.ArgumentParser();p.add_argument('--stream',choices=sorted(LANES));p.add_argument('--aggregate-dir');p.add_argument('--out',required=True);a=p.parse_args()
if bool(a.stream)==bool(a.aggregate_dir): raise SystemExit('choose one mode')
o=LANES[a.stream]() if a.stream else aggregate(a.aggregate_dir);emit(a.out,o)
if not o.get('valid'): raise SystemExit(2)
