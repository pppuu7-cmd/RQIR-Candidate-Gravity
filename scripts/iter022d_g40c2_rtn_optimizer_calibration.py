#!/usr/bin/env python3
"""Iter022D / G40-C2: corrected positive-control optimizer calibration.

Authorized only after G40-C2-E terminal eligibility PASS.  The optimizer,
family bounds, probe states, time grid and thresholds are identical to G40-C.
Controls 0/1/2 are unchanged; control 3 is the new preregistered strict-BLP
eligible target certified by G40-C2-E.  No RCG-002 target is used.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter022b_g40c_rtn_optimizer_calibration import METHODS,TIMES,PROBES,RECOVERY_TOL,BACKFLOW_MIN,trajectory,optimize,blp_u
from iter022c_g40c2_control_eligibility import CONTROLS_C2


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--method',choices=METHODS,required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    hidden=CONTROLS_C2[a.shard]; target_traj=trajectory(hidden); gap,rn,nfev,ok,u=optimize(a.method,a.shard,target_traj); backflow=blp_u(u)
    structural=bool(np.all(np.isfinite([gap,rn,backflow])))
    support=bool(structural and gap<RECOVERY_TOL and backflow>BACKFLOW_MIN)
    out={'iteration':'Iter022D','gate':'G40-C2','method':a.method,'shard':a.shard,'best_max_trace_gap':gap,'residual_norm':rn,'nfev':nfev,'optimizer_success_flag':ok,'recovered_BLP_total_positive_increment':backflow,'structural_valid':structural,'scientific_support':support,
         'frozen':{'times':TIMES.tolist(),'n_probes':len(PROBES),'recovery_tolerance':RECOVERY_TOL,'BLP_backflow_min':BACKFLOW_MIN,'optimizer_and_bounds_identical_to_G40C':True,'controls_0_1_2_unchanged':True,'control_3_prevalidated_by_G40C2E':True,'hidden_control_never_used_as_start':True},
         'scope_lock':'Finite symmetric hidden-classical RTN with arbitrary local Pauli axes; same G40-C family and optimizer.',
         'interpretation':'Corrected positive-control optimizer calibration only. PASS may authorize a separate RCG-002 adversarial trajectory gate; no novelty inference here.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not structural: raise SystemExit(2)
if __name__=='__main__': main()
