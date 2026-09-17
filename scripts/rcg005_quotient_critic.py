#!/usr/bin/env python3
"""Independent preprimary quotient-only Critic. Computes no derivative-order survivor."""
import argparse,json,sys
from pathlib import Path
import sympy as sp
sys.path.insert(0,'scripts')
import rcg005_dim6_critic as q

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args()
 cr=list(q.pairings(range(12)));creps,cz,cmp=q.classes(cr,q.cgroup());ci={m:i for i,m in enumerate(creps)};CM=q.pmat([q.cpoly(m) for m in creps]);cn=CM.nullspace()
 dr=list(q.pairings(range(10)));dreps,dz,dmp=q.classes(dr,q.dgroup());di={m:i for i,m in enumerate(dreps)};DM=q.pmat([q.dpoly(m) for m in dreps]);dn=DM.nullspace();cm=q.comm(dr,dmp,di,cmp,ci,len(dreps),len(creps));rows=[]
 for v in dn:rows.append(list(v)+[sp.Rational(0)]*len(creps))
 for v in cn:rows.append([sp.Rational(0)]*len(dreps)+list(v))
 rows += [[sp.Rational(x) for x in r] for r in cm];R=sp.Matrix(rows);qdim=R.cols-R.rank();parent=json.loads(Path('results/raw/RCG004_CANONICAL_ARTIFACT_MANIFEST.json').read_text());parentok=parent.get('aggregate_valid') is True and parent['exact_results']['constructor_primary_hessian_rank']==6
 valid=all([len(cr)==10395,len(creps)==13,CM.rank()==6,len(q.HID)==200,len(dr)==945,len(dreps)==12,DM.rank()==4,len(cm)==3,sp.Matrix(cm).rank()==3,R.rank()==17,qdim==8,parentok])
 out={'phase':'RCG005_PREPRIMARY_QUOTIENT_ONLY_INDEPENDENT_CRITIC','run_head':a.run_head,'prereg_sha':q.PREREG,'heldout_prereg_sha':q.HELDOUT,'method':'REVERSE_PAIRINGS_SELFDUAL_CUBIC_NORMAL_COORDINATE_200_METRIC_THIRD_JETS','constructor_not_imported':True,'raw_counts':{'cubic':len(cr),'D1D1':len(dr)},'class_counts':{'cubic_nonzero':len(creps),'D1D1_nonzero':len(dreps)},'cubic_rank':CM.rank(),'normal_coordinate_metric_third_jet_variables':len(q.HID),'D1D1_pointwise_rank':DM.rank(),'commutator_relation_count':len(cm),'relation_rank':R.rank(),'relation_rref_sha256':q.rrhash(R),'quotient_dimension':qdim,'independent_basis_policy':'RELATION_RREF_FREE_REPRESENTATIVES_NOT_CONSTRUCTOR_LABEL_PROOF','rcg004_parent_lock':parentok,'no_primary_dynamics_computed':True,'valid':valid,'classification':'PASS_INDEPENDENT_CRITIC_RCG005_PREPRIMARY_EXACT_QUOTIENT' if valid else 'INVALID_RCG005'};out['scientific_payload_sha256']=q.sha(out);Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'quotient_dimension':qdim,'relation_rank':R.rank(),'valid':valid,'classification':out['classification']},sort_keys=True))
if __name__=='__main__':main()
