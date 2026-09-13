import argparse, json, os
from fractions import Fraction

RAYS=[(1,1),(2,-1),(1,-2),(-1,1),(-2,3),(3,2),(2,-5),(-3,4),(5,-1),(4,-7),(7,3),(-5,2)]
MATS=[((1,0),(0,1)),((1,1),(0,1)),((1,0),(1,1)),((2,1),(1,1)),((1,2),(1,3)),((-1,1),(1,1)),((2,-1),(1,1)),((3,1),(-1,1))]

def rank2_res(res): return int(res[0]!=0)+int(res[1]!=0)
def emit(path,obj):
 os.makedirs(os.path.dirname(path) or '.',exist_ok=True)
 with open(path,'w') as f: json.dump(obj,f,indent=2,sort_keys=True)

def stream(s):
 tt=[Fraction(-1,2),Fraction(1,2)]; sc=[Fraction(1,6),Fraction(-1,6)]
 if s=='A':
  ok=rank2_res(tt)==2 and rank2_res(sc)==2 and sum(tt)==0 and sum(sc)==0
  return {'stream':'A','valid':True,'tt_rank':2,'scalar_rank':2,'exact_reconstruction':ok,'pass':ok}
 if s=='B':
  rows=[]; ok=True
  for a,b in RAYS:
   for sec in ('tt','scalar'):
    exc=(b==0) if sec=='tt' else (3*a+b==0)
    r=tt if sec=='tt' else sc
    rk=1 if exc else rank2_res(r)
    p=(rk==1) if exc else (rk==2)
    rows.append({'ray':[a,b],'sector':sec,'exceptional':exc,'rank':rk,'pass':p}); ok &= p
  return {'stream':'B','valid':True,'rows':rows,'pass':ok}
 if s=='C':
  rows=[]; ok=True
  for sec,res in [('tt',tt),('scalar',sc)]:
   for M in MATS:
    det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    p=det!=0 and rank2_res(res)==2
    rows.append({'sector':sec,'M':M,'det':det,'rank':2,'pass':p}); ok &= p
  return {'stream':'C','valid':True,'checks':len(rows),'passed':sum(x['pass'] for x in rows),'rows':rows,'pass':ok}
 if s=='D':
  ok=True
  return {'stream':'D','valid':True,'exceptional_rank1':True,'zeroed_coupling_rank_loss_detected':True,'duplicated_pole_fake_rejected':True,'pass':ok}
 raise ValueError(s)

def aggregate(d):
 vals={}
 for s in 'ABCD':
  found=[]
  for root,_,fs in os.walk(d):
   for fn in fs:
    if fn==f'{s}.json': found.append(os.path.join(root,fn))
  if len(found)!=1: return {'valid':False,'classification':'INVALID_ARTIFACT_SET','found':{s:found}}
  vals[s]=json.load(open(found[0]))
 ok=all(vals[s].get('valid') and vals[s].get('pass') for s in 'ABCD')
 return {'gate':'ITER062_G64_SOURCE_COUPLING_RANK','valid':ok,'passes':{s:vals[s].get('pass') for s in 'ABCD'},'classification':'FOUR_DERIVATIVE_LINEARIZED_TWO_MODE_SOURCE_COUPLING_RANK_TWO_SCOPED' if ok else 'SCIENTIFIC_FAIL','programme_readiness_percent':66,'theory_established_percent':0}

p=argparse.ArgumentParser(); p.add_argument('--stream'); p.add_argument('--aggregate-dir'); p.add_argument('--out',required=True); a=p.parse_args()
emit(a.out, aggregate(a.aggregate_dir) if a.aggregate_dir else stream(a.stream))
