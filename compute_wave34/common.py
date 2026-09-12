import json, math, pathlib
import numpy as np

PI=math.pi
COORDS=['mu','lambda3','lambda4','g3','g4']
X_TABLE=np.array([-0.23,-0.060,-0.11,0.64,0.55],float)
BAR_TARGET=np.array([-3.0,complex(-1.9,1.6),complex(-1.9,-1.6),1.7,3.4],complex)
CLASSIFICATION='SURROGATE_NOT_J8'

# Appendix-F Truncation-4 assumptions frozen before compute:
# eta_h(0)=eta_h=eta_c=eta_h'(0)=0,
# lambda5=lambda6=lambda3 and g5=g6=g4.

def flows(x):
    mu,l3,l4,g3,g4=map(float,x)
    if 1+mu <= 0 or g3 <= 0 or g4 <= 0:
        raise ValueError('outside frozen positive-coupling / away-from-pole domain')
    l5=l6=l3; g5=g6=g4
    # F1
    bmu = -2*mu
    bmu += (g4/(12*PI*(1+mu)**2))*(3*(-8)-8*l4*(-6))
    bmu -= (g3/(180*PI*(1+mu)**3))*(21*(-10)-120*l3*(-8)+320*l3*l3*(-6))
    bmu += (g3/(5*PI))*(-10)

    # F4: beta g3, eta=0
    t3=0.0
    t3 += (g3**0.5*g5**1.5)/(1+mu)**2*(47/6)*(-6)
    t3 += (g3*g4)/(18*(1+mu)**3)*(-45*(-8)+8*(30*l3-59*l4)*(-6)+360*l3*l4*(-4))
    t3 += (g3*g4)/(1+mu)**4*16*(1-3*l3)*l4
    t3 -= (g3*g3)/(80*(1+mu)**4)*(147*(-10)-1860*l3*(-8)+3380*l3*l3*(-6)+25920*l3**3*(-4))
    t3 -= (2*g3*g3)/(15*(1+mu)**5)*(229-1780*l3+3640*l3*l3-2336*l3**3)
    t3 += (g3*g3/10)*(53*(-10)+480)
    bg3 = 2*g3 + t3/(19*PI)

    # F5: beta g4, eta=0. Integer products are kept factored exactly as printed.
    t4=0.0
    t4 += (g6*g6)/(1+mu)**2*(32830375/25509168)*(-6)
    t4 -= (g4*g4)/(76527504*(1+mu)**3)*(11305705*(-8)+61298276*l4*(-6)+308793960*l4*l4*(-4))
    t4 -= (4*g4*g4)/(3188646*(1+mu)**4)*(16061481+8*(5355213*l4-5610604)*l4)
    t4 -= (g3**0.5*g5**1.5)/(19131876*(1+mu)**3)*(-34242339*(-8)+(86256922*l3-7511302*l5)*(-6)-4483422*l3*l5*(-4))
    t4 -= (g3**0.5*g5**1.5)/(1+mu)**4*(784609*(17-32*l3)-8937232*(4-9*l3)*l5)
    t4 += (g3*g4)/(90*(1+mu)**4)*(323831781*(-10)-(80*11179796*l3+203187860*l4)*(-8)-(10*129631943*l3-80*16941407*l4)*l3*(-6)-10*292902984*l3*l3*l4*(-4))
    t4 += (g3*g4)/(15*(1+mu)**5)*(26769135*(17+8*l3*(9*l3-8))-2*(353519805+4*l3*(742510961*l3-514449355))*l4)
    t4 += (2*g3*g4)/(9*(1+mu)**4)*(6783386859*(-10)-(140*86837935*l3+457106270*l4)*(-8)-(20*4067950507*l3+140*799593508*l4)*l3*(-6)-20*25136284404*l3*l3*l4*(-4))
    t4 += (g3*g4)/(15*(1+mu)**5)*(394709295-661068650*l4+40*(91735671*l4-34781816)*l3-8*(731880777*l4-220800215)*l3*l3)
    t4 += (g3*g3)/(45*(1+mu)**5)*(-125220803*(-12)+2*284391180*l3*(-10)+2*167456175*l3*l3*(-8)-2*236*13640606*l3**3*(-6)+2*236*36717495*l3**4*(-4))
    t4 -= (g3*g3)/(3*(1+mu)**6)*(112533531-855576992*l3+3683259968*l3*l3-7947008128*l3**3+6385327072*l3**4)
    t4 += 4*g3*g3*((23005837/5)*(-12)+11171540)
    bg4 = 2*g4 + (2125764/(6815761*PI))*t4

    # F2: beta lambda3. The beta_g3 term is part of the printed equation.
    bl3 = (-1-0.5*bg3/g3)*l3
    bl3 -= (1/(8*PI))*(g3**-0.5*g5**1.5)/(1+mu)**2*((-8)-4*l5*(-6))
    bl3 -= (1/(6*PI))*g4/(1+mu)**3*(3*l4*(-8)-16*l3*l4*(-6))
    bl3 += (1/(240*PI))*g3/(1+mu)**4*(11*(-12)-72*l3*(-10)+120*l3*l3*(-8)-80*l3**3*(-6))
    bl3 -= (g3/(10*PI))*(-12)

    # F3: beta lambda4. The beta_g4 term is part of the printed equation.
    s4=0.0
    s4 += 0.5*(g6*g6/g4)/(1+mu)**2*(-4472787*(-8)+1639004*l6*(-6))
    s4 += (1/15)*g4/(1+mu)**3*(5066361*(-10)-22517160*l4*(-8)+283174360*l4*l4*(-6))
    s4 += (2/15)*(g3**0.5*g5**1.5/g4)/(1+mu)**3*(3940503*(-10)-60*(187643*l3-1303286*l5)*(-8)+417051520*l3*l5*(-6))
    s4 += (2/5)*g3/(1+mu)**4*(-1313501*(-12)+3377574*(2*l3+l4)*(-10)-15011440*(l3+2*l4)*l3*(-8)+45442920*l3*l3*l4*(-6))
    s4 += (1/5)*(g3*g3/g4)/(1+mu)**5*(2874147*(-14)-20879816*l3*(-12)+36027456*l3*l3*(-10)+88161840*l3**3*(-8)-248160672*l3**4*(-6))
    s4 -= (10426288/7)*(g3*g3/g4)*(-14)
    bl4 = (-bg4/g4)*l4 + s4/(13387716*PI)

    return np.array([bmu,bl3,bl4,bg3,bg4],float)


