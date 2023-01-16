import pandas as pd
import numpy as np
from scipy import fft
import matplotlib.pyplot  as plt
import datetime as dt

##################################################################
#   parametri modificabili

path = '' #indicare la cartella di lavoro
    #è possibile lasciare la stringa vuota



s1 = pd.read_csv(path+'/stazione1_riempita.txt', sep='\t')
s2 = pd.read_csv(path+'/stazione2_riempita.txt', sep='\t')
s3 = pd.read_csv(path+'/stazione3_riempita.txt', sep='\t')
s4 = pd.read_csv(path+'/stazione4_riempita.txt', sep='\t')
california = pd.read_csv(path+'/medie_california_riempita.txt', sep='\t')
colorado = pd.read_csv(path+'/medie_colorado_riempita.txt', sep='\t')
new_york = pd.read_csv(path+'/medie_new_york_riempita.txt', sep='\t')
south_dakota = pd.read_csv(path+'/medie_south_dakota_riempita.txt', sep='\t')
texas = pd.read_csv(path+'/medie_texas_riempita.txt', sep='\t')
nazione = pd.read_csv(path+'/medie_nazione_riempita.txt', sep='\t')


#################################################################################
#     confronti temporali

def stazioni_temporale(multi_grafici): #confronto stazioni inquinante per inquinante
    inquinanti = ['NO2 Mean','O3 Mean','SO2 Mean','CO Mean']
    etichette = [r'concentrazione NO2 [ppb]',r'concentrazione O3 [ppm]',r'concentrazione SO2 [ppb]',r'concentrazione CO [ppm]']
    date = s1['Date Local']
    segni_x=[]
    j = 0
    for i in range(len(s1)): #segna sull'asse x solo i primi dei mesi dispari
        if ((date[i][-1]=='1') and (date[i][-2]=='0')):
            if ((j%2)==0):
                segni_x = np.append(segni_x,date[i])
            j=j+1
    segni_x = np.append(segni_x,date.loc[len(date)-1]) #segna l'ultima data disponibile sull'asse x

    def stazioni(inquinante,etichetta):
        plt.plot(date,s1[inquinante], label='Los Angeles (LAC)',alpha=0.8)
        plt.plot(date,s2[inquinante], label='Not a city (HUM)', alpha=0.8)
        plt.plot(date,s3[inquinante], label='Calexico (IMP)', alpha=0.8)
        plt.plot(date,s4[inquinante], label='San Pablo (CC)', alpha=0.8)
        plt.xlabel('data [yyyy-mm-dd]')
        plt.ylabel(etichetta)
        #plt.yscale('log')
        plt.xticks(segni_x,rotation=30, ha='right')
        plt.legend(fontsize=12, loc = 'best', frameon=True)
        plt.grid()
        plt.tight_layout()

    if multi_grafici==False:
        for i in range(0,len(inquinanti)):
            if i<2:
                plt.subplot(2,2,i+1)
                stazioni(inquinanti[i],etichette[i])
            else:
                plt.subplot(2,2,i+1)
                stazioni(inquinanti[i],etichette[i])
    else:
        for i in range(0,len(inquinanti)):
            plt.figure(i+1)
            stazioni(inquinanti[i],etichette[i])
    plt.show()


def stati_temporale(multi_grafici): #confronto stato inquinante per inquinante
    inquinanti = ['NO2 Mean','O3 Mean','SO2 Mean','CO Mean']
    etichette = [r'concentrazione NO2 [ppb]',r'concentrazione O3 [ppm]',r'concentrazione SO2 [ppb]',r'concentrazione CO [ppm]']
    date = california['Date Local']
    segni_x=[]
    j = 0
    for i in range(len(s1)):
        if ((date[i][-1]=='1') and (date[i][-2]=='0')):
            if ((j%2)==0):
                segni_x = np.append(segni_x,date[i])
            j=j+1
    segni_x = np.append(segni_x,date.loc[len(date)-1])
    
    def stati(inquinante,etichetta):
        plt.plot(date,california[inquinante], label='California', alpha=0.8)
        plt.plot(date,colorado[inquinante], label='Colorado', alpha=0.8)
        plt.plot(date,new_york[inquinante], label='New_York', alpha=0.8)
        plt.plot(date,south_dakota[inquinante], label='South Dakota', alpha=0.8)
        plt.plot(date,texas[inquinante], label='Texas', alpha=0.8)
        plt.xlabel('data [yyyy-mm-dd]')
        plt.ylabel(etichetta)
        #plt.yscale('log')
        plt.xticks(segni_x,rotation=30, ha='right')
        plt.legend(fontsize=12, loc = 'best', frameon=True)
        plt.grid()
        plt.tight_layout()

    if multi_grafici==False:
        for i in range(0,len(inquinanti)):
            if i<2:
                plt.subplot(2,2,i+1)
                stati(inquinanti[i],etichette[i])
            else:
                plt.subplot(2,2,i+1)
                stati(inquinanti[i],etichette[i])
    else:
        for i in range(0,len(inquinanti)):
            plt.figure(i+1)
            stati(inquinanti[i],etichette[i])
    plt.show()

