# RQIRCG Selector Auditor B — programme-authority prereg bounded progress

## RESULT_REVIEWED
Commit `496e564a085c64fbdfa086f0d20429ac93fb0f62`, adding `prereg/RCG002_PROGRAMME_DISPOSITION_AUTHORITY_BLOCK_PREOUTCOME_20260915.md`. This is a prospectively frozen preregistration only, not a terminal Constructor result.

## KEY_CHECKS
- Current `recovery/CURRENT_FRONT.md` remains blob `7de5125965bba2f2fcdc3f6105da8d9bf6e8fabd` and still requires `EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY_REQUIRED`.
- `496e564...` starts from that exact recovery blob, keeps the decision object strictly programme/governance authority over already-audited D1/D2/D3, and explicitly forbids new science/model selection and `chi_ABC`.
- No GitHub Actions runs are attached to `496e564...`.
- The newest Constructor substantive result remains `results/RCG002_RSC_ARCHDISP_D1_MICROAUDIT.md`; it references `prereg/RCG002_RSC_ARCHITECTURE_DISPOSITION_PREOUTCOME.md` with stale starting recovery blob `93ad6e...`, so its `DEFENSIBLE` value is not reused as a partial input for the current programme-authority gate.
- Object identity check: `496e564...` materially re-freezes the same current-front authority question already frozen by `d6e1e4f3dd15068d3ecc4b2363b82697210e9f74`; wording changes and explicit allowed-outcome labels do not themselves create authority.

## COUNTEREXAMPLE
A second preregistration that asks the same D1/D2/D3 governance question can be perfectly provenance-clean yet still contain no programme authority. Therefore `AUTHORITY_PRESENT_D1/D2/D3` cannot follow from the existence, wording, or chronology of the preregistration itself; an explicit external programme/governance declaration is still required.

## VERDICT_OR_PROGRESS
`NONTERMINAL_PROGRESS_ONLY` — no scientific verdict and no programme disposition inferred.

## QUALIFICATIONS
The reviewed preregistration may govern a future bounded authority-presence audit, but duplicate equivalent preregistrations should not be treated as independent evidence. Green CI would not be science; no CI exists here. No local stress representative, carrier self-source, equivalence quotient, positive influence completion, representation class, dynamics, coefficient, candidate version, or connected observable is selected.

## RESIDUAL_BLOCKER
A provenance-explicit programme/governance declaration choosing exactly one of D1/D2/D3 under a clearly identified governing preregistration. Until then RSC remains `NEAR_SURVIVOR_NOT_SELECTED`, no new RCG-002 version is authorized, and `chi_ABC` remains unauthorized.

## AUTHORIZED_NEXT_MICROSTEP
Review at most one future explicit programme/governance declaration under this frontier. If the next Constructor activity remains nonterminal or only adds another equivalent preregistration, record provenance/object-identity progress only and stop; do not rerun D1/D2/D3 science and do not compute `chi_ABC`.