#!/usr/bin/env python3
import argparse, json, pathlib, os

REQ_KEYS=["R1_PARENT_FUNCTIONAL","R2_SOURCE_SPACE","R3_THIRD_VARIATION_LICENSE","R4_CANDIDATE_INDEPENDENCE","R5_DOMAIN","R6_TRANSFORMATION_RULE","R7_ORDERING_RULE"]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--constructor",required=True)
    ap.add_argument("--critic",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    c=json.load(open(a.constructor))
    k=json.load(open(a.critic))

    disagreements=[]
    for key in REQ_KEYS:
        if c["requirements"][key]!=k["requirements"][key]:
            disagreements.append({"field":key,"constructor":c["requirements"][key],"critic":k["requirements"][key]})
    for key in ("G89","RQIRCGSF_SUCCESSOR","RCG002_CPI1","SYNTHETIC_COMPLETE_OBJECT"):
        if c["controls"][key]!=k["controls"][key]:
            disagreements.append({"field":"control:"+key,"constructor":c["controls"][key],"critic":k["controls"][key]})

    provenance_ok=bool(c["provenance_ok"] and k["provenance_ok"])
    controls_ok=bool(c["controls_ok"] and k["controls_ok"])

    if not provenance_ok or not controls_ok:
        classification="INVALID_RCG009_IMPLEMENTATION_OR_PROVENANCE"
    elif disagreements:
        classification="BLOCKED_SCOPED_RCG009_SOURCE_OWNERSHIP_OR_DOMAIN_UNRESOLVED"
    elif c["requirements"]["R1_PARENT_FUNCTIONAL"]=="FAIL_MISSING_PARENT_FUNCTIONAL":
        classification="BLOCKED_SCOPED_RCG009_RQIR_PRINCIPLES_DO_NOT_DEFINE_REQUIRED_HIGHER_ORDER_OBJECT"
    elif c["classification"]==k["classification"]=="PASS_SCOPED_RCG009_UPSTREAM_HIGHER_ORDER_RQIR_OBJECT_SOURCE_DEFINED":
        classification="PASS_SCOPED_RCG009_UPSTREAM_HIGHER_ORDER_RQIR_OBJECT_SOURCE_DEFINED"
    else:
        classification="BLOCKED_SCOPED_RCG009_SOURCE_OWNERSHIP_OR_DOMAIN_UNRESOLVED"

    out={
      "phase":"RCG009_UPSTREAM_THIRD_VARIATION_AGGREGATE",
      "run_id":os.environ.get("GITHUB_RUN_ID","LOCAL"),
      "selected_family":c["selected_family"],
      "requirements":c["requirements"] if not disagreements else {},
      "constructor_critic_disagreements":disagreements,
      "provenance_ok":provenance_ok,
      "controls_ok":controls_ok,
      "controls":c["controls"],
      "source_object_defined":classification=="PASS_SCOPED_RCG009_UPSTREAM_HIGHER_ORDER_RQIR_OBJECT_SOURCE_DEFINED",
      "source_ownership":"NOT_ESTABLISHED_NO_OBJECT" if classification!="PASS_SCOPED_RCG009_UPSTREAM_HIGHER_ORDER_RQIR_OBJECT_SOURCE_DEFINED" else "RQIR_UPSTREAM",
      "source_domain":"NOT_ESTABLISHED_NO_OBJECT" if classification!="PASS_SCOPED_RCG009_UPSTREAM_HIGHER_ORDER_RQIR_OBJECT_SOURCE_DEFINED" else "FROZEN_RQIR_SOURCE_DOMAIN",
      "candidate_independence":"NOT_ESTABLISHED_NO_OBJECT" if classification!="PASS_SCOPED_RCG009_UPSTREAM_HIGHER_ORDER_RQIR_OBJECT_SOURCE_DEFINED" else "ESTABLISHED_SCOPED",
      "derivability_status":"BLOCKED_AT_PARENT_FUNCTIONAL_DEFINITION" if classification=="BLOCKED_SCOPED_RCG009_RQIR_PRINCIPLES_DO_NOT_DEFINE_REQUIRED_HIGHER_ORDER_OBJECT" else ("SOURCE_DEFINED_ONLY" if classification.startswith("PASS_SCOPED") else "UNRESOLVED"),
      "classification":classification,
      "value_derivation_authorized":False,
      "bridge_gate_authorized":False,
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
