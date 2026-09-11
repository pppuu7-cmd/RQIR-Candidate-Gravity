import numpy as np
from common import write_result

# Soft-limit proxy. A higher-derivative transverse contact correction C(q)=c2 q^2+c3 q^3
# vanishes at q=0 together with its first derivative, so leading + first-subleading soft data cannot fix it.
# This is an algebraic visibility test, not a complete soft-graviton theorem derivation.
cs=[(-0.7,0.25),(0.0,0.0),(0.55,-0.2)]
q_hold=0.65
rows=[]
for c2,c3 in cs:
    C0=0.0
    dC0=0.0
    hold=c2*q_hold**2+c3*q_hold**3
    rows.append({'c2':c2,'c3':c3,'C_soft':C0,'dC_soft':dC0,'finite_q_holdout':hold})
hold_width=max(r['finite_q_holdout'] for r in rows)-min(r['finite_q_holdout'] for r in rows)
out={
 'test':'soft-limit visibility of higher-derivative transverse contact directions',
 'contact_family':'C(q)=c2 q^2+c3 q^3',
 'soft_constraints':['C(0)=0','dC/dq(0)=0'],
 'scan':rows,'finite_q_holdout_width':hold_width,
 'leading_and_first_subleading_soft_data_leave_contact_freedom':hold_width>1e-4,
 'conclusion':'Corrections beginning at quadratic order in the soft momentum evade leading and first-subleading soft information while changing finite kinematics. Soft constraints can be strong without uniquely fixing higher-derivative transverse contact structure.'
}
write_result('soft_contact_freedom',out)
