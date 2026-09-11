import numpy as np
from common import write_result

# CEMZ-inspired logical proxy: anomalous cubic gravity coupling is parametrically limited by a UV higher-spin gap.
# We intentionally avoid importing a numerical coefficient from the literature.
# |c3| <= 1/Delta_gap^2. If the UV gap is unknown, low-energy causality trades c3 freedom for UV-spectrum freedom.
gaps=np.array([2.0,3.0,5.0,8.0,12.0])
rows=[]
for gap in gaps:
    lim=1.0/(gap*gap)
    rows.append({'Delta_gap':float(gap),'allowed_abs_c3_max':float(lim),'allowed_width':float(2*lim)})
# Even at known finite gap, only a bound remains.
gap0=5.0; lim0=1/gap0**2
out={
 'test':'UV-completion/gap information versus unique cubic Wilson selection',
 'parametric_proxy':'|c3| <= Delta_gap^-2',
 'gap_scan':rows,
 'known_gap_control':gap0,
 'allowed_interval_at_known_gap':[-lim0,lim0],
 'UV_completion_information_trades_Wilson_freedom_for_UV_spectrum_data':True,
 'finite_gap_bound_not_unique':2*lim0>0,
 'conclusion':'Causality-compatible UV completion can strongly suppress an anomalous cubic coupling as the higher-spin gap grows, but without a microscopic spectrum it does not determine the coefficient. Even a known finite gap gives a bound rather than a unique sign/value. UV data are additional physics, not contained in frozen RQIR.'
}
write_result('uv_gap_selector',out)
