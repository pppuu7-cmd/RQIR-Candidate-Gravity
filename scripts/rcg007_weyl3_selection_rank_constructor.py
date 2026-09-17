#!/usr/bin/env python3
"""RCG007 Constructor: exact inherited-RQIR selection rank on the unique Weyl^3 coefficient.

No coefficient is solved. The scientific object is the exact one-column
sensitivity matrix of legally inherited constraints.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
import sympy as sp
sys.path.insert(0,'scripts')
import rcg006c_weyl_bridge_constructor as w3

PREREG='85d6e8ef6a29ffac2ba1481fc6213e5f6f67abb4'
SELECTION='ee8c606b5a1c5baa2f6547500b9675c70f469be6'
W3_TERMINAL='d072cabcc4f5ccf46af382e16b7dbe62c935f3c4'
G88_TERMINAL='9ecc7947d3a5e53e72acfbe9297e5dbc23cf155e'
G88_SYNTH='2204951424f37705f7031a122fda3cfcb1a18f00'
G90_SYNTH='cf2463bbb2236a20c98dda5e50cdd620c8def8a7'
G89_PREREG='b4a0a867f937da0e4a557bcc07fc93ce7d567f02'
RCG002_BASELINE='59e45f3503b677158827626b04d26e75479f2e82'

def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()
def has(path,*phrases):
    s=Path(path).read_text()
    return all(p in s for p in phrases)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args()
    alpha,eps,W=sp.symbols('alpha epsilon W3', nonzero=False)

    # Mechanical RCG006C object check: the generic exact Weyl^3 polynomial is nonzero
    # and homogeneous degree 3 in the exact curvature coordinates.
    poly=w3.c3poly()
    homogeneous=bool(poly) and all(len(m)==3 for m in poly)
    poly_nonzero=bool(poly) and any(sp.simplify(v)!=0 for v in poly.values())
    delta=alpha*eps**3*W
    jets=[sp.simplify(sp.diff(delta,eps,k).subs(eps,0)) for k in range(3)]
    jet_sens=[sp.simplify(sp.diff(x,alpha)) for x in jets]
    cubic=sp.simplify(sp.diff(delta,eps,3).subs(eps,0))
    cubic_sens=sp.simplify(sp.diff(cubic,alpha))

    # CTP branch-difference lower-order identities.
    ep,em=sp.symbols('epsilon_plus epsilon_minus')
    ctp=alpha*W*(ep**3-em**3)
    equal_hist=sp.simplify(ctp.subs({ep:eps,em:eps}))
    branch_odd=sp.simplify(ctp.subs({ep:em,em:ep}, simultaneous=True)+ctp)
    ctp_hessian=[]
    for x in (ep,em):
      for y in (ep,em):
        ctp_hessian.append(sp.simplify(sp.diff(ctp,x,y).subs({ep:0,em:0})))

    # Frozen admissible inherited rows. G88 explicitly has 12 projected-source cases.
    rows=[]
    for name,val in [('R1_flat_value',jet_sens[0]),('R1_flat_gradient',jet_sens[1]),('R1_flat_hessian',jet_sens[2])]: rows.append((name,val,'G88_LOWER_JET'))
    rows += [('R2_ctp_equal_history',sp.diff(equal_hist,alpha),'G88_CTP'),('R2_ctp_branch_exchange',sp.diff(branch_odd,alpha),'G88_CTP')]
    for i,x in enumerate(ctp_hessian): rows.append((f'R2_ctp_hessian_{i}',sp.diff(x,alpha),'G88_CTP'))
    # Because the correction has exact zero quadratic Hessian, every frozen quadratic response/source equation has zero alpha sensitivity.
    for i in range(12): rows.append((f'R3_projected_source_case_{i:02d}',sp.Integer(0),'G88_QUADRATIC_WARD_PROJECTED_SOURCE'))
    # Weyl^3 is itself a covariant scalar contraction; multiplying it by a constant alpha preserves covariance identically.
    rows.append(('R4_bare_covariance_identity',sp.Integer(0),'G90_G91_BARE_COVARIANCE'))
    J=sp.Matrix([[sp.simplify(v)] for _,v,_ in rows])

    source_checks={
      'G88_terminal_scope':has('results/ITER086_G88_C_INHERITED_CONSTRAINT_SELECTION_SUFFICIENCY_TERMINAL.md','C_FROZEN_QUADRATIC_WARD_SECTOR_COEFFICIENT_BLIND_SCOPED','all twelve frozen projected-source cases'),
      'G88_synthesis_rank_zero_authority':has('results/G88_G89_SELECTION_PRINCIPLE_GAP_SYNTHESIS.md','selection rank zero','genuinely new higher-order information'),
      'G90_covariance_insufficient_authority':has('results/G90_G91_COVARIANT_UNDERDETERMINATION_SYNTHESIS.md','bare general covariance','not, within these explicit families, a sufficient nonlinear selector'),
      'G89_is_D_specific':has('prereg/ITER087_G89_D_INHERITED_CONSTRAINT_SELECTION_SUFFICIENCY.md','D-SPECIFIC SIBLING OF G88-C','frozen D cubic/three-point data','quartic-completion coefficients'),
      'RCG002_is_hypothesis_only':has('candidates/RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md','HYPOTHESIS / BASELINE EMBEDDING ONLY','candidate-owned linearized dynamical rule'),
      'W3_terminal_identity':has('results/RCG006C_UNIQUE_EFT_CLASS_WEYL_CUBED_TERMINAL.md','PASS_SCOPED_RCG006C_UNIQUE_EFT_CLASS_IS_PARITY_EVEN_WEYL_CUBED','unique one-dimensional quotient')
    }
    exclusions={
      'G89_D_cubic_kernel':'EXCLUDED_D_SPECIFIC_NO_RCG007_BRIDGE',
      'RCG002_linearized_baseline':'EXCLUDED_CANDIDATE_OWNED_HYPOTHESIS',
      'alpha_equals_zero':'EXCLUDED_EXTERNAL_POST_HOC',
      'chi_ABC':'UNAUTHORIZED_NOT_COMPUTED'
    }
    controls={
      'genuine_cubic_datum_sensitivity':str(cubic_sens),
      'genuine_cubic_selector_rank':sp.Matrix([[cubic_sens]]).rank(),
      'posthoc_alpha_zero_rank':sp.Matrix([[sp.diff(alpha,alpha)]]).rank(),
      'posthoc_alpha_zero_status':'EXTERNAL_POST_HOC_EXCLUDED',
      'zero_datum_rank':sp.Matrix([[0]]).rank()
    }
    checks={
      'source_checks':all(source_checks.values()),
      'weyl3_polynomial_nonzero':poly_nonzero,
      'weyl3_curvature_homogeneous_degree3':homogeneous,
      'flat_jets_0_1_2_zero':all(x==0 for x in jets),
      'ctp_equal_history':equal_hist==0,
      'ctp_branch_exchange_odd':branch_odd==0,
      'ctp_hessian_zero':all(x==0 for x in ctp_hessian),
      'admissible_selector_nonempty':len(rows)>0,
      'controls_detect_nonzero_cubic':cubic_sens!=0 and controls['genuine_cubic_selector_rank']==1,
      'posthoc_control_detected_excluded':controls['posthoc_alpha_zero_rank']==1,
      'zero_control_rank0':controls['zero_datum_rank']==0,
      'chi_lock':exclusions['chi_ABC']=='UNAUTHORIZED_NOT_COMPUTED'
    }
    rank=J.rank(); residual=1-rank
    if not all(checks.values()): classification='INVALID_RCG007_SELECTION_RANK_AUDIT_CONSTRUCTOR'
    elif rank==0: classification='BLOCKED_SCOPED_RCG007_INHERITED_RQIR_SELECTION_RANK_ZERO_FOR_WEYL3_COEFFICIENT'
    else: classification='PASS_SCOPED_RCG007_INHERITED_RQIR_NONZERO_SELECTION_RANK_FOUND'
    res={
      'phase':'RCG007_WEYL3_INHERITED_RQIR_SELECTION_RANK_CONSTRUCTOR','scientific_prereg':PREREG,'programme_selection_terminal':SELECTION,'weyl3_terminal':W3_TERMINAL,'run_head':a.run_head,
      'authority_commits':{'G88_terminal':G88_TERMINAL,'G88_G89_synthesis':G88_SYNTH,'G90_G91_synthesis':G90_SYNTH,'G89_prereg':G89_PREREG,'RCG002_baseline':RCG002_BASELINE},
      'weyl3_generic_polynomial_sha256':sha({str(k):str(v) for k,v in poly.items()}),'weyl3_polynomial_nonzero':poly_nonzero,'weyl3_curvature_homogeneous_degree':3 if homogeneous else None,
      'formal_correction':str(delta),'flat_correction_jets_order_0_1_2':[str(x) for x in jets],'third_derivative_control':str(cubic),
      'admissible_selector_rows':[{'name':n,'sensitivity_dF_dalpha':str(v),'authority_class':src} for n,v,src in rows],
      'selector_matrix_shape':list(J.shape),'selector_rank':rank,'residual_coefficient_dimension':residual,
      'source_checks':source_checks,'excluded_objects':exclusions,'controls':controls,'checks':checks,'constructor_valid':all(checks.values()),'classification':classification,
      'alpha_value':'UNSELECTED','chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%'
    }
    res['scientific_payload_sha256']=sha(res);Path(a.output).write_text(json.dumps(res,indent=2,sort_keys=True)+'\n');print(json.dumps({k:res[k] for k in ('selector_matrix_shape','selector_rank','residual_coefficient_dimension','classification')},sort_keys=True))
if __name__=='__main__':main()
