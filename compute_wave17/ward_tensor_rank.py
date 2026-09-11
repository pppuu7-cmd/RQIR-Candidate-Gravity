import numpy as np
from common import projectors, conserved_tensor, contract, write_result

k=np.array([0.6,-0.1,0.7,0.2])
P,theta,_=projectors(k)
basis=['P2','P1','P0s','P0w','P0sw','P0ws']
rng=np.random.default_rng(1703)
rows_cons=[]
rows_generic=[]
for _ in range(14):
    T=conserved_tensor(rng,theta); U=conserved_tensor(rng,theta)
    rows_cons.append([contract(T,P[n],U) for n in basis])
    S=rng.normal(size=(4,4)); S=0.5*(S+S.T)
    V=rng.normal(size=(4,4)); V=0.5*(V+V.T)
    rows_generic.append([contract(S,P[n],V) for n in basis])
A=np.asarray(rows_cons); G=np.asarray(rows_generic)
sv=np.linalg.svd(A,compute_uv=False); svg=np.linalg.svd(G,compute_uv=False)
rank=int(np.linalg.matrix_rank(A,tol=1e-10)); rankg=int(np.linalg.matrix_rank(G,tol=1e-10))
nullity=len(basis)-rank
column_norms={basis[i]:float(np.linalg.norm(A[:,i])) for i in range(len(basis))}
out={
 'test':'observable rank of general symmetric-tensor kernel under conserved-source Ward reduction',
 'basis':basis,
 'conserved_source_rank':rank,
 'conserved_source_nullity':nullity,
 'generic_source_rank':rankg,
 'singular_values_conserved':sv.tolist(),
 'singular_values_generic':svg.tolist(),
 'conserved_column_norms':column_norms,
 'only_two_transverse_structures_survive': rank==2 and nullity==4 and column_norms['P2']>1e-6 and column_norms['P0s']>1e-6 and max(column_norms[n] for n in ['P1','P0w','P0sw','P0ws'])<1e-10,
 'ward_conservation_has_nontrivial_rank_reduction': rankg>=5 and rank==2,
 'conclusion':'The concrete tensor representation turns the frozen conservation/Ward gate into a measurable rank reduction: four longitudinal/mixed coefficient directions become operationally null for conserved sources, but two independent transverse structures survive.'
}
write_result('ward_tensor_rank',out)
