import json
from pathlib import Path

def write_result(name,obj):
    Path('wave21_results').mkdir(exist_ok=True)
    text=json.dumps(obj,indent=2,sort_keys=True)
    Path(f'wave21_results/{name}.json').write_text(text)
    print(text)

def load_snapshot():
    return json.loads(Path('cross_route/KMQGB_AUTHORITY_SNAPSHOT_ITER209.json').read_text())
