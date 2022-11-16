import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy import fft
import pandas as pd
#importo
d1=pd.read_csv('/home/gb980061/repo_metodi_computazionali/06/data_sample1.csv')
d2=pd.read_csv('/home/gb980061/repo_metodi_computazionali/06/data_sample2.csv')
d3=pd.read_csv('/home/gb980061/repo_metodi_computazionali/06/data_sample3.csv')
#grafici dati
plt.plot(d1['time'],d1['meas'], color= 'grey')
plt.plot(d2['time'],d2['meas'], color= 'pink')
plt.plot(d3['time'],d3['meas'], color= 'red')
plt.xlabel('t')
plt.ylabel('misure')
plt.grid()
plt.minorticks_on()
plt.tight_layout()
plt.show()
#fft
f1=fft.rfft(d1['meas'].values)
freq1=0.5*fft.rfftfreq(len(f1),d=1)
plt.plot(freq1[20:len(f1)//2],np.absolute(f1[20:len(f1)//2])**2, color='grey')
f2=fft.rfft(d2['meas'].values)
freq2=0.5*fft.rfftfreq(len(f2),d=1)
plt.plot(freq2[20:len(f2)//2],np.absolute(f2[20:len(f2)//2])**2, color='pink')
f3=fft.rfft(d3['meas'].values)
freq3=0.5*fft.rfftfreq(len(f3),d=1)
plt.plot(freq3[20:len(f3)//2],np.absolute(f3[20:len(f3)//2])**2, color='red')
#funzione fit
def f_fit(f,b,a):
    return a*(f**-b)
par=[1,-1]
par,parcov=optimize.curve_fit(f_fit,freq1[20:len(f1)//2],np.absolute(f1[20:len(f1)//2])**2,p0=[par], absolute_sigma=True)
for i in range(len(par)):
    print ('grey:',par[i],'+/-', np.sqrt(parcov[i][i]))
plt.plot(freq1[20:len(f1)//2],f_fit(freq1[20:len(f1)//2],par[0],par[1]),color='green')
par,parcov=optimize.curve_fit(f_fit,freq2[20:len(f2)//2],np.absolute(f2[20:len(f2)//2])**2,p0=[par], absolute_sigma=True)
for i in range(len(par)):
    print ('pink:',par[i],'+/-', np.sqrt(parcov[i][i]))
plt.plot(freq2[20:len(f2)//2],f_fit(freq2[20:len(f2)//2],par[0],par[1]),color='green')
par,parcov=optimize.curve_fit(f_fit,freq3[20:len(f3)//2],np.absolute(f3[20:len(f3)//2])**2,p0=[par], absolute_sigma=True)
for i in range(len(par)):
    print ('red:',par[i],'+/-', np.sqrt(parcov[i][i]))
plt.plot(freq3[20:len(f3)//2],f_fit(freq3[20:len(f3)//2],par[0],par[1]),color='green')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('f')
plt.ylabel('trasformate')
plt.grid()
plt.minorticks_on()
plt.tight_layout()
plt.show()
