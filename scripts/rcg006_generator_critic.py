#!/usr/bin/env python3
"""Independent pre-map Critic for RCG006 generator completeness.

Uses reverse pairing enumeration, the pre-existing self-dual/anti-self-dual generic-curvature route,
and an independently indexed normal-coordinate fourth-metric-jet reconstruction. It imports no RCG006 Constructor data.
"""
from __future__ import annotations
import argparse, hashlib, json, platform, sys
from collections import defaultdict
from itertools import combinations, product
from pathlib import Path
import sympy as sp
sys.path.insert(0,"scripts")
import rcg004_complete_cubic_critic as c4

SELECTION="dc955720822d353d446186437ee2ca69458633bd"
PREREG="fc3ff1f49c56f2befc039e09ebd8f388833dbff1"
HELDOUT="43748579a78f40e0825d5ae01dc634d55ba7b928"
PARENT="aef9882924ffd128c6c30934e4f95394aae874fc"
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()

def pairings(rem):
    rem=tuple(rem)
    if not rem:yield ();return
    x=rem[-1]
    for k in range(len(rem)-1):
        y=rem[k];rest=rem[:k]+rem[k+1:-1]
        for t in pairings(rest):yield tuple(sorted(t+((min(x,y),max(x,y)),)))

def raw(n):
    out=[]
    for j,i in reversed(list(combinations(range(n),2))):
        # reversed orientation/order intentionally differs; canonical output symmetrization erases label convention
        rem=[x for x in range(n) if x not in (i,j)]
        for m in pairings(rem):out.append(("free",min(i,j),max(i,j),tuple(m)))
    for m in pairings(range(n)):out.append(("metric",tuple(m)))
    return out

def add(o,p,c=sp.Rational(1)):
    for k,v in p.items():o[k]+=c*v

def mul(a,b):
    o=defaultdict(sp.Rational)
    for i,x in a.items():
      for j,y in b.items():o[tuple(sorted((i,j)))]+=x*y
    return dict(o)
def slots(n,m,free):
    s=[None]*n
    for k,v in free.items():s[k]=v
    for e,(a,b) in enumerate(m):s[a]=s[b]=("e",e)
    return s

def algcomp(r,u,v):
    if r[0]=="metric":
        if u!=v:return{}
        m=r[1];free={}
    else:
        _,i,j,m=r;free={i:u,j:v}
    s=slots(8,m,free);o=defaultdict(sp.Rational)
    for vals in product(range(4),repeat=len(m)):
        ind=[vals[z[1]] if isinstance(z,tuple) else z for z in s]
        a=c4.rf(*ind[:4]);b=c4.rf(*ind[4:])
        if a and b:add(o,mul(a,b))
    return dict(o)
def algcol(r):
    o=defaultdict(sp.Rational)
    for u in range(4):
      for v in range(u,4):
        p=algcomp(r,u,v);q=algcomp(r,v,u) if r[0]=="free" else p
        for m,c in p.items():o[(u,v,m)]+=c
        for m,c in q.items():o[(u,v,m)]+=c
    return {k:v for k,v in o.items() if v}

# Independent indexing: derivative multi-index first, metric pair second, and opposite overall R convention.
H=[]
for a in range(4):
 for b in range(a,4):
  for c in range(b,4):
   for d in range(c,4):
    for m in range(4):
     for n in range(m,4):H.append(((a,b,c,d),(m,n)))
HI={k:i for i,k in enumerate(H)}
def h(m,n,a,b,c,d):return {HI[(tuple(sorted((a,b,c,d))),tuple(sorted((m,n))))]:sp.Rational(1)}
def lin(*ts):
    o=defaultdict(sp.Rational)
    for c,p in ts:add(o,p,c)
    return dict(o)
def d2(e,f,a,b,c,d):
    # opposite convention to Constructor; rank/span dimension is convention-invariant
    return lin((-sp.Rational(1,2),h(a,d,b,c,e,f)),(-sp.Rational(1,2),h(b,c,a,d,e,f)),(sp.Rational(1,2),h(a,c,b,d,e,f)),(sp.Rational(1,2),h(b,d,a,c,e,f)))
def dercomp(r,u,v):
    if r[0]=="metric":
        if u!=v:return{}
        m=r[1];free={}
    else:
        _,i,j,m=r;free={i:u,j:v}
    s=slots(6,m,free);o=defaultdict(sp.Rational)
    for vals in product(range(4),repeat=len(m)):
        ind=[vals[z[1]] if isinstance(z,tuple) else z for z in s];add(o,d2(*ind))
    return dict(o)
