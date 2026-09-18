#!/usr/bin/env python3
import argparse, json, pathlib, subprocess, os

def hb(p): return subprocess.check_output(["git","hash-object",p],text=True).strip()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--manifest",required=True); ap.add_argument("--aggregate",required=True); ap.add_argument("--out",required=True); a=ap.parse_args()
    m=json.load(open(a.manifest)); g=json.load(open(a.aggregate))
    # Auditor reconstructs the decisive frontier directly from durable source records, not from Constructor logic.
    decisive={
      "G88":("results/ITER086_G88_C_INHERITED_CONSTRAINT_SELECTION_SUFFICIENCY_TERMINAL.md","lower-order Ward/CTP constraints","FOUND_BUT_TOO_LOW_ORDER_FOR_ALPHA"),
      "G89":("results/ITER087_G89_D_INHERITED_CONSTRAINT_SELECTION_SUFFICIENCY_TERMINAL.md","D_FROZEN_RETARDED_CUBIC_SECTOR_COEFFICIENT_BLIND_SCOPED","FOUND_BUT_D_SPECIFIC_UNBRIDGED"),
      "G93":("results/ITER091_G93_C_CONNECTED_THREE_SOURCE_PHASE_SELECTOR_TERMINAL.md","BLOCKED_MISSING_CANDIDATE_OWNED_DATUM","REJECT_CANDIDATE_OWNED"),
      "G94":("results/ITER092_G94_D_NATIVE_THREE_SOURCE_PHASE_BRIDGE_TERMINAL.md","UNDEFINED_NATIVE_BRIDGE_INCOMPLETE","REJECT_D_SPECIFIC_UNBRIDGED"),
      "RCG007_SYNTHETIC_CUBIC_CONTROL":("results/RCG007_WEYL3_INHERITED_RQIR_SELECTION_RANK_TERMINAL.md","genuinely cubic synthetic selector","FOUND_BUT_SYNTHETIC_CONTROL")
    }
    byid={o["id"]:o for o in m["objects"]}; checks={}
    for oid,(p,anchor,expect) in decisive.items():
        if hb(p)!=byid[oid]["blob"]: raise SystemExit("auditor blob mismatch "+oid)
        txt=pathlib.Path(p).read_text()
        if anchor not in txt: raise SystemExit("auditor anchor missing "+oid)
        checks[oid]=expect
    expected_class="BLOCKED_SCOPED_RCG008_NO_EXISTING_APPLICABLE_HIGHER_ORDER_RQIR_DATUM_IN_CURRENT_AUTHORITY"
    confirmed=(g["classification"]==expected_class and g["qualifying_datum_count"]==0 and g["controls_ok"] and g["provenance_ok"]
               and g["G88_control_status"]=="FOUND_BUT_TOO_LOW_ORDER_FOR_ALPHA"
               and g["G89_control_status"]=="FOUND_BUT_D_SPECIFIC_UNBRIDGED"
               and g["synthetic_control_status"]=="FOUND_BUT_SYNTHETIC_CONTROL"
               and g["alpha_status"]=="UNSELECTED" and g["chi_ABC"]=="UNAUTHORIZED_NOT_COMPUTED")
    out={"phase":"RCG008_INDEPENDENT_SELECTOR_AUDITOR","run_id":os.environ.get("GITHUB_RUN_ID","LOCAL"),
         "verdict":"CONFIRMED_SCOPED" if confirmed else "NOT_CONFIRMED",
         "aggregate_classification":g["classification"],"decisive_reconstruction":checks,
         "qualifying_datum_count":g["qualifying_datum_count"],"alpha_status":"UNSELECTED",
         "chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","THEORY_ESTABLISHED":"0%"}
    pathlib.Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,sort_keys=True))
    if not confirmed: raise SystemExit(2)
if __name__=="__main__": main()
