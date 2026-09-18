#!/usr/bin/env python3
import argparse, json, pathlib, subprocess

def gh_blob(p):
    return subprocess.check_output(["git","hash-object",p],text=True).strip()

# Independent reconstruction: evidence anchors and decisions are intentionally encoded here,
# not imported from the Constructor.
DECISIONS={
"G88":("lower-order Ward/CTP constraints","LOWER_THAN_CUBIC_INHERITED","INHERITED_RQIR","YES","C_INHERITED","LOWER_ORDER_CONSTRAINT_SET","NO_DIRECT_WEYL3_SENSITIVITY","NO","NO","TOO_LOW_ORDER","FOUND_BUT_TOO_LOW_ORDER_FOR_ALPHA"),
"G89":("cubic/retarded/CTP constraints","CUBIC","INHERITED_D_ARCHITECTURE","YES","D_SPECIFIC","CUBIC_RETARDED_CTP_CONSTRAINT_SET","DOMAIN_MISMATCH","NO","NO","DOMAIN_SPECIFIC_UNBRIDGED","FOUND_BUT_D_SPECIFIC_UNBRIDGED"),
"G90":("not a physical nonlinear completion","CUBIC","GRAVITY_CANDIDATE_GENERATED","NO","C_COVARIANT_CANDIDATE","CANDIDATE_COMPLETION_FAMILY","YES_BUT_SELF_GENERATED","NO","NO","CANDIDATE_OWNED","FOUND_BUT_CANDIDATE_OWNED"),
"G91":("explicit local generally covariant two-invariant family","QUARTIC","GRAVITY_CANDIDATE_GENERATED","NO","D_COVARIANT_CANDIDATE","CANDIDATE_COMPLETION_FAMILY","YES_BUT_SELF_GENERATED","NO","NO","CANDIDATE_OWNED","FOUND_BUT_CANDIDATE_OWNED"),
"G92":("does not select any Weyl/Riemann operator","HIGHER_CURVATURE_DIAGNOSTIC","CANDIDATE_AUDIT","NO","VACUUM_SHELL_AUDIT","DIAGNOSTIC_AUDIT","DIAGNOSTIC_ONLY","NO","NO","DIAGNOSTIC_ONLY","FOUND_BUT_NOT_SELECTOR_DATUM"),
"G93":("BLOCKED_MISSING_CANDIDATE_OWNED_DATUM","THIRD_FINITE_DIFFERENCE_FORM","RCG002_CANDIDATE_OWNED","NO","RCG002","CANDIDATE_OPERATIONAL_FORM_WITHOUT_MAP","MAP_UNDEFINED","NO","NO","CANDIDATE_OWNED","FOUND_BUT_CANDIDATE_OWNED"),
"G94":("D_REUSE_INSUFFICIENT","CUBIC_D_ALGEBRA","D_CANDIDATE_OWNED","NO","D_SPECIFIC","CANDIDATE_BRIDGE_AUDIT","DOMAIN_MISMATCH","NO","NO","DOMAIN_SPECIFIC_UNBRIDGED","FOUND_BUT_D_SPECIFIC_UNBRIDGED"),
"G95":("minimal source-only finite ansatz","CUBIC_ANSATZ","CANDIDATE_ANSATZ","NO","RCG002_FINITE_HISTORY","CANDIDATE_SOURCE_ANSATZ","NO_ESTABLISHED_GRAVITY_LAW","NO","NO","CANDIDATE_OWNED","FOUND_BUT_CANDIDATE_OWNED"),
"G96":("diagnostic connected directions","CUBIC_ANSATZ_DIAGNOSTIC","CANDIDATE_DIAGNOSTIC","NO","RCG002_DIAGNOSTIC","CONSTRAINT_ATTRIBUTION_DIAGNOSTIC","DIAGNOSTIC_ONLY","NO","NO","DIAGNOSTIC_ONLY","FOUND_BUT_NOT_SELECTOR_DATUM"),
"G97":("classical source-preparation mechanics only","CLASSICAL_SOURCE_PREPARATION","CANDIDATE_SOURCE_BOOKKEEPING","NO","CLASSICAL_SOURCE_PREPARATION","SOURCE_BOOKKEEPING_PREREQUISITE","NO_NONLINEAR_GRAVITY_LAW","NO","NO","CLASSICAL_BOOKKEEPING_ONLY","FOUND_BUT_NOT_HIGHER_ORDER_SELECTOR"),
"RCG002_LINEARIZED":("Candidate-owned linearized dynamical rule","LINEARIZED","RCG002_CANDIDATE_OWNED","NO","RCG002_LINEARIZED","CANDIDATE_BASELINE_HYPOTHESIS","LINEARIZED_ONLY","NO","NO","CANDIDATE_OWNED","FOUND_BUT_CANDIDATE_OWNED"),
"RCG007_SYNTHETIC_CUBIC_CONTROL":("genuinely cubic synthetic selector","CUBIC_SYNTHETIC","SYNTHETIC_CONTROL","NO","RCG007_CONTROL","SYNTHETIC_SENSITIVITY_CONTROL","CONTROL_ONLY","NO","YES","SYNTHETIC_CONTROL","FOUND_BUT_SYNTHETIC_CONTROL")
}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--manifest",required=True); ap.add_argument("--out",required=True); a=ap.parse_args()
    m=json.load(open(a.manifest,encoding="utf-8"))
    # independent provenance pass over support, objects and every direct dependency
    seen={}
    for rec in m["support_records"]:
        seen[rec["path"]]=rec["blob"]
    for obj in m["objects"]:
        seen[obj["path"]]=obj["blob"]
        for d in obj["dependencies"]: seen[d["path"]]=d["blob"]
    for p,expected in sorted(seen.items()):
        got=gh_blob(p)
        if got!=expected: raise SystemExit(f"provenance mismatch {p}: {got} != {expected}")
    rows=[]
    for obj in m["objects"]:
        oid=obj["id"]
        if oid not in DECISIONS: raise SystemExit("critic missed "+oid)
        anchor,order,own,ind,domain,otype,gapp,bridge,synthetic,reason,status=DECISIONS[oid]
        src=pathlib.Path(obj["path"]).read_text(encoding="utf-8")
        if anchor not in src: raise SystemExit(f"critic evidence anchor missing {oid}: {anchor}")
        rows.append({
          "OBJECT_ID":oid,"PATH":obj["path"],"COMMIT_OR_BLOB":obj["blob"],
          "PERTURBATIVE_ORDER":order,"RQIR_OWNERSHIP":own,"CANDIDATE_INDEPENDENCE":ind,
          "DOMAIN":domain,"OBSERVABLE_TYPE":otype,"GRAVITY_APPLICABILITY":gapp,
          "BRIDGE_PRESENT":bridge,"PROVENANCE_STATUS":"EXACT","SYNTHETIC_STATUS":synthetic,
          "QUALIFIES":False,"REJECTION_REASON":reason,"CENSUS_STATUS":status})
    controls={r["OBJECT_ID"]:r["CENSUS_STATUS"] for r in rows if r["OBJECT_ID"] in m["mandatory_controls"]}
    out={"phase":"RCG008_INDEPENDENT_CRITIC","authority_base_commit":m["authority_base_commit"],
         "corpus_valid":True,"object_count":len(rows),"controls":controls,
         "qualifying_count":sum(bool(r["QUALIFIES"]) for r in rows),"inventory":rows}
    pathlib.Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(out,sort_keys=True))
if __name__=="__main__": main()
