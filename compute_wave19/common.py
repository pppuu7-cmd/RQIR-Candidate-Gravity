import json
from pathlib import Path

def _json_default(obj):
    # Serialize NumPy scalar-like objects without importing NumPy in jobs that do not need it.
    item=getattr(obj,'item',None)
    if callable(item):
        return item()
    raise TypeError(f'Object of type {type(obj).__name__} is not JSON serializable')

def write_result(name,obj):
    Path('wave19_results').mkdir(exist_ok=True)
    text=json.dumps(obj,indent=2,sort_keys=True,default=_json_default)
    Path(f'wave19_results/{name}.json').write_text(text)
    print(text)
