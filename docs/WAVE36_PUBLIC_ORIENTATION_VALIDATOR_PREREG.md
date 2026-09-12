# Wave 36 preregistration — public orientation-object audit and drop-in validator

Status: **FROZEN BEFORE COMPUTE**
Date: 2026-09-12
Branch: `f1-public-orientation-audit-wave36`

## Public-audit claim

The frozen claim is deliberately scoped:

> No reusable same-realization five-dimensional stability matrix or equivalent right eigensystem was located in the audited public sources.

Wave 36 does **not** claim global nonexistence and does not infer anything from absence beyond the audited source registry.

## Physical promotion contract

A candidate may be promoted to physical J8 orientation input only if it carries all of:

1. target paper/realization identifier;
2. same-closure fixed point;
3. ordered coordinates `(mu, lambda3, lambda4, g3, g4)`;
4. numerical 5x5 stability matrix **or** equivalent right eigensystem;
5. closure / higher-vertex identification;
6. projection prescription;
7. regulator/gauge/truncation provenance;
8. derivative-generation provenance;
9. numerical precision/tolerances;
10. checksum/version provenance.

Critical exponents without orientation data fail this contract.

## Predeclared tests

1. `audit_registry`: every checked source has an explicit orientation-object result and the scope statement forbids a global absence claim.
2. `valid_matrix_candidate`: a complete synthetic same-schema 5x5 object is accepted by the validator and yields three attractive real directions.
3. `exponents_only_rejected`: critical exponents/fixed point without matrix/eigenvectors are rejected.
4. `provenance_rejections`: candidates with wrong coordinate order, wrong closure identifier, missing regulator/projection provenance, missing numerical precision, or missing checksum are rejected.
5. `matrix_eigenbasis_consistency`: for a candidate containing both matrix and eigensystem, the reconstructed relevant projectors must agree within `1e-8`; a deliberately perturbed eigensystem must be rejected.
6. `complex_pair_realification`: the validator must correctly realify one attractive complex-conjugate pair into a two-dimensional real plane plus one real attractive mode.
7. `public_audit_no_promotion`: because the frozen public-source registry contains no located orientation object, Wave 36 must leave physical J8 blocked.
8. `information_firewall`: no polygon/KMQGB-derived QGR content may enter validator inputs or code.

## Pass semantics

PASS means:
- the scoped public-source audit is reproducible;
- the orientation-object acceptance/rejection boundary is executable;
- a future external matrix/eigensystem can be ingested without changing criteria.

PASS does **not** mean physical J8 is closed.

## Next scientific route

If no audited public candidate passes, Wave 37 should freeze a minimal new-FRG-computation request and a finite-difference derivative consistency protocol for producing the missing 5x5 object under the exact F1 closure.
