import pandas as pd
import numpy as np
from scipy import fft
import matplotlib.pyplot  as plt

def inversa(df,inquinante):
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

    filtro_freq1 = 0.4e-2 #filtro in ampiezza
    # filtro_amp = 1e5 #filtro in ampiezza
    filtro_freq2 = 0.7e-2 #filtro in frequenza

    ##############################################################################
    # fourier, spettro potenza log e lin
    coef_f = fft.rfft(dati)
    indici =  np.arange(1,(coef_f.size//2))
    # indici =  np.arange(0,(coef_f.size//2)) #coef. 0. escluso per coerenza con quanto fatto precedentemente
    coef_ps = np.absolute(coef_f[indici])**2
    coef_freq_f = 0.5*fft.rfftfreq(coef_f.size, d=1)
    plt.figure(1)
    plt.plot(coef_freq_f[indici],coef_ps)
    plt.axvline (filtro_freq1,color='red',linestyle=':',alpha=0.8,label='filtro 1') # filtro in freq
    # plt.axhline (1e5,color='red',linestyle=':',alpha=0.8,label='filtro 1') #filtro amp
    plt.axvline (filtro_freq2,linestyle=':',alpha=0.8,label='filtro 2') #filtro freq
    plt.xscale('log')
    plt.xlabel(r'frequenza [$d^{-1}$]')
    plt.ylabel('spettro potenza '+inquinante)
    plt.legend(fontsize=12, loc='best', frameon=True)
    plt.grid()
    plt.tight_layout()
    plt.figure(2)
    plt.plot(coef_freq_f[indici],coef_ps)
    plt.axvline (filtro_freq1,color='red',linestyle=':',alpha=0.8,label='filtro 1') # filtro in freq
    # plt.axhline (1e5,color='red',linestyle=':',alpha=0.8,label='filtro 1') #filtro amp
    plt.axvline (filtro_freq2,linestyle=':',alpha=0.8,label='filtro 2') #filtro freq
    plt.xscale('log')
    plt.xlabel(r'frequenza [$d^{-1}$]')
    plt.ylabel('spettro potenza '+inquinante)
    plt.legend(fontsize=12, loc='best', frameon=True)
    plt.grid()
    plt.tight_layout()
    plt.yscale('log')
    plt.show()

    ######################################################################
    # inversa

    # !!
    # maschera_freq1 =  ((np.absolute(coef_freq_f)) >filtro_freq1)&((np.absolute(coef_f[:len(coef_freq_f)]))**2 <filtro_amp) #filtro in frequenza basato su apmiezza dello spettro di potenza. incasinato ma 1/7 si vede

    maschera_freq1 = np.absolute(coef_freq_f) > filtro_freq1 #filtro in freq
    filtrato_freq1 = coef_f[:len(maschera_freq1)].copy()
    filtrato_freq1[maschera_freq1] = 0
    dati_inversa_freq1 = fft.irfft(filtrato_freq1, n=len(dati))

    maschera_freq2 = np.absolute(coef_freq_f) > filtro_freq2 #filtro in freq
    filtrato_freq2 = coef_f[:len(maschera_freq2)].copy()
    filtrato_freq2[maschera_freq2] = 0
    dati_inversa_freq2 = fft.irfft(filtrato_freq2, n=len(dati))

    #################################################################################
    #grafico temporale dati originali e filtrati e residui

    plt.subplot(2,1,1)
    plt.plot(tempo, dati,label='dati originali',alpha=0.5)
    plt.plot(tempo,dati_inversa_freq1,label='ricostruzione',color='red',alpha=0.8)
    plt.plot(tempo,dati_inversa_freq2,label='ricostruzione 2',alpha=0.8)
    plt.xlabel('data [yyyy-mm-dd]')
    plt.ylabel('concentrazione '+inquinante)
    plt.xticks(segni_x,rotation=30, ha='right')
    plt.legend(fontsize=12, loc = 'best', frameon=True)
    plt.grid()
    # residui
    plt.subplot(2,1,2)
    plt.plot(tempo,dati-dati_inversa_freq2,alpha=0.8)
    media = np.mean(np.diff(dati-dati_inversa_freq1))
    plt.axhline (media,color='red',linestyle=':',alpha=0.5,label='media 2={:.2f}'.format(media)) #filtro in frequenza E AMPIEZZA
    plt.xlabel('data [yyyy-mm-dd]')
    plt.ylabel('residui')
    plt.xticks(segni_x,rotation=30, ha='right')
    plt.legend(fontsize=12, loc = 'best', frameon=True)
    plt.grid()
    plt.tight_layout()
    plt.show()


####################################################################
# grafico temporale dati originali e filtrati
    # plt.plot(tempo, dati,label='dati originali',alpha=0.5)
    # plt.plot(tempo,dati_inversa_freq1,label='ricostruzione 1',color='red',alpha=0.8)
    # plt.plot(tempo,dati_inversa_freq2,label='ricostruzione 2',alpha=0.8)
    # plt.xlabel('data [yyyy-mm-dd]')
    # plt.ylabel('concentrazione '+inquinante)
    # plt.xticks(segni_x,rotation=30, ha='right')
    # plt.legend(fontsize=12, loc = 'best', frameon=True)
    # plt.grid()
    # plt.tight_layout()
    # plt.show()



