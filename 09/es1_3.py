import reco
import pandas as pd

#da cambaire!! non usare evento. crea solo array di hit
def leggi_dati(df):
    e=reco.Event()
    for i in range(len(df['hit_time'])):
        Hit=reco.Hit(df['mod_id'][i],df['det_id'][i],df['hit_time'][i])
        #e=reco.Event.aggiungi_hit(e,Hit)
        e.aggiungi_hit(Hit)
    return e.a_Hit


df0=pd.read_csv('/home/gb980061/repo_metodi_computazionali/09/hit_times_M0.csv')
df1=pd.read_csv('/home/gb980061/repo_metodi_computazionali/09/hit_times_M1.csv')
df2=pd.read_csv('/home/gb980061/repo_metodi_computazionali/09/hit_times_M2.csv')
df3=pd.read_csv('/home/gb980061/repo_metodi_computazionali/09/hit_times_M3.csv')
#print(df0.keys())
#e=reco.Event()
#print(e.nhit)
print(leggi_dati(df0))
