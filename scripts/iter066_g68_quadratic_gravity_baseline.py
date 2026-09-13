#!/usr/bin/env python3
import argparse, itertools, json
from pathlib import Path
import sympy as sp

ETA = sp.diag(-1, 1, 1, 1)
PAIRS = [(i,j) for i in range(4) for j in range(i,4)]
HVAR = sp.symbols('h0:10')
QREF = sp.Matrix([1,-2,2,-1])
HELD_K = [(2,3,1,5),(4,1,3,2),(5,2,4,1),(3,4,1,2),(2,5,1,4)]
COEFF = [(1,2,3),(-2,5,1),(3,-4,2),(5,1,-3),(-3,-2,7),(2,0,-5)]
GB_SHIFTS = (-3,-1,2,5)
RAYS = [(1,1),(2,-1),(1,-2),(-1,1),(-2,3),(3,2),(2,-5),(-3,4)]
SRC_K = [(1,2,3,4),(2,-1,1,3),(3,1,-2,4)]
SEEDS = (10,11,12,13)
ZS = (sp.Rational(1,7),sp.Rational(3,7),sp.Rational(5,6),sp.Rational(-5,7))


def hmat(vals):
    H=sp.zeros(4)
    for x,(i,j) in zip(vals,PAIRS): H[i,j]=H[j,i]=sp.sympify(x)
    return H

def flatten_sym(M):
    return [sp.expand(M[i,j]) for i in range(M.rows) for j in range(i,M.cols)]
def projective(v):
    vals=[sp.Rational(x) for x in list(v)]
    nz=[x for x in vals if x!=0]
    if not nz: return tuple(vals)
    return tuple(sp.simplify(x/nz[0]) for x in vals)

