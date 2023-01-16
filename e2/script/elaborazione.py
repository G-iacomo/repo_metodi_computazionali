import pandas as pd
import numpy as np
from tqdm import tqdm
import moduli_elaborazione as me

######################################################################################
#   parametri modificabili
salvataggio=True #default=True, salva i dati elaborati finali necessari ai successivi file 
check = True #se true esegue piccoli controlli durante la prima parte della rielaborazione dei dati
path = '' #percorso alla cartella di lavoro                                                                                                             /home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/script/
    # è possibile lasciare la stringa vuota

#############################################################################################
#   stati d'interesse

dati_iniziali = pd.read_csv(path+'/pollution_us_2013_2015.csv')
stati = np.array([6,8,48,46,36]) # codici degli stati analizzati.
                        #rispettivamente California, Colorado, Texas, South Dakota, New York
stati_nome={'california','colorado','texas','south dakota','new york'}

dati = me.funzione_stati2(dati_iniziali,stati,check)

# # dati.to_csv(path+'/dati_no_medie.txt', sep='\t', na_rep='', index=False)
##############################################################################################
#   medie giornaliere singole stazioni
# dati = pd.read_csv(path+'/dati_no_medie.txt', sep='\t')

print('\ncalcolo delle medie giornaliere:\n')
medie = me.medie2(dati)

# # medie.to_csv(path+'/medie.txt', sep='\t', na_rep='', index=False)
##############################################################################################
#   stati singoli & stazioni california
# medie = pd.read_csv(path+'/medie.txt', sep='\t')

indici_california = me.selezione_stato(medie,6)
california = me.dataframe_filtrato(medie,indici_california)

indici_colorado = me.selezione_stato(medie,8)
colorado = me.dataframe_filtrato(medie,indici_colorado)

indici_new_york = me.selezione_stato(medie,36)
new_york = me.dataframe_filtrato(medie,indici_new_york)

indici_south_dakota = me.selezione_stato(medie,46)
south_dakota = me.dataframe_filtrato(medie,indici_south_dakota)

indici_texas = me.selezione_stato(medie,48)
texas = me.dataframe_filtrato(medie,indici_texas)

indici_stazione1 = me.selezione_indirizzo(california,'1630 N MAIN ST, LOS ANGELES') #site num=1103 univoco ma non usato per uniformità
stazione1 = me.dataframe_filtrato(california,indici_stazione1)
if any(stazione1['City']!='Los Angeles')==True:
    print(r'CHECK: La selezione della stazione 1 è ambigua')

indici_stazione2 = me.selezione_indirizzo(california,'170 meters SE of Donna Dr. & Humboldt Hill Rd., Eureka, CA') #site num=1005 univoco ma non usato per uniformità
stazione2 = me.dataframe_filtrato(california,indici_stazione2)
if any(stazione2['City']!='Not in a city')==True:
    print(r'CHECK: La selezione della stazione 2 è ambigua')

indici_stazione3 = me.selezione_indirizzo(california,'1029 ETHEL ST, CALEXICO HIGH SCHOOL') #site num causa ambiguità. 'Site Num'=5 non univoco con indirizzo e/o contea e/o città
stazione3 = me.dataframe_filtrato(california,indici_stazione3)
if any(stazione3['City']!='Calexico')==True:
    print(r'CHECK: La selezione della stazione 3 è ambigua')

indici_stazione4 = me.selezione_indirizzo(california,'1865 D RUMRILL BLVD, San Pablo') #site num causa ambiguità. 'Site Num'=1004 non univoco con indirizzo e/o contea e/o città
stazione4 = me.dataframe_filtrato(california,indici_stazione4)
if any(stazione4['City']!='San Pablo')==True:
    print(r'CHECK: La selezione della stazione 4 è ambigua')


# # stazione1.to_csv(path+'/stazione1.txt', sep='\t', na_rep='', index=False)
# # stazione2.to_csv(path+'/stazione2.txt', sep='\t', na_rep='', index=False)
# # stazione3.to_csv(path+'/stazione3.txt', sep='\t', na_rep='', index=False)
# # stazione4.to_csv(path+'/stazione4.txt', sep='\t', na_rep='', index=False)
# # california.to_csv(path+'/california.txt', sep='\t', na_rep='', index=False)
# # colorado.to_csv(path+'/colorado.txt', sep='\t', na_rep='', index=False)
# # new_york.to_csv(path+'/new_york.txt', sep='\t', na_rep='', index=False)
# # south_dakota.to_csv(path+'/south_dakota.txt', sep='\t', na_rep='', index=False)
# # texas.to_csv(path+'/texas.txt', sep='\t', na_rep='', index=False)
##############################################################################################
#   medie giornaliere stati
# stazione1 = pd.read_csv(path+'/stazione1.txt', sep='\t')
# stazione2 = pd.read_csv(path+'/stazione2.txt', sep='\t')
# stazione3 = pd.read_csv(path+'/stazione3.txt', sep='\t')
# stazione4 = pd.read_csv(path+'/stazione4.txt', sep='\t')
# california = pd.read_csv(path+'/california.txt', sep='\t')
# colorado = pd.read_csv(path+'/colorado.txt', sep='\t')
# new_york = pd.read_csv(path+'/new_york.txt', sep='\t')
# south_dakota = pd.read_csv(path+'/south_dakota.txt', sep='\t')
# texas = pd.read_csv(path+'/texas.txt', sep='\t')


