import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import emcee
import corner

#monte carlo con markov chian di una fittizia linea di assorbimento

w=16 #numero di walker
p=[4.5,0.5,-0.2,10,-5] #media, deviazione, m, b, alpha. stima parametri

df=pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/08/dati.csv')
#print(df.columns) #E, f, ferr = energia, flusso, incertezza flusso
xx=np.linspace(0,10,100) #dummy array per grafici

def flusso(e,par):
    # parametri: energia, media, deviazione
    # e=energia
    mu=par[0] #media
    sigma=par[1] #deviazione standard
    m=par[2] #?
    b=par[3] #?
    a=par[4] #=alpha=?
    return m*e+b+a*np.exp((-(e-mu)**2)/(2*(sigma)**2))

def loglike(x,y,yerr,par): #likelihood logaritmica (ergo -0.5*)
    #parametri: e, f, ferr, parametri
    return -0.5*np.sum(((y-flusso(x,par))/yerr)**2)

def logprior(par): #probabilità a priori logaritmica ergo -inf=probabilità nulla e 0=prob. certa
    mu,sigma,m,b,a=par
    if (0<mu<10 and 0<sigma<3 and m<0 and 0<b<15 and -10<a<0): #probabilità uniforme in questo range
        return 0.0
    else:
        return -np.inf

def logprob(par,x,y,yerr): #probabilità logaritmica a posteriori
    #parametri: e, f, ferr, parametri
    return logprior(par)+loglike(x,y,yerr,par)

#pos=np.random.rand(w,len(p)) #posizione iniziale totalmente casuale dei walker = valori totalmente random dei parametri iniziali. sbagliato perchè sono fuori dal range iniziali molti. e in generale troppo lontani dal vero
pos=p+0.1*np.random.rand(w,len(p)) #posizione iniziale dei walker a partire dai parametri stimati con l'aggiunta di una variazione

sampler = emcee.EnsembleSampler(w, len(p), logprob, args=(df['E'],df['f'],df['ferr'])) #nota: i parametri vengono presi sotto con pos. un argomento in meno
sampler.run_mcmc(pos, 1000, progress=True) #1000 passi per ogni walker 

#grafici parametri
fig, axes = plt.subplots(len(p), figsize=(10, 9), sharex=True)
fila_sampler = sampler.get_chain() #dispone in fila i parametri comodo per grafici

for i in range(len(p)):
    ax = axes[i]
    ax.plot(fila_sampler[:, :, i], "k", alpha=0.3)
    ax.set_xlim(0, len(fila_sampler))
    ax.yaxis.set_label_coords(-0.1, 0.5)
axes[-1].set_xlabel("numero passi");
plt.grid()
plt.show()

#grafico iniziale: dati e funzione con parametri iniziali
plt.errorbar(df['E'],df['f'],df['ferr'])
plt.plot(xx,flusso(xx,p))
plt.grid()
#plt.show()

#campionamento risultati e suo grafico
flat_sampler = sampler.get_chain(discard=120, thin=15, flat=True) #ignora i primi 120 punti e poi ne campiona 1 ogni 15. flat significa che fa una matrice
#print(len(flat_sampler))
plt.errorbar(df['E'],df['f'],df['ferr'])
for i in flat_sampler[np.random.randint( len(flat_sampler), size=10)]: #prende 10 set di parametri estratti a caso tra quelli forniti
    plt.plot(xx,flusso(xx,i), alpha=0.3)
plt.grid()
plt.show()

#corner plot
fig = corner.corner( flat_sampler)
plt.show()