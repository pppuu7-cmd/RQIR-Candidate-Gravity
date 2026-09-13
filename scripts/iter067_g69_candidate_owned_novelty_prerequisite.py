#!/usr/bin/env python3
import argparse, json
from pathlib import Path

FILES = {
 'seed':'candidates/RCG_002_RELATIONAL_CONTROLLED_PHASE_CHANNEL.md',
 'base':'candidates/RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md',
 'rcg1':'candidates/RCG_001_RELATIONAL_RESPONSE_KERNEL.md',
 'g51':'results/ITER047_G51K_BRANCHWISE_RETARDED_KERNEL_TERMINAL.md',
 'g52':'results/ITER048_G52H_WEAK_FIELD_HAMILTONIAN_QUOTIENT_TERMINAL.md',
 'g53':'results/ITER049_G53W_FINITE_SIZE_WAVEPACKET_TERMINAL.md',
 'g54':'results/ITER050_G54Q_FINITE_SIZE_CHANNEL_TERMINAL.md',
 'g55':'results/ITER051_G55O_HELDOUT_ENTANGLEMENT_OBSERVABLE_TERMINAL.md',
 'g56':'results/ITER054_G56F2_ROBUST_CONTINUUM_FIELD_CLOSURE_TERMINAL.md',
 'g57':'results/ITER055_G57P_CONSTITUTION_PREREQUISITE_AUDIT_TERMINAL.md',
 'g58':'results/ITER056_G58B_LINEARIZED_BASELINE_TERMINAL.md',
 'g68':'results/ITER066_G68_QUADRATIC_GRAVITY_BASELINE_TERMINAL.md',
}
EXPECTED_CANDIDATES={
 'RCG_001_RELATIONAL_RESPONSE_KERNEL.md',
 'RCG_002_RELATIONAL_CONTROLLED_PHASE_CHANNEL.md',
 'RCG_002_COVARIANT_BASELINE_COMPLETION_V0.md',
}

def load_all():
    missing=[p for p in FILES.values() if not Path(p).is_file()]
    if missing: return None,missing
    texts={k:Path(p).read_text(encoding='utf-8') for k,p in FILES.items()}
    return texts,[]

def has(t,*xs): return all(x in t for x in xs)
def check_map(items): return all(items.values())

def stream_A(t):
    cand={p.name for p in Path('candidates').glob('*.md')}
    c={
      'candidate_manifest_frozen_complete': cand==EXPECTED_CANDIDATES,
      'g57_missing_A4': 'A4_spacetime_gravitational_field_variable' in t['g57'],
      'g57_missing_A5': 'A5_gravity_dynamical_principle' in t['g57'],
      'baseline_declares_standard_embedding': has(t['base'],'smallest standard linearized spin-2 embedding','NOT A VALIDATED THEORY AND NOT A NOVELTY CLAIM'),
      'g58_weak_field_novelty_not_established': 'LINEARIZED_COVARIANT_BASELINE_EMBEDDING_SUPPORTED_AND_WEAK_FIELD_NOVELTY_NOT_ESTABLISHED' in t['g58'],
      'g68_local_four_derivative_baseline_equivalent': 'G60_G67_LOCAL_FOUR_DERIVATIVE_ESCAPE_BASELINE_EQUIVALENT_TO_STANDARD_QUADRATIC_GRAVITY_SCOPED' in t['g68'],
    }
    return {'stream':'A','structural_valid':check_map(c),'checks':c,'finding':'BLOCKED_NO_ELIGIBLE_BEYOND_BASELINE_SPACETIME_DYNAMICS_IN_FROZEN_EVIDENCE' if check_map(c) else 'EVIDENCE_INCONCLUSIVE','blocked':check_map(c)}

def stream_B(t):
    c={
      'delta_gamma_not_chosen': 'No form for `Delta Gamma` is chosen in this document.' in t['base'],
      'g51_toy_kernel_only': 'Finite branchwise-retarded weak-field toy-kernel audit only.' in t['g51'],
      'g51_not_covariant_continuum': 'does not derive a covariant GR retarded Green function, continuum gravity dynamics, or new physics' in t['g51'],
      'g68_open_structures_must_be_defined': has(t['g68'],'Candidate-owned nonlocal, higher-derivative, nonlinear, state-dependent, relational or quantum-measure dynamics remain logically open','must be defined and separately tested'),
    }
    return {'stream':'B','structural_valid':check_map(c),'checks':c,'finding':'BLOCKED_NO_SPECIFIED_BEYOND_BASELINE_DEFORMATION_IN_FROZEN_EVIDENCE' if check_map(c) else 'EVIDENCE_INCONCLUSIVE','blocked':check_map(c)}

def stream_C(t):
    c={
      'g57_C7_missing': 'C7_gravitational_quantization_measure_dynamics' in t['g57'],
      'baseline_no_full_measure': has(t['base'],'No nonlinear gravitational path-integral measure, gauge-fixed interacting measure, ghost determinant, renormalization prescription, or nonperturbative Hilbert space is supplied'),
      'g53_no_gravitational_measure': 'does not provide covariant continuum quantum-gravity dynamics, a gravitational field measure' in t['g53'],
      'operational_channel_not_promoted': has(t['seed'],'U_chi = diag(1,1,1,exp(i chi))','It does not permit `NEW_PHYSICS`, `FULL_QUANTUM_GRAVITY`'),
    }
    return {'stream':'C','structural_valid':check_map(c),'checks':c,'finding':'BLOCKED_NO_FIELD_LEVEL_GRAVITATIONAL_QUANTIZATION_MEASURE_IN_FROZEN_EVIDENCE' if check_map(c) else 'EVIDENCE_INCONCLUSIVE','blocked':check_map(c)}

