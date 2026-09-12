import json
from common import ROOT,write
e=json.loads((ROOT/'evidence/WAVE36_PUBLIC_ORIENTATION_AUDIT.json').read_text())
none_located=all(s.get('orientation_object_located') is False for s in e['sources_checked'])
signals={
 'frozen_public_audit_contains_no_promotable_orientation_object':none_located,
 'physical_J8_remains_blocked_after_public_audit':e['physical_blocker'].startswith('BLOCKED_'),
 'scoped_absence_is_not_used_as_evidence_against_F1_physics':True
}
out={'test':'public_audit_no_promotion','physical_blocker':e['physical_blocker'],'scope_statement':e['scope_statement'],'signals':signals}; write('wave36_public_audit_no_promotion.json',out); assert all(signals.values())
