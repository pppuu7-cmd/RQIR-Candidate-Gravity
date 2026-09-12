# ITER022C / G40-C2-E — prospective hidden-control eligibility gate

The original G40-C remains frozen as `PROTOCOL_DESIGN_FAIL / OUT_OF_FAMILY_POSITIVE_CONTROL`: shard 3 had target BLP ≈0.009095 < 0.02. No threshold is changed and no old lane is promoted.

This separate gate performs no optimization. It keeps G40-C controls 0/1/2 unchanged and introduces one new preregistered shard-3 control. Before any new calibration is authorized, all four controls must:
- lie inside the same frozen G40-C parameter bounds;
- independently have BLP total positive trace-distance increment `>0.02` on the same 241-point witness grid;
- produce finite structural diagnostics.

Only terminal PASS authorizes a separately launched G40-C2 optimizer calibration. This eligibility result is not calibration, adversarial evidence, or novelty evidence.
