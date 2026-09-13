import argparse
import json
import os
from pathlib import Path
import sympy as sp

MANIFEST = {
    "g72_prereg": "prereg/ITER070_G72_CD_MINIMAL_COMPLETION_EXISTENCE.md",
    "g81_terminal": "results/ITER079_G81_D_NATIVE_SOURCE_ANCHOR_AUDIT_TERMINAL.md",
    "g83_prereg": "prereg/ITER081_G83_D_MINIMAL_SOURCE_CALIBRATION_AUGMENTATION.md",
    "g52_terminal": "results/ITER048_G52H_WEAK_FIELD_HAMILTONIAN_QUOTIENT_TERMINAL.md",
    "g57_terminal": "results/ITER055_G57P_CONSTITUTION_PREREQUISITE_AUDIT_TERMINAL.md",
    "g69_terminal": "results/ITER067_G69_CANDIDATE_OWNED_NOVELTY_PREREQUISITE_TERMINAL.md",
    "g93_terminal": "results/ITER091_G93_C_CONNECTED_THREE_SOURCE_PHASE_SELECTOR_TERMINAL.md",
}


def read_manifest():
    data = {}
    for key, path in MANIFEST.items():
        p = Path(path)
        if not p.exists():
            raise RuntimeError(f"missing frozen authority file: {path}")
        data[key] = p.read_text(encoding="utf-8")
    return data


def require(text, needles, label):
    missing = [x for x in needles if x not in text]
    if missing:
        raise RuntimeError(f"{label}: missing frozen evidence tokens: {missing}")
    return True


def chi_abc(expr, a, b, c):
    total = 0
    for av in (0, 1):
        for bv in (0, 1):
            for cv in (0, 1):
                sign = (-1) ** (3 - (av + bv + cv))
                total += sign * expr.subs({a: av, b: bv, c: cv})
    return sp.simplify(total)


def lane_a():
    f = read_manifest()
    require(f["g72_prereg"], [
        "Every extra object introduced here is labeled HYPOTHESIS/CONSTRUCTION, not DERIVED RCG-002 physics.",
        "D_MINIMAL_RETARDED_CUBIC_COMPLETION_EXISTS_SCOPED",
    ], "G72")
    require(f["g81_terminal"], [
        "BLOCKED_D_NATIVE_SOURCE_OBJECT_DOES_NOT_BREAK_EXACT_CUBIC_CALIBRATION_ALIAS_SCOPED",
        "No physical observable, detector calibration, source preparation, nonlinear candidate law",
    ], "G81")
    require(f["g83_prereg"], [
        "This channel is not claimed to exist physically.",
        "defined outside the candidate D functional",
        "not an established physical signal",
    ], "G83")
    require(f["g52_terminal"], [
        "WEAK_FIELD_PAIR_ENERGY_TO_CONTROLLED_PHASE_QUOTIENT_BRIDGE_VALIDATED",
        "Weak-field point-particle branch-energy quotient bridge only.",
    ], "G52")
    require(f["g93_terminal"], [
        "BLOCKED_MISSING_CANDIDATE_OWNED_NONLINEAR_THREE_SOURCE_PHASE_MAP_SCOPED",
        "No frozen authority file supplies an explicit candidate-owned map from two independent nonlinear completion coordinates into `chi_ABC` across physical source protocols.",
    ], "G93")

    result = {
        "lane": "A",
        "pass": True,
        "classification": "D_BRIDGE_PROVENANCE_SCOPE_REPRODUCED_SCOPED",
        "objects": {
            "G72_D_cubic": "HYPOTHESIS_CONSTRUCTION",
            "G81_native_D_source": "ESTABLISHED_SCOPED_ALIAS_BLOCKER",
            "G83_reference": "CONSTRUCTION_ONLY_NOT_NATIVE_PHYSICS",
            "G52_pair_phase_bridge": "ESTABLISHED_SCOPED_PAIRWISE",
            "G93_three_source_map": "MISSING",
        },
        "manifest": MANIFEST,
    }
    return result


