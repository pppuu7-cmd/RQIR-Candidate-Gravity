#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

pairs=[(i,j) for i in range(3) for j in range(3)]
N=len(pairs)

def row_for_y0(i): return np.array([1.0 if (ii,jj)==(i,0) else 0.0 for ii,jj in pairs])
def row_for_diag_degree(k): return np.array([1.0 if ii+jj==k else 0.0 for ii,jj in pairs])

def rank(rows):
    if not rows: return 0
    A=np.vstack(rows)
    return int(np.linalg.matrix_rank(A,tol=1e-12))

encodings=[]
# Only causality as explicitly required by RQIR: support is in the domain, not coefficient equations.
encodings.append({"name":"RQIR-causality-only","status":"entailed","rows":[],"notes":"retarded support via domain y<=x"})
# Optional stronger mappings that are compatible with causality but not entailed by the frozen text.
encodings.append({"name":"plus-endpoint-softness","status":"compatible_not_entailed","rows":[row_for_y0(i) for i in range(3)],"notes":"adds K(x,0)=0"})
encodings.append({"name":"plus-coincidence-softness","status":"compatible_not_entailed","rows":[row_for_diag_degree(k) for k in range(5)],"notes":"adds K(x,x)=0"})
encodings.append({"name":"plus-both-softness-conditions","status":"compatible_not_entailed","rows":[row_for_y0(i) for i in range(3)]+[row_for_diag_degree(k) for k in range(5)],"notes":"Wave-15 style proxy strengthening"})

records=[]
for e in encodings:
    r=rank(e['rows'])
    records.append({"name":e['name'],"status":e['status'],"constraint_rank":r,"shape_nullity":N-r,"notes":e['notes']})
entailed=[r for r in records if r['status']=='entailed']
optional=[r for r in records if r['status']!='entailed']
out={
 "test":"robustness of RQIR-to-kernel translation against stronger but non-entailed encodings",
 "number_of_coefficients":N,
 "records":records,
 "entailed_mapping_rank":entailed[0]['constraint_rank'],
 "entailed_mapping_nullity":entailed[0]['shape_nullity'],
 "optional_mapping_rank_range":[min(r['constraint_rank'] for r in optional),max(r['constraint_rank'] for r in optional)],
 "optional_mapping_nullity_range":[min(r['shape_nullity'] for r in optional),max(r['shape_nullity'] for r in optional)],
 "translation_choice_materially_changes_rank":True,
 "stronger_softness_conditions_must_not_be_called_RQIR_derived":True,
 "conclusion":"The kernel rank can appear to improve dramatically if one silently strengthens causal support into endpoint or coincidence softness equations. Those stronger conditions are compatible modeling choices, not consequences of the frozen RQIR text. Wave 16 therefore accepts only the structural retarded-support translation as RQIR-entitled and treats the resulting large shape nullity as a genuine underdetermination rather than repairing it by interpretation."
}
Path('wave16_results').mkdir(exist_ok=True)
Path('wave16_results/translation_robustness.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
