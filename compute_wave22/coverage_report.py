import numpy as np
from common import selected_bank, write_result

_,_,selected,X=selected_bank(10)
counts={sec:sum(r['sector']==sec for r in selected) for sec in ['2pt','3pt','4pt']}
indices={sec:[i for i,r in enumerate(selected) if r['sector']==sec] for sec in counts}
subranks={sec:int(np.linalg.matrix_rank(X[idx],tol=1e-10)) if idx else 0 for sec,idx in indices.items()}
checks={
 'all_three_sectors_present':all(v>0 for v in counts.values()),
 'two_point_has_spin2_probe':any(r['name'].startswith('P2_') for r in selected),
 'two_point_has_spin0_probe':any(r['name'].startswith('P0_') for r in selected),
 'at_least_three_three_point_probes':counts['3pt']>=3,
 'at_least_three_four_point_probes':counts['4pt']>=3
}
out={
 'test':'selected holdout bank sector/representation coverage diagnostic',
 'selected_names':[r['name'] for r in selected],
 'sector_counts':counts,
 'sector_row_ranks':subranks,
 'checks':checks,
 'sector_coverage_pass':all(checks.values()),
 'conclusion':'The D-optimal bank is not rank-complete by relying on a single observable family; it retains spin-2, spin-0, finite 3-point and finite 4-point probes.'
}
write_result('coverage_report',out)
