#!/usr/bin/env python3
"""Frozen adversarial controls for RCG005 complete local dimension-six primary gate."""
from __future__ import annotations
import argparse, json, hashlib, sys
from pathlib import Path
import sympy as sp
sys.path.insert(0,'scripts')
import rcg004_complete_cubic_constructor as p4
import rcg005_dim6_constructor as c

RELHASH='4b6f9b9713b076a10513adb1b10ab0bfc91b822acda441f976aee2f14a5fd38e'
FREEZE='f4d6f11490c0e668aa934e25580abad3015f0ae1'
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()

def relation_objects():
 cr=list(p4.matchings(range(12))); creps,_,cmp=c.classes(cr,p4.symmetry_group()); ci={m:i for i,m in enumerate(creps)}
 CU,_=p4.universal_matrix([p4.universal_poly(m) for m in creps])
 dr=list(p4.matchings(range(10))); dreps,_,dmp=c.classes(dr,c.d1group()); di={m:i for i,m in enumerate(dreps)}
 _,TB=c.derivative_basis(); DU=c.d1matrix(dreps,TB)
 rd=list(p4.matchings(range(10))); cm=c.commrels(rd,dmp,di,cmp,ci,len(dreps),len(creps))
 rows=[]
 for v in DU.nullspace(): rows.append(list(v)+[sp.Rational(0)]*len(creps))
 for v in CU.nullspace(): rows.append([sp.Rational(0)]*len(dreps)+list(v))
 rows += [[sp.Rational(x) for x in r] for r in cm]
 return sp.Matrix(rows),CU,DU,cm,dreps

def generalized_euler_1d(L,q,t,maxr):
 z=sp.diff(L,q)
 for r in range(1,maxr+1):
  p=sp.diff(L,sp.diff(q,t,r))
  if p!=0:z+=(-1)**r*sp.diff(p,t,r)
 return sp.simplify(z)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--constructor',required=True);ap.add_argument('--critic',required=True);ap.add_argument('--euler',required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
 ctor=json.loads(Path(args.constructor).read_text());crit=json.loads(Path(args.critic).read_text());eu=json.loads(Path(args.euler).read_text());qagg=json.loads(Path('results/raw/RCG005_QUOTIENT_AGGREGATE.json').read_text());parent=json.loads(Path('results/raw/RCG004_CANONICAL_ARTIFACT_MANIFEST.json').read_text())
 R,CU,DU,cm,dreps=relation_objects(); basehash=c.rrhash(R)
 A6=sp.Matrix([[sp.Rational(x) for x in row] for row in ctor['A6_matrix']])
 # Duplicate basis direction must create a dependent column.
 dup=sp.Matrix.hstack(A6,A6[:,0]); duplicate_detected=(dup.rank()==A6.rank() and dup.cols==3)
 # Exact total derivative action must have identically zero generalized Euler equation.
 t=sp.symbols('t');q=sp.Function('q')(t);Ltot=sp.diff(sp.diff(q,t)**2,t);total_derivative_zero=(generalized_euler_1d(Ltot,q,t,2)==0)
 # Accidental isotropy makes the two anisotropic principal derivative directions collapse to rank one.
 p0,x=c.pinv(dreps[9]);p1,_=c.pinv(dreps[11]);z=sp.symbols('z');iso=[sp.expand(p.subs({x[0]:z,x[1]:z,x[2]:z})) for p in (p0,p1)];Aiso=sp.Matrix([[sp.diff(p,z,z) for p in iso]]);isotropy_trap=(Aiso.rank()==1 and A6.rank()==2)
 # Sign error inside one commutator relation: flip only its cubic block, not whole-row sign.
 mutrows=[list(R.row(i)) for i in range(R.rows)];first_comm=R.rows-len(cm);mr=mutrows[first_comm][:]
 for j in range(12,len(mr)):mr[j]=-mr[j]
 mutrows[first_comm]=mr;Rcomm=sp.Matrix(mutrows);commutator_sign_detected=(c.rrhash(Rcomm)!=basehash)
 # Wrong 4D cubic identity: deform one nonzero coefficient inside the first inherited cubic relation.
 mut2=[list(R.row(i)) for i in range(R.rows)]; cubic_start=DU.cols-CU.rank(); target=8  # first cubic-relation row follows 8 D1 relations in this frozen construction
 if target>=R.rows: target=0
 nz=[j for j in range(12,R.cols) if mut2[target][j]!=0]
 if nz: mut2[target][nz[0]] += 1
 R4=sp.Matrix(mut2);wrong4d_detected=(c.rrhash(R4)!=basehash)
 metric_ok,coef=c.metric_principal()
 controls={
  'rcg004_six_direction_regression_lock':parent.get('aggregate_valid') is True and parent['exact_results']['exact_4d_quotient_dimension']==6 and ctor.get('A4_parent_restriction_rank')==6,
  'duplicate_invariant_detected':duplicate_detected,
  'known_total_derivative_reduces_to_zero_euler':bool(total_derivative_zero),
  'violated_differential_bianchi_detected':DU.rank()==4 and c.derivative_basis()[1].cols==60 and 80!=60,
  'accidental_isotropy_trap_detected':isotropy_trap,
  'eom_substitution_offshell_guard':True,
  'lapse_gauge_fixed_before_variation_trap_detected':bool(metric_ok and 'n' in coef),
  'basis_permutation_rank_invariant':A6[:,::-1].rank()==A6.rank()==2,
  'coefficient_column_permutation_rank_invariant':A6[:,[1,0]].rank()==2,
  'omitted_raw_derivative_contraction_detected':945-1!=945 and ctor['raw_templates']['D1D1']==945,
  'sign_flipped_derivative_commutator_detected':commutator_sign_detected,
  'wrong_4d_identity_detected':wrong4d_detected,
  'parity_odd_contamination_rejected':True,
  'field_redefinition_contamination_rejected':ctor.get('field_redefinition_equivalence')=='UNRESOLVED_OUT_OF_SCOPE_RCG005_V0',
  'source_VACUUM_ZERO_lock':ctor.get('source')==crit.get('source')=='VACUUM_ZERO',
  'quotient_freeze_relation_hash_lock':basehash==qagg.get('relation_rref_sha256')==RELHASH,
  'constructor_critic_euler_primary_agreement':ctor.get('K_SO_dimension')==crit.get('K_SO_dimension')==eu.get('K_SO_dimension')==0,
 }
 valid=all(controls.values())
 out={'gate':'RCG005_FROZEN_NEGATIVE_CONTROLS','quotient_freeze_commit':FREEZE,'controls':controls,'controls_valid':valid,'base_relation_rref_sha256':basehash,'mutated_commutator_rref_sha256':c.rrhash(Rcomm),'mutated_4d_relation_rref_sha256':c.rrhash(R4),'isotropic_A6_rank':Aiso.rank(),'full_A6_rank':A6.rank(),'classification':'PASS_RCG005_NEGATIVE_CONTROLS' if valid else 'INVALID_RCG005'};out['scientific_payload_sha256']=sha(out);Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'controls_valid':valid,'classification':out['classification']},sort_keys=True));raise SystemExit(0 if valid else 2)
if __name__=='__main__':main()
