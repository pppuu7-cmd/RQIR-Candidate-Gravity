#!/usr/bin/env python3
"""Preprimary quotient-only Constructor. Deliberately computes no derivative-order nullspace."""
import argparse,json,sys
from pathlib import Path
import sympy as sp
sys.path.insert(0,'scripts')
import rcg004_complete_cubic_constructor as p4
import rcg005_dim6_constructor as c

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args()
 cr=list(p4.matchings(range(12)));creps,cz,cmp=c.classes(cr,p4.symmetry_group());ci={m:i for i,m in enumerate(creps)};CU,_=p4.universal_matrix([p4.universal_poly(m) for m in creps]);_,cp=CU.rref()
 dr=list(p4.matchings(range(10)));dreps,dz,dmp=c.classes(dr,c.d1group());di={m:i for i,m in enumerate(dreps)};DB,TB=c.derivative_basis();DU=c.d1matrix(dreps,TB)
 rd=list(p4.matchings(range(10)));rr,rz,_=c.classes(rd,c.rd2group());d4=list(p4.matchings(range(8)));fr,fz,_=c.classes(d4,c.d4group());cm=c.commrels(rd,dmp,di,cmp,ci,len(dreps),len(creps));rows=[]
 for v in DU.nullspace():rows.append(list(v)+[sp.Rational(0)]*len(creps))
 for v in CU.nullspace():rows.append([sp.Rational(0)]*len(dreps)+list(v))
 rows += [[sp.Rational(x) for x in r] for r in cm];R=sp.Matrix(rows);qdim=R.cols-R.rank();chosen=[9,11]+[len(dreps)+i for i in c.PARENT_BASIS];aug=sp.Matrix.vstack(R,*[sp.Matrix([[1 if j==i else 0 for j in range(R.cols)]]) for i in chosen]);parent=json.loads(Path('results/raw/RCG004_CANONICAL_ARTIFACT_MANIFEST.json').read_text());parentok=parent.get('aggregate_valid') is True and parent['exact_results']['constructor_basis_class_indices']==c.PARENT_BASIS
 valid=all([len(cr)==10395,len(dr)==945,len(rd)==945,len(d4)==105,len(creps)==13,len(dreps)==12,len(rr)==14,len(fr)==12,TB.cols==60,DU.rank()==4,len(cm)==3,sp.Matrix(cm).rank()==3,R.rank()==17,qdim==8,list(cp)==c.PARENT_BASIS,aug.rank()==R.cols,parentok])
 out={'phase':'RCG005_PREPRIMARY_QUOTIENT_ONLY','run_head':a.run_head,'prereg_sha':c.PREREG,'heldout_prereg_sha':c.HELDOUT,'raw_counts':{'cubic':len(cr),'D1D1':len(dr),'RD2':len(rd),'D4':len(d4),'total':len(cr)+len(dr)+len(rd)+len(d4)},'class_counts':{'cubic_nonzero':len(creps),'cubic_zero':len(cz),'D1D1_nonzero':len(dreps),'D1D1_zero':len(dz),'RD2_nonzero':len(rr),'RD2_zero':len(rz),'D4_nonzero':len(fr),'D4_zero':len(fz)},'generic_dR_dimension':TB.cols,'D1D1_pointwise_rank':DU.rank(),'commutator_relation_count':len(cm),'relation_rank':R.rank(),'relation_rref_sha256':c.rrhash(R),'quotient_dimension':qdim,'frozen_basis_candidate':{'new_derivative_D1D1_class_indices':[9,11],'inherited_RCG004_class_indices':c.PARENT_BASIS},'rcg004_embedding_rank':6 if aug.rank()==R.cols else 0,'no_primary_dynamics_computed':True,'valid':valid,'classification':'PASS_RCG005_PREPRIMARY_EXACT_QUOTIENT_COMPLETENESS' if valid else 'INVALID_RCG005'};out['scientific_payload_sha256']=c.sha(out);Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'quotient_dimension':qdim,'relation_rank':R.rank(),'valid':valid,'classification':out['classification']},sort_keys=True))
if __name__=='__main__':main()
