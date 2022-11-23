import numpy as np
import matplotlib.pyplot as plt
import sys
'''
def cumulativa(theta):
    y=(1-np.cos(theta/2))/2
    return y
'''
n=100
s=1
def inversa(yy):
    xx=2*np.arccos(1-2*yy)
    return xx
#yy=np.random.random(10000)
#plt.hist(inversa(yy),bins=100,range=(0,10))
#plt.show()
def random(yy):
    x=np.zeros(1)
    y=np.zeros(1)
    x=np.sum(s*np.cos(inversa(yy)))
    y=np.sum(s*np.sin(inversa(yy)))
    return x,y
x=np.zeros(n)
y=np.zeros(n)
for i in range(n):
    yy=np.random.random(100)
    x[i],y[i]=random(yy)
plt.plot(x,y,'o')
plt.show()
