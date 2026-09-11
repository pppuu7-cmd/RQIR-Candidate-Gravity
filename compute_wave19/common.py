import json
from pathlib import Path
import numpy as np

def write_result(name,obj):
    Path('wave19_results').mkdir(exist_ok=True)
    Path(f'wave19_results/{name}.json').write_text(json.dumps(obj,indent=2,sort_keys=True))
    print(json.dumps(obj,indent=2,sort_keys=True))
