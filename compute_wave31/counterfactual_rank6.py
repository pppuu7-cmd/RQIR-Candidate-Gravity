import json, pathlib
import numpy as np
rng=np.random.default_rng(3105)
full=0; trials=1000
examples=[]
for i in range(trials):
    P4=rng.normal(size=(6,4))
    while np.linalg.matrix_rank(P4)<4: P4=rng.normal(size=(6,4))
    E=rng.normal(size=(6,2))
    r=int(np.linalg.matrix_rank(np.hstack([P4,E])))
    full += int(r==6)
    if i<5: examples.append(r)
frac=full/trials
# Frozen evidence explicitly does not supply two independently reconstructed GEH residual columns.
e=json.loads(pathlib.Path('evidence/WAVE31_GENERALIZED_EH_EVIDENCE.json').read_text())
physical_evidence=bool(e['published_generalized_EH_facts']['explicit_two_independent_generalized_EH_residual_coefficients_after_GR_baseline_subtraction'])
signals={
 'two_transverse_extra_columns_can_close_rank6_mathematically':frac>0.99,
 'counterfactual_closure_does_not_count_as_F2_physical_evidence':not physical_evidence
}
out={'test':'counterfactual_rank6','trials':trials,'full_rank_fraction':frac,'example_ranks':examples,'published_two_column_physical_evidence':physical_evidence,'classification':'COUNTERFACTUAL_MATHEMATICAL_POSSIBILITY_ONLY','signals':signals}
pathlib.Path('wave31_counterfactual_rank6.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
