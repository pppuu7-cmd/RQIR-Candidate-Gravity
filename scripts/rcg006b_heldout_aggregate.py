#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--constructor',required=True);ap.add_argument('--critic',required=True);ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args()
    c=json.loads(Path(a.constructor).read_text());k=json.loads(Path(a.critic).read_text())
    checks={
      'constructor_valid':c.get('constructor_valid') is True,
      'critic_valid':k.get('critic_valid') is True,
      'curvature_manifest':c.get('coordinate_manifest',{}).get('curvature_sha256')==k.get('coordinate_manifest',{}).get('curvature_sha256'),
      'h4_manifest':c.get('coordinate_manifest',{}).get('h4_sha256')==k.get('coordinate_manifest',{}).get('h4_sha256'),
      'final_bank_hash':c.get('banks',{}).get('final',{}).get('sha256')==k.get('banks',{}).get('final',{}).get('sha256'),
      'final_bank_sample_count':c.get('banks',{}).get('final',{}).get('samples')==k.get('banks',{}).get('final',{}).get('samples')==16,
      'canonical_MFR_identity':c.get('canonical_MFR_sha256')==k.get('canonical_MFR_sha256')=='7ac6ba6d1003c676899c0017409e3466a7f5e12fbb4114feee94580f1b0799bd',
      'final_stats_exact':c.get('final_bank_stats')==k.get('final_bank_stats'),
      'negative_controls':all(c.get('negative_controls',{}).values()) and all(k.get('negative_controls',{}).values())
    }
    valid=all(checks.values())
    r={'phase':'RCG006B_GENERIC_METRIC_JET_HELDOUT_AGGREGATE','run_head':a.run_head,'aggregate_valid':valid,'agreement_checks':checks,
      'coordinate_manifest':c.get('coordinate_manifest'),'constructor_bank':c.get('banks',{}).get('constructor'),'critic_bank':k.get('banks',{}).get('critic'),'final_bank':c.get('banks',{}).get('final'),
      'constructor_bank_stats':c.get('constructor_bank_stats'),'critic_bank_stats':k.get('critic_bank_stats'),'final_bank_stats':c.get('final_bank_stats'),
      'canonical_MFR_sha256':c.get('canonical_MFR_sha256'),'classification':'PASS_SCOPED_RCG006B_GENERIC_METRIC_JET_HELDOUT' if valid else 'INVALID_RCG006B_HELDOUT_VALIDATION',
      'interpretation':'Exact preregistered rational held-out banks validate frozen generator tensors, EH raw images and final quotient map without refit. Finite held-out agreement is a validation layer only and is not promoted to a universal identity proof.',
      'chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%'}
    r['scientific_payload_sha256']=sha(r);Path(a.output).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({'aggregate_valid':valid,'classification':r['classification'],'final_bank':r['final_bank'],'final_bank_stats':r['final_bank_stats']},sort_keys=True))
if __name__=='__main__':main()
