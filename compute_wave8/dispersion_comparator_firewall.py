#!/usr/bin/env python3
import json
from pathlib import Path

anchors=[
 {"arxiv":"2202.08280","year":2022,"role":"gravitational Regge bounds; under stated assumptions two-subtraction dispersion relations and schematic local growth <= s^2"},
 {"arxiv":"2501.17949","year":2025,"role":"graviton-loop corrections to dispersive/positivity bounds; warns against naive fixed-t positivity in gravity"},
 {"arxiv":"2603.15755","year":2026,"role":"RG running and loop-sensitive gravitational positivity bookkeeping"},
 {"arxiv":"2607.14230","year":2026,"role":"strong factorization/positivity constraints in maximally supersymmetric gravitational EFTs can sharply restrict Wilson space and, with extra assumptions, isolate a string amplitude"}
]
routes=[
 {"mechanism":"two-subtraction dispersion + Regge growth","closest_comparator":"gravitational S-matrix dispersion/bootstrap","novel_by_itself":False},
 {"mechanism":"crossing/positivity + finite-state/tower assumptions","closest_comparator":"amplitude bootstrap / string-higher-spin UV completion","novel_by_itself":False},
 {"mechanism":"RG-corrected positivity","closest_comparator":"gravitational EFT + loop dispersion / asymptotic-safety positivity studies","novel_by_itself":False},
 {"mechanism":"shared latent primitive linking RG, spectral and amplitude data","closest_comparator":"none assigned until an explicit physical map is derived","novel_by_itself":False}
]
out={
 "test":"Wave-8 comparator firewall",
 "anchors":anchors,
 "routes":routes,
 "novelty_rule":"The synthetic existence of a low-dimensional cross-sector map is not novelty. Candidate Gravity only earns novelty if RQIR or another independently motivated physical principle derives a quantitative relation among RG-relevant coordinates, spectral data and amplitude/subtraction data that is not inherited from known bootstrap, string/Regge, FRG or EFT frameworks.",
 "candidate_novelty_earned":False,
 "conclusion":"Dispersion/Regge constraints are powerful but established. Wave 8 can identify the exact finite data a new theory must derive and can demonstrate the value of a shared latent law, but cannot claim new physics until the cross-sector law itself is physically derived and prospectively falsifiable."
}
Path('wave8_results').mkdir(exist_ok=True)
Path('wave8_results/dispersion_comparator_firewall.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
