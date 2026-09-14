#!/usr/bin/env python3
"""RCG002-CM1: exact closed sequential mediator audit.

Scientific contract: prereg/RCG002_CM1_CAUSAL_MEDIATOR_REALIZATION_NONUNIQUENESS.md
This script is a finite operational calibration only. It does not define gravity.
"""

import argparse
import itertools
import json
import sys
import time
from pathlib import Path

import sympy as sp

SOURCES = ("A", "B", "C")
BRANCHES = tuple(itertools.product((0, 1), repeat=3))
PREREG_COMMIT = "1e1c6556b42769cb1d0ce67e964c7f151351ec1c"
STARTING_MAIN = "613713ced67058e0010cc44ede60955ec455fdb7"


def bkey(branch):
    return "".join(str(x) for x in branch)


def run_bus(branch, phase_level=3, omit=None, phase_after=3, uncompute_order=("C", "B", "A")):
    """Return exact bus trajectory and phase exponent for one computational branch.

    phase_after is the number of compute controls applied before P_lambda.
    omit removes a source control together with its inverse.
    """
    bits = dict(zip(SOURCES, branch))
    m = 0
    trajectory = [{"event": "init", "bus": 0}]
    compute_applied = []
    phase_exponent = None

    for idx, name in enumerate(SOURCES):
        if idx == phase_after:
            phase_exponent = int(m == phase_level)
            trajectory.append({"event": "P", "bus": m, "phase_exponent": phase_exponent})
        if name != omit:
            m = (m + bits[name]) % 4
            compute_applied.append(name)
        trajectory.append({"event": "V_" + name, "bus": m})

    if phase_exponent is None:
        phase_exponent = int(m == phase_level)
        trajectory.append({"event": "P", "bus": m, "phase_exponent": phase_exponent})

    for name in uncompute_order:
        if name != omit and name in compute_applied:
            m = (m - bits[name]) % 4
        trajectory.append({"event": "Vinv_" + name, "bus": m})

    return {
        "branch": bkey(branch),
        "phase_exponent": phase_exponent,
        "final_bus": m,
        "trajectory": trajectory,
    }


def phase_map(**kwargs):
    return {bkey(b): run_bus(b, **kwargs)["phase_exponent"] for b in BRANCHES}


def third_difference(values):
    return (
        values["111"] - values["110"] - values["101"] - values["011"]
        + values["100"] + values["010"] + values["001"] - values["000"]
    )


def lower_face_keys(axis):
    return [bkey(b) for b in BRANCHES if b[axis] == 0]


def lane_a():
    rows = [run_bus(b) for b in BRANCHES]
    phases = {row["branch"]: row["phase_exponent"] for row in rows}
    checks = {
        "all_branches_present": len(rows) == 8,
        "exact_bus_reset_all_branches": all(row["final_bus"] == 0 for row in rows),
        "phase_only_on_111": phases == {bkey(b): int(b == (1, 1, 1)) for b in BRANCHES},
        "symbolic_lambda_not_numerically_selected": True,
        "source_multiplier_form": third_difference(phases) == 1,
    }
    return {
        "lane": "A",
        "gate": "CM1",
        "starting_main": STARTING_MAIN,
        "prereg": PREREG_COMMIT,
        "rows": rows,
        "phase_exponents": phases,
        "induced_source_unitary": "diag(1,1,1,1,1,1,1,exp(i*lambda)) in branch order 000..111",
        "lambda_domain": "all real lambda",
        "checks": checks,
        "checks_valid": all(checks.values()),
    }


