from common import EXPECTED_BANK_BLOB, PREREG, git_blob_sha, load_protocol, write_result
proto=load_protocol()
actual=git_blob_sha('holdouts/WAVE22_FROZEN_BANK.json')
text=PREREG.read_text()
checks={
 'bank_blob_exact':actual==EXPECTED_BANK_BLOB,
 'protocol_frozen':proto.get('status')=='FROZEN_PROSPECTIVE_FILTER',
 'protocol_wave_24':proto.get('authority_wave')==24,
 'no_polygon_equations_imported':'No KMQGB/polygon candidate equations or architecture may be imported.' in text,
 'five_principles_preregistered':all(k in text for k in ['K1 Soft/Ward','K2 Gravitational positivity','K3 Causality','K4 Asymptotic-safety','K5 Double copy'])
}
out={'actual_bank_blob':actual,'expected_bank_blob':EXPECTED_BANK_BLOB,'checks':checks,'future_candidate_information_firewall_pass':all(checks.values())}
write_result('information_firewall',out)
