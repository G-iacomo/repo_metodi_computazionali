import pandas as pd
import numpy as np
from tqdm import tqdm
import warnings
import rielaborazione_dati2 as rd

#!! potevo fare la prima media solo della california e dopo fare la media degli altri stati solo in base alla data.. sarebbe stato più rapido
#!! giustificalo dicendo che valutare giorno per giorno stazione per stazione è meglio per casi negativi ecc (ma la media è additiva..)

##############################################################################################
#   prove

# x=[2,2,10,10,2,10,10,10,10,13]
# y=['a','b','c','e','f','g','h','i','l','m']
# d={'lettera':y,'numero':x}
# df=pd.DataFrame(d)
# a=[2,2,10,10,2,10,10,10,10,13]
# b=['a','b','c','e','f','g','h','i','l','m']
# d2={'lettera':a,'numero':b}
# df2=pd.DataFrame(d2)
# uniti=pd.concat([df,df2],keys=['primo','secondo'],names=['State'])
# uniti.reset_index(inplace=True) #permette di riferirsi alle righe partendo dall'indice 0
# uniti.drop(['level_1'], axis=1, inplace=True) #non serve avere l'indice esplicito in una colonna
# print(uniti)
# start=0 #indice da cui si vuole partire a controllare
# stop_finto=8 #indice a cui ci si vuole fermare -1
# stop=stop_finto+1 #ultimo indice che si vuole controllare incluso
# filtro_lettera='c'
# indici=(df.index[start:stop+1][((df.loc[start:stop,'lettera']).to_numpy()=='c')]).to_numpy() #[] esclude l'utimo indice
# maschera=df['numero']>=10
# print(df)
# print(df[0:1])
# print(df.loc[:0])
# print(indici)
# print(maschera)
# print(df[maschera])
# print(df[indici[0]:indici[-1]+1][df.index[indici[0]:indici[-1]+1].isin(indici)]) #è inutile controllare all'infuori di dove sono gli indici anche se range minore di start:stop



#############################################################################################
#   stati d'interesse

# dati_iniziali = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/progetto/pollution_us_2013_2015.csv')

# stati = np.array([6,8,48,46,36]) # codici degli stati analizzati.
#                         #rispettivamente California, Colorado, Texas, South Dakota, New York
# stati_nome={'california','colorado','texas','south dakota','new york'}
# check = True

# dati = rd.funzione_stati2(dati_iniziali,stati,check)

# # dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/dati_no_medie.txt', sep='\t', na_rep='', index=False)

##############################################################################################
#   medie giornaliere singole stazioni

# dati = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/dati_no_medie.txt', sep='\t')

# print('\ncalcolo delle medie giornaliere:\n')
# medie = rd.medie2(dati)

# # medie.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie.txt', sep='\t', na_rep='', index=False)

##############################################################################################
#   stati singoli & stazioni california

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
#   medie giornaliere stati

california = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/california.txt', sep='\t')
colorado = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/colorado.txt', sep='\t')
new_york = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/new_york.txt', sep='\t')
south_dakota = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/south_dakota.txt', sep='\t')
texas = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/texas.txt', sep='\t')

print('\ncalcolo delle medie giornaliere dei cinque stati:\n')

date = np.unique(california['Date Local'].to_numpy()) #le date contenute in california prese una sola volta in formato numpy
medie_california = pd.DataFrame(columns=['Date Local','NO2 Mean','NO2 AQI','NO2 1st Max Value','O3 Mean','O3 AQI','O3 1st Max Value','SO2 Mean','SO2 AQI','SO2 1st Max Value','CO Mean','CO AQI','CO 1st Max Value'])
for i in tqdm(range(len(date))):
    data=date[i]
    indici_data = rd.selezione_data(california,data)
    medie_california.loc[i]=np.append(data,rd.media_stato(california,indici_data))

date = np.unique(colorado['Date Local'].to_numpy()) #le date contenute in colorado prese una sola volta in formato numpy
medie_colorado = pd.DataFrame(columns=['Date Local','NO2 Mean','NO2 AQI','NO2 1st Max Value','O3 Mean','O3 AQI','O3 1st Max Value','SO2 Mean','SO2 AQI','SO2 1st Max Value','CO Mean','CO AQI','CO 1st Max Value'])
for i in tqdm(range(len(date))):
    data=date[i]
    indici_data = rd.selezione_data(colorado,data)
    medie_colorado.loc[i]=np.append(data,rd.media_stato(colorado,indici_data))

