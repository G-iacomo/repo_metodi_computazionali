import pandas as pd
import numpy as np
import warnings
import time

##################################################################
#   parametri modificabili

numero_dati=1000
path='' #specificare la cartella di lavoro                                                                                                                                         /home/gb/Desktop/giacomo/ubuntu/unipg/metodi_computazionali/progetto


dati = pd.read_csv(path+'/pollution_us_2013_2015.csv', nrows=numero_dati)


def medie_index(dati):
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
    indici= indici.astype(int) #converte eventuali indici salvati come float in int
    dati = dati[dati.index.isin(indici)] #conservo solo le righe con indici d'interesse. index.isin dà array di bool
    dati = dati.fillna(0) #nanmean non dispone di un qualcosa analogo ad intial per nanmax. sostituisco i risultati nan con 0. circa 18k casi
    dati.reset_index(inplace=True) #permette di riferirsi alle righe partendo dall'indice 0
    dati.drop(['index'], axis=1, inplace=True) #non serve avere l'indice esplicito in una colonna
    return dati



def medie_for_at(dati):
    i=0 
    indici=[] #array degli indici delle righe da conservare
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
        if (((all(dati.loc[i:stop,'SO2 Mean']<0) or all(dati.loc[i:stop,'CO Mean']<0))) or all(dati.loc[i:stop,'NO2 Mean']<0)):
            print('giornata con almeno un inquinante sempre negativo!')
        with warnings.catch_warnings(): #a causa di righe in cui tutti i valori sono inesistensi np.nanmean resitituisce nan e un warning
            warnings.simplefilter("ignore", category=RuntimeWarning) #il warning viene silenziato. il while permette di non perderne altri altrove
            i_stop=np.empty(0)
            for i in range(i,stop):
                if dati.at[i,'NO2 Mean']>=0:
                    i_stop=np.append(i_stop,i)
            dati.at[i,'NO2 Mean']=np.nanmean(dati.loc[i_stop,'NO2 Mean']) #calcolo la media dei valori medi, se il è dato inesistente viene ignorato 
            dati.at[i,'NO2 AQI']=max(dati.loc[i_stop,'NO2 AQI'], default=0) #calcolo la media dei valori AQI. se dato inenistente viene ignorato
            dati.at[i,'NO2 1st Max Value']=max(dati.loc[i_stop,'NO2 1st Max Value'], default=0) #seleziona il valore massimo
            i_stop=np.empty(0)
            for i in range(i,stop):
                if dati.at[i,'O3 Mean']>=0:
                    i_stop=np.append(i_stop,i)
            dati.at[i,'O3 Mean']=np.nanmean(dati.loc[i_stop,'O3 Mean'])
            dati.at[i,'O3 AQI']=max(dati.loc[i_stop,'O3 AQI'], default=0)
            dati.at[i,'O3 1st Max Value']=max(dati.loc[i_stop,'O3 1st Max Value'], default=0)
            i_stop=np.empty(0)
            for i in range(i,stop):
                if dati.at[i,'SO2 Mean']>=0:
                    i_stop=np.append(i_stop,i)
            dati.at[i,'SO2 Mean']=np.nanmean(dati.loc[i_stop,'SO2 Mean'])
            dati.at[i,'SO2 AQI']=max(dati.loc[i_stop,'SO2 AQI'], default=0)
            dati.at[i,'SO2 1st Max Value']=max(dati.loc[i_stop,'SO2 1st Max Value'], default=0)
            i_stop=np.empty(0)
            for i in range(i,stop):
                if dati.at[i,'CO Mean']>=0:
                    i_stop=np.append(i_stop,i)
            dati.at[i,'CO Mean']=np.nanmean(dati.loc[i_stop,'CO Mean'])
            dati.at[i,'CO 1st Max Value']=max(dati.loc[i_stop,'CO 1st Max Value'], default=0)
            dati.at[i,'CO AQI']=max(dati.loc[i_stop,'CO AQI'], default=0)
        indici=np.append(indici,i)
        i=stop+1 #salto gli indici [i+1:stop] poichè già analizzati
    indici= indici.astype(int) #converte eventuali indici salvati come float in int
    dati = dati[dati.index.isin(indici)] #conservo solo le righe con indici d'interesse. index.isin dà array di bool
    return dati



print('Il file iniziale, con tutti gli stati, contiene 392220 righe\nper la media giornaliera di {} righe:'.format(numero_dati))
start_time = time.time()
a=medie_index(dati)
print('\nla funzione che utilizza gli indici gestiti tramite array numpy impiega:\n')
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
b=medie_for_at(dati)
print('\nla funzione che utilizza dei cicli for con accesso agli elementi tramite .at impiega:\n')
print("--- %s seconds ---" % (time.time() - start_time))