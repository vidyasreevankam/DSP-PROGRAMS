import numpy as np
from matplotlib import pyplot as plt
m=input('enter m value')
w=np.ones(m)#rectangular
plt.stem(w)
n=np.arange(0,(m-1))
p=(m-1)/2.0
k=np.abs(n-p)
k1=k/(m-1)
k2=2*k1
k3=1-k2
plt.stem(k3)#triangular
m1=0.5*np.cos((2*np.pi*n)/(m-1))
m2=0.5-m1
plt.stem(m2)#hanning
k5=0.46*np.cos((2*np.pi*n)/(m-1))
k6=0.54-k5
plt.stem(k6)#hamming
x1=-0.5*np.cos(2*np.pi*n/(m-1))
x2=0.08*np.cos(4*np.pi*n/(m-1))
w=0.42+x1+x2
plt.stem(n,w)
plt.show()