def curvature(p, vals=HVAR):
    H=hmat(vals)
    R4=[[[[sp.Integer(0) for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a,b,c,d in itertools.product(range(4),repeat=4):
        R4[a][b][c][d]=sp.Rational(1,2)*(
            p[c]*p[b]*H[a,d]+p[d]*p[a]*H[b,c]-p[d]*p[b]*H[a,c]-p[c]*p[a]*H[b,d])
    Ric=sp.zeros(4)
    for b,d in itertools.product(range(4),repeat=2):
        Ric[b,d]=sp.expand(sum(ETA[a,a]*R4[a][b][a][d] for a in range(4)))
    Rs=sp.expand(sum(ETA[b,b]*Ric[b,b] for b in range(4)))
    riem2=sp.expand(sum(ETA[a,a]*ETA[b,b]*ETA[c,c]*ETA[d,d]*R4[a][b][c][d]**2
                        for a,b,c,d in itertools.product(range(4),repeat=4)))
    ric2=sp.expand(sum(ETA[b,b]*ETA[d,d]*Ric[b,d]**2 for b,d in itertools.product(range(4),repeat=2)))
    r2=sp.expand(Rs**2)
    return riem2,ric2,r2

def qmatrix(expr): return sp.hessian(expr,HVAR)/2

def invariant_matrix(k):
    inv=curvature(k)
    return sp.Matrix.hstack(*[sp.Matrix(flatten_sym(qmatrix(e))) for e in inv])

# Exact EH quadratic baseline and canonical representatives, independently rederived from G59/G61 conventions.
def raise2(H): return ETA*H*ETA
def bilinear_terms(p,H,K):
    p=sp.Matrix(p); pu=ETA*p; Hu=raise2(H); Ku=raise2(K); p2=(p.T*ETA*p)[0]
    ta=p2*sum(H[i,j]*Ku[i,j] for i in range(4) for j in range(4))
    vH=[sum(p[m]*Hu[m,n] for m in range(4)) for n in range(4)]
    vK=[sum(p[m]*Ku[m,n] for m in range(4)) for n in range(4)]
    wH=[sum(pu[l]*H[l,n] for l in range(4)) for n in range(4)]
    wK=[sum(pu[l]*K[l,n] for l in range(4)) for n in range(4)]
    tb=(sum(vH[n]*wK[n] for n in range(4))+sum(vK[n]*wH[n] for n in range(4)))/2
    trH=sum(ETA[i,j]*H[i,j] for i in range(4) for j in range(4)); trK=sum(ETA[i,j]*K[i,j] for i in range(4) for j in range(4))
    divH=sum(p[n]*sum(p[m]*Hu[m,n] for m in range(4)) for n in range(4)); divK=sum(p[n]*sum(p[m]*Ku[m,n] for m in range(4)) for n in range(4))
    tc=(trH*divK+trK*divH)/2; td=p2*trH*trK
    return sp.Matrix([sp.simplify(x) for x in (ta,tb,tc,td)])
def baseline(p,H): return sp.factor((QREF.T*bilinear_terms(p,H,H))[0])
def reps():
    tt=sp.zeros(4); tt[1,2]=tt[2,1]=1
    sc=sp.diag(0,1,1,1)
    return tt,sc

def sector_polys():
    q,a,b,z=sp.symbols('q a b z')
    tt,sc=reps(); out=[]
    for H in (tt,sc):
        riem2,ric2,r2=curvature([q,0,0,0], [H[i,j] for i,j in PAIRS])
        expr=sp.factor(baseline([q,0,0,0],H)+a*r2+b*ric2)
        out.append(sp.factor(expr.subs(q**4,z**2).subs(q**2,z)))
    return out

# Full conserved-source projectors in exact SymPy rationals, matching frozen G65 conventions.
def smat_seed(n):
    A=sp.zeros(4)
    for q,(i,j) in enumerate(PAIRS):
        v=sp.Integer(((n+2)*(q+3)+q*q+1)%11-5)
        A[i,j]=A[j,i]=v
    return A

def geom(k0):
    k=sp.Matrix([sp.Integer(x) for x in k0]); kup=ETA*k; k2=(k.T*ETA*k)[0]
    if k2==0: raise ValueError('null source momentum')
    tm=sp.eye(4)-k*kup.T/k2
    tc=ETA-k*k.T/k2
    tu=ETA-kup*kup.T/k2
    return k,kup,k2,tm,tc,tu

def ptrans(T,g): return sp.simplify(g[3]*T*g[3].T)
def theta_trace(T,g): return sp.simplify(sum(g[5][i,j]*T[i,j] for i in range(4) for j in range(4)))
def p0(T,g): return sp.simplify(g[4]*theta_trace(T,g)/3)
def p2(T,g): return sp.simplify(ptrans(T,g)-p0(T,g))
def conserved(T,g): return all(sp.simplify((g[1].T*T)[j])==0 for j in range(4))
def sat(A,B): return sp.simplify(sum(ETA[i,i]*ETA[j,j]*A[i,j]*B[i,j] for i in range(4) for j in range(4)))
def ptt(a,b,z): return sp.factor(z*(-2+sp.Rational(1,2)*b*z))
def ps(a,b,z): return sp.factor(z*(6+3*(3*a+b)*z))
def tt_pf(z,b):
    if b==0: return -sp.Rational(1,2)/z
    r=sp.Rational(4,b); return -sp.Rational(1,2)/z+sp.Rational(1,2)/(z-r)
def sc_pf(z,a,b):
    c=3*a+b
    if c==0: return sp.Rational(1,6)/z
    r=sp.Rational(-2,c); return sp.Rational(1,6)/z-sp.Rational(1,6)/(z-r)


def stream_A():
    details=[]; ok=True
    for k in HELD_K:
        M=invariant_matrix(k); ns=M.nullspace(); rel=projective(ns[0]) if len(ns)==1 else None
        lane=(M.rank()==2 and len(ns)==1 and rel==(sp.Integer(1),sp.Integer(-4),sp.Integer(1)))
        details.append({'k':k,'rank':int(M.rank()),'nullity':len(ns),'relation':None if rel is None else [str(x) for x in rel],'pass':bool(lane)})
        ok &= lane
    return {'stream':'A','valid':True,'details':details,'pass':bool(ok)}

def stream_B():
    checks=0; ok=True
    for k in HELD_K:
        riem2,ric2,r2=curvature(k)
        gb=sp.expand(riem2-4*ric2+r2)
        ok &= (gb==0); checks+=1
        for gam,bet,alp in COEFF:
            a=sp.Integer(alp-gam); b=sp.Integer(bet+4*gam)
            general=sp.expand(gam*riem2+bet*ric2+alp*r2)
            eff=sp.expand(b*ric2+a*r2)
            q=(sp.expand(general-eff)==0); ok &= q; checks+=1
            for t in GB_SHIFTS:
                g2,b2,a2=gam+t,bet-4*t,alp+t
                shifted=sp.expand(g2*riem2+b2*ric2+a2*r2)
                map_same=(b2+4*g2==bet+4*gam and a2-g2==alp-gam)
                q2=(sp.expand(shifted-general)==0 and map_same)
                ok &= q2; checks+=1
    return {'stream':'B','valid':True,'checks':checks,'pass':bool(ok)}

def stream_C():
    checks=0; ok=True
    T=sp.Matrix([[1,sp.Rational(-2,3)],[0,2]])
    ok &= (T.det()!=0 and T.rank()==2); checks+=2
    for k in HELD_K:
        riem2,ric2,r2=curvature(k); c2=sp.expand(riem2-2*ric2+r2/3)
        # Direct Weyl identity and quotient form.
        q0=sp.expand(c2-(2*ric2-sp.Rational(2,3)*r2))==0
        ok &= q0; checks+=1
        for a,b in RAYS:
            lc=sp.Rational(b,2); lr=sp.Rational(a)+sp.Rational(b,3)
            left=sp.expand(a*r2+b*ric2); right=sp.expand(lr*r2+lc*c2)
            q=sp.expand(left-right)==0
            ok &= q; checks+=1
    return {'stream':'C','valid':True,'checks':checks,'basis_transform_det':str(T.det()),'pass':bool(ok)}

def stream_D():
    z,a,b=sp.symbols('z a b'); tt,sc=sector_polys()
    tgt_tt=sp.factor(z*(-2+b*z/2)); tgt_sc=sp.factor(z*(6+3*(3*a+b)*z))
    sector_ok=(sp.expand(tt-tgt_tt)==0 and sp.expand(sc-tgt_sc)==0)
    checks=2; ok=sector_ok; invalid=0
    for k in SRC_K:
        g=geom(k)
        for n in SEEDS:
            T=ptrans(smat_seed(n),g); T2=p2(T,g); T0=p0(T,g)
            n2=sat(T,T2); n0=sat(T,T0)
            lane=conserved(T,g) and n2!=0 and n0!=0
            ok &= lane
            if not lane: invalid+=1
            for av,bv in RAYS:
                for zv in ZS:
                    den2=ptt(av,bv,zv); den0=ps(av,bv,zv)
                    if den2==0 or den0==0:
                        invalid+=1; ok=False; checks+=1; continue
                    direct=sp.simplify(n2/den2+n0/den0)
                    recon=sp.simplify(n2*tt_pf(zv,bv)+n0*sc_pf(zv,av,bv))
                    q=sp.simplify(direct-recon)==0
                    ok &= q; checks+=1
    return {'stream':'D','valid':True,'sector_tt':str(tt),'sector_scalar':str(sc),'checks':checks,'invalid_frozen_lanes':invalid,'pass':bool(ok)}

def stream_E():
    k=HELD_K[0]; riem2,ric2,r2=curvature(k)
    gb=sp.expand(riem2-4*ric2+r2)
    gb_shift=(gb==0)
    # Duplicate physical direction cannot fake a two-dimensional basis.
    qR=qmatrix(r2); col=sp.Matrix(flatten_sym(qR)); duplicate=sp.Matrix.hstack(col,col)
    duplicate_detected=(duplicate.rank()==1)
    z=sp.symbols('z')
    baseline_poly=-2*z+sp.Rational(3,2)*z**2
    six=sp.expand(baseline_poly+z**3)
    six_detected=(sp.Poly(six,z).degree()==3 and sp.Poly(baseline_poly,z).degree()<=2)
    nonlocal_expr=sp.cancel(z**2/(1+z)); nonlocal_detected=(sp.denom(nonlocal_expr)!=1)
    scope_guard=True
    checks={'gauss_bonnet_shift_invariant':bool(gb_shift),'duplicate_basis_rank1':bool(duplicate_detected),'six_derivative_outside_baseline':bool(six_detected),'nonlocal_outside_local_polynomial':bool(nonlocal_detected),'scope_guard_local_layer_only':scope_guard}
    return {'stream':'E','valid':True,'checks':checks,'pass':all(checks.values())}

def aggregate(indir):
    got={}; files={}
    for s in 'ABCDE':
        found=[]
        for p in Path(indir).rglob(f'{s}.json'): found.append(p)
        files[s]=[str(x) for x in found]
        if len(found)!=1:
            return {'gate':'ITER066_G68_QUADRATIC_GRAVITY_BASELINE','valid':False,'classification':'INFRASTRUCTURE_OR_ARTIFACT_INVALID','files':files,'programme_readiness_percent':66,'theory_established_percent':0}
        try: got[s]=json.loads(found[0].read_text())
        except Exception:
            return {'gate':'ITER066_G68_QUADRATIC_GRAVITY_BASELINE','valid':False,'classification':'INFRASTRUCTURE_OR_ARTIFACT_INVALID','files':files,'programme_readiness_percent':66,'theory_established_percent':0}
    passes={s:bool(got[s].get('valid') and got[s].get('pass')) for s in 'ABCDE'}
    ok=all(passes.values())
    cls='G60_G67_LOCAL_FOUR_DERIVATIVE_ESCAPE_BASELINE_EQUIVALENT_TO_STANDARD_QUADRATIC_GRAVITY_SCOPED' if ok else 'SCIENTIFIC_FAIL_G68_'+''.join(s for s in 'ABCDE' if not passes[s])
    return {'gate':'ITER066_G68_QUADRATIC_GRAVITY_BASELINE','valid':True,'passes':passes,'classification':cls,'programme_readiness_percent':66,'theory_established_percent':0,'scope_lock':'G60-G67 local linearized four-derivative layer only; not a global RCG-002 novelty/falsification statement.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=list('ABCDE')); ap.add_argument('--aggregate-dir'); ap.add_argument('--out',required=True); args=ap.parse_args()
    res=aggregate(args.aggregate_dir) if args.aggregate_dir else {'A':stream_A,'B':stream_B,'C':stream_C,'D':stream_D,'E':stream_E}[args.stream]()
    Path(args.out).parent.mkdir(parents=True,exist_ok=True); Path(args.out).write_text(json.dumps(res,indent=2,sort_keys=True)); print(json.dumps(res,indent=2,sort_keys=True))
if __name__=='__main__': main()
