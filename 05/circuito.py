import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def Vi(t):
    if int(t)%2==0:
        return 1
    else:
        return -1

def f_diff(Vo,t,Vi,rc):
    return (Vi(t)-Vo)/rc

rc=[1,0.1]
color=['blue','green']
t=np.linspace(0,10,1000)

Vo=np.zeros(len(t))
Vi_plot=np.zeros(len(t))
for i in range(len(t)):
    Vi_plot[i]=(Vi(t[i]))
for i in range(len(rc)):
    Vo=integrate.odeint(f_diff,Vo[0],t,args=(Vi,rc[i]))
    plt.plot(t,Vo,color=color[i],label='output rc={:}'.format(rc[i]))
plt.plot(t,Vi_plot,color='red',label='input')
plt.xlabel('t')
plt.ylabel('Volt')
plt.grid()
plt.minorticks_on()
plt.legend(fontsize = 12, loc = "upper left", frameon=True)
plt.tight_layout()
plt.show()
