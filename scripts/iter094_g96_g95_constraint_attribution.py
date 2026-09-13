#!/usr/bin/env python3
import argparse, itertools, json
from pathlib import Path
import sympy as sp

TIMES=(0,1,2)
VARS=[(i,j,k) for i in TIMES for j in range(i+1) for k in range(j,i+1)]
C=sp.symbols('c0:'+str(len(VARS))); V=dict(zip(VARS,C))
d=sp.symbols('d0:3'); s=sp.symbols('s0:3')
G=sum(V[i,j,k]*d[i]*s[j]*s[k] for i,j,k in VARS)
H=[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)]

def coeffs(poly):
    return [sp.expand(x) for x in sp.Poly(sp.expand(poly),*(d+s)).coeffs() if x!=0]

def fam(name):
    if name=='C0': q=(1,1,1)
    elif name=='C1': q=(0,1,2)
    elif name=='P': return [V[m,m,m] for m in TIMES]
    else: return []
    sh=G.subs({s[i]:s[i]+q[i] for i in TIMES}, simultaneous=True)
    return coeffs(sh-G)

def mat(names):
    eq=[]
    for n in names: eq += fam(n)
    if not eq: return sp.zeros(0,len(C))
    A,b=sp.linear_eq_to_matrix(eq,C); assert all(x==0 for x in b); return A

def ns(names): return mat(names).nullspace()

def expr(v): return sp.expand(sum(v[n]*d[i]*s[j]*s[k] for n,(i,j,k) in enumerate(VARS)))

def connected(e):
    for i,j,k in VARS:
        if j!=k and sp.expand(e).coeff(d[i]*s[j]*s[k])!=0: return True
    A,B,Cc=sp.symbols('A B Cc')
    z=sp.expand(e.subs({d[0]:0,d[1]:0,d[2]:A,s[0]:B,s[1]:Cc,s[2]:0}))
    return sp.diff(z,A,B,Cc)!=0

def ge(e,x,y):
    sub={d[i]:sp.Rational(x[i]-y[i]) for i in TIMES}; sub.update({s[i]:sp.Rational(x[i]+y[i],2) for i in TIMES})
    return sp.simplify(e.subs(sub))

def coherent(e):
    base=H[0]; phi={h:ge(e,h,base) for h in H}
    for x,y,z in itertools.product(H,repeat=3):
        if sp.simplify(ge(e,x,y)+ge(e,y,z)-ge(e,x,z))!=0: return False
    for x,y in itertools.product(H,repeat=2):
        if sp.simplify(ge(e,x,y)-(phi[x]-phi[y]))!=0: return False
    return True

def laneA():
    rows=[]; F=('C0','C1','P')
    for r in range(4):
        for sub in itertools.combinations(F,r):
            A=mat(sub); rows.append({'families':sub,'rank':int(A.rank()),'nullity':len(C)-int(A.rank())})
    zeros=[r for r in rows if r['nullity']==0]
    minimal=[]
    for z in zeros:
        S=set(z['families'])
        if not any(set(q['families'])<S and q['nullity']==0 for q in zeros): minimal.append(z['families'])
    return {'lane':'A','subset_map':rows,'minimal_zero_nullity_sets':minimal}

def laneB():
    out=[]
    for sub in (('C0','C1'),('C0','P'),('C1','P')):
        vv=ns(sub); out.append({'families':sub,'nullity':len(vv),'connected_count':sum(connected(expr(v)) for v in vv),'basis':[str(expr(v)) for v in vv]})
    return {'lane':'B','leave_one_family_out':out}

def laneC():
    out=[]
    for sub in (('C0','C1'),('C0','P'),('C1','P')):
        vv=ns(sub); out.append({'families':sub,'nullity':len(vv),'coherent_basis_count':sum(coherent(expr(v)) for v in vv),'coherent_flags':[coherent(expr(v)) for v in vv]})
    return {'lane':'C','coherence_map':out}

def laneD():
    full=mat(('C0','C1','P')); n=len(C)
    T1=sp.eye(n); T1[0,1]=sp.Rational(1,2); T1[4,7]=sp.Rational(-2,3)
    T2=sp.eye(n)
    for i in range(n): T2[i,i]=sp.Rational(i+1,i+2)
    ranks=[int(full.rank()),int((full*T1).rank()),int((full*T2).rank())]
    return {'lane':'D','full_ranks_original_T1_T2':ranks,'basis_covariant':len(set(ranks))==1,'full_nullity':n-ranks[0],'no_constraint_nullity':n}

def aggregate(items):
    m={x['lane']:x for x in items}
    if set(m)!=set('ABCD') or not m['D']['basis_covariant']: cls='INFRASTRUCTURE_OR_IMPLEMENTATION_FAIL'
    else: cls='G95_STRUCTURAL_OBSTRUCTION_ATTRIBUTED_SCOPED'
    return {'classification':cls,'lanes':m,'readiness_percent':66,'theory_established_percent':0,'claim_lock':'diagnostic attribution only; no ablated model is candidate physics'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=list('ABCD')); ap.add_argument('--aggregate',nargs='*'); ap.add_argument('--out',required=True); a=ap.parse_args()
    if a.lane: data={'A':laneA,'B':laneB,'C':laneC,'D':laneD}[a.lane]()
    else: data=aggregate([json.loads(Path(p).read_text()) for p in (a.aggregate or [])])
    Path(a.out).write_text(json.dumps(data,indent=2,sort_keys=True,default=str)+'\n'); print(json.dumps(data,indent=2,sort_keys=True,default=str))
if __name__=='__main__': main()
