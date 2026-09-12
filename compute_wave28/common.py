import json, hashlib
from pathlib import Path
import numpy as np
EVIDENCE=Path('evidence/WAVE28_F1F2_DATA_AVAILABILITY.json')
PREREG=Path('post_freeze/WAVE28_JACOBIAN_DATA_CONTRACT_PREREGISTRATION.md')
BANK=Path('holdouts/WAVE22_FROZEN_BANK.json')
EXPECTED_BANK_BLOB='c32bd52edd003589ef65e0240c757475f215f55f'

def load(): return json.loads(EVIDENCE.read_text())
def blob_sha(path):
 data=Path(path).read_bytes(); return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
def write(name,obj):
 Path('wave28_results').mkdir(exist_ok=True)
 def default(v):
  if isinstance(v,np.ndarray): return v.tolist()
  if hasattr(v,'item'): return v.item()
  raise TypeError(type(v).__name__)
 text=json.dumps(obj,indent=2,sort_keys=True,default=default)
 Path(f'wave28_results/{name}.json').write_text(text); print(text)
