import numpy as np
from common import projectors, compose, conserved_tensor, contract, write_result

k = np.array([0.7,-0.2,0.5,1.1])
P, theta, omega = projectors(k)
projector_names = ['P2','P1','P0s','P0w']
expected_rank = {'P2':5.0,'P1':3.0,'P0s':1.0,'P0w':1.0}
idempotence = {n: float(np.linalg.norm(compose(P[n],P[n])-P[n])) for n in projector_names}
traces = {n: float(np.einsum('mnmn->',P[n])) for n in projector_names}
orthogonality = {}
for i,a in enumerate(projector_names):
    for b in projector_names[i+1:]:
        orthogonality[f'{a}:{b}'] = float(np.linalg.norm(compose(P[a],P[b])))

rng = np.random.default_rng(1701)
T = conserved_tensor(rng, theta)
U = conserved_tensor(rng, theta)
conservation_T = float(np.linalg.norm(k @ T))
conservation_U = float(np.linalg.norm(k @ U))
sector_amplitudes = {n: contract(T,P[n],U) for n in P}
longitudinal_max = max(abs(sector_amplitudes[n]) for n in ['P1','P0w','P0sw','P0ws'])
transverse_signal = max(abs(sector_amplitudes['P2']),abs(sector_amplitudes['P0s']))

out = {
 'test':'Barnes-Rivers tensor projector algebra and conserved-source reduction',
 'representation':'Euclidean D=4 symmetric rank-2 projector proxy; algebraic rank audit only',
 'idempotence_errors':idempotence,
 'orthogonality_errors':orthogonality,
 'operator_traces':traces,
 'expected_projector_ranks':expected_rank,
 'source_conservation_norms':[conservation_T,conservation_U],
 'sector_amplitudes':sector_amplitudes,
 'longitudinal_amplitude_max_abs':longitudinal_max,
 'transverse_amplitude_scale':transverse_signal,
 'projector_algebra_closes': max(idempotence.values()) < 1e-12 and max(orthogonality.values()) < 1e-12,
 'conserved_sources_remove_longitudinal_sectors': longitudinal_max < 1e-12 and transverse_signal > 1e-6,
 'conclusion':'For conserved symmetric sources the spin-1, longitudinal scalar and mixed sectors decouple, while transverse spin-2 and transverse scalar structures remain. This is the concrete tensor representation needed before assigning Ward/gauge rank.'
}
write_result('projector_algebra',out)
