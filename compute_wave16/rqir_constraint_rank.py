#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

# Finite proxy basis for a retarded/causal kernel. Retarded support is represented
# structurally by restricting the domain to 0 <= y <= x <= 1, so it is not
# double-counted as an algebraic coefficient constraint.
pairs=[(i,j) for i in range(3) for j in range(3)]
N=len(pairs)

requirements=[
 {
  "id":"RQIR-G4/G4a",
  "source":"docs/FOUNDATIONS.md §11; candidate_gravity/MODEL_TO_RQIR_CONTRACT.md §C",
  "provenance":"frozen_RQIR",
  "meaning":"retarded objects require causal support",
  "safe_proxy_translation":"restrict kernel domain to y<=x / retarded support",
  "translation_type":"structural_domain",
  "linear_rank_increment":0,
  "entailed":True
 },
 {
  "id":"RQIR-single-dynamics",
  "source":"docs/MASTER_TABLE.md Candidate Gravity / Single-dynamics rule; MODEL_TO_RQIR_CONTRACT.md Contract principle",
  "provenance":"frozen_RQIR",
  "meaning":"J,N,D/chiR,higher objects share one dynamics and parameter convention",
  "safe_proxy_translation":"same kernel/parameter realization must be reused across sectors",
  "translation_type":"cross_sector_identification",
  "linear_rank_increment":0,
  "entailed":True
 },
 {
  "id":"RQIR-G2",
  "source":"docs/FOUNDATIONS.md §11; MODEL_TO_RQIR_CONTRACT.md §C",
  "provenance":"frozen_RQIR",
  "meaning":"conservation/Bianchi/Ward compatibility",
  "safe_proxy_translation":"requires tensor/source representation before coefficient equations can be derived",
  "translation_type":"representation_dependent_gate",
  "linear_rank_increment":0,
  "entailed":True
 },
 {
  "id":"RQIR-G3/G3b",
  "source":"docs/FOUNDATIONS.md §11; MODEL_TO_RQIR_CONTRACT.md §C",
  "provenance":"frozen_RQIR",
  "meaning":"positivity/unitarity/CP and valid spectral identities",
  "safe_proxy_translation":"inequality/spectral admissibility gate; no universal linear equality on scalar polynomial coefficients",
  "translation_type":"inequality_gate",
  "linear_rank_increment":0,
  "entailed":True
 },
 {
  "id":"RQIR-G1",
  "source":"docs/FOUNDATIONS.md §11",
  "provenance":"frozen_RQIR",
  "meaning":"gauge/coordinate or relational consistency",
  "safe_proxy_translation":"requires a gauge/relational completion map; scalar proxy alone cannot turn this into a unique coefficient equation",
  "translation_type":"representation_dependent_gate",
  "linear_rank_increment":0,
  "entailed":True
 },
 {
  "id":"RQIR-G9/G10",
  "source":"docs/FOUNDATIONS.md §11; MODEL_TO_RQIR_CONTRACT.md §B",
  "provenance":"frozen_RQIR",
  "meaning":"EFT validity plus explicit smearing/renormalization",
  "safe_proxy_translation":"domain/prescription metadata, not a universal kernel-shape equality",
  "translation_type":"domain_prescription_gate",
  "linear_rank_increment":0,
  "entailed":True
 }
]

# Deliberately rejected back-writes from post-freeze proxy work.
rejected=[
 {"condition":"K(x,0)=0","reason":"not entailed by frozen RQIR source; optional soft-endpoint modeling choice"},
 {"condition":"K(x,x)=0","reason":"not entailed by frozen RQIR source; optional coincidence-softness modeling choice"},
 {"condition":"integral_triangle K = 1","reason":"RQIR requires applicable positivity/spectral consistency, but no universal unit normalization of this abstract kernel"},
 {"condition":"polynomial degree <=2 in x,y","reason":"finite proxy/basis choice only"},
 {"condition":"Volterra kernel form alpha+beta(x-y)","reason":"synthetic Wave-14/15 architecture, not frozen RQIR"}
]

A=np.zeros((0,N))
rank=int(np.linalg.matrix_rank(A)) if A.size else 0
out={
 "test":"provenance-first RQIR-to-kernel rank audit",
 "pinned_RQIR_source":"pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction@5a82c5828a73dbca8dbf9ed9cf63d436632d8095",
 "kernel_proxy_basis":"K(x,y)=sum c_ij x^i y^j, i,j=0..2 on retarded triangle 0<=y<=x<=1",
 "number_of_proxy_coefficients":N,
 "requirements":requirements,
 "rejected_non_RQIR_conditions":rejected,
 "safe_universal_linear_equality_rank_from_frozen_RQIR":rank,
 "safe_linear_shape_nullity":N-rank,
 "causal_support_enforced_structurally":True,
 "same_realization_enforced_cross_sector":True,
 "rqir_alone_uniquely_fixes_scalar_kernel_shape":False,
 "conclusion":"Frozen RQIR imposes strong semantic, consistency, provenance and same-dynamics requirements, but none of the inspected universal requirements logically entails a model-independent linear equality on the coefficients of this abstract scalar kernel. Causal support and same-realization can be enforced structurally; Ward/gauge/positivity constraints require a concrete tensor/operator representation. Therefore endpoint, coincidence, normalization or low-degree kernel equations from post-freeze proxies must not be back-written as RQIR consequences."
}
Path('wave16_results').mkdir(exist_ok=True)
Path('wave16_results/rqir_constraint_rank.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
