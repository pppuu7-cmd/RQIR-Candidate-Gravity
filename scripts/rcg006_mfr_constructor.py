#!/usr/bin/env python3
"""RCG006 frozen L0 first-order EH field-redefinition map Constructor.

Executes the already-preregistered map contract after the nine-dimensional
generator-space freeze. This is a bounded map subgate, not the terminal RCG006 audit.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
import sympy as sp
sys.path.insert(0, "scripts")
import rcg004_complete_cubic_constructor as p4
import rcg005_dim6_constructor as p5
import rcg006_generator_constructor as g6

PREREG="fc3ff1f49c56f2befc039e09ebd8f388833dbff1"
GEN_FREEZE="8c8314d2b857d6caa9719d6ba33e856ea0a697af"
MAP_CONTRACT="78789e048ab3d67fc8f2e901176ff3a352aad749"
PARENT_FREEZE="f4d6f11490c0e668aa934e25580abad3015f0ae1"
REL_HASH="4b6f9b9713b076a10513adb1b10ab0bfc91b822acda441f976aee2f14a5fd38e"
ALG_PIV=[16,19,46,52,436,439]
DER_PIV=[1,30,46]
PARENT_BASIS=[0,1,2,4,5,8]

def sha(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()

def mjson(M):
    return [[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]

def nz_rref_rows(M):
    R,_=M.rref()
    return [[R[i,j] for j in range(R.cols)] for i in range(R.rows) if any(R[i,j] for j in range(R.cols))]

def parent_quotient():
    cr=list(p4.matchings(range(12)))
    creps,_,cmp=p5.classes(cr,p4.symmetry_group()); ci={m:i for i,m in enumerate(creps)}
    CU,_=p4.universal_matrix([p4.universal_poly(m) for m in creps])
    dr=list(p4.matchings(range(10)))
    dreps,_,dmp=p5.classes(dr,p5.d1group()); di={m:i for i,m in enumerate(dreps)}
    _,TB=p5.derivative_basis(); DU=p5.d1matrix(dreps,TB)
    cm=p5.commrels(dr,dmp,di,cmp,ci,len(dreps),len(creps))
    rows=[]
    for v in DU.nullspace(): rows.append(list(v)+[sp.Rational(0)]*len(creps))
    for v in CU.nullspace(): rows.append([sp.Rational(0)]*len(dreps)+list(v))
    rows += [[sp.Rational(x) for x in r] for r in cm]
    Rel=sp.Matrix(rows)
    rr=nz_rref_rows(Rel)
    axes=[9,11]+[len(dreps)+i for i in PARENT_BASIS]
    E=sp.zeros(Rel.cols,8)
    for j,a in enumerate(axes): E[a,j]=1
    C=E.row_join(sp.Matrix(rr).T)
    if Rel.rank()!=17 or p5.rrhash(Rel)!=REL_HASH or C.rank()!=25:
        raise RuntimeError("parent quotient lock mismatch")
    Q=C.inv()[:8,:]
    return Q,creps,cmp,ci,dreps,dmp,di,Rel

def canon_add(v, offset, mp, idx, m, coef):
    m=tuple(sorted((min(a,b),max(a,b)) for a,b in m))
    rep,sg=mp[m]
    if rep is not None:
        v[offset+idx[rep],0] += sp.Rational(coef)*sg

def alg_raw_vector(raw,cmp,ci):
    v=sp.zeros(25,1)
    if raw[0]=="metric":
        mm=list(raw[1])+[(8,10),(9,11)]
        canon_add(v,12,cmp,ci,mm,1)
    else:
        _,i,j,base=raw
        canon_add(v,12,cmp,ci,list(base)+[(8,10),(i,9),(j,11)],-1)
        canon_add(v,12,cmp,ci,list(base)+[(8,10),(9,11),(i,j)],sp.Rational(1,2))
    return v

def remap_pairs(mm,mp):
    return [(mp[a],mp[b]) for a,b in mm]

def der_raw_vector(raw,dmp,di):
    v=sp.zeros(25,1); mp={0:4,1:5,2:6,3:7,4:8,5:9}
    terms=[]
    if raw[0]=="metric":
        terms.append((remap_pairs(raw[1],mp)+[(0,2),(1,3)],sp.Rational(1)))
    else:
        _,i,j,base=raw; oi,oj=mp[i],mp[j]; b=remap_pairs(base,mp)
        terms.append((b+[(0,2),(1,oi),(3,oj)],sp.Rational(-1)))
        terms.append((b+[(0,2),(1,3),(oi,oj)],sp.Rational(1,2)))
    for mm,c in terms:
        # Frozen one-IBP route R*nabla^2R -> (nabla R)^2.
        ib=p5.ibp(tuple(sorted((min(a,b),max(a,b)) for a,b in mm)))
        canon_add(v,0,dmp,di,ib,-c)
    return v

def image_basis_rows(M):
    return nz_rref_rows(M.T)

def axis_witness(M,i):
    e=sp.zeros(8,1); e[i,0]=1; r=M.rank(); aug=M.row_join(e)
    has_component=any(M[i,j]!=0 for j in range(M.cols))
    return {"axis":i,"in_image":aug.rank()==r,"rank_with_axis":aug.rank(),"image_has_axis_component":bool(has_component)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); ap.add_argument("--run-head",default=""); a=ap.parse_args()
    Q,creps,cmp,ci,dreps,dmp,di,Rel=parent_quotient()
    ar=g6.alg_raw(); dr=g6.der_raw()
    cols25=[alg_raw_vector(ar[i],cmp,ci) for i in ALG_PIV]+[der_raw_vector(dr[i],dmp,di) for i in DER_PIV]
    raw25=sp.Matrix.hstack(*cols25); M=Q*raw25
    rank=M.rank(); alg_rank=M[:,:6].rank(); ker=M.nullspace(); span=image_basis_rows(M)
    cubic=sp.zeros(8,6)
    for j,i in enumerate(range(2,8)): cubic[i,j]=1
    union=M.row_join(cubic).rank(); inter=rank+6-union
    complement=[]; B=sp.Matrix.hstack(*M.columnspace()) if rank else sp.zeros(8,0); br=rank
    for i in range(8):
        e=sp.zeros(8,1); e[i,0]=1
        if B.row_join(e).rank()>br:
            complement.append(i); B=B.row_join(e); br+=1
        if br==8: break
    checks={
      "parent_relation_rank_17":Rel.rank()==17,
      "parent_relation_hash":p5.rrhash(Rel)==REL_HASH,
      "generator_counts":len(ar)==525 and len(dr)==60,
      "frozen_generator_indices":ALG_PIV==[16,19,46,52,436,439] and DER_PIV==[1,30,46],
      "matrix_shape_8x9":M.shape==(8,9),
      "rank_consistent":rank==len(span),
      "quotient_dimension_consistent":8-rank==len(complement),
    }
    res={
      "phase":"RCG006_MFR_L0_CONSTRUCTOR_PROGRESS",
      "scientific_prereg":PREREG,"generator_freeze":GEN_FREEZE,"map_contract":MAP_CONTRACT,"parent_freeze":PARENT_FREEZE,"run_head":a.run_head,
      "generator_order":{"ALG":ALG_PIV,"DER":DER_PIV},
      "parent_relation_rank":Rel.rank(),"parent_relation_rref_sha256":p5.rrhash(Rel),
      "raw25_matrix_sha256":sha(mjson(raw25)),"M_FR_shape":list(M.shape),"M_FR":mjson(M),"M_FR_sha256":sha(mjson(M)),
      "rank_M_ALG":alg_rank,"rank_M_FULL":rank,"kernel_dimension":9-rank,"kernel_basis":[[str(x) for x in v] for v in ker],
      "image_rref_rows":[[str(x) for x in r] for r in span],"image_span_sha256":sha([[str(x) for x in r] for r in span]),
      "Q_RCG005_dimension":8,"Q_EFT_dimension":8-rank,"lexicographic_complement_axes":complement,
      "RCG004_intersection_dimension":inter,"RCG004_residual_dimension":6-inter,
      "derivative_axis_witnesses":{"D1D1_CLASS_9":axis_witness(M,0),"D1D1_CLASS_11":axis_witness(M,1)},
      "LS_companion_status":"NOT_COMPUTED_THIS_BOUNDED_SUBGATE","A_HD_transport_status":"NOT_COMPUTED_THIS_BOUNDED_SUBGATE","chi_ABC":"UNAUTHORIZED_NOT_COMPUTED",
      "checks":checks,"constructor_valid":all(checks.values()),
      "classification":"RCG006_MFR_L0_CONSTRUCTOR_PROGRESS_VALID" if all(checks.values()) else "INVALID_RCG006_MFR_L0_CONSTRUCTOR_PROGRESS"
    }
    res["scientific_payload_sha256"]=sha(res)
    Path(a.output).write_text(json.dumps(res,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:res[k] for k in ("rank_M_ALG","rank_M_FULL","Q_EFT_dimension","RCG004_intersection_dimension","classification")},sort_keys=True))
if __name__=="__main__": main()
