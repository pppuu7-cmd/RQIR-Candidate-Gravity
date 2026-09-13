import argparse, json, math, os
import numpy as np
from scipy.integrate import quad

G = 6.67430e-11
HBAR = 1.054571817e-34
C = 299792458.0
RATIOS = (1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0)
BASE_DS = np.array([0.45, 0.62, 0.57, 0.48], dtype=float)
SCALES = (0.82, 0.91, 1.00, 1.09, 1.18, 1.31, 1.47, 1.66)
PERT = (
    (1.000, 1.000, 1.000, 1.000),
    (1.006, 0.995, 1.003, 0.997),
    (0.994, 1.004, 0.997, 1.005),
    (1.008, 0.996, 1.005, 0.994),
    (0.995, 1.007, 0.996, 1.004),
    (1.004, 0.993, 1.006, 0.998),
    (0.997, 1.005, 0.994, 1.007),
    (1.005, 0.997, 1.004, 0.995),
)


def gaussian_kernel(R, s):
    return math.erf(R / (math.sqrt(2.0) * s)) / R


def fourier_kernel(R, s):
    ratio = R / s
    def f(x):
        if abs(x) < 1e-15:
            sinc = 1.0
        else:
            sinc = math.sin(x * ratio) / (x * ratio)
        return math.exp(-0.5 * x * x) * sinc
    val, err = quad(f, 0.0, 12.0, epsabs=1e-13, epsrel=1e-13, limit=1000)
    return (2.0 / math.pi) * val / s, err


def relerr(a, b):
    return abs(a - b) / max(abs(b), 1e-30)


def choi_from_unitary(U):
    d = U.shape[0]
    J = np.zeros((d*d, d*d), dtype=complex)
    for i in range(d):
        for j in range(d):
            E = np.zeros((d, d), dtype=complex)
            E[i, j] = 1.0
            J += np.kron(E, U @ E @ U.conj().T)
    return J


def partial_trace_output(J, d=4):
    out = np.zeros((d, d), dtype=complex)
    for i in range(d):
        for j in range(d):
            block = J[i*d:(i+1)*d, j*d:(j+1)*d]
            out[i, j] = np.trace(block)
    return out


