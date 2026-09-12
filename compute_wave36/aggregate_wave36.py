import json, pathlib
required=['wave36_audit_registry.json','wave36_valid_matrix_candidate.json','wave36_provenance_rejections.json','wave36_matrix_eigenbasis_consistency.json','wave36_complex_pair_realification.json','wave36_public_audit_no_promotion.json','wave36_information_firewall.json']
found={}
for p in pathlib.Path('wave36_downloads').rglob('*.json'):
    if p.name in required: found[p.name]=json.loads(p.read_text())
all_present=all(k in found for k in required)
signals={}
for obj in found.values(): signals.update(obj.get('signals',{}))
all_true=bool(signals) and all(bool(v) for v in signals.values())
summary={
 'campaign':'f1-public-orientation-audit-wave36',
 'classification':'SCOPED_PUBLIC_SOURCE_AUDIT_PLUS_DROPIN_VALIDATOR',
 'all_required_present':all_present,
 'all_predeclared_signals_true':all_true,
 'audited_public_orientation_object_located':False,
 'blocking_object':'BLOCKED_NO_PUBLIC_SAME_REALIZATION_5X5_STABILITY_MATRIX_OR_RIGHT_EIGENSYSTEM_LOCATED_IN_AUDITED_SOURCES_AND_NEW_FRG_OR_PRIVATE_ARTIFACT_INPUT_STILL_REQUIRED',
 'scientific_verdict':'Wave 36 closes the public-source audit only in a scoped sense and freezes an executable acceptance boundary for future orientation data. The audited Springer/arXiv/SCOAP3/INSPIRE/GitHub source registry contains no located reusable same-realization five-dimensional stability matrix or right eigensystem. This does not prove global absence. The drop-in validator accepts a provenance-complete 5x5 orientation object, rejects critical exponents alone and incomplete/wrong-closure objects, and verifies matrix/eigenbasis projector consistency including complex-pair realification. Physical J8 remains blocked because no audited public candidate supplies the required orientation data.',
 'next_target':'Wave 37: freeze and test the minimal new-FRG-computation request. Specify the exact 25 beta derivatives under the F1 closure, finite-difference/automatic-differentiation consistency tolerances, fixed-point residual tests, eigenpair residual tests, and a seven-trajectory handoff artifact compatible with Wave 33.',
 'signals':signals
}
pathlib.Path('wave36_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)); print(json.dumps(summary,indent=2,sort_keys=True)); assert all_present and all_true
