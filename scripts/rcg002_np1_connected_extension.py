#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
import platform
import time

import sympy as sp

PREREG = "1c63d49ccfbc0978c0d791fabd335a00186fa4f4"
BASE = "94467fdacc93f65102333fa01b7a34bb0d857a79"
BITS = list(itertools.product((0, 1), repeat=3))


def q(bits):
    a, b, c = bits
    return a * b * c


def delta3(expr, vars_):
    out = 0
    for bits in BITS:
        sign = (-1) ** (3 - sum(bits))
        out += sign * expr.subs(dict(zip(vars_, bits)), simultaneous=True)
    return sp.expand(out)


def lane_a():
    r = sp.symbols("r", real=True, nonnegative=True)
    lam = sp.symbols("lambda", real=True)
    # Seven cube vertices have q=0 and one has q=1.  In the normalized
    # q-sector basis, the real dephasing kernel has this only nonzero block.
    compressed = sp.Matrix([[7, sp.sqrt(7) * r], [sp.sqrt(7) * r, 1]])
    det_compressed = sp.simplify(compressed.det())
    trace_compressed = sp.trace(compressed)

    # Explicit Gram vectors for the q sectors; a diagonal phase congruence
    # supplies lambda and preserves PSD.
    gram_v0 = sp.Matrix([1, 0])
    gram_v1 = sp.Matrix([r, sp.sqrt(1 - r**2)])
    gram_cross = sp.simplify((gram_v0.T * gram_v1)[0])

    neg = sp.Matrix([[1, 1, 1], [1, 1, -1], [1, -1, 1]])
    neg_det = sp.factor(neg.det())

    checks = {
        "compressed_trace_positive": trace_compressed == 8,
        "compressed_determinant": det_compressed == 7 * (1 - r**2),
        "gram_cross_is_r": gram_cross == r,
        "gamma_zero_rank_one": compressed.subs(r, 1).rank() == 1,
        "negative_control_fails_psd": neg_det == -4,
    }
    return {
        "lane": "A",
        "checks": checks,
        "compressed_kernel": str(compressed),
        "compressed_det": str(det_compressed),
        "gram_vectors": {"q0": [str(x) for x in gram_v0], "q1": [str(x) for x in gram_v1]},
        "phase_congruence": "C = D(lambda) R D(lambda)^dagger, D_x=exp(i lambda q(x)); PSD preserved",
        "schur_extension_theorem": "If F0>=0 and C>=0 then F0 .* C>=0; both unit diagonal imply normalized Schur channel.",
        "negative_control_det": str(neg_det),
        "scope": "Operational Schur-kernel theorem; no gravitational dynamics or spacetime locality is inferred.",
    }


def lane_b():
    a, b, c, lam, gam = sp.symbols("a b c lambda gamma", real=True)
    c0, ca, cb, cc, cab, cac, cbc = sp.symbols("c0 ca cb cc cab cac cbc", real=True)
    lower = c0 + ca*a + cb*b + cc*c + cab*a*b + cac*a*c + cbc*b*c
    connected = lam * a * b * c
    d3_lower = delta3(lower, (a, b, c))
    d3_conn = delta3(connected, (a, b, c))

    face_checks = {}
    for idx, var in enumerate((a, b, c)):
        face_checks[f"face_{idx}_q_zero"] = sp.expand((a*b*c).subs(var, 0)) == 0

    # q is binary.  C has modulus one for equal q and exp(-gamma) for
    # coherences crossing q=0 <-> q=1.  Phase and log-modulus responses are
    # independent coordinates at 111<->000.
    phase_111_000 = sp.simplify(lam * (1 - 0))
    logmod_111_000 = -gam
    jac = sp.Matrix([[sp.diff(phase_111_000, lam), sp.diff(phase_111_000, gam)],
                     [sp.diff(logmod_111_000, lam), sp.diff(logmod_111_000, gam)]])

    checks = {
        **face_checks,
        "lower_body_third_difference_zero": d3_lower == 0,
        "connected_third_difference_lambda": d3_conn == lam,
        "phase_noise_coordinates_independent": jac.det() == -1,
    }
    return {
        "lane": "B",
        "checks": checks,
        "third_difference_lower": str(d3_lower),
        "third_difference_connected": str(d3_conn),
        "observable_jacobian_lambda_gamma": str(jac),
        "face_statement": "On a=0 or b=0 or c=0, q=abc=0 for every state on that face, so C_lambda,gamma=1 identically.",
        "rephasing_statement": "Adding any constant/one-body/two-body diagonal phase changes no third finite difference; lambda is not removable by that lower-body rephasing quotient.",
        "scope": "Moebius/face theorem on the binary branch cube; not a proof of physical gravitational accessibility.",
    }


