import pandas as pd
import numpy as np
from tqdm import tqdm
import rielaborazione_dati2 as rd

stazione1 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione1.txt', sep='\t')
stazione2 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione2.txt', sep='\t')
stazione3 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione3.txt', sep='\t')
stazione4 = pd.read_csv('/home/gb/Desktop/unipg//metodi_computazionali/repo_metodi_computazionali/e2/stazione4.txt', sep='\t')
# medie_california = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_california.txt', sep='\t')
# medie_colorado = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_colorado.txt', sep='\t')
# medie_new_york = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_new_york.txt', sep='\t')
# medie_south_dakota = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_south_dakota.txt', sep='\t')
# medie_texas = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie_texas.txt', sep='\t')
# medie = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/medie.txt', sep='\t')
# california = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/california.txt', sep='\t')
# colorado = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/colorado.txt', sep='\t')
# new_york = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/new_york.txt', sep='\t')
# south_dakota = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/south_dakota.txt', sep='\t')
# texas = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/repo_metodi_computazionali/e2/texas.txt', sep='\t')

