#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--constructor',required=True);ap.add_argument('--critic',required=True);ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args()
    c=json.loads(Path(a.constructor).read_text());k=json.loads(Path(a.critic).read_text())
    checks={'constructor_valid':c.get('constructor_valid') is True,'critic_valid':k.get('critic_valid') is True,'companion_dim':c.get('Q_dim4_companion_dimension')==k.get('Q_dim4_companion_dimension')==2,'leakage_rank':c.get('Lambda_FULL_leakage_rank')==k.get('Lambda_FULL_leakage_rank'),'rowspace':c.get('Lambda_leakage_generator_rowspace_sha256')==k.get('Lambda_leakage_generator_rowspace_sha256'),'der_zero':c.get('DER_bulk_companion_zero') is True and k.get('DER_bulk_companion_zero') is True}
    valid=all(checks.values())
    r={'phase':'RCG006_SYMBOLIC_LAMBDA_COMPANION_AGGREGATE','run_head':a.run_head,'aggregate_valid':valid,'agreement_checks':checks,
      'Q_dim4_companion_dimension':c.get('Q_dim4_companion_dimension'),'Lambda_ALG_leakage_rank':c.get('Lambda_ALG_leakage_rank'),'Lambda_FULL_leakage_rank':c.get('Lambda_FULL_leakage_rank'),'Lambda_leakage_generator_rowspace_sha256':c.get('Lambda_leakage_generator_rowspace_sha256'),
      'DER_bulk_companion_zero':c.get('DER_bulk_companion_zero'),'DER_boundary_sensitive_divergence':c.get('DER_boundary_sensitive_divergence'),
      'classification':'PASS_SCOPED_RCG006_SYMBOLIC_LAMBDA_BULK_COMPANION' if valid else 'INVALID_RCG006_SYMBOLIC_LAMBDA_COMPANION_AGGREGATE',
      'interpretation':'At symbolic Lambda, the Lambda-weighted dimension-four bulk companion is tracked separately from the L0 8D parent. Any nonzero leakage does not alter L0 M_FR rank. DER traces contribute only boundary-sensitive total divergences in this frozen bulk-action scope.',
      'chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%'}
    r['scientific_payload_sha256']=sha(r);Path(a.output).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({k:r[k] for k in ('aggregate_valid','Q_dim4_companion_dimension','Lambda_FULL_leakage_rank','classification')},sort_keys=True))
if __name__=='__main__':main()