def lane_c():
    lam, gam, t = sp.symbols("lambda gamma t", real=True, nonnegative=True)
    # Toy spatial generator tensored with exact 8-dimensional branch space.
    P = sp.diag(-1, 1)
    I8 = sp.eye(8)
    Q = sp.diag(*([0] * 7 + [1]))
    Ptot = sp.kronecker_product(P, I8)
    Qfull = sp.kronecker_product(sp.eye(2), Q)
    comm = sp.simplify(Ptot * Qfull - Qfull * Ptot)

    h = 6 * lam * t * (1 - t)
    integrated = sp.integrate(h, (t, 0, 1))

    # For X~N(0,2 gamma), E exp(i X Delta q)=exp(-gamma Delta q^2).
    dq = sp.symbols("dq", integer=True)
    gaussian_characteristic = sp.exp(-gam * dq**2)

    checks = {
        "translation_commutator_zero": comm == sp.zeros(16),
        "time_profile_integrates_lambda": integrated == lam,
        "gaussian_characteristic_normalized": gaussian_characteristic.subs(dq, 0) == 1,
        "gaussian_crossing_factor": gaussian_characteristic.subs(dq, 1) == sp.exp(-gam),
        "gaussian_reverse_crossing_factor": gaussian_characteristic.subs(dq, -1) == sp.exp(-gam),
    }
    return {
        "lane": "C",
        "checks": checks,
        "Q_rank": Q.rank(),
        "commutator_rank": comm.rank(),
        "time_profile": str(h),
        "time_integral": str(integrated),
        "dilation": "U_X=exp(i (lambda+X) Q), X Gaussian with variance 2 gamma; averaging is random-unitary CPTP.",
        "scope": "Finite laboratory-time normalized evolution and total-translation compatibility only; no relativistic microcausality, stress-energy, Bianchi or gravity claim.",
    }


def lane_d(repo_root: Path):
    files = {
        "seed": repo_root / "candidates/RCG_002_RELATIONAL_CONTROLLED_PHASE_CHANNEL.md",
        "contract": repo_root / "docs/CONSTRUCTION_CONTRACT.md",
        "baseline": repo_root / "candidates/RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md",
        "recovery": repo_root / "recovery/CURRENT_FRONT.md",
        "ncp1": repo_root / "results/RCG002_NCP1_NOISY_COMPLETION_TERMINAL.md",
    }
    texts = {k: p.read_text(encoding="utf-8") for k, p in files.items()}
    markers = {
        "seed_no_microscopic_chi": "no microscopic formula for `chi` is asserted" in texts["seed"],
        "seed_must_derive_not_fit": "rather than fit it freely" in texts["seed"],
        "contract_search_minimal_dynamics": "minimal dynamics" in texts["contract"],
        "baseline_delta_gamma_unselected": "No form for `Delta Gamma` is chosen" in texts["baseline"],
        "recovery_no_candidate_owned_law": "At present no such candidate-owned law exists" in texts["recovery"],
        "recovery_requires_new_principle": "RCG002_REQUIRES_NEW_NONLINEAR_PRINCIPLE" in texts["recovery"],
        "ncp1_physical_evolution_blocked": "BLOCKED_PHYSICAL_EVOLUTION" in texts["ncp1"],
        "ncp1_requires_new_principle": "RCG002_REQUIRES_NEW_NONLINEAR_PRINCIPLE" in texts["ncp1"],
    }
    return {
        "lane": "D",
        "checks": markers,
        "authority_files": {k: str(p) for k, p in files.items()},
        "ownership": {
            "DERIVED_FROM_RCG002": [
                "normalized quantum-state evolution at the operational level",
                "relational phase quotient / controlled-phase architecture",
                "recover validated weak-field branch",
                "closed total-source translation/conservation prerequisite from G97",
            ],
            "ALLOWED_BUT_NOT_SELECTED": [
                "connected unitary phase lambda",
                "connected dephasing gamma",
                "other positive higher-order channel completions",
            ],
            "REQUIRES_NEW_PRINCIPLE": [
                "microscopic nonlinear source/state/evolution law",
                "rule fixing connected phase/noise hierarchy",
                "nonlinear stress-energy/Bianchi/constraint completion",
                "physical source-to-branch-history map and spacetime causal realization",
            ],
        },
        "authority_result": "NO_EXISTING_NATIVE_SELECTOR_FOUND" if all(markers.values()) else "AUTHORITY_MARKER_MISMATCH",
        "scope": "Repository-authority sufficiency audit; marker success is supporting provenance, not by itself a no-go theorem.",
    }


