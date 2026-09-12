import json, math, pathlib
import numpy as np
CLASSIFICATION='PARTIAL_SURROGATE_NOT_J8'
ANCHOR=np.array([-0.23,-0.060,0.64],float)
L4_0=-0.11; G4_0=0.55

def beta3(y,l4=L4_0,g4=G4_0):
    mu,l3,g3=np.asarray(y,float); A=1+mu; l5=l3; g5=g4
    if A<=0 or g3<=0 or g5<=0: return np.array([np.nan]*3)
    # Appendix-F F4 with all anomalous dimensions zero and g5=g4.
    bg3=2*g3 + 1/(19*math.pi)*(
      (g3**0.5*g5**1.5)/A**2*(47/6)*(-6)
      +(g3*g4)/(18*A**3)*(360+8*(30*l3-59*l4)*(-6)+360*l3*l4*(-4))
      +(g3*g4)/A**4*16*(1-3*l3)*l4
      -(g3**2)/(80*A**4)*(147*(-10)-1860*l3*(-8)+3380*l3**2*(-6)+25920*l3**3*(-4))
      -(2*g3**2)/(15*A**5)*(229-1780*l3+3640*l3**2-2336*l3**3)
      +(g3**2)/10*(53*(-10)+480))
    # Appendix-F F1.
    bmu=-2*mu +(1/(12*math.pi))*g4/A**2*(3*(-8)-8*l4*(-6)) \
         -(1/(180*math.pi))*g3/A**3*(21*(-10)-120*l3*(-8)+320*l3**2*(-6)) \
         +g3/(5*math.pi)*(-10)
    # Appendix-F F2, self-consistent in F4 through bg3/g3.
    bl3=(-1-0.5*bg3/g3)*l3 \
         -(1/(8*math.pi))*(g3**-0.5*g5**1.5)/A**2*((-8)-4*l5*(-6)) \
         -(1/(6*math.pi))*g4/A**3*(3*l4*(-8)-16*l3*l4*(-6)) \
         +(1/(240*math.pi))*g3/A**4*(11*(-12)-72*l3*(-10)+120*l3**2*(-8)-80*l3**3*(-6)) \
         -g3/(10*math.pi)*(-12)
    return np.array([bmu,bl3,bg3],float)

def jac_fd(f,x,h=1e-6):
    x=np.asarray(x,float); y=f(x); J=np.zeros((len(y),len(x)))
    for j in range(len(x)):
        d=np.zeros_like(x); d[j]=h*max(1.0,abs(x[j]))
        J[:,j]=(f(x+d)-f(x-d))/(2*d[j])
    return J

def solve_conditional(l4=L4_0,g4=G4_0,start=ANCHOR,tol=1e-10,maxit=60):
    f=lambda y: beta3(y,l4,g4); x=np.array(start,float)
    for it in range(maxit):
        b=f(x); nb=float(np.linalg.norm(b))
        if nb<tol: return x,True,it,nb
        J=jac_fd(f,x)
        try: d=np.linalg.solve(J,b)
        except np.linalg.LinAlgError: return x,False,it,nb
        alpha=1.0; moved=False
        for _ in range(24):
            z=x-alpha*d
            if z[0]>-0.95 and z[2]>1e-8 and np.all(np.isfinite(z)) and np.linalg.norm(f(z))<nb:
                x=z; moved=True; break
            alpha*=0.5
        if not moved: return x,False,it,nb
    nb=float(np.linalg.norm(f(x))); return x,nb<tol,maxit,nb

def write(name,obj):
    obj=dict(obj); obj.setdefault('classification',CLASSIFICATION)
    pathlib.Path(name).write_text(json.dumps(obj,indent=2,sort_keys=True)); print(json.dumps(obj,indent=2,sort_keys=True))
