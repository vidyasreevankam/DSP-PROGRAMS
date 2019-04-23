import numpy as np
from matplotlib import pyplot as plt
n=input('enter n')
t=np.arange(0,10,0.1)
x1=np.sin(2*np.pi*t)
b=np.random.rand(x1.shape[0])
e=x1+b
c=len(x1)
z=np.zeros(len(e))
p=int(input('enter p value'))
for i in range(c):
	for k in range(int(p-1)):
		s=np.sum(e[i-k:i])
		#z[k-1]=e[k]+x1[99]
		#z[c-1]=x1[k]+x1[c-1]
		z[i]=s/p

plt.subplot(2,2,1)
plt.plot(x1)
plt.subplot(2,2,2)
plt.plot(b)
plt.subplot(2,2,3)
plt.plot(e)
plt.subplot(2,2,4)
plt.plot(z)
plt.show()
