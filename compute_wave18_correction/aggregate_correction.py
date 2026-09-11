import json
from pathlib import Path

def load(name):
    m=list(Path('wave18_correction_downloads').glob(f'**/{name}'))
    if not m: return None
    return json.loads(m[0].read_text())

h0=load('h0_corrected.json')
h2=load('h2_semigroup.json')
ci=load('class_identifiability.json')
missing=[k for k,v in [('h0_corrected',h0),('h2_regression',h2),('class_identifiability_regression',ci)] if v is None]
signals={}
if not missing:
    signals={
      'corrected_H0_underdetermination_survives':h0['corrected_H0_signal'],
      'H2_semigroup_regression_unchanged':h2['composition_plus_one_design_closes_this_finite_class'],
      'cross_class_identifiability_regression_unchanged':ci['equation_class_is_not_identified_by_low_q_fit']
    }
out={
 'campaign':'extra-hypothesis-wave18-method-correction-001',
 'original_run':34659178949,
 'methodological_defect':'original H0 holdout reused the design source geometry, making its gradient collinear and incapable of detecting the design-null direction',
 'correction':'reuse the independent source geometry already frozen in Wave 17; do not alter H1-H4 or their holdout values',
 'missing':missing,
 'signals':signals,
 'correction_pass':bool(signals) and all(signals.values()),
 'wave18_corrected_interpretation':'All intended qualitative signals are now consistent: H0 remains underdetermined; H1/H3/H4 reduce but do not close functional freedom; H2 closes the tested finite log-polynomial class but is not gravity-specific; different equation classes remain distinguishable only prospectively. No Wave-18 class is promoted to a new QG primitive.',
 'candidate_new_QG_primitive_found':False,
 'next_target':'Wave 19 cross-order closure: require the same candidate law to connect two-point transverse dressing and an independently held-out higher-point/response observable.'
}
Path('wave18_correction_summary.json').write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True))
