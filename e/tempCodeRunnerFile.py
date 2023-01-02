dati=e.funzione_stati()
dati=e.funzione_medie2(dati)
print(dati)

dati.to_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e/medie_temporanee.txt', sep='\t', na_rep='!!', index=False)
