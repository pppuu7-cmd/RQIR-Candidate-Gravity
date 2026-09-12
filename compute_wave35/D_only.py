from common import run_scenario,write
name='D_only'; rows=run_scenario(name)
signals={'D_block_alone_has_nonzero_orientation_or_topology_leverage':max((r['median_max_principal_angle_rad'] or 0)+r['topology_change_fraction'] for r in rows)>1e-4,'topology_changes_are_recorded_not_silently_discarded':all('topology_change_fraction' in r for r in rows)}
out={'test':name,'rows':rows,'signals':signals}; write('wave35_D_only.json',out); assert all(signals.values())
