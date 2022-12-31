import pandas as pd
pd.set_option('display.max_columns', 500)
dati_iniziali = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/progetto/pollution_us_2013_2015.csv')
n=int(input())
print(dati_iniziali[0:n])