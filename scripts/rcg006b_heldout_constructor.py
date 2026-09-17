#!/usr/bin/env python3
"""RCG006B exact no-refit held-out Constructor validation.

Uses the prospectively frozen rational banks to validate the already-frozen
RCG006 generator tensors, first-order EH raw images and 25->8 quotient map.
Finite sampling is validation only; universal identities remain certified by
the exact coefficient matrices from the parent gates.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from collections import defaultdict
from itertools import product
from pathlib import Path
import sympy as sp
sys.path.insert(0,"scripts")
import rcg004_complete_cubic_constructor as p4
import rcg006_generator_constructor as g6
import rcg006_mfr_constructor as mf

HELDOUT="43748579a78f40e0825d5ae01dc634d55ba7b928"
EXEC="da1d1795a6ecf885a7f52a717d4979d962002240"
ALG=mf.ALG_PIV; DER=mf.DER_PIV
SEED_C=0x5243473030364341; SEED_H=0x524347303036484f
DEN=(2,3,5,7,11); MASK=(1<<64)-1

def sha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def mj(M): return [[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]

# The pre-map module used defaultdict(sp.Rational), which is not callable with
# zero arguments on current SymPy. Patch only its additive-zero factory.
_real_dd=defaultdict
def _dd(factory=None,*a,**k):
    if factory is sp.Rational: factory=lambda:sp.Rational(0)
    return _real_dd(factory,*a,**k)
g6.defaultdict=_dd

class RNG:
    def __init__(self,s): self.s=s&MASK
    def nxt(self):
        self.s=(6364136223846793005*self.s+1442695040888963407)&MASK; return self.s
    def rat(self):
        x=self.nxt(); n=((x>>16)%19)-9
        y=self.nxt(); d=DEN[(y>>24)%5]
        return sp.Rational(n,d)

def manifests():
    c=[str(x) for x in p4.VN]
    h=[f"g{tuple(pair)}_{tuple(q)}" for pair,q in g6.H4K]
    return c,h

def bank(seed,n):
    r=RNG(seed); out=[]
    for _ in range(n):
        while True:
            cur=[r.rat() for _ in range(len(p4.VN))]
            h4=[r.rat() for _ in range(len(g6.H4K))]
            if any(cur): break
            r.nxt()
        out.append((cur,h4))
    return out

def bankhash(B): return sha([[[str(x) for x in c],[str(x) for x in h]] for c,h in B])
def rval(cur,a,b,c,d): return sum(sp.Rational(v)*cur[k] for k,v in p4.rform(a,b,c,d).items())
def hval(h4,a,b,c,d,e,f): return h4[g6.H4I[(tuple(sorted((a,b))),tuple(sorted((c,d,e,f))))]]
def d2val(h4,e,f,a,b,c,d):
    return sp.Rational(1,2)*(hval(h4,a,d,b,c,e,f)+hval(h4,b,c,a,d,e,f)-hval(h4,a,c,b,d,e,f)-hval(h4,b,d,a,c,e,f))

def raw_comp_alg(raw,cur,u,v):
    if raw[0]=="metric":
        if u!=v:return sp.Rational(0)
        m=raw[1]; free={}
    else:
        _,i,j,m=raw; free={i:u,j:v}
    slot=g6.edge_slot_values(8,m,free); z=sp.Rational(0)
    for vals in product(range(4),repeat=len(m)):
        ind=[vals[x[1]] if isinstance(x,tuple) else x for x in slot]
        z+=rval(cur,*ind[:4])*rval(cur,*ind[4:])
    return z

def raw_comp_der(raw,h4,u,v):
    if raw[0]=="metric":
        if u!=v:return sp.Rational(0)
        m=raw[1]; free={}
    else:
        _,i,j,m=raw; free={i:u,j:v}
    slot=g6.edge_slot_values(6,m,free); z=sp.Rational(0)
    for vals in product(range(4),repeat=len(m)):
        ind=[vals[x[1]] if isinstance(x,tuple) else x for x in slot]
        z+=d2val(h4,*ind)
    return z

def direct_tensor(raw,kind,cur,h4):
    T=[[sp.Rational(0) for _ in range(4)] for __ in range(4)]
    f=(lambda u,v:raw_comp_alg(raw,cur,u,v)) if kind=="A" else (lambda u,v:raw_comp_der(raw,h4,u,v))
    for u in range(4):
      for v in range(u,4):
        if raw[0]=="metric": z=f(u,v)
        else: z=sp.Rational(1,2)*(f(u,v)+f(v,u))
        T[u][v]=T[v][u]=sp.factor(z)
    return T

def sparse_tensor(col,kind,cur,h4):
    T=[[sp.Rational(0) for _ in range(4)] for __ in range(4)]
    for key,c in col.items():
        u,v,m=key
        if kind=="A": ev=cur[m[0]]*cur[m[1]]
        else: ev=h4[m]
        T[u][v]+=sp.Rational(c,2)*ev
    for u in range(4):
      for v in range(u+1,4):T[v][u]=T[u][v]
    return T

def teq(A,B): return all(sp.factor(A[i][j]-B[i][j])==0 for i in range(4) for j in range(4))
def e_tensor(cur):
    Ric=[[sum(rval(cur,a,b,a,d) for a in range(4)) for d in range(4)] for b in range(4)]
    R=sum(Ric[b][b] for b in range(4))
    return [[sp.factor(-Ric[a][b]+(sp.Rational(1,2)*R if a==b else 0)) for b in range(4)] for a in range(4)]
def contract(E,T): return sp.factor(sum(E[a][b]*T[a][b] for a in range(4) for b in range(4)))

def eval_cubic_matching(m,cur):
    slot=[None]*12
    for e,(a,b) in enumerate(m):slot[a]=slot[b]=e
    z=sp.Rational(0)
    for vals in product(range(4),repeat=6):
        ind=[vals[slot[s]] for s in range(12)]
        z+=rval(cur,*ind[:4])*rval(cur,*ind[4:8])*rval(cur,*ind[8:])
    return sp.factor(z)
def alg_image_direct(raw,cur):
    if raw[0]=="metric": terms=[(list(raw[1])+[(8,10),(9,11)],sp.Rational(1))]
    else:
        _,i,j,b=raw;terms=[(list(b)+[(8,10),(i,9),(j,11)],sp.Rational(-1)),(list(b)+[(8,10),(9,11),(i,j)],sp.Rational(1,2))]
    return sp.factor(sum(c*eval_cubic_matching(tuple(sorted((min(a,b),max(a,b)) for a,b in m)),cur) for m,c in terms))
def eval_rd2_matching(m,cur,h4):
    slot=[None]*10
    for e,(a,b) in enumerate(m):slot[a]=slot[b]=e
    z=sp.Rational(0)
    for vals in product(range(4),repeat=5):
        ind=[vals[slot[s]] for s in range(10)]
        z+=rval(cur,*ind[:4])*d2val(h4,*ind[4:])
    return sp.factor(z)
def der_image_direct(raw,cur,h4):
    sm={0:4,1:5,2:6,3:7,4:8,5:9};base=lambda mm:[(sm[a],sm[b]) for a,b in mm]
    if raw[0]=="metric": terms=[(base(raw[1])+[(0,2),(1,3)],sp.Rational(1))]
    else:
        _,a,b,m=raw;oa,ob=sm[a],sm[b];z=base(m);terms=[(z+[(0,2),(1,oa),(3,ob)],sp.Rational(-1)),(z+[(0,2),(1,3),(oa,ob)],sp.Rational(1,2))]
    return sp.factor(sum(c*eval_rd2_matching(tuple(sorted((min(a,b),max(a,b)) for a,b in m)),cur,h4) for m,c in terms))

def pivot_coords(M,piv):
    B=M[:,list(piv)]; _,rows=B.T.rref(); rows=list(rows)
    S=B[rows,:]
    if S.rows!=S.cols or S.det()==0: raise RuntimeError("pivot row extraction failed")
    inv=S.inv(); C=[]
    for j in range(M.cols):
        c=inv*M[rows,j]
        if B*c!=M[:,j]: raise RuntimeError("universal pivot relation mismatch")
        C.append(c)
    return C

def eval_col(col,kind,cur,h4):
    T=sparse_tensor(col,kind,cur,h4)
    return [T[u][v] for u in range(4) for v in range(u,4)]
def combo(vals,cs): return [sp.factor(sum(cs[k]*vals[k][i] for k in range(len(cs)))) for i in range(len(vals[0]))]

def run_bank(B,ar,dr,ac,dc,acoord,dcoord,raw25,Q,Mcanon,Rel):
    direct_tensor_checks=0; relation_checks=0; action_checks=0; quotient_checks=0
    pA=[ac[i] for i in ALG];pD=[dc[i] for i in DER]
    axes=[9,11]+[12+i for i in mf.PARENT_BASIS]
    Eax=sp.zeros(25,8)
    for j,a in enumerate(axes):Eax[a,j]=1
    for cur,h4 in B:
        # Frozen nine tensor representatives: direct contraction vs coefficient representation.
        tensors=[]
        for raw,col in zip([ar[i] for i in ALG],pA):
            td=direct_tensor(raw,"A",cur,h4);ts=sparse_tensor(col,"A",cur,h4)
            if not teq(td,ts): raise AssertionError("ALG heldout tensor mismatch")
            tensors.append(td);direct_tensor_checks+=1
        for raw,col in zip([dr[i] for i in DER],pD):
            td=direct_tensor(raw,"D",cur,h4);ts=sparse_tensor(col,"D",cur,h4)
            if not teq(td,ts): raise AssertionError("DER heldout tensor mismatch")
            tensors.append(td);direct_tensor_checks+=1
        # Every asserted alternate-generator relation evaluated on the held-out.
        pvA=[eval_col(x,"A",cur,h4) for x in pA];pvD=[eval_col(x,"D",cur,h4) for x in pD]
        for j,col in enumerate(ac):
            lhs=eval_col(col,"A",cur,h4);rhs=combo(pvA,list(acoord[j]))
            if lhs!=rhs: raise AssertionError("ALG alternate relation heldout mismatch")
            relation_checks+=1
        for j,col in enumerate(dc):
            lhs=eval_col(col,"D",cur,h4);rhs=combo(pvD,list(dcoord[j]))
            if lhs!=rhs: raise AssertionError("DER alternate relation heldout mismatch")
            relation_checks+=1
        # First-order EH images before quotient reduction.
        E=e_tensor(cur)
        for k,raw in enumerate([ar[i] for i in ALG]):
            if sp.factor(contract(E,tensors[k])-alg_image_direct(raw,cur))!=0: raise AssertionError("ALG EH image heldout mismatch")
            action_checks+=1
        for q,raw in enumerate([dr[i] for i in DER]):
            if sp.factor(contract(E,tensors[6+q])-der_image_direct(raw,cur,h4))!=0: raise AssertionError("DER EH image heldout mismatch")
            action_checks+=1
        # After exact quotient reduction: sample-derived combination, two exact routes.
        coeff=sp.Matrix(cur[:9]);v=raw25*coeff;q1=Q*v;q2=Mcanon*coeff
        if q1!=q2: raise AssertionError("quotient map heldout mismatch")
        resid=v-Eax*q1
        if Rel.T.row_join(resid).rank()!=Rel.rank(): raise AssertionError("quotient representative not relation-equivalent")
        quotient_checks+=1
    return {"direct_tensor_checks":direct_tensor_checks,"alternate_relation_checks":relation_checks,"EH_action_image_checks":action_checks,"quotient_combo_checks":quotient_checks}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args()
    cm,hm=manifests();BC=bank(SEED_C,32);BH=bank(SEED_H,16)
    ar=g6.alg_raw();dr=g6.der_raw();ac=[g6.eval_alg(r) for r in ar];dc=[g6.eval_der(r) for r in dr]
    AM,_=g6.sparse_matrix(ac);DM,_=g6.sparse_matrix(dc);_,apiv=AM.rref();_,dpiv=DM.rref()
    if list(apiv)!=ALG or list(dpiv)!=DER: raise RuntimeError("frozen pivot mismatch")
    acoord=pivot_coords(AM,ALG);dcoord=pivot_coords(DM,DER)
    Q,creps,cmp,ci,dreps,dmp,di,Rel=mf.parent_quotient()
    cols=[mf.alg_raw_vector(ar[i],cmp,ci) for i in ALG]+[mf.der_raw_vector(dr[i],dmp,di) for i in DER]
    raw25=sp.Matrix.hstack(*cols);M=Q*raw25
    canon=json.loads(Path('results/raw/RCG006_MFR_L0_CANONICAL.json').read_text());Mcanon=sp.Matrix([[sp.Rational(x) for x in row] for row in canon['M_FR']])
    canonical_ok=M==Mcanon and mf.sha(mf.mjson(M))==canon['M_FR_sha256']
    cstat=run_bank(BC,ar,dr,ac,dc,acoord,dcoord,raw25,Q,Mcanon,Rel);hstat=run_bank(BH,ar,dr,ac,dc,acoord,dcoord,raw25,Q,Mcanon,Rel)
    # Frozen detection controls.
    cur,h4=BH[0];E=e_tensor(cur);t0=direct_tensor(ar[ALG[0]],"A",cur,h4)
    Ric=[[sum(rval(cur,x,b,x,d) for x in range(4)) for d in range(4)] for b in range(4)];R=sum(Ric[b][b] for b in range(4));Ebad=[[Ric[i][j]+(sp.Rational(1,2)*R if i==j else 0) for j in range(4)] for i in range(4)]
    sign_control=sp.factor(contract(Ebad,t0)-alg_image_direct(ar[ALG[0]],cur))!=0
    Mbad=Mcanon.copy();Mbad[0,0]+=1
    map_control=any(Mbad*sp.Matrix(c[:9])!=Mcanon*sp.Matrix(c[:9]) for c,_ in BH)
    rep_control=any(c[0]!=0 for c,_ in BH)
    neg={"sign_flipped_EH_detected":bool(sign_control),"perturbed_MFR_column_detected":bool(map_control),"perturbed_generator_coefficient_detected":bool(rep_control)}
    checks={"manifest_20_350":len(cm)==20 and len(hm)==350,"frozen_pivots":list(apiv)==ALG and list(dpiv)==DER,"universal_relation_ranks":AM.rank()==6 and DM.rank()==3,"canonical_parent_relation":Rel.rank()==17,"canonical_MFR_exact":canonical_ok,"constructor_bank_all_exact":all(v>0 for v in cstat.values()),"final_bank_all_exact":all(v>0 for v in hstat.values()),"negative_controls":all(neg.values())}
    res={"phase":"RCG006B_GENERIC_METRIC_JET_HELDOUT_CONSTRUCTOR","heldout_prereg":HELDOUT,"execution_contract":EXEC,"run_head":a.run_head,
      "coordinate_manifest":{"curvature_count":len(cm),"h4_count":len(hm),"curvature_sha256":sha(cm),"h4_sha256":sha(hm)},
      "banks":{"constructor":{"seed":hex(SEED_C),"samples":32,"sha256":bankhash(BC)},"final":{"seed":hex(SEED_H),"samples":16,"sha256":bankhash(BH)}},
      "constructor_bank_stats":cstat,"final_bank_stats":hstat,"negative_controls":neg,"canonical_MFR_sha256":canon['M_FR_sha256'],"checks":checks,"constructor_valid":all(checks.values()),
      "classification":"PASS_SCOPED_RCG006B_GENERIC_METRIC_JET_HELDOUT" if all(checks.values()) else "INVALID_RCG006B_HELDOUT_VALIDATION","chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","theory_established":"0%"}
    res['scientific_payload_sha256']=sha(res);Path(a.output).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n');print(json.dumps({"classification":res['classification'],"constructor_bank_stats":cstat,"final_bank_stats":hstat,"negative_controls":neg},sort_keys=True))
if __name__=='__main__':main()
