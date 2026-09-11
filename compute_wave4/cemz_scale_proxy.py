#!/usr/bin/env python3
import json, math
from pathlib import Path

OUT=Path("wave4_results"); OUT.mkdir(exist_ok=True)

# Dimensional proxy for a six-derivative R^3-like correction to a two-derivative
# Einstein graviton interaction: relative correction Delta_3(E) ~ c6 (E/M)^4.
# This is NOT a derivation of the CEMZ theorem. It converts a preselected Wilson
# coefficient and target fractional deviation into the energy fraction E/M at
# which the correction becomes visible/order-one. CEMZ-type causality results are
# a separate literature input saying large such corrections cannot be isolated
# arbitrarily far below the additional higher-spin physics in weakly coupled gravity.

cs=[0.01,0.1,1.0,10.0,100.0]
deltas=[1e-6,1e-4,1e-2,0.1,1.0]
rows=[]
for c in cs:
    vals=[]
    for d in deltas:
        em=(d/c)**0.25
        vals.append({"target_fractional_deviation":d,"E_over_M":em})
    rows.append({"c6_dimensionless":c,"thresholds":vals})

summary={
 "test":"dimensional onset scale for a six-derivative graviton cubic correction",
 "proxy":"Delta_3(E)=c6*(E/M)^4",
 "rows":rows,
 "interpretation":"A measurable higher-derivative three-graviton correction determines a characteristic scale relative to its suppressing scale. Causality constraints from CEMZ are not re-derived here and must be applied as external theory input.",
 "scope":"dimensional bookkeeping only; not a causality proof and not a model selection theorem"
}
(OUT/"cemz_scale_proxy.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
