x=input("")
h=input("")
import numpy as np
x1=len(x)
h1=len(h)
c1=max(x1,h1)
c=x1+h1-1
b=(2*c)-1
y=np.zeros(c)
for n in range(0,c):
	p=0
	for k in range(0,x1):
		if (n-k>=0 and n-k<h1):
			p=p+x[k]*h[n-k]
		y[n]=p
print(y)
s=[]
for i in range(c1,c):
	y2=+y[i]+y[i-4]
	s=np.append(s,y2)
h2=y[3]
s=np.append(s,h2)
print(s)

