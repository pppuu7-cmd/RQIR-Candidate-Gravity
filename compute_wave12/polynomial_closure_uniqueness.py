#!/usr/bin/env python3
import json
from pathlib import Path

a,b=1.7,2.4
kappa=1.0/(a+b)
eigs=[n*(n+a+b-1.0)/(a+b) for n in range(1,7)]
out={
 "test":"extra polynomial-closure axiom applied to reversible Beta diffusion",
 "assumptions":[
   "local second-order diffusion Lf=A(x)f''+B(x)f' on [0,1]",
   "A is polynomial degree <=2 and vanishes at x=0,1",
   "B is polynomial degree <=1",
   "Beta(a,b) stationary density",
   "zero-current detailed balance",
   "first nonzero relaxation gap fixed to 1"
 ],
 "derivation":"A(0)=A(1)=0 with deg(A)<=2 forces A=kappa*x*(1-x). Detailed balance B=A'+A*d(log rho)/dx then forces B=kappa*[a-(a+b)x]. Fixing lambda_1=kappa(a+b)=1 fixes kappa=1/(a+b).",
 "a":a,"b":b,"kappa_for_unit_gap":kappa,
 "predicted_nonzero_eigenvalues_n1_to_n6":[float(x) for x in eigs],
 "unique_within_declared_polynomial_class_up_to_timescale":True,
 "timescale_fixed_by_gap":True,
 "known_comparator_identity":"Jacobi/Wright-Fisher diffusion",
 "candidate_new_physics":False,
 "conclusion":"A strong polynomial-closure axiom collapses the reversible family to the Jacobi/Wright-Fisher generator and the unit-gap condition fixes its remaining scale. This is mathematically sharp but belongs to a known comparator class, so the closure axiom cannot itself be counted as new QG physics."
}
Path('wave12_results').mkdir(exist_ok=True)
Path('wave12_results/polynomial_closure_uniqueness.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
