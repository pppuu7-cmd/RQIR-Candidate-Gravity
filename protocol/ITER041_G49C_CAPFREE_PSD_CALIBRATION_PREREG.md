# Iter041 / G49-C preregistration — cap-free/direct-PSD calibration

Frozen before implementation/production.

## Question
Can the existing real-PSD Markovian comparator be optimized in direct physical-scale coordinates without an explicit trace cap, while retaining response-blind recovery on known PSD controls and demonstrating that the purely numerical coordinate box is inactive?

## Family
`A` is a real symmetric 6x6 matrix represented by its 21 Frobenius-weighted lower-triangle coordinates `w`; `C=A^2`. This spans real PSD `C`. There is **no trace cap** in the model. For numerical optimization only, each weighted coordinate is bounded to `[-8,8]`; this box is not a physical family restriction and must be shown inactive for PASS.

## Frozen response-blind controls
Ranks 1..6. Deterministic hidden PSD controls use independent fixed RNG seeds and target `sqrt(tr(C))` values `[0.5,1,2,3,4,5]`. Methods `{sobol_lsq,lhs_lsq}`; hidden coordinates are never supplied as starts. Same TIMES/PROBES/trajectory map as the established trace-ball calibration layer. 32 starts, refine best 6, max_nfev 1200.

## Frozen PASS per lane
All outputs finite; hidden and recovered effective rank match requested rank; max trajectory gap `<0.002`; relative Kossakowski error `<0.02`; min eigenvalue `>=-1e-10`; TP/CP/state/trace physicality controls use the same tolerances as G48-A; and numerical box inactivity requires `max(abs(w_i))/8 < 0.80` for the selected best candidate.

Aggregate PASS requires 12/12 lanes PASS and both methods PASS for every rank. Cross-method recovered best-gap difference must be `<=0.002`.

## Interpretation
PASS authorizes only a subsequent prospectively frozen RCG-002 transport in this cap-free/direct-PSD numerical parameterization. PASS does **not** prove a mathematical optimum over all unbounded PSD generators. FAIL is retained without threshold retuning; implementation/numerical failure is repaired minimally without changing this science.

Readiness does not increase for calibration alone. Theory established remains 0%.
