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
'''
#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione  4 - Equazioni e Minimizzazione:    #
#                                                   #
#   Fit di un set di dati                           #
#                                                   #
#####################################################

import sys,os
import numpy as np
import pandas as pd

from scipy import optimize

import matplotlib.pyplot as plt


# Funzione Lognormale per Fit 
def flogn(x, A, xm, s):
    return A*np.exp(-(np.log(x)-xm)**2/s**2 )


def fit_data():

    ################################### Dati Input  ##########################################
    # Lettura file 
    lndf = pd.read_csv('fit_data.csv')

    # Colonne Data Frame
    print('Columns:', lndf.columns)


    #############################  Grafici Preliminari  ######################################
    ## grafico y vs. x
    plt.subplots(figsize=(10,6))
    plt.errorbar(lndf['x'], lndf['y'], yerr=np.sqrt(lndf['y']), fmt='o' )
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()
    

    ## grafico y vs. x logy
    plt.subplots(figsize=(10,6))
    plt.errorbar(lndf['x'], lndf['y'], yerr=np.sqrt(lndf['y']), fmt='o' )
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xscale('log')
    plt.show()


    #####################################  Fit  ############################################
    ## Fit 
    par, par_cov = optimize.curve_fit(flogn, lndf['x'], lndf['y'], p0=[50, 2, 2], absolute_sigma=True, method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15)
    print('--------------------------------------------------------')
    print('Parametri fit:\n      A = {:3.1f} +- {:.1f}\n   mean = {:3.3f} +- {:.3f}\n  sigma = {:3.3f} +- {:.3f}'.format(
        par[0], np.sqrt(par_cov[0,0]),        par[1], np.sqrt(par_cov[1,1]),        par[2], np.sqrt(par_cov[2,2]) ))

    #print(p,'\n',pc)

    # valri della funzione di fit con aramtri ottimizzati
    fity = flogn(lndf['x'], par[0], par[1], par[2])

    # Calcolo Chi2 
    chi2 = np.sum( (fity - lndf['y'])**2 /lndf['y'] )
    # Gradi di libertà
    ndof = lndf.shape[0]-len(par)
    print('--------------------------------------------------------')
    print('Chi2 / ndf: {:4.2f} / {:d} = {:2.3f}'.format( chi2, ndof,  chi2/ndof))



    #########################  Grafico Finale Dati e Fit  ##################################
    # Grafico con due subplot
    fig, ax = plt.subplots(2,1, figsize=(10,7), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
    # Rimuovo spazio verticale fra i subplot
    fig.subplots_adjust(hspace=0)

    # Grafico subplot 0 (dati e funzione di fit)
    ax[0].errorbar(lndf['x'], lndf['y'], yerr=np.sqrt(lndf['y']), fmt='o', color='royalblue', label='Data' )
    ax[0].plot(lndf['x'], fity, color='orange',  label='Lognormal Fit' )
    ax[0].set_ylabel('y', fontsize=14)
    ax[0].tick_params(axis="y", labelsize=14) 
    ax[0].legend(fontsize=14, frameon=False)
    ax[0].text(lndf['x'][0], max(lndf['y']), r'$\chi^2$ / ndf : {:3.2f} / {:d}'.format(chi2, ndof), fontsize=16, color='dimgray')

    # Grafico subplot 1 (rapporto dati / funzione di fit)
    ax[1].errorbar(lndf['x'], lndf['y']/fity, yerr=np.sqrt(lndf['y'])/fity, fmt='o', color='royalblue' )
    ax[1].axhline(1, color='orange')

    ax[1].set_xlabel('x', fontsize=14)
    ax[1].set_ylabel('Data/Fit', fontsize=14)

    ax[1].tick_params(axis="x", labelsize=14) 
    ax[1].tick_params(axis="y", labelsize=14) 

    ax[1].set_xscale('log')
    ax[1].set_ylim(0.0, 2.0)
    ax[1].set_yticks(np.arange(0.0, 2.1, 0.5))
    ax[1].grid(True, axis='y')

    # Salvo immagine grafico come file .png e .pdf 
    plt.savefig('lognormal_fit.png')
    plt.savefig('lognormal_fit.pdf')
    plt.show()
    


    

if __name__ == "__main__":

    fit_data()
 '''
