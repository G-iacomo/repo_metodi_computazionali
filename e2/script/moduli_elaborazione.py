import pandas as pd
import numpy as np
from tqdm import tqdm
import warnings
import datetime as dt


def funzione_stati2(dati_iniziali,stati,check):
    '''
    Seleziona i dati di interesse dal dataframe di partenza selezionando quelli apparteneti agli stati scelti

    dati_iniziali : dataframe originario
    stati : array numpy contenete i codici degli stati scelti. tale informazione si trova nella colonna 'State Code'
    check : bool. se true esegui piccoli controlli sul processo

    Return: dataframe dati
    '''

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
        booleano = True #dummy bool
        for i in stati: #confronta le ricorrenze degli stati di interesse
            if conteggi_dati_iniziali.at[i,'State Code'] != conteggi_dati.at[i,'State Code']:
                print('CHECK: errore sul filtro degli stati. lo stato che genera l\'errore è:',i,'\n')
                booleano = False
                break
        if booleano:
            print('CHECK: gli stati di interesse sono stati selezionati correttamente\n')
    return dati

def medie2(dati):
    '''
    calcola le medie giornaliere delle singole stazioni;
    seleziona i valori massimi per la qualità dell'aria (AQI alto, inquinante più presente) e il valor massimo; dati successivamente non utilizzati
    se i dati sono negativi vengono ignorati
    se i dati di un intera giornata sono negativi viene sostituito al loro posto 0
    i dati calcolati sono salvati nella prima riga di ogni giornata. l'indice di tale riga è conservato in 'indici'
    il dataframe viene filtrato attraverso l'uso di indici (attraverso .index e .isin) e restituito

    dati : dataframe su cui eseguire i calcoli

    return : dati :dataframe contenente solo i dati calcolati
    '''
    i=0
    indici=[]
    with tqdm(total=37730) as pbar: #dato l'importante tempo impiegato è utile una barra di progressione. total=ripetizioni del ciclo+1. real time=6m
         while i<(len(dati)):
            data=dati.at[i,'Date Local'] #giorno di riferimento. salvato eplicitamente per chiarezza
            stop=0 #indice dell'ultima riga appartenente alla stessa giornata di i
            for j in range(len(dati)): #scorro le righe successive,a partire da i, per trovare qunado cambia la data.
                        #range(len(dati)) è un caso estremo: ogni dato dovrebbe appartenere allo stesso giorno;
                if (i+j<(len(dati))): #controlla fino all'ultima riga
                    if (data!=(dati.at[i+j,'Date Local'])): #confronta la data con quella di riferimento
                        stop=i+j-1 #gli indici [i:stop] si riferiscono a dati della stessa giornata
                        break
                else: #superfluo ma così l'uscita dal for è assicurata sempre
                    break
                if((i+j==(len(dati)-1))): #caso in cui l'ultima riga abbia la stessa data delle precedenti
                    stop=i+j #in tal caso devo includere l'ultima riga
                    break
            with warnings.catch_warnings(): #a causa di righe in cui tutti i valori sono inesistensi np.nanmean resitituisce nan e un warning
                warnings.simplefilter("ignore", category=RuntimeWarning) #il warning viene silenziato. il while permette di non perderne altri altrove
                indici_NO2 = (dati.index[i:stop+1][((dati.loc[i:stop,'NO2 Mean']).to_numpy()>=0)]).to_numpy()
                dati.at[i,'NO2 Mean']=np.nanmean(dati.loc[indici_NO2,'NO2 Mean']) #calcolo la media dei valori medi, se il è dato inesistente viene ignorato 
                dati.at[i,'NO2 AQI']=np.nanmax(dati.loc[indici_NO2,'NO2 AQI'], initial=0) #calcolo la media dei valori AQI. se dato inenistente viene ignorato. se tutti vuoti=0                
                dati.at[i,'NO2 1st Max Value']=np.nanmax(dati.loc[indici_NO2,'NO2 1st Max Value'], initial=0) #seleziona il valore massimo

                indici_O3 = (dati.index[i:stop+1][((dati.loc[i:stop,'O3 Mean']).to_numpy()>=0)]).to_numpy()
                dati.at[i,'O3 Mean']=np.nanmean(dati.loc[indici_O3,'O3 Mean']) #calcolo la media dei valori medi, se il è dato inesistente viene ignorato 
                dati.at[i,'O3 AQI']=np.nanmax(dati.loc[indici_O3,'O3 AQI'], initial=0) #calcolo la media dei valori AQI. se dato inenistente viene ignorato
                dati.at[i,'O3 1st Max Value']=np.nanmax(dati.loc[indici_O3,'O3 1st Max Value'], initial=0) #seleziona il valore massimo

                indici_SO2 = (dati.index[i:stop+1][((dati.loc[i:stop,'SO2 Mean']).to_numpy()>=0)]).to_numpy()
                dati.at[i,'SO2 Mean']=np.nanmean(dati.loc[indici_SO2,'SO2 Mean']) #calcolo la media dei valori medi, se il è dato inesistente viene ignorato 
                dati.at[i,'SO2 AQI']=np.nanmax(dati.loc[indici_SO2,'SO2 AQI'], initial=0) #calcolo la media dei valori AQI. se dato inenistente viene ignorato
                dati.at[i,'SO2 1st Max Value']=np.nanmax(dati.loc[indici_SO2,'SO2 1st Max Value'], initial=0) #seleziona il valore massimo

                indici_CO = (dati.index[i:stop+1][((dati.loc[i:stop,'CO Mean']).to_numpy()>=0)]).to_numpy()
                dati.at[i,'CO Mean']=np.nanmean(dati.loc[indici_CO,'CO Mean']) #calcolo la media dei valori medi, se il è dato inesistente viene ignorato 
                dati.at[i,'CO AQI']=np.nanmax(dati.loc[indici_CO,'CO AQI'], initial=0) #calcolo la media dei valori AQI. se dato inenistente viene ignorato
                dati.at[i,'CO 1st Max Value']=np.nanmax(dati.loc[indici_CO,'CO 1st Max Value'], initial=0) #seleziona il valore massimo

            indici=np.append(indici,i)
            i=stop+1 #salto gli indici [i+1:stop] poichè già analizzati
            pbar.update(1) #avanza la barra di progresso di 1/total
    indici= indici.astype(int) #converte eventuali indici salvati come float in int
    dati = dati[dati.index.isin(indici)] #conservo solo le righe con indici d'interesse. index.isin dà array di bool
    dati = dati.fillna(0) #nanmean non dispone di un qualcosa analogo ad intial per nanmax. sostituisco i risultati nan con 0. circa 18k casi
    dati.reset_index(inplace=True) #permette di riferirsi alle righe partendo dall'indice 0
    dati.drop(['index'], axis=1, inplace=True) #non serve avere l'indice esplicito in una colonna
    return dati


