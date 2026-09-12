# ITER022C / G40-C2-E — terminal eligibility classification

Run: `34708494925`
Head: `1b52b4c50a4a7840109a92a4d593a9873afd7973`
Aggregate job: `103592871261`
Summary artifact: `10302253344`
Digest: `sha256:8beb6836a6a846243df916616ed5234cdf22935f51e7447ce13f8eb30739cf24`

All four targets are inside the unchanged G40-C parameter bounds and independently satisfy the frozen strict-BLP eligibility rule `BLP > 0.02` before any optimizer is run:
- shard 0: `0.022161811061064185`
- shard 1: `0.07584060292605893`
- shard 2: `0.7778334797535692`
- new preregistered shard 3: `0.16064058660706515`

Classification: `STRICT_BLP_HIDDEN_CONTROL_ELIGIBILITY_PASS`.

This is eligibility only. It authorizes the separately preregistered G40-C2 optimizer calibration and provides no RCG-002 adversarial or novelty inference by itself.
