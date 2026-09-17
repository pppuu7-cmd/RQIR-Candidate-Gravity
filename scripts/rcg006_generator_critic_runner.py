#!/usr/bin/env python3
"""Execution-only wrapper for rcg006_generator_critic.py; repairs Rational zero-default factory only."""
import collections
import rcg006_generator_critic as m
_real=collections.defaultdict
def fixed_defaultdict(factory=None,*args,**kwargs):
    if factory is m.sp.Rational:
        factory=lambda: m.sp.Rational(0)
    return _real(factory,*args,**kwargs)
m.defaultdict=fixed_defaultdict
if __name__=='__main__':
    m.main()
