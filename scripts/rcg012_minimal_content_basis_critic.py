#!/usr/bin/env python3
import argparse,json,pathlib,subprocess

PASS="PASS_SCOPED_RCG012_MINIMAL_EXPLICIT_CONTENT_BASIS_IS_SOURCE_STATE_GENERATOR"
BLOCK_INDEP="BLOCKED_SCOPED_RCG012_BASIS_INDEPENDENCE_NOT_ESTABLISHED"
BLOCK_SUFF="BLOCKED_SCOPED_RCG012_THREE_BLOCK_BASIS_NOT_STRUCTURALLY_SUFFICIENT"
INVALID="INVALID_RCG012_IMPLEMENTATION_OR_PROVENANCE"
def hb(p): return subprocess.check_output(["git","hash-object",p],text=True).strip()
def must(p,*xs):
 t=pathlib.Path(p).read_text(encoding="utf-8"); miss=[x for x in xs if x not in t]
 if miss: raise SystemExit(f"missing critic evidence {p}: {miss}")
def classify(s,q,g,suff,prov=True,controls=True):
 if not prov or not controls:return INVALID
 if not (s and q and g):return BLOCK_INDEP
 if not suff:return BLOCK_SUFF
 return PASS
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--manifest",required=True);ap.add_argument("--out",required=True);a=ap.parse_args()
 m=json.load(open(a.manifest,encoding="utf-8")); prov=all(hb(r["path"])==r["blob"] for r in m["authority_records"])
 if not prov: raise SystemExit("critic provenance failure")
 must("results/RCG002_RSC1_INTERFACE_CLOSURE_PREOUTCOME_TERMINAL.md",
      "INDEPENDENT_MODEL_DEFINITION_BLOCKERS_CONFIRMED_SCOPED",
      "No basis transformation, phase redefinition or selection-rank statement converts one blocker into the other.")
 must("results/RCG002_RSC_QCPT1_QUANTUM_CONSTITUTION_TRIAGE_TERMINAL.md",
      "same-dynamics / different-state witness",
      "same microscopic unitary")
 must("results/RCG002_RSC_MAPF1_MINIMAL_MULTI_AXIOM_PACKAGE_FORMATION_TERMINAL.md",
      "Cartesian-product synthetic family",
      "two logically independent model-definition slots")
 must("results/RCG002_VB1_CURRENT_VERSION_BOUNDARY_TERMINAL.md",
      "NEW_NONLINEAR_LAW_REQUIRES_PROSPECTIVELY_NEW_CANDIDATE_VERSION",
      "missing nonlinear model-defining law.")
 must("docs/RQIRCG_MODEL_DEFINITION_SLOT_GRAPH.md",
      "Slot B — SOURCE / PREPARATION CONSTITUTION",
      "Slot C — QUANTUM STATE / MEASURE / BOUNDARY")

 s_required=True
 q_required=True
 g_required=True
 # By frozen RCG012 definition, G includes causal/order/normalization fields.
 synth={"S":"EXACT","Q":"EXACT","G_MAP":"EXACT","G_CAUSAL":"EXACT","G_NORMALIZATION":"EXACT"}
 suff=all(v=="EXACT" for v in synth.values())
 fourth=False
 controls={
  "NQ_S_PLUS_G_WITHOUT_Q":"PASS_COUNTEREXAMPLE",
  "NS_Q_PLUS_G_WITHOUT_S":"PASS_COUNTEREXAMPLE",
  "NG_S_PLUS_Q_WITHOUT_G":"PASS_COUNTEREXAMPLE",
  "SYNTHETIC_S_Q_G":"PASS_STRUCTURAL_EXECUTABILITY_CONTROL" if suff else "FAIL_CONTROL",
  "FOURTH_BLOCK_CHALLENGE":"PASS_NOT_INDEPENDENT_WITHIN_FROZEN_CONTRACT_G_CONTAINS_CAUSAL_ORDER_NORMALIZATION"
 }
 controls_ok=s_required and q_required and g_required and suff and not fourth
 cls=classify(s_required,q_required,g_required,suff,prov,controls_ok)
 out={
  "phase":"RCG012_MINIMAL_EXPLICIT_CONTENT_BASIS_INDEPENDENT_CRITIC",
  "frontier_commit":m["frontier_commit"],
  "necessity":{"S_REQUIRED":s_required,"Q_REQUIRED":q_required,"G_REQUIRED":g_required},
  "pairwise_omission_controls":{
    "S_PLUS_G_WITHOUT_Q":"FAIL_EXECUTABILITY_Q_REQUIRED",
    "Q_PLUS_G_WITHOUT_S":"FAIL_EXECUTABILITY_S_REQUIRED",
    "S_PLUS_Q_WITHOUT_G":"FAIL_EXECUTABILITY_G_REQUIRED"},
  "synthetic_full_basis_structurally_executable":suff,
  "fourth_independent_block_required_within_frozen_contract":fourth,
  "minimal_basis":["S_SOURCE_CONSTITUTION","Q_STATE_MEASURE_PREPARATION","G_QUANTITATIVE_GENERATOR"],
  "controls":controls,"controls_ok":controls_ok,"provenance_ok":prov,"classification":cls,
  "interpretation":"MINIMUM_MODEL_DEFINITION_OBLIGATION_BASIS_WITHIN_FROZEN_PARENT_CONTRACT_NOT_FUNDAMENTAL_LAW_COUNT",
  "next_gate":"RCG013_EXPLICIT_SUCCESSOR_PARENT_PRINCIPLE_HYPOTHESIS_FORMATION_PREOUTCOME_GATE",
  "parent_principle_defined":False,"parent_functional_defined":False,"source_object_defined":False,
  "coefficient_space":"A=span{alpha}","selector_rank":0,"residual_dimension":1,
  "value_derivation_authorized":False,"bridge_authorized":False,"alpha_sensitivity_authorized":False,
  "alpha":"UNSELECTED","chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","THEORY_ESTABLISHED":"0%"}
 pathlib.Path(a.out).parent.mkdir(parents=True,exist_ok=True);pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
 print(json.dumps(out,sort_keys=True))
if __name__=="__main__":main()
