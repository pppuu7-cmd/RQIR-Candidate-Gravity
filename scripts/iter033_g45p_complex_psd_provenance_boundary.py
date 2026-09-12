#!/usr/bin/env python3
"""Iter033 / G45-P: response-blind provenance boundary audit for complex
Hermitian PSD Kossakowski generators on the six strictly local Pauli
operators. No RCG-002 target is used.
"""
import argparse, json, sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm

sys.path.insert(0, str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I2, I4, X, Y, Z, choi, neg
from iter024a_g41p_high_rank_classical_kossakowski import LOCAL, map_apply, split_local

TIMES = (0.1, 0.5, 1.0)
HERM_TOL = 1e-12
KOSS_FLOOR = -1e-10
TP_TOL = 1e-10
CHOI_FLOOR = -1e-8
UNITAL_REAL_TOL = 1e-10
DIFF_REAL_TOL = 1e-12
CLASSICAL_SPAN_REAL_TOL = 1e-10
FACTOR_TOL = 1e-12
NEG_REAL_TOL = 1e-9
OBSTRUCTION = 1e-6

PAULI = (I2, X, Y, Z)
FULL_H = [np.kron(PAULI[a], PAULI[b]) for a in range(4) for b in range(4) if not (a == 0 and b == 0)]
SAME_PAIRS = ((0, 1), (1, 2), (3, 4), (4, 5))
CROSS_PAIRS = ((0, 3), (1, 5), (2, 4), (0, 5))


def generator_from_C(C):
    C = np.asarray(C, complex)
    G = np.zeros((16, 16), complex)
    for i, Fi in enumerate(LOCAL):
        for j, Fj in enumerate(LOCAL):
            cij = C[i, j]
            if abs(cij) < 1e-18:
                continue
            P = Fj @ Fi
            G += cij * (np.kron(Fj.T, Fi) - 0.5 * (np.kron(I4, P) + np.kron(P.T, I4)))
    return G


def comm_super(H):
    return -1j * (np.kron(I4, H) - np.kron(H.T, I4))


def realvec(M):
    M = np.asarray(M, complex)
    return np.concatenate((M.real.ravel(), M.imag.ravel()))


def projection_residual(target, basis):
    A = np.stack([realvec(B) for B in basis], axis=1)
    y = realvec(target)
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(np.linalg.norm(y - A @ coef)), float(np.linalg.norm(y))


def real_symmetric_dissipator_basis():
    out = []
    for i in range(6):
        C = np.zeros((6, 6), float)
        C[i, i] = 1.0
        out.append(generator_from_C(C))
    for i in range(6):
        for j in range(i):
            C = np.zeros((6, 6), float)
            C[i, j] = C[j, i] = 1.0
            out.append(generator_from_C(C))
    assert len(out) == 21
    return out


REAL_DISSIPATORS = real_symmetric_dissipator_basis()
LOCAL_H_COMM = [comm_super(H) for H in LOCAL]
FULL_H_COMM = [comm_super(H) for H in FULL_H]
CLASSICAL_LINEAR_SPAN = REAL_DISSIPATORS + LOCAL_H_COMM


def real_control(shard):
    rank = 3 + (shard % 3)
    rng = np.random.default_rng(133000 + shard)
    M = rng.normal(size=(6, rank))
    Q, _ = np.linalg.qr(M)
    V = Q[:, :rank].T
    rates = np.asarray([0.045 + 0.016 * j + 0.003 * shard for j in range(rank)], float)
    C = V.T @ np.diag(rates) @ V
    return C.astype(complex), V, rates


def complex_control(panel, shard):
    pairs = SAME_PAIRS if panel == 'same_site_complex' else CROSS_PAIRS
    a, b = pairs[shard]
    v = np.zeros(6, complex)
    v[a] = 1.0 / np.sqrt(2.0)
    v[b] = 1j / np.sqrt(2.0)
    rate = 0.12 + 0.01 * shard
    C = rate * np.outer(v, v.conj())
    # Small real classical background, frozen before production, avoids making
    # the diagnostic depend on a completely isolated rank-one channel.
    bg = 0.012 + 0.002 * shard
    C[(shard + 2) % 6, (shard + 2) % 6] += bg
    return C, None, None


def factorization_error(V, rates, shard):
    xi = np.asarray([np.sin((j + 1) * (shard + 1) * 0.71) + 0.31 * np.cos((j + 2) * 1.17) for j in range(len(rates))], float)
    coeff = np.sqrt(rates) * xi
    Htot = sum(float(coeff[k]) * sum(float(V[k, q]) * LOCAL[q] for q in range(6)) for k in range(len(rates)))
    va = coeff @ V
    HA, HB = split_local(va)
    dt = 0.137
    return float(np.linalg.norm(expm(-1j * dt * Htot) - np.kron(expm(-1j * dt * HA), expm(-1j * dt * HB))))


def max_product_negativity(E, seed):
    rng = np.random.default_rng(seed)
    m = 0.0
    for _ in range(16):
        x = rng.normal(size=2) + 1j * rng.normal(size=2)
        y = rng.normal(size=2) + 1j * rng.normal(size=2)
        x /= np.linalg.norm(x); y /= np.linalg.norm(y)
        psi = np.kron(x, y)
        rho = np.outer(psi, psi.conj())
        m = max(m, float(neg(map_apply(E, rho))))
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--panel', choices=('real_psd_control', 'same_site_complex', 'cross_site_complex'), required=True)
    ap.add_argument('--shard', type=int, choices=range(4), required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    if a.panel == 'real_psd_control':
        C, V, rates = real_control(a.shard)
    else:
        C, V, rates = complex_control(a.panel, a.shard)

    herm = float(np.linalg.norm(C - C.conj().T))
    eig = np.linalg.eigvalsh((C + C.conj().T) / 2)
    min_eig = float(eig.min())
    G = generator_from_C(C)
    Greal = generator_from_C(C.real)
    D = G - Greal

    tr = I4.reshape(-1, order='F').conj()
    ivec = I4.reshape(-1, order='F')
    tp, cp, unital = [], [], []
    E07 = expm(G * 0.7)
    for t in TIMES:
        E = expm(G * float(t))
        tp.append(float(np.linalg.norm(tr @ E - tr)))
        cp.append(float(np.min(np.linalg.eigvalsh(choi(E)))))
        unital.append(float(np.linalg.norm(E @ ivec - ivec)))

    diff_real = float(np.linalg.norm(D))
    local_h_res, diff_norm = projection_residual(D, LOCAL_H_COMM)
    full_h_res, _ = projection_residual(D, FULL_H_COMM)
    classical_span_res, generator_norm = projection_residual(G, CLASSICAL_LINEAR_SPAN)
    maxneg = max_product_negativity(E07, 134000 + 100 * ('real_psd_control', 'same_site_complex', 'cross_site_complex').index(a.panel) + a.shard)
    fact = factorization_error(V, rates, a.shard) if V is not None else None

    vals = [herm, *eig, *tp, *cp, *unital, diff_real, local_h_res, full_h_res, classical_span_res, maxneg, generator_norm, diff_norm]
    if fact is not None:
        vals.append(fact)
    structural = bool(np.all(np.isfinite(vals)))
    admissible = bool(structural and herm <= HERM_TOL and min_eig >= KOSS_FLOOR and max(tp) <= TP_TOL and min(cp) >= CHOI_FLOOR)

    if a.panel == 'real_psd_control':
        classical_control_pass = bool(admissible and max(unital) <= UNITAL_REAL_TOL and diff_real <= DIFF_REAL_TOL and classical_span_res <= CLASSICAL_SPAN_REAL_TOL and fact <= FACTOR_TOL and maxneg <= NEG_REAL_TOL)
        obstruction = False
        scientific_support = classical_control_pass
        classification = 'REAL_PSD_CLASSICAL_PROVENANCE_CONTROL_PASS' if classical_control_pass else ('REAL_PSD_CLASSICAL_PROVENANCE_CONTROL_FAIL' if structural else 'STRUCTURAL_NUMERICAL_FAIL')
    else:
        classical_control_pass = None
        obstruction = bool(admissible and classical_span_res > OBSTRUCTION)
        scientific_support = obstruction
        classification = 'COMPLEX_PSD_FROZEN_CLASSICAL_SPAN_OBSTRUCTION_WITNESS' if obstruction else ('COMPLEX_PSD_PROVENANCE_OBSTRUCTION_NOT_SHOWN' if structural else 'STRUCTURAL_NUMERICAL_FAIL')

    out = {
        'iteration': 'Iter033', 'gate': 'G45-P', 'panel': a.panel, 'shard': a.shard,
        'kossakowski': {'hermiticity_residual': herm, 'min_eigenvalue': min_eig, 'max_eigenvalue': float(eig.max()), 'rank_1e-10': int(np.sum(eig > 1e-10))},
        'admissibility': {'max_tp_residual': max(tp), 'min_choi_eigenvalue': min(cp), 'max_unitality_residual': max(unital)},
        'provenance': {
            'generator_distance_from_ReC': diff_real,
            'difference_local_H_projection_residual': local_h_res,
            'difference_full_H_projection_residual': full_h_res,
            'full_realKoss_plus_localH_span_residual': classical_span_res,
            'generator_norm': generator_norm,
            'product_unitary_factorization_error': fact,
            'max_product_input_output_negativity': maxneg,
            'classical_provenance_obstruction_witness': obstruction,
            'real_classical_control_pass': classical_control_pass,
        },
        'structural_valid': structural, 'admissible': admissible, 'scientific_support': scientific_support, 'classification': classification,
        'frozen': {
            'times': list(TIMES), 'hermiticity_tol': HERM_TOL, 'kossakowski_floor': KOSS_FLOOR, 'tp_tol': TP_TOL, 'choi_floor': CHOI_FLOOR,
            'real_unital_tol': UNITAL_REAL_TOL, 'real_ReC_difference_tol': DIFF_REAL_TOL, 'real_classical_span_tol': CLASSICAL_SPAN_REAL_TOL,
            'factorization_tol': FACTOR_TOL, 'real_negativity_tol': NEG_REAL_TOL, 'complex_classical_span_obstruction': OBSTRUCTION,
            'RCG002_target_used': False,
        },
        'scope_lock': 'Frozen complex-Hermitian PSD GKSL provenance audit on the six local Pauli generators only; no comparator or universal mediator claim.',
        'interpretation': 'Response-blind provenance boundary only. No readiness increase and no RCG-002 separation inference.'
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))
    if not structural:
        raise SystemExit(2)

if __name__ == '__main__':
    main()
