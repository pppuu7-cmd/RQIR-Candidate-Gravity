#!/usr/bin/env python3
"""Exact Constructor for prospectively frozen RCG004 complete 4D parity-even algebraic curvature-cubic class."""
from __future__ import annotations
import argparse, hashlib, json, platform, sys
from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import sympy as sp

PREREG="345213253f2ecf415af40cb4fbae47b4f58d8870"
HELDOUT="5f83a594309429b45a8edd1bdc72b9653fffdc75"
AUTH="28781bc1873413b214f751eaa963cf1c51423e0b"
PARENT="72f9ab2ab5ad85259a18fc1f368777c431a56324"

def sha(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def matchings(items):
    items=tuple(items)
    if not items:
        yield (); return
    a=items[0]
    for i in range(1,len(items)):
        b=items[i]; rest=items[1:i]+items[i+1:]
        for m in matchings(rest): yield tuple(sorted(((min(a,b),max(a,b)),)+m))

def local_group(offset):
    out={}
    for exch in (0,1):
      for s1 in (0,1):
       for s2 in (0,1):
        arr=[0,1,2,3]; sign=1
        if s1: arr[0],arr[1]=arr[1],arr[0]; sign*=-1
        if s2: arr[2],arr[3]=arr[3],arr[2]; sign*=-1
        if exch: arr=[arr[2],arr[3],arr[0],arr[1]]
        inv=[0]*4
        for new,old in enumerate(arr): inv[old]=new
        out[tuple(offset+x for x in inv)]=sign
    return list(out.items())

def symmetry_group():
    ls=[local_group(4*k) for k in range(3)]; out=[]
    for fp in permutations(range(3)):
      for (p0,s0),(p1,s1),(p2,s2) in product(*ls):
        maps=[p0,p1,p2]; P=[None]*12
        for f in range(3):
          for i in range(4): P[4*f+i]=4*fp[f]+maps[f][i]-4*f
        out.append((tuple(P),s0*s1*s2))
    return out

def transform_matching(m,P): return tuple(sorted((min(P[a],P[b]),max(P[a],P[b])) for a,b in m))

def canonical_classes(raw):
    G=symmetry_group(); unseen=set(raw); nonzero=[]; zero=[]
    while unseen:
        m=min(unseen); d=defaultdict(set)
        for P,s in G: d[transform_matching(m,P)].add(s)
        unseen-=set(d); rep=min(d)
        (zero if any(len(v)>1 for v in d.values()) else nonzero).append(rep)
    return sorted(nonzero),sorted(zero)

# Exact generic 4D algebraic curvature tensor as Sym^2(Lambda^2) with the one 4D Bianchi relation.
PAIRS=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]; PI={p:i for i,p in enumerate(PAIRS)}
VAR={}; VN=[]
for i in range(6):
  for j in range(i,6):
    if (i,j)==(2,3): continue
    VAR[(i,j)]=len(VN); VN.append(f"s{i}{j}")

def sform(i,j):
    if i>j: i,j=j,i
    if (i,j)==(2,3): return {VAR[(1,4)]:1,VAR[(0,5)]:-1}
    return {VAR[(i,j)]:1}

def opair(a,b):
    if a==b:return None,0
    return (PI[(a,b)],1) if a<b else (PI[(b,a)],-1)

def rform(a,b,c,d):
    p,s1=opair(a,b); q,s2=opair(c,d)
    if p is None or q is None:return {}
    return {k:s1*s2*v for k,v in sform(p,q).items()}

def p3(out,a,b,c,coef=1):
    for i,x in a.items():
      for j,y in b.items():
       for k,z in c.items(): out[tuple(sorted((i,j,k)))]+=coef*x*y*z

def universal_poly(m):
    slot=[None]*12
    for e,(a,b) in enumerate(m):slot[a]=slot[b]=e
    out=defaultdict(int)
    for vals in product(range(4),repeat=6):
        ind=[vals[slot[s]] for s in range(12)]
        a=rform(*ind[:4]); b=rform(*ind[4:8]); c=rform(*ind[8:])
        if a and b and c:p3(out,a,b,c)
    return {k:v for k,v in out.items() if v}

def universal_matrix(polys):
    mons=sorted(set().union(*(p.keys() for p in polys))); mi={m:i for i,m in enumerate(mons)}
    M=sp.MutableSparseMatrix(len(mons),len(polys),{})
    for j,p in enumerate(polys):
      for m,v in p.items():M[mi[m],j]=v
    return M,mons

