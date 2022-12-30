import pandas as pd
import numpy as np
#import scipy

###########################################
#               PARAMETRI

numero_dati = None # Default=None. numero di righe da importare.
stati = np.array([6,8,48,46,36]) # codici degli stati analizzati. rispettivamente California, Colorado, Texas, South Dakota, New York
check = False #se True lo script esegue piccoli controlli del corretto funzionamento in alcuni punti salienti

###########################################
#              RIELABORAZIONE DEI DATI

dati_iniziali = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/progetto/pollution_us_2013_2015.csv', nrows=numero_dati)
if check: #controlla la presenza di eventuali dati ripetuti
    #print('columns name:                            values:\n', dati_iniziali.iloc[0])
    #print(dati_iniziali['State'].value_counts())
    if all(dati_iniziali.duplicated())==False:
        print('\nCHECK: non ci sono duplicati\n   oppure il dataframe è vuoto\n')
    else:
        print('\nCHECK: ci sono dei duplicati\n')


condizione = (i in stati for i in dati_iniziali['State Code']) #generatore degli stati:
                                        #array con indici delle righe riferite ad uno stato in 'stati'
dati = (dati_iniziali.loc[condizione]).copy() #mi assicuro di non modificare accidentalmente i dati
if check: #controlla la correttezza della selezione dei dati confrontando il numero di dati per gli stati d'interesse
    conteggi_dati_iniziali=(dati_iniziali['State Code'].value_counts()).to_frame() #conteggio ricorrenze di ogni stato
    conteggi_dati=dati['State Code'].value_counts().to_frame() #conteggio ricorrenze dati selezionati
    #print(conteggi_dati_iniziali) #se non commentato stampa il numero di volte che uno stesso stato compare. per controllo manuale
    #print(conteggi_dati) #se non commentato stampa il numero di volte che uno stesso stato compare. per controllo manuale
    j=True
    for i in stati: #confronta le ricorrenze degli stati di interesse
        if conteggi_dati_iniziali.at[i,'State Code'] != conteggi_dati.at[i,'State Code']:
            print('CHECK: errore sul filtro degli stati. lo stato che genera l\'errore è:',i,'\n')
            j=False
            break
    if j:
        print('CHECK: gli stati di interesse sono stati selezionati correttamente\n')
