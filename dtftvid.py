import numpy as np
import cmath
from matplotlib import pyplot as plt
j=cmath.sqrt(-1)
w=np.linspace(0,2*np.pi,1000)
x=[1.0/3,1.0/3,1.0/3,0]
p=[]
p=np.zeros(1000)
h=len(x)
g=[]
g=np.zeros(1000)
for i in range(0,1000):
	sum=0
	for n in range(0,h-1):
		sum=sum+(x[n]*(np.exp(-j*w[i]*n)))
	p[i]=sum
	p=np.append(p,sum)
print(g)
j1=(np.abs(p))
plt.subplot(2,1,1)
plt.plot(j1)
		
j2=(np.angle(p))
plt.subplot(2,1,2)
plt.plot(j2)
plt.show()
