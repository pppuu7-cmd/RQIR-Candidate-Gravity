# ITER022F / G40-A — terminal fixed-witness strict-BLP RTN adversarial classification

Run: `34708971194`
Head: `dab6418075f5f7122e72444c61c7d3554a0002fb`
Aggregate job: `103594269913`
Summary artifact: `10302404036`
Digest: `sha256:5f299a2a08e228894b1cb52cb2059f4f1c961c387f0e30e0842307a1d8eafe52`

All 8 lanes were structurally valid, but the preregistered all-shards support rule failed.

Per-shard aggregate:
- shard 0: neither method produced an admissible fixed-witness BLP>0.02 refined candidate;
- shard 1: neither method produced an admissible fixed-witness BLP>0.02 refined candidate;
- shard 2: both methods produced admissible candidates and agreed: gaps `0.6316999358506555` and `0.6316992655897476`, BLP `0.34388675247275996` and `0.34388454929499646`;
- shard 3: both methods produced admissible candidates with nonzero gaps, but the gaps `0.7472831704713611` and `0.7495355611279814` differ by more than the frozen `0.002` agreement tolerance; BLP values also differ strongly (`0.43843347766934604` vs `0.19107175531985504`).

Classification: `NEGATIVE_RESULT / G40A_FROZEN_SUPPORT_RULE_NOT_MET`.

Interpretation lock: this is not evidence that the RTN family fits RCG-002 and not a no-go against it. The fixed-witness finite-family adversarial gate is inconclusive on shards 0,1,3 and gives scoped comparator-separation support only on shard 2. The failed all-shard gate must remain failed; no threshold, witness, target, optimizer or family is retuned post hoc.

Next admissible diagnostic: prospectively test witness/basis fragility of the refined RTN candidate set without using the result to retroactively promote G40-A.
