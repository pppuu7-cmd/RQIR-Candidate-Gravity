#!/usr/bin/env python3
import json
import math
from pathlib import Path

# If an R^3-like cubic correction has four extra derivatives relative to the Einstein cubic seed,
# its amplitude ratio is schematically |alpha| E^4. The onset scale is E_* ~ |alpha|^{-1/4}.
alphas=[1e-2,1e-4,1e-6,1e-8,1e-10,1e-12]
records=[]
for a in alphas:
    Estar=a**(-0.25)
    ratios={str(f):a*(f*Estar)**4 for f in [0.1,0.3,1.0,3.0]}
    records.append({"alpha":a,"onset_E_star":Estar,"ratio_at_fraction_or_multiple_of_E_star":ratios})

out={
 "test":"dimensional onset scale associated with one residual higher-derivative cubic defect",
 "assumed_relative_scaling":"|delta A/A_EH| ~ |alpha| E^4",
 "records":records,
 "nonzero_defect_implies_finite_onset_scale":True,
 "conclusion":"Once all lower-order data are fixed, a nonzero four-extra-derivative cubic defect necessarily introduces a finite scale at which it becomes order one. This maps the remaining coefficient into a falsifiable scale but does not determine its value. In weakly coupled regimes sizeable higher-derivative graviton three-point deviations also carry the known CEMZ causality/UV-completion burden.",
 "scope":"dimensional scaling proxy; not a full eikonal causality computation and not a numerical bound on an R^3 Wilson coefficient"
}
Path('wave9_results').mkdir(exist_ok=True)
Path('wave9_results/higher_derivative_onset_scale.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
