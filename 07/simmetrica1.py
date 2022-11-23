#stampa il cammino di n random walker per tot passi
import numpy as np
import matplotlib.pyplot as plt
import sys
s=1 #modulo lunghezza 1 passo
n=5 #numero di random walker
passi=100
def spostamenti(p): #p=numero di passi
    x=np.zeros(1)
    y=np.zeros(1)
    theta=np.random.uniform(low=0.0, high=2*np.pi,size=p)
    x=(s*np.cos(theta))
    y=(s*np.sin(theta))
    return x,y #attenzione ritorna una tuple
xx=np.zeros(passi)
yy=np.zeros(passi)
for j in range (n):
    (x,y)=spostamenti(passi+1)
    for i in range(passi):
        xx[i]=np.sum(x[:i]) #somma di ogni spostamento cioè la posizione totale                                                                                                           
        yy[i]=np.sum(y[:i])
    plt.plot(xx,yy,linestyle='-', marker='.')
plt.grid()
plt.legend(loc="upper left")
plt.show()