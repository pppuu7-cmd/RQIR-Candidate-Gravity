#!/usr/bin/env python3
import json,glob,os
from pathlib import Path
files=glob.glob('wave16_downloads/*/*.json')
data={os.path.basename(p):json.load(open(p,encoding='utf-8')) for p in files}
need=['rqir_constraint_rank.json','translation_robustness.json','rqir_same_dynamics_rank.json','higher_order_closure_residual.json','provenance_firewall.json','minimal_extra_principle.json']
missing=[n for n in need if n not in data]
signals={
 'frozen_RQIR_constraints_have_clean_provenance':data.get('provenance_firewall.json',{}).get('firewall_pass',False),
 'single_dynamics_removes_sector_copy_nullity':data.get('rqir_same_dynamics_rank.json',{}).get('single_dynamics_removes_sector_copy_nullity',False),
 'safe_RQIR_translation_does_not_uniquely_fix_kernel_shape':not data.get('rqir_constraint_rank.json',{}).get('rqir_alone_uniquely_fixes_scalar_kernel_shape',True),
 'stronger_softness_mappings_are_not_RQIR_entailed':data.get('translation_robustness.json',{}).get('stronger_softness_conditions_must_not_be_called_RQIR_derived',False),
 'higher_order_closure_freedom_survives_without_extra_law':data.get('higher_order_closure_residual.json',{}).get('higher_order_freedom_survives_without_extra_law',False),
 'one_extra_shape_relation_would_close_strengthened_proxy_but_RQIR_does_not_supply_it':bool(data.get('minimal_extra_principle.json',{}).get('number_of_independent_extra_scalar_equalities_needed_in_this_proxy')==1 and not data.get('minimal_extra_principle.json',{}).get('rqir_supplies_value_for_any_detecting_functional',True))
}
allok=(not missing) and all(signals.values())
out={
 'campaign':'rqir-provenance-kernel-wave16',
 'missing':missing,
 'signals':signals,
 'all_required_present':allok,
 'rqir_single_dynamics_has_nontrivial_constraining_power':bool(signals['single_dynamics_removes_sector_copy_nullity']),
 'frozen_RQIR_alone_derives_unique_operator_kernel':False,
 'post_freeze_proxy_axioms_promoted_to_RQIR':False,
 'independent_extra_hypothesis_required_for_unique_C5_distinct_kernel':True,
 'candidate_new_QG_primitive_found':False,
 'scientific_verdict':'The provenance-first audit cleanly separates genuine frozen-RQIR consequences from post-freeze modeling choices. RQIR has real constraining power: causal support is structural, and the single-dynamics/same-parameter rule removes sector-copy null directions and forbids separate tuning of J,N,D/chiR or spectral/dispersion sectors. However, the inspected frozen RQIR requirements do not logically provide a model-independent coefficient equation fixing the internal shape of an abstract scalar kernel; Ward/gauge/positivity gates require a concrete representation, and higher-order closure remains free without additional microscopic dynamics. Endpoint softness, coincidence softness, unit normalization of the abstract kernel and Volterra/polynomial forms are therefore not allowed to be back-written as RQIR axioms. In the already-strengthened Wave-15 finite proxy, only one further independent shape relation would be mathematically sufficient, but frozen RQIR supplies neither its value nor its physical origin. This is consistent with the frozen independent reconstruction: RQIR v1.0 defines an equivalence class, not a unique C5-distinct microscopic theory.',
 'next_target':'Wave 17: do not invent the missing relation. Search independent physical EXTRA-HYPOTHESIS candidates outside RQIR—each with explicit provenance, gravitational motivation, comparator distinction and falsifiable cross-sector consequences. Run them in parallel through the same frozen RQIR gates. Promising classes: gravity-specific composition/locality principle, UV/IR self-similarity tied to gravitational scaling, relational-information conservation, or a microscopic causal-kernel law. Keep at least one branch as a no-extra-hypothesis control. Any candidate chosen only because it kills the residual null vector is REJECTED-AS-RETROFIT.',
 'scope':'provenance/rank audit on a finite scalar kernel proxy plus the frozen RQIR equivalence-class authority; not a theorem that concrete tensor realizations cannot acquire additional Ward/gauge restrictions.'
}
Path('wave16_summary.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
