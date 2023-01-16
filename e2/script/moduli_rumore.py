import pandas as pd
import numpy as np
from scipy import fft, optimize
import matplotlib.pyplot  as plt

def rumore(df,inquinante,filtro_freq1,filtro_amp):

    dati = df[inquinante].to_numpy()
    tempo = df['Date Local'].to_numpy()
    date = df['Date Local']
    segni_x=[]
    j = 0
    for i in range(len(df)):
        if ((date[i][-1]=='1') and (date[i][-2]=='0')):
            if ((j%2)==0):
                segni_x = np.append(segni_x,date[i])
            j=j+1
    segni_x = np.append(segni_x,date.loc[len(date)-1])

    ##############################################################################
    # fourier dati
    coef_f = fft.rfft(dati)
    indici =  np.arange(1,(coef_f.size//2))
    coef_ps = np.absolute(coef_f[indici])**2
    coef_freq_f = 0.5*fft.rfftfreq(coef_f.size, d=1)

    ######################################################################
    # inversa dati

    if np.isnan(filtro_amp)==False:
        maschera_1 =  ((np.absolute(coef_freq_f)) > filtro_freq1) & ((np.absolute(coef_f[:len(coef_freq_f)]))**2 < filtro_amp) #filtro in frequenza basato su apmiezza dello spettro di potenza. 
    else:
        maschera_1 = np.absolute(coef_freq_f) > filtro_freq1 #filtro in freq

    filtrato_freq1 = coef_f[:len(maschera_1)].copy()
    filtrato_freq1[maschera_1] = 0
    dati_inversa_freq1 = fft.irfft(filtrato_freq1, n=len(dati))


    ##############################################################################
    # fourier residui

    rumore = ((dati-dati_inversa_freq1))
    indice2=[] # così considero rumore tutte le frequenza non attivamente filtrate

    for i in range(len(maschera_1)-1): #-1 è dovuto all'esclusione del coef. 0 nel calcolo di coef_ps in 'fourier dati'
        if maschera_1[i]==True:
            indice2=np.append(indice2,i)

    indice2=indice2.astype(int)
    coef_f_rumore = fft.rfft(rumore)
    indici =  indice2
    coef_ps_rumore = np.absolute(coef_f_rumore[indici])**2
    coef_freq_rumore = 0.5*fft.rfftfreq(coef_f_rumore.size, d=1)
    coef_plot_rumore = coef_freq_rumore[indici]

    ###################################################
    #   fit

    def f_rumore(f, N, beta):
        '''
        Funzione per fit Spettro Potenza rumore

        f: frequenze
        N    : normalizzazione
        beta : esponente 

        return N/f^beta
        '''
    
        return (N/f**beta)
    
    val, cov= optimize.curve_fit(f_rumore , coef_plot_rumore, coef_ps_rumore, p0=[1,0])
    print('\n'+'normalizzazione = {:1.2f} +- {:1.2f}'.format(val[0], np.sqrt(cov[0,0]))+'\n')
    print('\n'+'beta = {:1.2f} +- {:1.2f}'.format(val[1], np.sqrt(cov[1,1]))+'\n')

    ################################################
    #   grafico
    plt.plot( coef_plot_rumore,  coef_ps_rumore,label='rumore')
    plt.plot( coef_plot_rumore, f_rumore(coef_plot_rumore, val[0], val[1]),label=r'fit N/$(f^{\beta})$')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('frequenza [1/d]')
    plt.ylabel('rumore '+inquinante)
    plt.legend(fontsize=12, loc = 'best', frameon=True)
    plt.grid()
    plt.tight_layout()
    plt.show()
