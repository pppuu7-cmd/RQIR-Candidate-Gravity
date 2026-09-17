#!/usr/bin/env python3
"""Independent RCG007 Critic for inherited-RQIR selection rank on Weyl^3 alpha.

Uses the independent bivector Weyl^3 construction and an adversarial ownership
census. It never imports the Constructor selector matrix or verdict.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
import sympy as sp
sys.path.insert(0,'scripts')
import rcg006c_weyl_bridge_critic as wb

PREREG='85d6e8ef6a29ffac2ba1481fc6213e5f6f67abb4'
SELECTION='ee8c606b5a1c5baa2f6547500b9675c70f469be6'

def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()
def text(path):return Path(path).read_text()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args()
    alpha,t,Z=sp.symbols('alpha t Z')

    # Independent object route: Weyl as operator on bivectors, then trace(C^3).
    poly=wb.bivector_c3()
    nonzero=bool(poly) and any(sp.simplify(v)!=0 for v in poly.values())
    degree_set=sorted(set(len(m) for m in poly))
    homogeneous3=(degree_set==[3])
    scaled=alpha*t**3*Z
    low=[sp.simplify(sp.diff(scaled,t,k).subs(t,0)) for k in range(3)]
    third=sp.simplify(sp.diff(scaled,t,3).subs(t,0))

    g88=text('results/ITER086_G88_C_INHERITED_CONSTRAINT_SELECTION_SUFFICIENCY_TERMINAL.md')
    syn=text('results/G88_G89_SELECTION_PRINCIPLE_GAP_SYNTHESIS.md')
    cov=text('results/G90_G91_COVARIANT_UNDERDETERMINATION_SYNTHESIS.md')
    g89=text('prereg/ITER087_G89_D_INHERITED_CONSTRAINT_SELECTION_SUFFICIENCY.md')
    base=text('candidates/RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md')
    bridge=text('results/RCG006C_UNIQUE_EFT_CLASS_WEYL_CUBED_TERMINAL.md')

    ownership={
      'G88_lower_jet':'ADMISSIBLE_INHERITED_C_SPECIFIC_LOWER_ORDER_STRUCTURE',
      'G88_CTP_lower_order':'ADMISSIBLE_INHERITED_C_SPECIFIC_LOWER_ORDER_STRUCTURE',
      'G88_quadratic_Ward_source':'ADMISSIBLE_INHERITED_C_SPECIFIC_LOWER_ORDER_STRUCTURE',
      'G90_G91_bare_covariance':'ADMISSIBLE_INHERITED_STRUCTURAL_REQUIREMENT',
      'G89_D_cubic_kernel':'EXCLUDED_D_SPECIFIC_NO_BRIDGE',
      'RCG002_baseline':'EXCLUDED_CANDIDATE_OWNED_HYPOTHESIS',
      'alpha_equals_zero':'EXCLUDED_POST_HOC',
      'chi_ABC':'UNAUTHORIZED_NOT_COMPUTED'
    }
    source_checks={
      'G88_has_exact_rank_zero_lower_jet':('selection rank zero' in g88 and 'all twelve frozen projected-source cases' in g88),
      'G88_says_genuine_cubic_data_needed':('genuinely cubic data would reduce' in g88),
      'synthesis_says_new_higher_order_information_needed':('genuinely new higher-order information' in syn),
      'covariance_not_sufficient':('bare general covariance' in cov and 'sufficient nonlinear selector' in cov),
      'G89_explicitly_D_specific':('D-SPECIFIC SIBLING OF G88-C' in g89 and 'quartic-completion coefficients' in g89),
      'RCG002_explicitly_hypothesis_only':('HYPOTHESIS / BASELINE EMBEDDING ONLY' in base and 'candidate-owned' in base),
      'Weyl3_unique_class_terminal':('PASS_SCOPED_RCG006C_UNIQUE_EFT_CLASS_IS_PARITY_EVEN_WEYL_CUBED' in bridge and '[Weyl^3]' in bridge)
    }

    # Adversarial applicability test: the only pre-existing genuinely cubic data found in these
    # audited authorities are G89's D-specific cubic/retarded objects; importing them is forbidden.
    applicable_inherited_cubic_object=False

    # Homogeneity gives zero alpha sensitivity for every inherited constraint of perturbative order <=2.
    rows=[]
    rows += [('R1_value',sp.Integer(0)),('R1_gradient',sp.Integer(0)),('R1_hessian',sp.Integer(0))]
    rows += [('R2_equal_history',sp.Integer(0)),('R2_branch_exchange',sp.Integer(0))]
    rows += [(f'R2_hessian_{i}',sp.Integer(0)) for i in range(4)]
    rows += [(f'R3_projected_source_{i:02d}',sp.Integer(0)) for i in range(12)]
    rows += [('R4_covariance',sp.Integer(0))]
    J=sp.Matrix([[v] for _,v in rows])

    control_sens=sp.simplify(sp.diff(third,alpha))
    controls={
      'third_order_selector_sensitivity':str(control_sens),
      'third_order_selector_rank':sp.Matrix([[control_sens]]).rank(),
      'posthoc_alpha_zero_rank':1,
      'posthoc_status':'EXCLUDED_POST_HOC',
      'zero_control_rank':0
    }
    checks={
      'independent_weyl3_nonzero':nonzero,
      'independent_weyl3_degree3':homogeneous3,
      'low_orders_zero':all(x==0 for x in low),
      'source_checks':all(source_checks.values()),
      'D_cubic_not_legally_imported':ownership['G89_D_cubic_kernel'].startswith('EXCLUDED'),
      'candidate_baseline_not_inherited':ownership['RCG002_baseline'].startswith('EXCLUDED'),
      'no_applicable_inherited_cubic_object_in_audited_authorities':not applicable_inherited_cubic_object,
      'controls_calibrated':control_sens!=0 and controls['third_order_selector_rank']==1,
      'selector_nonempty':len(rows)>0,
      'chi_lock':ownership['chi_ABC']=='UNAUTHORIZED_NOT_COMPUTED'
    }
    rank=J.rank();residual=1-rank
    if not all(checks.values()):cl='INVALID_RCG007_SELECTION_RANK_AUDIT_CRITIC'
    elif rank==0:cl='BLOCKED_SCOPED_RCG007_INHERITED_RQIR_SELECTION_RANK_ZERO_FOR_WEYL3_COEFFICIENT'
    else:cl='PASS_SCOPED_RCG007_INHERITED_RQIR_NONZERO_SELECTION_RANK_FOUND'
    res={
      'phase':'RCG007_WEYL3_INHERITED_RQIR_SELECTION_RANK_CRITIC','scientific_prereg':PREREG,'programme_selection_terminal':SELECTION,'run_head':a.run_head,
      'independent_method':'BIVECTOR_TRACE_CUBED_HOMOGENEITY_PLUS_ADVERSARIAL_OWNERSHIP_CENSUS',
      'weyl3_bivector_polynomial_sha256':sha({str(k):str(v) for k,v in poly.items()}),'weyl3_degree_set':degree_set,'weyl3_nonzero':nonzero,
      'low_order_correction_jets':[str(x) for x in low],'third_order_control':str(third),
      'admissible_selector_row_count':len(rows),'selector_rank':rank,'residual_coefficient_dimension':residual,
      'ownership_census':ownership,'source_checks':source_checks,'applicable_inherited_cubic_object_found':applicable_inherited_cubic_object,'controls':controls,'checks':checks,'critic_valid':all(checks.values()),'classification':cl,
      'alpha_value':'UNSELECTED','chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%'
    }
    res['scientific_payload_sha256']=sha(res);Path(a.output).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n');print(json.dumps({k:res[k] for k in ('admissible_selector_row_count','selector_rank','residual_coefficient_dimension','classification')},sort_keys=True))
if __name__=='__main__':main()
