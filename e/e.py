import pandas as pd
import numpy as np
import statistics as st
from tqdm import tqdm

###########################################
#               PARAMETRI

numero_dati = None # Default=None. numero di righe da importare.
stati = np.array([6,8,48,46,36]) # codici degli stati analizzati.
                        #rispettivamente California, Colorado, Texas, South Dakota, New York
check = False #se True lo script esegue piccoli controlli del corretto funzionamento in alcuni punti salienti
pd.set_option('display.max_columns', 500) #il numero di colonne massime da stampare
#pd.set_option('display.max_rows', 500) #il numero di righe massime da stampare

###########################################
#              SELEZIONE STATI D'INTERESSE

dati_iniziali = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/progetto/pollution_us_2013_2015.csv', nrows=numero_dati)

if check: #controlla la presenza di eventuali dati ripetuti
    #print('columns name:                            values:\n', dati_iniziali.iloc[0])
    #print(dati_iniziali['State'].value_counts())
    if all(dati_iniziali.duplicated())==False:
        print('\nCHECK: non ci sono duplicati\n   oppure il dataframe è vuoto\n')
    else:
        print('\nCHECK: ci sono dei duplicati\n')

dati_iniziali.drop(['Unnamed: 0'], axis=1, inplace=True) #elimino la colonna senza nome. 
            #non sono indici in quanto si ripetevano pur non essendo duplicate le righe
dati_iniziali.reset_index(inplace=True,names='original row-2') #assegno un indice ad ogni riga. la colonna si chiama'original row-2'
        #così tengo conto della riga di provenienza una volta elaborati i dati: riga originaria=('original row-2'+2)

selezione_stati = (i in stati for i in dati_iniziali['State Code']) #maschera degli stati d'interesse: type=generator
                                        #array con indici delle righe riferite ad uno stato in 'stati'
dati = (dati_iniziali.loc[selezione_stati]).copy() #mi assicuro di non modificare accidentalmente i dati
#dati.rename(columns={'Unnamed: 0':'original row'}, inplace=True)
dati.reset_index(inplace=True)
dati.drop(['index'], axis=1, inplace=True)

if check: #controlla la correttezza della selezione dei dati confrontando il numero di dati per gli stati d'interesse
    conteggi_dati_iniziali=(dati_iniziali['State Code'].value_counts()).to_frame() #conteggio ricorrenze di ogni stato
    conteggi_dati=dati['State Code'].value_counts().to_frame() #conteggio ricorrenze dati selezionati
    #print(conteggi_dati_iniziali) #se non commentato stampa il numero di volte che uno stesso stato compare. per controllo manuale
    #print(conteggi_dati) #se non commentato stampa il numero di volte che uno stesso stato compare. per controllo manuale
    j = True
    for i in stati: #confronta le ricorrenze degli stati di interesse
        if conteggi_dati_iniziali.at[i,'State Code'] != conteggi_dati.at[i,'State Code']:
            print('CHECK: errore sul filtro degli stati. lo stato che genera l\'errore è:',i,'\n')
            j = False
            break
    if j:
        print('CHECK: gli stati di interesse sono stati selezionati correttamente\n')

##########################################
#           SELEZIONE MEDIE

#dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/dati.csv', sep=',', index=False)
dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/dati.txt', sep='\t', na_rep='!!', index=False)


indici=[] #indici da tenere
for i in tqdm(range(0,len(dati)-4+1,4)):
#for i in tqdm(range(0,8,4)):
    if (((dati.at[i+1,'SO2 Mean']>=0) and (dati.at[i+1,'CO Mean']>=0) )and (dati.at[i+1,'CO Mean']>=0)):
        dati.at[i+1,'SO2 Mean'] = st.fmean([dati.at[i+1,'SO2 1st Max Value'],dati.at[i+2,'SO2 1st Max Value']])
        dati.at[i+1,'SO2 1st Max Value'] = max(dati.at[i+1,'SO2 1st Max Value'],dati.at[i+2,'SO2 1st Max Value'])
        dati.at[i+1,'CO Mean'] = st.fmean([dati.at[i+1,'SO2 1st Max Value'],dati.at[i+2,'SO2 1st Max Value']])
        dati.at[i+1,'CO 1st Max Value'] = max(dati.at[i+1,'CO 1st Max Value'],dati.at[i+2,'CO 1st Max Value'])
        indici=np.append(indici,i+1)

indici= indici.astype(int)
dati = dati[dati.index.isin(indici)]

# if all(dati.duplicated())==False:
#     print('ok')
# else:
#     print('errore nel for')

#dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/medie_temporanee.csv', sep=',', index=False)
dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/medie_temporanee.txt', sep='\t', na_rep='!!', index=False)

#!!!!!!! problema: alcuni valori con aqi sono invertiti eg. 158512-158516 quindi perdi valori.
#!!!!! alcune righe dei dati originarili hanno piu di 4 rivelazione per un solo giorno! (ad occhio solo 19805)
#!! togliere !!

