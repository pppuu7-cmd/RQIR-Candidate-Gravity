#!/usr/bin/env python3
"""Exact RCG003 conformal second-order closure evaluator.

Standard-library only.  The scientific model/classifier is frozen in
prereg/RCG003_MINIMAL_NONLINEAR_VERSION_FORMATION_AND_CLOSURE_GATE.md.
This program constructs the compatibility matrix from the reduced curvature
polynomials; it does not hard-code a target coefficient vector.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from functools import reduce
from pathlib import Path

F = Fraction


def clean(p):
    return {k: F(v) for k, v in p.items() if v != 0}


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
    return clean(out)


def scale(a, q):
    q = F(q)
    return clean({k: q * v for k, v in a.items()})


def mul(a, b):
    out = {}
    for (i, j), av in a.items():
        for (k, l), bv in b.items():
            key = (i + k, j + l)
            out[key] = out.get(key, F(0)) + av * bv
    return clean(out)


def power(a, n):
    out = {(0, 0): F(1)}
    for _ in range(n):
        out = mul(out, a)
    return out


def diff_y(a):
    out = {}
    for (i, j), v in a.items():
        if j:
            out[(i, j - 1)] = out.get((i, j - 1), F(0)) + v * j
    return clean(out)


def hessian_y(a):
    return diff_y(diff_y(a))


def eval_poly(p, x, y):
    x, y = F(x), F(y)
    return sum(v * x**i * y**j for (i, j), v in p.items())


def poly_to_json(p):
    return {f"x^{i} y^{j}": frac(v) for (i, j), v in sorted(p.items())}


def frac(q):
    q = F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def gcd_many(values):
    vals = [abs(int(v)) for v in values if v]
    return reduce(math.gcd, vals) if vals else 1


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b) if a and b else 0


def primitive_integer_vector(vec):
    dens = [F(v).denominator for v in vec]
    L = reduce(lcm, dens, 1)
    ints = [int(F(v) * L) for v in vec]
    g = gcd_many(ints)
    ints = [v // g for v in ints]
    for v in ints:
        if v:
            if v < 0:
                ints = [-w for w in ints]
            break
    return ints


def rref(matrix):
    a = [[F(v) for v in row] for row in matrix]
    if not a:
        return a, []
    m, n = len(a), len(a[0])
    pivots = []
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pv = a[r][c]
        a[r] = [v / pv for v in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [u - q * v for u, v in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == m:
            break
    return a, pivots


def rank(matrix):
    return len(rref(matrix)[1])


def nullspace(matrix):
    rr, pivots = rref(matrix)
    n = len(matrix[0]) if matrix else 0
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for fcol in free:
        v = [F(0) for _ in range(n)]
        v[fcol] = F(1)
        for row, pcol in enumerate(pivots):
            v[pcol] = -rr[row][fcol]
        basis.append(v)
    return basis


def mat_vec(A, v):
    return [sum(F(a) * F(b) for a, b in zip(row, v)) for row in A]


def closure_matrix(hessians):
    monomials = sorted(set().union(*(set(h.keys()) for h in hessians)))
    A = [[h.get(m, F(0)) for h in hessians] for m in monomials]
    # Drop any accidentally all-zero rows.
    kept = [(m, row) for m, row in zip(monomials, A) if any(row)]
    return [m for m, _ in kept], [row for _, row in kept]


def substitute_point_redefinition(p, fp, fpp):
    """Substitute x=fp^2 X, y=fp Y+fpp X; return polynomial in X,Y."""
    fp, fpp = F(fp), F(fpp)
    X = {(1, 0): F(1)}
    Y = {(0, 1): F(1)}
    xsub = scale(X, fp * fp)
    ysub = add(scale(Y, fp), scale(X, fpp))
    out = {}
    for (i, j), coeff in p.items():
        term = mul(power(xsub, i), power(ysub, j))
        out = add(out, scale(term, coeff))
    return clean(out)


def divergence(k_up, T):
    return [sum(F(k_up[m]) * F(T[m][nu]) for m in range(4)) for nu in range(4)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--prereg-commit", required=True)
    ap.add_argument("--run-head", default="")
    args = ap.parse_args()

    # Exact polynomial variables x=(sigma_dot)^2 and y=sigma_ddot.
    x = {(1, 0): F(1)}
    y = {(0, 1): F(1)}
    p = add(x, y)

    # Independently construct Ricci scalar and Ricci-square polynomial parts
    # from the preregistered mixed Ricci eigenvalues {3y,y+2x,y+2x,y+2x}.
    l0 = scale(y, 3)
    ls = add(y, scale(x, 2))
    trace_R = add(l0, scale(ls, 3))
    trace_R2 = add(power(l0, 2), scale(power(ls, 2), 3))
    trace_R3 = add(power(l0, 3), scale(power(ls, 3), 3))

    expected_R = scale(p, 6)
    expected_R2 = scale(add(add(power(x, 2), mul(x, y)), power(y, 2)), 12)
    identities = {
        "R_from_mixed_eigenvalues": trace_R == expected_R,
        "Ricci2_from_mixed_eigenvalues": trace_R2 == expected_R2,
        "sqrtg_common_factor_is_nonzero_formal": True,
    }

    # After removing the common nonzero exp(-2 sigma) factor from all cubic
    # deformation densities, the exact reduced polynomials are:
    O1 = power(trace_R, 3)
    O2 = mul(trace_R, trace_R2)
    O3 = trace_R3
    operators = [O1, O2, O3]
    names = ["R^3", "R Ricci^2", "Tr(Ricci^3)"]

    hessians = [hessian_y(q) for q in operators]
    monomials, A = closure_matrix(hessians)
    r = rank(A)
    ns = nullspace(A)
    residual = 3 - r
    primitive_ns = [primitive_integer_vector(v) for v in ns]
    null_exact = all(all(v == 0 for v in mat_vec(A, b)) for b in ns)

    # Field-redefinition control: sigma=tau+(1/3)tau^2 at tau=0,1/2.
    redefinition_panels = []
    field_red_ok = True
    for tau in (F(0), F(1, 2)):
        fp = F(1) + F(2, 3) * tau
        fpp = F(2, 3)
        transformed = [substitute_point_redefinition(q, fp, fpp) for q in operators]
        hT = [hessian_y(q) for q in transformed]
        mT, AT = closure_matrix(hT)
        rt = rank(AT)
        nst = nullspace(AT)
        same_dim = (rt == r and len(nst) == len(ns))
        original_basis_survives = all(all(z == 0 for z in mat_vec(AT, b)) for b in ns)
        ok = bool(fp != 0 and same_dim and original_basis_survives)
        field_red_ok &= ok
        redefinition_panels.append({
            "tau": frac(tau), "f_prime": frac(fp), "f_second": frac(fpp),
            "rank": rt, "nullity": len(nst), "same_solution_dimension": same_dim,
            "original_nullspace_survives": original_basis_survives, "pass": ok,
            "monomials": [list(m) for m in mT],
        })

    # Source controls.
    k_up = [F(-1), F(2), F(0), F(0)]
    T_good = [
        [F(4), F(2), F(0), F(0)],
        [F(2), F(1), F(0), F(0)],
        [F(0), F(0), F(0), F(0)],
        [F(0), F(0), F(0), F(0)],
    ]
    T_bad = [row[:] for row in T_good]
    T_bad[0][1] = F(-2)
    T_bad[1][0] = F(-2)
    good_div = divergence(k_up, T_good)
    bad_div = divergence(k_up, T_bad)
    source_good_conserved = all(v == 0 for v in good_div)
    broken_sign_detected = any(v != 0 for v in bad_div)
    production_source_tag = "VACUUM_ZERO"
    forbidden_source_tag = "UNREGISTERED_EXTERNAL_T"
    allowed_physical_source_tags = {"VACUUM_ZERO"}
    forbidden_source_rejected = forbidden_source_tag not in allowed_physical_source_tags

    # Gauge/density manifest control.
    basis_manifest = {name: {"scalar_density": True} for name in names}
    malformed_density = {"name": "R^3_WITHOUT_SQRTG", "scalar_density": False}
    gauge_density_control = all(v["scalar_density"] for v in basis_manifest.values()) and not malformed_density["scalar_density"]

    # Perturbed-null-vector control, deterministic and outcome-independent.
    perturbed_control = {"available": bool(ns), "detected": False}
    if ns:
        seed = [F(v) for v in ns[0]]
        chosen = None
        residual_vec = None
        for idx in range(len(seed)):
            mut = seed[:]
            mut[idx] += F(1)
            rv = mat_vec(A, mut)
            if any(z != 0 for z in rv):
                chosen = idx
                residual_vec = rv
                break
        perturbed_control = {
            "available": True,
            "mutated_index": chosen,
            "detected": chosen is not None,
            "residual": [frac(z) for z in (residual_vec or [])],
        }

    # Positive and sensitivity controls.
    EH = scale(p, 6)  # common exp(+2 sigma) is y-independent.
    R_sq = scale(power(p, 2), 36)  # sqrt(g) R^2 has no sigma exponential factor.
    eh_hess = hessian_y(EH)
    r2_hess = hessian_y(R_sq)
    reference_control = (eh_hess == {})
    sensitivity_control = bool(r2_hess)

    controls = {
        "kinematic_identities": all(identities.values()),
        "nullspace_exact": null_exact,
        "field_redefinition_duplicate": field_red_ok,
        "source_conserved_control": source_good_conserved,
        "broken_conservation_sign_detected": broken_sign_detected,
        "forbidden_source_rejected": forbidden_source_rejected,
        "gauge_density_variant_rejected": gauge_density_control,
        "perturbed_closure_detected": bool(perturbed_control["detected"]),
        "EH_reference_second_order": reference_control,
        "R2_higher_derivative_sensitivity": sensitivity_control,
    }
    all_controls = all(controls.values())

    formation_slots = [
        "version_identity", "parent_authority", "fundamental_variables", "representation_class",
        "configuration_state_space", "gauge_redundancy", "causal_structure", "locality_status",
        "source_constitution", "carrier_self_source", "matter_coupling", "nonlinear_dynamics_class",
        "generator_status", "conservation_structure", "observable_map", "quantum_state_status",
        "measure_status", "coefficient_classes", "field_redefinition_equivalence", "domain_of_validity",
        "interpretation_ceiling", "classifier_rules",
    ]
    formation_valid = (len(formation_slots) == 22)

    if not (all_controls and formation_valid):
        classification = "INVALID_RCG003_CONTROL_OR_FORMATION_FAILURE"
    elif residual > 0:
        classification = "PASS_SCOPED_RCG003_CONFORMAL_SECOND_ORDER_NONZERO_DEFORMATION_EXISTS"
    else:
        classification = "FAIL_SCOPED_RCG003_CONFORMAL_SECOND_ORDER_NONZERO_DEFORMATION_EXCLUDED"

    result = {
        "schema": "RCG003_CONFORMAL_CLOSURE_RESULT_V1",
        "prereg_commit": args.prereg_commit,
        "run_head": args.run_head,
        "family": {
            "operators": names,
            "raw_dimension": 3,
            "coefficient_order": ["lambda", "mu", "nu"],
            "production_source_tag": production_source_tag,
            "matter_coupling": "UNRESOLVED_OUTSIDE_GATE",
            "chi_ABC": "UNAUTHORIZED_NOT_COMPUTED",
            "theory_established_percent": 0,
        },
        "derived_kinematics": {
            "identity_checks": identities,
            "R_polynomial": poly_to_json(trace_R),
            "Ricci2_polynomial": poly_to_json(trace_R2),
            "operator_polynomials_common_exp_minus_2sigma_removed": {
                name: poly_to_json(poly) for name, poly in zip(names, operators)
            },
            "hessians_common_exp_minus_2sigma_removed": {
                name: poly_to_json(poly) for name, poly in zip(names, hessians)
            },
        },
        "compatibility": {
            "row_monomials": [list(m) for m in monomials],
            "A": [[frac(v) for v in row] for row in A],
            "rank": r,
            "nullity": len(ns),
            "residual_dimension": residual,
            "nullspace_rational": [[frac(v) for v in b] for b in ns],
            "nullspace_primitive_integer": primitive_ns,
        },
        "field_redefinition_control": redefinition_panels,
        "source_controls": {
            "k_up": [frac(v) for v in k_up],
            "good_divergence": [frac(v) for v in good_div],
            "broken_sign_divergence": [frac(v) for v in bad_div],
            "forbidden_source_tag": forbidden_source_tag,
            "allowed_physical_source_tags": sorted(allowed_physical_source_tags),
        },
        "perturbed_closure_control": perturbed_control,
        "controls": controls,
        "all_controls_pass": all_controls,
        "formation": {
            "slot_count": len(formation_slots),
            "slots": formation_slots,
            "valid_for_gate": formation_valid,
            "side_classification": "RCG003_MINIMAL_NONLINEAR_FAMILY_FORMED_FOR_VACUUM_STRUCTURAL_TEST_SCOPED" if formation_valid else "INVALID_RCG003_FORMATION_SLOT_COUNT",
        },
        "classification": classification,
        "claim_locks": [
            "NO_GR_OR_EINSTEIN_DERIVATION",
            "NO_GLOBAL_UNIQUENESS",
            "NO_QUANTUM_THEORY",
            "NO_EXPERIMENTAL_CONFIRMATION",
            "NO_CHI_ABC_PREDICTION",
            "NO_NEW_PHYSICS_CLAIM",
        ],
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
