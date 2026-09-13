#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import sympy as sp

p = argparse.ArgumentParser()
p.add_argument('--lane', required=True, choices=['A','B','C','D'])
p.add_argument('--out', required=True)
a = p.parse_args()


def emit(stream, classification, checks, valid, **extra):
    row = {
        'stream': stream,
        'classification': classification if valid else 'SCIENTIFIC_OR_GATE_FAIL',
        'checks': checks,
        'valid': bool(valid),
        'readiness': 66,
        'theory_established': 0,
    }
    row.update(extra)
    Path(a.out).write_text(json.dumps(row, indent=2, sort_keys=True))
    if not valid:
        raise SystemExit(2)


def connected(expr, av, bv, cv):
    total = 0
    for aa in (0,1):
        for bb in (0,1):
            for cc in (0,1):
                sign = (-1) ** (3 - aa - bb - cc)
                total += sign * sp.expand(expr.subs({av:aa,bv:bb,cv:cc}))
    return sp.simplify(total)

if a.lane == 'A':
    av,bv,cv = sp.symbols('a b c')
    k,A,B,C,AB,AC,BC,T = sp.symbols('k A B C AB AC BC T')
    inherited = k + A*av + B*bv + C*cv + AB*av*bv + AC*av*cv + BC*bv*cv
    chi_inherited = connected(inherited, av,bv,cv)
    chi_connected = connected(inherited + T*av*bv*cv, av,bv,cv)
    extra_local_pair = sp.symbols('u0') + sp.symbols('uA')*av + sp.symbols('uB')*bv + sp.symbols('uC')*cv + sp.symbols('uAB')*av*bv + sp.symbols('uAC')*av*cv + sp.symbols('uBC')*bv*cv
    invariance = sp.simplify(connected(inherited + T*av*bv*cv + extra_local_pair,av,bv,cv) - chi_connected)
    checks = {
        'chi_inherited': str(chi_inherited),
        'chi_with_true_connected_term': str(chi_connected),
        'local_pairwise_shift_invariance_delta': str(invariance),
    }
    valid = (chi_inherited == 0 and sp.simplify(chi_connected-T)==0 and invariance==0)
    emit('A','RCG002_THREE_SOURCE_CONNECTED_PHASE_IS_GENUINELY_BEYOND_PAIRWISE_SCOPED',checks,valid)

elif a.lane == 'B':
    authority = {
        'seed': 'candidates/RCG_002_RELATIONAL_CONTROLLED_PHASE_CHANNEL.md',
        'baseline': 'candidates/RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md',
        'g52': 'results/ITER048_G52H_WEAK_FIELD_HAMILTONIAN_QUOTIENT_TERMINAL.md',
        'g57': 'results/ITER055_G57P_CONSTITUTION_PREREQUISITE_AUDIT_TERMINAL.md',
        'g69': 'results/ITER067_G69_CANDIDATE_OWNED_NOVELTY_PREREQUISITE_TERMINAL.md',
        'g86': 'results/ITER084_G86_C_NONLINEAR_COMPLETION_NONUNIQUENESS_TERMINAL.md',
        'g88': 'results/ITER086_G88_C_INHERITED_CONSTRAINT_SELECTION_SUFFICIENCY_TERMINAL.md',
        'g90': 'results/ITER088_G90_C_COVARIANT_CUBIC_LIFT_TERMINAL.md',
        'g92': 'results/ITER090_G92_LEADING_VACUUM_SHELL_WITNESS_AUDIT_TERMINAL.md',
        'front': 'recovery/CURRENT_FRONT.md',
        'ledger': 'research_log/RQIRCG_RESEARCH_LEDGER.md',
    }
    texts = {}
    presence = {}
    for key,path in authority.items():
        q = Path(path)
        presence[key] = q.exists()
        texts[key] = q.read_text() if q.exists() else ''

    markers = {
        'g52_pairwise_bridge': 'WEAK_FIELD_PAIR_ENERGY_TO_CONTROLLED_PHASE_QUOTIENT_BRIDGE_VALIDATED' in texts['g52'],
        'g57_missing_dynamics': 'A5_gravity_dynamical_principle' in texts['g57'],
        'g69_blocked_beyond_baseline': 'BLOCKED_CANDIDATE_OWNED_BEYOND_BASELINE_DYNAMICS_NOT_YET_DEFINED' in texts['g69'],
        'g90_not_physical_completion': 'physical nonlinear completion' in texts['g90'],
        'g92_requires_candidate_owned_map': 'candidate-owned map' in texts['g92'],
        'front_map_absent_rule': 'nonlinear map is absent' in texts['front'],
        'ledger_no_selector': 'no candidate-owned genuinely higher-order physical selector has yet been justified' in texts['ledger'],
    }
    # A present map must be an already-authoritative explicit object in the frozen source set,
    # not this preregistration or a synthetic control. No such object is inferred from wish-list text.
    explicit_map_hits = []
    for key,text in texts.items():
        low = text.lower()
        if ('chi_abc' in low and 'theta1' in low and 'theta2' in low and 'source protocol' in low):
            explicit_map_hits.append(key)
    map_present = len(explicit_map_hits) > 0
    valid = all(presence.values()) and all(markers.values())
    classification = ('CANDIDATE_OWNED_THREE_SOURCE_NONLINEAR_PHASE_MAP_PRESENT_SCOPED'
                      if map_present else
                      'BLOCKED_CANDIDATE_OWNED_THREE_SOURCE_NONLINEAR_PHASE_MAP_NOT_DEFINED_SCOPED')
    checks = {
        'authority_files_present': presence,
        'source_lock_markers': markers,
        'explicit_map_hits': explicit_map_hits,
        'map_present': map_present,
    }
    emit('B',classification,checks,valid,map_status=('PRESENT' if map_present else 'MISSING'))

