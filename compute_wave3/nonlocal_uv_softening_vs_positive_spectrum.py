#!/usr/bin/env python3
import json, math
from pathlib import Path

OUT=Path("wave3_results")
OUT.mkdir(exist_ok=True)

# Compare a common entire UV-softened proxy
#   D_entire(Q^2)=exp(-ell^2 Q^2)/Q^2
# with a standard positive spectral representation at fixed unit massless residue
#   D_KL(Q^2)=1/Q^2 + integral rho(mu^2)/(Q^2+mu^2), rho>=0.
# For Q^2>0 every positive spectral correction is nonnegative, hence D_KL>=1/Q^2.
# But D_entire<1/Q^2 for ell>0. Therefore the target cannot be represented by
# such a positive spectral density with the same massless residue.

ell=[0.25,0.5,1.0,2.0]
Q2=[0.01,0.05,0.1,0.25,0.5,1,2,5,10,20]
rows=[]
for L in ell:
    vals=[]
    all_below=True
    for x in Q2:
        gr=1.0/x
        target=math.exp(-(L*L)*x)/x
        gap=gr-target
        all_below=all_below and target < gr
        vals.append({"Q2":x,"GR_lower_bound_for_positive_extra_spectrum":gr,"entire_target":target,"gap":gap,"target_below_bound":target<gr})
    rows.append({"ell":L,"all_test_points_below_positive_spectral_bound":all_below,"values":vals})

summary={
 "test":"entire exponential UV softening versus positive KL-type TT spectrum",
 "target":"exp(-ell^2 Q^2)/Q^2",
 "assumptions":["unit massless GR residue","nonnegative additional spectral density","ordinary additive Kallen-Lehmann/Stieltjes form"],
 "analytic_result":"For every ell>0 and Q^2>0, exp(-ell^2 Q^2)/Q^2 < 1/Q^2, whereas adding nonnegative spectral weight gives D(Q^2)>=1/Q^2. Thus this target is incompatible with the stated positive-spectral assumptions.",
 "rows":rows,
 "positive_spectral_representation_possible_under_assumptions":False,
 "scope":"specific exponentially softened two-point proxy and standard positive spectral assumptions; does not exclude nonstandard inner products, subtractions, gauge-dependent propagators, fakeons, or other nonlocal prescriptions"
}
(OUT/"nonlocal_uv_softening_vs_positive_spectrum.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
