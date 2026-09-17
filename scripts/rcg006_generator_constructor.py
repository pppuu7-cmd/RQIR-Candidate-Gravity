#!/usr/bin/env python3
"""RCG006 pre-map Constructor: mechanically enumerate and exactly quotient the bounded local metric-redefinition generator class.

This phase deliberately computes no M_FR image/rank and no discriminator outcome.
"""
from __future__ import annotations
import argparse, hashlib, json, platform, sys
from collections import defaultdict
from itertools import combinations, product, permutations
from pathlib import Path
import sympy as sp
sys.path.insert(0,"scripts")
import rcg004_complete_cubic_constructor as p4

SELECTION="dc955720822d353d446186437ee2ca69458633bd"
PREREG="fc3ff1f49c56f2befc039e09ebd8f388833dbff1"
HELDOUT="43748579a78f40e0825d5ae01dc634d55ba7b928"
PARENT="aef9882924ffd128c6c30934e4f95394aae874fc"

def sha(o):
    return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()

def mmul(a,b):
    out=defaultdict(sp.Rational)
    for i,x in a.items():
        for j,y in b.items(): out[tuple(sorted((i,j)))]+=x*y
    return {k:sp.factor(v) for k,v in out.items() if v}

def padd(out,p,c=sp.Rational(1)):
    for k,v in p.items():
        out[k]+=c*v
        if not out[k]: del out[k]

def alg_raw():
    out=[]
    for i,j in combinations(range(8),2):
        rem=[x for x in range(8) if x not in (i,j)]
        for m in p4.matchings(rem): out.append(("free",i,j,tuple(m)))
    for m in p4.matchings(range(8)): out.append(("metric",tuple(m)))
    return out

def der_raw():
    out=[]
    for i,j in combinations(range(6),2):
        rem=[x for x in range(6) if x not in (i,j)]
        for m in p4.matchings(rem): out.append(("free",i,j,tuple(m)))
    for m in p4.matchings(range(6)): out.append(("metric",tuple(m)))
    return out

def edge_slot_values(nslots,matching,free_assign):
    slot=[None]*nslots
    for s,v in free_assign.items(): slot[s]=v
    for e,(a,b) in enumerate(matching): slot[a]=slot[b]=("E",e)
    return slot

def eval_alg_component(raw,u,v):
    kind=raw[0]
    if kind=="metric":
        if u!=v:return {}
        matching=raw[1]; free={}
    else:
        _,i,j,matching=raw;free={i:u,j:v}
    slot=edge_slot_values(8,matching,free)
    out=defaultdict(sp.Rational)
    for vals in product(range(4),repeat=len(matching)):
        ind=[vals[z[1]] if isinstance(z,tuple) else z for z in slot]
        a=p4.rform(*ind[:4]);b=p4.rform(*ind[4:])
        if a and b:padd(out,mmul(a,b))
    return dict(out)

def eval_alg(raw):
    out=defaultdict(sp.Rational)
    for u in range(4):
      for v in range(u,4):
        p=eval_alg_component(raw,u,v)
        q=eval_alg_component(raw,v,u) if raw[0]=="free" else p
        z=defaultdict(sp.Rational);padd(z,p);padd(z,q)
        for m,c in z.items():out[(u,v,m)]+=c
    return {k:v for k,v in out.items() if v}

def h4_index():
    pairs=list(combinations(range(4),2))+[(i,i) for i in range(4)]
    pairs=sorted(tuple(sorted(p)) for p in pairs)
    quads=[]
    for a in range(4):
      for b in range(a,4):
       for c in range(b,4):
        for d in range(c,4):quads.append((a,b,c,d))
    keys=[(p,q) for p in pairs for q in quads]
    return {k:i for i,k in enumerate(keys)},keys
H4I,H4K=h4_index()
def h4(a,b,c,d,e,f):
    key=(tuple(sorted((a,b))),tuple(sorted((c,d,e,f))))
    return {H4I[key]:sp.Rational(1)}
def ladd(*terms):
    o=defaultdict(sp.Rational)
    for coef,p in terms:padd(o,p,coef)
    return dict(o)
def d2r_principal(e,f,a,b,c,d):
    # Normal-coordinate principal part: 1/2(g_ad,bcef+g_bc,adef-g_ac,bdef-g_bd,acef)
    return ladd((sp.Rational(1,2),h4(a,d,b,c,e,f)),(sp.Rational(1,2),h4(b,c,a,d,e,f)),(-sp.Rational(1,2),h4(a,c,b,d,e,f)),(-sp.Rational(1,2),h4(b,d,a,c,e,f)))

