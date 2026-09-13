#!/usr/bin/env python3
"""Iter046/G50-R: preregistered local-basis covariance audit of terminal G50-A candidates."""
import argparse,json,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import td
from iter043_g50p_four_state_classical_switching_provenance import product_states,apply_map
from iter044_g50c_four_state_switching_calibration import TIMES,HOLDOUT,superops
from iter045_g50a_four_state_switching_adversarial import target_superops

GAP=1e-4; GAP_INV=1e-9; DIRECT=1e-10; TRACE=1e-10; EIG=-1e-10
REF={
(0,'lhs_lsq'):(0.531223338369052,0.44103892972269876,[0.11394120412259612,0.12119914010409205,.14,.14,.14,.14,.14,.14,.14,.14,0.07902733489253805,.14,.55,.55,.55,.55,.55,.55,.55,.55]),
(0,'sobol_lsq'):(0.5312233387405476,0.4410389303302068,[0.1139412015094443,0.12119916197766317,.14,.14,.14,.14,.14,.14,.14,.14,0.0790273364488576,.14,.55,.55,.55,.55,.55,.55,.55,.55]),
(1,'lhs_lsq'):(0.5754531494905043,0.48368432074397105,[0.11275014450331473,0.12230692728610841,.14,.14,.14,.14,.14,.14,.14,.14,0.0787502290842646,.14,.55,.55,.55,.55,.55,.55,.55,.55]),
(1,'sobol_lsq'):(0.5754531507488185,0.4836843219439568,[0.11275014219295282,0.12230693428308032,.14,.14,.14,.14,.14,.14,.14,.14,0.0787502242035436,.14,.55,.55,.55,.55,.55,.55,.55,.55]),
(2,'lhs_lsq'):(0.7457060128507964,0.6597794159553227,[.14,0.08757398430957383,.14,.14,.14,.14,.14,0.07889693479196361,0.13999999670995308,.14,0.07916048757824773,.14,.55,.55,.55,.55,.55,.55,.55,.55]),
(2,'sobol_lsq'):(0.7457060134860737,0.6597794166083825,[.14,0.08757400663008409,.14,.14,.14,.14,.14,0.07889694457931996,.14,.14,0.07916049487561014,.14,.55,.55,.55,.55,.55,.55,.55,.55]),
(3,'lhs_lsq'):(0.8312502929923469,0.8641865593011,[0.1392583261370048,.015,.14,.14,.14,0.05758548970561911,.015,.015,.015,.14,.015,0.0351759251383573,.55,1.4499999999999997,1.354183175443884,.55,.55,1.4499999996132293,1.3570879770389601,0.9062218174003133]),
(3,'sobol_lsq'):(0.8312499916467507,0.8641859248779529,[0.13926508440949834,.015,.14,.14,.14,0.0575893290767447,.015,.015,.015,.14,.015,0.03517508375466066,.55,1.4499999999930828,1.354182968890081,.55,.55,1.4499999999999997,1.357089186738182,0.9061484626811291])}
THETA=[0.025,0.10,0.40,1.40]
PROBES=product_states()

def su2(rng):
 z=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)); q,r=np.linalg.qr(z)
 ph=np.diag(r); ph=np.where(np.abs(ph)>0,ph/np.abs(ph),1); q=q@np.diag(ph.conj())
 q=q/np.sqrt(np.linalg.det(q)); return q

def gap_and_controls(x,theta,times,U):
 S=np.kron(U.conj(),U); Sinv=S.conj().T
 Es=superops(np.asarray(x,float),times); Ts=target_superops(theta,times)
 Er=[S@E@Sinv for E in Es]; Tr=[S@T@Sinv for T in Ts]
 gap=0.; direct=0.; trace=0.; mineig=1.
 for E,T,RE,RT in zip(Es,Ts,Er,Tr):
  for rho in PROBES:
   rr=U@rho@U.conj().T
   eo=apply_map(RE,rr); to=apply_map(RT,rr)
   gap=max(gap,td(eo,to))
   ed=U@apply_map(E,rho)@U.conj().T; tdir=U@apply_map(T,rho)@U.conj().T
   direct=max(direct,td(eo,ed),td(to,tdir))
   trace=max(trace,float(abs(np.trace(eo)-1)),float(abs(np.trace(to)-1)))
   mineig=min(mineig,float(np.min(np.linalg.eigvalsh((eo+eo.conj().T)/2))),float(np.min(np.linalg.eigvalsh((to+to.conj().T)/2))))
 return float(gap),float(direct),float(trace),float(mineig)

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--rotation-seed',type=int,choices=[4601,4602,4603,4604],required=True); ap.add_argument('--shard',type=int,choices=range(4),required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
 rng=np.random.default_rng(a.rotation_seed); UA=su2(rng); UB=su2(rng); U=np.kron(UA,UB)
 methods=[]
 for method in ('lhs_lsq','sobol_lsq'):
  bt,bh,x=REF[(a.shard,method)]
  gt,dt,tt,et=gap_and_controls(x,THETA[a.shard],TIMES,U); gh,dh,th,eh=gap_and_controls(x,THETA[a.shard],HOLDOUT,U)
  rec={'method':method,'canonical_train_gap':bt,'canonical_holdout_gap':bh,'rotated_train_gap':gt,'rotated_holdout_gap':gh,'train_gap_delta':abs(gt-bt),'holdout_gap_delta':abs(gh-bh),'max_direct_discrepancy':max(dt,dh),'max_trace_residual':max(tt,th),'min_output_eigenvalue':min(et,eh)}
  vals=list(rec.values())[1:]; rec['finite']=bool(np.all(np.isfinite(vals))); rec['pass']=bool(rec['finite'] and rec['train_gap_delta']<=GAP_INV and rec['holdout_gap_delta']<=GAP_INV and rec['max_direct_discrepancy']<=DIRECT and rec['max_trace_residual']<=TRACE and rec['min_output_eigenvalue']>=EIG and gt>GAP and gh>GAP)
  methods.append(rec)
 valid=bool(len(methods)==2 and all(m['finite'] for m in methods)); support=bool(valid and all(m['pass'] for m in methods))
 out={'iteration':'Iter046','gate':'G50-R','rotation_seed':a.rotation_seed,'shard':a.shard,'methods':methods,'structural_valid':valid,'lane_support':support,'classification':'G50R_LOCAL_BASIS_COVARIANCE_LANE_PASS' if support else ('G50R_IMPLEMENTATION_OR_NUMERICAL_INVALID' if not valid else 'G50R_FROZEN_ROBUSTNESS_RULE_NOT_MET'),'frozen':{'rotation_seeds':[4601,4602,4603,4604],'gap_invariance_tolerance':GAP_INV,'direct_implementation_tolerance':DIRECT,'trace_tolerance':TRACE,'output_eigenvalue_floor':EIG,'support_gap_floor':GAP,'no_refitting':True,'same_terminal_G50A_candidates':True},'scope_lock':'Local-unitary basis covariance of exact terminal G50-A finite-panel separation only; no family expansion or all-classical no-go.'}
 Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
 if not valid: raise SystemExit(2)
if __name__=='__main__': main()
