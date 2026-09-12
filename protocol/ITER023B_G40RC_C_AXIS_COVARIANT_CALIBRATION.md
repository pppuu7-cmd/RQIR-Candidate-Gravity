# ITER023B / G40-RC-C — preregistered axis-covariant RTN witness calibration

Purpose: replace the basis-fragile fixed BLP witness exposed by terminal G40-D with a family-covariant witness rule, and calibrate that rule before any new RCG-002 adversarial use.

Frozen before results:
- same finite 8-parameter hidden-classical symmetric RTN family, parameter bounds, four corrected C2 hidden positive controls, Sobol/LHS designs, 16 starts, top-4 least-squares refinements, trajectory times/probes, `max_nfev=600`, recovery tolerance `<0.002`, and BLP threshold `>0.02` as G40-C2/C3;
- no RCG-002 target is used in this gate;
- for each candidate with local noise axes `A(thetaA,phiA)` and `B(thetaB,phiB)`, define the BLP state pair in the candidate's own local frame: rotate the canonical `|+>_A|0>_B` / `|->_A|0>_B` pair by the local unitaries that map `Z` to `A` and `Z` to `B`;
- this axis-frame witness is therefore covariant under local basis rotations of the finite RTN family; it is not claimed to be the globally optimized BLP witness over all state pairs;
- every hidden control must itself have axis-covariant BLP `>0.02`; otherwise classify the calibration protocol as ineligible rather than changing controls or the threshold;
- a recovered candidate is scientifically admissible only if its axis-covariant BLP is `>0.02`;
- per lane support requires structural validity, hidden-control eligibility, an admissible recovered candidate, and max trajectory trace-distance gap `<0.002`;
- overall calibration support requires 4/4 support for each independently seeded Sobol and LHS construction.

Interpretation lock:
- PASS authorizes only a separate prospective RCG-002 adversarial gate using this exact axis-covariant witness/search rule;
- FAIL is retained as calibration/eligibility failure; no threshold/control/search retuning inside this run;
- neither PASS nor FAIL establishes an all-non-Markovian/all-classical result.
