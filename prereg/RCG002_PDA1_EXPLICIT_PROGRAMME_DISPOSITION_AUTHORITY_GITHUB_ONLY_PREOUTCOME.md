# RCG-002 PDA1 — explicit programme disposition authority check

Status: PROSPECTIVELY FROZEN; NO SUBSTANTIVE AUTHORITY VERDICT
Date: 2026-09-15
Starting recovery blob: `7de5125965bba2f2fcdc3f6105da8d9bf6e8fabd`
Frontier: `PROGRAMME_DISPOSITION_AUTHORITY_FRONTIER`
Required action: `EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY_REQUIRED`

## Question
Does current GitHub-authoritative programme/governance state explicitly choose exactly one of the already frozen AD1 dispositions D1, D2, or D3?

## Frozen admissible outcomes
- `AUTHORITY_PRESENT_D1`
- `AUTHORITY_PRESENT_D2`
- `AUTHORITY_PRESENT_D3`
- `BLOCKED_PENDING_EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY`
- `INVALID_AMBIGUOUS_OR_MULTIPLE_AUTHORITY`

## Frozen audit rule
A future bounded audit may inspect only authority that is explicitly identified by the then-current recovery frontier as programme/governance authority. Scientific admissibility of D1/D2/D3 is not itself programme authority. No historical scan, Actions evidence, connected outcome, theorem preference, administrative convenience, or successor-only result may be used as a selector.

Exactly one explicit D1/D2/D3 choice is required for an `AUTHORITY_PRESENT_*` classification. If no such choice is explicitly authoritative, classify `BLOCKED_PENDING_EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY`; this is not FAIL. If authority is conflicting or selects multiple dispositions without a unique precedence rule, classify `INVALID_AMBIGUOUS_OR_MULTIPLE_AUTHORITY`.

## Claim ceiling
This gate cannot select representation class, dynamics, action, source constitution, state/measure, quantum law, coefficient, candidate version, or observable. It cannot compute `chi_ABC`. It cannot reinterpret D1/D2/D3 as scientific ranking, and it cannot support `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `THEORY_ESTABLISHED`, `RQIR_REQUIRES_RCG002`, universal no-go, or family-wide uniqueness claims.

No substantive authority verdict is made in this preregistration commit.
