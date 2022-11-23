#programma che stampa le posizioni (finali) dopo tot passi di n random walker

import numpy as np
import matplotlib.pyplot as plt
import sys
s=1 #modulo lunghezza 1 passo
n=100 #numero di random walker
passi=[10,100]
def random(p): #p=numero di passi
    x=np.zeros(1)
    y=np.zeros(1)
    theta=np.random.uniform(low=0.0, high=2*np.pi, size=p)
    x=np.sum(s*np.cos(theta))
    y=np.sum(s*np.sin(theta))
    return x,y #attenzione ritorna una tuple
x=np.zeros(n)
y=np.zeros(n)
for j in range (len(passi)):
    for i in range(n):
        x[i],y[i]=random(passi[j])
    plt.plot(x,y,'.',label='passo {}'.format(passi[j]))
plt.grid()
plt.legend(loc="upper left")
plt.show()

    