elif a.lane == 'C':
    t1,t2 = sp.symbols('theta1 theta2')
    rank2 = sp.Matrix([[sp.diff(t1+2*t2,t1), sp.diff(t1+2*t2,t2)],
                       [sp.diff(3*t1-t2,t1), sp.diff(3*t1-t2,t2)]]).rank()
    rank1 = sp.Matrix([[1,1],[2,2]]).rank()
    rank0 = sp.zeros(2,2).rank()
    J = sp.Matrix([[1,2],[3,-1]])
    transforms = [sp.Matrix([[1,1],[0,1]]), sp.Matrix([[2,0],[1,1]]), sp.Matrix([[-1,2],[1,1]])]
    transformed = []
    for M in transforms:
        transformed.append({'det': str(M.det()), 'rank': int((J*M).rank())})
    valid = (rank2==2 and rank1==1 and rank0==0 and all(r['det']!='0' and r['rank']==2 for r in transformed))
    checks = {'rank_two_control':rank2,'rank_one_control':rank1,'rank_zero_control':rank0,'invertible_reparameterizations':transformed}
    emit('C','THREE_SOURCE_SELECTOR_RANK_PIPELINE_CALIBRATED_SCOPED',checks,valid)

elif a.lane == 'D':
    av,bv,cv = sp.symbols('a b c')
    # Completely arbitrary binary pair functions represented by multilinear expansions.
    p0,pA,pB,pAB,q0,qA,qC,qAC,r0,rB,rC,rBC,T = sp.symbols('p0 pA pB pAB q0 qA qC qAC r0 rB rC rBC T')
    pair_sum = (p0+pA*av+pB*bv+pAB*av*bv) + (q0+qA*av+qC*cv+qAC*av*cv) + (r0+rB*bv+rC*cv+rBC*bv*cv)
    pair_connected = connected(pair_sum,av,bv,cv)
    true_connected = connected(pair_sum + T*av*bv*cv,av,bv,cv)
    duplicate_rank = sp.Matrix([[1,2],[2,4]]).rank()
    J = sp.Matrix([[1,2],[3,-1]])
    M = sp.Matrix([[1,1],[0,1]])
    basis_rank_before = J.rank(); basis_rank_after = (J*M).rank()
    valid = (pair_connected==0 and sp.simplify(true_connected-T)==0 and duplicate_rank==1 and basis_rank_before==2 and basis_rank_after==2)
    checks = {
        'arbitrary_pairwise_connected_phase': str(pair_connected),
        'true_connected_term_detected': str(true_connected),
        'proportional_duplicate_protocol_rank': duplicate_rank,
        'rank_before_basis_change': basis_rank_before,
        'rank_after_invertible_basis_change': basis_rank_after,
    }
    emit('D','THREE_SOURCE_SELECTOR_INHERITED_AND_FALSE_POSITIVE_CONTROLS_SCOPED',checks,valid)
