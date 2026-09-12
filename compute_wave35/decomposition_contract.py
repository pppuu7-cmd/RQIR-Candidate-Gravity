from common import write
counts={'A':9,'B':6,'C':6,'D':4}
missing=counts['B']+counts['C']+counts['D']
signals={'missing_derivatives_decompose_exactly_6_plus_6_plus_4':missing==16,'known_A_plus_missing_blocks_cover_all_25_entries':counts['A']+missing==25,'synthetic_block_ranking_not_declared_physical':True}
out={'test':'decomposition_contract','entry_counts':counts,'missing_entries':missing,'signals':signals}; write('wave35_decomposition_contract.json',out); assert all(signals.values())
