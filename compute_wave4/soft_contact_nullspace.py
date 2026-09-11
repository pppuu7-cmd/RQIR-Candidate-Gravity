#!/usr/bin/env python3
import json
from pathlib import Path

OUT=Path("wave4_results"); OUT.mkdir(exist_ok=True)

# Algebraic four-point contact proxy with s+t+u=0 and crossing-symmetric
# generators sigma2 (degree 2) and sigma3 (degree 3).
# Under uniform soft scaling s,t,u -> eps(s,t,u), monomial sigma2^a sigma3^b
# scales eps^(2a+3b). If a finite soft/low-energy analysis fixes all terms up
# through degree P, every higher-degree contact term remains invisible to that
# finite-order constraint. Count the residual contact nullspace up to cutoff D.

records=[]
for D in range(4,25):
    mon=[]
    for a in range(D//2+1):
        for b in range(D//3+1):
            deg=2*a+3*b
            if deg>=2 and deg<=D:
                mon.append((a,b,deg))
    for P in [2,3,4,6,8,10]:
        fixed=[m for m in mon if m[2]<=P]
        free=[m for m in mon if m[2]>P]
        records.append({"max_degree":D,"soft_constraints_through_degree":P,"total_basis":len(mon),"fixed_or_seen":len(fixed),"residual_contact_nullspace":len(free)})

summary={
 "test":"finite-order soft/low-energy constraints versus higher contact terms",
 "records":records,
 "sample_D24": [r for r in records if r["max_degree"]==24],
 "result":"At any finite soft/derivative order P, increasing the EFT cutoff D leaves crossing-symmetric higher-degree contact directions unconstrained.",
 "scope":"scalarized crossing-symmetric contact proxy; not a full helicity-resolved graviton soft theorem"
}
(OUT/"soft_contact_nullspace.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
