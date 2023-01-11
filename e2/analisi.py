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

##################################################################################
# confronto temporale

def confronto_temporale():
    multi_grafici = True #true se si vogliono molteplici singoli grafici di maggiori dimensioni.
    print('\nconfronto temporale delle stazioni californiane selezionate, inquinante per inquinante:\n')
    ma.stazioni_temporale(multi_grafici)
    print('\nconfronto temporale degli stati selezionati, inquinante per inquinante:\n')
    ma.stati_temporale(multi_grafici)
    print('\nconfronto temporale degli stati selezionati:\nATTENZIONE: i dati sono stati moltiplicati a fini grafici; riferirsi alla legenda')
    ma.nazione_temporale()










confronto_temporale()
ma.spettro_nazione()
ma.spettro_stati()
ma.spettro_stazioni()