def nazione_temporale(): #confronto inquinanti con coefficienti moltiplicativi
    inquinanti = ['NO2 Mean','SO2 Mean','O3 Mean','CO Mean']
    etichette = [r'NO2 [ppb]',r'10$\cdot$SO2 [ppb]',r'1000$\cdot$O3 [ppm]',r'100$\cdot$CO [ppm]']
    moltiplicatori = [1,10,1000,100] # cambio scala per fini grafici. i dati modificati non sono conservati
    date = nazione['Date Local']
    segni_x=[]
    j = 0
    for i in range(len(nazione)):
        if ((date[i][-1]=='1') and (date[i][-2]=='0')):
            if ((j%2)==0):
                segni_x = np.append(segni_x,date[i])
            j=j+1
    segni_x = np.append(segni_x,date.loc[len(date)-1])
    
    for i in range(0,len(inquinanti)):
        plt.plot(date,(nazione[inquinanti[i]]*moltiplicatori[i]), label=etichette[i], alpha=0.8)
    plt.xlabel('data [yyyy-mm-dd]')
    plt.ylabel('concentrazioni')
    #plt.yscale('log')
    plt.xticks(segni_x,rotation=30, ha='right')
    plt.legend(fontsize=12, loc = 'best', frameon=True)
    plt.grid()
    plt.tight_layout()
    plt.show()


#############################################################################
#   calcolo Fourier: spettro di potenza

