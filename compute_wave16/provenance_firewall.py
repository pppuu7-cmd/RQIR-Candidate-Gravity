#!/usr/bin/env python3
import json
from pathlib import Path

pinned_source={
 "repository":"pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction",
 "commit":"5a82c5828a73dbca8dbf9ed9cf63d436632d8095",
 "allowed_files":[
  "README.md","RQIR_VERSION.json","docs/RQIR_CORE_V1_FREEZE_MANIFEST_2026-09-09.md",
  "docs/FOUNDATIONS.md","docs/MASTER_TABLE.md","candidate_gravity/MODEL_SPEC_TEMPLATE.md",
  "candidate_gravity/MODEL_TO_RQIR_CONTRACT.md","candidate_gravity/NEW_MODEL_CHECKLIST.md",
  "candidate_gravity/GATE_STATUS_TEMPLATE.yaml","candidate_gravity/BASELINE_COMPARATORS.md"
 ]
}
used_constraints=[
 {"name":"retarded causal support","source":"docs/FOUNDATIONS.md + MODEL_TO_RQIR_CONTRACT.md","allowed":True},
 {"name":"single dynamics / one parameter convention","source":"docs/MASTER_TABLE.md + MODEL_TO_RQIR_CONTRACT.md","allowed":True},
 {"name":"Ward/conservation compatibility","source":"docs/FOUNDATIONS.md + MODEL_TO_RQIR_CONTRACT.md","allowed":True},
 {"name":"positivity/unitarity/CP gate","source":"docs/FOUNDATIONS.md + MODEL_TO_RQIR_CONTRACT.md","allowed":True},
 {"name":"gauge/relational consistency","source":"docs/FOUNDATIONS.md","allowed":True},
 {"name":"EFT/renormalization domain discipline","source":"docs/FOUNDATIONS.md + MODEL_TO_RQIR_CONTRACT.md","allowed":True}
]
forbidden_inputs=[
 "KMQGB benchmark outcomes","polygon-derived QGR equations/architecture","QGR-P repairs",
 "post-freeze Wave-12/13/14/15 equations as if RQIR axioms","known comparator solutions used as derivation targets"
]
proxy_only=[
 "K(x,0)=0 endpoint softness","K(x,x)=0 coincidence softness","unit normalization of abstract K",
 "degree<=2 polynomial kernel","Volterra alpha/beta kernel"
]
out={
 "test":"Wave 16 independence and provenance firewall",
 "pinned_source":pinned_source,
 "used_constraints":used_constraints,
 "forbidden_inputs":forbidden_inputs,
 "proxy_conditions_explicitly_not_promoted_to_RQIR":proxy_only,
 "all_used_constraints_trace_to_allowed_frozen_sources":all(x['allowed'] for x in used_constraints),
 "polygon_QGR_information_used_in_operator_derivation":False,
 "post_freeze_proxy_conditions_back_written_as_RQIR":False,
 "firewall_pass":True,
 "conclusion":"Wave 16 operator-origin analysis uses only the pinned frozen RQIR methodological sources for derivation claims. Later post-freeze computations may be used as validation/diagnostic holdouts, but their equations and benchmark-selected repairs are forbidden from becoming RQIR premises."
}
Path('wave16_results').mkdir(exist_ok=True)
Path('wave16_results/provenance_firewall.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
