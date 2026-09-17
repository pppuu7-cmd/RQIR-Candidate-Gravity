#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
import sympy as sp

def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--constructor',required=True);ap.add_argument('--critic',required=True);ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args();c=json.loads(Path(a.constructor).read_text());k=json.loads(Path(a.critic).read_text());p=json.loads(Path('results/raw/RCG006_MFR_L0_CANONICAL.json').read_text())
    I=sp.Matrix([[sp.Rational(x) for x in r] for r in p['image_rref_rows']]).T;xc=sp.Matrix([sp.Rational(x) for x in c['RCG005_coordinates']]);xk=sp.Matrix([sp.Rational(x) for x in k['bivector_RCG005_coordinates']])
    checks={'constructor_valid':c.get('constructor_valid') is True,'critic_valid':k.get('critic_valid') is True,'image_rank7':I.rank()==7,'constructor_extends_to8':I.row_join(xc).rank()==8,'critic_extends_to8':I.row_join(xk).rank()==8,'same_one_dimensional_quotient_ray':I.row_join(xc).row_join(xk).rank()==8}
    valid=all(checks.values());r={'phase':'RCG006C_WEYL_CUBED_BRIDGE_AGGREGATE','run_head':a.run_head,'aggregate_valid':valid,'agreement_checks':checks,'constructor_RCG004_coordinates':c.get('RCG004_coordinates'),'critic_bivector_RCG004_coordinates':k.get('bivector_RCG004_coordinates'),'C3_over_D1D1_CLASS_11_mod_image':c.get('C3_over_D1D1_CLASS_11_mod_image'),'C3_over_RCG004_AXIS_8_mod_image':c.get('C3_over_RCG004_AXIS_8_mod_image'),'classification':'PASS_SCOPED_RCG006C_UNIQUE_EFT_CLASS_IS_PARITY_EVEN_WEYL_CUBED' if valid else 'INVALID_RCG006C_WEYL_BRIDGE_AGGREGATE','interpretation':'The mechanically constructed parity-even Weyl-cubed invariant is nonzero modulo Im(M_FR) and therefore spans the unique one-dimensional first-order local pure-metric bulk EFT quotient. This is an operator-identity bridge, not a viability claim.','chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%'};r['scientific_payload_sha256']=sha(r);Path(a.output).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({k:r[k] for k in ('aggregate_valid','classification','C3_over_D1D1_CLASS_11_mod_image')},sort_keys=True))
if __name__=='__main__':main()
