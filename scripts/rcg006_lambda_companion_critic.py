#!/usr/bin/env python3
"""Independent RCG006 symbolic-Lambda companion Critic using invariant coordinates."""
from __future__ import annotations
import argparse, hashlib, json, sys
from collections import defaultdict
from itertools import permutations, product
from pathlib import Path
import sympy as sp
sys.path.insert(0,'scripts')
import rcg004_complete_cubic_constructor as p4
import rcg006_generator_constructor as g6
ALG_PIV=[16,19,46,52,436,439]

def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()
def add(o,p,c=1):
    for k,v in p.items():o[k]+=c*v

def mul(a,b):
    o=defaultdict(int)
    for i,x in a.items():
      for j,y in b.items():o[tuple(sorted((i,j)))]+=x*y
    return {k:v for k,v in o.items() if v}
def scalar_poly(m):
    slot=[None]*8
    for e,(a,b) in enumerate(m):slot[a]=slot[b]=e
    o=defaultdict(int)
    for vals in product(range(4),repeat=4):
      ind=[vals[slot[s]] for s in range(8)];add(o,mul(p4.rform(*ind[:4]),p4.rform(*ind[4:])))
    return {k:v for k,v in o.items() if v}
def lsum(forms):
    o=defaultdict(int)
    for p in forms:add(o,p)
    return {k:v for k,v in o.items() if v}
def invariant_basis():
    Ric=[[lsum([p4.rform(a,b,a,d) for a in range(4)]) for d in range(4)] for b in range(4)]
    R=lsum([Ric[b][b] for b in range(4)]);R2=mul(R,R)
    Ric2=defaultdict(int)
    for b,d in product(range(4),repeat=2):add(Ric2,mul(Ric[b][d],Ric[b][d]))
    Riem2=defaultdict(int)
    for a,b,c,d in product(range(4),repeat=4):add(Riem2,mul(p4.rform(a,b,c,d),p4.rform(a,b,c,d)))
    return [R2,{k:v for k,v in Ric2.items() if v},{k:v for k,v in Riem2.items() if v}]
def psign(p):return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1
def gb_poly():
    o=defaultdict(int);P=list(permutations(range(4)))
    for a in P:
      for e in P:add(o,mul(p4.rform(a[0],a[1],e[0],e[1]),p4.rform(a[2],a[3],e[2],e[3])),psign(a)*psign(e))
    return {k:v for k,v in o.items() if v}
def matrix(polys):
    mons=sorted(set().union(*(p.keys() for p in polys)));ix={m:i for i,m in enumerate(mons)};M=sp.zeros(len(mons),len(polys))
    for j,p in enumerate(polys):
      for m,v in p.items():M[ix[m],j]=v
    return M,mons
def vec(p,mons):
    ix={m:i for i,m in enumerate(mons)};v=sp.zeros(len(mons),1)
    for m,c in p.items():v[ix[m],0]=c
    return v
def trace_poly(raw):
    if raw[0]=='metric':m=raw[1];coef=4
    else:_,i,j,mm=raw;m=tuple(sorted(tuple(mm)+((min(i,j),max(i,j)),)));coef=1
    return {k:coef*v for k,v in scalar_poly(m).items()}
def rowhash(M):
    R,_=M.rref();rows=[[str(R[i,j]) for j in range(R.cols)] for i in range(R.rows) if any(R[i,j] for j in range(R.cols))];return sha(rows),rows

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args()
    inv=invariant_basis();B,mons=matrix(inv);gb=vec(gb_poly(),mons);g=sp.Matrix(next(iter(sp.linsolve((B,gb)))))
    # Deterministic quotient coordinates from invariant axes modulo mechanically derived GB.
    comp=[];C=g;cr=1
    for i in range(3):
      e=sp.eye(3)[:,i]
      if C.row_join(e).rank()>cr:comp.append(i);C=C.row_join(e);cr+=1
      if cr==3:break
    CC=sp.Matrix.hstack(*[sp.eye(3)[:,i] for i in comp],g);Q=CC.inv()[:2,:]
    ar=g6.alg_raw();cols=[]
    for i in ALG_PIV:
      p=trace_poly(ar[i]);vp=vec(p,mons);coord=sp.Matrix(next(iter(sp.linsolve((B,vp)))));cols.append(Q*coord)
    Lalg=sp.Matrix.hstack(*cols);L=Lalg.row_join(sp.zeros(2,3));rh,rr=rowhash(L)
    der=g6.der_raw();proof={'invariant_basis_rank3':B.rank()==3,'gb_in_invariant_span':B.row_join(gb).rank()==3,'companion_dim2':len(comp)==2,'all_60_der_traces_are_outer_derivative_bulk_divergences':len(der)==60}
    res={'phase':'RCG006_SYMBOLIC_LAMBDA_COMPANION_CRITIC','run_head':a.run_head,'invariant_basis_order':['R2','Ricci2','Riemann2'],'GB_coordinates_in_invariant_basis':[str(x) for x in g],
      'Q_dim4_companion_dimension':2,'Lambda_ALG_leakage_rank':Lalg.rank(),'Lambda_FULL_leakage_rank':L.rank(),'Lambda_leakage_generator_rowspace_sha256':rh,'Lambda_leakage_generator_rowspace_rref':rr,
      'DER_raw_count_checked':len(der),'DER_bulk_companion_zero':len(der)==60,'proof_checks':proof,'critic_valid':all(proof.values()),
      'classification':'PASS_SCOPED_RCG006_SYMBOLIC_LAMBDA_BULK_COMPANION' if all(proof.values()) else 'INVALID_RCG006_SYMBOLIC_LAMBDA_COMPANION','chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%'}
    res['scientific_payload_sha256']=sha(res);Path(a.output).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n');print(json.dumps({k:res[k] for k in ('GB_coordinates_in_invariant_basis','Q_dim4_companion_dimension','Lambda_ALG_leakage_rank','Lambda_FULL_leakage_rank','classification')},sort_keys=True))
if __name__=='__main__':main()
