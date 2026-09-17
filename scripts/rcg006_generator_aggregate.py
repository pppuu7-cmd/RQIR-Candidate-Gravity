#!/usr/bin/env python3
"""Frozen pre-map aggregate for RCG006 generator completeness only."""
import argparse,hashlib,json
from pathlib import Path

def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--constructor',required=True);p.add_argument('--critic',required=True);p.add_argument('--output',required=True);p.add_argument('--run-head',default='');a=p.parse_args()
 c=json.loads(Path(a.constructor).read_text());k=json.loads(Path(a.critic).read_text())
 pred={
  'constructor_pass':c.get('classification')=='PASS_RCG006_GENERATOR_COMPLETENESS_READY_TO_FREEZE',
  'critic_pass':k.get('classification')=='PASS_INDEPENDENT_CRITIC_RCG006_GENERATOR_COMPLETENESS',
  'raw_counts_agree':c.get('raw_counts')==k.get('raw_counts'),
  'ALG_dimension_agree':c.get('ALG_generator_dimension')==k.get('ALG_generator_dimension'),
  'DER_dimension_agree':c.get('DER_new_principal_dimension')==k.get('DER_new_principal_dimension'),
  'total_dimension_agree':c.get('generator_dimension_M')==k.get('generator_dimension_M'),
  'commutator_completion_both':c.get('commutator_completion_all_in_ALG_span') is True and k.get('commutator_completion_all_in_ALG_span') is True,
  'constructor_no_map':c.get('no_M_FR_computed') is True,
  'critic_no_map':k.get('no_M_FR_computed') is True,
  'prereg_exact':c.get('scientific_prereg')=='fc3ff1f49c56f2befc039e09ebd8f388833dbff1' and k.get('scientific_prereg')=='fc3ff1f49c56f2befc039e09ebd8f388833dbff1',
  'heldout_exact':c.get('heldout_prereg')=='43748579a78f40e0825d5ae01dc634d55ba7b928' and k.get('heldout_prereg')=='43748579a78f40e0825d5ae01dc634d55ba7b928',
  'run_head_agree':c.get('run_head')==a.run_head and k.get('run_head')==a.run_head,
 }
 valid=all(pred.values())
 out={'phase':'RCG006_GENERATOR_COMPLETENESS_PREMAP_AGGREGATE','run_head':a.run_head,'aggregate_valid':valid,'predicates':pred,'raw_counts':c.get('raw_counts'),'ALG_generator_dimension':c.get('ALG_generator_dimension'),'DER_new_principal_dimension':c.get('DER_new_principal_dimension'),'generator_dimension_M':c.get('generator_dimension_M'),'constructor_basis':c.get('deterministic_generator_basis'),'constructor_payload_sha256':c.get('scientific_payload_sha256'),'critic_payload_sha256':k.get('scientific_payload_sha256'),'M_FR_status':'NOT_COMPUTED_PREMAP','classification':'PASS_RCG006_GENERATOR_COMPLETENESS_READY_TO_FREEZE' if valid else 'INVALID_RCG006_GENERATOR_COMPLETENESS_AGGREGATE','claim_locks':{'chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%','RCG005_reclassified':False}}
 out['scientific_payload_sha256']=sha(out);Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'aggregate_valid':valid,'generator_dimension_M':out['generator_dimension_M'],'classification':out['classification']},sort_keys=True))
if __name__=='__main__':main()
