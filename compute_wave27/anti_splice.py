from common import load,NODES,write
D=load(); srcs=D['sources']
union={n:any(s['support'].get(n,False) for s in srcs) for n in NODES}
missing=[n for n,v in union.items() if not v]
lineages=sorted(set(s['lineage'] for s in srcs))
out={'cross_lineage_union_support':union,'cross_lineage_union_missing':missing,'lineages_spliced':lineages,'policy':D['lineage_policy'],'cross_lineage_union_cannot_substitute_same_realization_chain':bool(len(lineages)>1 and ('J8' in missing or 'J9' in missing))}
write('anti_splice',out)
