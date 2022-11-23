#programma che stampa il cammino 2d di un random walker. inutilmente complicato

import numpy as np
import matplotlib.pyplot as plt
import sys
s=1 #modulo passo
passimax=200 #il massimo numero di passi che voglio
def spostamento(): #quanto cammino ogni passo
    theta=np.random.uniform(low=0.0, high=2*np.pi, size=1000)
    x=s*np.cos(theta)
    y=s*np.sin(theta)
    return x,y
xx=np.zeros(passimax) #conterrà la posizione dopo i-indicesimo passo di x
yy=np.zeros(passimax)
passi=np.array([passimax,100,10])
x,y=spostamento()
color=(['red','green','pink'])
for i in range(passimax):
    xx[i]=np.sum(x[:i]) #somma di ogni spostamento cioè la posizione totale                                                                                                           
    yy[i]=np.sum(y[:i])
for j in range(len(passi)): #stampa il cammino fino al passo iesimo letto in ordine inverso
    plt.plot(xx[0:passi[j]],yy[0:passi[j]],linestyle='-', marker='.',color=color[j])
plt.grid(True)
plt.show()

    
