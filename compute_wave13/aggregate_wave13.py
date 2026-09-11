#!/usr/bin/env python3
import json,glob,os
from pathlib import Path
files=glob.glob('wave13_downloads/*/*.json')
data={os.path.basename(p):json.load(open(p,encoding='utf-8')) for p in files}
need=['endpoint_sumrule_nullspace.json','finite_ward_sumrules_nullspace.json','stieltjes_dispersion_holdout.json','uv_ir_asymptotic_nullspace.json','comparator_firewall.json']
missing=[n for n in need if n not in data]
signals={
 'positive_unit_weight_low_moment_endpoint_constraints_leave_nullspace': data.get('endpoint_sumrule_nullspace.json',{}).get('finite_static_constraints_leave_functional_null_direction',False),
 'five_exact_sum_rules_still_leave_nullspace': data.get('finite_ward_sumrules_nullspace.json',{}).get('finite_number_of_sum_rules_not_functionally_complete',False),
 'nonlocal_dispersion_holdouts_resolve_static_nullspace': data.get('stieltjes_dispersion_holdout.json',{}).get('nonlocal_holdouts_discriminate_static_nullspace',False),
 'fixed_IR_UV_power_laws_still_leave_interior_nullspace': data.get('uv_ir_asymptotic_nullspace.json',{}).get('same_asymptotic_exponents_across_deformations',False),
 'static_constraints_are_comparator_gates_not_new_dynamics': data.get('comparator_firewall.json',{}).get('finite_positivity_sumrule_asymptotic_constraints_are_not_new_physics',False)
}
out={
 'campaign':'post-freeze-spectral-selector-wave13',
 'missing':missing,
 'signals':signals,
 'all_required_present':(not missing) and all(signals.values()),
 'positivity_normalization_IR_UV_asymptotics_and_finite_sum_rules_sufficient_for_unique_continuum':False,
 'genuine_dynamical_equation_or_kernel_required':True,
 'candidate_new_QG_primitive_found':False,
 'scientific_verdict':'Current Lorentzian-QG-inspired static spectral gates—positivity, unit total weight, fixed IR/UV power laws and finitely many exact Ward/sum-rule moments—do not uniquely determine a continuum. Constructive positive deformations preserve these constraints while changing higher moments and nonlocal Stieltjes/dispersion observables. Therefore the missing parent law cannot be a finite checklist of spectral properties; it must be a dynamical flow/integral/functional equation or kernel that fixes the interior continuum and predicts holdouts. Any such equation must be comparator-distinct from spectral FRG, Schwinger-Dyson and bootstrap/dispersion frameworks.',
 'next_target':'Wave 14: search finite QG-specific dynamical equations for the spectral density/kernel. Test candidate first-order nonlinear flow, Volterra/Fredholm self-consistency, and Ward-coupled flow architectures. Freeze equation form before fitting; use static gates only as admissibility constraints and reserve Stieltjes/time-domain observables as prospective holdouts. Reject equations equivalent by reparameterization to known spectral-FRG/SD/bootstrap comparators.',
 'scope':'constructive functional-nullspace tests in positive spectral-density proxies informed by current Lorentzian-QG constraints; not a theorem that every possible infinite set of Ward identities is incomplete.'
}
Path('wave13_summary.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
