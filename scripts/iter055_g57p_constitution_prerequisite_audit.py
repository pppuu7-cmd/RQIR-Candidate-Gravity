import argparse
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EVIDENCE = {
    "contract": "docs/CONSTRUCTION_CONTRACT.md",
    "candidate": "candidates/RCG_002_RELATIONAL_CONTROLLED_PHASE_CHANNEL.md",
    "g50r": "results/ITER046_G50R_LOCAL_BASIS_COVARIANCE_TERMINAL.md",
    "g51k": "results/ITER047_G51K_BRANCHWISE_RETARDED_KERNEL_TERMINAL.md",
    "g52h": "results/ITER048_G52H_WEAK_FIELD_HAMILTONIAN_QUOTIENT_TERMINAL.md",
    "g53w": "results/ITER049_G53W_FINITE_SIZE_WAVEPACKET_TERMINAL.md",
    "g54q": "results/ITER050_G54Q_FINITE_SIZE_CHANNEL_TERMINAL.md",
    "g55o": "results/ITER051_G55O_HELDOUT_ENTANGLEMENT_OBSERVABLE_TERMINAL.md",
    "g56f": "results/ITER052_G56F_GAUSSIAN_CONTINUUM_FIELD_CLOSURE_TERMINAL.md",
    "g56d": "results/ITER053_G56D_DIAGNOSTICS_TERMINAL.md",
    "front": "recovery/CURRENT_FRONT.md",
    "ledger": "research_log/RQIRCG_RESEARCH_LEDGER.md",
}


def load():
    out = {}
    missing = []
    for key, rel in EVIDENCE.items():
        p = ROOT / rel
        if not p.exists():
            missing.append(rel)
            out[key] = ""
        else:
            out[key] = p.read_text(encoding="utf-8")
    return out, missing


def item(status, scope, evidence, test):
    return {"status": status, "scope": scope, "evidence": evidence, "test": bool(test)}


def stream_a(text):
    cand = text["candidate"]
    g52 = text["g52h"]
    g53 = text["g53w"]
    g56f = text["g56f"]
    g56d = text["g56d"]

    a1_ok = all(x in cand for x in ["rho -> E_eta", "U_chi = diag", "two-level probes"])
    a2_ok = "WEAK_FIELD_PAIR_ENERGY_TO_CONTROLLED_PHASE_QUOTIENT_BRIDGE_VALIDATED" in g52 and "FINITE_SIZE_GAUSSIAN_WAVEPACKET_WEAK_FIELD_BRIDGE_VALIDATED" in g53
    a3_defined = all(x in g56f for x in ["Gaussian", "source/kernel identity", "G56F_FROZEN_CONTINUUM_FIELD_CLOSURE_RULE_NOT_MET"]) and "INDEPENDENT_IDENTITY_SUPPORT" in g56d

    # Candidate-owned continuum gravity structure must be an actual definition, not a scope-lock/desideratum.
    definition_corpus = cand
    a4_markers = ["g_{mu nu}", "g_mu", "h_{mu nu}", "h_mu", "spacetime metric field", "gravitational tensor field"]
    a5_markers = ["S[g", "delta S", "field equation :=", "dynamics :=", "influence functional :="]
    a6_markers = ["nonlinear classical limit :=", "Einstein equation recovered", "nonlinear GR limit"]
    a4 = any(m in definition_corpus for m in a4_markers)
    a5 = any(m in definition_corpus for m in a5_markers)
    a6 = any(m in definition_corpus for m in a6_markers)

    items = {
        "A1_operational_quantum_channel": item("EXPLICIT" if a1_ok else "ABSENT", "two-probe operational channel", [EVIDENCE["candidate"]], a1_ok),
        "A2_microscopic_weak_field_phase_source_map": item("EXPLICIT" if a2_ok else "ABSENT", "weak-field pair-energy / finite-size source to phase bridge only", [EVIDENCE["g52h"], EVIDENCE["g53w"]], a2_ok),
        "A3_continuum_weak_field_source_kernel_object": item("EXPLICIT" if a3_defined else "ABSENT", "Gaussian weak-field source/kernel object; historical G56-F frozen FAIL retained", [EVIDENCE["g56f"], EVIDENCE["g56d"]], a3_defined),
        "A4_spacetime_gravitational_field_variable": item("EXPLICIT" if a4 else "ABSENT", "would require candidate-owned spacetime field/tensor definition", [EVIDENCE["candidate"]], a4),
        "A5_gravity_dynamical_principle": item("EXPLICIT" if a5 else "ABSENT", "would require candidate-owned field equation/action/functional", [EVIDENCE["candidate"]], a5),
        "A6_nonlinear_classical_gravity_limit": item("EXPLICIT" if a6 else "ABSENT", "would require a candidate-owned nonlinear classical gravity recovery statement/derivation", [EVIDENCE["candidate"]], a6),
    }
    return {"stream": "A_OBJECT_INVENTORY", "items": items}


