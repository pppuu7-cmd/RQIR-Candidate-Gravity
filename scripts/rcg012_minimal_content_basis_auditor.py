#!/usr/bin/env python3
import argparse,json,pathlib,subprocess,os
PASS="PASS_SCOPED_RCG012_MINIMAL_EXPLICIT_CONTENT_BASIS_IS_SOURCE_STATE_GENERATOR"
INVALID="INVALID_RCG012_IMPLEMENTATION_OR_PROVENANCE"
def hb(p):return subprocess.check_output(["git","hash-object",p],text=True).strip()
def has(p,s):return s in pathlib.Path(p).read_text(encoding="utf-8")
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--manifest",required=True);ap.add_argument("--aggregate",required=True);ap.add_argument("--out",required=True);a=ap.parse_args()
 m=json.load(open(a.manifest));g=json.load(open(a.aggregate))
 prov=all(hb(r["path"])==r["blob"] for r in m["authority_records"])
 s=has("results/RCG002_RSC1_INTERFACE_CLOSURE_PREOUTCOME_TERMINAL.md","A quantum influence prescription could be specified abstractly while the physical closed source feeding the nonlinear carrier remains ambiguous.")
 q=has("results/RCG002_RSC_QCPT1_QUANTUM_CONSTITUTION_TRIAGE_TERMINAL.md","does not determine a unique operational influence map unless the physical initial state/measure is also fixed.")
 gg=has("results/RCG002_VB1_CURRENT_VERSION_BOUNDARY_TERMINAL.md","Lane A finds no existing current-version nonlinear source/state/evolution rule")
 indep=has("results/RCG002_RSC_MAPF1_MINIMAL_MULTI_AXIOM_PACKAGE_FORMATION_TERMINAL.md","Cartesian-product synthetic family")
 controls=s and q and gg and indep
 independent=PASS if prov and controls else INVALID
 expected=["S_SOURCE_CONSTITUTION","Q_STATE_MEASURE_PREPARATION","G_QUANTITATIVE_GENERATOR"]
 confirmed=(g["classification"]==independent and g["minimal_basis"]==expected and g["constructor_critic_disagreements"]==[] and g["synthetic_full_basis_structurally_executable"] is True and g["fourth_independent_block_required_within_frozen_contract"] is False and g["parent_principle_defined"] is False and g["source_object_defined"] is False and g["alpha"]=="UNSELECTED" and g["chi_ABC"]=="UNAUTHORIZED_NOT_COMPUTED")
 out={"phase":"RCG012_MINIMAL_EXPLICIT_CONTENT_BASIS_INDEPENDENT_SELECTOR_AUDITOR","run_id":os.environ.get("GITHUB_RUN_ID","LOCAL"),
 "verdict":"CONFIRMED_SCOPED" if confirmed else "NOT_CONFIRMED","independent_classification":independent,"aggregate_classification":g["classification"],
 "provenance_ok":prov,"controls_ok":controls,"minimal_basis":expected if confirmed else [],
 "interpretation":"MINIMUM_MODEL_DEFINITION_OBLIGATION_BASIS_WITHIN_FROZEN_PARENT_CONTRACT_NOT_FUNDAMENTAL_LAW_COUNT",
 "parent_principle_defined":False,"parent_functional_defined":False,"source_object_defined":False,
 "value_derivation_authorized":False,"bridge_authorized":False,"alpha_sensitivity_authorized":False,
 "alpha":"UNSELECTED","chi_ABC":"UNAUTHORIZED_NOT_COMPUTED","THEORY_ESTABLISHED":"0%"}
 pathlib.Path(a.out).parent.mkdir(parents=True,exist_ok=True);pathlib.Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
 print(json.dumps(out,sort_keys=True))
 if not confirmed: raise SystemExit(2)
if __name__=="__main__":main()