print('\ncalcolo delle medie giornaliere dei cinque stati:\n')
date = np.unique(california['Date Local'].to_numpy()) #le date contenute in california prese una sola volta in formato numpy
medie_california = pd.DataFrame(columns=['Date Local','NO2 Mean','NO2 AQI','NO2 1st Max Value','O3 Mean','O3 AQI','O3 1st Max Value','SO2 Mean','SO2 AQI','SO2 1st Max Value','CO Mean','CO AQI','CO 1st Max Value'])
for i in tqdm(range(len(date))):
    data=date[i]
    indici_data = me.selezione_data(california,data)
    medie_california.loc[i,'Date Local'] = data
    medie_california.iloc[i,1:] = me.media_stato(california,indici_data)

date = np.unique(colorado['Date Local'].to_numpy()) #le date contenute in colorado prese una sola volta in formato numpy
medie_colorado = pd.DataFrame(columns=['Date Local','NO2 Mean','NO2 AQI','NO2 1st Max Value','O3 Mean','O3 AQI','O3 1st Max Value','SO2 Mean','SO2 AQI','SO2 1st Max Value','CO Mean','CO AQI','CO 1st Max Value'])
for i in tqdm(range(len(date))):
    data=date[i]
    indici_data = me.selezione_data(colorado,data)
    medie_colorado.loc[i,'Date Local'] = data
    medie_colorado.iloc[i,1:] = me.media_stato(colorado,indici_data)

date = np.unique(new_york['Date Local'].to_numpy()) #le date contenute in new_york prese una sola volta in formato numpy
medie_new_york = pd.DataFrame(columns=['Date Local','NO2 Mean','NO2 AQI','NO2 1st Max Value','O3 Mean','O3 AQI','O3 1st Max Value','SO2 Mean','SO2 AQI','SO2 1st Max Value','CO Mean','CO AQI','CO 1st Max Value'])
for i in tqdm(range(len(date))):
    data=date[i]
    indici_data = me.selezione_data(new_york,data)
    medie_new_york.loc[i,'Date Local'] = data
    medie_new_york.iloc[i,1:] = me.media_stato(new_york,indici_data)

date = np.unique(south_dakota['Date Local'].to_numpy()) #le date contenute in south_dakota prese una sola volta in formato numpy
medie_south_dakota = pd.DataFrame(columns=['Date Local','NO2 Mean','NO2 AQI','NO2 1st Max Value','O3 Mean','O3 AQI','O3 1st Max Value','SO2 Mean','SO2 AQI','SO2 1st Max Value','CO Mean','CO AQI','CO 1st Max Value'])
for i in tqdm(range(len(date))):
    data=date[i]
    indici_data = me.selezione_data(south_dakota,data)
    medie_south_dakota.loc[i,'Date Local'] = data
    medie_south_dakota.iloc[i,1:] = me.media_stato(south_dakota,indici_data)

date = np.unique(texas['Date Local'].to_numpy()) #le date contenute in texas prese una sola volta in formato numpy
medie_texas = pd.DataFrame(columns=['Date Local','NO2 Mean','NO2 AQI','NO2 1st Max Value','O3 Mean','O3 AQI','O3 1st Max Value','SO2 Mean','SO2 AQI','SO2 1st Max Value','CO Mean','CO AQI','CO 1st Max Value'])
for i in tqdm(range(len(date))):
    data=date[i]
    indici_data = me.selezione_data(texas,data)
    medie_texas.loc[i,'Date Local'] = data
    medie_texas.iloc[i,1:] = me.media_stato(texas,indici_data)

