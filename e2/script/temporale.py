import moduli_temporale as mt

##################################################################
#   parametri modificabili

#path=''    #modificare il path di lavoro in 'moduli_temporale.py
multi_grafici = True #true se si vogliono molteplici singoli grafici di maggiori dimensioni. esclusiamente per la parte di confronto temporale
esemplificativi = True #default=True. per visualizzare tutti i grafici realizzabili False.

def confronto_temporale(multi_grafici):
    print('\nconfronto temporale delle stazioni californiane selezionate, inquinante per inquinante:\n')
    mt.stazioni_temporale(multi_grafici) #confronto temporale stazioni inquinante per inquinante
    print('\nconfronto temporale degli stati selezionati, inquinante per inquinante:\n')
    mt.stati_temporale(multi_grafici)
    print('\nconfronto temporale degli stati selezionati:\nATTENZIONE: i dati sono stati moltiplicati a fini grafici; riferirsi alla legenda')
    mt.nazione_temporale()


confronto_temporale(multi_grafici)
mt.spettro_nazione()
mt.spettro_stati(esemplificativi)
mt.spettro_stazioni(esemplificativi)