def lane_b():
    f = read_manifest()
    # Frozen negative/limitation evidence for the five indispensable bridge components.
    require(f["g72_prereg"], [
        "HYPOTHESIS/CONSTRUCTION, not DERIVED RCG-002 physics",
        "finite discrete-time cubic CTP kernel",
    ], "G72 bridge scope")
    require(f["g81_terminal"], [
        "does not contain an independent information direction",
        "No physical observable, detector calibration, source preparation, nonlinear candidate law",
    ], "G81 native source scope")
    require(f["g57_terminal"], [
        "A5_gravity_dynamical_principle",
        "B3_conserved_source_law",
        "B4_Bianchi_constraint_compatibility",
        "B6_covariant_relativistic_retarded_dynamics",
    ], "G57 constitution gaps")
    require(f["g69_terminal"], [
        "BLOCKED_CANDIDATE_OWNED_BEYOND_BASELINE_DYNAMICS_NOT_YET_DEFINED",
        "BLOCKED_NO_SPECIFIED_BEYOND_BASELINE_DEFORMATION_IN_FROZEN_EVIDENCE",
    ], "G69 dynamics blocker")
    require(f["g93_terminal"], [
        "No frozen authority file supplies an explicit candidate-owned map from two independent nonlinear completion coordinates into `chi_ABC` across physical source protocols.",
        "physical three-source/reference preparation protocol",
    ], "G93 bridge requirement")

    components = {
        "physical_three_source_preparation": "MISSING",
        "source_to_Delta_Sigma_embedding": "MISSING",
        "physical_source_kernel_contraction": "MISSING",
        "dimensionless_nonlinear_phase_normalization": "MISSING",
        "completion_coordinate_dependence": "MISSING",
    }
    native_complete = all(v == "EXPLICIT_NATIVE" for v in components.values())
    return {
        "lane": "B",
        "pass": True,
        "classification": "D_NATIVE_THREE_SOURCE_BRIDGE_COMPONENTS_INCOMPLETE_SCOPED",
        "components": components,
        "native_complete": native_complete,
        "selection_rank": "UNDEFINED_NATIVE_BRIDGE_INCOMPLETE",
    }


def lane_c():
    a, b, c = sp.symbols("a b c")
    d0, d1, s0, s1 = sp.symbols("d0 d1 s0 s1")
    z, r = sp.symbols("z r", nonzero=True)
    G3 = d0 * s0**2 + 2*d0*s0*s1 + d1*s1**2
    vars4 = [d0, d1, s0, s1]
    H = sp.hessian(G3, vars4).subs({v: 0 for v in vars4})
    third = [[[sp.diff(G3, vars4[i], vars4[j], vars4[k]).subs({v: 0 for v in vars4})
               for k in range(4)] for j in range(4)] for i in range(4)]
    third_nonzero = any(x != 0 for plane in third for row in plane for x in row)

    synthetic = sp.expand(G3.subs({d0: a, d1: 0, s0: b, s1: c}))
    chi_syn = chi_abc(synthetic, a, b, c)
    chi_scaled = chi_abc(sp.expand(z*synthetic), a, b, c)
    chi_rescaled_coord = chi_abc(sp.expand(G3.subs({d0: r*a, d1: 0, s0: b, s1: c})), a, b, c)

    k0, A, B, C, AB, AC, BC = sp.symbols("k0 A B C AB AC BC")
    pairwise = k0 + A*a + B*b + C*c + AB*a*b + AC*a*c + BC*b*c
    chi_pair = chi_abc(pairwise, a, b, c)

    duplicate_rank = sp.Matrix([[1, 1], [2, 2], [3, 3]]).rank()
    ok = (
        H == sp.zeros(4)
        and third_nonzero
        and sp.simplify(chi_syn - 2) == 0
        and sp.simplify(chi_scaled - 2*z) == 0
        and sp.simplify(chi_rescaled_coord - 2*r) == 0
        and chi_pair == 0
        and duplicate_rank == 1
    )
    return {
        "lane": "C",
        "pass": bool(ok),
        "classification": "D_CUBIC_ALGEBRA_HAS_CONNECTED_SENSITIVITY_BUT_NORMALIZATION_IS_EXTERNAL_SCOPED" if ok else "INVALID_G94_ALGEBRA_CONTROL",
        "hessian_zero": bool(H == sp.zeros(4)),
        "third_derivative_nonzero": bool(third_nonzero),
        "synthetic_embedding_expression": str(synthetic),
        "chi_synthetic": str(chi_syn),
        "chi_scaled_by_z": str(chi_scaled),
        "chi_under_coordinate_rescaling_r": str(chi_rescaled_coord),
        "chi_pairwise_null": str(chi_pair),
        "duplicate_protocol_rank": int(duplicate_rank),
        "scope_lock": "synthetic calibration only; no embedding, r, or z is candidate physics",
    }


