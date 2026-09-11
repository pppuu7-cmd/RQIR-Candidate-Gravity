#!/usr/bin/env python3
import json
from pathlib import Path

# Crossing-symmetric massless 2->2 local contact basis with s+t+u=0.
# Use x=s^2+t^2+u^2 and y=s*t*u. At fixed t and large s, both x and y scale as s^2.
# Monomial x^a y^b therefore grows as s^[2(a+b)] in the Regge limit.
basis=[]
for a in range(5):
    for b in range(5):
        if a==0 and b==0:
            name='1'
        else:
            parts=[]
            if a: parts.append('x' if a==1 else f'x^{a}')
            if b: parts.append('y' if b==1 else f'y^{b}')
            name='*'.join(parts)
        basis.append({"a":a,"b":b,"name":name,"regge_power_s":2*(a+b),"total_invariant_order":a+b})

allowed=[q for q in basis if q['regge_power_s']<=2]
# Soft/no-constant condition removes 1. Fixing one leading low-energy contact coefficient (x) still leaves y.
soft_allowed=[q for q in allowed if not (q['a']==0 and q['b']==0)]
after_fix_x=[q for q in soft_allowed if q['name']!='x']

out={
 "test":"crossing-symmetric local contact freedom under schematic gravitational Regge growth <= s^2",
 "basis_scanned":len(basis),
 "regge_allowed_basis":[q['name'] for q in allowed],
 "regge_allowed_dimension":len(allowed),
 "after_soft_no_constant_basis":[q['name'] for q in soft_allowed],
 "after_soft_dimension":len(soft_allowed),
 "after_fix_one_leading_x_coefficient_basis":[q['name'] for q in after_fix_x],
 "residual_dimension_after_one_low_energy_fix":len(after_fix_x),
 "unique_after_regge_plus_soft_plus_one_fix":len(after_fix_x)==0,
 "conclusion":"A schematic s^2 Regge-growth bound drastically truncates polynomial contact freedom but does not by itself force uniqueness: in this symmetric proxy, x and y both survive after removing the constant, and one further low-energy matching condition still leaves one contact datum.",
 "scope":"crossing-symmetric polynomial counting proxy using s+t+u=0; not a proof of the complete graviton helicity-amplitude contact basis"
}
Path('wave8_results').mkdir(exist_ok=True)
Path('wave8_results/regge_contact_nullspace.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
