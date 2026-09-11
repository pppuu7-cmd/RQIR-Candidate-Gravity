#!/usr/bin/env python3
import json
from pathlib import Path

anchors=[
 {"arxiv":"2111.13232","year":2021,"role":"positive graviton spectral function with massless one-graviton peak plus multi-graviton continuum in Lorentzian/asymptotic-safety framework"},
 {"arxiv":"2507.22169","year":2025,"role":"self-consistent positive graviton spectral function using full nonperturbative scattering continuum; massless peak plus multi-graviton continuum"},
 {"arxiv":"2606.19321","year":2026,"role":"Lorentzian quantum-gravity spectral functions with Ward-identity improvements and normalisable graviton spectral functions across GR-to-UV interpolation"}
]
out={
 "test":"finite-rank spectral closure versus current graviton-continuum comparator",
 "anchors":anchors,
 "full_graviton_spectrum_known_comparator_contains_continuum":True,
 "exact_finite_atomic_rank_as_full_spectrum_is_supported_by_these_anchors":False,
 "finite_rank_may_still_apply_to_reduced_effective_or_truncated_sector":True,
 "new_target":"A finite parent law for the full spectral sector should be sought as a finite generative equation/kernel/flow for a continuum, not automatically as a finite list of poles or fixed Hankel rank.",
 "conclusion":"Current Lorentzian spectral-QG calculations make a naive exact finite-atomic closure for the full graviton spectral function physically unattractive. This does not exclude finite-dimensional reduced descriptions, rational approximants, or a finite equation that generates a continuum.",
 "scope":"provenance/comparator firewall based on cited spectral-FRG literature; not a theorem that every quantum-gravity completion must have the same continuum."
}
Path('wave10_results').mkdir(exist_ok=True)
Path('wave10_results/continuum_comparator_firewall.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
