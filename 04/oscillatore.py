import numpy as np
import scipy
from scipy import integrate
import matplotlib.pyplot as plt
import pandas as pd
#m=k=1
x=np.arange(2,10,0.01)
def t(x0):
    xx=np.arange(0,x0,0.01)
    y=1/((x0**6-xx**6)**0.5)
    periodo=(8**0.5)*scipy.integrate.simpson(y,xx)
    return periodo
T=np.zeros(len(x))
for i in range(len(x)):
    T[i]=t(x[i])
plt.plot(x,T)
plt.show()