def lane_d():
    f = read_manifest()
    require(f["g83_prereg"], [
        "This channel is not claimed to exist physically.",
        "defined outside the candidate D functional",
        "does **not** show that such a reference channel is physically realizable, measurable, unique, natural, or candidate-owned",
    ], "G83 anti-rescue")
    require(f["g81_terminal"], [
        "Retarded support, Sigma permutation information, CTP normalization and the zero-Hessian/nonzero-third-derivative structure constrain the object but do not calibrate its overall same-shape cubic gain.",
    ], "G81 anti-rescue")
    require(f["g93_terminal"], [
        "field redefinition, nuisance/source realizability, gauge dependence, CTP/Ward/retarded compatibility, conservation and nonlinear Bianchi/diffeomorphism consistency: **not established because the candidate-owned nonlinear map itself is absent**",
    ], "G93 downstream lock")
    require(f["g57_terminal"], [
        "B3_conserved_source_law",
        "B4_Bianchi_constraint_compatibility",
        "B6_covariant_relativistic_retarded_dynamics",
    ], "G57 consistency gaps")

    rescues = {
        "promote_G83_reference_to_native": "REJECTED_PROVENANCE",
        "identify_abstract_CTP_legs_with_physical_sources": "REJECTED_MISSING_EMBEDDING",
        "set_phase_normalization_to_one": "REJECTED_HIDDEN_NORMALIZATION",
        "promote_pairwise_G52_bridge_to_cubic": "REJECTED_ORDER_PROMOTION",
        "retardedness_implies_Bianchi_or_conservation": "REJECTED_LOGICAL_PROMOTION",
        "count_D_N3_as_two_completion_directions": "REJECTED_NUISANCE_AS_PHYSICS",
        "import_other_candidate_project": "REJECTED_INDEPENDENCE_FIREWALL",
    }
    downstream = {
        "nonlinear_conservation": False,
        "Bianchi_diffeomorphism_completion": False,
        "gauge_independent_three_source_extraction": False,
        "physical_three_source_realizability": False,
    }
    return {
        "lane": "D",
        "pass": True,
        "classification": "D_THREE_SOURCE_BRIDGE_ANTI_RESCUE_LOCKS_HOLD_SCOPED",
        "rescues": rescues,
        "downstream_established": downstream,
    }


def aggregate(root):
    data = []
    for lane in "ABCD":
        found = []
        for dp, _, files in os.walk(root):
            for fn in files:
                if fn == f"g94_{lane}.json":
                    found.append(os.path.join(dp, fn))
        if len(found) != 1:
            raise RuntimeError(f"lane {lane}: expected exactly one raw json, got {found}")
        with open(found[0], encoding="utf-8") as fh:
            data.append(json.load(fh))
    by = {x["lane"]: x for x in data}
    controls_valid = all(x.get("pass") for x in data)
    native_complete = bool(by["B"].get("native_complete"))
    if not controls_valid:
        classification = "INVALID_G94_IMPLEMENTATION_OR_PROVENANCE"
        rank = "INVALID"
    elif not native_complete:
        classification = "BLOCKED_D_CUBIC_CTP_OBJECT_LACKS_NATIVE_THREE_SOURCE_SOURCE_TO_PHASE_BRIDGE_SCOPED"
        rank = "UNDEFINED_NATIVE_BRIDGE_INCOMPLETE"
    else:
        # The current frozen implementation has no evidence path that can reach this branch;
        # a future native bridge would require a new preregistration rather than post-hoc promotion.
        classification = "INVALID_G94_UNPREREGISTERED_NATIVE_BRIDGE_PROMOTION"
        rank = "INVALID_REQUIRES_NEW_GATE"
    return {
        "gate": "G94",
        "pass": bool(controls_valid),
        "classification": classification,
        "selection_rank": rank,
        "native_complete": native_complete,
        "lanes": data,
        "programme_readiness_percent": 66,
        "theory_established_percent": 0,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--lane", choices=list("ABCD"))
    p.add_argument("--aggregate")
    p.add_argument("--out", required=True)
    args = p.parse_args()
    if args.aggregate:
        result = aggregate(args.aggregate)
    else:
        result = {"A": lane_a, "B": lane_b, "C": lane_c, "D": lane_d}[args.lane]()
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result.get("pass", False):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