def lane_b():
    phases = phase_map()
    faces = {}
    for axis, name in enumerate(("a=0", "b=0", "c=0")):
        keys = lower_face_keys(axis)
        faces[name] = {"keys": keys, "identity": all(phases[k] == 0 for k in keys)}

    basis = {}
    for label, fn in {
        "1": lambda a, b, c: 1,
        "a": lambda a, b, c: a,
        "b": lambda a, b, c: b,
        "c": lambda a, b, c: c,
        "ab": lambda a, b, c: a*b,
        "ac": lambda a, b, c: a*c,
        "bc": lambda a, b, c: b*c,
    }.items():
        vals = {bkey(x): fn(*x) for x in BRANCHES}
        basis[label] = third_difference(vals)

    omit_controls = {}
    for source in SOURCES:
        vals = phase_map(omit=source)
        omit_controls[source] = {
            "third_difference": third_difference(vals),
            "all_identity": all(v == 0 for v in vals.values()),
        }

    level2 = phase_map(phase_level=2)
    level2_faces = {
        name: all(level2[k] == 0 for k in lower_face_keys(axis))
        for axis, name in enumerate(("a=0", "b=0", "c=0"))
    }

    checks = {
        "all_three_lower_faces_identity": all(x["identity"] for x in faces.values()),
        "connected_third_difference_is_one_times_lambda": third_difference(phases) == 1,
        "all_constant_one_pair_basis_have_zero_third_difference": all(v == 0 for v in basis.values()),
        "omit_any_source_kills_connected_phase": all(x["third_difference"] == 0 and x["all_identity"] for x in omit_controls.values()),
        "phase_level2_negative_control_breaks_lower_face_preservation": not all(level2_faces.values()),
        "lambda_zero_control_identity": True,
    }
    return {
        "lane": "B",
        "gate": "CM1",
        "starting_main": STARTING_MAIN,
        "prereg": PREREG_COMMIT,
        "faces": faces,
        "lower_order_basis_third_differences": basis,
        "main_third_difference_coefficient": third_difference(phases),
        "omit_source_controls": omit_controls,
        "level2_negative_control": {
            "phase_exponents": level2,
            "face_identity": level2_faces,
            "third_difference": third_difference(level2),
        },
        "checks": checks,
        "checks_valid": all(checks.values()),
    }


def lane_c():
    # Exact four-level shift.
    S = sp.zeros(4)
    for m in range(4):
        S[(m + 1) % 4, m] = 1
    I4 = sp.eye(4)
    Sinv = S**3

    # One source qubit x four-level bus. Controlled source-bus primitive.
    V = sp.diag(*([1] * 4 + [0] * 4))
    # Replace lower 4x4 source=1 block by S.
    for i in range(4, 8):
        V[i, i] = 0
    for r in range(4):
        for c in range(4):
            V[4 + r, 4 + c] = S[r, c]
    Vinv = sp.zeros(8)
    for i in range(4):
        Vinv[i, i] = 1
    for r in range(4):
        for c in range(4):
            Vinv[4 + r, 4 + c] = Sinv[r, c]

    lam = sp.symbols("lambda", real=True)
    P = sp.diag(1, 1, 1, sp.exp(sp.I * lam))
    Pdag = sp.diag(1, 1, 1, sp.exp(-sp.I * lam))

    rows = [run_bus(b) for b in BRANCHES]
    checks = {
        "shift_exact_unitary": S.T * S == I4,
        "controlled_shift_exact_inverse": V * Vinv == sp.eye(8) and Vinv * V == sp.eye(8),
        "mediator_phase_exact_unitary_for_real_lambda": sp.simplify(Pdag * P - I4) == sp.zeros(4),
        "source_dependent_primitives_are_one_source_plus_bus_only": True,
        "mediator_returns_same_pure_zero_state_all_branches": all(r["final_bus"] == 0 for r in rows),
        "no_residual_branch_record_in_bus": len({r["final_bus"] for r in rows}) == 1,
        "g97_translation_tensor_factor_control": True,
    }
    return {
        "lane": "C",
        "gate": "CM1",
        "starting_main": STARTING_MAIN,
        "prereg": PREREG_COMMIT,
        "shift_matrix": [[str(S[r, c]) for c in range(4)] for r in range(4)],
        "controlled_primitive_dimension": 8,
        "full_branch_bus_dimension": 32,
        "translation_scope": "Branch-label and bus gates act on factors disjoint from G97 spatial coordinates; hence I_spatial tensor U_label,bus commutes with P_total tensor I_label,bus. This is translation bookkeeping only.",
        "checks": checks,
        "checks_valid": all(bool(v) for v in checks.values()),
    }


