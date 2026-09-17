#!/usr/bin/env python3
"""Independent RCG006 A_HD transport Critic.

Uses the frozen parent block ranks plus direct exact product reconstruction to avoid
relying on the Constructor's final A_HD matrix or verdict.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
import sympy as sp
sys.path.insert(0,"scripts")
import rcg004_complete_cubic_constructor as p4

PREREG="fc3ff1f49c56f2befc039e09ebd8f388833dbff1"
PARENT_HSHA="7014978a97fce634d93f00e414903597245b8e4268b2c575dd1764547f96ced9"
PARENT_BASIS=[0,1,2,4,5,8]

def sha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def mj(M): return [[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]
def q(x): return sp.Rational(str(x))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args()
    c=json.loads(Path('results/raw/RCG006_MFR_L0_CANONICAL.json').read_text())
    M=sp.Matrix([[q(x) for x in row] for row in c['M_FR']])
    A6=sp.Matrix([[-2,-2],[-2,0],[-2,0],[-2,-2],[-2,0],[-2,-2]])
    raw=list(reversed(list(p4.matchings(range(12)))))
    # Recanonicalize independently from reverse enumeration, then restore lexical class order.
    reps,_=p4.canonical_classes(raw)
    U,_=p4.universal_matrix([p4.universal_poly(m) for m in reps]);_,piv=U.rref()
    H=p4.hessian_matrix([p4.invariant_poly(reps[i]) for i in piv])
    hsha=sha(mj(H))
    # Analytic block proof: A6 acts only on derivative axes 0..1; H acts only on cubic axes 2..7.
    block_rank=A6.rank()+H.rank()
    A=sp.zeros(A6.rows+H.rows,8);A[:A6.rows,:2]=A6;A[A6.rows:,2:]=H
    P=A*M
    proof={
      'reverse_enumeration_parent_basis_lock':list(piv)==PARENT_BASIS,
      'parent_H_hash_lock':hsha==PARENT_HSHA,
      'disjoint_block_rank_sum_8':block_rank==8,
      'direct_A_rank8':A.rank()==8,
      'direct_A_kernel_zero':len(A.nullspace())==0,
      'M_rank7':M.rank()==7,
      'injectivity_forces_transport_rank7':P.rank()==M.rank()==7
    }
    branch='CASE_II_NONINVARIANT' if P.rank()>0 else 'CASE_III_INVARIANT_ON_IMAGE'
    res={
      'phase':'RCG006_A_HD_TRANSPORT_CRITIC','scientific_prereg':PREREG,'run_head':a.run_head,
      'M_FR_sha256':c['M_FR_sha256'],'rank_M_FR':M.rank(),
      'RCG004_H_sha256':hsha,'analytic_block_rank':block_rank,'A_HD_rank':A.rank(),'A_HD_kernel_dimension':len(A.nullspace()),
      'A_HD_M_FR_rank':P.rank(),'A_HD_M_FR_sha256':sha(mj(P)),
      'field_redefinition_image_kernel_dimension_under_A_HD':M.rank()-P.rank(),
      'structural_branch':branch,'proof_checks':proof,'critic_valid':all(proof.values()),
      'classification':'PASS_SCOPED_RCG006_A_HD_TRANSPORT_NONINVARIANT' if all(proof.values()) and branch=='CASE_II_NONINVARIANT' else 'INVALID_RCG006_A_HD_TRANSPORT',
      'chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%'
    }
    res['scientific_payload_sha256']=sha(res);Path(a.output).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:res[k] for k in ('A_HD_rank','A_HD_kernel_dimension','A_HD_M_FR_rank','structural_branch','classification')},sort_keys=True))
if __name__=='__main__':main()
