#!/usr/bin/env python3
import json
from pathlib import Path

root = Path("downloaded_results")
items = {}
for path in root.rglob("*.json"):
    if path.name == "campaign_summary.json":
        continue
    try:
        items[path.stem] = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        items[path.stem] = {"parse_error": str(exc), "path": str(path)}

required = {"channel_polytope", "spectral_moment_problem", "cumulant_hierarchy", "crossing_eft_basis"}
missing = sorted(required - set(items))

signals = {}
if "channel_polytope" in items:
    rs = items["channel_polytope"].get("results", [])
    signals["channel_nonunique_nontrivial_eta"] = any((not r.get("unique_at_tolerance_1e-9", True)) for r in rs if r.get("eta", 1.0) < 1.0)
if "spectral_moment_problem" in items:
    rs = items["spectral_moment_problem"].get("records", [])
    signals["spectral_finite_moments_nonunique"] = any((not r.get("unique_at_tolerance_1e-10", True)) for r in rs)
if "cumulant_hierarchy" in items:
    d = items["cumulant_hierarchy"]
    signals["L4_not_closed"] = d.get("L4", {}).get("kappa4_width", 0.0) > 1e-9
    signals["L6_not_closed_after_L4"] = d.get("L6_given_E4_3", {}).get("kappa6_width", 0.0) > 1e-9
if "crossing_eft_basis" in items:
    rs = items["crossing_eft_basis"].get("records", [])
    signals["crossing_higher_order_freedom_grows"] = bool(rs) and rs[-1].get("free_after_fixing_sigma2", 0) > rs[0].get("free_after_fixing_sigma2", 0)
    signals["forward_blind_sector_exists"] = any(r.get("forward_invisible_free", 0) > 0 for r in rs)

summary = {
    "campaign": "post-freeze-parallel-compute-v1",
    "required_artifacts": sorted(required),
    "missing": missing,
    "signals": signals,
    "all_required_present": not missing,
    "all_tested_closure_proxies_show_residual_freedom": bool(signals) and all(signals.values()),
    "scientific_scope": "finite/proxy uniqueness tests; they can falsify naive closure claims but do not prove a quantum-gravity no-go",
}

Path("campaign_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
lines = [
    "# Post-freeze parallel compute campaign summary",
    "",
    f"Artifacts complete: **{not missing}**",
    "",
]
for k, v in signals.items():
    lines.append(f"- `{k}`: **{v}**")
lines += [
    "",
    f"All tested finite closure proxies show residual freedom: **{summary['all_tested_closure_proxies_show_residual_freedom']}**",
    "",
    "Scope warning: these are finite/proxy counterexample searches. They strengthen or falsify candidate closure principles; they are not by themselves a theorem about full quantum gravity.",
]
Path("campaign_summary.md").write_text("\n".join(lines), encoding="utf-8")
print(json.dumps(summary, indent=2))
if missing:
    raise SystemExit(2)
