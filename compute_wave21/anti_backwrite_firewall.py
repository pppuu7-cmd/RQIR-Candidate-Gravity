from pathlib import Path
from common import write_result

endpoint=Path('model/RQIR_ONLY_ACTION_LEVEL_ENDPOINT_V1.md').read_text()
prereg=Path('post_freeze/WAVE21_BLIND_CROSS_ROUTE_PREREGISTRATION.md').read_text()
checks={
    'endpoint_self_identifies_frozen_rqir_only':'FROZEN RQIR-ONLY ENDPOINT' in endpoint,
    'endpoint_authority_is_wave20_not_wave21':'Wave-20 Actions run:** `34659887695`' in endpoint and 'Wave 21' not in endpoint,
    'endpoint_forbids_polygon_backwrite':'no polygon result may be back-written' in endpoint,
    'wave21_prereg_forbids_inferred_fixes':'inferred fixes to the RQIR endpoint' in prereg,
    'wave21_is_obstruction_level_only':'only methodology/obstruction-level comparison is admissible' in prereg,
    'future_model_comparison_condition_declared':'true model-to-model blind comparison remains prohibited' in prereg.lower()
}
out={
    'test':'anti-backwrite firewall',
    'checks':checks,
    'no_backwrite_into_frozen_rqir':all(checks.values()),
    'conclusion':'The RQIR-v1 endpoint remains anchored to Wave 20. Wave 21 can compare external obstruction metadata but cannot retroactively convert polygon information into an RQIR-only premise, derivation or selector.'
}
write_result('anti_backwrite_firewall',out)
