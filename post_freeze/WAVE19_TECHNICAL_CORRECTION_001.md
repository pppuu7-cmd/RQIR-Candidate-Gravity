# Wave 19 Technical Correction 001

**Failed run retained:** `34659505867`

Three Wave-19 jobs failed for infrastructure reasons before producing authoritative artifacts:

1. `ward-cross-order`: JSON could not serialize a NumPy boolean scalar.
2. `cubic-only-eft`: common result writer unnecessarily imported NumPy although the job intentionally had no NumPy install step.
3. `comparator-firewall`: same unnecessary common-writer NumPy import.

## Correction

Only `compute_wave19/common.py` is changed:

- remove the unused global NumPy import;
- add a JSON fallback using scalar `.item()` when available.

No scientific script, matrix, coefficient, kinematic point, pass/fail criterion, preregistration statement or holdout is changed.

The original failed run remains part of provenance. The correction triggers a complete fresh Wave-19 run so all primary jobs again originate from one commit.
