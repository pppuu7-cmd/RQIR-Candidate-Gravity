#!/usr/bin/env python3
"""Execution wrapper: distinguish free output values from contraction-edge labels in Critic slots."""
import rcg006b_heldout_critic as m

def fixed_slots(n,matching,free):
    s=[None]*n
    for k,v in free.items(): s[k]=v
    for e,(a,b) in enumerate(matching): s[a]=s[b]=('e',e)
    return s

m.slots=fixed_slots

# All consumers use the convention: edge labels are tuples, free physical indices are ints.
def fixed_direct_component(raw,kind,cur,h4,u,v):
    if raw[0]=='metric':
        if u!=v:return m.sp.Rational(0)
        matching=raw[1];free={}
    else:
        _,i,j,matching=raw;free={i:u,j:v}
    s=fixed_slots(8 if kind=='A' else 6,matching,free);z=m.sp.Rational(0)
    for vals in m.product(range(4),repeat=len(matching)):
        ind=[vals[x[1]] if isinstance(x,tuple) else x for x in s]
        if kind=='A':z+=m.rval(cur,*ind[:4])*m.rval(cur,*ind[4:])
        else:z+=m.d2v(h4,*ind)
    return z
m.direct_component=fixed_direct_component

def fixed_symbolic_component(raw,kind,u,v):
    if raw[0]=='metric':
        if u!=v:return{}
        matching=raw[1];free={}
    else:
        _,i,j,matching=raw;free={i:u,j:v}
    s=fixed_slots(8 if kind=='A' else 6,matching,free);o=m.defaultdict(lambda:m.sp.Rational(0))
    for vals in m.product(range(4),repeat=len(matching)):
        ind=[vals[x[1]] if isinstance(x,tuple) else x for x in s]
        if kind=='A':m.add(o,m.mul(m.rpoly(*ind[:4]),m.rpoly(*ind[4:])))
        else:m.add(o,m.d2poly(*ind))
    return {k:v for k,v in o.items() if v}
m.symbolic_component=fixed_symbolic_component

def fixed_eval_cubic(match,cur):
    s=fixed_slots(12,match,{});z=m.sp.Rational(0)
    for vals in m.product(range(4),repeat=6):
        ind=[vals[x[1]] for x in s];z+=m.rval(cur,*ind[:4])*m.rval(cur,*ind[4:8])*m.rval(cur,*ind[8:])
    return m.sp.factor(z)
m.eval_cubic=fixed_eval_cubic

def fixed_eval_rd2(match,cur,h4):
    s=fixed_slots(10,match,{});z=m.sp.Rational(0)
    for vals in m.product(range(4),repeat=5):
        ind=[vals[x[1]] for x in s];z+=m.rval(cur,*ind[:4])*m.d2v(h4,*ind[4:])
    return m.sp.factor(z)
m.eval_rd2=fixed_eval_rd2

if __name__=='__main__':m.main()
