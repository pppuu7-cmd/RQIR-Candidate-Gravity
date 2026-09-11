#!/usr/bin/env python3
import json
import math
from pathlib import Path

# Veneziano/Regge-style finite generative law proxy.
# alpha(s)=alpha0+alpha_prime*s; poles occur at alpha(s)=n.
alpha0=0.0
alpha_prime=0.5
N=16
m2=[(n-alpha0)/alpha_prime for n in range(N)]
spacing=[m2[i+1]-m2[i] for i in range(N-1)]

# Residue polynomial degree at the nth pole grows with n in the standard beta-function amplitude.
# We record only the tower-generating structure, not a full string spectrum.
residue_degrees=list(range(N))

out={
 "test":"finite Regge/Veneziano-like law generating an infinite pole tower",
 "alpha0":alpha0,
 "alpha_prime":alpha_prime,
 "first_mass_squared_poles":m2,
 "mass_squared_spacing":spacing,
 "residue_polynomial_degrees":residue_degrees,
 "finite_input_parameter_count":2,
 "infinite_tower_generated":True,
 "known_comparator_identity":"string/Regge-type meromorphic completion",
 "candidate_novel_by_itself":False,
 "conclusion":"A finite analytic rule can close infinitely many higher-spin/Regge poles, demonstrating the kind of compression an all-order parent law needs; however this mechanism is already a known string/Regge comparator and is not a new Candidate Gravity principle by itself.",
 "scope":"pole-spectrum/generative-law proxy; not a full critical-string amplitude or proof of UV completeness"
}
Path('wave6_results').mkdir(exist_ok=True)
Path('wave6_results/regge_tower_completion.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
