import moduli_residui as mr
import numpy as np
import pandas as pd

esemplificativi = True #default=True. per visualizzare tutti i grafici False. 
    # WARNING: 140 grafici totali


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


if esemplificativi==False:
    inquinanti = ['NO2 Mean','O3 Mean','SO2 Mean','CO Mean']
    stati=[california,colorado,new_york,south_dakota,texas]
    nomi_stati = ['california','colorado','new_york','south_dakota','texas']
    stazioni=[s1,s2,s3,s4]
    nomi_stazioni=['Los Angeles (LAC)','Not a city (HUM)','Calexico (IMP)','San Pablo (CC)']
else:
    inquinanti = ['NO2 Mean']
    stati=[california]
    nomi_stati = ['california']
    stazioni=[s1]
    nomi_stazioni=['Los Angeles (LAC)']



inquinanti = ['NO2 Mean','O3 Mean','SO2 Mean','CO Mean']


print('\n\nnazione')
filtro_freq=np.array([4e-3,4e-3,7e-3,0.57e-2])
filtro_amp=np.array([1e5,0.2,1e3,40])
for i in range(len(inquinanti)):
    mr.inversa(nazione,inquinanti[i],filtro_freq[i],filtro_amp[i])