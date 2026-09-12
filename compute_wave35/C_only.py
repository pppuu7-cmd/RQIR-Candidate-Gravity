from common import run_scenario,write
name='C_only'; rows=run_scenario(name)
signals={'C_cross_block_has_nonzero_orientation_leverage':max(r['median_max_principal_angle_rad'] or 0 for r in rows)>1e-4,'topology_changes_are_recorded_not_silently_discarded':all('topology_change_fraction' in r for r in rows)}
out={'test':name,'rows':rows,'signals':signals}; write('wave35_C_only.json',out); assert all(signals.values())
