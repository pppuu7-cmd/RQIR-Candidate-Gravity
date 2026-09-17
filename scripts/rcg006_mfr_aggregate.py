#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,hashlib
from pathlib import Path

def sha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--constructor',required=True); ap.add_argument('--critic',required=True); ap.add_argument('--output',required=True); ap.add_argument('--run-head',default=''); a=ap.parse_args()
    c=json.loads(Path(a.constructor).read_text()); k=json.loads(Path(a.critic).read_text())
    same={
      'parent_relation_hash':c['parent_relation_rref_sha256']==k['parent_relation_rref_sha256'],
      'shape':c['M_FR_shape']==k['M_FR_shape']==[8,9],
      'rank_alg':c['rank_M_ALG']==k['rank_M_ALG'],
      'rank_full':c['rank_M_FULL']==k['rank_M_FULL'],
      'kernel_dimension':c['kernel_dimension']==k['kernel_dimension'],
      'image_span':c['image_span_sha256']==k['image_span_sha256'],
      'qeft_dimension':c['Q_EFT_dimension']==k['Q_EFT_dimension'],
      'rcg004_intersection':c['RCG004_intersection_dimension']==k['RCG004_intersection_dimension'],
      'constructor_valid':c.get('constructor_valid') is True,
      'critic_valid':k.get('critic_valid') is True,
    }
    valid=all(same.values())
    r={
      'phase':'RCG006_MFR_L0_BOUNDED_AGGREGATE', 'run_head':a.run_head,
      'constructor_payload_sha256':c.get('scientific_payload_sha256'),'critic_payload_sha256':k.get('scientific_payload_sha256'),
      'agreement_checks':same,'aggregate_valid':valid,
      'M_FR_shape':c['M_FR_shape'],'M_FR_sha256_constructor':c['M_FR_sha256'],'M_FR_sha256_critic':k['M_FR_sha256'],
      'rank_M_ALG':c['rank_M_ALG'],'rank_M_FULL':c['rank_M_FULL'],'kernel_dimension':c['kernel_dimension'],
      'Q_EFT_dimension':c['Q_EFT_dimension'],'RCG004_intersection_dimension':c['RCG004_intersection_dimension'],'RCG004_residual_dimension':c['RCG004_residual_dimension'],
      'derivative_axis_witnesses':c['derivative_axis_witnesses'],'lexicographic_complement_axes':c['lexicographic_complement_axes'],
      'image_span_sha256':c['image_span_sha256'],'A_HD_transport_status':'NOT_COMPUTED_THIS_BOUNDED_SUBGATE','LS_companion_status':'NOT_COMPUTED_THIS_BOUNDED_SUBGATE',
      'chi_ABC':'UNAUTHORIZED_NOT_COMPUTED',
      'classification':'PASS_SCOPED_RCG006_MFR_L0_MAP_SUBGATE' if valid else 'INVALID_RCG006_MFR_L0_MAP_SUBGATE'
    }
    r['scientific_payload_sha256']=sha(r); Path(a.output).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:r[k] for k in ('aggregate_valid','rank_M_ALG','rank_M_FULL','Q_EFT_dimension','RCG004_intersection_dimension','classification')},sort_keys=True))
if __name__=='__main__': main()
