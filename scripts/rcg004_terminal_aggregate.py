#!/usr/bin/env python3
"""Frozen aggregate/classifier for RCG004 complete cubic-curvature primary gate."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
PREREG="345213253f2ecf415af40cb4fbae47b4f58d8870";HELDOUT="5f83a594309429b45a8edd1bdc72b9653fffdc75";AUTH="28781bc1873413b214f751eaa963cf1c51423e0b";PARENT="72f9ab2ab5ad85259a18fc1f368777c431a56324"
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--constructor",required=True);ap.add_argument("--critic",required=True);ap.add_argument("--euler",required=True);ap.add_argument("--negative",required=True);ap.add_argument("--output",required=True);ap.add_argument("--run-head",default="");args=ap.parse_args()
    C=json.loads(Path(args.constructor).read_text());K=json.loads(Path(args.critic).read_text());E=json.loads(Path(args.euler).read_text());N=json.loads(Path(args.negative).read_text())
    predicates={
      "authority_exact":C.get("authority_terminal")==AUTH==K.get("authority_terminal")==E.get("authority_terminal"),
      "prereg_exact":C.get("prereg_sha")==PREREG==K.get("prereg_sha")==E.get("prereg_sha"),
      "heldout_frozen_before_outcome":C.get("heldout_prereg_sha")==HELDOUT==K.get("heldout_prereg_sha")==E.get("heldout_prereg_sha"),
      "parent_exact":C.get("parent_terminal")==PARENT==K.get("parent_terminal"),
      "run_head_exact":C.get("run_head")==args.run_head==K.get("run_head")==E.get("run_head"),
      "source_lock":C.get("source")=="VACUUM_ZERO"==K.get("source"),
      "field_redefinition_firewall":C.get("field_redefinition_equivalence")=="OUT_OF_SCOPE_RCG004_V0"==K.get("field_redefinition_equivalence"),
      "complete_raw_enumeration_agrees":C.get("raw_contraction_count")==10395==K.get("raw_contraction_count") and C.get("canonical_nonzero_class_count")==13==K.get("canonical_nonzero_class_count") and C.get("canonical_zero_class_count")==20==K.get("canonical_zero_class_count"),
      "canonical_class_manifests_agree":C.get("canonical_nonzero_classes")==K.get("canonical_nonzero_classes"),
      "constructor_exact_4d_quotient":C.get("universal_generic_curvature_dimension")==20 and C.get("quotient_dimension")==6 and C.get("relation_nullity")==7,
      "critic_independent_exact_4d_quotient":K.get("constructor_not_imported") is True and K.get("generic_curvature_dimension")==20 and K.get("selfdual_bianchi_exact") is True and K.get("quotient_dimension")==6,
      "independent_bases_not_forced_identical":C.get("quotient_pivot_class_indices")!=K.get("critic_basis_class_indices"),
      "metric_derivations_valid":C.get("metric_to_compact_orthonormal_riemann_verified") is True and K.get("metric_to_compact_orthonormal_riemann_verified") is True and E.get("metric_to_compact_orthonormal_riemann_verified") is True,
      "rcg003_embedding_rank_three":C.get("rcg003_embedding_rank")==3,
      "rcg003_regression_exact":C.get("rcg003_axisymmetric_obstruction_exact_match") is True,
      "constructor_primary_rank_full":C.get("primary_hessian_columns")==6 and C.get("primary_hessian_rank")==6 and C.get("primary_hessian_nullity")==0,
      "critic_primary_rank_full":K.get("primary_hessian_columns")==6 and K.get("primary_hessian_rank")==6 and K.get("primary_hessian_nullity")==0,
      "euler_full_nullity_zero":E.get("basis_dimension")==6 and E.get("high_derivative_rank")==6 and E.get("high_derivative_nullity")==0 and E.get("fourth_derivative_rank")==6,
      "euler_hessian_correspondence":E.get("fourth_hessian_correspondence") is True,
      "constructor_controls_valid":C.get("controls_valid") is True,
      "critic_controls_valid":K.get("controls_valid") is True and K.get("classification")=="PASS_INDEPENDENT_CRITIC_RCG004_COMPLETENESS_AND_PRIMARY_NULLITY_ZERO",
      "negative_controls_valid":N.get("all_negative_controls_pass") is True and N.get("classification")=="PASS_RCG004_NEGATIVE_CONTROLS",
      "heldout_not_applicable_only_because_primary_zero":C.get("heldout_status")=="NOT_APPLICABLE_PRIMARY_NULLITY_ZERO"
    }
    valid=all(predicates.values())
    if valid:
      classification="FAIL_SCOPED_RCG004_COMPLETE_PARITY_EVEN_ALGEBRAIC_CUBIC_CURVATURE_CLASS_HAS_NO_NONZERO_TRIAXIAL_SECOND_ORDER_SURVIVOR"
    else: classification="INVALID_RCG004"
    result={"gate":"RCG004_COMPLETE_PARITY_EVEN_ALGEBRAIC_CUBIC_CURVATURE_FAMILY_V0_TERMINAL_AGGREGATE","run_head":args.run_head,"aggregate_valid":valid,"predicates":predicates,"classification":classification,"dimension_chain":{"raw_matchings":C.get("raw_contraction_count"),"nonzero_symmetry_classes":C.get("canonical_nonzero_class_count"),"exact_4d_quotient_dimension":C.get("quotient_dimension"),"triaxial_hessian_survivor_dimension":C.get("primary_hessian_nullity"),"hessian_plus_curl_survivor_dimension":0 if C.get("primary_hessian_nullity")==0 else None,"direct_euler_verified_survivor_dimension":E.get("high_derivative_nullity"),"heldout_survivor_dimension":0 if C.get("primary_hessian_nullity")==0 else None},"heldout_status":"NOT_APPLICABLE_PRIMARY_NULLITY_ZERO" if C.get("primary_hessian_nullity")==0 else "REQUIRED","constructor_payload_sha256":C.get("scientific_payload_sha256"),"critic_payload_sha256":K.get("scientific_payload_sha256"),"euler_payload_sha256":E.get("scientific_payload_sha256"),"negative_controls":N.get("tests"),"claim_locks":{"scope":"COMPLETE_BOUNDED_4D_PARITY_EVEN_ALGEBRAIC_CURVATURE_CUBIC_V0_ONLY","all_cubic_gravity_fails":False,"all_higher_curvature_gravity_fails":False,"GR_unique":False,"chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","theory_established":"0%","ghost_free":False,"stable":False,"hyperbolic":False,"unitary":False,"quantum_gravity":False,"new_physics":False}}
    result["scientific_payload_sha256"]=sha(result);Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n");print(json.dumps({"aggregate_valid":valid,"classification":classification,"dimension_chain":result["dimension_chain"],"failed_predicates":[k for k,v in predicates.items() if not v]},sort_keys=True))
if __name__=="__main__":main()
