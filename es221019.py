import numpy as np
import matplotlib.pyplot as plt
t=np.arange(-5,5,0.5)
v=np.ones(20)
for i in range(len(t)):
    #print (t[i])
    v[i]=(t[i]**2)-2
    #print (v[i])
plt.plot(t,v)
plt.show()
