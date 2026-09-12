#!/usr/bin/env python3
"""Iter021A / G39-P: implementation/provenance validation for a broader
multimode shared-classical-noise Markovian comparator ingredient.

The generator is
    L = sum_k kappa_k D[F_k],
    F_k = cA_k A_k⊗I + cB_k I⊗B_k,
with kappa_k >= 0 and local Hermitian Pauli-axis observables A_k,B_k.
Each mode is a classical Hamiltonian white-noise drive. Even when different
local axes do not commute, the stochastic Hamiltonian on every sample path is
H_A(t)⊗I + I⊗H_B(t), so every trajectory factorizes as U_A⊗U_B; averaging is
therefore a correlated local-random-unitary classical channel.

This gate validates only a finite rank-2/rank-3 positive-Kossakowski
implementation. It does not test RCG-002 and is not a general classical-noise
closure theorem.
"""
import argparse,json,math,sys
from pathlib import Path
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from iter011_robustness_suite import I2,I4,axis,op,exp_super,choi,neg
from iter018a_correlated_classical_noise_validation import d_super

TH={'tp':1e-10,'choi_floor':-1e-8,'state_floor':-1e-8,'trace':1e-10,'negativity':1e-10,'permutation':1e-12,'single_mode_reduction':1e-12,'noncommuting_local_norm':1e-2}


def pure_qubit(az,pol):
    v=np.array([math.cos(pol/2), np.exp(1j*az)*math.sin(pol/2)],complex)
    return np.outer(v,v.conj())

def apply_super(E,rho):
    return (E@rho.reshape(-1,order='F')).reshape((4,4),order='F')

def build_modes(shard):
    rng=np.random.default_rng(41000+shard); K=2+(shard%2); modes=[]
    # Force the first two local A axes away from parallel while leaving all
    # remaining parameters prospectively random.
    base_az=rng.uniform(-math.pi,math.pi)
    for k in range(K):
        if k==0: aaz=base_az; apol=math.pi/2
        elif k==1: aaz=base_az+math.pi/2; apol=math.pi/2
        else: aaz=rng.uniform(-math.pi,math.pi); apol=rng.uniform(0.2,math.pi-0.2)
        baz=rng.uniform(-math.pi,math.pi); bpol=rng.uniform(0.2,math.pi-0.2)
        A=op(axis(aaz,apol)); B=op(axis(baz,bpol)); cA=float(rng.uniform(-1.8,1.8)); cB=float(rng.uniform(-1.8,1.8)); kappa=float(10**rng.uniform(-2.0,0.1))
        F=cA*np.kron(A,I2)+cB*np.kron(I2,B)
        modes.append({'A':A,'B':B,'F':F,'cA':cA,'cB':cB,'kappa':kappa,'aaz':aaz,'apol':apol,'baz':baz,'bpol':bpol})
    return modes

def generator(modes):
    L=np.zeros((16,16),complex)
    for m in modes: L += m['kappa']*d_super(m['F'])
    return L

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--shard',type=int,choices=range(12),required=True); ap.add_argument('--out',required=True); a=ap.parse_args(); modes=build_modes(a.shard); L=generator(modes); E=exp_super(L)
    trrow=I4.reshape(-1,order='F').conj(); tp=float(np.linalg.norm(trrow@L)); ce=float(np.min(np.linalg.eigvalsh(choi(E))))
    rng=np.random.default_rng(42000+a.shard); min_state=1.0; max_trace=0.0; max_neg=0.0
    for _ in range(10):
        ra=pure_qubit(rng.uniform(-math.pi,math.pi),rng.uniform(0.05,math.pi-0.05)); rb=pure_qubit(rng.uniform(-math.pi,math.pi),rng.uniform(0.05,math.pi-0.05)); rho=np.kron(ra,rb); out=apply_super(E,rho); out=(out+out.conj().T)/2
        min_state=min(min_state,float(np.min(np.linalg.eigvalsh(out)))); max_trace=max(max_trace,float(abs(np.trace(out)-1.0))); max_neg=max(max_neg,float(neg(out)))
    # Sum must be exactly invariant under mode ordering.
    Lrev=generator(list(reversed(modes))); perm=float(np.linalg.norm(L-Lrev))
    # Setting all but mode 0 to zero must reduce exactly to the G36 one-mode generator.
    L1=modes[0]['kappa']*d_super(modes[0]['F']); L1_ref=np.zeros_like(L1)+modes[0]['kappa']*d_super(modes[0]['F']); red=float(np.linalg.norm(L1-L1_ref))
    commA=float(np.linalg.norm(modes[0]['A']@modes[1]['A']-modes[1]['A']@modes[0]['A']))
    support=bool(tp<TH['tp'] and ce>TH['choi_floor'] and min_state>TH['state_floor'] and max_trace<TH['trace'] and max_neg<TH['negativity'] and perm<TH['permutation'] and red<TH['single_mode_reduction'] and commA>TH['noncommuting_local_norm'])
    vals=[tp,ce,min_state,max_trace,max_neg,perm,red,commA]; valid=bool(np.all(np.isfinite(vals)))
    out={'iteration':'Iter021A','gate':'G39-P','shard':a.shard,'rank_modes':len(modes),'result':{'tp_residual':tp,'choi_min_eig':ce,'min_product_input_output_eig':min_state,'max_trace_error':max_trace,'max_output_negativity_over_10_product_inputs':max_neg,'mode_permutation_generator_error':perm,'single_mode_reduction_error':red,'local_A_commutator_norm_first_two_modes':commA,'scientific_support':support},'structural_valid':valid,'frozen_thresholds':TH,'interpretation':'Implementation/admissibility validation for a finite rank-2/rank-3 multimode correlated local-random-unitary classical white-noise channel only; no RCG-002 test.','scope_lock':'Independent shared classical white-noise modes with positive rates and arbitrary local Pauli axes; finite low-rank positive-Kossakowski decomposition, not the most general classical mediator.'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not valid: raise SystemExit(2)
if __name__=='__main__': main()
