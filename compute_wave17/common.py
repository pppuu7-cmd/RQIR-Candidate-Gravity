import json
from pathlib import Path
import numpy as np

D = 4

def projectors(k):
    k = np.asarray(k, dtype=float)
    k2 = float(k @ k)
    if k2 <= 0:
        raise ValueError('nonzero Euclidean momentum required')
    I = np.eye(D)
    omega = np.einsum('m,n->mn', k, k) / k2
    theta = I - omega
    P2 = 0.5*(np.einsum('mr,ns->mnrs', theta, theta) + np.einsum('ms,nr->mnrs', theta, theta)) - np.einsum('mn,rs->mnrs', theta, theta)/(D-1)
    P1 = 0.5*(np.einsum('mr,ns->mnrs', theta, omega) + np.einsum('ms,nr->mnrs', theta, omega) + np.einsum('nr,ms->mnrs', theta, omega) + np.einsum('ns,mr->mnrs', theta, omega))
    P0s = np.einsum('mn,rs->mnrs', theta, theta)/(D-1)
    P0w = np.einsum('mn,rs->mnrs', omega, omega)
    P0sw = np.einsum('mn,rs->mnrs', theta, omega)/np.sqrt(D-1)
    P0ws = np.einsum('mn,rs->mnrs', omega, theta)/np.sqrt(D-1)
    return {'P2':P2,'P1':P1,'P0s':P0s,'P0w':P0w,'P0sw':P0sw,'P0ws':P0ws}, theta, omega

def compose(A,B):
    return np.einsum('mnab,abrs->mnrs', A, B)

def contract(T, P, U):
    return float(np.einsum('mn,mnrs,rs->', T, P, U))

def conserved_tensor(rng, theta):
    S = rng.normal(size=(D,D))
    S = 0.5*(S+S.T)
    return theta @ S @ theta

def write_result(name, obj):
    Path('wave17_results').mkdir(exist_ok=True)
    Path(f'wave17_results/{name}.json').write_text(json.dumps(obj, indent=2, sort_keys=True))
    print(json.dumps(obj, indent=2, sort_keys=True))
