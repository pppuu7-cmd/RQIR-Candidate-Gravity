#!/usr/bin/env python3
import argparse, json, pathlib, subprocess

def blob(path):
    return subprocess.check_output(["git","hash-object",path],text=True).strip()

def require(path, *anchors):
    text=pathlib.Path(path).read_text(encoding="utf-8")
    missing=[a for a in anchors if a not in text]
    if missing:
        raise SystemExit(f"missing constructor evidence in {path}: {missing}")
    return text

def classify(req, provenance_ok=True, controls_ok=True):
    if not provenance_ok or not controls_ok:
        return "INVALID_RCG009_IMPLEMENTATION_OR_PROVENANCE"
    if req["R1_PARENT_FUNCTIONAL"]=="PASS":
        needed=["R2_SOURCE_SPACE","R3_THIRD_VARIATION_LICENSE","R4_CANDIDATE_INDEPENDENCE","R5_DOMAIN","R6_TRANSFORMATION_RULE"]
        if all(req[k]=="PASS" for k in needed) and req["R7_ORDERING_RULE"] in ("PASS","NOT_APPLICABLE"):
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

    for r in m["authority_records"]:
        got=blob(r["path"])
        if got!=r["blob"]:
            raise SystemExit(f"provenance mismatch {r['path']}: {got} != {r['blob']}")

    require("results/RQIRCGSF_STRUCTURAL_IMPORT_TERMINAL.md",
            "any future source principle",
            "No future result from either track is parent authority until separately imported or promoted with provenance.")
    require("research_log/RQIRCGSF_STRUCTURAL_IMPORT_MANIFEST.md",
            "No successor-only content receives retroactive authority in RCG-002.",
            "any future source constitution principle")
    require("docs/RQIRCG_MODEL_DEFINITION_SLOT_GRAPH.md",
            "Slot B — SOURCE / PREPARATION CONSTITUTION",
            "A predictive successor must specify")
    require("docs/RQIRCG_SELECTOR_OBSERVABLE_OBLIGATIONS.md",
            "These obligations do not select RHPI, a quantum law, a source constitution")
    require("results/RCG002_CPI1_NONLINEAR_CONSTRUCTOR_TERMINAL.md",
            "A conditional structural formula can be derived before choosing any dynamics. Suppose coherent factorization supplies a real action-valued functional W",
            "W3 and W4 have not been derived or chosen for RCG-002.")
    require("results/RCG002_RSC_SCPT1_SOURCE_CONSTITUTION_TRIAGE_TERMINAL.md",
            "Current RCG-002 does not contain the closed flat-space local source action/field ontology",
            "current repository simply does not contain such an object.")
    require("results/RCG002_RSC_SSE1_SOURCE_STRESS_EQUIVALENCE_TERMINAL.md",
            "Current authority does not contain such a complete closed-system action.",
            "metric-variation source cannot presently be evaluated without adding new model-defining information.")
    require("results/ITER087_G89_D_INHERITED_CONSTRAINT_SELECTION_SUFFICIENCY_TERMINAL.md",
            "D_FROZEN_RETARDED_CUBIC_SECTOR_COEFFICIENT_BLIND_SCOPED",
            "D constraints already frozen")

    controls={
      "G89":"REJECT_D_SPECIFIC_NOT_UPSTREAM",
      "RQIRCGSF_SUCCESSOR":"REJECT_SUCCESSOR_ONLY_NOT_PARENT_AUTHORITY",
      "RCG002_CPI1":"REJECT_CONDITIONAL_OR_CANDIDATE_OWNED_W",
    }

    # The frozen authority explicitly treats source constitution as future/missing,
    # successor principles as non-parent authority, and the only analytic W as conditional.
    req={
      "R1_PARENT_FUNCTIONAL":"FAIL_MISSING_PARENT_FUNCTIONAL",
      "R2_SOURCE_SPACE":"NOT_REACHED_PARENT_MISSING",
      "R3_THIRD_VARIATION_LICENSE":"NOT_REACHED_PARENT_MISSING",
      "R4_CANDIDATE_INDEPENDENCE":"NO_OBJECT_TO_OWN",
      "R5_DOMAIN":"NO_OBJECT_DOMAIN_TO_DECLARE",
      "R6_TRANSFORMATION_RULE":"NOT_REACHED_PARENT_MISSING",
      "R7_ORDERING_RULE":"NOT_APPLICABLE"
    }

    synthetic_req={
      "R1_PARENT_FUNCTIONAL":"PASS",
      "R2_SOURCE_SPACE":"PASS",
      "R3_THIRD_VARIATION_LICENSE":"PASS",
      "R4_CANDIDATE_INDEPENDENCE":"PASS",
      "R5_DOMAIN":"PASS",
      "R6_TRANSFORMATION_RULE":"PASS",
      "R7_ORDERING_RULE":"NOT_APPLICABLE"
    }
    synthetic_class=classify(synthetic_req,True,True)
    synthetic_ok=(synthetic_class=="PASS_SCOPED_RCG009_UPSTREAM_HIGHER_ORDER_RQIR_OBJECT_SOURCE_DEFINED")
    controls["SYNTHETIC_COMPLETE_OBJECT"]="PASS_CLASSIFIER_CONTROL" if synthetic_ok else "FAIL_CLASSIFIER_CONTROL"

    controls_ok=synthetic_ok and controls["G89"]=="REJECT_D_SPECIFIC_NOT_UPSTREAM" and controls["RQIRCGSF_SUCCESSOR"]=="REJECT_SUCCESSOR_ONLY_NOT_PARENT_AUTHORITY" and controls["RCG002_CPI1"]=="REJECT_CONDITIONAL_OR_CANDIDATE_OWNED_W"
    classification=classify(req,True,controls_ok)

    out={
      "phase":"RCG009_UPSTREAM_THIRD_VARIATION_CONSTRUCTOR",
      "frontier_commit":m["frontier_commit"],
      "selected_family":m["selected_family"],
      "formal_target":m["target_formal_object"],
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