def media_stato(dati,indici):
    '''
    esegue la media, seleziona il massimo della qualità d'aria e massimo valore registrato solo tra gli indici richiesti
    e ne restituisce i valori sotto forma di array

    dati : dataframe su cui eseguire i calcoli
    indici : indici su cui eseguire i calcoli

    return: array : numpy.arrai contenente i valori calcolati
    '''
    no2=np.nanmean(dati.loc[indici,'NO2 Mean']) #calcolo la media dei valori medi, se il è dato inesistente viene ignorato 
    no2_aqi=np.nanmax(dati.loc[indici,'NO2 AQI'], initial=0) #calcolo la media dei valori AQI. se dato inenistente viene ignorato. se tutti vuoti=0                
    no2_max=np.nanmax(dati.loc[indici,'NO2 1st Max Value'], initial=0) #seleziona il valore massimo

    o3=np.nanmean(dati.loc[indici,'O3 Mean']) #calcolo la media dei valori medi, se il è dato inesistente viene ignorato 
    o3_aqi=np.nanmax(dati.loc[indici,'O3 AQI'], initial=0) #calcolo la media dei valori AQI. se dato inenistente viene ignorato
    o3_max=np.nanmax(dati.loc[indici,'O3 1st Max Value'], initial=0) #seleziona il valore massimo

    so2=np.nanmean(dati.loc[indici,'SO2 Mean']) #calcolo la media dei valori medi, se il è dato inesistente viene ignorato 
    so2_aqi=np.nanmax(dati.loc[indici,'SO2 AQI'], initial=0) #calcolo la media dei valori AQI. se dato inenistente viene ignorato
    so2_max=np.nanmax(dati.loc[indici,'SO2 1st Max Value'], initial=0) #seleziona il valore massimo

    co=np.nanmean(dati.loc[indici,'CO Mean']) #calcolo la media dei valori medi, se il è dato inesistente viene ignorato 
    co_aqi=np.nanmax(dati.loc[indici,'CO AQI'], initial=0) #calcolo la media dei valori AQI. se dato inenistente viene ignorato
    co_max=np.nanmax(dati.loc[indici,'CO 1st Max Value'], initial=0) #seleziona il valore massimo

    array=np.array([no2,no2_aqi,no2_max,o3,o3_aqi,o3_max,so2,so2_aqi,so2_max,co,co_aqi,co_max])
    return array

