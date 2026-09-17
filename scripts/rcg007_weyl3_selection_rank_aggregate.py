#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--constructor',required=True);ap.add_argument('--critic',required=True);ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args()
    c=json.loads(Path(a.constructor).read_text());k=json.loads(Path(a.critic).read_text())
    checks={
      'constructor_valid':c.get('constructor_valid') is True,
      'critic_valid':k.get('critic_valid') is True,
      'same_prereg':c.get('scientific_prereg')==k.get('scientific_prereg')=='85d6e8ef6a29ffac2ba1481fc6213e5f6f67abb4',
      'weyl3_nonzero':c.get('weyl3_polynomial_nonzero') is True and k.get('weyl3_nonzero') is True,
      'weyl3_order3':c.get('weyl3_curvature_homogeneous_degree')==3 and k.get('weyl3_degree_set')==[3],
      'same_row_count':len(c.get('admissible_selector_rows',[]))==k.get('admissible_selector_row_count')==22,
      'same_selector_rank':c.get('selector_rank')==k.get('selector_rank'),
      'same_residual_dimension':c.get('residual_coefficient_dimension')==k.get('residual_coefficient_dimension'),
      'controls_nonzero':c.get('controls',{}).get('genuine_cubic_selector_rank')==1 and k.get('controls',{}).get('third_order_selector_rank')==1,
      'posthoc_excluded':c.get('excluded_objects',{}).get('alpha_equals_zero')=='EXCLUDED_EXTERNAL_POST_HOC' and k.get('ownership_census',{}).get('alpha_equals_zero')=='EXCLUDED_POST_HOC',
      'G89_D_excluded':str(c.get('excluded_objects',{}).get('G89_D_cubic_kernel','')).startswith('EXCLUDED') and str(k.get('ownership_census',{}).get('G89_D_cubic_kernel','')).startswith('EXCLUDED'),
      'RCG002_excluded':str(c.get('excluded_objects',{}).get('RCG002_linearized_baseline','')).startswith('EXCLUDED') and str(k.get('ownership_census',{}).get('RCG002_baseline','')).startswith('EXCLUDED'),
      'chi_locked':c.get('chi_ABC')==k.get('chi_ABC')=='UNAUTHORIZED_NOT_COMPUTED'
    }
    valid=all(checks.values());rank=c.get('selector_rank') if valid else None;resid=c.get('residual_coefficient_dimension') if valid else None
    if not valid:cl='INVALID_RCG007_SELECTION_RANK_AUDIT_AGGREGATE'
    elif rank==0:cl='BLOCKED_SCOPED_RCG007_INHERITED_RQIR_SELECTION_RANK_ZERO_FOR_WEYL3_COEFFICIENT'
    else:cl='PASS_SCOPED_RCG007_INHERITED_RQIR_NONZERO_SELECTION_RANK_FOUND'
    r={
      'phase':'RCG007_WEYL3_INHERITED_RQIR_SELECTION_RANK_AGGREGATE','run_head':a.run_head,'aggregate_valid':valid,'agreement_checks':checks,
      'admissible_selector_row_count':22 if valid else None,'selector_rank':rank,'residual_coefficient_dimension':resid,
      'classification':cl,
      'scientific_consequence':'The already-frozen admissible inherited RQIR lower-jet/CTP/quadratic-Ward/covariance information has exact selection rank zero on the unique Weyl^3 coefficient; a genuinely cubic candidate-independent datum or separately justified selection principle is required before alpha can be selected.' if valid and rank==0 else 'See classification.',
      'G89_D_cubic_kernel_status':'EXCLUDED_D_SPECIFIC_NO_RCG007_BRIDGE','RCG002_baseline_status':'EXCLUDED_CANDIDATE_OWNED_HYPOTHESIS','alpha_value':'UNSELECTED','chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%'
    }
    r['scientific_payload_sha256']=sha(r);Path(a.output).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({k:r[k] for k in ('aggregate_valid','selector_rank','residual_coefficient_dimension','classification')},sort_keys=True))
if __name__=='__main__':main()
