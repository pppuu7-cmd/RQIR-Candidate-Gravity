#!/usr/bin/env python3
"""Frozen RCG003B aggregate: Constructor + independent Critic + EL cross-check."""
from __future__ import annotations
import argparse, hashlib, json, platform, sys
from pathlib import Path

PASS="PASS_SCOPED_RCG003B_AXISYMMETRIC_SECOND_ORDER_DERIVATIVE_CLOSURE"
FAIL="FAIL_SCOPED_RCG003B_AXISYMMETRIC_HIGHER_DERIVATIVE_SURVIVOR_FALSIFIED"
INVALID="INVALID_RCG003B"

def load(p): return json.loads(Path(p).read_text())

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--constructor",required=True); ap.add_argument("--critic",required=True)
    ap.add_argument("--euler",required=True); ap.add_argument("--output",required=True)
    ap.add_argument("--prereg-sha",required=True); ap.add_argument("--parent-terminal",required=True)
    ap.add_argument("--run-head",required=True)
    args=ap.parse_args()
    c=load(args.constructor); k=load(args.critic); e=load(args.euler)

    checks={
      "prereg_all_exact": all(x.get("prereg_sha")==args.prereg_sha for x in (c,k,e)),
      "parent_terminal_all_exact": all(x.get("parent_terminal")==args.parent_terminal for x in (c,k,e)),
      "run_head_all_exact": all(x.get("run_head")==args.run_head for x in (c,k,e)),
      "fixed_ray_all_exact": all(x.get("production_ray")==[7,-36,36] for x in (c,k,e)),
      "constructor_controls_valid": c.get("controls_valid") is True,
      "critic_controls_valid": k.get("controls_valid") is True,
      "critic_provenance_pass": k.get("critic_classification")=="PASS_INDEPENDENT_CRITIC_RCG003B_SCOPE_AND_PROVENANCE",
      "constructor_critic_hessian_exact_match": c.get("hessian_normalized_by_exp_a_plus_2b")==k.get("hessian_normalized_by_exp_a_plus_2b"),
      "euler_hessian_correspondence": e.get("fourth_hessian_correspondence") is True,
      "lane_classifications_agree": len({c.get("classification"),k.get("classification"),e.get("classification")})==1,
      "classification_allowed": c.get("classification") in {PASS,FAIL},
      "source_lock": c.get("source")=="VACUUM_ZERO" and k.get("source")=="VACUUM_ZERO",
    }
    valid=all(checks.values())
    terminal=c.get("classification") if valid else INVALID
    residual=1 if terminal==PASS else (0 if terminal==FAIL else None)

    payload={
      "gate":"RCG003B_AXISYMMETRIC_BIANCHI_I_DERIVATIVE_CLOSURE",
      "prereg_sha":args.prereg_sha,
      "parent_terminal":args.parent_terminal,
      "run_head":args.run_head,
      "aggregate_valid":valid,
      "checks":checks,
      "constructor_scientific_payload_sha256":c.get("scientific_payload_sha256"),
      "critic_scientific_payload_sha256":k.get("scientific_payload_sha256"),
      "euler_scientific_payload_sha256":e.get("scientific_payload_sha256"),
      "constructor_symbolic_sha256":c.get("symbolic_sha256"),
      "critic_symbolic_sha256":k.get("symbolic_sha256"),
      "euler_symbolic_sha256":e.get("symbolic_sha256"),
      "exact_hessian_normalized":c.get("hessian_normalized_by_exp_a_plus_2b"),
      "constructor_witness":c.get("minimal_exact_obstruction"),
      "critic_witness":k.get("minimal_exact_obstruction"),
      "euler_witness":e.get("minimal_exact_obstruction"),
      "input_nonzero_ray_dimension":1,
      "residual_nonzero_ray_dimension":residual,
      "classification":terminal,
      "critic_classification":k.get("critic_classification"),
      "environment":{"python":sys.version.split()[0],"platform":platform.platform()},
      "claim_locks":{
        "theory_established":"0%",
        "chi_ABC":"UNAUTHORIZED_NOT_COMPUTED",
        "arbitrary_nonlinear_gravity_no_go":False,
        "full_constraint_closure":False,
        "hyperbolicity":False,
        "quantum_gravity":False,
        "new_physics":False
      }
    }
    payload["scientific_payload_sha256"]=hashlib.sha256(
        json.dumps(payload,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    Path(args.output).write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"valid":valid,"classification":terminal,"residual_nonzero_ray_dimension":residual},sort_keys=True))
    if not valid:
        raise SystemExit(2)

if __name__=="__main__": main()
