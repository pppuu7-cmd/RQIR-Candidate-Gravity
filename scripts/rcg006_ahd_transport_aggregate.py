#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def sha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--constructor',required=True);ap.add_argument('--critic',required=True);ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args()
    c=json.loads(Path(a.constructor).read_text());k=json.loads(Path(a.critic).read_text())
    checks={
      'constructor_valid':c.get('constructor_valid') is True,
      'critic_valid':k.get('critic_valid') is True,
      'A_HD_rank':c.get('A_HD_rank')==k.get('A_HD_rank')==8,
      'A_HD_kernel':c.get('A_HD_kernel_dimension')==k.get('A_HD_kernel_dimension')==0,
      'transport_rank':c.get('A_HD_M_FR_rank')==k.get('A_HD_M_FR_rank')==7,
      'transport_hash':c.get('A_HD_M_FR_sha256')==k.get('A_HD_M_FR_sha256'),
      'branch':c.get('structural_branch')==k.get('structural_branch')=='CASE_II_NONINVARIANT',
      'image_kernel':c.get('field_redefinition_image_kernel_dimension_under_A_HD')==k.get('field_redefinition_image_kernel_dimension_under_A_HD')==0,
      'parent_H_hash':c.get('RCG004_H_sha256')==k.get('RCG004_H_sha256')=='7014978a97fce634d93f00e414903597245b8e4268b2c575dd1764547f96ced9'
    }
    valid=all(checks.values())
    r={
      'phase':'RCG006_A_HD_TRANSPORT_AGGREGATE','run_head':a.run_head,'aggregate_valid':valid,'agreement_checks':checks,
      'A_HD_rank':c.get('A_HD_rank'),'A_HD_kernel_dimension':c.get('A_HD_kernel_dimension'),'A_HD_sha256':c.get('A_HD_sha256'),
      'rank_M_FR':c.get('rank_M_FR'),'A_HD_M_FR_rank':c.get('A_HD_M_FR_rank'),'A_HD_M_FR_sha256':c.get('A_HD_M_FR_sha256'),
      'field_redefinition_image_kernel_dimension_under_A_HD':c.get('field_redefinition_image_kernel_dimension_under_A_HD'),
      'structural_branch':c.get('structural_branch'),'quotient_aware_second_order_space_dimension':c.get('quotient_aware_second_order_space_dimension'),
      'classification':'PASS_SCOPED_RCG006_FIELD_REDEFINITION_DISCRIMINATOR_NONINVARIANT' if valid else 'INVALID_RCG006_A_HD_TRANSPORT_AGGREGATE',
      'interpretation':'Nonzero field-redefinition image directions are representative-level higher-derivative under the frozen A_HD discriminator while EFT-equivalent to EH at first order. Historical RCG005 remains unchanged; the representative-level discriminator is not invariant along admitted EFT orbits.',
      'chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%'
    }
    r['scientific_payload_sha256']=sha(r);Path(a.output).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({k:r[k] for k in ('aggregate_valid','A_HD_rank','A_HD_M_FR_rank','structural_branch','classification')},sort_keys=True))
if __name__=='__main__':main()
