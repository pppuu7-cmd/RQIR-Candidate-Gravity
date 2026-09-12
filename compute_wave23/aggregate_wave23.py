import json
from pathlib import Path

required={
 'integrity':'bank_integrity.json',
 'basis':'basis_invariance.json',
 'units':'unit_rescaling.json',
 'jackknife':'jackknife.json',
 'nuisance':'extended_nuisance.json',
 'omitted':'omitted_physics.json',
 'firewall':'information_firewall.json'
}

def find_one(filename):
    hits=list(Path('wave23_downloads').glob(f'**/{filename}'))
    return hits[0] if len(hits)==1 else None

loaded={}; missing=[]
for k,f in required.items():
    p=find_one(f)
    if p is None: missing.append(f)
    else: loaded[k]=json.loads(p.read_text())

signals={
 'frozen_bank_integrity_pass':bool(loaded.get('integrity',{}).get('integrity_pass',False)),
 'orthogonal_basis_all_rank_6':bool(loaded.get('basis',{}).get('all_rank_6',False)),
 'orthogonal_basis_singular_spectrum_invariant':bool(loaded.get('basis',{}).get('singular_spectrum_invariant_le_1e_12',False)),
 'orthogonal_basis_predictions_invariant':bool(loaded.get('basis',{}).get('predictions_invariant_le_1e_12',False)),
 'unit_rescaling_all_rank_6':bool(loaded.get('units',{}).get('all_rank_6',False)),
 'unit_rescaling_predictions_invariant':bool(loaded.get('units',{}).get('predictions_invariant_le_1e_12',False)),
 'all_leave_one_rank_6':bool(loaded.get('jackknife',{}).get('all_leave_one_rank_6',False)),
 'leave_two_full_rank_fraction_ge_0_80':bool(loaded.get('jackknife',{}).get('leave_two_full_rank_fraction_ge_0_80',False)),
 'extended_nuisance_rank_6':bool(loaded.get('nuisance',{}).get('profiled_rank_6',False)),
 'extended_nuisance_min_sv_ge_0_03':bool(loaded.get('nuisance',{}).get('profiled_min_sv_ge_0_03',False)),
 'omitted_shape_signal_residual_ge_0_05':bool(loaded.get('omitted',{}).get('signal_only_residual_fraction_ge_0_05',False)),
 'omitted_shape_nuisance_residual_ge_0_005':bool(loaded.get('omitted',{}).get('nuisance_aware_residual_fraction_ge_0_005',False)),
 'information_firewall_pass':bool(loaded.get('firewall',{}).get('firewall_pass',False))
}
all_present=len(missing)==0
all_true=all_present and all(signals.values())
out={
 'campaign':'holdout-stress-wave23',
 'all_required_present':all_present,
 'missing':missing,
 'signals':signals,
 'all_predeclared_signals_true':all_true,
 'wave22_bank_stronger_robustness_certified':all_true,
 'leave_one_full_rank_fraction':loaded.get('jackknife',{}).get('leave_one_full_rank_fraction'),
 'leave_two_full_rank_fraction':loaded.get('jackknife',{}).get('leave_two_full_rank_fraction'),
 'extended_nuisance_min_singular_value':loaded.get('nuisance',{}).get('profiled_min_singular_value'),
 'omitted_signal_residual_fraction':loaded.get('omitted',{}).get('signal_only_residual_fraction'),
 'omitted_nuisance_aware_residual_fraction':loaded.get('omitted',{}).get('signal_plus_sector_nuisance_residual_fraction'),
 'scientific_verdict':('Wave 23 certifies that the frozen Wave-22 prospective exam is not an artifact of orthogonal residual coordinates or parameter units, survives every single-probe deletion and the preregistered fraction of double deletions, remains full-rank under one additional drift nuisance, and leaves a detectable residual for the preregistered omitted seventh higher-momentum/helicity shape. This strengthens the future-candidate exam while remaining a finite proxy, not a completeness theorem.' if all_true else 'Wave 23 failed at least one preregistered robustness gate. The Wave-22 bank remains frozen and valid only at its prior certification level; the stronger robustness claim is not earned.'),
 'next_target':'If clean, freeze a Wave-23 robustness certificate. Continue the independent polygon route toward a concrete frozen QGR-P. When it exists, score it against the unchanged Wave-22 bank and use out-of-model residuals as a diagnostic rather than retuning the bank.'
}
text=json.dumps(out,indent=2,sort_keys=True)
Path('wave23_summary.json').write_text(text)
print(text)
if not all_true:
    raise SystemExit(2)
