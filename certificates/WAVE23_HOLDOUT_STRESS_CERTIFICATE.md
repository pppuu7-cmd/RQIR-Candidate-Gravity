# Wave 23 Holdout Stress / Misspecification Certificate

**Status:** STRONGER ROBUSTNESS CERTIFIED  
**Authority commit:** `6d4582e754eddc1936fe9a2bf614765ca7fb2711`  
**Authority Actions run:** `34662161876`  
**Frozen Wave-22 bank blob:** `c32bd52edd003589ef65e0240c757475f215f55f`

All preregistered signals passed with no corrective rerun.

## Exact robustness results

- frozen-bank integrity: PASS;
- 500 orthogonal basis rotations: rank/prediction/singular-spectrum invariance PASS;
- 500 parameter-unit rescalings across four decades: rank/prediction invariance PASS;
- leave-one-out: `10/10` retain rank 6;
- leave-two-out: `45/45` retain rank 6 (`fraction=1.0`, preregistered threshold `>=0.80`);
- extended nuisance (2pt/3pt/4pt normalizations + centered drift): rank remains 6;
- extended-nuisance minimum singular value: `0.030758529723915844` (`>=0.03` preregistered threshold);
- preregistered omitted seventh shape residual fraction after six-signal fit: `0.13237166204950424`;
- omitted-shape residual fraction after signal + sector-nuisance fit: `0.1213384672243101`;
- candidate-information firewall: PASS.

## Meaning

The frozen prospective exam is not merely full-rank in one convenient coordinate system. It survives basis rotations, unit changes, every one- and two-probe deletion in this finite bank, one additional coherent nuisance direction, and one explicit out-of-class higher-momentum/helicity deformation.

The positive omitted-physics residual is particularly important: the test architecture can diagnose at least this preregistered form of model misspecification instead of forcing all candidate behavior into the six-dimensional RQIR residual proxy.

## Claim boundary

This remains a finite-proxy robustness result. It is not proof that every possible omitted quantum-gravity operator is detectable, nor a forecast of achievable experimental error bars.
