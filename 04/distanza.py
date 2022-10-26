import numpy as np
import scipy
from scipy import integrate
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('/home/gb980061/repo_metodi_computazionali/04/vel_vs_time.csv')
s=np.zeros(len(df['t']))
for i in range(len(df['t'])-1):                                                                                                                                      
    s[i]=scipy.integrate.simpson(df['v'][0:i+1],df['t'][0:i+1])
s[len(df['t'])-1]=scipy.integrate.simpson(df['v'],df['t'])
plt.plot(df['t'],df['v'],'red')
plt.plot(df['t'],s,'green')
'''
t=df['t']
v=df['v']
s=np.zeros(len(t))
for i in range(len(t)-1):
    s[i]=scipy.integrate.simpson(v[0:i+1],t[0:i+1])
s[len(t)-1]=scipy.integrate.simpson(v,t)
plt.plot(t,v,'red')
plt.plot(t,s,'green')
'''
plt.show()
