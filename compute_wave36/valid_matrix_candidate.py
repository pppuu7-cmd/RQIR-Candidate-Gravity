from common import complete_candidate,validate,relevant_basis_from_matrix,canonical_matrix,write
c=complete_candidate(); ok,reasons,err=validate(c); B,vals=relevant_basis_from_matrix(canonical_matrix())
signals={
 'complete_synthetic_same_schema_matrix_candidate_is_accepted':ok and not reasons,
 'accepted_candidate_has_three_attractive_real_dimensions':B.shape==(5,3),
 'accepted_candidate_matrix_and_basis_are_consistent':err is not None and err<1e-10
}
out={'test':'valid_matrix_candidate','accepted':ok,'reasons':reasons,'projector_error':err,'eigenvalues':[str(z) for z in vals],'signals':signals}; write('wave36_valid_matrix_candidate.json',out); assert all(signals.values())
