#!/usr/bin/env python3
import argparse, json, pathlib, subprocess, os

SOURCE_DEFINED="SOURCE_DEFINED_SCOPED_RCG010_PARENT_SOURCE_PRINCIPLE_DERIVED_FROM_EXISTING_RQIR_AUTHORITY"
BLOCKED_UNDER="BLOCKED_SCOPED_RCG010_EXISTING_RQIR_PRINCIPLES_UNDERDETERMINE_PARENT_SOURCE_PRINCIPLE"
BLOCKED_FIELDS="BLOCKED_SCOPED_RCG010_SOURCE_SPACE_DOMAIN_OR_TRANSFORMATION_LAW_UNRESOLVED"
INVALID="INVALID_RCG010_IMPLEMENTATION_OR_PROVENANCE"

def hb(path):
    return subprocess.check_output(["git","hash-object",path],text=True).strip()

def has(path,s):
    return s in pathlib.Path(path).read_text(encoding="utf-8")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",required=True)
    ap.add_argument("--aggregate",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    m=json.load(open(a.manifest,encoding="utf-8"))
    g=json.load(open(a.aggregate,encoding="utf-8"))

    provenance_ok=all(hb(r["path"])==r["blob"] for r in m["authority_records"])
    inherited_constraints=(
      has("candidates/RCG_002_RELATIONAL_CONTROLLED_PHASE_CHANNEL.md","no microscopic formula for `chi` is asserted") and
      has("docs/CONSTRUCTION_CONTRACT.md","minimal dynamics") and
      has("candidates/RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md","No nonlinear metric completion is asserted.") and
      has("results/ITER095_G97_CLOSED_TOTAL_SOURCE_PREPARATION_TERMINAL.md","classical source-preparation mechanics only")
    )
    content_underdefined=(
      has("results/RCG002_RSC_SCPT1_SOURCE_CONSTITUTION_TRIAGE_TERMINAL.md","NO_PREOUTCOME_SOURCE_CONSTITUTION_SELECTED") and
      has("results/RCG002_RSC_QCPT1_QUANTUM_CONSTITUTION_TRIAGE_TERMINAL.md","NO_PREOUTCOME_QUANTUM_CONSTITUTION_SELECTED") and
      has("results/RCG002_RSC_MAPF1_MINIMAL_MULTI_AXIOM_PACKAGE_FORMATION_TERMINAL.md","RSC_PACKAGE_SCHEMA_ONLY_MODEL_DEFINITION_INCOMPLETE") and
      has("results/RCG002_RSC_AB1_NEW_AXIOM_ANCHOR_BUDGET_TERMINAL.md","RSC_NO_NEW_MODEL_DEFINING_AXIOM_INDEPENDENTLY_ANCHORED_PREOUTCOME_SCOPED") and
      has("results/RCG002_RSC_S2PA1_SPIN2_CONSISTENCY_PREMISE_AUTHORITY_TERMINAL.md","NO_SPIN2_CONSISTENCY_PREMISE_CLASS_FORCED_BY_CURRENT_RQIRCG_SCOPED")
    )
    successor_firewall=(
      has("results/RQIRCGSF_STRUCTURAL_IMPORT_TERMINAL.md","any future source principle") and
      has("docs/RQIRCG_MODEL_DEFINITION_SLOT_GRAPH.md","This slot is not fixed by classical-law selection alone.")
    )
    rcg009_lock=has("results/RCG009_UPSTREAM_THIRD_VARIATION_SOURCE_DEFINITION_TERMINAL.md","SOURCE_OBJECT_DEFINED = NO")
    controls_ok=inherited_constraints and content_underdefined and successor_firewall and rcg009_lock

    if not provenance_ok or not controls_ok:
        independent=INVALID
    elif content_underdefined and inherited_constraints and successor_firewall:
        independent=BLOCKED_UNDER
    else:
        independent=BLOCKED_FIELDS

    confirmed=(
      g["classification"]==independent and
      g["parent_functional_defined"] is False and
      g["source_object_defined"] is False and
      g["value_derivation_authorized"] is False and
      g["bridge_authorized"] is False and
      g["alpha_sensitivity_authorized"] is False and
      g["selector_rank"]==0 and
      g["residual_dimension"]==1 and
      g["alpha"]=="UNSELECTED" and
      g["chi_ABC"]=="UNAUTHORIZED_NOT_COMPUTED"
    )
    out={
      "phase":"RCG010_PARENT_SOURCE_PRINCIPLE_INDEPENDENT_SELECTOR_AUDITOR",
      "run_id":os.environ.get("GITHUB_RUN_ID","LOCAL"),
      "verdict":"CONFIRMED_SCOPED" if confirmed else "NOT_CONFIRMED",
      "independent_classification":independent,
      "aggregate_classification":g["classification"],
      "provenance_ok":provenance_ok,
      "controls_ok":controls_ok,
      "parent_principle_defined":False,
      "parent_functional_defined":False,
      "source_object_defined":False,
      "source_space_status":"NOT_DEFINED_PARENT_PRINCIPLE_UNDERDETERMINED",
      "domain_status":"NOT_DEFINED_PARENT_PRINCIPLE_UNDERDETERMINED",
      "transformation_law_status":"NOT_DEFINED_PARENT_PRINCIPLE_UNDERDETERMINED",
      "candidate_independence":"NOT_ESTABLISHED_NO_PARENT_PRINCIPLE",
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
    if not confirmed:
        raise SystemExit(2)
if __name__=="__main__":
    main()
