grafico iniziale: dati e funzione con parametri iniziali
plt.errorbar(df['E'],df['f'],df['ferr'])
xx=np.linspace(0,10,100)
plt.plot(xx,flusso(xx,p))
plt.grid()
plt.show()