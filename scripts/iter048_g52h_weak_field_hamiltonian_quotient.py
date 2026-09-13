import argparse, json, math, os
import numpy as np

G = 6.67430e-11
HBAR = 1.054571817e-34
C = 299792458.0

CASES = [
    ((0.45,0.62,0.57,0.48), 1.0e-14, 1.3e-14, 2.0),
    ((0.37,0.54,0.49,0.41), 1.7e-14, 1.1e-14, 1.5),
    ((0.28,0.51,0.44,0.35), 0.8e-14, 2.0e-14, 3.0),
    ((0.73,0.91,0.82,0.77), 2.2e-14, 1.4e-14, 1.2),
    ((0.19,0.32,0.27,0.22), 1.2e-14, 2.4e-14, 2.5),
    ((1.10,1.40,1.25,1.17), 2.5e-14, 0.9e-14, 4.0),
    ((0.52,0.89,0.71,0.58), 1.6e-14, 1.8e-14, 1.8),
    ((0.33,0.77,0.61,0.39), 0.9e-14, 2.7e-14, 2.2),
]


def relerr(a,b):
    return abs(a-b)/max(abs(b),1e-30)


def chi_cross(phi):
    return phi[0] + phi[3] - phi[1] - phi[2]


def run(case):
    ds,m1,m2,T = CASES[case]
    pref = G*m1*m2*T/HBAR
    phi = np.array([pref/d for d in ds], dtype=float)
    chi = float(chi_cross(phi))
    geom = 1.0/ds[0] + 1.0/ds[3] - 1.0/ds[1] - 1.0/ds[2]
    expected_chi = pref*geom

    g = phi[0]
    beta = phi[1]-phi[0]
    alpha = phi[2]-phi[0]
    U = np.diag(np.exp(1j*phi))
    Urec = np.exp(1j*g)*np.diag([
        1.0,
        np.exp(1j*beta),
        np.exp(1j*alpha),
        np.exp(1j*(alpha+beta+chi)),
    ])
    factorization_error = float(np.max(np.abs(U-Urec)))

    # Deterministic branch-local phase shifts c + a_i + b_j.
    a0 = 0.071*(case+1)
    a1 = -0.043*(case+1)
    b0 = 0.029*(case+1)
    b1 = -0.037*(case+1)
    cc = 0.013*(case+1)
    local = np.array([cc+a0+b0, cc+a0+b1, cc+a1+b0, cc+a1+b1])
    shifted_chi = float(chi_cross(phi+local))
    local_shift_error = abs(shifted_chi-chi)

    exchange_phi = np.array([phi[0],phi[2],phi[1],phi[3]])
    exchange_chi = float(chi_cross(exchange_phi))
    exchange_rel_error = relerr(exchange_chi, chi)

    equal_d = 0.5
    null_phi = np.array([pref/equal_d]*4)
    null_chi = float(chi_cross(null_phi))

    compactness = max(G*m1/(min(ds)*C*C), G*m2/(min(ds)*C*C))

    checks = {
        'factorization': factorization_error <= 1e-12,
        'analytic_cross_phase': relerr(chi, expected_chi) <= 1e-12,
        'local_phase_quotient_invariance': local_shift_error <= 1e-12,
        'exchange_symmetry': exchange_rel_error <= 1e-12,
        'equal_geometry_null': abs(null_chi) <= 1e-12,
        'weak_field_compactness': compactness < 1e-12,
    }
    structural_valid = all(d>0 for d in ds) and m1>0 and m2>0 and T>0
    lane_support = bool(structural_valid and all(checks.values()))

    result = {
        'iteration':'Iter048','gate':'G52-H','case':case,
        'distances_m':list(ds),'m1_kg':m1,'m2_kg':m2,'time_s':T,
        'phase_vector':phi.tolist(),'chi_cross':chi,'analytic_chi':expected_chi,
        'chi_relative_error':relerr(chi,expected_chi),
        'factorization_error':factorization_error,
        'local_shift_chi':shifted_chi,'local_shift_absolute_error':local_shift_error,
        'exchange_chi':exchange_chi,'exchange_relative_error':exchange_rel_error,
        'equal_geometry_null_chi':null_chi,
        'compactness':compactness,
        'checks':checks,'structural_valid':structural_valid,'lane_support':lane_support,
        'frozen_thresholds':{
            'unitary_factorization_abs':1e-12,'chi_relative':1e-12,
            'local_shift_chi_abs':1e-12,'exchange_relative':1e-12,
            'null_chi_abs':1e-12,'compactness_ceiling':1e-12,
        },
        'scope_lock':'Weak-field point-particle branch-energy quotient bridge only; not a covariant full-gravity derivation.'
    }
    return result


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--case',type=int,required=True); ap.add_argument('--out',required=True)
    a=ap.parse_args(); r=run(a.case)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(r,f,indent=2)
    print(json.dumps(r,indent=2))
    if not r['lane_support']: raise SystemExit(1)

if __name__=='__main__': main()
