#!/usr/bin/env python3
import argparse, json, pathlib, subprocess, os

def hb(path):
    return subprocess.check_output(["git","hash-object",path],text=True).strip()

def has(path, text):
    return text in pathlib.Path(path).read_text(encoding="utf-8")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",required=True)
    ap.add_argument("--aggregate",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    m=json.load(open(a.manifest))
    g=json.load(open(a.aggregate))

    provenance_ok=all(hb(r["path"])==r["blob"] for r in m["authority_records"])

    successor_rejected=(
      has("research_log/RQIRCGSF_STRUCTURAL_IMPORT_MANIFEST.md","No successor-only content receives retroactive authority in RCG-002.") and
      has("results/RQIRCGSF_STRUCTURAL_IMPORT_TERMINAL.md","No future result from either track is parent authority until separately imported or promoted with provenance.")
    )
    g89_rejected=(
      has("results/ITER087_G89_D_INHERITED_CONSTRAINT_SELECTION_SUFFICIENCY_TERMINAL.md","D_FROZEN_RETARDED_CUBIC_SECTOR_COEFFICIENT_BLIND_SCOPED")
    )
    cpi_conditional=(
      has("results/RCG002_CPI1_NONLINEAR_CONSTRUCTOR_TERMINAL.md","W3 and W4 have not been derived or chosen for RCG-002.") and
      has("results/RCG002_CPI1_NONLINEAR_CONSTRUCTOR_TERMINAL.md","Current RCG-002 does not supply the nonlinear U/F needed to evaluate these phases.")
    )
    parent_missing=(
      has("docs/RQIRCG_MODEL_DEFINITION_SLOT_GRAPH.md","A predictive successor must specify") and
      has("docs/RQIRCG_SELECTOR_OBSERVABLE_OBLIGATIONS.md","These obligations do not select RHPI, a quantum law, a source constitution") and
      has("results/RCG002_RSC_SCPT1_SOURCE_CONSTITUTION_TRIAGE_TERMINAL.md","NO_PREOUTCOME_SOURCE_CONSTITUTION_SELECTED") and
      has("results/RCG002_RSC_SSE1_SOURCE_STRESS_EQUIVALENCE_TERMINAL.md","Current authority does not contain such a complete closed-system action.")
    )
    controls_ok=successor_rejected and g89_rejected and cpi_conditional

    if not provenance_ok or not controls_ok:
        independent_class="INVALID_RCG009_IMPLEMENTATION_OR_PROVENANCE"
    elif parent_missing:
        independent_class="BLOCKED_SCOPED_RCG009_RQIR_PRINCIPLES_DO_NOT_DEFINE_REQUIRED_HIGHER_ORDER_OBJECT"
    else:
        independent_class="BLOCKED_SCOPED_RCG009_SOURCE_OWNERSHIP_OR_DOMAIN_UNRESOLVED"

    confirmed=(
      g["classification"]==independent_class and
      g["value_derivation_authorized"] is False and
      g["bridge_gate_authorized"] is False and
      g["alpha_sensitivity_authorized"] is False and
      g["alpha"]=="UNSELECTED" and
      g["chi_ABC"]=="UNAUTHORIZED_NOT_COMPUTED"
    )

    out={
      "phase":"RCG009_UPSTREAM_THIRD_VARIATION_INDEPENDENT_AUDITOR",
      "run_id":os.environ.get("GITHUB_RUN_ID","LOCAL"),
      "verdict":"CONFIRMED_SCOPED" if confirmed else "NOT_CONFIRMED",
      "independent_classification":independent_class,
      "aggregate_classification":g["classification"],
      "provenance_ok":provenance_ok,
      "controls_ok":controls_ok,
      "parent_functional_defined":not parent_missing,
      "source_object_defined":False if parent_missing else None,
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
    if not confirmed:
        raise SystemExit(2)
if __name__=="__main__":
    main()