def jacobian(x,h):
    x=np.asarray(x,float); J=np.zeros((5,5),float)
    for j in range(5):
        step=h*max(1.0,abs(x[j]))
        xp=x.copy(); xm=x.copy(); xp[j]+=step; xm[j]-=step
        J[:,j]=(flows(xp)-flows(xm))/(2*step)
    return J


def sorted_spectrum(vals):
    return np.array(sorted(vals,key=lambda z:(round(z.real,10),round(z.imag,10))),complex)


def assignment_distance(vals,target=BAR_TARGET):
    # exact minimum over 5! permutations; cheap and convention independent.
    import itertools
    vals=list(map(complex,vals)); target=list(map(complex,target))
    best=None; bestp=None
    for p in itertools.permutations(range(5)):
        d=max(abs(vals[p[i]]-target[i]) for i in range(5))
        if best is None or d<best:
            best=d; bestp=p
    return float(best),list(bestp)


def json_default(v):
    if isinstance(v,np.ndarray): return v.tolist()
    if isinstance(v,np.generic): return v.item()
    if isinstance(v,complex): return {'real':float(v.real),'imag':float(v.imag)}
    raise TypeError(type(v).__name__)

def write(name,obj):
    obj=dict(obj); obj.setdefault('classification',CLASSIFICATION)
    text=json.dumps(obj,indent=2,sort_keys=True,default=json_default)
    pathlib.Path(name).write_text(text); print(text)
