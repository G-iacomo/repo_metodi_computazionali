import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import math
def f_diff(r,t,l):
    '''
    r(theta,omega) vettore 
    l lunghezza pendolo
    d=derivata rispetto al tempo
    '''
    dtheta=r[1]
    dw=-9.81*math.sin(r[0])/l
    dr=[dtheta,dw]
    return dr

l=[0.5,1,0.5]
r0=[[np.pi/4,0],[np.pi/4,0],[np.pi/3,0]] #parametri iniziali
t=np.linspace(0,10,1000)
for i in range(len(l)):
    sol=integrate.odeint(f_diff,r0[i],t,args=(l[i],)) #args=(l,) serve , perchè deve avere più elementi
    plt.plot(t,sol[:,1],label='omega')
    plt.plot(t,sol[:,0],label='theta')
    plt.xlabel('t')
    plt.grid()
    plt.minorticks_on()
    plt.legend(fontsize = 12, loc = "upper left", frameon=True)
    plt.tight_layout()
    plt.show()