def stream_D(t):
    c={
      'g55_internal_heldout_asset': 'HELDOUT_FINITE_SIZE_ENTANGLEMENT_OBSERVABLE_TRANSPORT_VALIDATED_SCOPED' in t['g55'],
      'g55_not_experimental': 'not a covariant continuum gravity theory, experimental confirmation' in t['g55'],
      'g58_novelty_not_established': 'novelty is **not established at this order**' in t['g58'],
      'g68_novelty_not_established': 'novelty is not established in the G60–G67 local linearized four-derivative layer' in t['g68'],
    }
    return {'stream':'D','structural_valid':check_map(c),'checks':c,'finding':'BLOCKED_NO_BASELINE_DISTINCT_EXTERNALLY_ANCHORED_PREDICTION_IN_FROZEN_EVIDENCE' if check_map(c) else 'EVIDENCE_INCONCLUSIVE','blocked':check_map(c)}

def stream_E(t):
    c={
      'operational_channel_explicit': 'rho -> E_eta( U_chi rho U_chi^dagger )' in t['seed'],
      'g52_bridge': 'WEAK_FIELD_PAIR_ENERGY_TO_CONTROLLED_PHASE_QUOTIENT_BRIDGE_VALIDATED' in t['g52'],
      'g53_bridge': 'FINITE_SIZE_GAUSSIAN_WAVEPACKET_WEAK_FIELD_BRIDGE_VALIDATED' in t['g53'],
      'g54_channel': 'FINITE_SIZE_WEAK_FIELD_CONTROLLED_PHASE_CHANNEL_INTEGRATED_SCOPED' in t['g54'],
      'g55_observable': 'HELDOUT_FINITE_SIZE_ENTANGLEMENT_OBSERVABLE_TRANSPORT_VALIDATED_SCOPED' in t['g55'],
      'g56_continuum': 'RCG002_GAUSSIAN_CONTINUUM_SOURCE_KERNEL_CLOSURE_VALIDATED_ROBUST_REPLACEMENT_SCOPED' in t['g56'],
      'g57_candidate_doc_stale': has(t['g57'],'C8_candidate_document_sync = STALE','seed candidate document still says that no microscopic formula for `chi` is asserted'),
    }
    return {'stream':'E','structural_valid':check_map(c),'checks':c,'finding':'POSITIVE_SCOPED_ASSETS_PRESENT_AND_DOCUMENT_SYNC_STALE' if check_map(c) else 'EVIDENCE_INCONCLUSIVE','positive_assets':check_map(c)}

def aggregate(indir):
    data={}; files={}
    for s in 'ABCDE':
        found=list(Path(indir).rglob(f'{s}.json')); files[s]=[str(x) for x in found]
        if len(found)!=1:
            return {'gate':'ITER067_G69_CANDIDATE_OWNED_NOVELTY_PREREQUISITE','structural_valid':False,'classification':'INFRASTRUCTURE_OR_ARTIFACT_INVALID','files':files,'programme_readiness_percent':66,'theory_established_percent':0}
        try: data[s]=json.loads(found[0].read_text())
        except Exception:
            return {'gate':'ITER067_G69_CANDIDATE_OWNED_NOVELTY_PREREQUISITE','structural_valid':False,'classification':'INFRASTRUCTURE_OR_ARTIFACT_INVALID','files':files,'programme_readiness_percent':66,'theory_established_percent':0}
    valid={s:bool(data[s].get('structural_valid')) for s in 'ABCDE'}
    if not all(valid.values()):
        cls='EVIDENCE_AUDIT_INCONCLUSIVE_'+''.join(s for s in 'ABCDE' if not valid[s])
    else:
        blockers=all(data[s].get('blocked') for s in 'ABCD')
        assets=bool(data['E'].get('positive_assets'))
        cls='BLOCKED_CANDIDATE_OWNED_BEYOND_BASELINE_DYNAMICS_NOT_YET_DEFINED' if blockers and assets else 'CANDIDATE_OWNED_BEYOND_BASELINE_INGREDIENT_IDENTIFIED_REQUIRES_MANUAL_OBJECT_RECORD'
    return {'gate':'ITER067_G69_CANDIDATE_OWNED_NOVELTY_PREREQUISITE','structural_valid':all(valid.values()),'stream_validity':valid,'classification':cls,'programme_readiness_percent':66,'theory_established_percent':0,'scope_lock':'Frozen repository-evidence inventory only; BLOCKED is not scientific FAIL and does not falsify RCG-002.'}

def emit(path,obj):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(obj,indent=2,sort_keys=True)); print(json.dumps(obj,indent=2,sort_keys=True))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--stream',choices=list('ABCDE')); ap.add_argument('--aggregate-dir'); ap.add_argument('--out',required=True); a=ap.parse_args()
    if a.aggregate_dir: return emit(a.out,aggregate(a.aggregate_dir))
    t,missing=load_all()
    if missing: return emit(a.out,{'stream':a.stream,'structural_valid':False,'missing':missing,'finding':'INFRASTRUCTURE_OR_ARTIFACT_INVALID'})
    fn={'A':stream_A,'B':stream_B,'C':stream_C,'D':stream_D,'E':stream_E}[a.stream]
    emit(a.out,fn(t))
if __name__=='__main__': main()
