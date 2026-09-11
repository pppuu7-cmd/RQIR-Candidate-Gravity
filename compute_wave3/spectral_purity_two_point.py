#!/usr/bin/env python3
import json
from pathlib import Path

OUT=Path("wave3_results")
OUT.mkdir(exist_ok=True)

# Positive Kallen-Lehmann-type TT proxy with a fixed unit-residue massless graviton:
# D(Q^2)=1/Q^2 + sum_i w_i/(Q^2+M_i^2), w_i>=0.
# Under the extra hypothesis "spectral purity" (no additional massive/continuum
# support), all w_i vanish and the two-point function is exactly the GR pole.
# Conversely, any positive-residue two-point deviation requires extra spectral support.

Q2_values=[0.05,0.1,0.25,0.5,1,2,5,10]
examples=[
    {"name":"pure_GR","masses":[],"weights":[]},
    {"name":"one_extra_state","masses":[2.0],"weights":[0.15]},
    {"name":"two_extra_states","masses":[1.5,5.0],"weights":[0.08,0.12]},
]
rows=[]
for ex in examples:
    vals=[]
    for q2 in Q2_values:
        gr=1.0/q2
        corr=sum(w/(q2+m*m) for m,w in zip(ex["masses"],ex["weights"]))
        vals.append({"Q2":q2,"GR":gr,"correction":corr,"total":gr+corr,"ratio_total_to_GR":(gr+corr)/gr})
    rows.append({"name":ex["name"],"extra_support_count":len(ex["masses"]),"values":vals})

summary={
  "test":"spectral purity of physical TT two-point function",
  "assumptions":["fixed unit-residue massless GR pole","positive extra spectral weights","no negative-norm cancellation"],
  "rigidity_statement":"If extra positive spectral support is forbidden, the TT two-point function is exactly the GR massless pole. Any positive-spectral two-point deviation requires additional states/resonance/continuum support.",
  "examples":rows,
  "does_spectral_purity_fix_two_point_to_GR":True,
  "does_it_fix_interactions_or_higher_points":False,
  "scope":"two-point spectral statement only; does not determine higher-point vertices or nonstandard analytic prescriptions"
}
(OUT/"spectral_purity_two_point.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
