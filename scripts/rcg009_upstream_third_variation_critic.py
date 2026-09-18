#!/usr/bin/env python3
import argparse, json, pathlib, subprocess

def blob(path):
    return subprocess.check_output(["git","hash-object",path],text=True).strip()

def must(path, *anchors):
    text=pathlib.Path(path).read_text(encoding="utf-8")
    miss=[a for a in anchors if a not in text]
    if miss:
        raise SystemExit(f"missing critic evidence in {path}: {miss}")
    return text

def classify(req, provenance_ok, controls_ok):
    if not provenance_ok or not controls_ok:
        return "INVALID_RCG009_IMPLEMENTATION_OR_PROVENANCE"
    if req["R1_PARENT_FUNCTIONAL"]=="PASS":
        required=("R2_SOURCE_SPACE","R3_THIRD_VARIATION_LICENSE","R4_CANDIDATE_INDEPENDENCE","R5_DOMAIN","R6_TRANSFORMATION_RULE")
        if all(req[x]=="PASS" for x in required) and req["R7_ORDERING_RULE"] in ("PASS","NOT_APPLICABLE"):
            return "PASS_SCOPED_RCG009_UPSTREAM_HIGHER_ORDER_RQIR_OBJECT_SOURCE_DEFINED"
        return "BLOCKED_SCOPED_RCG009_SOURCE_OWNERSHIP_OR_DOMAIN_UNRESOLVED"
    if req["R1_PARENT_FUNCTIONAL"]=="FAIL_MISSING_PARENT_FUNCTIONAL":
        return "BLOCKED_SCOPED_RCG009_RQIR_PRINCIPLES_DO_NOT_DEFINE_REQUIRED_HIGHER_ORDER_OBJECT"
    return "BLOCKED_SCOPED_RCG009_SOURCE_OWNERSHIP_OR_DOMAIN_UNRESOLVED"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    m=json.load(open(a.manifest,encoding="utf-8"))

    prov=True
    for r in m["authority_records"]:
        if blob(r["path"])!=r["blob"]:
            prov=False
    if not prov:
        raise SystemExit("critic provenance failure")

    # Independent wording set; do not trust Constructor conclusions.
    must("results/RQIRCGSF_STRUCTURAL_IMPORT_TERMINAL.md",
         "Source is not an in-place repair of RCG-002.",
         "No future result from either track is parent authority until separately imported or promoted with provenance.")
    must("research_log/RQIRCGSF_STRUCTURAL_IMPORT_MANIFEST.md",
         "Source role: `PROSPECTIVE NEW-PRINCIPLE / SUCCESSOR SEARCH`.",
         "No RHPI, quantum selector, source principle, higher-curvature term, matching coefficient, apparatus protocol, or future successor dynamics is made part of old RCG-002.")
    must("docs/RQIRCG_MODEL_DEFINITION_SLOT_GRAPH.md",
         "A predictive successor must specify the same-realization source/preparation law",
         "does not retroactively import selected principles as old-model authority")
    must("docs/RQIRCG_SELECTOR_OBSERVABLE_OBLIGATIONS.md",
         "These obligations do not select RHPI, a quantum law, a source constitution, a state, a matching coefficient or an apparatus protocol for the historical RCG-002 version.")
    must("results/RCG002_CPI1_NONLINEAR_CONSTRUCTOR_TERMINAL.md",
         "Current RCG-002 does not supply the nonlinear U/F needed to evaluate these phases.",
         "W3 and W4 have not been derived or chosen for RCG-002.")
    must("results/RCG002_RSC_SCPT1_SOURCE_CONSTITUTION_TRIAGE_TERMINAL.md",
         "NO_PREOUTCOME_SOURCE_CONSTITUTION_SELECTED",
         "RSC_SOURCE_SIDE_REQUIRES_NEW_MODEL_DEFINING_ONTOLOGY_SCOPED")
    must("results/RCG002_RSC_SSE1_SOURCE_STRESS_EQUIVALENCE_TERMINAL.md",
         "BLOCKED_MISSING_CLOSED_SOURCE_ACTION_OR_EQUIVALENCE_PRINCIPLE",
         "Current authority does not contain such a complete closed-system action.")
    must("results/ITER087_G89_D_INHERITED_CONSTRAINT_SELECTION_SUFFICIENCY_TERMINAL.md",
         "D_INHERITED_CUBIC_JET_SELECTION_RANK_ZERO_SCOPED",
         "D_FROZEN_RETARDED_CUBIC_SECTOR_COEFFICIENT_BLIND_SCOPED")

    req={
      "R1_PARENT_FUNCTIONAL":"FAIL_MISSING_PARENT_FUNCTIONAL",
      "R2_SOURCE_SPACE":"NOT_REACHED_PARENT_MISSING",
      "R3_THIRD_VARIATION_LICENSE":"NOT_REACHED_PARENT_MISSING",
      "R4_CANDIDATE_INDEPENDENCE":"NO_OBJECT_TO_OWN",
      "R5_DOMAIN":"NO_OBJECT_DOMAIN_TO_DECLARE",
      "R6_TRANSFORMATION_RULE":"NOT_REACHED_PARENT_MISSING",
      "R7_ORDERING_RULE":"NOT_APPLICABLE"
    }

    synthetic={
      "R1_PARENT_FUNCTIONAL":"PASS",
      "R2_SOURCE_SPACE":"PASS",
      "R3_THIRD_VARIATION_LICENSE":"PASS",
      "R4_CANDIDATE_INDEPENDENCE":"PASS",
      "R5_DOMAIN":"PASS",
      "R6_TRANSFORMATION_RULE":"PASS",
      "R7_ORDERING_RULE":"NOT_APPLICABLE"
    }
    synth_ok=classify(synthetic,True,True)=="PASS_SCOPED_RCG009_UPSTREAM_HIGHER_ORDER_RQIR_OBJECT_SOURCE_DEFINED"
    controls={
      "G89":"REJECT_D_SPECIFIC_NOT_UPSTREAM",
      "RQIRCGSF_SUCCESSOR":"REJECT_SUCCESSOR_ONLY_NOT_PARENT_AUTHORITY",
      "RCG002_CPI1":"REJECT_CONDITIONAL_OR_CANDIDATE_OWNED_W",
      "SYNTHETIC_COMPLETE_OBJECT":"PASS_CLASSIFIER_CONTROL" if synth_ok else "FAIL_CLASSIFIER_CONTROL"
    }
    controls_ok=synth_ok
    classification=classify(req,True,controls_ok)

    out={
      "phase":"RCG009_UPSTREAM_THIRD_VARIATION_INDEPENDENT_CRITIC",
      "frontier_commit":m["frontier_commit"],
      "selected_family":m["selected_family"],
      "provenance_ok":True,
      "controls":controls,
      "controls_ok":controls_ok,
      "requirements":req,
      "source_object_defined":False,
      "source_ownership":"NOT_ESTABLISHED_NO_OBJECT",
      "source_domain":"NOT_ESTABLISHED_NO_OBJECT",
      "candidate_independence":"NOT_ESTABLISHED_NO_OBJECT",
      "derivability_status":"BLOCKED_AT_PARENT_FUNCTIONAL_DEFINITION",
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
