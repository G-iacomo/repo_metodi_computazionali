#cammino di n random walker con propabilità asimmetrica
import numpy as np
import matplotlib.pyplot as plt
import sys
'''
def cumulativa(theta):
    y=(1-np.cos(theta/2))/2
    return y
'''
n=5 #numero di random walker
s=1
passi=100
def inversa(yy):
    xx=2*np.arccos(1-2*yy)
    return xx
#plt.hist(inversa(yy),bins=100,range=(0,10))
#plt.show()
def random(yy):
    x=np.zeros(1)
    y=np.zeros(1)
    x=s*np.cos(inversa(yy))
    y=s*np.sin(inversa(yy))
    return x,y
x=np.zeros(n)
y=np.zeros(n)
xx=np.zeros(passi)
zz=np.zeros(passi)
for j in range(n):
    yy=np.random.random(passi)
    x,y=random(yy)
    for i in range(passi):
        xx[i]=np.sum(x[:i]) #somma di ogni spostamento cioè la posizione totale                                                                                                           
        zz[i]=np.sum(y[:i])
    plt.plot(xx,zz,linestyle='-', marker='.')
plt.grid()
plt.show()
