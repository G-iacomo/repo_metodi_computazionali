import pandas as pd
import numpy as np
#from tqdm import tqdm
#import rielaborazione_dati2 as rd
from scipy import fft
import matplotlib.pyplot  as plt

stazione1 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione1.txt', sep='\t')
stazione2 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione2.txt', sep='\t')
stazione3 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione3.txt', sep='\t')
stazione4 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione4.txt', sep='\t')
# medie_california = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_california.txt', sep='\t')
# medie_colorado = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_colorado.txt', sep='\t')
# medie_new_york = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_new_york.txt', sep='\t')
# medie_south_dakota = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_south_dakota.txt', sep='\t')
# medie_texas = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_texas.txt', sep='\t')
# medie = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie.txt', sep='\t')
# california = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/california.txt', sep='\t')
# colorado = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/colorado.txt', sep='\t')
# new_york = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/new_york.txt', sep='\t')
# south_dakota = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/south_dakota.txt', sep='\t')
# texas = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/texas.txt', sep='\t')

print(stazione1.loc[0,'Date Local'])
print(stazione2.loc[0,'Date Local'])
print(stazione3.loc[0,'Date Local'])
print(stazione4.loc[0,'Date Local'])
print(stazione1.loc[len(stazione1)-1,'Date Local'])
print(stazione2.loc[len(stazione2)-1,'Date Local'])
print(stazione3.loc[len(stazione3)-1,'Date Local'])
print(stazione4.loc[len(stazione4)-1,'Date Local'])

print(len(stazione1))
print(len(stazione2))
print(len(stazione3))
print(len(stazione4))


plt.plot(stazione1['Date Local'],stazione1['SO2 Mean'], label='Los Angeles (LAC)')
# plt.plot(stazione2['Date Local'],stazione1['NO2 Mean'], label='Not a city (HUM)')
# plt.plot(stazione3['Date Local'],stazione1['NO2 Mean'], label='Calexico (IMP)')
# plt.plot(stazione4['Date Local'],stazione1['NO2 Mean'], label='San Pablo (CC)')
plt.xlabel('data [yyyy-mm-dd]')
plt.ylabel(r'NO2 medio [$10^{-6}$]')
segni_x=[]
for i in range(0,len(stazione1),100):
    segni_x = np.append(segni_x,stazione1.loc[i,'Date Local'])
plt.xticks(segni_x,rotation=30)
plt.legend(fontsize=14)
plt.grid()
plt.minorticks_on
plt.tight_layout()
plt.show()