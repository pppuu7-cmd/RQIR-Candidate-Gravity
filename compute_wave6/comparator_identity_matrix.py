#!/usr/bin/env python3
import json
from pathlib import Path

routes=[
 {"route":"UV fixed point with finitely many relevant directions","closest_known_comparator":"asymptotic safety / functional RG","finite_parent_candidate":True,"novel_by_itself":False,"missing_for_RQIR_candidate":"new comparator-orthogonal relation fixing relevant coordinates/observables prospectively"},
 {"route":"finite-rank spectral recurrence / rational closure","closest_known_comparator":"spectral reconstruction / Padé / finite-pole ansatz","finite_parent_candidate":True,"novel_by_itself":False,"missing_for_RQIR_candidate":"physical derivation of rank and recurrence rather than assuming them"},
 {"route":"meromorphic Regge tower from finite analytic law","closest_known_comparator":"string/Regge/higher-spin completion","finite_parent_candidate":True,"novel_by_itself":False,"missing_for_RQIR_candidate":"new generating law or quantitative relation not equivalent to known Regge/string structure"},
 {"route":"nonperturbative transfer/path-integral state selection","closest_known_comparator":"lattice/path-integral/spinfoam/CDT-type nonperturbative programs","finite_parent_candidate":True,"novel_by_itself":False,"missing_for_RQIR_candidate":"unique independently motivated measure/state rule with RQIR observables"},
 {"route":"modular/algebraic state selection","closest_known_comparator":"algebraic QFT / modular bootstrap / holographic state-selection families","finite_parent_candidate":True,"novel_by_itself":False,"missing_for_RQIR_candidate":"gravity-specific finite axiom yielding prospective amplitudes or correlators"}
]
out={
 "test":"comparator identity firewall for all-order closure routes",
 "routes":routes,
 "routes_examined":len(routes),
 "routes_novel_by_name_only":0,
 "rule":"Do not count a route as Candidate Gravity novelty until it produces a quantitative comparator-orthogonal relation, observable, or closure law not inherited from its closest known school.",
 "conclusion":"All currently obvious all-order closure mechanisms sit close to established quantum-gravity/QFT programs. Novelty must therefore come from a new cross-constraint or finite generating principle, not from relabeling a known route."
}
Path('wave6_results').mkdir(exist_ok=True)
Path('wave6_results/comparator_identity_matrix.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
