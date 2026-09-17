#!/usr/bin/env python3
"""Independent Critic for RCG004 complete cubic class. Does not import Constructor code, matrices, basis, kernel or verdict."""
from __future__ import annotations
import argparse, hashlib, json, platform, sys
from collections import defaultdict
from itertools import permutations, product
from pathlib import Path
import sympy as sp

PREREG="345213253f2ecf415af40cb4fbae47b4f58d8870"; HELDOUT="5f83a594309429b45a8edd1bdc72b9653fffdc75"; AUTH="28781bc1873413b214f751eaa963cf1c51423e0b"; PARENT="72f9ab2ab5ad85259a18fc1f368777c431a56324"
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def pairings(rem):
    if not rem: yield (); return
    x=max(rem); rest=[q for q in rem if q!=x]
    for y in rest:
      rem2=[q for q in rest if q!=y]
      for tail in pairings(rem2):yield tuple(sorted(tail+((min(x,y),max(x,y)),)))

def local_syms():
    out=[]
    for ex in (0,1):
      for s1 in (0,1):
       for s2 in (0,1):
        arr=[0,1,2,3];sg=1
        if s1:arr[0],arr[1]=arr[1],arr[0];sg*=-1
        if s2:arr[2],arr[3]=arr[3],arr[2];sg*=-1
        if ex:arr=[arr[2],arr[3],arr[0],arr[1]]
        inv=[0]*4
        for n,o in enumerate(arr):inv[o]=n
        out.append((tuple(inv),sg))
    return out
LS=local_syms()
def transforms():
    out=[]
    for fp in permutations((0,1,2)):
      for l0,l1,l2 in product(LS,repeat=3):
        ls=[l0,l1,l2];P=[None]*12;sg=1
        for f in range(3):
          lp,s=ls[f];sg*=s
          for i in range(4):P[4*f+i]=4*fp[f]+lp[i]
        out.append((tuple(P),sg))
    return out
TG=transforms()
def tmatch(m,P):return tuple(sorted((min(P[a],P[b]),max(P[a],P[b])) for a,b in m))
def classes(raw):
    unseen=set(raw);nz=[];zz=[]
    while unseen:
      m=next(iter(unseen));d=defaultdict(set)
      for P,s in TG:d[tmatch(m,P)].add(s)
      unseen-=set(d); rep=min(d)
      (zz if any(len(v)>1 for v in d.values()) else nz).append(rep)
    return sorted(nz),sorted(zz)

# Distinct exact universal tensor route: self-dual/anti-self-dual Lambda^2 block parametrization with tr(A)=tr(C).
U=sp.Matrix([[1,0,0,1,0,0],[0,1,0,0,1,0],[0,0,1,0,0,1],[0,0,1,0,0,-1],[0,-1,0,0,1,0],[1,0,0,-1,0,0]])
X=sp.symbols("x0:20"); it=iter(X);A=sp.zeros(3,3);B=sp.zeros(3,3);C=sp.zeros(3,3)
for i in range(3):
  for j in range(i,3):z=next(it);A[i,j]=A[j,i]=z
for i in range(3):
  for j in range(3):B[i,j]=next(it)
for i,j in ((0,0),(0,1),(0,2),(1,1),(1,2)):
    z=next(it);C[i,j]=C[j,i]=z
C[2,2]=sp.trace(A)-C[0,0]-C[1,1]
M=A.row_join(B).col_join(B.T.row_join(C)); S=sp.expand(U*M*U.T); XI={x:i for i,x in enumerate(X)}
SF={}
for i,j in product(range(6),repeat=2):
    p=sp.Poly(S[i,j],*X,domain=sp.QQ);SF[(i,j)]={XI[x]:int(p.coeff_monomial(x)) for x in X if p.coeff_monomial(x)}
PAIRS=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)];PI={p:i for i,p in enumerate(PAIRS)}
def op(a,b):
    if a==b:return None,0
    return (PI[(a,b)],1) if a<b else (PI[(b,a)],-1)
def rf(a,b,c,d):
    p,s1=op(a,b);q,s2=op(c,d)
    if p is None or q is None:return {}
    return {k:s1*s2*v for k,v in SF[(p,q)].items()}
