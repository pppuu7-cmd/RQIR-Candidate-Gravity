# Iter021B / G39-C terminal result

Authoritative run `34704727102`, launch head `389b8723f81c8e94f864fcf1b82de4503c329c7e`, aggregate job `103582784567`, summary artifact `10300663179`, digest `sha256:4f2365d8ef2d491478bfc6b184a0121d57aaeac1032755055f4574eeb3455959`.

All 16 prospectively frozen positive-control artifacts were structurally valid. Rank 2 and rank 3 were calibrated separately under both independently defined designs.

Rank 2:
- Sobol-LSQ: 4/4 PASS, worst trace-distance recovery `3.046037374961641e-12`;
- LHS-LSQ: 4/4 PASS, worst trace-distance recovery `2.8729779065034747e-12`.

Rank 3:
- Sobol-LSQ: 4/4 PASS, worst trace-distance recovery `2.4922953513899816e-11`;
- LHS-LSQ: 4/4 PASS, worst trace-distance recovery `4.2675460593425e-12`.

Frozen acceptance remained trace distance `<0.002`. Controls included exact lower-rank boundaries via zero rate. Hidden source coordinates were never supplied as optimizer starts.

Classification: `POSITIVE_CONTROL_METHOD_CALIBRATED_MULTIMODE_RANK2_RANK3`.

This authorizes separate prospective RCG-002 adversarial tests for rank 2 and rank 3 under the unchanged calibrated constructions. Rank 3 contains rank 2 exactly through a zero third-mode rate, so a rank-3-vs-rank-2 nesting sanity check is valid. No nesting claim to the earlier G36 family is imposed without an exact parameter-domain containment proof.