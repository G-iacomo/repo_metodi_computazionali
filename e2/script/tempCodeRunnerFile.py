print('\n\nnazione')
filtro_freq=np.array([7.5e-3,7e-3,10e-3,7e-3]) 
if filtrare_ampiezza==True:
    filtro_amp=np.array([1e5,0.15,1e3,40]) 
else:
    filtro_amp=np.array([np.nan,np.nan,np.nan,np.nan])
for i in range(len(inquinanti)):
    mc.inversa(nazione,inquinanti[i],filtro_freq[i],filtro_amp[i])