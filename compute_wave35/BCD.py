from common import run_scenario,write
name='BCD'; rows=run_scenario(name)
med=[r['median_max_principal_angle_rad'] for r in rows]
mono=all(med[i+1] >= med[i]-0.01 for i in range(len(med)-1))
signals={'full_missing_block_ensemble_has_nonzero_orientation_leverage':max(med)>1e-4,'orientation_uncertainty_is_nondecreasing_with_scale_within_0p01rad_tolerance':mono,'topology_changes_are_recorded_not_silently_discarded':all('topology_change_fraction' in r for r in rows)}
out={'test':name,'rows':rows,'monotonic_tolerance_rad':0.01,'signals':signals}; write('wave35_BCD.json',out); assert all(signals.values())
