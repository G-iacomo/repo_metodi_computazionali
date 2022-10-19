import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/gb/Desktop/unipg/metodi_computazionali/eserciziL02a1.csv')
print(df.columns)
g=df['giorno']
t=df['temperatura']
dt=df['err. t']
p=df['pioggia']
plt.plot(g, t, '.', color='limegreen')
plt.plot(g, p, '.',  color='red')
plt.xlabel('giorno')
plt.ylabel('t')

plt.show()
