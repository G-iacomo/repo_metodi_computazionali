import e
import pandas as pd
#import numpy as np
#from tqdm import tqdm
#import statistics as st

#df=pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/medie_temporanee.txt',sep='\t')

dati=e.funzione_stati()

#dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/dati.csv', sep=',', index=False)
#dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/dati.txt', sep='\t', na_rep='', index=False)

dati=e.funzione_medie(dati)

#dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/medie.csv', sep=',', index=False)
#dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/medie.txt', sep='\t', na_rep='', index=False)
