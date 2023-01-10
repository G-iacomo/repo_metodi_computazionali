import pandas as pd
import numpy as np
#from tqdm import tqdm
#import rielaborazione_dati2 as rd
from scipy import fft
import matplotlib.pyplot  as plt
import datetime as dt

s1 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione1_riempita.txt', sep='\t')
s2 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione2_riempita.txt', sep='\t')
s3 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione3_riempita.txt', sep='\t')
s4 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione4_riempita.txt', sep='\t')
# california = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_california_riempita.txt', sep='\t')
# colorado = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_colorado_riempita.txt', sep='\t')
# new_york = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_new_york_riempita.txt', sep='\t')
# south_dakota = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_south_dakota_riempita.txt', sep='\t')
# texas = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_texas_riempita.txt', sep='\t')
# nazione = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_nazione_riempita.txt', sep='\t')


inquinanti = ['NO2 Mean','O3 Mean','SO2 Mean','CO Mean']
etichette = [r'NO2 medio [$10^{-9}$]',r'O3 medio [$10^{-6}$]',r'SO2 medio [$10^{-9}$]',r'CO medio [$10^{-6}$]']

def stazioni(inquinante,etichetta):
    date = s1['Date Local']
    plt.plot(date,s1[inquinante], label='Los Angeles (LAC)')
    plt.plot(date,s2[inquinante], label='Not a city (HUM)')
    plt.plot(date,s3[inquinante], label='Calexico (IMP)')
    plt.plot(date,s4[inquinante], label='San Pablo (CC)')
    plt.xlabel('data [yyyy-mm-dd]')
    plt.ylabel(etichetta)
    segni_x=[]
    for i in range(0,len(s1),100):
        segni_x = np.append(segni_x,date[i])
    plt.xticks(segni_x,rotation=30)
    plt.legend(fontsize = 12, loc = 'best', frameon=True)
    plt.grid()
    plt.minorticks_on
    plt.tight_layout()
    plt.show()

for i in range(len(inquinanti)):
    stazioni(inquinanti[i],etichette[i])