def eval_der_component(raw,u,v):
    kind=raw[0]
    if kind=="metric":
        if u!=v:return {}
        matching=raw[1];free={}
    else:
        _,i,j,matching=raw;free={i:u,j:v}
    slot=edge_slot_values(6,matching,free)
    out=defaultdict(sp.Rational)
    for vals in product(range(4),repeat=len(matching)):
        ind=[vals[z[1]] if isinstance(z,tuple) else z for z in slot]
        padd(out,d2r_principal(*ind))
    return dict(out)
def eval_der(raw):
    out=defaultdict(sp.Rational)
    for u in range(4):
      for v in range(u,4):
        p=eval_der_component(raw,u,v);q=eval_der_component(raw,v,u) if raw[0]=="free" else p
        z=defaultdict(sp.Rational);padd(z,p);padd(z,q)
        for k,c in z.items():out[(u,v,k)]+=c
    return {k:v for k,v in out.items() if v}

def sparse_matrix(cols):
    rows=sorted(set().union(*(c.keys() for c in cols)));ri={r:i for i,r in enumerate(rows)}
    M=sp.MutableSparseMatrix(len(rows),len(cols),{})
    for j,c in enumerate(cols):
      for r,v in c.items():M[ri[r],j]=v
    return M,rows

def raw_matching(raw,n,out0,out1):
    if raw[0]=="metric":m=list(raw[1])+[(out0,out1)]
    else:
        _,i,j,mm=raw;m=list(mm)+[(i,out0),(j,out1)]
    return tuple(sorted((min(a,b),max(a,b)) for a,b in m))
def canon_output(m,out0,out1):
    pa=next(a if b==out0 else b for a,b in m if out0 in (a,b) and out1 not in (a,b)) if (out0,out1) not in m else None
    pb=next(a if b==out1 else b for a,b in m if out1 in (a,b) and out0 not in (a,b)) if (out0,out1) not in m else None
    if pa is not None and pa>pb:
        def f(x):return out1 if x==out0 else out0 if x==out1 else x
        m=tuple(sorted((min(f(a),f(b)),max(f(a),f(b))) for a,b in m))
    return m

def local_on(slots):
    out=[]
    base=slots[0]
    for p,s in p4.local_group(0):
        out.append(({slots[i]:slots[p[i]] for i in range(4)},s))
    return out

def alg_group():
    L=local_on([0,1,2,3]);R=local_on([4,5,6,7]);out=[]
    for swap in (0,1):
      for p,s in L:
       for q,t in R:
        P={**p,**q}
        if swap:
            P={k:(v+4 if v<4 else v-4) for k,v in P.items()}
        out.append((P,s*t))
    return out
def der_group():return local_on([2,3,4,5])
def tmatch(m,P):
    def f(x):return P.get(x,x)
    return tuple(sorted((min(f(a),f(b)),max(f(a),f(b))) for a,b in m))
def symmetry_classes(raws,n,out0,out1,G):
    enc={raw_matching(r,n,out0,out1):i for i,r in enumerate(raws)};unseen=set(enc);nz=[];zz=[]
    while unseen:
        m=min(unseen);d=defaultdict(set)
        for P,s in G:
            q=canon_output(tmatch(m,P),out0,out1);d[q].add(s)
        unseen-=set(d);rep=min(d);(zz if any(len(x)>1 for x in d.values()) else nz).append(rep)
    return sorted(nz),sorted(zz)

def comm_form(e,f,a,b,c,d):
    # [nabla_e,nabla_f]R_abcd for all-lower R, Euclidean point convention; sign is frozen and later independently controlled.
    o=defaultdict(sp.Rational)
    for p in range(4):
        terms=[mmul(p4.rform(p,a,e,f),p4.rform(p,b,c,d)),mmul(p4.rform(p,b,e,f),p4.rform(a,p,c,d)),mmul(p4.rform(p,c,e,f),p4.rform(a,b,p,d)),mmul(p4.rform(p,d,e,f),p4.rform(a,b,c,p))]
        for z in terms:padd(o,z,-1)
    return dict(o)
def eval_comm_component(raw,u,v):
    if raw[0]=="metric":
        if u!=v:return {}
        matching=raw[1];free={}
    else:
        _,i,j,matching=raw;free={i:u,j:v}
    slot=edge_slot_values(6,matching,free);out=defaultdict(sp.Rational)
    for vals in product(range(4),repeat=len(matching)):
        ind=[vals[z[1]] if isinstance(z,tuple) else z for z in slot];padd(out,comm_form(*ind))
    return dict(out)
