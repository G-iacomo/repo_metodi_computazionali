import moduli_analisi as ma

def confronto_temporale(multi_grafici):
    print('\nconfronto temporale delle stazioni californiane selezionate, inquinante per inquinante:\n')
    ma.stazioni_temporale(multi_grafici)
    print('\nconfronto temporale degli stati selezionati, inquinante per inquinante:\n')
    ma.stati_temporale(multi_grafici)
    print('\nconfronto temporale degli stati selezionati:\nATTENZIONE: i dati sono stati moltiplicati a fini grafici; riferirsi alla legenda')
    ma.nazione_temporale()


multi_grafici = False #true se si vogliono molteplici singoli grafici di maggiori dimensioni.
esemplificativi = True #default=True. per visualizzare tutti i grafici realizzabili False.

confronto_temporale(multi_grafici)
ma.spettro_nazione()
ma.spettro_stati(esemplificativi)
ma.spettro_stazioni(esemplificativi)
