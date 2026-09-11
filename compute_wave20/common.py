import json
from pathlib import Path

def _default(o):
    item=getattr(o,'item',None)
    if callable(item): return item()
    raise TypeError(f'{type(o).__name__} not JSON serializable')

def write_result(name,obj):
    Path('wave20_results').mkdir(exist_ok=True)
    text=json.dumps(obj,indent=2,sort_keys=True,default=_default)
    Path(f'wave20_results/{name}.json').write_text(text)
    print(text)