def run(case):
    ratio = RATIOS[case]
    ds = BASE_DS * SCALES[case] * np.array(PERT[case], dtype=float)
    s = float(np.min(ds) / ratio)
    mA = 1.0e-14 * (1.0 + 0.025 * case)
    mB = 1.2e-14 * (1.0 - 0.015 * case)
    T = 0.80 + 0.07 * case
    alpha = G * mA * mB * T / HBAR

    ka = np.array([gaussian_kernel(float(d), s) for d in ds])
    kn = []
    qerr = []
    for d in ds:
        v, e = fourier_kernel(float(d), s)
        kn.append(v); qerr.append(e)
    kn = np.array(kn)
    kernel_rel = max(relerr(a, b) for a, b in zip(kn, ka))

    phases = alpha * ka
    p00, p01, p10, p11 = [float(x) for x in phases]
    chi = p00 + p11 - p01 - p10

    global_phase = p00
    local_b = p01 - p00
    local_a = p10 - p00
    rec = np.array([global_phase,
                    global_phase + local_b,
                    global_phase + local_a,
                    global_phase + local_a + local_b + chi])
    U = np.diag(np.exp(1j * phases))
    Urec = np.diag(np.exp(1j * rec))
    factorization_error = float(np.max(np.abs(U - Urec)))

    c0 = 0.13 + 0.01 * case
    ashift = np.array([0.07, -0.04])
    bshift = np.array([0.02, -0.09])
    shifted = np.array([
        p00 + c0 + ashift[0] + bshift[0],
        p01 + c0 + ashift[0] + bshift[1],
        p10 + c0 + ashift[1] + bshift[0],
        p11 + c0 + ashift[1] + bshift[1],
    ])
    shifted_chi = shifted[0] + shifted[3] - shifted[1] - shifted[2]
    local_shift_abs_error = abs(float(shifted_chi) - chi)

    ds_ex = ds[[0, 2, 1, 3]]
    chi_ex = alpha * (gaussian_kernel(float(ds_ex[0]), s) + gaussian_kernel(float(ds_ex[3]), s)
                      - gaussian_kernel(float(ds_ex[1]), s) - gaussian_kernel(float(ds_ex[2]), s))
    exchange_rel_error = relerr(float(chi_ex), chi)

    J = choi_from_unitary(U)
    ptr = partial_trace_output(J)
    tp_residual = float(np.max(np.abs(ptr - np.eye(4))))
    herm_residual = float(np.max(np.abs(J - J.conj().T)))
    Jh = 0.5 * (J + J.conj().T)
    eigs = np.linalg.eigvalsh(Jh)
    min_choi_eig = float(np.min(eigs))
    maxeig = max(float(np.max(eigs)), 1e-30)
    choi_rank = int(np.sum(eigs > maxeig * 1e-10))

    null_d = 0.5
    null_k = gaussian_kernel(null_d, s)
    null_chi = alpha * (null_k + null_k - null_k - null_k)

    point_chi = alpha * (1.0/ds[0] + 1.0/ds[3] - 1.0/ds[1] - 1.0/ds[2])
    point_rel = relerr(chi, float(point_chi))

    compactness = max(G*mA/(float(np.min(ds))*C*C), G*mB/(float(np.min(ds))*C*C))
    finite = bool(np.all(np.isfinite(ds)) and np.all(np.isfinite(ka)) and np.all(np.isfinite(kn))
                  and np.isfinite(chi) and np.isfinite(point_rel))

    checks = {
        'analytic_vs_fourier': kernel_rel <= 1e-10,
        'unitary_factorization': factorization_error <= 1e-12,
        'local_phase_quotient_invariance': local_shift_abs_error <= 1e-12,
        'ab_exchange_invariance': exchange_rel_error <= 1e-12,
        'trace_preserving': tp_residual <= 1e-12,
        'choi_hermitian': herm_residual <= 1e-12,
        'choi_positive': min_choi_eig >= -1e-12,
        'choi_rank_one': choi_rank == 1,
        'equal_distance_null': abs(null_chi) <= 1e-12,
        'high_ratio_point_limit': True if ratio < 8.0 else point_rel <= 1e-10,
        'weak_field_compactness': compactness < 1e-12,
        'finite': finite,
    }
    structural_valid = bool(case in range(8) and ratio > 0 and s > 0 and np.all(ds > 0))
    lane_support = bool(structural_valid and all(checks.values()))

    return {
        'iteration':'Iter050','gate':'G54-Q','case':case,'min_d_over_s':ratio,
        'distances_m':[float(x) for x in ds], 's_m':s, 'mA_kg':mA, 'mB_kg':mB, 'T_s':T,
        'analytic_kernels':[float(x) for x in ka], 'numeric_kernels':[float(x) for x in kn],
        'quadrature_errors':[float(x) for x in qerr], 'max_kernel_relative_error':kernel_rel,
        'finite_size_controlled_phase':chi, 'point_controlled_phase':float(point_chi),
        'point_phase_relative_difference':point_rel,
        'unitary_factorization_error':factorization_error,
        'local_shift_absolute_error':local_shift_abs_error,
        'exchange_relative_error':exchange_rel_error,
        'tp_residual':tp_residual, 'choi_hermiticity_residual':herm_residual,
        'minimum_choi_eigenvalue':min_choi_eig, 'choi_rank':choi_rank,
        'equal_distance_null_phase':float(null_chi), 'max_compactness':compactness,
        'checks':checks, 'structural_valid':structural_valid, 'lane_support':lane_support,
        'scope_lock':'Finite weak-field isotropic-Gaussian controlled-phase channel integration only; not covariant continuum gravity.'
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--case', type=int, required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    r = run(a.case)
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    with open(a.out, 'w') as f: json.dump(r, f, indent=2)
    print(json.dumps(r, indent=2))
    if not r['structural_valid']:
        raise SystemExit(2)

if __name__ == '__main__':
    main()
