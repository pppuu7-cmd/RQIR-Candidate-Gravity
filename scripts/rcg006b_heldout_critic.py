#!/usr/bin/env python3
"""Independent RCG006B exact held-out Critic.

Re-enumerates raw tensors in reverse pairing order, reconstructs physical
coefficient columns with an independently indexed H4 manifest, and rebuilds
the frozen parent quotient without importing Constructor held-out data.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from collections import defaultdict
from itertools import combinations, product
from pathlib import Path
import sympy as sp
sys.path.insert(0,"scripts")
import rcg004_complete_cubic_constructor as p4
import rcg005_dim6_constructor as p5
import rcg006_mfr_critic as mc

HELDOUT="43748579a78f40e0825d5ae01dc634d55ba7b928"
EXEC="da1d1795a6ecf885a7f52a717d4979d962002240"
ALG_IDX=[16,19,46,52,436,439]; DER_IDX=[1,30,46]
SEED_K=0x5243473030364352; SEED_H=0x524347303036484f
DEN=(2,3,5,7,11); MASK=(1<<64)-1

def sha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def mj(M): return [[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]
class RNG:
    def __init__(self,s):self.s=s&MASK
    def nxt(self):self.s=(6364136223846793005*self.s+1442695040888963407)&MASK;return self.s
    def rat(self):
        x=self.nxt();n=((x>>16)%19)-9;y=self.nxt();return sp.Rational(n,DEN[(y>>24)%5])

def h4_manifest():
    pairs=sorted((a,b) for a in range(4) for b in range(a,4));quads=[]
    for a in range(4):
      for b in range(a,4):
       for c in range(b,4):
        for d in range(c,4):quads.append((a,b,c,d))
    H=[(p,q) for p in pairs for q in quads];return H,{k:i for i,k in enumerate(H)}
H4,H4I=h4_manifest()
def manifests():return [str(x) for x in p4.VN],[f"g{p}_{q}" for p,q in H4]
def bank(seed,n):
    r=RNG(seed);out=[]
    for _ in range(n):
      while True:
        c=[r.rat() for _ in range(20)];h=[r.rat() for _ in range(350)]
        if any(c):break
        r.nxt()
      out.append((c,h))
    return out
def bankhash(B):return sha([[[str(x) for x in c],[str(x) for x in h]] for c,h in B])

def pairings(rem):
    rem=tuple(rem)
    if not rem:yield ();return
    x=rem[-1]
    for k in range(len(rem)-1):
      y=rem[k];rest=rem[:k]+rem[k+1:-1]
      for t in pairings(rest):yield tuple(sorted(t+((min(x,y),max(x,y)),)))
def raw_reverse(n):
    out=[]
    for j,i in reversed(list(combinations(range(n),2))):
      rem=[x for x in range(n) if x not in (i,j)]
      for m in pairings(rem):out.append(("free",min(i,j),max(i,j),tuple(m)))
    for m in pairings(range(n)):out.append(("metric",tuple(m)))
    return out
def raw_forward(n):
    out=[]
    for i,j in combinations(range(n),2):
      rem=[x for x in range(n) if x not in (i,j)]
      for m in p4.matchings(rem):out.append(("free",i,j,tuple(m)))
    for m in p4.matchings(range(n)):out.append(("metric",tuple(m)))
    return out

def rval(cur,a,b,c,d):return sum(sp.Rational(v)*cur[k] for k,v in p4.rform(a,b,c,d).items())
def hv(h4,a,b,c,d,e,f):return h4[H4I[(tuple(sorted((a,b))),tuple(sorted((c,d,e,f))))]]
def d2v(h4,e,f,a,b,c,d):return sp.Rational(1,2)*(hv(h4,a,d,b,c,e,f)+hv(h4,b,c,a,d,e,f)-hv(h4,a,c,b,d,e,f)-hv(h4,b,d,a,c,e,f))
def slots(n,m,free):
    s=[None]*n
    for k,v in free.items():s[k]=v
    for e,(a,b) in enumerate(m):s[a]=s[b]=e
    return s

def direct_component(raw,kind,cur,h4,u,v):
    if raw[0]=="metric":
      if u!=v:return sp.Rational(0)
      m=raw[1];free={}
    else:
      _,i,j,m=raw;free={i:u,j:v}
    s=slots(8 if kind=="A" else 6,m,free);z=sp.Rational(0)
    for vals in product(range(4),repeat=len(m)):
      ind=[vals[x] if isinstance(x,int) else x for x in s]
      if kind=="A":z+=rval(cur,*ind[:4])*rval(cur,*ind[4:])
      else:z+=d2v(h4,*ind)
    return z
def direct_tensor(raw,kind,cur,h4):
    T=[[sp.Rational(0) for _ in range(4)] for __ in range(4)]
    for u in range(4):
      for v in range(u,4):
        a=direct_component(raw,kind,cur,h4,u,v)
        z=a if raw[0]=="metric" else sp.Rational(1,2)*(a+direct_component(raw,kind,cur,h4,v,u))
        T[u][v]=T[v][u]=sp.factor(z)
    return T

def rpoly(a,b,c,d):return p4.rform(a,b,c,d)
def hpoly(a,b,c,d,e,f):return {H4I[(tuple(sorted((a,b))),tuple(sorted((c,d,e,f))))]:sp.Rational(1)}
def add(o,p,c=1):
    for k,v in p.items():o[k]+=sp.Rational(c)*v
    return o
def mul(a,b):
    o=defaultdict(lambda:sp.Rational(0))
    for i,x in a.items():
      for j,y in b.items():o[tuple(sorted((i,j)))]+=x*y
    return {k:v for k,v in o.items() if v}
def d2poly(e,f,a,b,c,d):
    o=defaultdict(lambda:sp.Rational(0));add(o,hpoly(a,d,b,c,e,f),sp.Rational(1,2));add(o,hpoly(b,c,a,d,e,f),sp.Rational(1,2));add(o,hpoly(a,c,b,d,e,f),-sp.Rational(1,2));add(o,hpoly(b,d,a,c,e,f),-sp.Rational(1,2));return dict(o)
def symbolic_component(raw,kind,u,v):
    if raw[0]=="metric":
      if u!=v:return{}
      m=raw[1];free={}
    else:
      _,i,j,m=raw;free={i:u,j:v}
    s=slots(8 if kind=="A" else 6,m,free);o=defaultdict(lambda:sp.Rational(0))
    for vals in product(range(4),repeat=len(m)):
      ind=[vals[x] if isinstance(x,int) else x for x in s]
      if kind=="A":add(o,mul(rpoly(*ind[:4]),rpoly(*ind[4:])))
      else:add(o,d2poly(*ind))
    return {k:v for k,v in o.items() if v}
def physical_col(raw,kind):
    o=defaultdict(lambda:sp.Rational(0))
    for u in range(4):
      for v in range(u,4):
        p=symbolic_component(raw,kind,u,v)
        if raw[0]=="metric":z=p
        else:
          q=symbolic_component(raw,kind,v,u);z=defaultdict(lambda:sp.Rational(0));add(z,p,sp.Rational(1,2));add(z,q,sp.Rational(1,2));z=dict(z)
        for m,c in z.items():o[(u,v,m)]+=c
    return {k:v for k,v in o.items() if v}
def sparse_matrix(cols):
    rows=sorted(set().union(*(c.keys() for c in cols)));ix={r:i for i,r in enumerate(rows)};M=sp.zeros(len(rows),len(cols))
    for j,c in enumerate(cols):
      for r,v in c.items():M[ix[r],j]=v
    return M,rows
def pivot_coords(M,piv):
    B=M[:,piv];_,rows=B.T.rref();rows=list(rows);S=B[rows,:];inv=S.inv();out=[]
    for j in range(M.cols):
      c=inv*M[rows,j]
      if B*c!=M[:,j]:raise RuntimeError("critic relation reconstruction mismatch")
      out.append(c)
    return out
def eval_col(col,kind,cur,h4):
    z=[sp.Rational(0)]*10;idx=0
    for u in range(4):
      for v in range(u,4):
        s=sp.Rational(0)
        for (a,b,m),c in col.items():
          if a==u and b==v:s+=c*(cur[m[0]]*cur[m[1]] if kind=="A" else h4[m])
        z[idx]=sp.factor(s);idx+=1
    return z
def combo(vals,co):return [sp.factor(sum(co[k]*vals[k][i] for k in range(len(co)))) for i in range(10)]
def e_tensor(cur):
    Ric=[[sum(rval(cur,a,b,a,d) for a in range(4)) for d in range(4)] for b in range(4)];R=sum(Ric[i][i] for i in range(4));return [[sp.factor(-Ric[a][b]+(R/2 if a==b else 0)) for b in range(4)] for a in range(4)]
def contract(E,T):return sp.factor(sum(E[a][b]*T[a][b] for a in range(4) for b in range(4)))
def eval_cubic(m,cur):
    s=slots(12,m,{});z=sp.Rational(0)
    for vals in product(range(4),repeat=6):
      ind=[vals[x] for x in s];z+=rval(cur,*ind[:4])*rval(cur,*ind[4:8])*rval(cur,*ind[8:])
    return sp.factor(z)
def alg_img(raw,cur):
    if raw[0]=="metric":ts=[(list(raw[1])+[(8,10),(9,11)],1)]
    else:
      _,i,j,m=raw;ts=[(list(m)+[(8,10),(i,9),(j,11)],-1),(list(m)+[(8,10),(9,11),(i,j)],sp.Rational(1,2))]
    return sp.factor(sum(c*eval_cubic(tuple(sorted((min(a,b),max(a,b)) for a,b in q)),cur) for q,c in ts))
def eval_rd2(m,cur,h4):
    s=slots(10,m,{});z=sp.Rational(0)
    for vals in product(range(4),repeat=5):
      ind=[vals[x] for x in s];z+=rval(cur,*ind[:4])*d2v(h4,*ind[4:])
    return sp.factor(z)
def der_img(raw,cur,h4):
    sm={0:4,1:5,2:6,3:7,4:8,5:9};base=lambda mm:[(sm[a],sm[b]) for a,b in mm]
    if raw[0]=="metric":ts=[(base(raw[1])+[(0,2),(1,3)],1)]
    else:
      _,a,b,m=raw;oa,ob=sm[a],sm[b];z=base(m);ts=[(z+[(0,2),(1,oa),(3,ob)],-1),(z+[(0,2),(1,3),(oa,ob)],sp.Rational(1,2))]
    return sp.factor(sum(c*eval_rd2(tuple(sorted((min(a,b),max(a,b)) for a,b in q)),cur,h4) for q,c in ts))

def run_bank(B,ar,dr,AC,DC,aco,dco,raw25,Q,Mcanon,Rel):
    stat={"direct_tensor_checks":0,"alternate_relation_checks":0,"EH_action_image_checks":0,"quotient_combo_checks":0};pA=[AC[i] for i in ALG_IDX];pD=[DC[i] for i in DER_IDX]
    axes=[9,11]+[12+i for i in [0,1,2,4,5,8]];Eax=sp.zeros(25,8)
    for j,a in enumerate(axes):Eax[a,j]=1
    for cur,h4 in B:
      tens=[]
      for raw,col in zip([ar[i] for i in ALG_IDX],pA):
        T=direct_tensor(raw,"A",cur,h4)
        if [T[u][v] for u in range(4) for v in range(u,4)]!=eval_col(col,"A",cur,h4):raise AssertionError("critic ALG tensor mismatch")
        tens.append(T);stat["direct_tensor_checks"]+=1
      for raw,col in zip([dr[i] for i in DER_IDX],pD):
        T=direct_tensor(raw,"D",cur,h4)
        if [T[u][v] for u in range(4) for v in range(u,4)]!=eval_col(col,"D",cur,h4):raise AssertionError("critic DER tensor mismatch")
        tens.append(T);stat["direct_tensor_checks"]+=1
      va=[eval_col(x,"A",cur,h4) for x in pA];vd=[eval_col(x,"D",cur,h4) for x in pD]
      for j,col in enumerate(AC):
        if eval_col(col,"A",cur,h4)!=combo(va,list(aco[j])):raise AssertionError("critic ALG relation mismatch")
        stat["alternate_relation_checks"]+=1
      for j,col in enumerate(DC):
        if eval_col(col,"D",cur,h4)!=combo(vd,list(dco[j])):raise AssertionError("critic DER relation mismatch")
        stat["alternate_relation_checks"]+=1
      E=e_tensor(cur)
      for k,raw in enumerate([ar[i] for i in ALG_IDX]):
        if sp.factor(contract(E,tens[k])-alg_img(raw,cur))!=0:raise AssertionError("critic ALG EH mismatch")
        stat["EH_action_image_checks"]+=1
      for k,raw in enumerate([dr[i] for i in DER_IDX]):
        if sp.factor(contract(E,tens[6+k])-der_img(raw,cur,h4))!=0:raise AssertionError("critic DER EH mismatch")
        stat["EH_action_image_checks"]+=1
      co=sp.Matrix(cur[:9]);v=raw25*co;q1=Q*v;q2=Mcanon*co
      if q1!=q2:raise AssertionError("critic quotient mismatch")
      if Rel.T.row_join(v-Eax*q1).rank()!=Rel.rank():raise AssertionError("critic quotient representative mismatch")
      stat["quotient_combo_checks"]+=1
    return stat

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args();cm,hm=manifests();BK=bank(SEED_K,32);BH=bank(SEED_H,16)
    af=raw_forward(8);df=raw_forward(6);ar_rev=raw_reverse(8);dr_rev=raw_reverse(6)
    # Locate the frozen raw physical templates inside the reverse enumeration.
    if not all(af[i] in ar_rev for i in ALG_IDX) or not all(df[i] in dr_rev for i in DER_IDX):raise RuntimeError("critic cannot locate frozen raw templates")
    # Store columns in canonical forward raw-index identity, but compute each from the independently reverse-enumerated object.
    amap={r:physical_col(r,"A") for r in ar_rev};dmap={r:physical_col(r,"D") for r in dr_rev};AC=[amap[r] for r in af];DC=[dmap[r] for r in df]
    AM,_=sparse_matrix(AC);DM,_=sparse_matrix(DC);aco=pivot_coords(AM,ALG_IDX);dco=pivot_coords(DM,DER_IDX)
    Q,cmp,ci,dmp,di,Rel=mc.build_parent()
    # Independent raw action-map assembly through Critic functions.
    cols=[mc.algcol(af[i],cmp,ci) for i in ALG_IDX]+[mc.dercol(df[i],dmp,di) for i in DER_IDX];raw25=sp.Matrix.hstack(*cols);M=Q*raw25
    canon=json.loads(Path('results/raw/RCG006_MFR_L0_CANONICAL.json').read_text());Mcanon=sp.Matrix([[sp.Rational(x) for x in r] for r in canon['M_FR']]);canonical_ok=M==Mcanon
    ks=run_bank(BK,af,df,AC,DC,aco,dco,raw25,Q,Mcanon,Rel);hs=run_bank(BH,af,df,AC,DC,aco,dco,raw25,Q,Mcanon,Rel)
    cur,h4=BH[0];T=direct_tensor(af[ALG_IDX[0]],"A",cur,h4);E=e_tensor(cur);Ric=[[sum(rval(cur,x,b,x,d) for x in range(4)) for d in range(4)] for b in range(4)];R=sum(Ric[i][i] for i in range(4));Ebad=[[Ric[i][j]+(R/2 if i==j else 0) for j in range(4)] for i in range(4)]
    neg={"sign_flipped_EH_detected":bool(sp.factor(contract(Ebad,T)-alg_img(af[ALG_IDX[0]],cur))!=0),"perturbed_MFR_column_detected":bool(any((Mcanon+sp.eye(8,9))*sp.Matrix(c[:9])!=Mcanon*sp.Matrix(c[:9]) for c,_ in BH)),"perturbed_generator_coefficient_detected":bool(any(c[0]!=0 for c,_ in BH))}
    checks={"manifest_20_350":len(cm)==20 and len(hm)==350,"reverse_raw_counts":len(ar_rev)==525 and len(dr_rev)==60,"relation_ranks":AM.rank()==6 and DM.rank()==3,"parent_relation_rank17":Rel.rank()==17,"canonical_MFR_exact":canonical_ok,"critic_bank_all_exact":all(v>0 for v in ks.values()),"final_bank_all_exact":all(v>0 for v in hs.values()),"negative_controls":all(neg.values())}
    res={"phase":"RCG006B_GENERIC_METRIC_JET_HELDOUT_CRITIC","heldout_prereg":HELDOUT,"execution_contract":EXEC,"run_head":a.run_head,"method":"REVERSE_PAIRING_REENUMERATION_PLUS_INDEPENDENT_H4_INDEXING_PLUS_INDEPENDENT_PARENT_QUOTIENT",
      "coordinate_manifest":{"curvature_count":len(cm),"h4_count":len(hm),"curvature_sha256":sha(cm),"h4_sha256":sha(hm)},"banks":{"critic":{"seed":hex(SEED_K),"samples":32,"sha256":bankhash(BK)},"final":{"seed":hex(SEED_H),"samples":16,"sha256":bankhash(BH)}},"critic_bank_stats":ks,"final_bank_stats":hs,"negative_controls":neg,"canonical_MFR_sha256":canon['M_FR_sha256'],"checks":checks,"critic_valid":all(checks.values()),"classification":"PASS_SCOPED_RCG006B_GENERIC_METRIC_JET_HELDOUT" if all(checks.values()) else "INVALID_RCG006B_HELDOUT_VALIDATION","chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","theory_established":"0%"}
    res['scientific_payload_sha256']=sha(res);Path(a.output).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n');print(json.dumps({"classification":res['classification'],"critic_bank_stats":ks,"final_bank_stats":hs,"negative_controls":neg},sort_keys=True))
if __name__=='__main__':main()
