#!/usr/bin/env python3
"""Aggregate constructor and independent Critic without changing frozen classifier."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ALLOWED = {
    "PASS_SCOPED_RCG003_CONFORMAL_SECOND_ORDER_NONZERO_DEFORMATION_EXISTS",
    "FAIL_SCOPED_RCG003_CONFORMAL_SECOND_ORDER_NONZERO_DEFORMATION_EXCLUDED",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--constructor", required=True)
    ap.add_argument("--critic", required=True)
    ap.add_argument("--output", required=True)
    a = ap.parse_args()
    cp, rp = Path(a.constructor), Path(a.critic)
    c = json.loads(cp.read_text(encoding="utf-8"))
    r = json.loads(rp.read_text(encoding="utf-8"))

    checks = {
        "constructor_controls_pass": bool(c.get("all_controls_pass")),
        "formation_valid": bool(c.get("formation", {}).get("valid_for_gate")),
        "constructor_classification_frozen": c.get("classification") in ALLOWED,
        "critic_pass": bool(r.get("critic_pass")),
        "prereg_commit_match": c.get("prereg_commit") == "0bba0ea6e1d4e13635f70f3b5056e131afba6c7d",
    }
    valid = all(checks.values())
    classification = c.get("classification") if valid else "INVALID_RCG003_AGGREGATE_OR_CRITIC_FAILURE"

    out = {
        "schema": "RCG003_TERMINAL_AGGREGATE_V1",
        "checks": checks,
        "valid": valid,
        "classification": classification,
        "formation_side_classification": c.get("formation", {}).get("side_classification"),
        "raw_dimension": c.get("compatibility", {}).get("rank") is not None and c.get("family", {}).get("raw_dimension"),
        "closure_rank": c.get("compatibility", {}).get("rank"),
        "residual_dimension": c.get("compatibility", {}).get("residual_dimension"),
        "nullspace_primitive_integer": c.get("compatibility", {}).get("nullspace_primitive_integer"),
        "critic_classification": r.get("classification"),
        "constructor_sha256": digest(cp),
        "critic_sha256": digest(rp),
        "chi_ABC": "UNAUTHORIZED_NOT_COMPUTED",
        "theory_established_percent": 0,
        "claim_ceiling": "classical vacuum conformal structural result inside frozen bounded RCG003-v0 family only",
    }
    p = Path(a.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