def riempi(dati):
    '''
    controlla che non vi siano giorni senza alcun dato. se un giorno presenta dati nulli allora i dati originari erano negativi
    se un giorno è mancante i dati originari erano assenti
    in caso il giorno sia presente ne salva i dati
    in caso il giorno sia mancante ne crea la relattiva riga e ne calcola il valore come la media tra il dato del giorno precedente e il successivo
    (NOTA: se più giorni mancanti sono consegutivi questi avranno tutti lo stesso valore)

    dati : dataframe su cui controllare le date

    return : dati_riempiti : dataframe con una riga per giornata
    '''
    j=0 #indice dati
    i=0 #indice dati_riempiti
    data = (dt.datetime.strptime(dati.loc[0,'Date Local'], '%Y-%m-%d').date()) #data di partenza
    dati_riempiti = pd.DataFrame(columns=['Date Local','NO2 Mean','NO2 AQI','NO2 1st Max Value','O3 Mean','O3 AQI','O3 1st Max Value','SO2 Mean','SO2 AQI','SO2 1st Max Value','CO Mean','CO AQI','CO 1st Max Value'])
    with tqdm(total=(((dt.datetime.strptime(dati.loc[len(dati)-1,'Date Local'], '%Y-%m-%d').date())-(dt.datetime.strptime(dati.loc[0,'Date Local'], '%Y-%m-%d').date())).days-1)) as pbar:
        while i<=(((dt.datetime.strptime(dati.loc[len(dati)-1,'Date Local'], '%Y-%m-%d').date())-(dt.datetime.strptime(dati.loc[0,'Date Local'], '%Y-%m-%d').date())).days-1):
            data_dati = dt.datetime.strptime(dati.loc[j,'Date Local'], '%Y-%m-%d').date()
            if data_dati == data:
                dati_riempiti.loc[i]=dati.loc[j]
                j=j+1
                i=i+1
            if data_dati > data:
                dati_riempiti.loc[i,'Date Local'] = data
                dati_riempiti.iloc[i,1:] = media_stato(dati,np.array([j-1,j]))
                i=i+1
            data = data + dt.timedelta(days=1)
            pbar.update(1) #avanza la barra di progresso di 1/total
    return dati_riempiti

def selezione_stato(dati,stato):
    '''
    seleziona gli indici di un dataframe in cui il valore 'State Code' è quello richiesto

    dati : dataframe da filtare
    stati : int. stato da selezionare

    return : gli indici delle righe selezionate
    '''
    indici = dati.index[dati['State Code'].to_numpy()==stato].to_numpy()
    return indici

def selezione_indirizzo(dati,indirizzo):
    '''
    seleziona gli indici di un dataframe in cui ilindirizzo è quello richiesto

    dati : dataframe da filtare
    indirizzo : stringa. l'indirizzo da selezionare

    return : gli indici delle righe selezionate
    '''
    indici = dati.index[dati['Address'].to_numpy()==indirizzo].to_numpy()
    return indici

def selezione_data(dati,data):
    '''
    seleziona gli indici di un dataframe la cui data è quella richiesta

    dati : dataframe da filtare
    data : stringa. l'indirizzo da selezionare

    return : gli indici delle righe selezionate
    '''
    indici = dati.index[dati['Date Local'].to_numpy()==data].to_numpy()
    return indici

def dataframe_filtrato(dati,indici):
    '''
    dato un dataframe e gli indici d'interesse, ne restituisce il dataframe filtrato
    controlla gli indici solo dove strettamente necessario

    dati : dataframe da filtrare
    indici : indici da conservare
    

    return :dataframe filtarto
    '''

    df = dati[indici[0]:indici[-1]+1][dati.index[indici[0]:indici[-1]+1].isin(indici)]
    df.reset_index(inplace=True) #permette di riferirsi alle righe partendo dall'indice 0
    df.drop(['index'], axis=1, inplace=True) #non serve avere l'indice esplicito in una colonna
    return df



