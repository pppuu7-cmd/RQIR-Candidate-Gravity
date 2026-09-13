import argparse, json, math, os
import numpy as np
from scipy.integrate import quad

G = 6.67430e-11
HBAR = 1.054571817e-34
C = 299792458.0
RATIOS = (1.25, 1.75, 2.50, 3.50, 5.00, 10.0)
BASE_DS = np.array([0.41, 0.67, 0.59, 0.46], dtype=float)
SCALES = (0.86, 0.96, 1.07, 1.20, 1.38, 1.61)
PERT = (
    (1.003, 0.996, 1.004, 0.998),
    (0.997, 1.005, 0.995, 1.003),
    (1.006, 0.994, 1.002, 0.997),
    (0.995, 1.004, 0.998, 1.006),
    (1.004, 0.997, 1.006, 0.995),
    (0.996, 1.006, 0.997, 1.004),
)
LOCAL_A = np.array([0.17, -0.11], dtype=float)
LOCAL_B = np.array([-0.07, 0.13], dtype=float)


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


def negativity(rho):
    rt = rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
    ev = np.linalg.eigvalsh(0.5 * (rt + rt.conj().T))
    return float(np.sum(np.maximum(-ev, 0.0))), [float(x) for x in ev]


def output_state(phases, local_a=None, local_b=None):
    plus2 = np.full(4, 0.5, dtype=complex)
    U = np.diag(np.exp(1j * np.asarray(phases, dtype=float)))
    psi = U @ plus2
    if local_a is not None and local_b is not None:
        UA = np.diag(np.exp(1j * np.asarray(local_a, dtype=float)))
        UB = np.diag(np.exp(1j * np.asarray(local_b, dtype=float)))
        psi = np.kron(UA, UB) @ psi
    return np.outer(psi, psi.conj())


def run(case):
    ratio = RATIOS[case]
    ds = BASE_DS * SCALES[case] * np.array(PERT[case], dtype=float)
    s = float(np.min(ds) / ratio)
    mA = 1.05e-14 * (1.0 + 0.031 * case)
    mB = 1.17e-14 * (1.0 - 0.012 * case)
    T = 0.91 + 0.083 * case
    alpha = G * mA * mB * T / HBAR

    ka = np.array([gaussian_kernel(float(d), s) for d in ds], dtype=float)
    kn, qerr = [], []
    for d in ds:
        v, e = fourier_kernel(float(d), s)
        kn.append(v); qerr.append(e)
    kn = np.asarray(kn, dtype=float)
    kernel_rel = float(max(relerr(a,b) for a,b in zip(kn,ka)))

    phases = alpha * ka
    p00,p01,p10,p11 = [float(x) for x in phases]
    chi = float(p00 + p11 - p01 - p10)

    rho = output_state(phases)
    n_direct, pt_eigs = negativity(rho)
    n_closed = float(abs(math.sin(0.5 * chi)) / 2.0)
    n_abs_diff = float(abs(n_direct - n_closed))

    rho_local = output_state(phases, LOCAL_A, LOCAL_B)
    n_local, _ = negativity(rho_local)
    local_inv = float(abs(n_local - n_direct))

    phases_ex = phases[[0,2,1,3]]
    rho_ex = output_state(phases_ex)
    n_ex, _ = negativity(rho_ex)
    exchange_inv = float(abs(n_ex - n_direct))

    null_d = float(np.mean(ds))
    null_phase = alpha * gaussian_kernel(null_d, s)
    null_phases = np.full(4, null_phase, dtype=float)
    n_null, _ = negativity(output_state(null_phases))

    tr_resid = float(abs(np.trace(rho) - 1.0))
    rho_h = 0.5 * (rho + rho.conj().T)
    rho_eigs = np.linalg.eigvalsh(rho_h)
    min_rho_eig = float(np.min(rho_eigs))
    compactness = float(max(G*mA/(float(np.min(ds))*C*C), G*mB/(float(np.min(ds))*C*C)))
    finite = bool(np.all(np.isfinite(ds)) and np.all(np.isfinite(phases)) and np.isfinite(n_direct)
                  and np.isfinite(n_closed) and np.isfinite(kernel_rel))

    checks = {
        'direct_vs_closed_negativity': bool(n_abs_diff <= 1e-12),
        'negativity_range': bool(n_direct >= -1e-15 and n_direct <= 0.5 + 1e-12),
        'density_trace': bool(tr_resid <= 1e-12),
        'density_positive': bool(min_rho_eig >= -1e-12),
        'local_z_invariance': bool(local_inv <= 1e-12),
        'ab_exchange_invariance': bool(exchange_inv <= 1e-12),
        'equal_distance_null': bool(n_null <= 1e-12),
        'analytic_vs_fourier': bool(kernel_rel <= 1e-10),
        'weak_field_compactness': bool(compactness < 1e-12),
        'finite': finite,
    }
    structural_valid = bool(case in range(6) and ratio > 0 and s > 0 and np.all(ds > 0))
    lane_support = bool(structural_valid and all(checks.values()))

    return {
        'iteration':'Iter051','gate':'G55-O','case':case,'min_d_over_s':float(ratio),
        'distances_m':[float(x) for x in ds], 's_m':s, 'mA_kg':float(mA), 'mB_kg':float(mB), 'T_s':float(T),
        'analytic_kernels':[float(x) for x in ka], 'numeric_kernels':[float(x) for x in kn],
        'quadrature_errors':[float(x) for x in qerr], 'max_kernel_relative_error':kernel_rel,
        'controlled_phase':chi, 'direct_negativity':n_direct, 'closed_form_negativity':n_closed,
        'negativity_absolute_difference':n_abs_diff, 'partial_transpose_eigenvalues':pt_eigs,
        'local_z_negativity_difference':local_inv, 'exchange_negativity_difference':exchange_inv,
        'equal_distance_null_negativity':float(n_null), 'density_trace_residual':tr_resid,
        'minimum_density_eigenvalue':min_rho_eig, 'max_compactness':compactness,
        'checks':checks, 'structural_valid':structural_valid, 'lane_support':lane_support,
        'scope_lock':'Prospectively held-out finite weak-field RCG-002 entanglement observable transport only; not covariant continuum gravity or experiment.'
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--case',type=int,required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    r=run(a.case)
    os.makedirs(os.path.dirname(a.out) or '.',exist_ok=True)
    with open(a.out,'w') as f: json.dump(r,f,indent=2)
    print(json.dumps(r,indent=2))
    if not r['structural_valid']:
        raise SystemExit(2)

if __name__=='__main__':
    main()
