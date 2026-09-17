#!/usr/bin/env python3
"""Frozen aggregate classifier for RCG005 complete local dimension-six primary gate."""
import argparse, hashlib, json
from pathlib import Path

FREEZE='f4d6f11490c0e668aa934e25580abad3015f0ae1'
PREREG='1ac1c032dcbbd8e3f0a527a470acc0a44ddffa08'
HELDOUT='1fb26a399264747fc2ffa8a564d4d281c0586f9c'
RELHASH='4b6f9b9713b076a10513adb1b10ab0bfc91b822acda441f976aee2f14a5fd38e'
FAIL='FAIL_SCOPED_RCG005_COMPLETE_LOCAL_DIM6_PURE_METRIC_CLASS_HAS_NO_NONZERO_SECOND_ORDER_SURVIVOR'
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--constructor',required=True);ap.add_argument('--critic',required=True);ap.add_argument('--euler',required=True);ap.add_argument('--controls',required=True);ap.add_argument('--output',required=True);ap.add_argument('--run-head',required=True);a=ap.parse_args()
 c=json.loads(Path(a.constructor).read_text());k=json.loads(Path(a.critic).read_text());e=json.loads(Path(a.euler).read_text());n=json.loads(Path(a.controls).read_text());q=json.loads(Path('results/raw/RCG005_QUOTIENT_AGGREGATE.json').read_text())
 pred={
  'preprimary_quotient_frozen_valid':q.get('aggregate_valid') is True and q.get('quotient_dimension')==8 and q.get('relation_rank')==17 and q.get('relation_rref_sha256')==RELHASH,
  'constructor_controls_valid':c.get('controls_valid') is True,
  'critic_controls_valid':k.get('controls_valid') is True,
  'direct_euler_valid':e.get('valid') is True,
  'negative_controls_valid':n.get('controls_valid') is True,
  'prereg_exact':c.get('prereg_sha')==k.get('prereg_sha')==PREREG,
  'heldout_frozen_exact':c.get('heldout_prereg_sha')==k.get('heldout_prereg_sha')==HELDOUT,
  'run_head_exact':c.get('run_head')==k.get('run_head')==e.get('run_head')==a.run_head,
  'quotient_dimension_eight':c.get('quotient_dimension')==k.get('quotient_dimension')==8,
  'relation_span_lock':c.get('relation_rref_sha256')==k.get('relation_rref_sha256')==RELHASH,
  'frozen_basis_exact':c.get('quotient_basis')=={'D1D1':[9,11],'RCG004':[0,1,2,4,5,8]},
  'rcg004_embedding_rank_six':c.get('rcg004_embedding_rank')==6,
  'constructor_A6_rank_two':c.get('A6_rank')==2,
  'critic_A6_rank_two':k.get('A6_rank')==2,
  'direct_euler_A6_rank_two':e.get('A6_rank')==2,
  'K6_exact_six':c.get('K6_dimension')==k.get('K6_dimension')==e.get('K6_dimension')==6,
  'A5_restricted_zero':c.get('A5_restricted_rank')==e.get('A5_restricted_rank')==0,
  'inherited_A4_rank_six':c.get('A4_parent_restriction_rank')==k.get('parent_A4_restriction_rank')==e.get('A4_parent_direct_euler_restriction_rank')==6,
  'final_K_SO_zero':c.get('K_SO_dimension')==k.get('K_SO_dimension')==e.get('K_SO_dimension')==0,
  'mechanism_branch_A':c.get('mechanism_branch')=='A_DERIVATIVE_SECTOR_HAS_NO_NONZERO_HIGHEST_ORDER_DEGENERATE_COMBINATION',
  'heldout_not_applicable_only_primary_zero':c.get('heldout_status')=='NOT_APPLICABLE_PRIMARY_NULLITY_ZERO' and c.get('K_SO_dimension')==0,
  'source_lock':c.get('source')==k.get('source')=='VACUUM_ZERO',
  'field_redefinition_firewall':c.get('field_redefinition_equivalence')=='UNRESOLVED_OUT_OF_SCOPE_RCG005_V0',
  'constructor_scoped_fail':c.get('classification')==FAIL,
  'critic_independent_pass':k.get('classification')=='PASS_INDEPENDENT_CRITIC_RCG005_QUOTIENT_AND_PRIMARY_NULLITY_ZERO',
  'euler_independent_pass':e.get('classification')=='PASS_RCG005_DIRECT_EL_CONFIRMS_PRIMARY_NULLITY_ZERO',
 }
 valid=all(pred.values());classification=FAIL if valid else 'INVALID_RCG005'
 out={'gate':'RCG005_COMPLETE_LOCAL_DIM6_PURE_METRIC_TERMINAL_AGGREGATE','run_head':a.run_head,'quotient_freeze_commit':FREEZE,'predicates':pred,'aggregate_valid':valid,'classification':classification,'mechanism_branch':c.get('mechanism_branch'),'dimension_chain':{'raw_templates_total':c.get('raw_templates',{}).get('total'),'exact_quotient_dimension':c.get('quotient_dimension'),'highest_order_A6_rank':c.get('A6_rank'),'K6_dimension':c.get('K6_dimension'),'K5_dimension':c.get('K5_dimension'),'K4_dimension':c.get('K4_dimension'),'K_SO_dimension':c.get('K_SO_dimension'),'heldout_survivor_dimension':0 if c.get('K_SO_dimension')==0 else None},'heldout_status':c.get('heldout_status'),'constructor_payload_sha256':c.get('scientific_payload_sha256'),'critic_payload_sha256':k.get('scientific_payload_sha256'),'euler_payload_sha256':e.get('scientific_payload_sha256'),'controls_payload_sha256':n.get('scientific_payload_sha256'),'claim_locks':{'chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%','GR_unique':False,'all_higher_curvature_gravity_fails':False,'ghost_free':False,'stable':False,'hyperbolic':False,'unitary':False,'quantum_gravity':False,'new_physics':False}}
 out['scientific_payload_sha256']=sha(out);Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'aggregate_valid':valid,'classification':classification,'dimension_chain':out['dimension_chain']},sort_keys=True));raise SystemExit(0 if valid else 2)
if __name__=='__main__':main()
