import numpy as np
import scipy
from scipy import integrate
import matplotlib.pyplot as plt
t,v=np.loadtxt('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/03/dati.txt', delimiter=',' , unpack=True)
s=np.zeros(len(t))
for i in range(len(t)-1):
    s[i]=scipy.integrate.simpson(v[0:i+1],t[0:i+1])
s[len(t)-1]=scipy.integrate.simpson(v,t)
plt.plot(t,v,'red')
plt.plot(t,s,'green')
plt.show()

#integrale di una funzione v arbitraria
# t=np.arange(0.1,100,1)
# v=np.ones(len(t))
# s=np.zeros(len(t))
# for i in range(len(t)-1):
#     s[i]=scipy.integrate.simpson(v[0:i+1],t[0:i+1])
# s[len(t)-1]=scipy.integrate.simpson(v,t)
# plt.plot(t,v,'red')
# plt.plot(t,s,'green')
# plt.show()