def eval_comm(raw):
    out=defaultdict(sp.Rational)
    for u in range(4):
      for v in range(u,4):
        p=eval_comm_component(raw,u,v);q=eval_comm_component(raw,v,u) if raw[0]=="free" else p
        z=defaultdict(sp.Rational);padd(z,p);padd(z,q)
        for m,c in z.items():out[(u,v,m)]+=c
    return {k:v for k,v in out.items() if v}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",required=True);ap.add_argument("--run-head",default="");args=ap.parse_args()
    ar=alg_raw();dr=der_raw();acols=[eval_alg(r) for r in ar];dcols=[eval_der(r) for r in dr];AM,arows=sparse_matrix(acols);DM,drows=sparse_matrix(dcols)
    arank=AM.rank();drank=DM.rank();_,apiv=AM.rref();_,dpiv=DM.rref()
    anz,azz=symmetry_classes(ar,8,8,9,alg_group());dnz,dzz=symmetry_classes(dr,6,6,7,der_group())
    # exact commutator-completion control: every ordered-derivative commutator tensor lies in ALG universal span.
    AB=AM[:,list(apiv)];comm_ok=True;comm_coords=[]
    ari={r:i for i,r in enumerate(arows)}
    for r in dr:
        cp=eval_comm(r);v=sp.zeros(len(arows),1)
        extra=False
        for k,c in cp.items():
            if k not in ari: extra=True;break
            v[ari[k],0]=c
        if extra:
            comm_ok=False;comm_coords.append([]);continue
        sol=sp.linsolve((AB,v))
        if sol is sp.EmptySet or not sol:
            comm_ok=False;comm_coords.append([])
        else:
            tup=next(iter(sol));comm_coords.append([str(x) for x in tup])
    result={
      "phase":"RCG006_GENERATOR_COMPLETENESS_PREMAP",
      "selection_terminal":SELECTION,"scientific_prereg":PREREG,"heldout_prereg":HELDOUT,"parent_rcg005_terminal":PARENT,"run_head":args.run_head,
      "no_M_FR_computed":True,"no_field_redefinition_image_rank_computed":True,"no_discriminator_outcome_computed":True,
      "generator_partitions":["ALG_RIEMANN2","DER_NABLA2_RIEMANN"],
      "raw_counts":{"ALG":len(ar),"DER":len(dr),"total":len(ar)+len(dr)},
      "raw_manifest_sha256":{"ALG":sha(ar),"DER":sha(dr)},
      "symmetry_classes":{"ALG_nonzero":len(anz),"ALG_zero":len(azz),"DER_ordered_nonzero":len(dnz),"DER_ordered_zero":len(dzz)},
      "universal_ALG_matrix_shape":list(AM.shape),"universal_ALG_matrix_sha256":sha([[str(AM[i,j]) for j in range(AM.cols)] for i in range(AM.rows)]),"ALG_generator_dimension":arank,"ALG_pivot_raw_indices":list(apiv),
      "normal_coordinate_h4_variable_count":len(H4K),"universal_DER_principal_matrix_shape":list(DM.shape),"universal_DER_principal_matrix_sha256":sha([[str(DM[i,j]) for j in range(DM.cols)] for i in range(DM.rows)]),"DER_new_principal_dimension":drank,"DER_pivot_raw_indices":list(dpiv),
      "commutator_completion_all_in_ALG_span":bool(comm_ok),"commutator_completion_coordinates_sha256":sha(comm_coords),
      "generator_dimension_M":arank+drank,
      "deterministic_generator_basis":{"ALG_raw_indices":list(apiv),"DER_raw_indices":list(dpiv)},
      "filtered_completion_statement":"ALG exact universal tensor quotient direct-summed with DER principal quotient; all derivative-order antisymmetry remainders lie in ALG by exact commutator completion.",
      "classification":"PASS_RCG006_GENERATOR_COMPLETENESS_READY_TO_FREEZE" if comm_ok else "INVALID_RCG006_GENERATOR_COMPLETENESS",
      "environment":{"python":sys.version.split()[0],"sympy":sp.__version__,"platform":platform.platform()},
      "claim_locks":{"chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","theory_established":"0%","RCG005_reclassified":False}
    }
    result["scientific_payload_sha256"]=sha(result);Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:result[k] for k in ("raw_counts","ALG_generator_dimension","DER_new_principal_dimension","generator_dimension_M","commutator_completion_all_in_ALG_span","classification")},sort_keys=True))
if __name__=="__main__":main()
