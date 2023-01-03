import pandas as pd
import numpy as np
from tqdm import tqdm
import warnings

###########################################
#               PARAMETRI

numero_dati = None # Default=None. numero di righe da importare. utilizzata in test iniziali
stati = np.array([6,8,48,46,36]) # codici degli stati analizzati.
                        #rispettivamente California, Colorado, Texas, South Dakota, New York
check = False #se True lo script esegue piccoli controlli del corretto funzionamento in alcuni punti salienti
#pd.set_option('display.max_columns', 500) #il numero di colonne massime da stampare
#pd.set_option('display.max_rows', 500) #il numero di righe massime da stampare

###########################################
#              SELEZIONE STATI D'INTERESSE

def funzione_stati():
    dati_iniziali = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/progetto/pollution_us_2013_2015.csv', nrows=numero_dati)

    if check: #controlla la presenza di eventuali righe ripetute
        if all(dati_iniziali.duplicated())==False:
            print('\nCHECK: non ci sono duplicati\n   oppure il dataframe è vuoto\n')
        else:
            print('\nCHECK: ci sono dei duplicati\n')

    dati_iniziali.drop(['Unnamed: 0'], axis=1, inplace=True) #elimino la colonna senza nome. 
                #non sono indici in quanto si ripetono pur non essendo duplicate le righe
    dati_iniziali.reset_index(inplace=True,names='original row-2') #assegno un indice ad ogni riga. la colonna si chiama'original row-2'
            #così tengo conto della riga di provenienza una volta elaborati i dati: riga originaria=('original row-2'+2)

    selezione_stati = (i in stati for i in dati_iniziali['State Code']) #maschera degli stati d'interesse: type=generator
                                            #equivale ad array con indici delle righe riferite ad uno stato in 'stati'
    dati = (dati_iniziali.loc[selezione_stati]).copy() #copy mi assicura di non modificare accidentalmente i dati originari
    dati.reset_index(inplace=True) #permette di riferirsi alle righe partendo dall'indice 0
    dati.drop(['index'], axis=1, inplace=True) #non serve avere l'indice esplicito in una colonna

    if check: #controlla la correttezza della selezione dei dati confrontando il numero di dati per gli stati d'interesse prima e dopo la selezione
        conteggi_dati_iniziali=(dati_iniziali['State Code'].value_counts()).to_frame() #conteggio ricorrenze di ogni stato. da dati originari
        conteggi_dati=dati['State Code'].value_counts().to_frame() #conteggio ricorrenze stati da dati selezionati
        #print(conteggi_dati_iniziali) #se non commentato stampa il numero di volte che uno stesso stato compare. per controllo manuale
        #print(conteggi_dati) #se non commentato stampa il numero di volte che uno stesso stato compare. per controllo manuale
        booleano = True #dummy bool
        for i in stati: #confronta le ricorrenze degli stati di interesse
            if conteggi_dati_iniziali.at[i,'State Code'] != conteggi_dati.at[i,'State Code']:
                print('CHECK: errore sul filtro degli stati. lo stato che genera l\'errore è:',i,'\n')
                booleano = False
                break
        if booleano:
            print('CHECK: gli stati di interesse sono stati selezionati correttamente\n')
    
    return dati

##########################################
#           MEDIE GIORNALIERE

# def funzione_medie(dati): #funzionante ma risultati errati poichè assunzione errata che ogni giorno ha 4 righe assegnate. real time:50s
#     indici=[] #indici da tenere
#     for i in tqdm(range(0,len(dati)-4+1,4)):
#     #for i in tqdm(range(0,8,4)):
#         if (((dati.at[i+1,'SO2 Mean']>=0) and (dati.at[i+1,'CO Mean']>=0) )and (dati.at[i+1,'NO2 Mean']>=0)):
#             dati.at[i+1,'SO2 Mean'] = np.nanmean([dati.at[i+1,'SO2 1st Mean'],dati.at[i+2,'SO2 1st Mean']])
#             dati.at[i+1,'SO2 1st Max Value'] = max(dati.at[i+1,'SO2 1st Max Value'],dati.at[i+2,'SO2 1st Max Value'])
#             dati.at[i+1,'CO Mean'] = np.nanmean([dati.at[i+1,'SO2 1st Mean'],dati.at[i+2,'SO2 1st Mean']])
#             dati.at[i+1,'CO 1st Max Value'] = max(dati.at[i+1,'CO 1st Max Value'],dati.at[i+2,'CO 1st Max Value'])
#             indici=np.append(indici,i+1)
#     indici= indici.astype(int)
#     dati = dati[dati.index.isin(indici)]
#     return dati

