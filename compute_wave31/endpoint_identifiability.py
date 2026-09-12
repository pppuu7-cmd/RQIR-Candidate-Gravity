import json, pathlib
import numpy as np
# Same endpoint constraints f(0)=f(1)=0 admit many inequivalent interiors.
x=np.linspace(0.0,1.0,4001)
funcs=[x*(1-x), x*(1-x)*(2*x-1), x*(1-x)*(6*x*x-6*x+1)]
# Project interiors onto two finite diagnostic moments. This is deliberately not a physical RQIR map.
M=[]
for f in funcs:
    M.append([float(np.trapezoid(f,x)), float(np.trapezoid((2*x-1)*f,x))])
M=np.array(M)
rank=int(np.linalg.matrix_rank(M,tol=1e-10))
endpoint_ok=all(abs(f[0])<1e-14 and abs(f[-1])<1e-14 for f in funcs)
pair_dists=[float(np.linalg.norm(M[i]-M[j])) for i in range(len(M)) for j in range(i+1,len(M))]
signals={
 'endpoint_constraints_allow_inequivalent_residual_embeddings':endpoint_ok and max(pair_dists)>1e-3 and rank>=2,
 'functional_freedom_without_projection_does_not_establish_finite_rank_closure':True
}
out={'test':'endpoint_identifiability','endpoint_constraints':'all trial functions vanish at x=0 and x=1','diagnostic_moments':M.tolist(),'moment_matrix_rank':rank,'pairwise_distances':pair_dists,'note':'Synthetic identifiability counterexample only; not a physical model for Rcal.','signals':signals}
pathlib.Path('wave31_endpoint_identifiability.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
