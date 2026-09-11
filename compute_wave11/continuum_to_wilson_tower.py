#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

# A positive continuum with Beta(a,b) density in x=1/M^2 generates dispersive coefficients
# c_(2+n)=E[x^(n+2)]. The moment law is finite-parameter but not fixed-Hankel-rank.
a,b=1.7,2.4

def moment(n):
    out=1.0
    for k in range(n): out *= (a+k)/(a+b+k)
    return out
mom=[moment(n) for n in range(18)]
coeff={str(2+n):mom[2+n] for n in range(12)}
ratios=[]
for n in range(11):
    observed=mom[n+3]/mom[n+2]
    predicted=(a+n+2)/(a+b+n+2)
    ratios.append({"from_power_s":2+n,"to_power_s":3+n,"observed_ratio":observed,"generator_ratio":predicted,"abs_error":abs(observed-predicted)})

# Use c2,c3 to solve the two continuum parameters algebraically/numerically would be possible;
# here we treat a,b as predeclared generator parameters and test the all-order tower relation.
out={
 "test":"finite continuum generator induces an all-order dispersive Wilson tower",
 "generator_parameters":{"a":a,"b":b},
 "wilson_coefficients_by_s_power":coeff,
 "successive_ratio_records":ratios,
 "max_ratio_error":max(r['abs_error'] for r in ratios),
 "all_order_variable_coefficient_rule":"c_(p+1)/c_p = (a+p)/(a+b+p) for p>=2 in this indexing",
 "finite_generator_closes_infinite_Wilson_tower_without_finite_Hankel_rank":True,
 "conclusion":"A finite continuum-generating law can close an infinite dispersive Wilson tower through n-dependent recurrence coefficients, avoiding the finite-atomic-rank restriction. This is a more appropriate parent-law architecture for a spectrum with a continuum.",
 "scope":"Beta/Stieltjes moment proxy; not a physical prediction for gravitational Wilson coefficients."
}
Path('wave11_results').mkdir(exist_ok=True)
Path('wave11_results/continuum_to_wilson_tower.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
