# Current Scientific Front

**Repository:** `RQIR-Candidate-Gravity`  
**Active branch:** `rqir-derived-model-v0`  
**Independence rule:** do not inspect or import the separately developed polygon-derived QGR candidate until the independent RQIR branch freezes its own architecture and gate state.

## Frozen authority

Use `docs/RQIR_V1_AUTHORITY_SNAPSHOT.md` and `model/REQUIREMENTS_MATRIX.md`.

## Active models

### ANSATZ-RQIR-MIN v0.1

Root/minimal metric quantum interface.

- QG-001: PASS
- QG-002: PASS
- Newtonian QG-003 subcheck: PASS, full gate BLOCKED
- novelty: expected/likely C5-degenerate; retained as control

Canonical files:

- `model/ANSATZ-RQIR-MIN/MODEL.md`
- `model/ANSATZ-RQIR-MIN/FOUNDATIONAL_DERIVATION_001.md`
- `model/ANSATZ-RQIR-MIN/MINIMALITY_RESULT_001.md`
- `model/ANSATZ-RQIR-MIN/GATE_STATUS.yaml`

### ANSATZ-RQIR-QLC v0.1

RQIR-native quantum-limited relational gravity channel.

Primary law:

`d_Y = K d_X + d_0`

`V_Y = K V_X K^T + Y_G`

with CP condition

`Y_G + i hbar/2 (Omega_Y - K Omega_X K^T) >= 0`.

QLC postulate: choose the minimum added noise compatible with CP and frozen physical symmetries in each uniquely canonicalizable physical mode block.

One-mode result:

`y_min = hbar |1-eta|/2`

for `K=sqrt(eta) I` in normalized canonical coordinates.

Current gates:

- QG-001: PASS
- QG-002: PASS
- QG-004: BLOCKED, with one-mode CP subcheck passed
- QG-007: BLOCKED, candidate closure relation identified but no comparator DISTINCT result yet

Canonical files:

- `model/ANSATZ-RQIR-QLC/MODEL.md`
- `model/ANSATZ-RQIR-QLC/FOUNDATIONAL_DERIVATION_001.md`
- `model/ANSATZ-RQIR-QLC/GATE_STATUS.yaml`

## Immediate next scientific task

Construct the first physical weak-field GR mode block and derive its `K`, `Omega_X`, `Omega_Y` and QLC noise floor in physical units. Then perform the C5 equivalence audit.

Do not add a new field, kernel, collapse term, nonlocal form factor or source rule merely to obtain novelty. A deformation is allowed only after a specific frozen RQIR obstruction is documented.
