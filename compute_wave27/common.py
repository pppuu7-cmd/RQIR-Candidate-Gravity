import json, hashlib
from pathlib import Path

EVIDENCE=Path('evidence/WAVE27_ASYMPTOTIC_SAFETY_LINEAGES.json')
BANK=Path('holdouts/WAVE22_FROZEN_BANK.json')
EXPECTED_BANK_BLOB='c32bd52edd003589ef65e0240c757475f215f55f'
NODES=[f'J{i}' for i in range(10)]

def load(): return json.loads(EVIDENCE.read_text())
def blob_sha(path):
    data=Path(path).read_bytes(); return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
def write(name,obj):
    Path('wave27_results').mkdir(exist_ok=True)
    text=json.dumps(obj,indent=2,sort_keys=True)
    Path(f'wave27_results/{name}.json').write_text(text)
    print(text)
