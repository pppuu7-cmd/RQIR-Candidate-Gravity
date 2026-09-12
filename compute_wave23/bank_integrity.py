from common import EXPECTED_BLOB_SHA, git_blob_sha, load_bank, write_result

b=load_bank(); actual=git_blob_sha()
checks={
 'git_blob_sha_exact':actual==EXPECTED_BLOB_SHA,
 'authority_run_exact':b.get('authority_run')==34661882499,
 'authority_commit_exact':b.get('authority_commit')=='9009bb7e68e083cc819ebf0a3d6b6a111950e456',
 'parameter_order_exact':b.get('parameter_order')==['c3','d3','e4','f4','s2','s0'],
 'probe_count_exact':len(b.get('probes',[]))==10,
 'status_frozen':b.get('status')=='FROZEN_CANDIDATE_BLIND_FINITE_PROXY_EXAM'
}
out={
 'test':'frozen Wave-22 bank integrity',
 'expected_blob_sha':EXPECTED_BLOB_SHA,
 'actual_blob_sha':actual,
 'checks':checks,
 'integrity_pass':all(checks.values()),
 'conclusion':'Wave 23 is reading the exact frozen Wave-22 candidate-blind bank rather than a silently modified copy.'
}
write_result('bank_integrity',out)
