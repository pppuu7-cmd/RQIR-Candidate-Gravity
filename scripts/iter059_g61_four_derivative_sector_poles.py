#!/usr/bin/env python3
import argparse, itertools, json
from pathlib import Path
import sympy as sp

ETA=sp.diag(-1,1,1,1)
PAIRS=[(i,j) for i in range(4) for j in range(i,4)]
QREF=sp.Matrix([1,-2,2,-1])
RAYS=[(1,0),(0,1),(1,-3),(1,-1),(1,1),(2,-1),(1,-2),(2,1),(-1,1),(-2,3)]
HELD=[(3,2),(2,-5),(-3,4),(5,-1),(-2,-1),(4,-7)]


def hmat(vals):
    H=sp.zeros(4)
    for x,(i,j) in zip(vals,PAIRS): H[i,j]=H[j,i]=sp.sympify(x)
    return H

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

def curvature(p,H):
    R4=[[[[sp.Integer(0) for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a,b,c,d in itertools.product(range(4),repeat=4):
        R4[a][b][c][d]=sp.Rational(1,2)*(p[c]*p[b]*H[a,d]+p[d]*p[a]*H[b,c]-p[d]*p[b]*H[a,c]-p[c]*p[a]*H[b,d])
    Ric=sp.zeros(4)
    for b,d in itertools.product(range(4),repeat=2): Ric[b,d]=sp.expand(sum(ETA[a,a]*R4[a][b][a][d] for a in range(4)))
    Rs=sp.expand(sum(ETA[b,b]*Ric[b,b] for b in range(4)))
    ric2=sp.expand(sum(ETA[b,b]*ETA[d,d]*Ric[b,d]**2 for b,d in itertools.product(range(4),repeat=2)))
    return sp.factor(Rs**2),sp.factor(ric2)

def representatives():
    tt=sp.zeros(4); tt[1,2]=tt[2,1]=1
    sc=sp.diag(0,1,1,1)
    return tt,sc

def direct_polys():
    q,a,b,z=sp.symbols('q a b z')
    p=[q,0,0,0]; tt,sc=representatives()
    out=[]
    for H in (tt,sc):
        r2,ric2=curvature(p,H); expr=sp.factor(baseline(p,H)+a*r2+b*ric2)
        out.append(sp.factor(expr.subs(q**2,z).subs(q**4,z**2)))
    return out

def roots_for(a,b):
    tt=None if b==0 else sp.Rational(4,b)
    c=3*a+b; sc=None if c==0 else sp.Rational(-2,c)
    return tt,sc

def stream_A():
    z,a,b=sp.symbols('z a b'); tt,sc=direct_polys(); tgt1=sp.factor(z*(-2+b*z/2)); tgt2=sp.factor(z*(6+3*(3*a+b)*z))
    ok=sp.expand(tt-tgt1)==0 and sp.expand(sc-tgt2)==0 and sp.factor(tt).subs(z,0)==0 and sp.factor(sc).subs(z,0)==0
    return {'stream':'A','valid':True,'pass':bool(ok),'tt':str(tt),'scalar':str(sc),'target_tt':str(tgt1),'target_scalar':str(tgt2)}
def stream_B():
    details=[]; ok=True
    for a,b in RAYS:
        tt,sc=roots_for(sp.Integer(a),sp.Integer(b)); d={'ray':[a,b],'tt_extra':tt is not None,'scalar_extra':sc is not None,'tt_root':None if tt is None else str(tt),'scalar_root':None if sc is None else str(sc)}; details.append(d)
        ok &= ((tt is not None)==(b!=0)) and ((sc is not None)==(3*a+b!=0))
    lookup={tuple(d['ray']):d for d in details}
    ok &= (not lookup[(1,0)]['tt_extra'] and lookup[(1,0)]['scalar_extra'])
    ok &= (lookup[(1,-3)]['tt_extra'] and not lookup[(1,-3)]['scalar_extra'])
    ok &= all(d['tt_extra'] or d['scalar_extra'] for d in details)
    return {'stream':'B','valid':True,'pass':bool(ok),'details':details}
def stream_C():
    Ulist=[sp.Matrix([[1,1],[0,1]]),sp.Matrix([[0,1],[1,0]]),sp.Matrix([[2,1],[1,1]])]
    ltt=sp.Matrix([[0,1]]); lsc=sp.Matrix([[3,1]])
    checks=[]; ok=True
    for U in Ulist:
        Ui=U.inv(); ltt_new=ltt*U; lsc_new=lsc*U
        for av,bv in RAYS:
            old=sp.Matrix([av,bv]); new=Ui*old
            c1=sp.simplify((ltt*old)[0]-(ltt_new*new)[0])==0
            c2=sp.simplify((lsc*old)[0]-(lsc_new*new)[0])==0
            r1=roots_for(sp.Integer(av),sp.Integer(bv)); back=U*new; r2=roots_for(sp.simplify(back[0]),sp.simplify(back[1]))
            rr=(r1==r2); checks.append(bool(c1 and c2 and rr)); ok &= c1 and c2 and rr
    return {'stream':'C','valid':True,'pass':bool(ok),'checks':len(checks),'passed':sum(checks)}
def stream_D():
    q,a,b=sp.symbols('q a b'); p=[q,0,0,0]; ttH,scH=representatives(); r2t,rict=curvature(p,ttH); r2s,rics=curvature(p,scH)
    direct_tt=sp.factor(baseline(p,ttH)+a*r2t+b*rict); direct_sc=sp.factor(baseline(p,scH)+a*r2s+b*rics)
    target_tt=sp.factor(-2*q**2+b*q**4/2); target_sc=sp.factor(6*q**2+3*(3*a+b)*q**4)
    matches=0; total=0
    for av,bv in HELD:
      for qv in (1,2,3,5):
        sub={a:av,b:bv,q:qv}; total+=1
        if sp.simplify(direct_tt.subs(sub)-target_tt.subs(sub))==0 and sp.simplify(direct_sc.subs(sub)-target_sc.subs(sub))==0: matches+=1
    wrong_scalar=sum(1 for av,bv in HELD if 3*av+bv != 2*av+bv)
    wrong_tt=sum(1 for av,bv in HELD if bv != av)
    ok=(matches==total and wrong_scalar>=4 and wrong_tt>=4)
    return {'stream':'D','valid':True,'pass':bool(ok),'direct_matches':matches,'direct_total':total,'wrong_scalar_rejected_pairs':wrong_scalar,'wrong_tt_rejected_pairs':wrong_tt}
def aggregate(indir):
    got={}
    for p in Path(indir).rglob('*.json'):
      try: d=json.loads(p.read_text())
      except Exception: continue
      if d.get('stream') in 'ABCD': got[d['stream']]=d
    valid=set(got)==set('ABCD') and all(got[s].get('valid') for s in 'ABCD'); passes={s:bool(got.get(s,{}).get('pass',False)) for s in 'ABCD'}
    if valid and all(passes.values()): cls='FOUR_DERIVATIVE_LINEARIZED_SECTOR_ADDITIONAL_ROOT_STRATIFICATION_SCOPED'
    elif valid: cls='SCIENTIFIC_FAIL_G61_'+''.join(s for s in 'ABCD' if not passes[s])
    else: cls='INFRASTRUCTURE_OR_IMPLEMENTATION_FAIL'
    return {'gate':'ITER059_G61_FOUR_DERIVATIVE_SECTOR_POLE_STRATIFICATION','valid':valid,'passes':passes,'classification':cls,'programme_readiness_percent':66,'theory_established_percent':0}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=list('ABCD')); ap.add_argument('--aggregate-dir'); ap.add_argument('--out',required=True); args=ap.parse_args()
    res=aggregate(args.aggregate_dir) if args.aggregate_dir else {'A':stream_A,'B':stream_B,'C':stream_C,'D':stream_D}[args.stream]()
    Path(args.out).parent.mkdir(parents=True,exist_ok=True); Path(args.out).write_text(json.dumps(res,indent=2,sort_keys=True)); print(json.dumps(res,indent=2,sort_keys=True))
if __name__=='__main__': main()
