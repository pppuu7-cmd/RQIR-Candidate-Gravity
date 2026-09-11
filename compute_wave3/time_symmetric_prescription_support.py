#!/usr/bin/env python3
import json, math
from pathlib import Path

OUT=Path("wave3_results")
OUT.mkdir(exist_ok=True)

# Simple oscillator Green-function proxy.
# Retarded: G_R(t)=theta(t) sin(Omega t)/Omega * exp(-eps |t|).
# Advanced: G_A(t)=-theta(-t) sin(Omega t)/Omega * exp(-eps |t|).
# Time-symmetric principal-value-like proxy: G_sym=(G_R+G_A)/2.
# It has support on both signs of t. This is NOT a full fakeon calculation; it
# quantifies the causal price of replacing a retarded pole prescription by a
# time-symmetric average in the simplest linear response model.

Omega=1.0
eps=0.03
T=80.0
dt=0.002
n=int(2*T/dt)+1
neg_energy_ret=tot_energy_ret=0.0
neg_energy_sym=tot_energy_sym=0.0
max_neg_ret=0.0
max_neg_sym=0.0
samples=[]
for i in range(n):
    t=-T+i*dt
    damp=math.exp(-eps*abs(t))
    GR=(math.sin(Omega*t)/Omega*damp) if t>=0 else 0.0
    GA=(-math.sin(Omega*t)/Omega*damp) if t<=0 else 0.0
    Gsym=0.5*(GR+GA)
    er=GR*GR*dt
    es=Gsym*Gsym*dt
    tot_energy_ret+=er; tot_energy_sym+=es
    if t<0:
        neg_energy_ret+=er; neg_energy_sym+=es
        max_neg_ret=max(max_neg_ret,abs(GR)); max_neg_sym=max(max_neg_sym,abs(Gsym))
    if abs(t) in (0.0,):
        pass

summary={
 "test":"retarded versus time-symmetric Green-function support",
 "Omega":Omega,"epsilon_damping":eps,"T":T,"dt":dt,
 "retarded_negative_time_L2_fraction":neg_energy_ret/tot_energy_ret if tot_energy_ret else None,
 "symmetric_negative_time_L2_fraction":neg_energy_sym/tot_energy_sym if tot_energy_sym else None,
 "retarded_max_negative_time_abs":max_neg_ret,
 "symmetric_max_negative_time_abs":max_neg_sym,
 "result":"The retarded proxy has zero negative-time response; the time-symmetric average carries approximately half of its L2 support at negative time.",
 "scope":"linear oscillator proxy for prescription-induced microscopic acausality/time symmetry; not a full fakeon/Lee-Wick gravity computation"
}
(OUT/"time_symmetric_prescription_support.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