def stream_b(text):
    cand = text["candidate"]
    g50 = text["g50r"]
    g51 = text["g51k"]

    b1 = "DERIVED_SCOPED_G50A_LOCAL_BASIS_COVARIANT_SUPPORT" in g50
    b5 = "BRANCHWISE_RETARDED_KERNEL_VALIDATED_AND_SHARED_RMAX_CAUSAL_PROXY_REJECTED" in g51

    # Search only the candidate definition for full spacetime laws, not negative scope-lock text in results.
    b2 = any(m in cand for m in ["diffeomorphism transformation :=", "coordinate transformation law :=", "Lie derivative gauge transformation :="])
    b3 = any(m in cand for m in ["nabla_mu T", "covariant divergence condition :=", "source conservation :="])
    b4 = any(m in cand for m in ["Bianchi identity :=", "constraint compatibility :=", "nabla_mu G"])
    b6 = any(m in cand for m in ["covariant retarded Green function :=", "G_ret^{mu", "relativistic causal field equation :="])

    items = {
        "B1_local_Hilbert_basis_covariance": item("EXPLICIT" if b1 else "ABSENT", "local-unitary basis covariance of finite-panel operational result only", [EVIDENCE["g50r"]], b1),
        "B2_spacetime_coordinate_diffeomorphism_law": item("EXPLICIT" if b2 else "ABSENT", "full spacetime covariance prerequisite", [EVIDENCE["candidate"]], b2),
        "B3_conserved_source_law": item("EXPLICIT" if b3 else "ABSENT", "candidate-owned covariant source conservation prerequisite", [EVIDENCE["candidate"]], b3),
        "B4_Bianchi_constraint_compatibility": item("EXPLICIT" if b4 else "ABSENT", "candidate-owned geometric/constraint identity prerequisite", [EVIDENCE["candidate"]], b4),
        "B5_causal_retarded_response": item("SCOPED_PROXY" if b5 else "ABSENT", "finite branchwise-retarded weak-field toy-kernel only", [EVIDENCE["g51k"]], b5),
        "B6_covariant_relativistic_retarded_dynamics": item("EXPLICIT" if b6 else "ABSENT", "requires tensor/spacetime retarded dynamics; G51-K explicitly does not establish this", [EVIDENCE["candidate"], EVIDENCE["g51k"]], b6),
    }
    return {"stream": "B_COVARIANCE_CONSERVATION_CAUSALITY", "items": items}


def stream_c(text):
    cand = text["candidate"]
    contract = text["contract"]
    g52 = text["g52h"]
    g53 = text["g53w"]
    g54 = text["g54q"]
    g55 = text["g55o"]

    c1 = all(x in cand for x in ["rho -> E_eta", "U_chi = diag"]) and "FINITE_SIZE_WEAK_FIELD_CONTROLLED_PHASE_CHANNEL_INTEGRATED_SCOPED" in g54
    c2 = "HELDOUT_FINITE_SIZE_ENTANGLEMENT_OBSERVABLE_TRANSPORT_VALIDATED_SCOPED" in g55
    c3 = all([
        "WEAK_FIELD_PAIR_ENERGY_TO_CONTROLLED_PHASE_QUOTIENT_BRIDGE_VALIDATED" in g52,
        "FINITE_SIZE_GAUSSIAN_WAVEPACKET_WEAK_FIELD_BRIDGE_VALIDATED" in g53,
        "FINITE_SIZE_WEAK_FIELD_CONTROLLED_PHASE_CHANNEL_INTEGRATED_SCOPED" in g54,
    ])

    # Checklist desiderata in CONSTRUCTION_CONTRACT do not count as derived candidate results.
    derived_corpus = cand + "\n" + g52 + "\n" + g53 + "\n" + g54 + "\n" + g55
    c4 = any(m in derived_corpus for m in ["QFT baseline derived :=", "EFT baseline derived :=", "QFT/EFT matching equation :="])
    c5 = any(m in derived_corpus for m in ["G -> 0: PASS", "G->0 decoupling validated", "G_zero_limit_validated=true"])
    c6 = any(m in derived_corpus for m in ["hbar -> 0: PASS", "hbar->0 classical limit validated", "hbar_zero_limit_validated=true"])
    c7 = any(m in cand for m in ["path integral :=", "functional measure :=", "quantized gravitational field :=", "gravitational Hilbert space :="])

    seed_old = "At this stage no microscopic formula for `chi` is asserted" in cand
    later_bridge = c3
    stale = bool(seed_old and later_bridge)

    items = {
        "C1_normalized_operational_quantum_evolution": item("EXPLICIT" if c1 else "ABSENT", "finite weak-field operational controlled-phase channel", [EVIDENCE["candidate"], EVIDENCE["g54q"]], c1),
        "C2_heldout_quantum_observable_relation": item("EXPLICIT" if c2 else "ABSENT", "held-out finite-size entanglement observable only", [EVIDENCE["g55o"]], c2),
        "C3_weak_field_source_energy_phase_reduction_chain": item("EXPLICIT" if c3 else "ABSENT", "weak-field point/finite-size source-energy-to-channel chain only", [EVIDENCE["g52h"], EVIDENCE["g53w"], EVIDENCE["g54q"]], c3),
        "C4_QFT_EFT_baseline_relation": item("EXPLICIT" if c4 else "ABSENT", "construction-contract checklist alone is not positive evidence", [EVIDENCE["contract"], EVIDENCE["candidate"]], c4),
        "C5_G_to_zero_decoupling_derived": item("EXPLICIT" if c5 else "ABSENT", "requires explicit tested/derived candidate result in frozen evidence set", [EVIDENCE["contract"], EVIDENCE["candidate"]], c5),
        "C6_hbar_to_zero_classical_limit_derived": item("EXPLICIT" if c6 else "ABSENT", "requires explicit tested/derived candidate result in frozen evidence set", [EVIDENCE["contract"], EVIDENCE["candidate"]], c6),
        "C7_gravitational_quantization_measure_dynamics": item("EXPLICIT" if c7 else "ABSENT", "requires candidate-owned quantum gravitational field/measure/dynamics", [EVIDENCE["candidate"]], c7),
        "C8_candidate_document_sync": {"status": "STALE" if stale else "CURRENT", "scope": "documentation consistency only", "evidence": [EVIDENCE["candidate"], EVIDENCE["g52h"], EVIDENCE["g53w"], EVIDENCE["g54q"]], "test": stale},
    }
    return {"stream": "C_QUANTUM_LIMIT_MEASURE_SYNC", "items": items}


