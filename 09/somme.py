import numpy as np

def somma_interi(n):
    return n*(n+1)/2

def somma_radici(n):
    a=np.arange(1,n+1)
    a=np.sqrt(a)
    return np.sum(a)
