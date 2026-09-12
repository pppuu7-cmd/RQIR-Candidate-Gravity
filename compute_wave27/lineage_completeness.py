from collections import defaultdict
from common import load,NODES,write
D=load(); groups=defaultdict(list)
for s in D['sources']: groups[s['lineage']].append(s)
rows=[]
for lineage,srcs in groups.items():
    support={n:any(s['support'].get(n,False) for s in srcs) for n in NODES}
    missing=[n for n,v in support.items() if not v]
    rows.append({'lineage':lineage,'sources':[s['id'] for s in srcs],'support':support,'supported_count':sum(support.values()),'missing':missing,'complete':not missing})
out={'lineages':rows,'max_same_lineage_supported_count':max(r['supported_count'] for r in rows),'no_single_published_lineage_closes_J0_J9':not any(r['complete'] for r in rows)}
write('lineage_completeness',out)
