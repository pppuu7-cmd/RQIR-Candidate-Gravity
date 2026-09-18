#!/usr/bin/env python3
import argparse,json,pathlib,os
PASS="PASS_SCOPED_RCG011_NEW_PARENT_PRINCIPLE_FAMILY_SELECTED_PREOUTCOME"
BLOCK_HIDDEN="BLOCKED_SCOPED_RCG011_FORMED_FAMILIES_LEAVE_HIDDEN_MODEL_DATA"
BLOCK_SELECT="BLOCKED_SCOPED_RCG011_NO_PREOUTCOME_PARENT_PRINCIPLE_FAMILY_SELECTED"
INVALID="INVALID_RCG011_IMPLEMENTATION_OR_PROVENANCE"
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--constructor",required=True);ap.add_argument("--critic",required=True);ap.add_argument("--out",required=True);a=ap.parse_args()
 c=json.load(open(a.constructor));k=json.load(open(a.critic))
 disagreements=[]
 for fam in sorted(set(c["family_rows"])|set(k["family_rows"])):
  for field in sorted(set(c["family_rows"].get(fam,{ }))|set(k["family_rows"].get(fam,{ }))):
   cv=c["family_rows"].get(fam,{}).get(field); kv=k["family_rows"].get(fam,{}).get(field)
   if cv!=kv: disagreements.append({"family":fam,"field":field,"constructor":cv,"critic":kv})
 prov=bool(c["provenance_ok"] and k["provenance_ok"]);controls=bool(c["controls_ok"] and k["controls_ok"])
 if not prov or not controls: cls=INVALID
 elif disagreements: cls=BLOCK_SELECT
 elif c["classification"]==k["classification"]: cls=c["classification"]
 else: cls=BLOCK_SELECT
 elig=c["structurally_eligible_families"] if not disagreements else []
 out={"phase":"RCG011_NEW_PARENT_PRINCIPLE_FAMILY_AGGREGATE","run_id":os.environ.get("GITHUB_RUN_ID","LOCAL"),
 "classification":cls,"constructor_critic_disagreements":disagreements,"provenance_ok":prov,"controls_ok":controls,
 "family_rows":c["family_rows"] if not disagreements else {},"structurally_eligible_families":elig,
 "selected_families":c["selected_families"] if not disagreements else [],
 "new_scientific_fact":"ALL_FROZEN_NEW_PARENT_PRINCIPLE_FAMILIES_RETAIN_HIDDEN_MODEL_CONTENT_BEFORE_SELECTION" if cls==BLOCK_HIDDEN else "UNRESOLVED",
 "residual_blocker":"EXACT_NEW_SOURCE_STATE_GENERATING_CONTENT_MUST_BE_PROSPECTIVELY_SPECIFIED",
 "parent_principle_defined":cls==PASS,"parent_functional_defined":False,"source_object_defined":False,
 "coefficient_space":"A=span{alpha}","selector_rank":0,"residual_dimension":1,
 "value_derivation_authorized":False,"bridge_authorized":False,"alpha_sensitivity_authorized":False,
 "alpha":"UNSELECTED","chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","THEORY_ESTABLISHED":"0%"}
 pathlib.Path(a.out).parent.mkdir(parents=True,exist_ok=True);pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
 print(json.dumps(out,sort_keys=True))
if __name__=="__main__":main()
