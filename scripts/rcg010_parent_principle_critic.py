#!/usr/bin/env python3
import argparse, json, pathlib, subprocess

SOURCE_DEFINED="SOURCE_DEFINED_SCOPED_RCG010_PARENT_SOURCE_PRINCIPLE_DERIVED_FROM_EXISTING_RQIR_AUTHORITY"
BLOCKED_UNDER="BLOCKED_SCOPED_RCG010_EXISTING_RQIR_PRINCIPLES_UNDERDETERMINE_PARENT_SOURCE_PRINCIPLE"
BLOCKED_FIELDS="BLOCKED_SCOPED_RCG010_SOURCE_SPACE_DOMAIN_OR_TRANSFORMATION_LAW_UNRESOLVED"
INVALID="INVALID_RCG010_IMPLEMENTATION_OR_PROVENANCE"

def hb(path):
    return subprocess.check_output(["git","hash-object",path],text=True).strip()

def must(path,*anchors):
    txt=pathlib.Path(path).read_text(encoding="utf-8")
    miss=[a for a in anchors if a not in txt]
    if miss:
        raise SystemExit(f"missing critic evidence in {path}: {miss}")
    return txt

def classify(req, prov=True, controls=True):
    if not prov or not controls:
        return INVALID
    if req["R1_PARENT_PRINCIPLE_OR_DERIVATION_RULE"]=="FAIL_UNDERDETERMINED":
        return BLOCKED_UNDER
    if req["R1_PARENT_PRINCIPLE_OR_DERIVATION_RULE"]=="PASS":
        needed=("R2_SOURCE_SPACE","R3_DOMAIN","R4_TRANSFORMATION_OR_EQUIVALENCE_LAW",
                "R6_NORMALIZATION_OR_EQUIVALENCE_CLASS","R7_GENERATING_OR_RESPONSE_RULE",
                "R8_CANDIDATE_INDEPENDENCE","R9_SUCCESSOR_FIREWALL","R10_PREOUTCOME_SELECTION")
        if all(req[k]=="PASS" for k in needed) and req["R5_CAUSAL_OR_ORDERING_RULE"] in ("PASS","NOT_APPLICABLE"):
            return SOURCE_DEFINED
    return BLOCKED_FIELDS

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",required=True)
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    m=json.load(open(a.manifest,encoding="utf-8"))

    prov=all(hb(r["path"])==r["blob"] for r in m["authority_records"])
    if not prov:
        raise SystemExit("critic provenance failure")

    # Independent evidence wording: attack every apparent rescue route.
    must("candidates/RCG_002_RELATIONAL_CONTROLLED_PHASE_CHANNEL.md",
         "no microscopic formula for `chi` is asserted",
         "future candidate must derive its source")
    must("docs/CONSTRUCTION_CONTRACT.md",
         "minimal degrees of freedom -> minimal dynamics -> observable map",
         "BLOCKED != FAIL")
    must("candidates/RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md",
         "No nonlinear metric completion is asserted.",
         "it is not yet a full nonlinear diffeomorphism constitution")
    must("results/ITER095_G97_CLOSED_TOTAL_SOURCE_PREPARATION_TERMINAL.md",
         "classical source-preparation mechanics only",
         "does NOT define the RCG-002 nonlinear gravitational law")
    must("results/RCG002_RSC_CSA1_CLOSED_SOURCE_ACTION_PROPOSAL_TERMINAL.md",
         "BLOCKED_SOURCE_ACTION_OBJECT_UNDERDEFINED",
         "candidate-owned source constitution")
    must("results/RCG002_RSC_SCPT1_SOURCE_CONSTITUTION_TRIAGE_TERMINAL.md",
         "NO_PREOUTCOME_SOURCE_CONSTITUTION_SELECTED",
         "genuinely model-defining **microphysical source ontology/constitution**")
    must("results/RCG002_RSC_QCPT1_QUANTUM_CONSTITUTION_TRIAGE_TERMINAL.md",
         "NO_PREOUTCOME_QUANTUM_CONSTITUTION_SELECTED",
         "physical state/measure/coarse-graining constitution")
    must("results/RCG002_RSC_MAPF1_MINIMAL_MULTI_AXIOM_PACKAGE_FORMATION_TERMINAL.md",
         "RSC_PACKAGE_SCHEMA_ONLY_MODEL_DEFINITION_INCOMPLETE",
         "actual new **content axioms**")
    must("results/RCG002_RSC_AB1_NEW_AXIOM_ANCHOR_BUDGET_TERMINAL.md",
         "RSC_NO_NEW_MODEL_DEFINING_AXIOM_INDEPENDENTLY_ANCHORED_PREOUTCOME_SCOPED",
         "STRUCTURAL_ANCHOR != MODEL_DEFINITION_SELECTOR")
    must("results/RCG002_RSC_S2PA1_SPIN2_CONSISTENCY_PREMISE_AUTHORITY_TERMINAL.md",
         "NO_SPIN2_CONSISTENCY_PREMISE_CLASS_FORCED_BY_CURRENT_RQIRCG_SCOPED",
         "A genuinely new rule choosing")
    must("docs/RQIRCG_MODEL_DEFINITION_SLOT_GRAPH.md",
         "This slot is not fixed by classical-law selection alone.",
         "STATE_MEASURE_SELECTION != QUANTUM_LAW_MATCHING_SELECTION")
    must("results/RQIRCGSF_STRUCTURAL_IMPORT_TERMINAL.md",
         "Source is not an in-place repair of RCG-002.",
         "any future source principle")
    must("results/RCG009_UPSTREAM_THIRD_VARIATION_SOURCE_DEFINITION_TERMINAL.md",
         "Current durable RQIR authority does **not** define the primitive candidate-independent parent source/generating/influence functional",
         "next scientific move")

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
    synth={k:"PASS" for k in req}
    synth["R5_CAUSAL_OR_ORDERING_RULE"]="NOT_APPLICABLE"
    synth_ok=classify(synth,True,True)==SOURCE_DEFINED
    controls={
      "SEED_DEMANDS_DERIVATION_NOT_LAW":"PASS_REQUIREMENT_NOT_GENERATOR",
      "CONSTRUCTION_CONTRACT":"PASS_SCHEMA_NOT_SELECTED_CONTENT",
      "LINEAR_BASELINE":"PASS_SCOPED_LINEAR_NOT_PARENT_NONLINEAR",
      "G97":"PASS_BOOKKEEPING_NOT_SOURCE_ONTOLOGY",
      "CLOSED_VARIATIONAL_SOURCE":"REJECT_UNDERDEFINED_ONTOLOGY_OR_COUPLING",
      "POSITIVE_INFLUENCE":"REJECT_UNSELECTED_STATE_MEASURE",
      "RELATIONAL_COMPOSITION":"REJECT_UNFORCED_PREMISE_CLASS",
      "FORMAL_MULTI_AXIOM_SCHEMA":"REJECT_PLACEHOLDERS_NOT_CONTENT",
      "SUCCESSOR_SOURCE_PRINCIPLE":"REJECT_RETROACTIVE_PARENT_AUTHORITY",
      "SYNTHETIC_COMPLETE_PARENT_PRINCIPLE":"PASS_SOURCE_DEFINED_CLASSIFIER_CONTROL" if synth_ok else "FAIL_CLASSIFIER_CONTROL"
    }
    controls_ok=synth_ok and all(v.startswith(("PASS","REJECT")) for v in controls.values())
    classification=classify(req,prov,controls_ok)
    out={
      "phase":"RCG010_PARENT_SOURCE_PRINCIPLE_INDEPENDENT_CRITIC",
      "frontier_commit":m["frontier_commit"],
      "selected_gate":m["selected_gate"],
      "provenance_ok":prov,
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
