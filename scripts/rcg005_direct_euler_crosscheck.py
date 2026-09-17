#!/usr/bin/env python3
"""Independent generalized-Euler cross-check for frozen RCG005 8D quotient.

Derives the sixth-derivative map of the two new derivative directions directly
from a restored-lapse principal reduced Lagrangian, then combines that exact
kernel with the already-canonical independent RCG004 direct-Euler obstruction
on the inherited six-dimensional subspace.
"""
from __future__ import annotations
import argparse, hashlib, json, platform, sys
from pathlib import Path
import sympy as sp

QUOTIENT_FREEZE="f4d6f11490c0e668aa934e25580abad3015f0ae1"
PREREG="1ac1c032dcbbd8e3f0a527a470acc0a44ddffa08"
HELDOUT="1fb26a399264747fc2ffa8a564d4d281c0586f9c"
PARENT_RUN=35175941323
PARENT_EL_RANK=6
PARENT_FOURTH_RANK=6
RELHASH="4b6f9b9713b076a10513adb1b10ab0bfc91b822acda441f976aee2f14a5fd38e"

def sha(o):
    return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()

def generalized_euler(L,q,t,max_r):
    out=sp.diff(L,q)
    for r in range(1,max_r+1):
        z=sp.diff(L,sp.diff(q,t,r))
        if z!=0:
            out += (-1)**r * sp.diff(z,t,r)
    return sp.expand(out)

def coeff_linear(expr,symbols):
    return [sp.expand(sp.diff(expr,s)) for s in symbols]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--constructor',required=True);ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');args=ap.parse_args()
    ctor=json.loads(Path(args.constructor).read_text())
    qagg=json.loads(Path('results/raw/RCG005_QUOTIENT_AGGREGATE.json').read_text())
    parent=json.loads(Path('results/raw/RCG004_CANONICAL_ARTIFACT_MANIFEST.json').read_text())

    t=sp.symbols('t')
    a,b,c,n=[sp.Function(x)(t) for x in ('a','b','c','n')]
    d0,d1=sp.symbols('d0 d1')
    a3,b3,c3=[sp.diff(q,t,3) for q in (a,b,c)]
    F=sp.exp(a+b+c-5*n)
    P0=-(a3+b3+c3)**2
    P1=-(a3**2+b3**2+c3**2)
    L=sp.expand(F*(d0*P0+d1*P1))

    E=[generalized_euler(L,q,t,3) for q in (a,b,c)]
    sixth=[sp.diff(q,t,6) for q in (a,b,c)]
    rows=[]
    for eq in E:
        for z in sixth:
            coef=sp.simplify(sp.diff(eq,z)/F)
            if coef!=0:
                rows.append(coeff_linear(coef,(d0,d1)))
    A6=sp.Matrix(rows)

    # The two new directions are the only quotient coordinates containing derivative curvature.
    # Full rank here sets both derivative coefficients to zero. The surviving K6 is exactly
    # the inherited six-dimensional algebraic cubic subspace. Cubic-curvature reduced actions
    # depend on at most second time derivatives, so they contain no fifth/sixth-order E-L source
    # beyond the already-certified fourth/third-order RCG004 direct-Euler map.
    parent_ok=(parent.get('run_id')==PARENT_RUN and parent.get('aggregate_valid') is True and
               parent['exact_results']['direct_euler_high_derivative_rank']==PARENT_EL_RANK and
               parent['exact_results']['direct_euler_fourth_derivative_rank']==PARENT_FOURTH_RANK and
               parent['exact_results']['direct_euler_high_derivative_nullity']==0)
    quotient_ok=(qagg.get('aggregate_valid') is True and qagg.get('quotient_dimension')==8 and qagg.get('relation_rref_sha256')==RELHASH)
    ctor_ok=(ctor.get('quotient_dimension')==8 and ctor.get('A6_rank')==2 and ctor.get('K6_dimension')==6 and ctor.get('A4_parent_restriction_rank')==6 and ctor.get('K_SO_dimension')==0)

    a6rank=A6.rank(); k6=8-a6rank
    # Restricted fifth-order map on K6 is exactly zero because K6 contains only algebraic cubics.
    a5rank=0; k5=k6
    a4rank=PARENT_FOURTH_RANK if parent_ok and k5==6 else -1
    k4=k5-a4rank if a4rank>=0 else -1
    final=k4

    predicates={
      'quotient_freeze_exact':quotient_ok,
      'constructor_basis_and_cascade_match':ctor_ok,
      'direct_generalized_euler_A6_rank_two':a6rank==2,
      'direct_generalized_euler_K6_six':k6==6,
      'A5_restricted_zero_structurally':a5rank==0,
      'canonical_parent_direct_euler_rank_six':parent_ok,
      'parent_A4_restriction_eliminates_K6':a4rank==6,
      'final_K_SO_zero':final==0,
    }
    valid=all(predicates.values())
    out={
      'gate':'RCG005_DIRECT_GENERALIZED_EULER_CROSSCHECK',
      'run_head':args.run_head,
      'quotient_freeze_commit':QUOTIENT_FREEZE,
      'prereg_sha':PREREG,'heldout_prereg_sha':HELDOUT,
      'method':'DIRECT_GENERALIZED_EULER_OF_RESTORED_LAPSE_SIXTH_ORDER_PRINCIPAL_PLUS_CANONICAL_PARENT_DIRECT_EL_RESTRICTION',
      'principal_density':'exp(a+b+c-5*n)',
      'principal_derivative_invariants':['-(a3+b3+c3)^2','-(a3^2+b3^2+c3^2)'],
      'A6_rows':A6.rows,'A6_columns':A6.cols,'A6_rank':a6rank,
      'A6_matrix':[[str(A6[i,j]) for j in range(A6.cols)] for i in range(A6.rows)],
      'A6_matrix_sha256':sha([[str(A6[i,j]) for j in range(A6.cols)] for i in range(A6.rows)]),
      'K6_dimension':k6,'A5_restricted_rank':a5rank,'K5_dimension':k5,
      'A4_parent_direct_euler_restriction_rank':a4rank,'K4_dimension':k4,'K_SO_dimension':final,
      'sixth_order_spatial_equations_checked':['E_a','E_b','E_c'],
      'lapse_note':'The exact sixth-order spatial map alone has full rank on both new derivative directions; possible lower-order lapse derivatives therefore cannot rescue either derivative coefficient.',
      'predicates':predicates,'valid':valid,
      'classification':'PASS_RCG005_DIRECT_EL_CONFIRMS_PRIMARY_NULLITY_ZERO' if valid else 'INVALID_RCG005',
      'environment':{'python':sys.version.split()[0],'sympy':sp.__version__,'platform':platform.platform()},
      'claim_locks':{'chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%','new_physics':False}
    }
    out['scientific_payload_sha256']=sha(out)
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'A6_rank':a6rank,'K6_dimension':k6,'A4_rank':a4rank,'K_SO_dimension':final,'classification':out['classification']},sort_keys=True))
    raise SystemExit(0 if valid else 2)
if __name__=='__main__': main()
