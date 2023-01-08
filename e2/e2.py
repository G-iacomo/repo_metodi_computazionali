import pandas as pd
import numpy as np
from tqdm import tqdm
import warnings
import rielaborazione_dati2 as rd

##############################################################################################

# x=[2,2,10,10,2,10,10,10,10,13]
# y=['a','b','c','e','f','g','h','i','l','m']
# d={'lettera':y,'numero':x}
# df=pd.DataFrame(d)
# start=0 #indice da cui si vuole partire a controllare
# stop_finto=8 #indice a cui ci si vuole fermare -1
# stop=stop_finto+1 #ultimo indice che si vuole controllare incluso
# indici=(df.index[start:stop+1][((df.loc[start:stop,'numero']).to_numpy()%2==0)]).to_numpy() #[] esclude l'utimo indice
# maschera=df['numero']>=10
# print(df)
# print(df[0:1])
# print(df.loc[:0])
# print(indici)
# print(maschera)
# print(df[maschera])
# print(df[indici[0]:indici[-1]+1][df.index[indici[0]:indici[-1]+1].isin(indici)]) #è inutile controllare all'infuori di dove sono gli indici anche se range minore di start:stop



#############################################################################################

# dati_iniziali = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/progetto/pollution_us_2013_2015.csv')

# stati = np.array([6,8,48,46,36]) # codici degli stati analizzati.
#                         #rispettivamente California, Colorado, Texas, South Dakota, New York
# stati_nome={'california','colorado','texas','south dakota','new york'}
# check = False
# dati = rd.funzione_stati2(dati_iniziali,stati,check)

# # dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/dati_no_medie.txt', sep='\t', na_rep='', index=False)

##############################################################################################

# dati = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/dati_no_medie.txt', sep='\t')

# medie = rd.medie2(dati)

# # medie.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie.txt', sep='\t', na_rep='', index=False)

##############################################################################################

# medie = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie.txt', sep='\t')

# indici_california = rd.selezione_stato(medie,6)
# california = rd.dataframe_filtrato(medie,indici_california)

# indici_colorado = rd.selezione_stato(medie,8)
# colorado = rd.dataframe_filtrato(medie,indici_colorado)

# indici_new_york = rd.selezione_stato(medie,36)
# new_york = rd.dataframe_filtrato(medie,indici_new_york)

# indici_south_dakota = rd.selezione_stato(medie,46)
# south_dakota = rd.dataframe_filtrato(medie,indici_south_dakota)

# indici_texas = rd.selezione_stato(medie,48)
# texas = rd.dataframe_filtrato(medie,indici_texas)

# indici_stazione1 = rd.selezione_stazioni(california,1103)
# stazione1 = rd.dataframe_filtrato(california,indici_stazione1)

# indici_stazione2 = rd.selezione_stazioni(california,1005)
# stazione2 = rd.dataframe_filtrato(california,indici_stazione2)

# indici_stazione3 = rd.selezione_stazioni(california,5)
# stazione3 = rd.dataframe_filtrato(california,indici_stazione3)

# indici_stazione4 = rd.selezione_stazioni(california,1004)
# stazione4 = rd.dataframe_filtrato(california,indici_stazione4)

# # california.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/california.txt', sep='\t', na_rep='', index=False)
# # colorado.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/colorado.txt', sep='\t', na_rep='', index=False)
# # new_york.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/new_york.txt', sep='\t', na_rep='', index=False)
# # south_dakota.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/south_dakota.txt', sep='\t', na_rep='', index=False)
# # texas.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/texas.txt', sep='\t', na_rep='', index=False)


##############################################################################################

california = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/california.txt', sep='\t')

