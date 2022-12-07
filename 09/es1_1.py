import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

bins=80 #numero dei bin 
df0=pd.read_csv('/home/gb980061/repo_metodi_computazionali/09/hit_times_M0.csv')
df1=pd.read_csv('/home/gb980061/repo_metodi_computazionali/09/hit_times_M1.csv')
df2=pd.read_csv('/home/gb980061/repo_metodi_computazionali/09/hit_times_M2.csv')
df3=pd.read_csv('/home/gb980061/repo_metodi_computazionali/09/hit_times_M3.csv')
#print(df3.keys())
#print(len(df3['hit_time']))
#istogramma
#plt.hist(df0['hit_time'],bins=bins)
#plt.grid()
#plt.show()
#istogramma log10
mask=(np.diff(df0['hit_time'].values))>0
t_diff=np.diff(df0['hit_time'].values)[mask]
logbins=np.logspace(np.log10(np.min(t_diff)),np.log10(np.max(t_diff)),bins) #larghezza bins log10
plt.hist(t_diff,bins=logbins)
plt.xscale('log')
plt.grid()
plt.show()

