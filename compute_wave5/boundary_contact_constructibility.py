#!/usr/bin/env python3
import json
from pathlib import Path

OUT=Path("wave5_results"); OUT.mkdir(exist_ok=True)

# Algebraic proxy for boundary/contact ambiguity under a constructibility demand.
# Consider a crossing-symmetric local contact polynomial built from sigma2, sigma3.
# Under a generic complex shift in which hard invariants scale with z, every
# nonconstant polynomial contact term scales as a nonnegative power of z and
# therefore cannot vanish at |z|->infinity by itself. If the pole/factorization
# part already has the required falloff and the full amplitude is required to
# vanish at infinity, such independent polynomial boundary contacts are removed.
# This is a proxy for the role of BCFW boundary conditions, NOT a proof of gravity
# large-z behavior; the latter is an external theorem/literature input.

records=[]
for D in range(2,25):
    mons=[]
    for a in range(D//2+1):
        for b in range(D//3+1):
            deg=2*a+3*b
            if 2<=deg<=D:
                mons.append((a,b,deg))
    records.append({
        "max_contact_degree":D,
        "crossing_symmetric_contact_directions":len(mons),
        "directions_surviving_generic_boundary_free_condition":0,
        "directions_requiring_boundary_data_if_allowed":len(mons),
    })

summary={
 "test":"boundary-free constructibility versus local contact ambiguity",
 "records":records,
 "D24_contact_directions":records[-1]["crossing_symmetric_contact_directions"],
 "result":"In this polynomial proxy, boundary-free recursion removes independent local contact data; allowing a nonzero boundary restores a growing contact family.",
 "scope":"algebraic contact proxy. Actual graviton BCFW large-z falloff is external theory input and helicity/shift dependent."
}
(OUT/"boundary_contact_constructibility.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
