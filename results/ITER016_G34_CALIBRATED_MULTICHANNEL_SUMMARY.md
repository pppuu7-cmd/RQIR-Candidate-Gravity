# Iter016 / G34 calibrated multichannel comparator — terminal classification

Authoritative run: `34695835216`

Authoritative head: `09d729764ca38a0d83f11b81dc59f157cd0cb734`

Aggregate job: `103562681303`

Aggregate artifact: `10299385844`

Artifact digest: `sha256:622e04cfdc1859561bd958962cadd293403defb8f8265641410c7119de2843c4`

## Frozen gate

All acceptance rules were fixed before result inspection. Scientific acceptance is evaluated in trace distance. Positive-control calibration requires `< 0.002`. Adversarial support requires both calibrated methods to retain gap `> 1e-4`, with cross-method agreement within `0.002` on each shard. Historical G30/G31 minima are not reused as authority.

## Terminal result

All 24 lanes were structurally valid.

### K=2 prospective adversarial rerun

Both independently calibrated methods retained nonzero gaps and agreed within the frozen `0.002` scale on all four shards:

| shard | Sobol-LSQ gap | LHS-LSQ gap |
|---|---:|---:|
| 0 | 0.02607083637907346 | 0.026070816008971712 |
| 1 | 0.10462725764602553 | 0.1046226877828865 |
| 2 | 0.40307763835411964 | 0.40307758671702226 |
| 3 | 0.532452669358466 | 0.5324532595059579 |

Classification: `DERIVED_SCOPED_K2_CALIBRATED_COMPARATOR_SUPPORT`.

This is support only inside the finite additive independent single-axis Markovian measurement-feedback GKSL comparator family. It is not a no-go theorem for semiclassical gravity or classical mediators generally.

### K=3 positive-control calibration

- Sobol-LSQ: 4/4 PASS; worst trace gap `4.864663671077271e-11`.
- LHS-LSQ: 4/4 PASS; worst trace gap `3.1874163425023643e-11`.

Classification: `POSITIVE_CONTROL_METHOD_CALIBRATED_K3`.

### K=4 positive-control calibration

- Sobol-LSQ: 4/4 PASS; worst trace gap `8.088582075956358e-13`.
- LHS-LSQ: 4/4 PASS; worst trace gap `2.658734486319925e-12`.

Classification: `POSITIVE_CONTROL_METHOD_CALIBRATED_K4`.

## Authorized next gate

Prospective adversarial RCG-002 reruns are now authorized for K=3 and K=4 using only the independently calibrated Sobol-LSQ and LHS-LSQ constructions fixed in G34. Each K must satisfy, on every shard: both methods retain `gap > 1e-4`, cross-method disagreement `<= 0.002`, and nesting sanity relative to the lower-K calibrated frontier. Historical G30/G31 results remain diagnostics only.

Claim locks remain unchanged.