import rielaborazione_dati as rd
import pandas as pd
import numpy as np
#from tqdm import tqdm
#import statistics as st

#df=pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/.txt',sep='\t')

dati=rd.funzione_stati()

print(dati)
#dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/dati.csv', sep=',', index=False)
#dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/dati.txt', sep='\t', na_rep='', index=False)

#dati=rd.funzione_medie(dati)

#dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/medie.csv', sep=',', index=False)
#dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/medie.txt', sep='\t', na_rep='', index=False)

# df=pd.DataFrame({'numero':[0,1,2,3],'lettera':['a','b','c','d']})
# indici=(i in ['a','b'] for i in df['lettera'])
# print(np.nanmean(df.loc[0:2,'numero']))