#!/usr/bin/env python3
"""Direct Euler-Lagrange highest-derivative cross-check for RCG004 quotient basis."""
from __future__ import annotations
import argparse, hashlib, json, platform, sys
from collections import defaultdict
from itertools import product
from pathlib import Path
import sympy as sp

PREREG="345213253f2ecf415af40cb4fbae47b4f58d8870"; HELDOUT="5f83a594309429b45a8edd1bdc72b9653fffdc75"; AUTH="28781bc1873413b214f751eaa963cf1c51423e0b"
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()

# Exact compact orthonormal Riemann polynomial for triaxial Bianchi-I, independently used here only after metric identity verification.
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
    m=[tuple(x) for x in m];slot=[None]*12
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
        rup=sp.diff(G[k][D0][B0],coords[C0])-sp.diff(G[k][C0][B0],coords[D0])+sum(G[k][C0][l]*G[l][D0][B0]-G[k][D0][l]*G[l][C0][B0] for l in range(4));rc+=g[A0,k]*rup
      rhv=sp.expand(sp.simplify(rc*sc[A0]*sc[B0]*sc[C0]*sc[D0]).subs(sub))
      if sp.expand(rhv-ex(A0,B0,C0,D0))!=0:return False
    return True

def expr_from_poly(p,us,vs):
    out=0
    for m,c in p.items():
      t=sp.Integer(c)
      for z,e in zip(us+vs,m):t*=z**e
      out+=t
    return sp.expand(out)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--constructor-json",required=True);ap.add_argument("--output",required=True);ap.add_argument("--run-head",default="");args=ap.parse_args()
    C=json.loads(Path(args.constructor_json).read_text()); basis=C["quotient_basis_matchings"]
    ua,ub,uc,va,vb,vc,wa,wb,wc,xa,xb,xc=sp.symbols("ua ub uc va vb vc wa wb wc xa xb xc");us=[ua,ub,uc];vs=[va,vb,vc];ws=[wa,wb,wc];xs=[xa,xb,xc]
    invs=[expr_from_poly(invpoly(m),us,vs) for m in basis];Sdot=sum(vs)
    def Dbar(P):
      q=sp.expand(Sdot*P)
      for i in range(3):q+=sp.diff(P,vs[i])*us[i]+sp.diff(P,us[i])*ws[i]+sp.diff(P,ws[i])*xs[i]
      return sp.expand(q)
    EL=[]
    for F in invs:EL.append([sp.expand(F-Dbar(sp.diff(F,vs[i]))+Dbar(Dbar(sp.diff(F,us[i])))) for i in range(3)])
    allvars=xs+ws+us+vs; high=[]; fourth=[]; third=[]; correspondence=True
    for bj,F in enumerate(invs):
      H=[[sp.diff(F,us[i],us[j]) for j in range(3)] for i in range(3)]
      for i in range(3):
        for j in range(3):
          if sp.expand(sp.diff(EL[bj][i],xs[j])-H[i][j])!=0:correspondence=False
    for ei in range(3):
      cols=[dict(sp.Poly(EL[b][ei],*allvars,domain=sp.QQ).terms()) for b in range(len(invs))];mons=set().union(*(d.keys() for d in cols))
      for mon in mons:
        hasx=any(mon[k] for k in range(3));hasw=any(mon[k] for k in range(3,6))
        if not(hasx or hasw):continue
        row=[cols[j].get(mon,0) for j in range(len(invs))]
        if any(row):
          high.append(row)
          if hasx:fourth.append(row)
          else:third.append(row)
    HIG=sp.Matrix(high);F4=sp.Matrix(fourth);F3=sp.Matrix(third);metric_ok=metric_verified()
    result={"lane":"DIRECT_EULER_LAGRANGE_ADVERSARIAL_CROSSCHECK","prereg_sha":PREREG,"heldout_prereg_sha":HELDOUT,"authority_terminal":AUTH,"run_head":args.run_head,"basis_manifest_sha256":sha(basis),"basis_dimension":len(basis),
      "metric_to_compact_orthonormal_riemann_verified":metric_ok,"high_derivative_rows":HIG.rows,"high_derivative_rank":HIG.rank(),"high_derivative_nullity":len(basis)-HIG.rank(),"fourth_derivative_rows":F4.rows,"fourth_derivative_rank":F4.rank(),"third_derivative_rows":F3.rows,"third_derivative_rank":F3.rank(),"fourth_hessian_correspondence":bool(correspondence),
      "classification":"PASS_RCG004_DIRECT_EL_CONFIRMS_PRIMARY_NULLITY_ZERO" if metric_ok and correspondence and HIG.rank()==len(basis) and F4.rank()==len(basis) else "INVALID_RCG004_EULER_CROSSCHECK",
      "environment":{"python":sys.version.split()[0],"sympy":sp.__version__,"platform":platform.platform()},"claim_locks":{"chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","theory_established":"0%"}}
    result["scientific_payload_sha256"]=sha(result);Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n");print(json.dumps({k:result[k] for k in ("basis_dimension","high_derivative_rank","fourth_derivative_rank","third_derivative_rank","fourth_hessian_correspondence","classification")},sort_keys=True))
if __name__=="__main__":main()
