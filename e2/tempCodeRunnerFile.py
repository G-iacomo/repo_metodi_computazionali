dati_iniziali = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/progetto/pollution_us_2013_2015.csv')

stati = np.array([6,8,48,46,36]) # codici degli stati analizzati.
                        #rispettivamente California, Colorado, Texas, South Dakota, New York
stati_nome={'california','colorado','texas','south dakota','new york'}
check = False
dati = rd.funzione_stati2(dati_iniziali,stati,check)
print(dati.loc[:0])
# dati.to_csv('/hom