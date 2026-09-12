import json
from common import ROOT,write
p=ROOT/'evidence/WAVE36_PUBLIC_ORIENTATION_AUDIT.json'; e=json.loads(p.read_text())
sources=e['sources_checked']
explicit=all('orientation_object_located' in s for s in sources)
none_located=all(s['orientation_object_located'] is False for s in sources)
scope=e.get('scope_statement','').lower()
signals={
 'all_audited_sources_have_explicit_orientation_object_result':explicit,
 'no_orientation_object_located_in_frozen_audited_registry':none_located,
 'audit_scope_explicitly_disclaims_global_nonexistence_claim':('not a proof' in scope and 'elsewhere' in scope)
}
out={'test':'audit_registry','source_count':len(sources),'sources':[s['source'] for s in sources],'scope_statement':e['scope_statement'],'signals':signals}; write('wave36_audit_registry.json',out); assert all(signals.values())
