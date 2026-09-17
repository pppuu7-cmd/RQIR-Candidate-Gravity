#!/usr/bin/env python3
"""RCG006 frozen higher-derivative discriminator transport Constructor."""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
import sympy as sp
sys.path.insert(0,"scripts")
import rcg004_complete_cubic_constructor as p4

PREREG="fc3ff1f49c56f2befc039e09ebd8f388833dbff1"
MFR_TERMINAL="12ca52947d1390a494634b7a6a2d98d9a7e4bf7d"
PARENT_HSHA="7014978a97fce634d93f00e414903597245b8e4268b2c575dd1764547f96ced9"
PARENT_BASIS=[0,1,2,4,5,8]
A6=sp.Matrix([[-2,-2],[-2,0],[-2,0],[-2,-2],[-2,0],[-2,-2]])

def sha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def mj(M): return [[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]
def q(x): return sp.Rational(str(x))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args()
    c=json.loads(Path('results/raw/RCG006_MFR_L0_CANONICAL.json').read_text())
    M=sp.Matrix([[q(x) for x in row] for row in c['M_FR']])
    raw=list(p4.matchings(range(12))); reps,_=p4.canonical_classes(raw)
    U,_=p4.universal_matrix([p4.universal_poly(m) for m in reps]);_,piv=U.rref()
    basis=[reps[i] for i in piv]; H=p4.hessian_matrix([p4.invariant_poly(m) for m in basis])
    hsha=sha(mj(H))
    A=sp.zeros(A6.rows+H.rows,8)
    A[:A6.rows,:2]=A6;A[A6.rows:,2:]=H
    P=A*M
    checks={
      'canonical_mfr_rank7':M.rank()==7,
      'parent_basis_lock':list(piv)==PARENT_BASIS,
      'A6_rank2':A6.rank()==2,
      'H_shape_54x6':H.shape==(54,6),
      'H_rank6':H.rank()==6,
      'H_hash_lock':hsha==PARENT_HSHA,
      'A_HD_rank8':A.rank()==8,
      'A_HD_kernel_zero':len(A.nullspace())==0,
      'transport_rank7':P.rank()==7,
      'image_kernel_zero':M.rank()-P.rank()==0
    }
    branch='CASE_II_NONINVARIANT' if M.rank()>0 and P.rank()>0 else ('CASE_I_IMAGE_ZERO' if M.rank()==0 else 'CASE_III_INVARIANT_ON_IMAGE')
    res={
      'phase':'RCG006_A_HD_TRANSPORT_CONSTRUCTOR', 'scientific_prereg':PREREG,'mfr_terminal':MFR_TERMINAL,'run_head':a.run_head,
      'M_FR_sha256':c['M_FR_sha256'],'rank_M_FR':M.rank(),
      'A6_shape':list(A6.shape),'A6_rank':A6.rank(),
      'RCG004_H_shape':list(H.shape),'RCG004_H_rank':H.rank(),'RCG004_H_sha256':hsha,
      'A_HD_shape':list(A.shape),'A_HD_rank':A.rank(),'A_HD_kernel_dimension':len(A.nullspace()),'A_HD_sha256':sha(mj(A)),
      'A_HD_M_FR_shape':list(P.shape),'A_HD_M_FR_rank':P.rank(),'A_HD_M_FR_sha256':sha(mj(P)),
      'field_redefinition_image_kernel_dimension_under_A_HD':M.rank()-P.rank(),
      'structural_branch':branch,
      'representative_nonzero_eft_quotient_zero_exists':bool(M.rank()>0 and P.rank()>0),
      'quotient_aware_second_order_space_dimension':0,
      'checks':checks,'constructor_valid':all(checks.values()),
      'classification':'PASS_SCOPED_RCG006_A_HD_TRANSPORT_NONINVARIANT' if all(checks.values()) and branch=='CASE_II_NONINVARIANT' else 'INVALID_RCG006_A_HD_TRANSPORT',
      'chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%'
    }
    res['scientific_payload_sha256']=sha(res);Path(a.output).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:res[k] for k in ('A_HD_rank','A_HD_kernel_dimension','A_HD_M_FR_rank','structural_branch','classification')},sort_keys=True))
if __name__=='__main__':main()
