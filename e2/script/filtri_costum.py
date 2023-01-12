import moduli_filtri_costum as mc
import numpy as np
import pandas as pd

#filtri modificabili più facilmente
#i valori dei filtri sono validi solo per i grafici prodotti con esemplificativi=True
#possibilità di filtrare anche in base al modulo delle ampiezze^2 dei coefficenti 


filtrare_ampiezza = True

esemplificativi = True #default=True. per visualizzare tutti i grafici False. 
    # WARNING: se false molti grafici
    # valori filtri potenzialmente non corretti pse False
print('\n\neseplificativi: {}'.format(esemplificativi)+'\n\nWARNING: se false molti grafici\n')



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
    stati=[california,colorado,new_york,south_dakota,texas]
    nomi_stati = ['california','colorado','new_york','south_dakota','texas']
    stazioni=[s1,s2,s3,s4]
    nomi_stazioni=['Los Angeles (LAC)','Not a city (HUM)','Calexico (IMP)','San Pablo (CC)']
else:
    stati=[california]
    nomi_stati = ['california']
    stazioni=[s1]
    nomi_stazioni=['Los Angeles (LAC)']

inquinanti = ['NO2 Mean','O3 Mean','SO2 Mean','CO Mean']

##########################################################
#   nazione
print('\n\nnazione')
filtro_freq=np.array([7e-3,7e-3,7e-3,7e-3])
if filtrare_ampiezza==True:
    filtro_amp=np.array([1e5,0.2,1e3,40])
else:
    filtro_amp=np.array([np.nan,np.nan,np.nan,np.nan])
for i in range(len(inquinanti)):
    mc.inversa(nazione,inquinanti[i],filtro_freq[i],filtro_amp[i])

#############################################
#   stazioni/città
for j in range(len(stazioni)):
    print('\n\n'+nomi_stazioni[j])
    filtro_freq=np.array([7e-3,7e-3,7e-3,7e-3])
    if filtrare_ampiezza==True:
     filtro_amp=np.array([1e6,0.5,1e3,5e2])
    else:
        filtro_amp=np.array([np.nan,np.nan,np.nan,np.nan])
    for i in range(len(inquinanti)):
        mc.inversa(stazioni[j],inquinanti[i],filtro_freq[i],filtro_amp[i])

