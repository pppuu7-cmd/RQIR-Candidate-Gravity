import numpy as np
from common import write_result

# Two proxy classes with the same massless IR normalization.
# Rational local higher-derivative modifier: 1/[x(1+alpha x)] has an extra finite denominator root.
# Entire modifier exp(-ell^2 x)/x has no additional finite poles but retains continuous shape freedom.
alphas=[-1.0,-0.3,0.3,1.0]
rational=[]
for a in alphas:
    root=None if abs(a)<1e-15 else -1.0/a
    rational.append({'alpha':a,'extra_denominator_root_x':root,'finite_extra_root':root is not None})

ells=[0.0,0.4,0.8,1.2]
xh=0.7
entire=[]
for ell in ells:
    modifier=float(np.exp(-(ell**2)*xh))
    entire.append({'ell':ell,'modifier_at_x_0p7':modifier,'finite_extra_poles':0,'IR_modifier':1.0})
width=max(r['modifier_at_x_0p7'] for r in entire)-min(r['modifier_at_x_0p7'] for r in entire)

out={
 'test':'no-extra-pole audit does not uniquely determine transverse form-factor shape',
 'rational_higher_derivative_family':rational,
 'entire_pole_free_family':entire,
 'pole_free_holdout_width_at_x_0p7':width,
 'rational_polynomial_denominator_generically_adds_finite_root': all(r['finite_extra_root'] for r in rational),
 'pole_free_entire_family_retains_shape_parameter': width>1e-3,
 'no_extra_pole_gate_is_not_a_unique_selector': width>1e-3,
 'scope_note':'This is an analytic-structure proxy, not a full Lorentzian ghost/unitarity theorem; physical pole interpretation depends on continuation, residues and gauge-invariant amplitudes.',
 'conclusion':'Excluding extra finite propagator poles removes a broad local rational deformation class but still does not select a unique kernel: pole-free entire form factors share the same IR residue and vary at finite momentum. Pole absence is therefore a gate, not the missing parent law.'
}
write_result('pole_audit',out)