def p3(out,a,b,c):
    for i,x in a.items():
      for j,y in b.items():
       for k,z in c.items():out[tuple(sorted((i,j,k)))]+=x*y*z
def upoly(m):
    slot=[None]*12
    for e,(a,b) in enumerate(m):slot[a]=slot[b]=e
    out=defaultdict(int)
    for vals in product(range(4),repeat=6):
      ind=[vals[slot[s]] for s in range(12)];a=rf(*ind[:4]);b=rf(*ind[4:8]);c=rf(*ind[8:])
      if a and b and c:p3(out,a,b,c)
    return {k:v for k,v in out.items() if v}

def exact_quotient(reps):
    polys=[upoly(m) for m in reps]; mons=sorted(set().union(*(p.keys() for p in polys)));mi={m:i for i,m in enumerate(mons)}
    Q=sp.MutableSparseMatrix(len(mons),len(polys),{})
    for j,p in enumerate(polys):
      for m,v in p.items():Q[mi[m],j]=v
    # reverse column order before pivoting to force an independently selected basis
    R=Q[:,::-1];rank=R.rank();_,pv=R.rref();basis_idx=[len(reps)-1-i for i in pv]
    return Q,mons,rank,basis_idx

# Independent direct metric derivation verification of compact orthonormal Bianchi-I curvature table.
def metric_verified():
    t,x,y,z=sp.symbols("t x y z");coords=(t,x,y,z);a,b,c=[sp.Function(n)(t) for n in ("a","b","c")]
    g=sp.diag(-1,sp.exp(2*a),sp.exp(2*b),sp.exp(2*c));gi=g.inv();n=4
    G=[[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for r,m,q in product(range(n),repeat=3):G[r][m][q]=sp.simplify(sp.Rational(1,2)*sum(gi[r,s]*(sp.diff(g[s,q],coords[m])+sp.diff(g[s,m],coords[q])-sp.diff(g[m,q],coords[s])) for s in range(n)))
    va,vb,vc,ua,ub,uc=sp.symbols("va vb vc ua ub uc");vs=[va,vb,vc];us=[ua,ub,uc]
    sub={sp.diff(a,t):va,sp.diff(b,t):vb,sp.diff(c,t):vc,sp.diff(a,(t,2)):ua,sp.diff(b,(t,2)):ub,sp.diff(c,(t,2)):uc};sc=[1,sp.exp(-a),sp.exp(-b),sp.exp(-c)]
    def ex(A,B,C,D):
      if A==B or C==D:return 0
      sg=1
      if A>B:A,B=B,A;sg*=-1
      if C>D:C,D=D,C;sg*=-1
      if (A,B)>(C,D):A,B,C,D=C,D,A,B
      if (A,B)!=(C,D):return 0
      return -sg*(us[B-1]+vs[B-1]**2) if A==0 else sg*vs[A-1]*vs[B-1]
    for A0,B0,C0,D0 in product(range(4),repeat=4):
      rc=0
      for k in range(4):
        rup=sp.diff(G[k][D0][B0],coords[C0])-sp.diff(G[k][C0][B0],coords[D0])+sum(G[k][C0][l]*G[l][D0][B0]-G[k][D0][l]*G[l][C0][B0] for l in range(4))
        rc+=g[A0,k]*rup
      rh=sp.expand(sp.simplify(rc*sc[A0]*sc[B0]*sc[C0]*sc[D0]).subs(sub))
      if sp.expand(rh-ex(A0,B0,C0,D0))!=0:return False
    return True

NV=6;ETA=[-1,1,1,1]
def mono(i,p=1):e=[0]*NV;e[i]=p;return tuple(e)
def madd(a,b):return tuple(x+y for x,y in zip(a,b))
def rh(a,b,c,d):
    if a==b or c==d:return{}
    sg=1
    if a>b:a,b=b,a;sg*=-1
    if c>d:c,d=d,c;sg*=-1
    if (a,b)>(c,d):a,b,c,d=c,d,a,b
    if (a,b)!=(c,d):return{}
    if a==0:
      i=b-1;return{mono(i):-sg,mono(3+i,2):-sg}
    e=[0]*NV;e[3+a-1]+=1;e[3+b-1]+=1;return{tuple(e):sg}
def invpoly(m):
    slot=[None]*12
    for e,(a,b) in enumerate(m):slot[a]=slot[b]=e
    out=defaultdict(int)
    for vals in product(range(4),repeat=6):
      sg=1
      for z in vals:sg*=ETA[z]
      ind=[vals[slot[s]] for s in range(12)];fs=[rh(*ind[o:o+4]) for o in (0,4,8)]
      if not all(fs):continue
      for m1,c1 in fs[0].items():
       for m2,c2 in fs[1].items():
        for m3,c3 in fs[2].items():out[madd(madd(m1,m2),m3)]+=sg*c1*c2*c3
    return {m:v for m,v in out.items() if v}
def der(p,i):
    o={}
    for m,c in p.items():
      if m[i]:q=list(m);f=q[i];q[i]-=1;o[tuple(q)]=c*f
    return o
def hmat(invs):
    rows=[]
    for i,j in ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2)):
      cols=[der(der(p,i),j) for p in invs];mons=set().union(*(p.keys() for p in cols))
      for m in mons:
        r=[p.get(m,0) for p in cols]
        if any(r):rows.append(r)
    return sp.Matrix(rows)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",required=True);ap.add_argument("--run-head",default="");args=ap.parse_args()
    raw=list(pairings(list(range(12)))); reps,zeros=classes(raw)
    bianchi_ok=sp.expand(S[0,5]-S[1,4]+S[2,3])==0
    Q,mons,qr,bidx=exact_quotient(reps);basis=[reps[i] for i in bidx];H=hmat([invpoly(m) for m in basis]);hr=H.rank();metric_ok=metric_verified()
    result={"lane":"INDEPENDENT_CRITIC","prereg_sha":PREREG,"heldout_prereg_sha":HELDOUT,"authority_terminal":AUTH,"parent_terminal":PARENT,"run_head":args.run_head,
      "method":"REVERSE_RAW_PAIRING_ENUMERATION_PLUS_SELFDUAL_ANTISELFDUAL_GENERIC_CURVATURE_PLUS_INDEPENDENT_METRIC_DERIVATION",
      "constructor_not_imported":True,"source":"VACUUM_ZERO","field_redefinition_equivalence":"OUT_OF_SCOPE_RCG004_V0",
      "raw_contraction_count":len(raw),"raw_manifest_sha256":sha(raw),"canonical_nonzero_class_count":len(reps),"canonical_zero_class_count":len(zeros),"canonical_nonzero_classes":[[list(x) for x in m] for m in reps],
      "generic_curvature_dimension":20,"selfdual_bianchi_exact":bool(bianchi_ok),"universal_polynomial_monomials":len(mons),"quotient_rank":qr,"quotient_dimension":qr,"critic_basis_class_indices":bidx,
      "metric_to_compact_orthonormal_riemann_verified":metric_ok,"primary_hessian_rows":H.rows,"primary_hessian_columns":H.cols,"primary_hessian_rank":hr,"primary_hessian_nullity":len(basis)-hr,"primary_hessian_matrix_sha256":sha([[str(H[i,j]) for j in range(H.cols)] for i in range(H.rows)]),
      "controls_valid":bool(len(raw)==10395 and len(reps)==13 and len(zeros)==20 and bianchi_ok and qr==6 and metric_ok and hr==6),
      "classification":"PASS_INDEPENDENT_CRITIC_RCG004_COMPLETENESS_AND_PRIMARY_NULLITY_ZERO" if len(raw)==10395 and qr==6 and hr==6 and metric_ok else "INVALID_RCG004_CRITIC",
      "environment":{"python":sys.version.split()[0],"sympy":sp.__version__,"platform":platform.platform()},"claim_locks":{"chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","theory_established":"0%","new_physics":False}}
    result["scientific_payload_sha256"]=sha(result);Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:result[k] for k in ("raw_contraction_count","canonical_nonzero_class_count","quotient_dimension","critic_basis_class_indices","primary_hessian_rank","primary_hessian_nullity","classification")},sort_keys=True))
if __name__=="__main__":main()
