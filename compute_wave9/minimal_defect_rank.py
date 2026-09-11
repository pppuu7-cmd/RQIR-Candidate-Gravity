#!/usr/bin/env python3
import json
import numpy as np
from pathlib import Path

# Toy finite parameter vector after earlier truncation:
# q=(g2,g3,g4,cx,cy), where g2,g3,g4 are Newton-coupling avatars and cx,cy
# represent the two Regge-allowed nonconstant crossing-symmetric contact directions from Wave 8.
# Known-structure constraints:
# 1) effective/universal Newton coupling avatars: g2=g3=g4 (two constraints)
# 2) one operational Newton normalization fixes the common g
# 3) one leading low-energy contact input fixes cx
# This should leave exactly cy as a residual defect.

gN=0.62
cx0=0.14
A=np.array([
 [1,-1,0,0,0],
 [0,1,-1,0,0],
 [1,0,0,0,0],
 [0,0,0,1,0],
],float)
b=np.array([0,0,gN,cx0],float)
rank=int(np.linalg.matrix_rank(A))
nullity=5-rank
q_part=np.linalg.lstsq(A,b,rcond=None)[0]
U,S,Vt=np.linalg.svd(A)
null_basis=Vt[rank:,:]

out={
 "test":"combined Newton-avatar universality + normalization + Regge-contact matching",
 "parameter_order":["g2","g3","g4","cx","cy"],
 "initial_parameter_dimension":5,
 "constraint_rank":rank,
 "residual_nullity":nullity,
 "singular_values":S.tolist(),
 "particular_solution":q_part.tolist(),
 "null_basis":null_basis.tolist(),
 "single_residual_defect_is_cy":bool(nullity==1 and abs(abs(null_basis[0,4])-1.0)<1e-10 and np.max(np.abs(null_basis[0,:4]))<1e-10),
 "conclusion":"In this finite bookkeeping proxy, known universality/normalization plus one leading Regge-contact input reduce the post-freeze theory space to one independent higher-derivative contact datum cy. This localizes, rather than solves, the missing physics.",
 "scope":"constraint-rank bookkeeping proxy; effective Newton-coupling universality is a known comparator property, not an exact theorem imposed on all quantum-gravity formulations"
}
Path('wave9_results').mkdir(exist_ok=True)
Path('wave9_results/minimal_defect_rank.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
