import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy
import pandas as pd
s=1
n=5 #numero di random walker
def random(passi):
    x=np.zeros(1)
    y=np.zeros(1)
    theta=np.random.uniform(low=0.0, high=2*np.pi, size=passi)
    x=np.sum(s*np.cos(theta))
    y=np.sum(s*np.sin(theta))
    return x,y
x=np.zeros(n)
y=np.zeros(n)
for i in range(n-1):
    x[i],y[i]=random(10)
    plt.plot(x,y,'o')
plt.show()
    
