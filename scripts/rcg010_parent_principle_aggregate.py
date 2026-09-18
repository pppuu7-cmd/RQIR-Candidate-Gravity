#!/usr/bin/env python3
import argparse, json, pathlib, os

SOURCE_DEFINED="SOURCE_DEFINED_SCOPED_RCG010_PARENT_SOURCE_PRINCIPLE_DERIVED_FROM_EXISTING_RQIR_AUTHORITY"
BLOCKED_UNDER="BLOCKED_SCOPED_RCG010_EXISTING_RQIR_PRINCIPLES_UNDERDETERMINE_PARENT_SOURCE_PRINCIPLE"
BLOCKED_FIELDS="BLOCKED_SCOPED_RCG010_SOURCE_SPACE_DOMAIN_OR_TRANSFORMATION_LAW_UNRESOLVED"
INVALID="INVALID_RCG010_IMPLEMENTATION_OR_PROVENANCE"

REQ_KEYS=[
 "R1_PARENT_PRINCIPLE_OR_DERIVATION_RULE","R2_SOURCE_SPACE","R3_DOMAIN",
 "R4_TRANSFORMATION_OR_EQUIVALENCE_LAW","R5_CAUSAL_OR_ORDERING_RULE",
 "R6_NORMALIZATION_OR_EQUIVALENCE_CLASS","R7_GENERATING_OR_RESPONSE_RULE",
 "R8_CANDIDATE_INDEPENDENCE","R9_SUCCESSOR_FIREWALL","R10_PREOUTCOME_SELECTION"
]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--constructor",required=True)
    ap.add_argument("--critic",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    c=json.load(open(a.constructor,encoding="utf-8"))
    k=json.load(open(a.critic,encoding="utf-8"))

    disagreements=[]
    for key in REQ_KEYS:
        if c["requirements"][key]!=k["requirements"][key]:
            disagreements.append({"field":key,"constructor":c["requirements"][key],"critic":k["requirements"][key]})
    for key in sorted(set(c["controls"])|set(k["controls"])):
        if c["controls"].get(key)!=k["controls"].get(key):
            disagreements.append({"field":"control:"+key,"constructor":c["controls"].get(key),"critic":k["controls"].get(key)})

    provenance_ok=bool(c["provenance_ok"] and k["provenance_ok"])
    controls_ok=bool(c["controls_ok"] and k["controls_ok"])
    if not provenance_ok or not controls_ok:
        classification=INVALID
    elif disagreements:
        classification=BLOCKED_FIELDS
    elif c["requirements"]["R1_PARENT_PRINCIPLE_OR_DERIVATION_RULE"]=="FAIL_UNDERDETERMINED":
        classification=BLOCKED_UNDER
    elif c["classification"]==k["classification"]==SOURCE_DEFINED:
        classification=SOURCE_DEFINED
    else:
        classification=BLOCKED_FIELDS

    source_defined=(classification==SOURCE_DEFINED)
    out={
      "phase":"RCG010_PARENT_SOURCE_PRINCIPLE_AGGREGATE",
      "run_id":os.environ.get("GITHUB_RUN_ID","LOCAL"),
      "requirements":c["requirements"] if not disagreements else {},
      "constructor_critic_disagreements":disagreements,
      "provenance_ok":provenance_ok,
      "controls_ok":controls_ok,
      "controls":c["controls"],
      "parent_principle_defined":source_defined,
      "parent_functional_defined":False,
      "source_object_defined":False,
      "source_space_status":"SOURCE_PRINCIPLE_DEFINED_SCOPED" if source_defined else "NOT_DEFINED_PARENT_PRINCIPLE_UNDERDETERMINED",
      "domain_status":"SOURCE_PRINCIPLE_DEFINED_SCOPED" if source_defined else "NOT_DEFINED_PARENT_PRINCIPLE_UNDERDETERMINED",
      "transformation_law_status":"SOURCE_PRINCIPLE_DEFINED_SCOPED" if source_defined else "NOT_DEFINED_PARENT_PRINCIPLE_UNDERDETERMINED",
      "candidate_independence":"ESTABLISHED_SCOPED" if source_defined else "NOT_ESTABLISHED_NO_PARENT_PRINCIPLE",
      "derivability_status":"SOURCE_PRINCIPLE_DEFINED_ONLY_STOP" if source_defined else ("BLOCKED_EXISTING_PRINCIPLES_UNDERDETERMINE_PARENT_SOURCE_PRINCIPLE" if classification==BLOCKED_UNDER else "UNRESOLVED"),
      "current_blocker":"NONE_AT_PRINCIPLE_LEVEL" if source_defined else ("EXISTING_RQIR_PRINCIPLES_UNDERDETERMINE_PARENT_SOURCE_PRINCIPLE" if classification==BLOCKED_UNDER else "SOURCE_SPACE_DOMAIN_OR_TRANSFORMATION_LAW_UNRESOLVED"),
      "classification":classification,
      "coefficient_space":"A=span{alpha}",
      "selector_rank":0,
      "residual_dimension":1,
      "value_derivation_authorized":False,
      "bridge_authorized":False,
      "alpha_sensitivity_authorized":False,
      "alpha":"UNSELECTED",
      "chi_ABC":"UNAUTHORIZED_NOT_COMPUTED",
      "THEORY_ESTABLISHED":"0%"
    }
    pathlib.Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(out,sort_keys=True))
if __name__=="__main__":
    main()
