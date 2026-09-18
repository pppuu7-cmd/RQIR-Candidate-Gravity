#!/usr/bin/env python3
import argparse,json,pathlib,os
PASS="PASS_SCOPED_RCG012_MINIMAL_EXPLICIT_CONTENT_BASIS_IS_SOURCE_STATE_GENERATOR"
BLOCK_INDEP="BLOCKED_SCOPED_RCG012_BASIS_INDEPENDENCE_NOT_ESTABLISHED"
BLOCK_SUFF="BLOCKED_SCOPED_RCG012_THREE_BLOCK_BASIS_NOT_STRUCTURALLY_SUFFICIENT"
INVALID="INVALID_RCG012_IMPLEMENTATION_OR_PROVENANCE"
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--constructor",required=True);ap.add_argument("--critic",required=True);ap.add_argument("--out",required=True);a=ap.parse_args()
 c=json.load(open(a.constructor));k=json.load(open(a.critic))
 fields=["necessity","pairwise_omission_controls","synthetic_full_basis_structurally_executable","fourth_independent_block_required_within_frozen_contract","minimal_basis"]
 disagreements=[]
 for f in fields:
  if c[f]!=k[f]: disagreements.append({"field":f,"constructor":c[f],"critic":k[f]})
 prov=c["provenance_ok"] and k["provenance_ok"]; controls=c["controls_ok"] and k["controls_ok"]
 if not prov or not controls: cls=INVALID
 elif disagreements: cls=BLOCK_INDEP
 elif c["classification"]==k["classification"]: cls=c["classification"]
 else: cls=BLOCK_INDEP
 out={"phase":"RCG012_MINIMAL_EXPLICIT_CONTENT_BASIS_AGGREGATE","run_id":os.environ.get("GITHUB_RUN_ID","LOCAL"),
 "classification":cls,"constructor_critic_disagreements":disagreements,"provenance_ok":bool(prov),"controls_ok":bool(controls),
 "necessity":c["necessity"] if not disagreements else {},"pairwise_omission_controls":c["pairwise_omission_controls"] if not disagreements else {},
 "synthetic_full_basis_structurally_executable":c["synthetic_full_basis_structurally_executable"],
 "fourth_independent_block_required_within_frozen_contract":c["fourth_independent_block_required_within_frozen_contract"],
 "minimal_basis":c["minimal_basis"] if cls==PASS else [],
 "interpretation":"MINIMUM_MODEL_DEFINITION_OBLIGATION_BASIS_WITHIN_FROZEN_PARENT_CONTRACT_NOT_FUNDAMENTAL_LAW_COUNT",
 "next_gate":"RCG013_EXPLICIT_SUCCESSOR_PARENT_PRINCIPLE_HYPOTHESIS_FORMATION_PREOUTCOME_GATE" if cls==PASS else "UNRESOLVED",
 "parent_principle_defined":False,"parent_functional_defined":False,"source_object_defined":False,
 "coefficient_space":"A=span{alpha}","selector_rank":0,"residual_dimension":1,
 "value_derivation_authorized":False,"bridge_authorized":False,"alpha_sensitivity_authorized":False,
 "alpha":"UNSELECTED","chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","THEORY_ESTABLISHED":"0%"}
 pathlib.Path(a.out).parent.mkdir(parents=True,exist_ok=True);pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
 print(json.dumps(out,sort_keys=True))
if __name__=="__main__":main()
