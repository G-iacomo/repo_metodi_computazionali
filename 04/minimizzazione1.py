import scipy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('/home/gb980061/repo_metodi_computazionali/04/fit_data.csv')
plt.plot(df['x'],df['y'], color= 'green', label='conteggi')
plt.xscale('log')
plt.xlabel('X')
plt.ylabel('conteggi')
plt.grid()
plt.minorticks_on()
plt.legend(fontsize = 12, loc = "upper left")
plt.tight_layout()
plt.show()
