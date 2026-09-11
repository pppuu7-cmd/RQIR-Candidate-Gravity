#!/usr/bin/env python3
import json
from pathlib import Path

anchors=[
 {"arxiv":"1804.00012","role":"effective universality of different dynamical Newton-coupling avatars in an asymptotic-safety gravity-matter computation"},
 {"arxiv":"1706.00759","role":"generic sub-subleading soft-graviton theorem contains universal and theory-dependent/non-universal contributions involving two- and three-point data"},
 {"arxiv":"1407.5597","role":"CEMZ causality constraints on sizeable higher-derivative graviton three-point couplings in the weakly coupled regime"},
 {"arxiv":"2202.08280","role":"gravitational Regge/dispersion growth constraints"}
]
out={
 "test":"minimal-defect comparator and provenance firewall",
 "anchors":anchors,
 "known_constraints_can_localize_one_higher_derivative_defect":True,
 "known_constraints_by_themselves_derive_defect_value":False,
 "spectral_recurrence_route_is_novel_by_itself":False,
 "novelty_requirement":"A Candidate Gravity advance requires an independently motivated physical principle that derives the remaining higher-derivative/contact datum or derives the spectral recurrence that predicts it, with an untouched prospective holdout. Reusing effective universality, soft theorems, Regge bounds, CEMZ or a chosen finite-pole recurrence is not novelty by itself.",
 "conclusion":"The scientifically valuable outcome of Wave 9 is expected to be localization of the missing physics to a very small datum set and a prospective validation protocol, not a claim that a new quantum-gravity law has already been found."
}
Path('wave9_results').mkdir(exist_ok=True)
Path('wave9_results/minimal_defect_comparator_firewall.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