def fourier(dati,inquinante):
    nyquist = 0.5 
    coef_f = fft.rfft(dati[inquinante].to_numpy())
    indici =  np.arange(1,(coef_f.size//2)) #escludo il coef. 0 "divergente"
    coef_ps = np.absolute(coef_f[indici])**2
    coef_freq_f = nyquist*fft.rfftfreq(coef_f.size, d=1)
    freq_plot = coef_freq_f[indici] 
    return freq_plot,coef_ps 




################################################################################
# spettro potenza inquinanti nazione

def spettro_nazione():
    print('\nconfronto dello spettro di potenza dei vari inquinanti a livello nazionale:\n')
    inquinanti = ['NO2 Mean','O3 Mean','SO2 Mean','CO Mean']
    etichette = [r'NO2 [$ppb^2$]',r'O3 [$ppb^2$]',r'SO2 [$ppm^2$]',r'CO [$ppm^2$]']
    for i in range(len(inquinanti)):
        freq_plot,spettro_pot = fourier(nazione,inquinanti[i])
        plt.plot(freq_plot,spettro_pot, label=etichette[i])
        indice_cmax = np.argmax(spettro_pot) #trova il massimo
        plt.plot(freq_plot[indice_cmax],spettro_pot[indice_cmax],'.',label='massimo')
        print('\n\n'+etichette[i]+'\nMassimo {:f}\nFreq {:f}\nPeriodo aprox. int. '.format( spettro_pot[indice_cmax], freq_plot[indice_cmax])+'{:d}'.format(int(1/freq_plot[indice_cmax]))  ) 
    plt.xlabel(r'frequenza [$d^{-1}$]')
    plt.ylabel('spettro potenza USA')
    plt.xscale('log')
    plt.yscale('log') 
    plt.axvline(1/365, color='red',linestyle=':',alpha=0.8,label=r'frequenza $1/365$') #linee frequenza esclusivamente grafiche
    plt.axvline(2/365, color='orange',linestyle=':',alpha=0.8,label=r'frequenza $2/365$')
    #plt.axvline(1/7, color='yellow',alpha=0.8,label=r'frequenza $1/7$')
    plt.legend(fontsize=12, loc='lower right', frameon=True)
    plt.grid()
    plt.tight_layout()
    plt.xlim(0.001,0.16)
    plt.show()


#############################################################################
# spettro potenza inquinanti stati

def spettro_stati(esemplificativi):
    print('\nconfronto dello spettro di potenza dei vari inquinanti a livello statale:\n')
    if esemplificativi==False: 
        stati=[california,colorado,new_york,south_dakota,texas]
        nome_stati = ['california','colorado','new_york','south_dakota','texas']
    else:
        stati=[california]
        nome_stati = ['california']
    inquinanti = ['NO2 Mean','O3 Mean','SO2 Mean','CO Mean']
    etichette = [r'NO2 [$ppb^2$]',r'O3 [$ppb^2$]',r'SO2 [$ppm^2$]',r'CO [$ppm^2$]']
    for j in range(len(stati)):
        print('\n\n'+nome_stati[j])
        plt.figure(j+1)
        for i in range(len(inquinanti)):
            freq_plot,spettro_pot = fourier(nazione,inquinanti[i])
            plt.plot(freq_plot,spettro_pot, label=etichette[i])
            indice_cmax = np.argmax(spettro_pot) 
            plt.plot(freq_plot[indice_cmax],spettro_pot[indice_cmax],'.',label='massimo')
            print('\n\n'+etichette[i]+'\nMassimo {:f}\nFreq {:f}\nPeriodo aprox. int. '.format( spettro_pot[indice_cmax], freq_plot[indice_cmax])+'{:d}'.format(int(1/freq_plot[indice_cmax]))  ) 
        plt.xlabel(r'frequenza [$d^{-1}$]')
        plt.ylabel('spettro potenza '+nome_stati[j])
        plt.xscale('log') 
        plt.yscale('log') 
        plt.axvline(1/365, color='red',linestyle=':',alpha=0.8,label=r'frequenza $1/365$')
        plt.axvline(2/365, color='orange',linestyle=':',alpha=0.8,label=r'frequenza $2/365$')
        #plt.axvline(1/7, color='yellow',alpha=0.8,label=r'frequenza $1/7$')
        plt.legend(fontsize=12, loc='lower right', frameon=True)
        plt.grid()
        plt.tight_layout()
        plt.xlim(0.001,0.16)
    plt.show()



################################################################
# spettro potenza inquinanti stazioni

def spettro_stazioni(esemplificativi):
    print('\nconfronto dello spettro di potenza dei vari inquinanti rilevati in quattro stazioni della California:\n')
    if esemplificativi==False:
        stati=[s1,s2,s3,s4]
        nome_città=['Los Angeles (LAC)','Not a city (HUM)','Calexico (IMP)','San Pablo (CC)']
    else:
        stati=[s1]
        nome_città=['Los Angeles (LAC)']
    inquinanti = ['NO2 Mean','O3 Mean','SO2 Mean','CO Mean']
    etichette = [r'NO2 [$ppb^2$]',r'O3 [$ppb^2$]',r'SO2 [$ppm^2$]',r'CO [$ppm^2$]']
    for j in range(len(stati)):
        print('\n\n'+nome_città[j])
        plt.figure(j+1)
        for i in range(len(inquinanti)):
            freq_plot,spettro_pot = fourier(nazione,inquinanti[i])
            plt.plot(freq_plot,spettro_pot, label=etichette[i])
            indice_cmax = np.argmax(spettro_pot) 
            plt.plot(freq_plot[indice_cmax],spettro_pot[indice_cmax],'.',label='massimo')
            print('\n\n'+etichette[i]+'\nMassimo {:f}\nFreq {:f}\nPeriodo aprox. int. '.format( spettro_pot[indice_cmax], freq_plot[indice_cmax])+'{:d}'.format(int(1/freq_plot[indice_cmax]))  ) 
        plt.xlabel(r'frequenza [$d^{-1}$]')
        plt.ylabel('spettro potenza '+nome_città[j])
        plt.xscale('log') 
        plt.yscale('log') 
        plt.axvline(1/365, color='red',linestyle=':',alpha=0.8,label=r'frequenza $1/365$')
        plt.axvline(2/365, color='orange',linestyle=':',alpha=0.8,label=r'frequenza $2/365$')
        #plt.axvline(1/7, color='yellow',alpha=0.8,label=r'frequenza $1/7$')
        plt.legend(fontsize=12, loc='lower right', frameon=True)
        plt.grid()
        plt.tight_layout()
        plt.xlim(0.001,0.16)
    plt.show()



