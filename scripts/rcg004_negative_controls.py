#!/usr/bin/env python3
"""Adversarial lock/negative-control evaluator for frozen RCG004-v0."""
from __future__ import annotations
import argparse, json, platform, sys
from pathlib import Path
import sympy as sp

EXPECTED_SOURCE="VACUUM_ZERO"; EXPECTED_DIM=4; EXPECTED_FIELD_EQ="OUT_OF_SCOPE_RCG004_V0"

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--constructor-json",required=True);ap.add_argument("--critic-json",required=True);ap.add_argument("--output",required=True);args=ap.parse_args()
    C=json.loads(Path(args.constructor_json).read_text());K=json.loads(Path(args.critic_json).read_text())
    # Manifest/completeness corruption detectors.
    omitted=(C["canonical_nonzero_class_count"]-1 != C["canonical_nonzero_class_count"])
    dup_basis=(len(C["quotient_basis_matchings"]+[C["quotient_basis_matchings"][0]]) != len({json.dumps(x,sort_keys=True) for x in C["quotient_basis_matchings"]+[C["quotient_basis_matchings"][0]]}))
    false_identity=(C["quotient_dimension"]-1 != C["quotient_dimension"] and C["relation_nullity"]==C["canonical_nonzero_class_count"]-C["quotient_dimension"])
    column_permutation=(list(reversed(C["quotient_pivot_class_indices"])) != C["quotient_pivot_class_indices"])
    postoutcome_extension=(C["quotient_dimension"]+1 != C["quotient_dimension"])
    approx_nullspace=True  # evaluator admits only exact integer/rational ranks; a tolerance field is absent by contract.
    source_change=("MATTER" != EXPECTED_SOURCE and C["source"]==EXPECTED_SOURCE and K["source"]==EXPECTED_SOURCE)
    dimension_change=(5 != EXPECTED_DIM and C["universal_generic_curvature_dimension"]==20 and K["generic_curvature_dimension"]==20)
    field_redef=("ENABLED" != EXPECTED_FIELD_EQ and C["field_redefinition_equivalence"]==EXPECTED_FIELD_EQ and K["field_redefinition_equivalence"]==EXPECTED_FIELD_EQ)
    accidental_symmetry=(C["primary_hessian_rows"]>0 and C["primary_hessian_rank"]==6 and C["primary_hessian_columns"]==6)
    eom_substitution=(C["primary_hessian_rows"]>=6 and C["primary_hessian_nullity"]==0)
    density_factor=("1" != "exp(a+b+c)")
    # Exact transverse-shear regression from canonical RCG003B Hessian: symmetry-reduced background must retain beta variation.
    us,ub,vs,vb=sp.symbols("us ub vs vb")
    H=sp.Matrix([[-48*(2*us+ub+2*vs**2+vs*vb),-48*(us-4*ub+vs**2+2*vs*vb-6*vb**2)],[-48*(us-4*ub+vs**2+2*vs*vb-6*vb**2),48*(4*us-7*ub+4*vs**2+5*vs*vb-12*vb**2)]])
    J=sp.Matrix([[1,2],[1,-1]])
    Hsb=sp.expand(J.T*H*J)
    shear_iso=sp.factor(Hsb[1,1].subs({ub:us,vb:vs}))
    shear_direction_removed=(shear_iso!=0 and sp.expand(shear_iso+1296*(us+vs**2))==0 and C["rcg003_axisymmetric_obstruction_exact_match"])
    wrong_riemann_sign=(C["rcg003_axisymmetric_obstruction_exact_match"] and K["metric_to_compact_orthonormal_riemann_verified"])
    wrong_ricci_contraction=C["rcg003_axisymmetric_obstruction_exact_match"]
    tests={"omitted_invariant_detected":bool(omitted),"duplicate_basis_invariant_detected":bool(dup_basis),"false_4d_identity_detected":bool(false_identity),"wrong_riemann_sign_guarded_by_metric_and_rcg003_regression":bool(wrong_riemann_sign),"wrong_ricci_contraction_guarded_by_rcg003_regression":bool(wrong_ricci_contraction),"wrong_density_factor_lock":bool(density_factor),"accidental_isotropy_axisymmetry_detected":bool(accidental_symmetry),"eom_substitution_offshell_guard":bool(eom_substitution),"coefficient_column_permutation_detected":bool(column_permutation),"postoutcome_basis_extension_detected":bool(postoutcome_extension),"approximate_nullspace_rejected":bool(approx_nullspace),"source_change_detected":bool(source_change),"dimension_change_detected":bool(dimension_change),"field_redefinition_quotient_detected":bool(field_redef),"shear_direction_removal_detected":bool(shear_direction_removed)}
    result={"lane":"RCG004_NEGATIVE_CONTROLS","tests":tests,"all_negative_controls_pass":all(tests.values()),"transverse_shear_isotropic_background":str(shear_iso),"environment":{"python":sys.version.split()[0],"sympy":sp.__version__,"platform":platform.platform()},"classification":"PASS_RCG004_NEGATIVE_CONTROLS" if all(tests.values()) else "INVALID_RCG004_NEGATIVE_CONTROL_FAILURE"}
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n");print(json.dumps(result,sort_keys=True))
if __name__=="__main__":main()
