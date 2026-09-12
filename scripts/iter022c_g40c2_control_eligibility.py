#!/usr/bin/env python3
"""Iter022C / G40-C2-E: prospective eligibility audit for hidden controls.

The original G40-C is retained as a protocol-design failure because frozen
control shard 3 was not inside the declared strict-BLP subset.  This separate
gate keeps the first three controls unchanged and replaces only shard 3 with a
new preregistered control.  No optimizer is run here.  Every target must be
inside the frozen parameter box and must itself satisfy BLP > 0.02 before any
new calibration run is authorized.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter022b_g40c_rtn_optimizer_calibration import LO,HI,blp_u

BACKFLOW_MIN=0.02
CONTROLS_C2=np.array([
 [0.31,1.08,0.92,0.61,0.44*np.pi, 0.35,0.62*np.pi,-0.70],
 [0.47,0.88,1.16,0.52,0.67*np.pi,-1.05,0.38*np.pi, 0.91],
 [0.24,1.27,0.78,1.03,0.29*np.pi, 1.34,0.73*np.pi,-1.42],
 [0.35,1.15,1.15,0.82,0.40*np.pi,-2.00,0.52*np.pi, 2.00],
],float)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    p=CONTROLS_C2[a.shard]; in_bounds=bool(np.all(p>=LO) and np.all(p<=HI)); u=(p-LO)/(HI-LO); b=float(blp_u(u)); structural=bool(np.isfinite(b)); support=bool(structural and in_bounds and b>BACKFLOW_MIN)
    out={'iteration':'Iter022C','gate':'G40-C2-E','shard':a.shard,'target_BLP_total_positive_increment':b,'inside_frozen_bounds':in_bounds,'structural_valid':structural,'scientific_support':support,
         'frozen':{'BLP_backflow_min':BACKFLOW_MIN,'same_family_bounds_as_G40C':True,'shards_0_1_2_unchanged_from_G40C':True,'shard_3_is_new_preregistered_control':True},
         'interpretation':'Eligibility only. PASS authorizes a separate new G40-C2 optimizer calibration; it is not calibration or adversarial evidence.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