def funzione_medie(dati): #calcola e salva valori giornalieri di: media,  massimo valore 
    i=0 
    indici=[] #array degli indici delle righe da conservare
    with tqdm(total=37731) as pbar: #dato l'importante tempo impiegato è utile una barra di progressione. total=ripetizioni del ciclo+1. real time=3m26s
        while i<(len(dati)):
            data=dati.at[i,'Date Local'] #giorno di riferimento. salvato eplicitamente per chiarezza
            stop=0 #indice dell'ultima riga appartenente alla stessa giornata di i
            for j in range(len(dati)): #scorro le righe successive,a partire da i, per trovare qunado cambia la data.
                        #range(len(dati)) è un caso estremo: ogni dato dovrebbe appartenere allo stesso giorno;
                        # dato l'uso di break non c'è dispendio di risorse
                if (i+j<(len(dati))): #controlla fino all'ultima riga
                    if (data!=(dati.at[i+j,'Date Local'])): #confronta la data con quella di riferimento
                        stop=i+j-1 #gli indici [i:stop] si riferiscono a dati della stessa giornata
                        break
                else: #superfluo ma così l'uscita dal for è assicurata sempre
                    break
                if((i+j==(len(dati)-1))): #caso in cui l'ultima riga abbia la stessa data delle precedenti
                    stop=i+j #in tal caso devo includere l'ultima riga
                    break
            if (((all(dati.loc[i:stop,'SO2 Mean']>=0) and all(dati.loc[i:stop,'CO Mean']>=0))) and all(dati.loc[i:stop,'NO2 Mean']>=0)):
                        #ignoro i dati fisicamente non accettabili
                indici=np.append(indici,i) #salvo l'indice di una sola riga per ogni giorno
                dati.at[i,'NO2 Mean']=np.nanmean(dati.loc[i:stop,'NO2 Mean']) #calcolo la media dei valori medi, se il è dato inesistente viene ignorato 
                dati.at[i,'O3 Mean']=np.nanmean(dati.loc[i:stop,'O3 Mean'])
                dati.at[i,'SO2 Mean']=np.nanmean(dati.loc[i:stop,'SO2 Mean'])
                dati.at[i,'CO Mean']=np.nanmean(dati.loc[i:stop,'CO Mean'])
                with warnings.catch_warnings(): #a causa di righe in cui tutti i valori sono inesistensi np.nanmean resitituisce nan e un warning
                    warnings.simplefilter("ignore", category=RuntimeWarning) #il warning viene silenziato. il while permette di non perderne altri altrove
                    dati.at[i,'NO2 AQI']=np.nanmean(dati.loc[i:stop,'NO2 AQI']) #calcolo la media dei valori AQI. se dato inenistente viene ignorato
                    dati.at[i,'O3 AQI']=np.nanmean(dati.loc[i:stop,'O3 AQI'])
                    dati.at[i,'SO2 AQI']=np.nanmean(dati.loc[i:stop,'SO2 AQI'])
                    dati.at[i,'CO AQI']=np.nanmean(dati.loc[i:stop,'CO AQI'])
                dati.at[i,'NO2 1st Max Value']=max(dati.loc[i:stop,'NO2 1st Max Value']) #seleziona il valore massimo 
                dati.at[i,'O3 1st Max Value']=max(dati.loc[i:stop,'O3 1st Max Value'])
                dati.at[i,'SO2 1st Max Value']=max(dati.loc[i:stop,'SO2 1st Max Value'])
                dati.at[i,'CO 1st Max Value']=max(dati.loc[i:stop,'CO 1st Max Value'])
            i=stop+1 #salto gli indici [i+1:stop] poichè già analizzati
            pbar.update(1) #avanza la barra di progresso di 1/total
    indici= indici.astype(int) #converte eventuali indici salvati come float in int
    dati = dati[dati.index.isin(indici)] #conservo solo le righe con indici d'interesse. index.isin dà array di bool
    return dati


#!! commentare per bene le funzioni
#!! i dati sono raggruppati per stazione di rilevamento quindi non è servito esplicitarne la condizione. specificare
#!! eliminate tutte le giornate con media negativa. elimiare solo le righe?
#!! AQI calcolato il valor medio. é più sensato prendere il valor massimo?
#!! 12 righe con CO AQI assente. specificare. inoltre causa anche warning
#!! warning silenziato: specificare
#!! togliere !!

