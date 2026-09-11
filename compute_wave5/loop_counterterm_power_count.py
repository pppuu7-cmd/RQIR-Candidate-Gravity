#!/usr/bin/env python3
import json
from pathlib import Path

OUT=Path("wave5_results"); OUT.mkdir(exist_ok=True)

# Standard EFT power-counting control for pure Einstein gravity:
# each loop raises the schematic local counterterm derivative order to 2L+2.
# This does not state that every candidate counterterm is nonzero on shell.
# In 4D pure gravity the one-loop on-shell divergence has special cancellations,
# while a genuine two-loop Riemann^3-type divergence is known (Goroff-Sagnotti).
# Purpose: tree constructibility does not by itself imply quantum/loop closure.

records=[]
for L in range(0,8):
    derivative_order=2*L+2
    curvature_power_proxy=L+1
    records.append({
        "loop_order":L,
        "schematic_counterterm_derivative_order":derivative_order,
        "schematic_curvature_power":curvature_power_proxy,
        "tree_level":L==0,
        "known_special_note": (
            "Einstein-Hilbert/tree layer" if L==0 else
            "4D pure-gravity one-loop on-shell cancellations; matter/off-shell terms can require curvature-squared EFT counterterms" if L==1 else
            "4D pure-gravity two-loop divergence includes curvature-cubic/Riemann^3 structure" if L==2 else
            "higher-loop EFT layer; detailed independent basis not computed here"
        )
    })

summary={
 "test":"loop-order versus local EFT counterterm derivative layer",
 "formula":"schematic derivative order = 2L+2 for Einstein-gravity power counting",
 "records":records,
 "result":"Even if the tree S-matrix is fixed by constructibility, loop renormalization opens higher-derivative EFT layers. Tree constructibility is therefore not a UV-completion principle.",
 "scope":"power-counting bookkeeping; not an explicit loop amplitude calculation"
}
(OUT/"loop_counterterm_power_count.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
