import pandas as pd
import numpy as np
from scipy import fft
# import datetime as dt
#from tqdm import tqdm
#import rielaborazione_dati2 as rd
import matplotlib.pyplot  as plt
import moduli_inversa as mi


esemplificativi = True #default=True. per visualizzare tutti i grafici realizzabili False. 
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

################################
#   inversa nazione 

print('\nricostruzione attraverso l\'inversa dei dati nazionali\nfiltri a frequenze [1/d]:'+ '4e-3 e 7e-3')
for inquinante in inquinanti:
    mi.inversa(nazione, inquinante)

################################
#   inversa stati

print('\nricostruzione attraverso l\'inversa dei dati statali\nfiltri a frequenze [1/d]:'+ '4e-3 e 7e-3')
for j in range(len(stati)):
    print('\n\n'+nomi_stati[j])
    for inquinante in inquinanti:
        mi.inversa(stati[j], inquinante)

###############################
#   inversa stazioni

print('\nricostruzione attraverso l\'inversa dei dati locali\nfiltri a frequenze [1/d]:'+ '4e-3 e 7e-3')
for j in range(len(stazioni)):
    print('\n\n'+nomi_stazioni[j])
    for inquinante in inquinanti:
        mi.inversa(stazioni[j], inquinante)