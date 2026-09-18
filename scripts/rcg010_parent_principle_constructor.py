#!/usr/bin/env python3
import argparse, json, pathlib, subprocess

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

def blob(path):
    return subprocess.check_output(["git","hash-object",path],text=True).strip()

def require(path,*anchors):
    txt=pathlib.Path(path).read_text(encoding="utf-8")
    miss=[a for a in anchors if a not in txt]
    if miss:
        raise SystemExit(f"missing constructor authority anchor in {path}: {miss}")
    return txt

def classify(req, provenance_ok=True, controls_ok=True):
    if not provenance_ok or not controls_ok:
        return INVALID
    if req["R1_PARENT_PRINCIPLE_OR_DERIVATION_RULE"]=="FAIL_UNDERDETERMINED":
        return BLOCKED_UNDER
    if req["R1_PARENT_PRINCIPLE_OR_DERIVATION_RULE"]=="PASS":
        must=("R2_SOURCE_SPACE","R3_DOMAIN","R4_TRANSFORMATION_OR_EQUIVALENCE_LAW",
              "R6_NORMALIZATION_OR_EQUIVALENCE_CLASS","R7_GENERATING_OR_RESPONSE_RULE",
              "R8_CANDIDATE_INDEPENDENCE","R9_SUCCESSOR_FIREWALL","R10_PREOUTCOME_SELECTION")
        if all(req[k]=="PASS" for k in must) and req["R5_CAUSAL_OR_ORDERING_RULE"] in ("PASS","NOT_APPLICABLE"):
            return SOURCE_DEFINED
        return BLOCKED_FIELDS
    return BLOCKED_FIELDS

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

    require("candidates/RCG_002_RELATIONAL_CONTROLLED_PHASE_CHANNEL.md",
            "At this stage no microscopic formula for `chi` is asserted. A future candidate must derive its source, distance, time, `G`, and `hbar` dependence rather than fit it freely.")
    require("docs/CONSTRUCTION_CONTRACT.md",
            "RQIR requirements -> formal constraints -> minimal degrees of freedom -> minimal dynamics -> observable map -> consistency gates -> comparator quotient -> holdout",
            "normalized quantum-state evolution")
    require("candidates/RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md",
            "No nonlinear metric completion is asserted.",
            "this document does not yet specify a complete interacting quantum-gravity measure or nonlinear renormalized stress tensor.")
    require("results/ITER095_G97_CLOSED_TOTAL_SOURCE_PREPARATION_TERMINAL.md",
            "PASS_CLOSED_TOTAL_SOURCE_PREPARATION_CONSERVATION_SCOPED",
            "It does NOT define the RCG-002 nonlinear gravitational law")
    require("results/RCG002_RSC1_INTERFACE_CLOSURE_PREOUTCOME_TERMINAL.md",
            "BLOCKED_SOURCE_STRESS_INTERFACE_MISSING_DATUM",
            "BLOCKED_POSITIVE_INFLUENCE_INTERFACE_MISSING_DATUM")
    require("results/RCG002_RSC_CSA1_CLOSED_SOURCE_ACTION_PROPOSAL_TERMINAL.md",
            "BLOCKED_SOURCE_ACTION_OBJECT_UNDERDEFINED",
            "CLOSED_VARIATIONAL_SOURCE_RULE_NOT_UNIQUE_WITHOUT_CONSTITUTIVE_CURVATURE_COUPLING_RULE_SCOPED")
    require("results/RCG002_RSC_SCPT1_SOURCE_CONSTITUTION_TRIAGE_TERMINAL.md",
            "NO_PREOUTCOME_SOURCE_CONSTITUTION_SELECTED",
            "RSC_SOURCE_SIDE_REQUIRES_NEW_MODEL_DEFINING_ONTOLOGY_SCOPED")
    require("results/RCG002_RSC_QCPT1_QUANTUM_CONSTITUTION_TRIAGE_TERMINAL.md",
            "NO_PREOUTCOME_QUANTUM_CONSTITUTION_SELECTED",
            "RSC_QUANTUM_SIDE_REQUIRES_NEW_STATE_MEASURE_CONSTITUTION_SCOPED")
    require("results/RCG002_RSC_MAPF1_MINIMAL_MULTI_AXIOM_PACKAGE_FORMATION_TERMINAL.md",
            "RSC_PACKAGE_SCHEMA_ONLY_MODEL_DEFINITION_INCOMPLETE",
            "CRVQ_FORMAL_CLOSURE_DOES_NOT_FIX_INDEPENDENT_SOURCE_AND_STATE_DATA_SCOPED")
    require("results/RCG002_RSC_AB1_NEW_AXIOM_ANCHOR_BUDGET_TERMINAL.md",
            "RSC_NO_NEW_MODEL_DEFINING_AXIOM_INDEPENDENTLY_ANCHORED_PREOUTCOME_SCOPED",
            "STRONG_STRUCTURAL_ANCHORS_EXIST_BUT_NO_LEVELIII_MODEL_SELECTOR_SCOPED")
    require("results/RCG002_RSC_S2PA1_SPIN2_CONSISTENCY_PREMISE_AUTHORITY_TERMINAL.md",
            "NO_SPIN2_CONSISTENCY_PREMISE_CLASS_FORCED_BY_CURRENT_RQIRCG_SCOPED",
            "SPIN2_RIGIDITY_IS_PREMISE_CLASS_DEPENDENT_AND_CURRENT_PARENT_DOES_NOT_SELECT_THE_PREMISE_CLASS_SCOPED")
    require("docs/RQIRCG_MODEL_DEFINITION_SLOT_GRAPH.md",
            "## Slot B — SOURCE / PREPARATION CONSTITUTION",
            "Status in historical parent: `UNRESOLVED_MODEL_DEFINITION_SLOT`")
    require("results/RQIRCGSF_STRUCTURAL_IMPORT_TERMINAL.md",
            "any future source principle",
            "No future result from either track is parent authority until separately imported or promoted with provenance.")
    require("results/RCG009_UPSTREAM_THIRD_VARIATION_SOURCE_DEFINITION_TERMINAL.md",
            "BLOCKED_SCOPED_RCG009_RQIR_PRINCIPLES_DO_NOT_DEFINE_REQUIRED_HIGHER_ORDER_OBJECT",
            "SOURCE_OBJECT_DEFINED = NO")

    controls={
      "SEED_DEMANDS_DERIVATION_NOT_LAW":"PASS_REQUIREMENT_NOT_GENERATOR",
      "CONSTRUCTION_CONTRACT":"PASS_SCHEMA_NOT_SELECTED_CONTENT",
      "LINEAR_BASELINE":"PASS_SCOPED_LINEAR_NOT_PARENT_NONLINEAR",
      "G97":"PASS_BOOKKEEPING_NOT_SOURCE_ONTOLOGY",
      "CLOSED_VARIATIONAL_SOURCE":"REJECT_UNDERDEFINED_ONTOLOGY_OR_COUPLING",
      "POSITIVE_INFLUENCE":"REJECT_UNSELECTED_STATE_MEASURE",
      "RELATIONAL_COMPOSITION":"REJECT_UNFORCED_PREMISE_CLASS",
      "FORMAL_MULTI_AXIOM_SCHEMA":"REJECT_PLACEHOLDERS_NOT_CONTENT",
      "SUCCESSOR_SOURCE_PRINCIPLE":"REJECT_RETROACTIVE_PARENT_AUTHORITY"
    }

    # Cheapest obstruction: current authority supplies constraints and negative
    # sufficiency results, but no explicit parent principle or derivation rule
    # with Level-III selection power on the source/state/generating content.
    req={
      "R1_PARENT_PRINCIPLE_OR_DERIVATION_RULE":"FAIL_UNDERDETERMINED",
      "R2_SOURCE_SPACE":"NOT_REACHED_R1_BLOCKER",
      "R3_DOMAIN":"NOT_REACHED_R1_BLOCKER",
      "R4_TRANSFORMATION_OR_EQUIVALENCE_LAW":"NOT_REACHED_R1_BLOCKER",
      "R5_CAUSAL_OR_ORDERING_RULE":"NOT_REACHED_R1_BLOCKER",
      "R6_NORMALIZATION_OR_EQUIVALENCE_CLASS":"NOT_REACHED_R1_BLOCKER",
      "R7_GENERATING_OR_RESPONSE_RULE":"NOT_REACHED_R1_BLOCKER",
      "R8_CANDIDATE_INDEPENDENCE":"NO_PARENT_PRINCIPLE_TO_OWN",
      "R9_SUCCESSOR_FIREWALL":"PASS",
      "R10_PREOUTCOME_SELECTION":"PASS"
    }

    synthetic={k:"PASS" for k in REQ_KEYS}
    synthetic["R5_CAUSAL_OR_ORDERING_RULE"]="NOT_APPLICABLE"
    synth_ok=classify(synthetic,True,True)==SOURCE_DEFINED
    controls["SYNTHETIC_COMPLETE_PARENT_PRINCIPLE"]="PASS_SOURCE_DEFINED_CLASSIFIER_CONTROL" if synth_ok else "FAIL_CLASSIFIER_CONTROL"
    controls_ok=synth_ok and all(v.startswith(("PASS","REJECT")) for v in controls.values())

    classification=classify(req,True,controls_ok)
    out={
      "phase":"RCG010_PARENT_SOURCE_PRINCIPLE_CONSTRUCTOR",
      "frontier_commit":m["frontier_commit"],
      "selected_gate":m["selected_gate"],
      "provenance_ok":True,
      "controls":controls,
      "controls_ok":controls_ok,
      "requirements":req,
      "parent_principle_defined":False,
      "parent_functional_defined":False,
      "source_object_defined":False,
      "source_space_status":"NOT_DEFINED_PARENT_PRINCIPLE_UNDERDETERMINED",
      "domain_status":"NOT_DEFINED_PARENT_PRINCIPLE_UNDERDETERMINED",
      "transformation_law_status":"NOT_DEFINED_PARENT_PRINCIPLE_UNDERDETERMINED",
      "candidate_independence":"NOT_ESTABLISHED_NO_PARENT_PRINCIPLE",
      "derivability_status":"BLOCKED_EXISTING_PRINCIPLES_UNDERDETERMINE_PARENT_SOURCE_PRINCIPLE",
      "current_blocker":"EXISTING_RQIR_PRINCIPLES_UNDERDETERMINE_PARENT_SOURCE_PRINCIPLE",
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