def metric_compact_verified():
    t,x,y,z=sp.symbols("t x y z"); coords=(t,x,y,z)
    a,b,c=[sp.Function(n)(t) for n in ("a","b","c")]
    q=[a,b,c]; g=sp.diag(-1,sp.exp(2*a),sp.exp(2*b),sp.exp(2*c)); gi=g.inv(); n=4
    G=[[[sp.Integer(0) for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for r in range(n):
      for m in range(n):
       for nu in range(n):
        G[r][m][nu]=sp.simplify(sp.Rational(1,2)*sum(gi[r,s]*(sp.diff(g[s,nu],coords[m])+sp.diff(g[s,m],coords[nu])-sp.diff(g[m,nu],coords[s])) for s in range(n)))
    va,vb,vc,ua,ub,uc=sp.symbols("va vb vc ua ub uc"); vs=[va,vb,vc]; us=[ua,ub,uc]
    subs={sp.diff(a,t):va,sp.diff(b,t):vb,sp.diff(c,t):vc,sp.diff(a,(t,2)):ua,sp.diff(b,(t,2)):ub,sp.diff(c,(t,2)):uc}
    scale=[1,sp.exp(-a),sp.exp(-b),sp.exp(-c)]
    def expected(A,B,C,D):
        if A==B or C==D:return 0
        sg=1
        if A>B:A,B=B,A;sg*=-1
        if C>D:C,D=D,C;sg*=-1
        if (A,B)>(C,D):A,B,C,D=C,D,A,B
        if (A,B)!=(C,D):return 0
        if A==0:return -sg*(us[B-1]+vs[B-1]**2)
        return sg*vs[A-1]*vs[B-1]
    for A,B,C,D in product(range(4),repeat=4):
        # compute only requested component directly from Christoffels
        rup=sp.diff(G[A][D][B],coords[C])-sp.diff(G[A][C][B],coords[D])+sum(G[A][C][l]*G[l][D][B]-G[A][D][l]*G[l][C][B] for l in range(n))
        rcov=sp.simplify(sum(g[A,k]*(sp.diff(G[k][D][B],coords[C])-sp.diff(G[k][C][B],coords[D])+sum(G[k][C][l]*G[l][D][B]-G[k][D][l]*G[l][C][B] for l in range(n))) for k in range(n)))
        rh=sp.expand(sp.simplify(rcov*scale[A]*scale[B]*scale[C]*scale[D]).subs(subs))
        if sp.expand(rh-expected(A,B,C,D))!=0:return False
    return True

# Fast exact Lorentzian triaxial polynomial evaluation, after metric-derived table is verified.
NV=6; ETA=[-1,1,1,1]
def mono(i,p=1): e=[0]*NV;e[i]=p;return tuple(e)
def madd(a,b):return tuple(x+y for x,y in zip(a,b))
def rhpoly(a,b,c,d):
    if a==b or c==d:return {}
    sg=1
    if a>b:a,b=b,a;sg*=-1
    if c>d:c,d=d,c;sg*=-1
    if (a,b)>(c,d):a,b,c,d=c,d,a,b
    if (a,b)!=(c,d):return {}
    if a==0:
        i=b-1;return {mono(i):-sg,mono(3+i,2):-sg}
    e=[0]*NV;e[3+a-1]+=1;e[3+b-1]+=1;return {tuple(e):sg}

def invariant_poly(m):
    slot=[None]*12
    for e,(a,b) in enumerate(m):slot[a]=slot[b]=e
    out=defaultdict(int)
    for vals in product(range(4),repeat=6):
        sg=1
        for z in vals:sg*=ETA[z]
        ind=[vals[slot[s]] for s in range(12)]; fs=[rhpoly(*ind[o:o+4]) for o in (0,4,8)]
        if not all(fs):continue
        for m1,c1 in fs[0].items():
          for m2,c2 in fs[1].items():
           for m3,c3 in fs[2].items():out[madd(madd(m1,m2),m3)]+=sg*c1*c2*c3
    return {m:v for m,v in out.items() if v}

def deriv(p,i):
    out={}
    for m,c in p.items():
      if m[i]:
        q=list(m);f=q[i];q[i]-=1;out[tuple(q)]=c*f
    return out

def hessian_matrix(invs):
    rows=[]
    for i,j in ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2)):
      cols=[deriv(deriv(p,i),j) for p in invs]; mons=sorted(set().union(*(p.keys() for p in cols)))
      for m in mons:
        r=[p.get(m,0) for p in cols]
        if any(r):rows.append(r)
    return sp.Matrix(rows)

def generic_embedding(B,mons):
    mi={m:i for i,m in enumerate(mons)}
    def ladd(a,b):
      z=defaultdict(int)
      for k,v in a.items():z[k]+=v
      for k,v in b.items():z[k]+=v
      return {k:v for k,v in z.items() if v}
    def pmul(p,q):
      z=defaultdict(int)
      for m,a in p.items():
       for n,b in q.items():z[tuple(sorted(m+n))]+=a*b
      return {k:v for k,v in z.items() if v}
    def lp(l):return {(k,):v for k,v in l.items()}
    Ric=[[{} for _ in range(4)] for __ in range(4)]
    for b in range(4):
      for d in range(4):
        q={}
        for a in range(4):q=ladd(q,rform(a,b,a,d))
        Ric[b][d]=q
    R={}
    for b in range(4):R=ladd(R,Ric[b][b])
    Rp=lp(R); R3=pmul(pmul(Rp,Rp),Rp)
    Ric2={}
    for b,d in product(range(4),repeat=2):
      q=pmul(lp(Ric[b][d]),lp(Ric[b][d])); Ric2=ladd(Ric2,q)
    RR2=pmul(Rp,Ric2); Ric3={}
    for a,b,c in product(range(4),repeat=3):Ric3=ladd(Ric3,pmul(pmul(lp(Ric[a][b]),lp(Ric[b][c])),lp(Ric[c][a])))
    allmons=sorted(set(mons)|set(R3)|set(RR2)|set(Ric3)); ix={m:i for i,m in enumerate(allmons)}
    BM=sp.zeros(len(allmons),B.shape[1])
    for oldm,row in mi.items():
      for j in range(B.shape[1]):BM[ix[oldm],j]=B[row,j]
    def vec(p):
      v=sp.zeros(len(allmons),1)
      for m,c in p.items():v[ix[m],0]=c
      return v
    coords=[]
    for p in (R3,RR2,Ric3):coords.append(sp.Matrix(next(iter(sp.linsolve((BM,vec(p)))))))
    return coords

def conventional_old_ray_axisym_regression():
    va,vb,vc,ua,ub,uc=sp.symbols("va vb vc ua ub uc"); vs=[va,vb,vc]; us=[ua,ub,uc]; eta=[-1,1,1,1]
    def R(A,B,C,D):
      if A==B or C==D:return 0
      sg=1
      if A>B:A,B=B,A;sg*=-1
      if C>D:C,D=D,C;sg*=-1
      if (A,B)>(C,D):A,B,C,D=C,D,A,B
      if (A,B)!=(C,D):return 0
      return -sg*(us[B-1]+vs[B-1]**2) if A==0 else sg*vs[A-1]*vs[B-1]
    Ric=sp.zeros(4,4)
    for b,d in product(range(4),repeat=2):Ric[b,d]=sp.expand(sum(eta[a]*R(a,b,a,d) for a in range(4)))
    Rs=sp.expand(sum(eta[b]*Ric[b,b] for b in range(4)))
    R2=sp.expand(sum(eta[b]*eta[d]*Ric[b,d]**2 for b,d in product(range(4),repeat=2)))
    M=sp.diag(*[eta[a]*Ric[a,a] for a in range(4)]); R3=sp.expand(sp.trace(M**3))
    O=sp.expand(7*Rs**3-36*Rs*R2+36*R3); H=sp.Matrix([[sp.diff(O,us[i],us[j]) for j in range(3)] for i in range(3)])
    J=sp.Matrix([[1,0],[0,1],[0,1]]); Hax=sp.expand(J.T*H.subs({vc:vb,uc:ub})*J)
    E=sp.Matrix([[-48*(2*ua+ub+2*va**2+va*vb),-48*(ua-4*ub+va**2+2*va*vb-6*vb**2)],[-48*(ua-4*ub+va**2+2*va*vb-6*vb**2),48*(4*ua-7*ub+4*va**2+5*va*vb-12*vb**2)]])
    return all(sp.expand(Hax[i,j]-E[i,j])==0 for i in range(2) for j in range(2))

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",required=True);ap.add_argument("--run-head",default="");args=ap.parse_args()
    raw=list(matchings(range(12))); reps,zeros=canonical_classes(raw)
    polys=[universal_poly(m) for m in reps]; U,mons=universal_matrix(polys); rank=U.rank(); _,piv=U.rref(); kernel=U.nullspace()
    basis=[reps[i] for i in piv]; basis_polys=[invariant_poly(m) for m in basis]; H=hessian_matrix(basis_polys); hr=H.rank(); hk=H.nullspace()
    metric_ok=metric_compact_verified(); coords=generic_embedding(U[:,list(piv)],mons); emb=sp.Matrix.hstack(*coords); old=7*coords[0]-36*coords[1]+36*coords[2]
    axis_ok=conventional_old_ray_axisym_regression()
    result={
      "gate":"RCG004_COMPLETE_PARITY_EVEN_ALGEBRAIC_CUBIC_CURVATURE_FAMILY_V0_PRIMARY",
      "prereg_sha":PREREG,"heldout_prereg_sha":HELDOUT,"authority_terminal":AUTH,"parent_terminal":PARENT,"run_head":args.run_head,
      "source":"VACUUM_ZERO","field_redefinition_equivalence":"OUT_OF_SCOPE_RCG004_V0",
      "raw_contraction_count":len(raw),"raw_manifest_sha256":sha(raw),"canonical_nonzero_class_count":len(reps),"canonical_zero_class_count":len(zeros),
      "canonical_nonzero_classes":[[list(x) for x in m] for m in reps],"canonical_zero_classes":[[list(x) for x in m] for m in zeros],
      "universal_generic_curvature_dimension":20,"universal_polynomial_monomials":len(mons),"universal_matrix_shape":list(U.shape),"universal_matrix_sha256":sha([[int(U[i,j]) for j in range(U.cols)] for i in range(U.rows)]),
      "quotient_rank":rank,"quotient_dimension":rank,"quotient_pivot_class_indices":list(piv),"quotient_basis_matchings":[[list(x) for x in m] for m in basis],
      "relation_nullity":len(kernel),"relation_kernel_basis":[[str(x) for x in v] for v in kernel],
      "metric_to_compact_orthonormal_riemann_verified":metric_ok,
      "primary_hessian_rows":H.rows,"primary_hessian_columns":H.cols,"primary_hessian_rank":hr,"primary_hessian_nullity":len(basis)-hr,"primary_hessian_kernel":[[str(x) for x in v] for v in hk],"primary_hessian_matrix_sha256":sha([[str(H[i,j]) for j in range(H.cols)] for i in range(H.rows)]),
      "rcg003_embedding_rank":emb.rank(),"rcg003_embedding_coordinates":{"R3":[str(x) for x in coords[0]],"R_Ricci2":[str(x) for x in coords[1]],"Ricci3":[str(x) for x in coords[2]],"old_ray_7_m36_36":[str(x) for x in old]},
      "rcg003_axisymmetric_obstruction_exact_match":axis_ok,
      "controls_valid":bool(metric_ok and axis_ok and emb.rank()==3 and len(raw)==10395 and rank==6 and hr==6),
      "candidate_classification":"FAIL_SCOPED_RCG004_COMPLETE_PARITY_EVEN_ALGEBRAIC_CUBIC_CURVATURE_CLASS_HAS_NO_NONZERO_TRIAXIAL_SECOND_ORDER_SURVIVOR" if hr==rank and hr==len(basis) else "PRIMARY_NONZERO_SURVIVOR_REQUIRES_CURL",
      "heldout_status":"NOT_APPLICABLE_PRIMARY_NULLITY_ZERO" if len(basis)-hr==0 else "REQUIRED_ON_PRIMARY_SURVIVOR_SUBSPACE",
      "environment":{"python":sys.version.split()[0],"sympy":sp.__version__,"platform":platform.platform()},
      "claim_locks":{"chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","theory_established":"0%","GR_derived":False,"all_cubic_gravity_fails":False,"quantum_gravity":False,"new_physics":False}
    }
    result["scientific_payload_sha256"]=sha(result)
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:result[k] for k in ("raw_contraction_count","canonical_nonzero_class_count","quotient_dimension","primary_hessian_rank","primary_hessian_nullity","rcg003_axisymmetric_obstruction_exact_match","candidate_classification")},sort_keys=True))
if __name__=="__main__":main()