def dercol(r):
    o=defaultdict(sp.Rational)
    for u in range(4):
      for v in range(u,4):
        p=dercomp(r,u,v);q=dercomp(r,v,u) if r[0]=="free" else p
        for k,c in p.items():o[(u,v,k)]+=c
        for k,c in q.items():o[(u,v,k)]+=c
    return {k:v for k,v in o.items() if v}
def mat(cols):
    rows=sorted(set().union(*(x.keys() for x in cols)));ix={r:i for i,r in enumerate(rows)};M=sp.MutableSparseMatrix(len(rows),len(cols),{})
    for j,x in enumerate(cols):
      for r,v in x.items():M[ix[r],j]=v
    return M,rows

def comm(e,f,a,b,c,d):
    # Critic uses the opposite R convention, so its commutator sign is independently paired to c4.rf.
    o=defaultdict(sp.Rational)
    for p in range(4):
      for z in (mul(c4.rf(p,a,e,f),c4.rf(p,b,c,d)),mul(c4.rf(p,b,e,f),c4.rf(a,p,c,d)),mul(c4.rf(p,c,e,f),c4.rf(a,b,p,d)),mul(c4.rf(p,d,e,f),c4.rf(a,b,c,p))):add(o,z,1)
    return dict(o)
def commcomp(r,u,v):
    if r[0]=="metric":
        if u!=v:return{}
        m=r[1];free={}
    else:
        _,i,j,m=r;free={i:u,j:v}
    s=slots(6,m,free);o=defaultdict(sp.Rational)
    for vals in product(range(4),repeat=len(m)):
        ind=[vals[z[1]] if isinstance(z,tuple) else z for z in s];add(o,comm(*ind))
    return dict(o)
def commcol(r):
    o=defaultdict(sp.Rational)
    for u in range(4):
      for v in range(u,4):
        p=commcomp(r,u,v);q=commcomp(r,v,u) if r[0]=="free" else p
        for k,c in p.items():o[(u,v,k)]+=c
        for k,c in q.items():o[(u,v,k)]+=c
    return {k:v for k,v in o.items() if v}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",required=True);ap.add_argument("--run-head",default="");a=ap.parse_args()
    ar=raw(8);dr=raw(6);AC=[algcol(r) for r in ar];DC=[dercol(r) for r in dr];AM,rows=mat(AC);DM,_=mat(DC)
    # Reverse columns before RREF so Critic pivot labels need not agree with Constructor.
    ARev=AM[:,::-1];DRev=DM[:,::-1];arank=ARev.rank();drank=DRev.rank();_,ap=ARev.rref();_,dp=DRev.rref();api=[len(ar)-1-i for i in ap];dpi=[len(dr)-1-i for i in dp]
    AB=AM[:,api];ri={r:i for i,r in enumerate(rows)};ok=True
    for r in dr:
        c=commcol(r);v=sp.zeros(len(rows),1)
        for k,z in c.items():
            if k not in ri:ok=False;break
            v[ri[k],0]=z
        if not ok:break
        if not sp.linsolve((AB,v)):ok=False;break
    res={"phase":"RCG006_GENERATOR_COMPLETENESS_PREMAP_INDEPENDENT_CRITIC","selection_terminal":SELECTION,"scientific_prereg":PREREG,"heldout_prereg":HELDOUT,"parent_rcg005_terminal":PARENT,"run_head":a.run_head,
      "method":"REVERSE_PAIRINGS_PLUS_SELFDUAL_ANTISELFDUAL_GENERIC_CURVATURE_PLUS_INDEPENDENT_NORMAL_COORDINATE_H4_INDEXING",
      "constructor_not_imported":True,"no_M_FR_computed":True,"raw_counts":{"ALG":len(ar),"DER":len(dr),"total":len(ar)+len(dr)},"ALG_generator_dimension":arank,"DER_new_principal_dimension":drank,"generator_dimension_M":arank+drank,"critic_ALG_pivot_raw_indices":api,"critic_DER_pivot_raw_indices":dpi,"normal_coordinate_h4_variable_count":len(H),"commutator_completion_all_in_ALG_span":bool(ok),"classification":"PASS_INDEPENDENT_CRITIC_RCG006_GENERATOR_COMPLETENESS" if ok else "INVALID_RCG006_GENERATOR_CRITIC","environment":{"python":sys.version.split()[0],"sympy":sp.__version__,"platform":platform.platform()},"claim_locks":{"chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","theory_established":"0%","RCG005_reclassified":False}}
    res["scientific_payload_sha256"]=sha(res);Path(a.output).write_text(json.dumps(res,indent=2,sort_keys=True)+"\n");print(json.dumps({k:res[k] for k in ("raw_counts","ALG_generator_dimension","DER_new_principal_dimension","generator_dimension_M","commutator_completion_all_in_ALG_span","classification")},sort_keys=True))
if __name__=="__main__":main()
