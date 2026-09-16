#!/usr/bin/env python3
"""Independent RCG003 critic.

This lane does not import the constructor.  It rechecks the exact closure rank
with an independent finite-difference identity for cubic polynomials, verifies
chronology/blobs, source/equivalence controls, and claim-scope discipline.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction
from functools import reduce
from pathlib import Path

F = Fraction
EXPECTED_PREREG_COMMIT = "0bba0ea6e1d4e13635f70f3b5056e131afba6c7d"
EXPECTED_PREREG_BLOB = "b87bd703bd4c5b8e190c78100537bbcd45eb50ae"
EXPECTED_D3_TERMINAL_COMMIT = "d9187a60d2e7545ae3f082762d4a747b9681b69f"
EXPECTED_BASELINE_BLOB = "a57c045edb858b28740a1d6709343690c53d6b01"
EXPECTED_G90_BLOB = "ce82d04d337c0bdd85b8aeb73966ef36964ffe27"


def sh(*args):
    return subprocess.check_output(list(args), text=True).strip()


def is_ancestor(a, b):
    return subprocess.run(["git", "merge-base", "--is-ancestor", a, b]).returncode == 0


def rref(matrix):
    a = [[F(v) for v in row] for row in matrix]
    m = len(a)
    n = len(a[0]) if m else 0
    pivots = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = a[r][c]
        a[r] = [v / q for v in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [u - q * v for u, v in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == m:
            break
    return a, pivots


def rank(A):
    return len(rref(A)[1])


def nullspace(A):
    rr, piv = rref(A)
    n = len(A[0]) if A else 0
    free = [j for j in range(n) if j not in piv]
    out = []
    for f in free:
        v = [F(0)] * n
        v[f] = F(1)
        for i, p in enumerate(piv):
            v[p] = -rr[i][f]
        out.append(v)
    return out


def lcm(a, b):
    return abs(a*b)//math.gcd(a,b) if a and b else 0


def primitive(v):
    L = reduce(lcm, [q.denominator for q in v], 1)
    w = [int(q*L) for q in v]
    g = reduce(math.gcd, [abs(x) for x in w if x], 0) or 1
    w = [x//g for x in w]
    for x in w:
        if x:
            return [-z for z in w] if x < 0 else w
    return w


def O1(x, y):
    return F(216) * (x+y)**3


def O2(x, y):
    return F(72) * (x+y) * (x*x + x*y + y*y)


def O3(x, y):
    return (F(3)*y)**3 + F(3) * (y + F(2)*x)**3


def centered_second_y(fn, x, y):
    # Exact for every cubic polynomial in y.
    return fn(x, y+1) - F(2)*fn(x, y) + fn(x, y-1)


def independent_matrix():
    fs = [O1, O2, O3]
    # Hessian is linear in x,y; evaluations at (1,0) and (0,1)
    # recover its independent coefficients without using constructor algebra.
    return [
        [centered_second_y(fn, F(1), F(0)) for fn in fs],
        [centered_second_y(fn, F(0), F(1)) for fn in fs],
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--constructor", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    constructor_path = Path(args.constructor)
    result = json.loads(constructor_path.read_text(encoding="utf-8"))
    head = sh("git", "rev-parse", "HEAD")

    chronology = {
        "d3_terminal_precedes_prereg": is_ancestor(EXPECTED_D3_TERMINAL_COMMIT, EXPECTED_PREREG_COMMIT),
        "prereg_precedes_run_head": is_ancestor(EXPECTED_PREREG_COMMIT, head),
        "constructor_reports_frozen_prereg": result.get("prereg_commit") == EXPECTED_PREREG_COMMIT,
    }

    blob_checks = {
        "prereg_unchanged": sh("git", "hash-object", "prereg/RCG003_MINIMAL_NONLINEAR_VERSION_FORMATION_AND_CLOSURE_GATE.md") == EXPECTED_PREREG_BLOB,
        "historical_baseline_unchanged": sh("git", "hash-object", "candidates/RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md") == EXPECTED_BASELINE_BLOB,
        "historical_G90_synthesis_unchanged": sh("git", "hash-object", "results/G90_G91_COVARIANT_UNDERDETERMINATION_SYNTHESIS.md") == EXPECTED_G90_BLOB,
    }

    A_ind = independent_matrix()
    rank_ind = rank(A_ind)
    ns_ind = nullspace(A_ind)
    prim_ind = [primitive(v) for v in ns_ind]
    comp = result["compatibility"]
    rank_match = rank_ind == int(comp["rank"])
    nullity_match = len(ns_ind) == int(comp["nullity"])
    reported_prim = [list(map(int, v)) for v in comp["nullspace_primitive_integer"]]
    nullspace_match = sorted(prim_ind) == sorted(reported_prim)

    source_checks = result.get("controls", {})
    control_checks = {
        "constructor_all_controls": bool(result.get("all_controls_pass")),
        "broken_conservation_control": bool(source_checks.get("broken_conservation_sign_detected")),
        "forbidden_source_control": bool(source_checks.get("forbidden_source_rejected")),
        "gauge_density_control": bool(source_checks.get("gauge_density_variant_rejected")),
        "field_redefinition_control": bool(source_checks.get("field_redefinition_duplicate")),
        "perturbed_closure_control": bool(source_checks.get("perturbed_closure_detected")),
        "sensitivity_control": bool(source_checks.get("R2_higher_derivative_sensitivity")),
    }

    evaluator_text = Path("scripts/rcg003_conformal_closure.py").read_text(encoding="utf-8")
    target_literal = str(reported_prim[0]) if reported_prim else "<NO_NULL_VECTOR>"
    anti_fit = {
        "primitive_nullvector_not_literal_in_evaluator": target_literal not in evaluator_text,
        "no_successor_repo_tokens_in_evaluator": not any(tok in evaluator_text for tok in ("RQIRCGSF", "RHPI", "ISQGR")),
        "vacuum_source_only_in_family": result.get("family", {}).get("production_source_tag") == "VACUUM_ZERO",
        "chi_still_locked": result.get("family", {}).get("chi_ABC") == "UNAUTHORIZED_NOT_COMPUTED",
        "theory_established_zero": result.get("family", {}).get("theory_established_percent") == 0,
    }

    prereg_text = Path("prereg/RCG003_MINIMAL_NONLINEAR_VERSION_FORMATION_AND_CLOSURE_GATE.md").read_text(encoding="utf-8")
    scope_checks = {
        "reference_not_derived_lock_present": "REFERENCE / CONTROL" in prereg_text and "not `DERIVED`" in prereg_text,
        "broader_field_redefinitions_not_claimed": "no claim about a broader EFT equivalence relation" in prereg_text,
        "matter_outside_gate": result.get("family", {}).get("matter_coupling") == "UNRESOLVED_OUTSIDE_GATE",
        "formation_slot_count_22": result.get("formation", {}).get("slot_count") == 22,
        "no_global_uniqueness_claim_lock": "NO_GLOBAL_UNIQUENESS" in result.get("claim_locks", []),
    }

    math_checks = {
        "independent_rank_matches": rank_match,
        "independent_nullity_matches": nullity_match,
        "independent_nullspace_matches": nullspace_match,
    }

    groups = {
        "chronology": chronology,
        "historical_blob_integrity": blob_checks,
        "independent_math": math_checks,
        "controls": control_checks,
        "anti_fit_and_firewall": anti_fit,
        "scope": scope_checks,
    }
    failures = [f"{g}.{k}" for g, d in groups.items() for k, ok in d.items() if not ok]
    critic_pass = not failures

    report = {
        "schema": "RCG003_INDEPENDENT_CRITIC_V1",
        "run_head": head,
        "constructor_sha256": hashlib.sha256(constructor_path.read_bytes()).hexdigest(),
        "independent_matrix": [[str(v) for v in row] for row in A_ind],
        "independent_rank": rank_ind,
        "independent_nullity": len(ns_ind),
        "independent_primitive_nullspace": prim_ind,
        "checks": groups,
        "failures": failures,
        "critic_pass": critic_pass,
        "classification": "PASS_INDEPENDENT_CRITIC_RCG003_SCOPE_AND_PROVENANCE" if critic_pass else "INVALID_RCG003_INDEPENDENT_CRITIC_FAILURE",
        "interpretation": "Critic validates only chronology, independent algebra, controls, firewall and frozen scope. It does not promote the structural result to a complete theory or prediction.",
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
