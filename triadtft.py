import numpy as np
import cmath
from matplotlib import pyplot as plt
def dtft(x):
	j=cmath.sqrt(-1)
	y=[]
	l=len(x)
	y=np.zeros(10000)
	w=np.linspace(-np.pi,np.pi,10000)
	l=len(x)	
	for i in range(0,10000):
		sum=0
		for n in range(0,l):
			sum=sum+(x[n]*(np.exp(-j*w[i]*n)))
		y1=np.abs(sum)
		y=np.append(y,y1)
	return y
n=np.arange(0,31)
p=(31-1)/2.0
k=np.abs(n-p)
k1=k/(31-1)
k2=2*k1
w=1-k2
plt.subplot(5,1,1)
plt.stem(w)#triangularindow
m=np.arange(-17,17,1)
h=0.25*np.sinc(0.25*m)
plt.subplot(5,1,2)
plt.stem(m,h)#sinc
f1=dtft(h)#dtft sinc
plt.subplot(5,1,3)
plt.plot(f1)#dtftsinc
g=[]
for i in range(0,31):
	g1=(h[i]*w[i])
	g=np.append(g,g1)
print(g)
g3=dtft(g)
plt.subplot(5,1,4)
plt.plot(g3)#product of sinc and triangularwindow
g4=20*np.log(g3)
plt.subplot(5,1,5)
plt.plot(g4)
plt.show()
