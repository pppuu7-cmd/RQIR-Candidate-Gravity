#!/usr/bin/env python3
"""Independent RCG006 L0 M_FR Critic reconstruction.

Uses reverse raw ordering and independently assembles the EH contraction columns;
compares only invariant rank/span data downstream in the aggregate.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
import sympy as sp
sys.path.insert(0,"scripts")
import rcg004_complete_cubic_constructor as p4
import rcg005_dim6_constructor as p5
import rcg006_generator_constructor as g6

PREREG="fc3ff1f49c56f2befc039e09ebd8f388833dbff1"
GEN_FREEZE="8c8314d2b857d6caa9719d6ba33e856ea0a697af"
MAP_CONTRACT="78789e048ab3d67fc8f2e901176ff3a352aad749"
REL_HASH="4b6f9b9713b076a10513adb1b10ab0bfc91b822acda441f976aee2f14a5fd38e"
ALG=[16,19,46,52,436,439]; DER=[1,30,46]; PB=[0,1,2,4,5,8]

def sha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def matj(M): return [[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]

def build_parent():
    cub=list(p4.matchings(range(12))); creps,_,cmp=p5.classes(cub,p4.symmetry_group()); ci={m:i for i,m in enumerate(creps)}
    CU,_=p4.universal_matrix([p4.universal_poly(m) for m in creps])
    d1=list(p4.matchings(range(10))); dreps,_,dmp=p5.classes(d1,p5.d1group()); di={m:i for i,m in enumerate(dreps)}
    _,TB=p5.derivative_basis(); DU=p5.d1matrix(dreps,TB)
    cm=p5.commrels(d1,dmp,di,cmp,ci,len(dreps),len(creps))
    rows=[]
    for v in DU.nullspace(): rows.append(list(v)+[sp.Rational(0)]*len(creps))
    for v in CU.nullspace(): rows.append([sp.Rational(0)]*len(dreps)+list(v))
    rows += [[sp.Rational(x) for x in r] for r in cm]
    Rel=sp.Matrix(rows); R,_=Rel.rref(); rr=[list(R.row(i)) for i in range(R.rows) if any(R.row(i))]
    axes=[9,11]+[12+i for i in PB]; E=sp.zeros(25,8)
    for j,a in enumerate(axes): E[a,j]=1
    C=E.row_join(sp.Matrix(rr).T)
    if Rel.rank()!=17 or p5.rrhash(Rel)!=REL_HASH or C.rank()!=25: raise RuntimeError("parent mismatch")
    return C.inv()[:8,:],cmp,ci,dmp,di,Rel

def put(v,off,mp,idx,pairs,c):
    m=tuple(sorted((min(a,b),max(a,b)) for a,b in pairs)); rep,s=mp[m]
    if rep is not None: v[off+idx[rep],0]+=sp.Rational(c)*s

def algcol(raw,cmp,ci):
    v=sp.zeros(25,1)
    if raw[0]=="metric": put(v,12,cmp,ci,list(raw[1])+[(8,10),(9,11)],1)
    else:
        _,a,b,m=raw
        put(v,12,cmp,ci,list(m)+[(8,10),(a,9),(b,11)],-1)
        put(v,12,cmp,ci,list(m)+[(8,10),(9,11),(a,b)],sp.Rational(1,2))
    return v

def dercol(raw,dmp,di):
    sm={0:4,1:5,2:6,3:7,4:8,5:9}; v=sp.zeros(25,1)
    base=lambda mm:[(sm[a],sm[b]) for a,b in mm]
    terms=[]
    if raw[0]=="metric": terms=[(base(raw[1])+[(0,2),(1,3)],1)]
    else:
        _,a,b,m=raw; oa,ob=sm[a],sm[b]; z=base(m)
        terms=[(z+[(0,2),(1,oa),(3,ob)],-1),(z+[(0,2),(1,3),(oa,ob)],sp.Rational(1,2))]
    for pairs,c in terms:
        mm=tuple(sorted((min(a,b),max(a,b)) for a,b in pairs))
        put(v,0,dmp,di,p5.ibp(mm),-c)
    return v

def rref_span(M):
    R,_=M.T.rref(); return [[str(R[i,j]) for j in range(R.cols)] for i in range(R.rows) if any(R.row(i))]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--run-head',default=''); a=ap.parse_args()
    Q,cmp,ci,dmp,di,Rel=build_parent(); ar=g6.alg_raw(); dr=g6.der_raw()
    # Reverse processing order is intentional; restore frozen production order only at final assembly.
    amap={i:algcol(ar[i],cmp,ci) for i in reversed(ALG)}; dmap={i:dercol(dr[i],dmp,di) for i in reversed(DER)}
    raw=sp.Matrix.hstack(*[amap[i] for i in ALG],*[dmap[i] for i in DER]); M=Q*raw
    rk=M.rank(); arank=M[:,:6].rank(); span=rref_span(M)
    cubic=sp.zeros(8,6)
    for j,i in enumerate(range(2,8)): cubic[i,j]=1
    inter=rk+6-M.row_join(cubic).rank()
    res={"phase":"RCG006_MFR_L0_CRITIC_PROGRESS","scientific_prereg":PREREG,"generator_freeze":GEN_FREEZE,"map_contract":MAP_CONTRACT,"run_head":a.run_head,
         "parent_relation_rank":Rel.rank(),"parent_relation_rref_sha256":p5.rrhash(Rel),"M_FR_shape":list(M.shape),"M_FR_sha256":sha(matj(M)),
         "rank_M_ALG":arank,"rank_M_FULL":rk,"kernel_dimension":9-rk,"Q_EFT_dimension":8-rk,"RCG004_intersection_dimension":inter,
         "image_rref_rows":span,"image_span_sha256":sha(span),"chi_ABC":"UNAUTHORIZED_NOT_COMPUTED",
         "critic_valid":Rel.rank()==17 and p5.rrhash(Rel)==REL_HASH and M.shape==(8,9),
         "classification":"RCG006_MFR_L0_CRITIC_PROGRESS_VALID"}
    if not res['critic_valid']: res['classification']="INVALID_RCG006_MFR_L0_CRITIC_PROGRESS"
    res['scientific_payload_sha256']=sha(res); Path(a.output).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:res[k] for k in ('rank_M_ALG','rank_M_FULL','Q_EFT_dimension','RCG004_intersection_dimension','classification')},sort_keys=True))
if __name__=='__main__': main()