def aggregate(directory):
    rows = []
    for p in sorted(Path(directory).rglob("*.json")):
        try:
            obj = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if obj.get("iteration") == "Iter055" and obj.get("gate") == "G57-P" and obj.get("stream"):
            rows.append(obj)
    by = {x["stream"]: x for x in rows}
    expected = {"A_OBJECT_INVENTORY", "B_COVARIANCE_CONSERVATION_CAUSALITY", "C_QUANTUM_LIMIT_MEASURE_SYNC"}
    structural = set(by) == expected and all(x.get("structural_valid") for x in by.values())
    merged = {}
    if structural:
        for stream in expected:
            merged.update(by[stream]["items"])
    required = [
        "A4_spacetime_gravitational_field_variable",
        "A5_gravity_dynamical_principle",
        "B2_spacetime_coordinate_diffeomorphism_law",
        "B3_conserved_source_law",
        "B4_Bianchi_constraint_compatibility",
        "B6_covariant_relativistic_retarded_dynamics",
        "C4_QFT_EFT_baseline_relation",
        "C5_G_to_zero_decoupling_derived",
        "C6_hbar_to_zero_classical_limit_derived",
        "C7_gravitational_quantization_measure_dynamics",
    ]
    ready = bool(structural and all(merged[k]["status"] == "EXPLICIT" for k in required))
    missing = [k for k in required if structural and merged[k]["status"] != "EXPLICIT"]
    proxies = [k for k, v in merged.items() if v.get("status") == "SCOPED_PROXY"]
    stale = [k for k, v in merged.items() if v.get("status") == "STALE"]
    return {
        "iteration": "Iter055",
        "gate": "G57-P",
        "streams_consumed": sorted(by),
        "all_streams_structural_valid": structural,
        "classification": "READY_FOR_FULL_CONSTITUTION_GATE" if ready else "BLOCKED_CONSTITUTION_INPUTS_IDENTIFIED",
        "missing_full_constitution_prerequisites": missing,
        "scoped_proxies": proxies,
        "documentation_sync_findings": stale,
        "programme_readiness_percent": 66,
        "theory_established_percent": 0,
        "scientific_fail": False,
        "readiness_change_allowed": False,
        "scope_lock": "Repository evidence inventory only; no missing physics is synthesized by the audit."
    }


def write(obj, out):
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps(obj, indent=2), encoding="utf-8")
    print(json.dumps(obj, indent=2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stream", choices=["a", "b", "c"])
    ap.add_argument("--aggregate-dir")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    if args.aggregate_dir:
        obj = aggregate(args.aggregate_dir)
        write(obj, args.out)
        if not obj["all_streams_structural_valid"]:
            raise SystemExit(2)
        return
    text, missing = load()
    if args.stream == "a":
        obj = stream_a(text)
    elif args.stream == "b":
        obj = stream_b(text)
    elif args.stream == "c":
        obj = stream_c(text)
    else:
        raise SystemExit("provide --stream or --aggregate-dir")
    obj.update({"iteration": "Iter055", "gate": "G57-P", "missing_evidence_files": missing, "structural_valid": not missing, "readiness_change_allowed": False})
    write(obj, args.out)
    if missing:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
