#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np

OUT=Path("wave2_results")
OUT.mkdir(exist_ok=True)

# Euclidean D=4 projector control. For nonzero k define theta = I - kk/k^2.
# The transverse symmetric-tensor projectors are
# P2 = 1/2(theta_mu_rho theta_nu_sigma + theta_mu_sigma theta_nu_rho)
#      - 1/(D-1) theta_mu_nu theta_rho_sigma
# P0 = 1/(D-1) theta_mu_nu theta_rho_sigma.
# Any K = A(k^2) P2 + B(k^2) P0 is Ward transverse. Therefore Ward identity
# alone constrains tensor structure but leaves scalar form factors A,B.

D=4
rng=np.random.default_rng(20260912)
k=rng.normal(size=D)
k2=float(k@k)
theta=np.eye(D)-np.outer(k,k)/k2

P2=np.zeros((D,D,D,D))
P0=np.zeros_like(P2)
for mu in range(D):
  for nu in range(D):
    for rho in range(D):
      for sig in range(D):
        P2[mu,nu,rho,sig]=0.5*(theta[mu,rho]*theta[nu,sig]+theta[mu,sig]*theta[nu,rho])-theta[mu,nu]*theta[rho,sig]/(D-1)
        P0[mu,nu,rho,sig]=theta[mu,nu]*theta[rho,sig]/(D-1)

ward_p2=np.einsum('m,mnrs->nrs',k,P2)
ward_p0=np.einsum('m,mnrs->nrs',k,P0)
ward_err=max(float(np.max(np.abs(ward_p2))),float(np.max(np.abs(ward_p0))))

# Construct a random conserved symmetric source T = theta S theta and verify.
S=rng.normal(size=(D,D)); S=(S+S.T)/2
T=theta@S@theta
cons_err=float(np.max(np.abs(k@T)))

# Count analytic regular EFT freedom after fixing the GR pole.
# Saturated GR kernel is proportional to [P2 - 1/(D-2) P0]/z.
# Let regular corrections be sum_{n=0}^N (a_n P2 + b_n P0) z^n.
# Ward transversality is automatic for every coefficient.
# We then optionally fix the first p regular coefficients in each sector and count residual freedom.
records=[]
for N in range(0,9):
    total=2*(N+1)
    for p in [0,1,2,3]:
        fixed=min(p,N+1)
        free=2*((N+1)-fixed)
        records.append({"max_regular_power":N,"fixed_regular_orders_each_sector":fixed,"total_regular_coefficients":total,"free_after_Ward_and_low_order_fixes":free})

# Demonstrate independent physical response directions using conserved sources:
# saturated contractions T P2 T and T P0 T are generally both nonzero.
c2=float(np.einsum('mn,mnrs,rs',T,P2,T))
c0=float(np.einsum('mn,mnrs,rs',T,P0,T))

summary={
 "test":"Ward-transverse flat-space symmetric-tensor response",
 "D":D,
 "k":[float(x) for x in k],
 "projector_Ward_max_abs_error":ward_err,
 "conserved_source_max_abs_error":cons_err,
 "conserved_source_spin2_contraction":c2,
 "conserved_source_spin0_contraction":c0,
 "GR_pole_ratio_B_over_A":-1.0/(D-2),
 "regular_form_factor_counting":records,
 "conclusion":"Ward transversality fixes projector support but does not fix the analytic scalar form factors A(k^2), B(k^2).",
 "scope":"flat-space finite-order form-factor count; additional GR-specific constraints can reduce this freedom and must be tested separately"
}
(OUT/"ward_transverse_form_factors.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
