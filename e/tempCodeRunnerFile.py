stato_stazioni=6
california=rd.selezione_stato(dati,stato_stazioni)
print(california.at[7766,'Site Num'])
california.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/california_temporaneo.txt', sep='\t', na_rep='', index=False)
for i in tqdm(range(0,len(california))):
#for i in tqdm(range(0,4)):
    i=california.at[i,'Site Num']
    stazioni=rd.selezione_stazione(california,i)
stazioni.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/stazioni_temporaneo.txt', sep='\t', na_rep='', index=False)