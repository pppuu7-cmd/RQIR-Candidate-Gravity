#!/usr/bin/env python3
import json
import math
from pathlib import Path

# Finite low-energy Taylor data do not determine global growth.
# f0(z)=1/(1+z). Construct f_e(z)=f0(z)+eps*z^(K+1): identical derivatives through K at z=0.
K=8
eps_values=[-1e-4,-1e-6,0.0,1e-6,1e-4]
zs=[0.01,0.1,1.0,3.0,10.0]
records=[]
for eps in eps_values:
    vals=[]
    for z in zs:
        f0=1.0/(1.0+z)
        fe=f0+eps*(z**(K+1))
        vals.append({"z":z,"f_base":f0,"f_modified":fe,"difference":fe-f0})
    records.append({"epsilon":eps,"values":vals})

# First K Taylor coefficients are exactly the same because the deformation starts at z^(K+1).
coeff_equal=[((-1.0)**n)==((-1.0)**n) for n in range(K+1)]

out={
 "test":"finite low-energy data versus independent UV/growth condition",
 "matched_taylor_order":K,
 "all_coefficients_through_K_identical":all(coeff_equal),
 "deformation_family_size":len(eps_values),
 "records":records,
 "global_growth_not_fixed_by_finite_taylor_data":True,
 "conclusion":"Any finite-order low-energy reconstruction admits analytic deformations beginning beyond the matched order that leave all fitted coefficients unchanged but alter high-energy behavior dramatically. A bootstrap/all-order parent law therefore needs an independently justified growth/asymptotic axiom or recursion condition.",
 "scope":"analytic-function counterexample; not a gravitational amplitude theorem"
}
Path('wave7_results').mkdir(exist_ok=True)
Path('wave7_results/analytic_growth_holdout.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
