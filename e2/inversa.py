import pandas as pd
import numpy as np
from scipy import fft
# import datetime as dt
from tqdm import tqdm
#import rielaborazione_dati2 as rd
import matplotlib.pyplot  as plt
import moduli_analisi as ma


s1 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione1_riempita.txt', sep='\t')
s2 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione2_riempita.txt', sep='\t')
s3 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione3_riempita.txt', sep='\t')
s4 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione4_riempita.txt', sep='\t')
california = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_california_riempita.txt', sep='\t')
colorado = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_colorado_riempita.txt', sep='\t')
new_york = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_new_york_riempita.txt', sep='\t')
south_dakota = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_south_dakota_riempita.txt', sep='\t')
texas = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_texas_riempita.txt', sep='\t')
nazione = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_nazione_riempita.txt', sep='\t')

dati = nazione['NO2 Mean'].to_numpy()
tempo = nazione['Date Local'].to_numpy()
date = nazione['Date Local'] #!!
segni_x=[]
j = 0
for i in range(len(nazione)):
    if ((date[i][-1]=='1') and (date[i][-2]=='0')):
        if ((j%2)==0):
            segni_x = np.append(segni_x,date[i])
        j=j+1
segni_x = np.append(segni_x,date.loc[len(date)-1])


filtro = 0.4e-2 #filtro in frequenza 
# filtro =1e5 #filtro in ampiezza

# fourier
coef_f = fft.rfft(dati)
# indici =  np.arange(1,(coef_f.size//2))
indici =  np.arange(0,(coef_f.size//2)) #coef. 0 !!
coef_ps = np.absolute(coef_f[indici])**2
coef_freq_f = 0.5*fft.rfftfreq(coef_f.size, d=1)
plt.plot(coef_freq_f[indici],coef_ps)
# plt.axhline (filtro,color='red',linestyle=':',alpha=0.8) # filtro in ampiezza
plt.axvline (filtro,color='red',linestyle=':',alpha=0.8) #filtro in frequenza
plt.yscale('log')
plt.xscale('log')
plt.show()




# inversa

# maschera = (np.absolute(coef_freq_f)**2 > 0.143) | ((np.absolute(coef_freq_f)**2 > filtro) & (np.absolute(coef_freq_f)**2 < 0.142))#filtro in freq strano
# differenze non tangibili

maschera = np.absolute(coef_freq_f)**2 > filtro #filtro in freq
# maschera = np.absolute(coef_f)**2 < filtro #filtro in ampiezza
filtrato = coef_f[:len(maschera)].copy()
filtrato[maschera] = 0
dati_inversa = fft.irfft(filtrato, n=len(dati))












#grafico temporale
plt.plot(tempo, dati)
plt.xlabel('data [yyyy-mm-dd]')
plt.ylabel('concentrazioni')
#plt.yscale('log')
plt.xticks(segni_x,rotation=30, ha='right')
#plt.legend(fontsize=12, loc = 'best', frameon=True)
plt.grid()
plt.tight_layout()

plt.plot(tempo,dati_inversa)

plt.show()