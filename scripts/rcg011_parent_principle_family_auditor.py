#!/usr/bin/env python3
import argparse,json,pathlib,subprocess,os
BLOCK_HIDDEN="BLOCKED_SCOPED_RCG011_FORMED_FAMILIES_LEAVE_HIDDEN_MODEL_DATA"
INVALID="INVALID_RCG011_IMPLEMENTATION_OR_PROVENANCE"
def hb(p): return subprocess.check_output(["git","hash-object",p],text=True).strip()
def has(p,s): return s in pathlib.Path(p).read_text(encoding="utf-8")
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--manifest",required=True);ap.add_argument("--aggregate",required=True);ap.add_argument("--out",required=True);a=ap.parse_args()
 m=json.load(open(a.manifest));g=json.load(open(a.aggregate))
 prov=all(hb(r["path"])==r["blob"] for r in m["authority_records"])
 source_block=has("results/RCG002_RSC_CSA1_CLOSED_SOURCE_ACTION_PROPOSAL_TERMINAL.md","candidate-owned source constitution") and has("results/RCG002_RSC_SCPT1_SOURCE_CONSTITUTION_TRIAGE_TERMINAL.md","NO_PREOUTCOME_SOURCE_CONSTITUTION_SELECTED")
 quantum_block=has("results/RCG002_RSC_QCPT1_QUANTUM_CONSTITUTION_TRIAGE_TERMINAL.md","NO_PREOUTCOME_QUANTUM_CONSTITUTION_SELECTED")
 schema_block=has("results/RCG002_RSC_MAPF1_MINIMAL_MULTI_AXIOM_PACKAGE_FORMATION_TERMINAL.md","RSC_PACKAGE_SCHEMA_ONLY_MODEL_DEFINITION_INCOMPLETE")
 anchor_block=has("results/RCG002_RSC_AB1_NEW_AXIOM_ANCHOR_BUDGET_TERMINAL.md","STRUCTURAL_ANCHOR != MODEL_DEFINITION_SELECTOR")
 premise_block=has("results/RCG002_RSC_S2PA1_SPIN2_CONSISTENCY_PREMISE_AUTHORITY_TERMINAL.md","NO_SPIN2_CONSISTENCY_PREMISE_CLASS_FORCED_BY_CURRENT_RQIRCG_SCOPED")
 controls=source_block and quantum_block and schema_block and anchor_block and premise_block
 independent=INVALID if (not prov or not controls) else BLOCK_HIDDEN
 confirmed=(g["classification"]==independent and g["structurally_eligible_families"]==[] and g["constructor_critic_disagreements"]==[] and g["parent_principle_defined"] is False and g["parent_functional_defined"] is False and g["source_object_defined"] is False and g["selector_rank"]==0 and g["alpha"]=="UNSELECTED" and g["chi_ABC"]=="UNAUTHORIZED_NOT_COMPUTED")
 out={"phase":"RCG011_NEW_PARENT_PRINCIPLE_FAMILY_INDEPENDENT_SELECTOR_AUDITOR","run_id":os.environ.get("GITHUB_RUN_ID","LOCAL"),
 "verdict":"CONFIRMED_SCOPED" if confirmed else "NOT_CONFIRMED","independent_classification":independent,"aggregate_classification":g["classification"],
 "provenance_ok":prov,"controls_ok":controls,"structurally_eligible_families":[],
 "residual_blocker":"EXACT_NEW_SOURCE_STATE_GENERATING_CONTENT_MUST_BE_PROSPECTIVELY_SPECIFIED",
 "parent_principle_defined":False,"parent_functional_defined":False,"source_object_defined":False,
 "value_derivation_authorized":False,"bridge_authorized":False,"alpha_sensitivity_authorized":False,
 "alpha":"UNSELECTED","chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","THEORY_ESTABLISHED":"0%"}
 pathlib.Path(a.out).parent.mkdir(parents=True,exist_ok=True);pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
 print(json.dumps(out,sort_keys=True))
 if not confirmed: raise SystemExit(2)
if __name__=="__main__":main()
