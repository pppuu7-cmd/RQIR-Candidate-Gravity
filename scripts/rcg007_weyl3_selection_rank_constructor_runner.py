#!/usr/bin/env python3
"""Execution-only wrapper for RCG007 Constructor.

Repairs only case-sensitive source-wording matching. Scientific rows, object,
rank, controls and classifiers remain in the frozen Constructor unchanged.
"""
from pathlib import Path
import rcg007_weyl3_selection_rank_constructor as m

def case_insensitive_has(path,*phrases):
    s=Path(path).read_text().lower()
    return all(p.lower() in s for p in phrases)

m.has=case_insensitive_has

if __name__=='__main__':
    m.main()
