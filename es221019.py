import numpy as np
import scipy
from scipy import integrate
import matplotlib.pyplot as plt
t=np.arange(-5,5,0.5)
v=np.ones(20)
s=np.zeros(20)
for i in range(len(t)):
    v[i]=(t[i]**2)-2
    s[i]=scipy.integrate.simpson(v,t)
#plt.plot(t,v)
#plt.show()
for i in range(len(t)):
    print (s[i])
plt.plot(t,s)
plt.show()
