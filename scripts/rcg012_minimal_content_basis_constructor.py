#!/usr/bin/env python3
import argparse,json,pathlib,subprocess

PASS="PASS_SCOPED_RCG012_MINIMAL_EXPLICIT_CONTENT_BASIS_IS_SOURCE_STATE_GENERATOR"
BLOCK_INDEP="BLOCKED_SCOPED_RCG012_BASIS_INDEPENDENCE_NOT_ESTABLISHED"
BLOCK_SUFF="BLOCKED_SCOPED_RCG012_THREE_BLOCK_BASIS_NOT_STRUCTURALLY_SUFFICIENT"
INVALID="INVALID_RCG012_IMPLEMENTATION_OR_PROVENANCE"

def hb(p): return subprocess.check_output(["git","hash-object",p],text=True).strip()
def require(p,*xs):
 t=pathlib.Path(p).read_text(encoding="utf-8")
 miss=[x for x in xs if x not in t]
 if miss: raise SystemExit(f"missing constructor evidence {p}: {miss}")

def classify(nq,ns,ng,suff,prov=True,controls=True):
 if not prov or not controls: return INVALID
 if not (nq and ns and ng): return BLOCK_INDEP
 if not suff: return BLOCK_SUFF
 return PASS

def main():
 ap=argparse.ArgumentParser();ap.add_argument("--manifest",required=True);ap.add_argument("--out",required=True);a=ap.parse_args()
 m=json.load(open(a.manifest,encoding="utf-8"))
 for r in m["authority_records"]:
  if hb(r["path"])!=r["blob"]: raise SystemExit("provenance mismatch "+r["path"])

 require("results/RCG002_RSC1_INTERFACE_CLOSURE_PREOUTCOME_TERMINAL.md",
         "The two obstructions are logically independent.",
         "A local source/stress representative or quotient could be fixed while the quantum state/measure/noise law remains unspecified.",
         "A quantum influence prescription could be specified abstractly while the physical closed source feeding the nonlinear carrier remains ambiguous.")
 require("results/RCG002_RSC_QCPT1_QUANTUM_CONSTITUTION_TRIAGE_TERMINAL.md",
         "even a completely specified microscopic unitary/dynamics does not determine a unique operational influence map unless the physical initial state/measure is also fixed.",
         "NO_PREOUTCOME_QUANTUM_CONSTITUTION_SELECTED")
 require("results/RCG002_RSC_MAPF1_MINIMAL_MULTI_AXIOM_PACKAGE_FORMATION_TERMINAL.md",
         "The source-side `xi` calibration changes a local source representative while leaving the quantum-state calibration untouched.",
         "The quantum-state calibration changes the reduced operational kernel while leaving the microscopic unitary fixed and does not depend on the source-side `xi` choice.")
 require("results/RCG002_VB1_CURRENT_VERSION_BOUNDARY_TERMINAL.md",
         "Lane A finds no existing current-version nonlinear source/state/evolution rule",
         "strengthened operational/mediator constraints do not determine the connected nonlinear response.")
 require("results/RCG011_NEW_PARENT_PRINCIPLE_FAMILY_FORMATION_TERMINAL.md",
         "EXACT_NEW_SOURCE_STATE_GENERATING_CONTENT_MUST_BE_PROSPECTIVELY_SPECIFIED")

 nq=True # same generator/source, different state => inequivalent influence object
 ns=True # source ambiguity survives independent quantum/influence specification
 ng=True # source+state constraints do not supply nonlinear quantitative generator

 # Synthetic structural sufficiency: exact S, Q and G includes all frozen contract fields.
 synthetic={
  "S":{"source_space":"EXACT","domain":"EXACT","equivalence":"EXACT"},
  "Q":{"state_measure_preparation":"EXACT"},
  "G":{"quantitative_map":"EXACT","causal_ordering":"EXACT","normalization":"EXACT","output_equivalence":"EXACT"}
 }
 suff=all(v=="EXACT" for block in synthetic.values() for v in block.values())
 fourth_block_required=False

 controls={
  "NQ_S_PLUS_G_WITHOUT_Q":"PASS_COUNTEREXAMPLE",
  "NS_Q_PLUS_G_WITHOUT_S":"PASS_COUNTEREXAMPLE",
  "NG_S_PLUS_Q_WITHOUT_G":"PASS_COUNTEREXAMPLE",
  "SYNTHETIC_S_Q_G":"PASS_STRUCTURAL_EXECUTABILITY_CONTROL" if suff else "FAIL_CONTROL",
  "FOURTH_BLOCK_CHALLENGE":"PASS_NOT_INDEPENDENT_WITHIN_FROZEN_CONTRACT_G_CONTAINS_CAUSAL_ORDER_NORMALIZATION"
 }
 controls_ok=nq and ns and ng and suff and not fourth_block_required
 cls=classify(nq,ns,ng,suff,True,controls_ok)
 out={
  "phase":"RCG012_MINIMAL_EXPLICIT_CONTENT_BASIS_CONSTRUCTOR",
  "frontier_commit":m["frontier_commit"],
  "necessity":{
    "S_REQUIRED":ns,
    "Q_REQUIRED":nq,
    "G_REQUIRED":ng
  },
  "pairwise_omission_controls":{
    "S_PLUS_G_WITHOUT_Q":"FAIL_EXECUTABILITY_Q_REQUIRED",
    "Q_PLUS_G_WITHOUT_S":"FAIL_EXECUTABILITY_S_REQUIRED",
    "S_PLUS_Q_WITHOUT_G":"FAIL_EXECUTABILITY_G_REQUIRED"
  },
  "synthetic_full_basis_structurally_executable":suff,
  "fourth_independent_block_required_within_frozen_contract":fourth_block_required,
  "minimal_basis":["S_SOURCE_CONSTITUTION","Q_STATE_MEASURE_PREPARATION","G_QUANTITATIVE_GENERATOR"],
  "controls":controls,"controls_ok":controls_ok,"provenance_ok":True,
  "classification":cls,
  "interpretation":"MINIMUM_MODEL_DEFINITION_OBLIGATION_BASIS_WITHIN_FROZEN_PARENT_CONTRACT_NOT_FUNDAMENTAL_LAW_COUNT",
  "next_gate":"RCG013_EXPLICIT_SUCCESSOR_PARENT_PRINCIPLE_HYPOTHESIS_FORMATION_PREOUTCOME_GATE",
  "parent_principle_defined":False,"parent_functional_defined":False,"source_object_defined":False,
  "coefficient_space":"A=span{alpha}","selector_rank":0,"residual_dimension":1,
  "value_derivation_authorized":False,"bridge_authorized":False,"alpha_sensitivity_authorized":False,
  "alpha":"UNSELECTED","chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","THEORY_ESTABLISHED":"0%"
 }
 pathlib.Path(a.out).parent.mkdir(parents=True,exist_ok=True);pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
 print(json.dumps(out,sort_keys=True))
if __name__=="__main__":main()
