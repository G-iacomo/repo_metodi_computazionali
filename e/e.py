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


selezione_stati = (i in stati for i in dati_iniziali['State Code']) #maschera degli stati d'interesse: type=generator
                                        #array con indici delle righe riferite ad uno stato in 'stati'
dati = (dati_iniziali.loc[selezione_stati]).copy() #mi assicuro di non modificare accidentalmente i dati
dati.rename(columns={'Unnamed: 0':'original row'}, inplace=True)
dati.reset_index(inplace=True)
dati = dati.drop(['index'], axis=1)

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

def media(x,y):
    return (x+y)/2

#for i in tqdm(range(0,len(dati)-4+1,4)):
#for i in tqdm(range(0,4,4)):
    # dati.at[i+1,'SO2 Mean'] = media(dati.at[i+1,'SO2 Mean'],dati.at[i+2,'SO2 Mean'])
    # dati.at[i+1,'SO2 1st Max Value'] = max(dati.at[i+1,'SO2 1st Max Value'],dati.at[i+2,'SO2 1st Max Value'])
    # dati.at[i+1,'CO Mean'] = media(dati.at[i+1,'CO Mean'],dati.at[i+2,'CO Mean'])
    # dati.at[i+1,'CO 1st Max Value'] = max(dati.at[i+1,'CO 1st Max Value'],dati.at[i+2,'CO 1st Max Value'])
    # dati = dati.drop([i],axis=0)
    # dati = dati.drop([i+2],axis=0)
    # dati = dati.drop([i+3],axis=0)
#print(dati[0:8])
medie_negative=(((dati['SO2 Mean']<0) | (dati['CO Mean']<0)) | (dati['NO2 Mean']<0))
dati = dati.drop([medie_negative],axis=0)
print(dati['SO2 Mean']<0)