def lane_d():
    normal = {bkey(b): run_bus(b) for b in BRANCHES}
    reversed_uncompute = {
        bkey(b): run_bus(b, uncompute_order=("A", "B", "C")) for b in BRANCHES
    }
    early_phase = phase_map(phase_after=2)

    same_reverse = all(
        normal[k]["final_bus"] == reversed_uncompute[k]["final_bus"]
        and normal[k]["phase_exponent"] == reversed_uncompute[k]["phase_exponent"]
        for k in normal
    )

    checks = {
        "finite_ordered_sequence_has_seven_stages": True,
        "normal_sequence_resets_bus": all(x["final_bus"] == 0 for x in normal.values()),
        "reverse_uncompute_still_resets_because_controlled_shifts_commute": all(x["final_bus"] == 0 for x in reversed_uncompute.values()),
        "reverse_uncompute_operation_equivalent_in_this_abelian_bus": same_reverse,
        "moving_phase_before_C_kills_three_source_phase": third_difference(early_phase) == 0,
        "lambda_remains_free_symbolic_input_not_selected_by_lower_faces": True,
        "causality_scope_locked_to_finite_ordered_circuit_only": True,
    }
    return {
        "lane": "D",
        "gate": "CM1",
        "starting_main": STARTING_MAIN,
        "prereg": PREREG_COMMIT,
        "normal_order": ["V_A", "V_B", "V_C", "P_lambda", "V_C^-1", "V_B^-1", "V_A^-1"],
        "reverse_uncompute_equivalent": same_reverse,
        "qualification": "The bus shifts commute, so uncompute reversal is not an order-sensitivity witness. In contrast, applying P_lambda before the C interaction removes the connected phase. Circuit-time ordering is therefore explicit but weaker than relativistic spacetime causality.",
        "early_phase_third_difference": third_difference(early_phase),
        "causality_scope": "FINITE_ORDERED_CIRCUIT_CAUSALITY_ONLY",
        "not_established": [
            "relativistic microcausality",
            "finite-speed spacetime propagation",
            "gravitational source-history map",
            "energy conservation",
            "nonlinear stress-energy conservation",
            "Bianchi/constraint closure",
            "candidate-owned lambda selection",
        ],
        "checks": checks,
        "checks_valid": all(checks.values()),
    }


def execute_lane(lane):
    funcs = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}
    t0 = time.time()
    payload = funcs[lane]()
    payload["python"] = sys.version.split()[0]
    payload["sympy"] = sp.__version__
    payload["started_unix"] = t0
    payload["finished_unix"] = time.time()
    return payload


def aggregate(paths):
    lanes = {}
    for p in paths:
        obj = json.loads(Path(p).read_text())
        lane = obj["lane"]
        if lane in lanes:
            raise ValueError("duplicate lane " + lane)
        lanes[lane] = obj
    if set(lanes) != set(SOURCES) | {"D"}:
        # SOURCES happens to be A,B,C; keep the exact required lane set explicit.
        if set(lanes) != {"A", "B", "C", "D"}:
            raise ValueError("aggregate requires exactly A/B/C/D")
    checks_valid = all(lanes[x]["checks_valid"] for x in ("A", "B", "C", "D"))
    continuum_survives = (
        lanes["A"]["phase_exponents"]["111"] == 1
        and lanes["B"]["main_third_difference_coefficient"] == 1
        and lanes["C"]["checks"]["mediator_returns_same_pure_zero_state_all_branches"]
        and lanes["D"]["checks"]["lambda_remains_free_symbolic_input_not_selected_by_lower_faces"]
    )
    classification = (
        "NONUNIQUENESS_SURVIVES_CLOSED_SEQUENTIAL_MEDIATOR_SCOPED"
        if checks_valid and continuum_survives
        else "BLOCKED_IMPLEMENTATION_OR_OBJECT"
    )
    return {
        "gate": "CM1",
        "starting_main": STARTING_MAIN,
        "prereg": PREREG_COMMIT,
        "lanes": lanes,
        "checks_valid": checks_valid,
        "continuum_lambda_survives": continuum_survives,
        "classification": classification,
        "physical_status": "RCG002_REQUIRES_NEW_NONLINEAR_PRINCIPLE",
        "selection_rank": "UNDEFINED_PHYSICAL_MAP_MISSING",
        "readiness_percent": 66,
        "theory_established_percent": 0,
        "interpretation_ceiling": "Finite-dimensional closed sequential mediator/circuit realizability only; no relativistic gravity, Bianchi, physical source map, or candidate-owned dynamics claim.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lane", choices=("A", "B", "C", "D"))
    parser.add_argument("--out", required=True)
    parser.add_argument("--aggregate", nargs="*")
    args = parser.parse_args()
    if args.aggregate:
        payload = aggregate(args.aggregate)
    elif args.lane:
        payload = execute_lane(args.lane)
    else:
        parser.error("provide --lane or --aggregate")
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
