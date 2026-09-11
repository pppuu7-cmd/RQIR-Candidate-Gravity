import numpy as np
from common import write_result

# EFT-control proxy: independent analytic corrections in the physical spin-2 and spin-0 transverse sectors.
# This does not assert exact Wilson-coefficient normalization; it tests whether two independent conventional
# low-energy operator directions can span the two transverse form-factor slopes.
xs=np.array([0.2,0.5])
# Observables chosen as direct transverse form-factor probes: delta f2(x)=c2*x, delta f0(x)=c0*x.
J=np.array([[xs[0],0.0],[0.0,xs[0]],[xs[1],0.0],[0.0,xs[1]]])
rank=int(np.linalg.matrix_rank(J))
sv=np.linalg.svd(J,compute_uv=False)
controls=[]
for c2,c0 in [(-0.15,0.1),(0,0),(0.2,-0.12)]:
    controls.append({'coefficients':[c2,c0], 'delta_f2':[float(c2*x) for x in xs], 'delta_f0':[float(c0*x) for x in xs]})
out={
 'test':'conventional EFT control for residual transverse tensor shape freedom',
 'scope':'rank proxy for independent curvature-squared/Wilson directions; not an exact operator-normalization derivation',
 'control_jacobian_rank':rank,
 'singular_values':sv.tolist(),
 'examples':controls,
 'two_transverse_slope_directions_are_EFT_compatible': rank==2,
 'residual_transverse_shape_is_not_by_itself_C5_distinct': rank==2,
 'conclusion':'The two physical transverse slope directions left after Ward/gauge reduction are compatible with ordinary low-energy EFT freedom. Their mere existence is therefore comparator-degenerate with C5; novelty would require an extra relation/prediction not available to the generic EFT control.'
}
write_result('eft_transverse_control',out)
