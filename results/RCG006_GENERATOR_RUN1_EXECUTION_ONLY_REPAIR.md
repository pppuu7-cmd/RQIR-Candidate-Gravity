# RCG-006 generator completeness run-1 execution-only repair

Date: 2026-09-17

Workflow run `35181593199` reached and passed all prospective chronology checks, then both Constructor and independent Critic failed before producing scientific artifacts.

Shared defect:
`defaultdict(sp.Rational)` invokes `sympy.Rational()` without the required numerator, raising `TypeError: Rational.__new__() missing 1 required positional argument: 'p'` at the first polynomial accumulation.

This is an implementation/runtime defect, not a scientific classification. No generator rank, basis, `M_FR`, image, quotient, or discriminator outcome was produced.

Frozen execution-only repair:
- do not edit the already-frozen scientific algorithms;
- invoke each script through a wrapper that replaces only its module-local `defaultdict` binding so the special case `factory is sp.Rational` is converted to `lambda: sp.Rational(0)`;
- all other `defaultdict` factories pass through unchanged;
- do not change raw enumeration, tensor formulas, symmetry handling, commutator completion, rank criterion, or aggregate classifier.

The failed run remains noncanonical infrastructure evidence only.
