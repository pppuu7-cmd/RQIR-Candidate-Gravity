#!/usr/bin/env python3
import json
from pathlib import Path

anchors=[
 {"year":2021,"arxiv":"2111.13232","claim":"Lorentzian RG computation of a positive graviton spectral function with massless peak and continuum in an asymptotic-safety setting."},
 {"year":2025,"arxiv":"2507.22169","claim":"Self-consistent positive graviton spectral function; physical on-shell scheme with unit total spectral weight reported."},
 {"year":2026,"arxiv":"2606.19321","claim":"Lorentzian quantum-gravity spectral functions with Ward-identity improvements and interpolation between GR and an asymptotically safe UV fixed point."}
]
out={
 "test":"current-literature comparator firewall for spectral plus RG closure",
 "anchors":anchors,
 "closest_known_comparator":"Lorentzian asymptotic safety / spectral functional RG",
 "positive_spectral_plus_fixed_point_route_is_novel_by_itself":False,
 "new_methodological_requirement":"Any RQIR candidate combining RG fixed-point scaling with spectral positivity must specify field/scheme, spectral normalization, Ward identities and the map from gauge-dependent correlators to operational observables before apparent scaling conflicts are interpreted physically.",
 "conclusion":"The spectral+RG route is active known literature, so Candidate Gravity novelty requires a comparator-orthogonal quantitative cross-relation rather than the coexistence of a positive spectral function and a UV fixed point alone."
}
Path('wave7_results').mkdir(exist_ok=True)
Path('wave7_results/current_spectral_rg_comparator.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
