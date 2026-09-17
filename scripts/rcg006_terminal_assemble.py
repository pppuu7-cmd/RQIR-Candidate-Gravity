#!/usr/bin/env python3
"""Outcome-independent terminal assembler for the frozen RCG006-v0 audit.

This script performs no new science. It consumes only already-materialized
canonical subgate authorities and applies the classifiers frozen in the
prospective RCG006 scientific preregistration.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--run-head',default='');a=ap.parse_args()
    m=load('results/raw/RCG006_MFR_L0_CANONICAL.json')
    h=load('results/raw/RCG006_A_HD_TRANSPORT_CANONICAL.json')
    l=load('results/raw/RCG006_SYMBOLIC_LAMBDA_CANONICAL.json')
    b=load('results/raw/RCG006B_HELDOUT_CANONICAL.json')
    checks={
      'mfr_terminal':m.get('classification')=='PASS_SCOPED_RCG006_MFR_L0_MAP_SUBGATE' and m.get('rank_M_FULL')==7 and m.get('Q_EFT_dimension')==1,
      'ahd_terminal':h.get('classification')=='PASS_SCOPED_RCG006_FIELD_REDEFINITION_DISCRIMINATOR_NONINVARIANT' and h.get('A_HD_rank')==8 and h.get('A_HD_kernel_dimension')==0 and h.get('A_HD_M_FR_rank')==7,
      'lambda_terminal':l.get('classification')=='PASS_SCOPED_RCG006_SYMBOLIC_LAMBDA_BULK_COMPANION' and l.get('Q_dim4_companion_dimension')==2 and l.get('Lambda_FULL_leakage_rank')==2,
      'heldout_terminal':b.get('classification')=='PASS_SCOPED_RCG006B_GENERIC_METRIC_JET_HELDOUT' and b.get('aggregate_valid') is True,
      'map_identity':m.get('M_FR_sha256')=='7ac6ba6d1003c676899c0017409e3466a7f5e12fbb4114feee94580f1b0799bd',
      'branch_noninvariant':h.get('structural_branch')=='CASE_II_NONINVARIANT',
      'claim_lock':m.get('chi_ABC')=='UNAUTHORIZED_NOT_COMPUTED' and h.get('chi_ABC')=='UNAUTHORIZED_NOT_COMPUTED' and l.get('chi_ABC')=='UNAUTHORIZED_NOT_COMPUTED' and b.get('chi_ABC')=='UNAUTHORIZED_NOT_COMPUTED'
    }
    valid=all(checks.values())
    classification='PASS_SCOPED_RCG006_FIELD_REDEFINITION_EQUIVALENCE_AUDIT_COMPLETE_NONINVARIANT_DISCRIMINATOR' if valid else 'INVALID_RCG006_TERMINAL_ASSEMBLY'
    r={
      'phase':'RCG006_V0_TERMINAL_ASSEMBLY','run_head':a.run_head,'aggregate_valid':valid,'checks':checks,'classification':classification,
      'generator_dimension_M':9,'Q_RCG005_dimension':8,'rank_M_ALG':m.get('rank_M_ALG'),'rank_M_FR':m.get('rank_M_FULL'),'kernel_M_FR_dimension':m.get('kernel_dimension'),'Q_EFT_dimension':m.get('Q_EFT_dimension'),
      'RCG004_intersection_dimension':m.get('RCG004_intersection_dimension'),'RCG004_residual_dimension':m.get('RCG004_residual_dimension'),'quotient_relation':m.get('quotient_relation'),
      'A_HD_rank':h.get('A_HD_rank'),'A_HD_kernel_dimension':h.get('A_HD_kernel_dimension'),'A_HD_M_FR_rank':h.get('A_HD_M_FR_rank'),'structural_branch':h.get('structural_branch'),'quotient_aware_second_order_space_dimension':h.get('quotient_aware_second_order_space_dimension'),
      'Q_dim4_companion_dimension':l.get('Q_dim4_companion_dimension'),'Lambda_ALG_leakage_rank':l.get('Lambda_ALG_leakage_rank'),'Lambda_FULL_leakage_rank':l.get('Lambda_FULL_leakage_rank'),'DER_bulk_companion_zero':l.get('DER_bulk_companion_zero'),
      'heldout_final_bank':b.get('final_bank'),'heldout_final_bank_stats':b.get('final_bank_stats'),
      'interpretation':'Seven of eight frozen RCG005 bulk action directions are first-order EH field-redefinition redundant; the remaining local parity-even pure-metric bulk EFT quotient is one-dimensional. The frozen representative-level higher-derivative discriminator is non-invariant along the redundant image, while the quotient-aware second-order survivor space remains zero. Symbolic Lambda adds a separate two-dimensional curvature-squared bulk companion. The preregistered exact held-out validates the frozen implementation without refit.',
      'historical_RCG005_reclassified':False,'boundary_observable_equivalence':False,'matter_equivalence':False,'nonperturbative_equivalence':False,
      'chi_ABC':'UNAUTHORIZED_NOT_COMPUTED','theory_established':'0%'
    }
    r['scientific_payload_sha256']=sha(r);Path(a.output).write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({'aggregate_valid':valid,'classification':classification,'rank_M_FR':r['rank_M_FR'],'Q_EFT_dimension':r['Q_EFT_dimension'],'structural_branch':r['structural_branch']},sort_keys=True))
if __name__=='__main__':main()