date = np.unique(new_york['Date Local'].to_numpy()) #le date contenute in new_york prese una sola volta in formato numpy
medie_new_york = pd.DataFrame(columns=['Date Local','NO2 Mean','NO2 AQI','NO2 1st Max Value','O3 Mean','O3 AQI','O3 1st Max Value','SO2 Mean','SO2 AQI','SO2 1st Max Value','CO Mean','CO AQI','CO 1st Max Value'])
for i in tqdm(range(len(date))):
    data=date[i]
    indici_data = rd.selezione_data(new_york,data)
    medie_new_york.loc[i]=np.append(data,rd.media_stato(new_york,indici_data))

date = np.unique(south_dakota['Date Local'].to_numpy()) #le date contenute in south_dakota prese una sola volta in formato numpy
medie_south_dakota = pd.DataFrame(columns=['Date Local','NO2 Mean','NO2 AQI','NO2 1st Max Value','O3 Mean','O3 AQI','O3 1st Max Value','SO2 Mean','SO2 AQI','SO2 1st Max Value','CO Mean','CO AQI','CO 1st Max Value'])
for i in tqdm(range(len(date))):
    data=date[i]
    indici_data = rd.selezione_data(south_dakota,data)
    medie_south_dakota.loc[i]=np.append(data,rd.media_stato(south_dakota,indici_data))

date = np.unique(texas['Date Local'].to_numpy()) #le date contenute in texas prese una sola volta in formato numpy
medie_texas = pd.DataFrame(columns=['Date Local','NO2 Mean','NO2 AQI','NO2 1st Max Value','O3 Mean','O3 AQI','O3 1st Max Value','SO2 Mean','SO2 AQI','SO2 1st Max Value','CO Mean','CO AQI','CO 1st Max Value'])
for i in tqdm(range(len(date))):
    data=date[i]
    indici_data = rd.selezione_data(texas,data)
    medie_texas.loc[i]=np.append(data,rd.media_stato(texas,indici_data))

# # medie_california.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_california.txt', sep='\t', na_rep='', index=False)
# # medie_colorado.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_colorado.txt', sep='\t', na_rep='', index=False)
# # medie_new_york.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_new_york.txt', sep='\t', index=False)
# # medie_south_dakota.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_south_dakota.txt', sep='\t', na_rep='', index=False)
# # medie_texas.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_texas.txt', sep='\t', na_rep='', index=False)

##############################################################################################
#   nazione & media giornaliera nazione

# medie_california = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_california.txt', sep='\t')
# medie_colorado = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_colorado.txt', sep='\t')
# medie_new_york = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_new_york.txt', sep='\t')
# medie_south_dakota = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_south_dakota.txt', sep='\t')
# medie_texas = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_texas.txt', sep='\t')

nazione = pd.concat([medie_california, medie_colorado, medie_new_york, medie_south_dakota, medie_texas], keys=['california','colorado','new york','south dakota','texas'], names=['State'] )
nazione.reset_index(inplace=True) #permette di riferirsi alle righe partendo dall'indice 0
# nazione.drop(['level_1','Unnamed: 0'], axis=1, inplace=True) #non serve avere l'indice esplicito in una colonna
nazione.drop(['level_1'], axis=1, inplace=True) #non serve avere l'indice esplicito in una colonna
print(nazione)

print('\ncalcolo delle medie giornaliere nazionali:\n')

date = np.unique(nazione['Date Local'].to_numpy()) #le date contenute in california prese una sola volta in formato numpy
medie_nazione = pd.DataFrame(columns=['Date Local','NO2 Mean','NO2 AQI','NO2 1st Max Value','O3 Mean','O3 AQI','O3 1st Max Value','SO2 Mean','SO2 AQI','SO2 1st Max Value','CO Mean','CO AQI','CO 1st Max Value'])
for i in tqdm(range(len(date))):
    data=date[i]
    indici_data = rd.selezione_data(nazione,data)
    medie_nazione.loc[i]=np.append(data,rd.media_stato(nazione,indici_data))

# nazione.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/nazione.txt', sep='\t', na_rep='', index=False)
# medie_nazione.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_nazione.txt', sep='\t', na_rep='', index=False)