import json
from pathlib import Path
variants=[0,1,2,4,8]
rows=[]
for V in variants:
    rows.append({'uncertainty_variants':V,'symmetric_full_trajectory_integrations':7*(1+V),'one_sided_minimum_integrations':4*(1+V)})
signals={
 'central_symmetric_budget_is_7':rows[0]['symmetric_full_trajectory_integrations']==7,
 'budget_scales_linearly_with_fully_propagated_variants':all(r['symmetric_full_trajectory_integrations']==7*(1+r['uncertainty_variants']) for r in rows),
 'symmetric_budget_remains_authority_over_one_sided_shortcut':all(r['symmetric_full_trajectory_integrations']>=r['one_sided_minimum_integrations'] for r in rows),
}
out={'test':'compute_budget','budgets':rows,'signals':signals}
Path('wave35_compute_budget.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
