import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy import optimize

def lognormale(x, mu, sigma, a):
    y=a*(np.exp(-(np.log(x)-mu)**2/(2*sigma**2)))
    return y

df=pd.read_csv('/home/gb980061/repo_metodi_computazionali/04/fit_data.csv')
dy=np.sqrt(df['y'])#errore manuale assoluto


par=np.array([np.log(100),np.log(50),120]) #mu,sigma,ampiezza. parametri iniziali 
#plt.plot(df['x'],lognormale(df['x'],par), color='black', label='parametri iniziali') #funzione di prova parametri iniziali
par,parcov=scipy.optimize.curve_fit(lognormale,df['x'],df['y'],p0=[par],sigma=dy, absolute_sigma=True) #absolute_sigma=True nel dubbio
#print (par)
print (parcov)
#print (np.sqrt(parcov.diagonal()))
for i in range(len(par)):
    print (par[i],'+/-', np.sqrt(parcov[i][i]))
chi2=np.sum((lognormale(df['x'],par[0],par[1],par[2])-df['y'])**2/(df['y']))
ndof=len(df['x'])-len(par)
print('chi^2/ndof', chi2/ndof)
print ('chi^2/ndof',chi2,'/',ndof)

plt.plot(df['x'],lognormale(df['x'],par[0],par[1],par[2]), color= 'red', label='fit')
plt.errorbar(df['x'],df['y'], yerr=dy, color= 'green', label='dati')
plt.xscale('log')
plt.xlabel('X')
plt.ylabel('conteggi')
plt.grid()
plt.minorticks_on()
plt.legend(fontsize = 12, loc = "upper left", frameon=False)
plt.tight_layout()
plt.show()