# # medie_california.to_csv(path+'/medie_california.txt', sep='\t', na_rep='', index=False)
# # medie_colorado.to_csv(path+'/medie_colorado.txt', sep='\t', na_rep='', index=False)
# # medie_new_york.to_csv(path+'/medie_new_york.txt', sep='\t', na_rep='', index=False)
# # medie_south_dakota.to_csv(path+'/medie_south_dakota.txt', sep='\t', na_rep='', index=False)
# # medie_texas.to_csv(path+'/medie_texas.txt', sep='\t', na_rep='', index=False)
##############################################################################################
#   nazione & media giornaliera nazione
# medie_california = pd.read_csv(path+'/medie_california.txt', sep='\t')
# medie_colorado = pd.read_csv(path+'/medie_colorado.txt', sep='\t')
# medie_new_york = pd.read_csv(path+'/medie_new_york.txt', sep='\t')
# medie_south_dakota = pd.read_csv(path+'/medie_south_dakota.txt', sep='\t')
# medie_texas = pd.read_csv(path+'/medie_texas.txt', sep='\t')


nazione = pd.concat([medie_california, medie_colorado, medie_new_york, medie_south_dakota, medie_texas], keys=['california','colorado','new york','south dakota','texas'], names=['State'] )
nazione.reset_index(inplace=True) #permette di riferirsi alle righe partendo dall'indice 0
nazione.drop(['level_1'], axis=1, inplace=True) #non serve avere l'indice esplicito in una colonna
print('\ncalcolo delle medie giornaliere nazionali:\n')
date = np.unique(nazione['Date Local'].to_numpy()) #le date contenute in california prese una sola volta in formato numpy
medie_nazione = pd.DataFrame(columns=['Date Local','NO2 Mean','NO2 AQI','NO2 1st Max Value','O3 Mean','O3 AQI','O3 1st Max Value','SO2 Mean','SO2 AQI','SO2 1st Max Value','CO Mean','CO AQI','CO 1st Max Value'])
for i in tqdm(range(len(date))):
    data=date[i]
    indici_data = me.selezione_data(nazione,data)
    medie_nazione.loc[i]=np.append(data,me.media_stato(nazione,indici_data))



# # nazione.to_csv(path+'/nazione.txt', sep='\t', na_rep='', index=False)
# # medie_nazione.to_csv(path+'/medie_nazione.txt', sep='\t', na_rep='', index=False)
###############################################################
#   riempo i giorni mancanti solo dove serve:
# medie_california = pd.read_csv(path+'/medie_california.txt', sep='\t')
# medie_colorado = pd.read_csv(path+'/medie_colorado.txt', sep='\t')
# medie_new_york = pd.read_csv(path+'/medie_new_york.txt', sep='\t')
# medie_south_dakota = pd.read_csv(path+'/medie_south_dakota.txt', sep='\t')
# medie_texas = pd.read_csv(path+'/medie_texas.txt', sep='\t')
# medie_nazione = pd.read_csv(path+'/medie_nazione.txt', sep='\t')
# nazione = pd.read_csv(path+'/nazione.txt', sep='\t')


print('\nriempo i giorni mancanti\nci sarnno 10 barre di progressione\n')
stazione1_riempita = me.riempi(stazione1)
stazione2_riempita = me.riempi(stazione2)
stazione3_riempita = me.riempi(stazione3)
stazione4_riempita = me.riempi(stazione4)
medie_california_riempita = me.riempi(medie_california)
medie_colorado_riempita = me.riempi(medie_colorado)
medie_new_york_riempita = me.riempi(medie_new_york)
medie_south_dakota_riempita = me.riempi(medie_south_dakota)
medie_texas_riempita = me.riempi(medie_texas)
medie_nazione_riempita = me.riempi(medie_nazione)


if salvataggio==True:
    stazione1_riempita.to_csv(path+'/stazione1_riempita.txt', sep='\t', na_rep='', index=False)
    stazione2_riempita.to_csv(path+'/stazione2_riempita.txt', sep='\t', na_rep='', index=False)
    stazione3_riempita.to_csv(path+'/stazione3_riempita.txt', sep='\t', na_rep='', index=False)
    stazione4_riempita.to_csv(path+'/stazione4_riempita.txt', sep='\t', na_rep='', index=False)
    medie_california_riempita.to_csv(path+'/medie_california_riempita.txt', sep='\t', na_rep='', index=False)
    medie_colorado_riempita.to_csv(path+'/medie_colorado_riempita.txt', sep='\t', na_rep='', index=False)
    medie_new_york_riempita.to_csv(path+'/medie_new_york_riempita.txt', sep='\t', na_rep='', index=False)
    medie_south_dakota_riempita.to_csv(path+'/medie_south_dakota_riempita.txt', sep='\t', na_rep='', index=False)
    medie_texas_riempita.to_csv(path+'/medie_texas_riempita.txt', sep='\t', na_rep='', index=False)
    medie_nazione_riempita.to_csv(path+'/medie_nazione_riempita.txt', sep='\t', na_rep='', index=False)

