#!/usr/bin/env python3
import json
from pathlib import Path

OUT=Path("wave2_results")
OUT.mkdir(exist_ok=True)

# Minimal local four-derivative modification of the physical TT propagator:
#   D_2(k^2) = 1 / [ k^2 (1 - a k^2) ].
# For a>0, the extra pole is at k^2=1/a>0 but partial fractions give
#   D_2 = 1/k^2 - 1/(k^2-1/a),
# so the massive pole has negative residue (spin-2 ghost).
# For a<0 the extra pole is at negative k^2 in the chosen Minkowski pole
# convention, i.e. tachyonic mass^2. a=0 is the GR TT pole only.
# This is a scoped algebraic filter for the simplest polynomial q^4 TT deformation.

coeffs=[-10,-3,-1,-0.3,-0.1,0.0,0.1,0.3,1,3,10]
records=[]
for a in coeffs:
    if a==0:
        records.append({"a":a,"extra_pole":None,"classification":"GR_ONLY","massive_residue":None,"healthy_extra_spin2":False})
    elif a>0:
        m2=1.0/a
        records.append({"a":a,"extra_pole_k2":m2,"classification":"POSITIVE_MASS2_NEGATIVE_RESIDUE_GHOST","massive_residue":-1.0,"healthy_extra_spin2":False})
    else:
        m2=1.0/a
        records.append({"a":a,"extra_pole_k2":m2,"classification":"NEGATIVE_MASS2_TACHYONIC_POLE","massive_residue":-1.0,"healthy_extra_spin2":False})

summary={
 "test":"local four-derivative TT propagator pole scan",
 "propagator":"1/[k^2(1-a k^2)]",
 "records":records,
 "healthy_nonzero_a_found":any(r["healthy_extra_spin2"] for r in records),
 "analytic_statement":"For real nonzero a in this one-factor q^4 TT ansatz: a>0 gives a positive-mass extra pole with negative residue; a<0 gives negative mass^2. Only a=0 avoids both in this restricted ansatz.",
 "scope":"simplest local polynomial TT correction only; does not exclude nonlocal entire form factors, additional constrained fields, Lee-Wick/fakeon prescriptions, or more general UV completions"
}
(OUT/"local_q4_tt_poles.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
