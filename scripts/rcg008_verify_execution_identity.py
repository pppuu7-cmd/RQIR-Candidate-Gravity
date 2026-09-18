#!/usr/bin/env python3
import json, pathlib, subprocess, sys
p=pathlib.Path("prereg/RCG008_EXECUTION_IDENTITY_FREEZE.json")
if not p.exists(): raise SystemExit("missing execution identity freeze")
f=json.loads(p.read_text())
parent=subprocess.check_output(["git","rev-parse","HEAD^"],text=True).strip()
if parent!=f["implementation_commit"]: raise SystemExit(f"implementation parent mismatch {parent} != {f['implementation_commit']}")
for path,sha in sorted(f["implementation_blobs"].items()):
    got=subprocess.check_output(["git","rev-parse",f"HEAD:{path}"],text=True).strip()
    if got!=sha: raise SystemExit(f"implementation blob mismatch {path}: {got} != {sha}")
print("RCG008_EXECUTION_IDENTITY_OK")
