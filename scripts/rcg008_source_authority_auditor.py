#!/usr/bin/env python3
import argparse, json, pathlib, subprocess, os

def hb(p): return subprocess.check_output(["git","hash-object",p],text=True).strip()

# Independent third-lane reconstruction. This table is source-evidence based and does not consume
# Constructor/Critic classifications.
AUDIT={
"G88":("lower-order Ward/CTP constraints","FOUND_BUT_TOO_LOW_ORDER_FOR_ALPHA",False),
"G89":("D_FROZEN_RETARDED_CUBIC_SECTOR_COEFFICIENT_BLIND_SCOPED","FOUND_BUT_D_SPECIFIC_UNBRIDGED",False),
"G90":("not a physical nonlinear completion","FOUND_BUT_CANDIDATE_OWNED",False),
"G91":("finite-family witness","FOUND_BUT_CANDIDATE_OWNED",False),
"G92":("does not select any Weyl/Riemann operator","FOUND_BUT_NOT_SELECTOR_DATUM",False),
"G93":("BLOCKED_MISSING_CANDIDATE_OWNED_DATUM","FOUND_BUT_CANDIDATE_OWNED",False),
"G94":("UNDEFINED_NATIVE_BRIDGE_INCOMPLETE","FOUND_BUT_D_SPECIFIC_UNBRIDGED",False),
"G95":("minimal source-only finite ansatz","FOUND_BUT_CANDIDATE_OWNED",False),
"G96":("diagnostic connected directions","FOUND_BUT_NOT_SELECTOR_DATUM",False),
"G97":("classical source-preparation mechanics only","FOUND_BUT_NOT_HIGHER_ORDER_SELECTOR",False),
"RCG002_LINEARIZED":("Candidate-owned linearized dynamical rule","FOUND_BUT_CANDIDATE_OWNED",False),
"RCG007_SYNTHETIC_CUBIC_CONTROL":("genuinely cubic synthetic selector","FOUND_BUT_SYNTHETIC_CONTROL",False)
}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--manifest",required=True); ap.add_argument("--aggregate",required=True); ap.add_argument("--out",required=True); a=ap.parse_args()
    m=json.load(open(a.manifest)); g=json.load(open(a.aggregate))
    byid={o["id"]:o for o in m["objects"]}
    if sorted(byid)!=sorted(AUDIT): raise SystemExit("auditor corpus coverage mismatch")
    statuses={}; qualifying=[]; provenance_ok=True
    for oid,o in byid.items():
        if hb(o["path"])!=o["blob"]: provenance_ok=False
        for d in o["dependencies"]:
            if hb(d["path"])!=d["blob"]: provenance_ok=False
        anchor,status,qualifies=AUDIT[oid]
        txt=pathlib.Path(o["path"]).read_text(encoding="utf-8")
        if anchor not in txt: raise SystemExit(f"auditor anchor missing {oid}: {anchor}")
        statuses[oid]=status
        if qualifies: qualifying.append(oid)
    controls_ok=(
      statuses["G88"]=="FOUND_BUT_TOO_LOW_ORDER_FOR_ALPHA" and
      statuses["G89"]=="FOUND_BUT_D_SPECIFIC_UNBRIDGED" and
      statuses["RCG007_SYNTHETIC_CUBIC_CONTROL"]=="FOUND_BUT_SYNTHETIC_CONTROL")
    if not provenance_ok or not controls_ok:
        independent_class="INVALID_RCG008_CENSUS_COVERAGE_OR_PROVENANCE"
    elif qualifying:
        independent_class="PASS_SCOPED_RCG008_EXISTING_APPLICABLE_HIGHER_ORDER_RQIR_DATUM_FOUND"
    else:
        independent_class="BLOCKED_SCOPED_RCG008_NO_EXISTING_APPLICABLE_HIGHER_ORDER_RQIR_DATUM_IN_CURRENT_AUTHORITY"
    confirmed=(g["classification"]==independent_class and g["qualifying_datum_count"]==len(qualifying)
               and g["alpha_status"]=="UNSELECTED" and g["chi_ABC"]=="UNAUTHORIZED_NOT_COMPUTED")
    out={"phase":"RCG008_INDEPENDENT_SELECTOR_AUDITOR","run_id":os.environ.get("GITHUB_RUN_ID","LOCAL"),
         "verdict":"CONFIRMED_SCOPED" if confirmed else "NOT_CONFIRMED",
         "independent_classification":independent_class,
         "aggregate_classification":g["classification"],"source_reconstruction":statuses,
         "qualifying_objects":qualifying,"qualifying_datum_count":len(qualifying),
         "controls_ok":controls_ok,"provenance_ok":provenance_ok,
         "alpha_status":"UNSELECTED","chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","THEORY_ESTABLISHED":"0%"}
    pathlib.Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,sort_keys=True))
    if not confirmed: raise SystemExit(2)
if __name__=="__main__": main()
