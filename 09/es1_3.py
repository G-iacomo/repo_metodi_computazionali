import matplotlib.pyplot as plt 
import reco
import pandas as pd
import numpy as np

def leggi_dati(df):
    ah=np.empty(0)
    for i in range(len(df['mod_id'])):
        hit=reco.Hit(df['mod_id'][i],df['det_id'][i],df['hit_time'][i])
        ah=np.append(ah, hit)
    return ah
'''
def nuovo_evento(dt,start):
    for i in range(len(dt[start:])):
        if dt>threshold:
            return i
        elif i==(len(dt[start:])-1):
            return i
        else:
            return -np.inf
    return -np.inf
def array_evento(dt,start,stop):
    ae=np.empty(0)
    ae=np.append(ae,dt[start:stop])
    return ae
'''

def array_evento(dt,array_hit):
    ae=np.empty(0)
    ae=np.append(ae,reco.Event())
    #ae=reco.Event()
    for i in range(len(dt)): #sbagliato perchè dt ha lunghezza meno uno. devi prima o differenza punto per punto e non array differenze. quindi così devi mettere prima il primo evento (benedetta)
        if dt[i]<=threshold:
            ae[-1].aggiungi_hit(array_hit[i])
        else:
            ae=np.append(ae,reco.Event())
            ae[-1].aggiungi_hit(array_hit[i])
    return ae

df0=pd.read_csv('/home/gb980061/repo_metodi_computazionali/09/hit_times_M0.csv')
df1=pd.read_csv('/home/gb980061/repo_metodi_computazionali/09/hit_times_M1.csv')
df2=pd.read_csv('/home/gb980061/repo_metodi_computazionali/09/hit_times_M2.csv')
df3=pd.read_csv('/home/gb980061/repo_metodi_computazionali/09/hit_times_M3.csv')
#print(df0.keys())
threshold=100
array_hit=np.empty(0)
array_hit=np.append(array_hit,leggi_dati(df0))
if True:
#if False:
    array_hit=np.append(array_hit,leggi_dati(df1))
    array_hit=np.append(array_hit,leggi_dati(df2))
    array_hit=np.append(array_hit,leggi_dati(df3))
array_hit=np.sort(array_hit)

bins=80 #numero dei bin   
mask=(np.diff(array_hit))>0
t_diff=np.diff(array_hit)[mask]
if False:
#if True:
    logbins=np.logspace(np.log10(np.min(t_diff)),np.log10(np.max(t_diff)),bins) #larghezza bins log10
    plt.hist(t_diff,bins=logbins)
    plt.xscale('log')
    plt.grid()
    plt.show()

ae=array_evento(t_diff,array_hit)
nhit_in_ae=np.empty(0)
for i in range(len(ae)):
    nhit_in_ae=np.append(nhit_in_ae,ae[i].nhit)
if True:
    plt.hist(nhit_in_ae,bins=20)
    plt.show() #risultato errato.

