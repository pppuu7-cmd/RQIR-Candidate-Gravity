#!/usr/bin/env python3
import argparse, json, pathlib, os

KEYS=["PERTURBATIVE_ORDER","RQIR_OWNERSHIP","CANDIDATE_INDEPENDENCE","DOMAIN","OBSERVABLE_TYPE",
"GRAVITY_APPLICABILITY","BRIDGE_PRESENT","PROVENANCE_STATUS","SYNTHETIC_STATUS","QUALIFIES",
"REJECTION_REASON","CENSUS_STATUS"]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",required=True); ap.add_argument("--constructor",required=True)
    ap.add_argument("--critic",required=True); ap.add_argument("--out",required=True)
    a=ap.parse_args()
    m=json.load(open(a.manifest)); c=json.load(open(a.constructor)); k=json.load(open(a.critic))
    exp=m["mandatory_controls"]; disagreements=[]
    ci={r["OBJECT_ID"]:r for r in c["inventory"]}; ki={r["OBJECT_ID"]:r for r in k["inventory"]}
    ids=[o["id"] for o in m["objects"]]
    if sorted(ci)!=sorted(ids) or sorted(ki)!=sorted(ids): raise SystemExit("inventory coverage mismatch")
    for oid in ids:
        for f in KEYS:
            if ci[oid][f]!=ki[oid][f]: disagreements.append({"object":oid,"field":f,"constructor":ci[oid][f],"critic":ki[oid][f]})
    controls_ok=(c["controls"]==exp and k["controls"]==exp)
    provenance_ok=bool(c["corpus_valid"] and k["corpus_valid"] and all(ci[x]["PROVENANCE_STATUS"]=="EXACT" for x in ids))
    q=[x for x in ids if ci[x]["QUALIFIES"]]
    if not provenance_ok or not controls_ok:
        classification="INVALID_RCG008_CENSUS_COVERAGE_OR_PROVENANCE"
    elif disagreements:
        classification="BLOCKED_RCG008_AMBIGUOUS_SOURCE_OWNERSHIP_OR_DOMAIN"
    elif q:
        classification="PASS_SCOPED_RCG008_EXISTING_APPLICABLE_HIGHER_ORDER_RQIR_DATUM_FOUND"
    else:
        classification="BLOCKED_SCOPED_RCG008_NO_EXISTING_APPLICABLE_HIGHER_ORDER_RQIR_DATUM_IN_CURRENT_AUTHORITY"
    reasons=[ci[x]["REJECTION_REASON"] for x in ids]
    out={
      "phase":"RCG008_AGGREGATE","run_id":os.environ.get("GITHUB_RUN_ID","LOCAL"),
      "authority_base_commit":m["authority_base_commit"],"controls_ok":controls_ok,
      "provenance_ok":provenance_ok,"constructor_critic_disagreements":disagreements,
      "candidate_object_count":len(ids),"qualifying_datum_count":len(q),
      "qualifying_objects":q,
      "rejected_candidate_owned_count":sum(r=="CANDIDATE_OWNED" for r in reasons),
      "rejected_too_low_order_count":sum(r=="TOO_LOW_ORDER" for r in reasons),
      "rejected_domain_count":sum(r=="DOMAIN_SPECIFIC_UNBRIDGED" for r in reasons),
      "rejected_unbridged_count":sum(r=="DOMAIN_SPECIFIC_UNBRIDGED" for r in reasons),
      "G88_control_status":ci["G88"]["CENSUS_STATUS"],
      "G89_control_status":ci["G89"]["CENSUS_STATUS"],
      "synthetic_control_status":ci["RCG007_SYNTHETIC_CUBIC_CONTROL"]["CENSUS_STATUS"],
      "classification":classification,
      "bridge_authorized": bool(classification.startswith("PASS_SCOPED_")),
      "coefficient_space":"A=span{alpha}","alpha_status":"UNSELECTED",
      "selector_rank_before":0,"selector_rank_after_rcg008":0,
      "chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","THEORY_ESTABLISHED":"0%",
      "inventory":c["inventory"]
    }
    pathlib.Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,sort_keys=True))
if __name__=="__main__": main()