def execute(lane: str, repo_root: Path):
    start = time.time()
    if lane == "A": result = lane_a()
    elif lane == "B": result = lane_b()
    elif lane == "C": result = lane_c()
    elif lane == "D": result = lane_d(repo_root)
    else: raise ValueError(lane)
    result.update({
        "gate": "RCG002-NP1",
        "prereg_commit": PREREG,
        "frozen_base": BASE,
        "started_unix": start,
        "finished_unix": time.time(),
        "python": platform.python_version(),
        "sympy": sp.__version__,
    })
    result["checks_valid"] = all(result["checks"].values())
    return result


def write_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=list("ABCD"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--aggregate", nargs="*")
    args = ap.parse_args()
    out = Path(args.out)
    root = Path(__file__).resolve().parents[1]

    if args.aggregate:
        lanes = {}
        raw_sha = {}
        for name in args.aggregate:
            p = Path(name)
            payload = json.loads(p.read_text(encoding="utf-8"))
            lanes[payload["lane"]] = payload
            raw_sha[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
        if set(lanes) != set("ABCD"):
            raise SystemExit("aggregate requires exactly A/B/C/D")
        all_valid = all(lanes[x]["checks_valid"] for x in "ABCD")
        authority_ok = lanes["D"]["authority_result"] == "NO_EXISTING_NATIVE_SELECTOR_FOUND"
        classification = (
            "RCG002_CURRENT_PRINCIPLES_ALLOW_CONTINUUM_CONNECTED_CHANNEL_EXTENSIONS_SCOPED"
            if all_valid and authority_ok else "INVALID_IMPLEMENTATION_OR_AUTHORITY"
        )
        agg = {
            "gate": "RCG002-NP1",
            "prereg_commit": PREREG,
            "frozen_base": BASE,
            "lanes": lanes,
            "raw_sha256": raw_sha,
            "all_checks_valid": all_valid,
            "classification": classification,
            "physical_classification": "RCG002_REQUIRES_NEW_NONLINEAR_PRINCIPLE" if classification.startswith("RCG002_CURRENT") else "UNRESOLVED",
            "operational_extension_dimension_lower_bound": 2 if classification.startswith("RCG002_CURRENT") else None,
            "coordinates": ["lambda_connected_phase", "gamma_connected_dephasing"] if classification.startswith("RCG002_CURRENT") else [],
            "physical_selector_rank": "UNDEFINED_PHYSICAL_MAP_MISSING",
            "readiness_percent": 66,
            "theory_established_percent": 0,
        }
        write_json(out, agg)
        print(json.dumps(agg, indent=2, sort_keys=True))
        if not all_valid:
            raise SystemExit(2)
        return

    if not args.lane:
        raise SystemExit("provide --lane or --aggregate")
    result = execute(args.lane, root)
    write_json(out, result)
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["checks_valid"]:
        raise SystemExit(2)

if __name__ == "__main__":
    main()
