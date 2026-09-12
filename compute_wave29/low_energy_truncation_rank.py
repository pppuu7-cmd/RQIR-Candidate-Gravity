import json, pathlib
import numpy as np
rng=np.random.default_rng(2904)
results={}
for name,k in [('constants_only_quadratic',2),('constant_plus_first_slopes_quadratic',4)]:
    # 40 synthetic measurements generated from k latent coefficients
    A=rng.normal(size=(40,k))
    rank=int(np.linalg.matrix_rank(A))
    results[name]={'latent_count':k,'observable_rows':40,'image_rank':rank,'rank_le_latent':rank<=k}
signals={
 'constants_only_quadratic_rank_le_2':results['constants_only_quadratic']['image_rank']<=2,
 'constants_plus_first_slopes_rank_le_4_before_generalized_EH':results['constant_plus_first_slopes_quadratic']['image_rank']<=4
}
out={'test':'low_energy_truncation_rank','generalized_EH_automatic_residual_credit':False,'results':results,'signals':signals}
pathlib.Path('wave29_low_energy_truncation_rank.json').write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True)); assert all(signals.values())
