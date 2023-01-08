import rielaborazione_dati as rd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import warnings
#import statistics as st
pd.set_option('display.max_columns', 500) #il numero di colonne massime da stampare

#dati=pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/medie.txt',sep='\t')
#dati_iniziali = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/progetto/pollution_us_2013_2015.csv')
dati=pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/dati.txt',sep='\t') #no dati iniziali


#dati=rd.funzione_stati()
#dati=rd.funzione_medie(dati)
#dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/medie.txt', sep='\t', na_rep='', index=False)

medie2 = rd.funzione_medie2(dati)
