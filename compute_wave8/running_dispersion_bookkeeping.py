#!/usr/bin/env python3
import json
import math
from pathlib import Path

# Toy scale-dependent Wilson/subtraction coefficient and compensating dispersive IR piece.
# The physical sum is scale independent in this bookkeeping proxy.
mu0=1.0
C0=0.02
I0=0.08
beta=0.015
mus=[1e-3,1e-2,1e-1,1.0,10.0,100.0,1000.0]
records=[]
for mu in mus:
    log=math.log(mu/mu0)
    C=C0+beta*log
    I=I0-beta*log
    B=C+I
    records.append({"mu":mu,"renormalized_local_coefficient_C":C,"dispersive_IR_piece_I":I,"physical_sum_B":B,"C_positive":C>=0,"B_positive":B>=0})
Bs=[r['physical_sum_B'] for r in records]
Cs=[r['renormalized_local_coefficient_C'] for r in records]
out={
 "test":"RG-running local coefficient versus scale-independent dispersive combination",
 "reference_scale":mu0,
 "C0":C0,
 "I0":I0,
 "beta":beta,
 "records":records,
 "local_coefficient_changes_sign_over_scan":min(Cs)<0<max(Cs),
 "physical_sum_variation":max(Bs)-min(Bs),
 "physical_sum_positive_all_scales":all(r['B_positive'] for r in records),
 "conclusion":"A renormalized local Wilson/subtraction coefficient can change sign under running while a properly combined dispersive quantity remains scale independent and positive. Positivity gates in gravity therefore need loop/RG-consistent bookkeeping rather than a naive sign test on one scheme-dependent coefficient.",
 "scope":"algebraic RG-bookkeeping proxy motivated by loop-corrected gravitational dispersion analyses; not a computed gravity beta function"
}
Path('wave8_results').mkdir(exist_ok=True)
Path('wave8_results/running_dispersion_bookkeeping.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
