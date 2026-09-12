import json, pathlib
import numpy as np
rng=np.random.default_rng(3004)
# Start with a full-rank 6x4 quadratic image. Add q extra columns.
P4=rng.normal(size=(6,4))
while np.linalg.matrix_rank(P4)<4: P4=rng.normal(size=(6,4))
results=[]
for q in [0,1,2]:
    maxrank=0
    full=0
    for _ in range(1000):
        E=rng.normal(size=(6,q)) if q else np.empty((6,0))
        P=np.hstack([P4,E])
        r=int(np.linalg.matrix_rank(P)); maxrank=max(maxrank,r); full += int(r==6)
    results.append({'extra_residual_directions':q,'latent_cap':4+q,'max_rank':maxrank,'full_rank_fraction':full/1000})
signals={
 'at_least_two_additional_independent_residual_directions_required_beyond_four_parameter_quadratic_truncation':results[1]['max_rank']<6 and results[2]['max_rank']==6,
 'six_dimensional_closure_requires_explicit_extra_directions_and_transversality':results[2]['full_rank_fraction']>0.99
}
out={'test':'generalized_eh_scenarios','results':results,'note':'q=2 demonstrates mathematical possibility under generic transverse extra directions only; it is not physical evidence that F2 supplies them.','signals':signals}
pathlib.Path('wave30_generalized_eh_scenarios.json').write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
